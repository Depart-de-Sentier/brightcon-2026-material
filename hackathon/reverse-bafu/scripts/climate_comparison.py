"""EF 3.1 Climate change of every rebuilt dataset against its original, for the results slide.

    uv run python scripts/climate_comparison.py [--project bafu-2026]

The fit and the flow comparison stay impact-free; this is an evaluation only. Same nodes and the
same counting rule as flow_comparison.py: the original (aggregated) dataset against the explicit
rebuild (<prefix>-disagg), not the hybrid node, which equals the original by construction. All nodes
go into one demand, so the technosphere matrix is factorised once.

Writes results/climate_comparison.csv (one row per spec) and prints the median deviation per route
and how many counted datasets are within +-10 % and +-25 %.
"""

from __future__ import annotations

import argparse
import csv
import glob
import warnings

import numpy as np

warnings.filterwarnings("ignore")

import bw2calc as bc  # noqa: E402
import bw2data as bd  # noqa: E402

from flow_comparison import MultiSystem  # noqa: E402
from reverse_bafu import db  # noqa: E402
from reverse_bafu import spec as spec_mod  # noqa: E402

METHOD = ("sentier", "EF v3.1", "Climate change")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default="bafu-2026")
    ap.add_argument("-o", "--out", default="results/climate_comparison.csv")
    a = ap.parse_args()
    db.set_project(a.project)

    specs = []
    for path in sorted(glob.glob("specs/*.json")):
        sp = spec_mod.load(path)
        t = bd.get_node(database=db.INVENTORY_DB, code=sp.target_code)
        e = bd.get_node(database=db.SANDBOX_DB, code=f"{spec_mod.node_prefix(sp)}-disagg")
        specs.append((path, sp, t, e))
    rank = {"": 0, "draft": 1, "chained": 2}
    counted = {}
    for path, sp, t, e in specs:
        r = rank.get(sp.variant or "", 3)
        if sp.target_code not in counted or r < counted[sp.target_code][0]:
            counted[sp.target_code] = (r, path)

    nodes = [n for _, _, t, e in specs for n in (t, e)]
    sys_ = MultiSystem(nodes)
    inv = sys_.cumulative([n.id for n in nodes])
    # characterisation factors on the same biosphere rows as the inventories
    lca = bc.LCA({n.id: 1 for n in nodes}, method=METHOD)   # the same demand, so the same biosphere rows
    lca.lci(); lca.lcia()
    cf = np.zeros(sys_.n_flows)
    diag = lca.characterization_matrix.diagonal()
    for flow_id, row in lca.dicts.biosphere.items():
        r2 = sys_.lca.dicts.biosphere.get(flow_id)
        if r2 is not None:
            cf[r2] = diag[row]
    scores = cf @ inv

    rows = []
    for j, (path, sp, t, e) in enumerate(specs):
        o, m = float(scores[2 * j]), float(scores[2 * j + 1])
        code = sp.target_code
        rows.append({"spec": path, "code": code, "name": t["name"], "variant": sp.variant or "",
                     "counted": counted[code][1] == path, "route": sp.raw.get("strategy", {}).get("code", "?"),
                     "original_kg_co2eq": f"{o:.5g}", "rebuilt_kg_co2eq": f"{m:.5g}",
                     "deviation_pct": f"{100 * (m / o - 1):.1f}" if o else ""})
    with open(a.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

    c = [r for r in rows if r["counted"] and r["deviation_pct"] != ""]
    dev = np.array([float(r["deviation_pct"]) for r in c])
    print(f"{len(c)} counted datasets, EF 3.1 Climate change: within ±10 % {int((np.abs(dev) <= 10).sum())}, "
          f"within ±25 % {int((np.abs(dev) <= 25).sum())}, median {np.median(dev):+.0f} %")
    for route in sorted({r["route"] for r in c}):
        d = np.array([float(r["deviation_pct"]) for r in c if r["route"] == route])
        print(f"  {route}: n={len(d):2d}  median {np.median(d):+.0f} %  within ±10 % {int((np.abs(d) <= 10).sum())}")
    print(f"-> {a.out}")


if __name__ == "__main__":
    main()
