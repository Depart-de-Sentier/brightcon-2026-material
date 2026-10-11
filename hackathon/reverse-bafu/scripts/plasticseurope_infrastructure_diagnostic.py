"""Where the 1790 flows of a PlasticsEurope dataset actually come from.

Each of the 14 PlasticsEurope datasets of BAFU-2026 declares 361-542 elementary flows of its own -
the eco-profile - and its cumulative inventory has 1790. The extra ~1350 are not upstream chemistry:
they are the background of the single ``4.0E-10 units of Chemical plant, organics`` that ESU added
when implementing the data ("For all datasets, the inventory regarding infrastructure contributions
was checked and supplemented. ... the standard amount for production of chemicals of 4.0E-10 p",
Rajabihamedani et al. 2025, sec. 3.6).

That one exchange dominates three quarters of the vector, which has a direct consequence for any
rebuild: ESU added one chemical plant per *dataset*, i.e. one per cradle-to-gate chain, so a
rebuilt unit process that links to a precursor which already carries one and then adds its own
doubles ~1300 of the 1790 flows. On HDPE that alone moved the harness from 4 % to 76 % of flows
within +-10 %. It is why every spec in this family carries the infrastructure as a free input
bounded by [0, 4.0E-10] instead of fixing it at the report's number.

    uv run python scripts/plasticseurope_infrastructure_diagnostic.py [--project bafu-2026]
"""
from __future__ import annotations

import argparse
import csv

import numpy as np
import bw2data as bd

from reverse_bafu import db
from reverse_bafu.lci import System

CHEM_PLANT = "13ed4fe0-7ba5-3b60-82b6-a63918ee814d"   # Chemical plant, organics [RER]
STANDARD_AMOUNT = 4.0e-10                              # Rajabihamedani 2025, sec. 3.6


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default="bafu-2026")
    a = ap.parse_args()
    db.set_project(a.project)
    rows = [r for r in csv.DictReader(open(db.SYSTEM_TERMINATED_CSV)) if r["family"] == "plasticseurope"]
    rows.sort(key=lambda r: -int(r["n_used_by"]))
    nodes = [bd.get_node(database=db.INVENTORY_DB, code=r["code"]) for r in rows]
    plant = bd.get_node(database=db.INVENTORY_DB, code=CHEM_PLANT)

    sys_ = System(nodes[0])
    inv = sys_.cumulative([n.id for n in nodes] + [plant.id])
    b_plant = inv[:, -1] * STANDARD_AMOUNT

    print(f"{'dataset':<58} {'own':>5} {'cum':>5} {'>50%':>6} {'>90%':>6} {'>90% share':>11}")
    for i, (r, n) in enumerate(zip(rows, nodes)):
        b = inv[:, i]
        own = sum(1 for e in n.exchanges() if e["type"] == "biosphere")
        nz = np.where(b != 0)[0]
        share = np.abs(b_plant[nz]) / np.abs(b[nz])
        print(f"{n['name'][:58]:<58} {own:5d} {len(nz):5d} {int((share > 0.5).sum()):6d} "
              f"{int((share > 0.9).sum()):6d} {(share > 0.9).mean():10.0%}")
    print("\nown   = elementary flows the BAFU dataset declares itself (the PlasticsEurope eco-profile)")
    print("cum   = non-zero flows of its cumulative inventory")
    print(">50 % / >90 % = flows for which 4.0E-10 units of 'Chemical plant, organics' alone already")
    print("        account for that share of the target's amount")
    n_in = {n["name"]: sum(1 for e in n.exchanges() if e["type"] == "technosphere") for n in nodes}
    print(f"\nPET bottle grade is the clean control: its only technosphere exchange is the chemical plant "
          f"({n_in['Polyethylene terephthalate, granulate, bottle grade, at plant']} input), and it still has "
          f"{int((inv[:, [n['name'] for n in nodes].index('Polyethylene terephthalate, granulate, bottle grade, at plant')] != 0).sum())} "
          f"cumulative flows against the 393 it declares.")


if __name__ == "__main__":
    main()
