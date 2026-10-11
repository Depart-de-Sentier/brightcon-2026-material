"""Original vs rebuilt elementary flows for every rebuilt dataset, for the flow-parity page.

    uv run python scripts/flow_comparison.py [--project bafu-2026]

Writes results/flow_comparison.json with, per spec:
  * the headline emissions (fossil CO2, fossil CH4, N2O, SO2, NOx, PM2.5, NMVOC, fossil CO), each
    summed over every compartment it appears in - a single row of "Carbon Dioxide (fossil)" can
    mislead, because the original and the rebuild may book the same kilogram in different air
    sub-compartments (burnt shale's NOx is the example: -95 % row by row, +-0 % summed)
  * every elementary flow, original vs rebuilt, for the parity plot

"Rebuilt" is the explicit unit process (<prefix>-disagg), NOT the hybrid node: the hybrid carries
the residual block and equals the original by construction, so comparing it would show nothing.
Both sides are cumulative inventories (B A^-1 e) in today's BAFU-2026 background. Flows that the
sparse solve only produces as round-off (lci.determined_flows) are dropped from the parity data.

All rebuilt nodes and their originals go into one demand, so the technosphere matrix is
factorised once instead of once per spec.
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import warnings
from pathlib import Path

import numpy as np

warnings.filterwarnings("ignore")

import bw2calc as bc  # noqa: E402
import bw2data as bd  # noqa: E402
import scipy.sparse.linalg as spl  # noqa: E402

from reverse_bafu import db  # noqa: E402
from reverse_bafu import spec as spec_mod  # noqa: E402
from reverse_bafu.lci import System, determined_flows  # noqa: E402

HEADLINE = [  # (key, label, lower-cased flow names summed over all their compartments)
    ("co2", "Fossil CO₂", {"carbon dioxide (fossil)"}),
    ("ch4", "Fossil CH₄", {"methane (fossil)"}),
    ("n2o", "N₂O", {"nitrous oxide"}),
    ("so2", "SO₂", {"sulfur dioxide"}),
    ("nox", "NOₓ", {"nitrogen oxides"}),
    ("pm25", "PM2.5", {"particles (pm2.5)", "particles (pm0.2 - pm2.5)", "particles (pm0.2)"}),
    ("nmvoc", "NMVOC", {"non-methane volatile organic compounds"}),
    ("co", "Fossil CO", {"carbon monoxide (fossil)"}),
]

class MultiSystem(System):
    """System over a demand of many nodes - one factorisation for all of them."""

    def __init__(self, nodes):  # noqa: D107 - same fields as System
        self.lca = bc.LCA({n.id: 1 for n in nodes})
        self.lca.lci()
        self.A = self.lca.technosphere_matrix.tocsc()
        self.B = self.lca.biosphere_matrix.tocsr()
        self.lu = spl.splu(self.A)
        self.n_flows = self.B.shape[0]
        self._groups = None


def sig(x: float) -> float:
    return float(f"{x:.4g}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default="bafu-2026")
    ap.add_argument("-o", "--out", default="results/flow_comparison.json")
    a = ap.parse_args()
    db.set_project(a.project)

    ext = {r["code"]: r for r in csv.DictReader(open("results/system_terminated_extended.csv"))}
    specs = []
    for path in sorted(glob.glob("specs/*.json")):
        sp = spec_mod.load(path)
        prefix = spec_mod.node_prefix(sp)
        t = bd.get_node(database=db.INVENTORY_DB, code=sp.target_code)
        e = bd.get_node(database=db.SANDBOX_DB, code=f"{prefix}-disagg")
        specs.append((path, sp, t, e))

    # the variant each dataset is counted with: the hand-written spec, else a draft; never a
    # "-chained" variant when the plain spec exists (the same rule as the per-dataset counts)
    rank = {"": 0, "draft": 1, "chained": 2}
    counted = {}
    for path, sp, t, e in specs:
        r = rank.get(sp.variant or "", 3)
        if sp.target_code not in counted or r < counted[sp.target_code][0]:
            counted[sp.target_code] = (r, path)

    sys_ = MultiSystem([n for _, _, t, e in specs for n in (t, e)])
    inv = sys_.cumulative([n.id for _, _, t, e in specs for n in (t, e)])

    flows, rows_by_name = [], {}
    for row in range(sys_.n_flows):
        node = sys_.flow_node(row)
        cats = node.get("categories") or ()
        flows.append([node["name"], " / ".join(str(c) for c in cats[:2]), node.get("unit", "")])
        rows_by_name.setdefault(node["name"].lower(), []).append(row)

    out = []
    for j, (path, sp, t, e) in enumerate(specs):
        bt, be = inv[:, 2 * j], inv[:, 2 * j + 1]
        keep = determined_flows(sys_, t.id) & determined_flows(sys_, e.id) & ((bt != 0) | (be != 0))
        head = {}
        for key, _label, names in HEADLINE:
            rows = [r for n in names for r in rows_by_name.get(n, [])]
            head[key] = [sig(bt[rows].sum()), sig(be[rows].sum())]
        code = sp.target_code
        current = sp.raw.get("strategy", {}).get("code", "?")
        out.append({
            "spec": path, "code": code, "name": t["name"], "location": t.get("location", ""),
            "unit": t.get("unit", ""), "variant": sp.variant or "",
            "counted": counted[code][1] == path,
            "strategy": current,
            "detected_by": ext.get(code, {}).get("detected_by", ""),
            "headline": head,
            "flows": [[int(r), sig(bt[r]), sig(be[r])] for r in np.where(keep)[0]],
        })
        print(f"{t['name'][:48]:50s} {sp.variant or '-':8s} {int(keep.sum()):5d} flows"
              f"  CO2 {head['co2'][0]:.3g} -> {head['co2'][1]:.3g}")

    doc = {"headline": [{"key": k, "label": lbl} for k, lbl, _ in HEADLINE],
           "flows": flows, "specs": out}
    Path(a.out).write_text(json.dumps(doc, ensure_ascii=False, separators=(",", ":")))
    n_counted = sum(s["counted"] for s in out)
    print(f"-> {a.out}  ({Path(a.out).stat().st_size / 1e6:.1f} MB, {len(out)} specs, {n_counted} counted datasets)")


if __name__ == "__main__":
    main()
