"""Score the LLM extraction route against a real answer key.

    uv run python scripts/transcription_vs_truth.py [--project bafu-2026]

``specs/c80b8e9e-epoxy-resin-liquid-at-plant.draft.json`` is a transcription of Tab. 31.2 of
``2007 - LCI chemicals - Althaus.pdf`` produced by the locate -> extract -> map route. BAFU-2026
contains the dataset that table describes - ``Epoxy resin, liquid, disaggregated data, at plant``
[RER] - so for once the route's output can be compared with the thing it was reading, instead of
with a cumulative vector.

Result on BAFU-2026: 9 of 9 technosphere amounts exact (2 of them mapped to a near-synonym
dataset), 34 elementary flows matched by (name, compartment) and all 34 within 1 %; everything else
is the same substance in a different sub-compartment, which is ``db.resolve_flow`` matching on the
top-level compartment only.
"""
from __future__ import annotations

import argparse
import warnings

warnings.filterwarnings("ignore")

import bw2data as bd  # noqa: E402

from reverse_bafu import db  # noqa: E402

TRUTH_PREFIX = "6ac7f2be"                                   # Epoxy resin, liquid, disaggregated data, at plant
MODEL_CODE = "c80b8e9e-8a0d-36f6-a4a2-1509d03e42c2-draft-disagg"


def techno(a):
    d: dict[str, float] = {}
    for e in a.technosphere():
        d[e.input["name"]] = d.get(e.input["name"], 0.0) + e.amount
    return d


def bio(a):
    d: dict[tuple, float] = {}
    for e in a.biosphere():
        k = (e.input["name"], tuple(str(c) for c in (e.input.get("categories") or ())))
        d[k] = d.get(k, 0.0) + e.amount
    return d


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default="bafu-2026")
    a = ap.parse_args()
    db.set_project(a.project)
    inv, sand = bd.Database(db.INVENTORY_DB), bd.Database(db.SANDBOX_DB)
    truth = next(x for x in inv if x["code"].startswith(TRUTH_PREFIX))
    model = sand.get(MODEL_CODE)

    t, m = techno(truth), techno(model)
    print(f"=== technosphere: {truth['name']}  vs  the drafted transcription")
    for k in sorted(set(t) | set(m)):
        x, y = t.get(k, 0.0), m.get(k, 0.0)
        d = "" if x == 0 else f"{(y - x) / x:+.1%}"
        flag = "  <-- differs" if x == 0 or y == 0 else ""
        print(f"  {x:12.6g} | {y:12.6g} | {d:>9s} | {k[:58]}{flag}")

    tb, mb = bio(truth), bio(model)
    both = set(tb) & set(mb)
    close = [k for k in both if tb[k] and abs(mb[k] - tb[k]) <= 0.01 * abs(tb[k])]
    print(f"\n=== elementary flows: answer key {len(tb)}, drafted {len(mb)}")
    print(f"  matched by (name, compartment): {len(both)};  of those within 1 %: {len(close)}")
    worst = sorted(((abs(mb[k] - tb[k]) / abs(tb[k]), k, tb[k], mb[k]) for k in both if tb[k]), reverse=True)
    print("  worst matched deviations:")
    for r, k, x, y in worst[:5]:
        print(f"    {r:+.2%}  {k[0][:40]:40s} {x:.4g} -> {y:.4g}")
    print(f"  only in the answer key: {len(set(tb) - both)};  only in the drafted node: {len(set(mb) - both)}"
          "  (same substances, different sub-compartment)")


if __name__ == "__main__":
    main()
