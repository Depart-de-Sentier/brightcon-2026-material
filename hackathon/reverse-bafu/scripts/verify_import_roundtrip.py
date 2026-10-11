#!/usr/bin/env python
"""End-to-end check of the export/import pair: does an arbitrary project really get usable datasets?

    uv run python scripts/verify_import_roundtrip.py [--source bafu-2026] [--scratch import-test]

It (1) proves the importer refuses a project without BAFU-2026, (2) copies the source project to a
scratch project and removes the build sandbox so nothing of the rebuild is already there,
(3) dry-runs, (4) imports, (5) counts what landed and looks for dangling references, and (6) runs
an LCA on every imported dataset and compares its cumulative inventory, flow by flow, with the
original aggregated BAFU dataset.

Step 6 is the one that matters: the hybrid nodes must come out equal to the originals (to numerical
noise) and the explicit nodes must not, because they are deliberately incomplete.

Beware: it deletes and recreates the scratch project. Do not point --scratch at anything you keep.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import bw2data as bd
import bw2calc as bc

sys.path.insert(0, str(Path(__file__).parent))
import import_disaggregated as imp  # noqa: E402

EXPORT = Path("exports/disaggregated_bafu2026.json")
TARGET_DB = "bafu-2026-disaggregated"
BIOSPHERE = ["ef-3.1-biosphere", "bafu-2026-residual"]


def cumulative(act) -> dict[int, float]:
    """The activity's cumulative inventory, keyed by biosphere flow id (NOT by matrix row: the row
    order differs between LCA objects, so comparing raw vectors silently compares different flows)."""
    lca = bc.LCA({act: 1})
    lca.lci()
    b = np.array(lca.inventory.sum(axis=1)).ravel()
    rev = {row: flow_id for flow_id, row in lca.dicts.biosphere.items()}
    return {rev[i]: v for i, v in enumerate(b) if v != 0.0}


def rel_dev(model: dict[int, float], target: dict[int, float]) -> float:
    keys = set(model) | set(target)
    num = sum(abs(model.get(k, 0.0) - target.get(k, 0.0)) for k in keys)
    den = sum(abs(target.get(k, 0.0)) for k in keys)
    return num / den if den else float("nan")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", default="bafu-2026", help="project to copy for the test")
    ap.add_argument("--scratch", default="import-test", help="scratch project (DELETED and recreated)")
    ap.add_argument("--file", type=Path, default=EXPORT)
    a = ap.parse_args()
    empty = a.scratch + "-empty"

    print("=" * 74)
    print("STEP 1  refuse to import into a project that has no BAFU-2026")
    print("=" * 74)
    if empty in bd.projects:
        bd.projects.delete_project(empty, delete_dir=True)
    bd.projects.set_current(empty)
    bd.projects.set_current("default")
    try:
        imp.run(empty, a.file, TARGET_DB, "bafu-2026", ["ef-3.1-biosphere"], "both", True, False)
        print("!! FAIL: the importer should have refused")
        return 1
    except SystemExit as exc:
        print("OK   refused with:", exc)

    print(f"\n{'=' * 74}\nSTEP 2  scratch project {a.scratch!r}, copied from {a.source!r}\n{'=' * 74}")
    if a.scratch in bd.projects:
        bd.projects.delete_project(a.scratch, delete_dir=True)
    bd.projects.set_current(a.source)
    bd.projects.copy_project(a.scratch, switch=True)
    if "reverse-bafu-sandbox" in bd.databases:
        del bd.databases["reverse-bafu-sandbox"]     # so nothing of the rebuild is already present
    print("databases:", sorted(bd.databases))

    print(f"\n{'=' * 74}\nSTEP 3  dry run\n{'=' * 74}")
    imp.run(a.scratch, a.file, TARGET_DB, "bafu-2026", BIOSPHERE, "both", True, False)

    print(f"\n{'=' * 74}\nSTEP 4  import\n{'=' * 74}")
    imp.run(a.scratch, a.file, TARGET_DB, "bafu-2026", BIOSPHERE, "both", False, True)

    print(f"\n{'=' * 74}\nSTEP 5  what landed\n{'=' * 74}")
    bd.projects.set_current(a.scratch)
    newdb = bd.Database(TARGET_DB)
    n_tech = n_bio = n_res = n_to_bafu = 0
    dangling = []
    for act in newdb:
        for ex in act.exchanges():
            if ex["type"] == "technosphere":
                n_tech += 1
            elif ex["type"] == "biosphere":
                n_bio += 1
                n_res += "residual" in (ex.get("comment") or "")
            try:
                if ex.input["database"] == "bafu-2026":
                    n_to_bafu += 1
            except Exception as exc:
                dangling.append((act["code"], str(exc)))
    print(f"nodes: {len(newdb)}")
    print(f"technosphere exchanges: {n_tech} (of which {n_to_bafu} link into bafu-2026)")
    print(f"biosphere exchanges: {n_bio} (of which residual: {n_res})")
    print(f"dangling references: {len(dangling)}")
    for d in dangling[:5]:
        print("  ", d)

    print(f"\n{'=' * 74}\nSTEP 6  LCA per imported dataset, cumulative inventory vs the original\n{'=' * 74}")
    payload = json.loads(a.file.read_text())
    print(f"{'dataset':46s} {'flows':>6} {'hybrid rel.dev':>15} {'explicit rel.dev':>17}")
    worst_h, best_e, worst_e, n = 0.0, 1e9, 0.0, 0
    for d in payload["datasets"]:
        if not d.get("residual"):
            continue
        orig = cumulative(bd.get_node(database="bafu-2026", code=d["bafu_code"]))
        hyb = cumulative(bd.get_node(database=TARGET_DB, code=d["residual"]["node_code"]))
        expl = cumulative(bd.get_node(database=TARGET_DB, code=d["main_node_code"]))
        dh, de = rel_dev(hyb, orig), rel_dev(expl, orig)
        worst_h, best_e, worst_e, n = max(worst_h, dh), min(best_e, de), max(worst_e, de), n + 1
        print(f"{d['bafu_name'][:46]:46s} {len(orig):6d} {dh:15.3e} {de:17.3e}")
    print(f"\n{n} datasets checked")
    print(f"worst hybrid deviation:   {worst_h:.3e}   (should be numerical noise)")
    print(f"explicit deviation range: {best_e:.1%} to {worst_e:.1%}   (should NOT be small)")
    ok = worst_h < 1e-5 and not dangling
    print("\nRESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
