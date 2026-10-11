"""Agreement restricted to the flows an eco-profile itself declares.

    uv run python scripts/ecoprofile_agreement.py [--project bafu-2026]

Why this exists
---------------
The 37 datasets `scripts/find_system_processes.py` finds by structure are APME /
PlasticsEurope era eco-profiles. Two facts make the usual headline number - the share
of *all* the target's flows a rebuild reproduces within +-10 % - close to meaningless
for them.

1. **The denominator is not the eco-profile.** These datasets are not pure system
   processes: they carry explicit waste-treatment exchanges (disposal of coal-mining
   spoil, incineration residue, hazardous waste ...). Those chains, not the eco-profile,
   contribute most of the ~1770 flows the harness compares. The eco-profile itself
   declares only 83-146 substances - the list the industry survey collected.
2. **A rebuilt unit process cannot help producing ~1670 flows**, because it runs through
   the full ecoinvent background. Flows the target never reported cannot agree, so they
   are counted as failures no model can avoid.

This script reports, per rebuilt dataset of that family:

  n_declared       flows the eco-profile itself declares (the target's own biosphere column)
  n_cumulative     non-zero flows of the target's cumulative inventory
  declared_share   n_declared / n_cumulative - how much of the comparison is the eco-profile
  within10_declared  of the declared flows, how many the rebuilt node reproduces within +-10 %
  kg_mass_declared_pct  same restricted to kilogram mass

It also reports, for every dataset of the family whether rebuilt or not, how much of the
cumulative vector comes from the declared waste-treatment services alone - i.e. the part
of the harness's denominator that any model omitting them gives up by construction.

Nothing here feeds the pipeline; it is a diagnostic, written for the report.
"""
from __future__ import annotations

import argparse
import csv
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

import numpy as np  # noqa: E402
import bw2data as bd  # noqa: E402

from reverse_bafu import db, lci  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default="bafu-2026")
    ap.add_argument("--datasets", default="results/system_terminated_extended.csv")
    ap.add_argument("--out", default="results/ecoprofile_agreement.csv")
    a = ap.parse_args()
    db.set_project(a.project)
    inv = bd.Database(db.INVENTORY_DB)
    sand = bd.Database(db.SANDBOX_DB)
    have = {n["code"]: n for n in sand}
    rows = [r for r in csv.DictReader(open(a.datasets)) if r["detected_by"] == "structure"]

    # Build the matrices from a SANDBOX node, not from a BAFU one: the demand activity decides which
    # databases the technosphere matrix spans, and the rebuilt nodes live in the sandbox.
    seed = next((n for n in sand if n["code"].endswith("-disagg")), None)
    if seed is None:
        raise SystemExit("no rebuilt node in the sandbox; run `reverse-bafu run-all` first")
    sys_ = lci.System(seed)
    out = []
    for r in rows:
        target = inv.get(r["code"])
        tvec = sys_.cumulative([target.id])[:, 0]
        n_cum = int((tvec != 0).sum())
        declared_rows, declared_amt = [], {}
        for e in target.biosphere():
            row = sys_.flow_row(e.input["database"], e.input["code"])
            if row is None:
                continue
            declared_amt[row] = declared_amt.get(row, 0.0) + e.amount
        declared_rows = [r_ for r_, v in declared_amt.items() if v]
        # share of the cumulative vector that the declared waste services bring in
        waste_ids = [e.input.id for e in target.technosphere()]
        waste_rows = 0
        if waste_ids:
            wvec = np.zeros_like(tvec)
            cols = sys_.cumulative(waste_ids)
            for j, e in enumerate(target.technosphere()):
                wvec += cols[:, j] * e.amount
            waste_rows = int(((wvec != 0) & (np.abs(wvec) > 0.5 * np.abs(tvec))).sum())
        base = {"code": r["code"], "name": r["name"], "n_declared": len(declared_rows),
                "n_cumulative": n_cum,
                "declared_share_pct": round(100 * len(declared_rows) / n_cum, 1) if n_cum else "",
                "flows_mostly_from_waste_services": waste_rows,
                "waste_share_pct": round(100 * waste_rows / n_cum, 1) if n_cum else ""}
        wrote = False
        for suffix, label in (("-disagg", "main"), ("-draft-disagg", "draft")):
            if r["code"] + suffix not in have:
                continue
            mvec = sys_.cumulative([have[r["code"] + suffix].id])[:, 0]
            hits = sum(1 for row in declared_rows
                       if abs(mvec[row] - declared_amt[row]) <= 0.10 * abs(declared_amt[row]))
            kg_rows = [row for row in declared_rows if sys_.flow_node(row).get("unit") == "kilogram"]
            kg_tot = sum(abs(declared_amt[row]) for row in kg_rows)
            kg_ok = sum(abs(declared_amt[row]) for row in kg_rows
                        if abs(mvec[row] - declared_amt[row]) <= 0.10 * abs(declared_amt[row]))
            out.append({**base, "variant": label, "within10_declared": hits,
                        "within10_declared_pct": round(100 * hits / len(declared_rows), 1) if declared_rows else "",
                        "kg_mass_declared_pct": round(100 * kg_ok / kg_tot, 1) if kg_tot else ""})
            print(f"{r['name'][:46]:46s} {label:5s} declared {len(declared_rows):4d} of {n_cum:5d} cumulative"
                  f" ({base['declared_share_pct']:>5} %)  ->  {hits:3d} within 10 %"
                  f" ({out[-1]['within10_declared_pct']:>5} %), kg mass {out[-1]['kg_mass_declared_pct']:>5} %")
            wrote = True
        if not wrote:
            out.append({**base, "variant": "", "within10_declared": "", "within10_declared_pct": "",
                        "kg_mass_declared_pct": ""})
            print(f"{r['name'][:46]:46s} {'-':5s} declared {len(declared_rows):4d} of {n_cum:5d} cumulative"
                  f" ({base['declared_share_pct']:>5} %)  ->  not rebuilt")
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    with open(a.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader(); w.writerows(out)
    print(f"\n{len(out)} rows -> {a.out}")


if __name__ == "__main__":
    main()
