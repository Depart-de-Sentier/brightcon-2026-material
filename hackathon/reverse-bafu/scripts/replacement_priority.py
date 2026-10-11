"""Rank the aggregated system processes by how much of BAFU's impact passes through them.

    uv run python scripts/replacement_priority.py [--project bafu-2026]

The question is which system processes are worth replacing first.
A system process matters in proportion to how much of the rest of the database depends on it, so
the score is:

    importance_c(s) = sum over every other BAFU dataset a of  clip( x_s(a) * h_c(s) / h_c(a), 0, 1 )

x_s(a) is the amount of s that one unit of a requires anywhere in its supply chain (row s of
A^-1), h_c the cumulative impact per unit in category c. Each term is the share of a's impact
that passes through s, so the sum is in "dataset-equivalents": 12 means the system process carries
twelve datasets' worth of impact. Unlike a count of consumers, a dataset that is 90 % driven by
s weighs 900 times one where s contributes 0.1 %.

The ranking score is the mean over the 16 headline EF 3.1 categories (sub-indicators left out),
so climate is not weighted against toxicity; climate change is also reported on its own.
Every dataset counts once - how often a dataset is used in real studies is not known here.

Next to the score, a recommendation from what we already know about each system process:
  rebuilt, fossil CO2 of the explicit rebuild within +-25 % of the original  -> review and adopt
  rebuilt, further off                                                     -> expert revision
  not rebuilt, its report is in the bundle but prints no usable inventory  -> expert, with report
  not rebuilt, no report                                                   -> expert, no report
(results/usable_information.csv: for all 87 not rebuilt we found too little for the algorithm.)
plus how many of our rebuilds terminate on it (the dependency the rebuild could not open).

Writes results/replacement_priority.csv and results/replacement_priority.md.
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import re
import warnings
from pathlib import Path

import numpy as np

warnings.filterwarnings("ignore")

import bw2calc as bc  # noqa: E402
import bw2data as bd  # noqa: E402
import scipy.sparse.linalg as spl  # noqa: E402

from reverse_bafu import db  # noqa: E402

CATEGORIES = [
    "Climate change", "Acidification", "EF-particulate Matter", "Ecotoxicity, freshwater",
    "Eutrophication marine", "Eutrophication, freshwater", "Eutrophication, terrestrial",
    "Human toxicity, cancer", "Human toxicity, non-cancer", "Ionising radiation, human health",
    "Land use", "Ozone depletion", "Photochemical ozone formation - human health",
    "Resource use, fossils", "Resource use, minerals and metals", "Water use",
]
METHOD = ("sentier", "EF v3.1")


def recommendation(rebuilt: dict | None, evidence: str) -> str:
    if rebuilt:
        o, m = rebuilt["co2"]
        return "rebuilt: review and adopt" if o and abs(m / o - 1) <= 0.25 else "rebuilt: expert revision"
    return "expert, no report" if evidence == "no-pdf" else "expert, with report"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default="bafu-2026")
    ap.add_argument("--share", type=float, default=0.10, help="threshold for 'datasets it drives' (default 10 %%)")
    a = ap.parse_args()
    db.set_project(a.project)

    sysp = list(csv.DictReader(open("results/system_terminated_extended.csv")))
    evidence = {r["code"]: r["status"] for r in csv.DictReader(open("results/drafting_status.csv"))}
    fc = json.load(open("results/flow_comparison.json"))
    rebuilt = {s["code"]: {"route": s["strategy"], "co2": s["headline"]["co2"]} for s in fc["specs"] if s["counted"]}
    agg = {r["code"] for r in sysp}
    blocks = collections.Counter()
    for s in fc["specs"]:
        if s["counted"]:
            spec = json.loads(Path(s["spec"]).read_text())
            for i in spec["node"]["inputs"]:
                if i.get("code") in agg and i["code"] not in rebuilt and i["code"] != s["code"]:
                    blocks[i["code"]] += 1

    nodes = {r["code"]: bd.get_node(database=db.INVENTORY_DB, code=r["code"]) for r in sysp}
    lca = bc.LCA({next(iter(nodes.values())).id: 1}, method=METHOD + (CATEGORIES[0],))
    lca.lci()
    lca.lcia()
    A = lca.technosphere_matrix.tocsc()
    B = lca.biosphere_matrix.tocsr()
    lu = spl.splu(A)
    n = A.shape[0]
    col = {r["code"]: lca.dicts.activity[nodes[r["code"]].id] for r in sysp}
    rev = {v: k for k, v in lca.dicts.activity.items()}
    names = {}

    E = np.zeros((n, len(sysp)))
    for j, r in enumerate(sysp):
        E[col[r["code"]], j] = 1.0
    Y = lu.solve(E, trans="T")                       # Y[a, j] = amount of s_j per unit of a
    Ar = A.tocsr()

    imp = np.zeros((len(CATEGORIES), len(sysp)))
    drives = np.zeros(len(sysp), dtype=int)
    top = [[] for _ in sysp]
    for c, cat in enumerate(CATEGORIES):
        lca.switch_method(METHOD + (cat,))
        q = lca.characterization_matrix.diagonal()
        h = lu.solve(np.asarray(B.T @ q).ravel(), trans="T")   # cumulative impact per unit of every dataset
        valid = h > 1e-12 * np.abs(h).max()                    # below that, h is solve round-off
        for j, r in enumerate(sysp):
            sc = col[r["code"]]
            share = np.zeros(n)
            share[valid] = Y[valid, j] * h[sc] / h[valid]
            share[sc] = 0.0
            share = np.clip(share, 0.0, 1.0)
            imp[c, j] = share.sum()
            if cat == "Climate change":
                drives[j] = int((share >= a.share).sum())
                for k in np.argsort(-share)[:3]:
                    if share[k] >= 0.01:
                        aid = rev[k]
                        if aid not in names:
                            names[aid] = bd.get_node(id=aid)["name"]
                        top[j].append(f"{names[aid]} ({share[k]:.0%})")
        print(f"  {cat:45s} done", flush=True)

    rows = []
    for j, r in enumerate(sysp):
        code = r["code"]
        row_s = Ar.getrow(col[code])
        consumers = int(sum(1 for k in row_s.indices if k != col[code]))
        rb = rebuilt.get(code)
        ev = evidence.get(code, "")
        rows.append({
            "code": code, "name": r["name"], "location": r["location"], "detected_by": r["detected_by"],
            "importance": round(float(imp[:, j].mean()), 3),
            "importance_median": round(float(np.median(imp[:, j])), 3),
            "dominant_category": CATEGORIES[int(np.argmax(imp[:, j]))],
            "dominant_share": round(float(imp[:, j].max() / max(imp[:, j].sum(), 1e-12)), 2),
            "breadth": int((imp[:, j] >= 1.0).sum()),
            "importance_climate": round(float(imp[0, j]), 3),
            "datasets_driven_climate": int(drives[j]),
            "direct_consumers": consumers,
            "blocks_our_rebuilds": blocks.get(code, 0),
            "evidence": ev,
            "rebuilt_route": rb["route"] if rb else "",
            "rebuilt_co2_ratio": round(rb["co2"][1] / rb["co2"][0], 2) if rb and rb["co2"][0] else "",
            "recommendation": recommendation(rb, ev),
            "top_climate_dependants": "; ".join(top[j]),
            **{"imp_" + re.sub(r"[^a-z0-9]+", "_", c.lower()).strip("_"): round(float(imp[i, j]), 3)
               for i, c in enumerate(CATEGORIES)},
        })
    for key, rk in (("importance_median", "rank_median"), ("importance_climate", "rank_climate")):
        for i, x in enumerate(sorted(rows, key=lambda x: -x[key]), 1):
            x[rk] = i
    rows.sort(key=lambda x: -x["importance"])
    for i, x in enumerate(rows, 1):
        x["rank"] = i
    top15 = {x["code"] for x in rows[:15]}
    for rk in ("rank_median", "rank_climate"):
        kept = sum(1 for x in rows if x[rk] <= 15 and x["code"] in top15)
        print(f"  top-15 by mean that are also top-15 by {rk[5:]}: {kept} of 15")
    out = Path("results/replacement_priority.csv")
    fields = ["rank"] + [k for k in rows[0] if k != "rank"]
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    rec = collections.Counter(x["recommendation"] for x in rows)
    md = ["# Which system processes to open first", "",
          f"{len(rows)} system processes, ranked by the share of BAFU's impact that passes through them "
          "(dataset-equivalents, mean over the 16 EF 3.1 categories). See the docstring of "
          "`scripts/replacement_priority.py` for the definition.", "",
          "Recommendations: " + ", ".join(f"{k} {v}" for k, v in rec.most_common()), "",
          "| # | system process | importance (mean) | climate | median | dominant category | breadth | blocks rebuilds | evidence | recommendation |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for x in rows[:40]:
        md.append(f"| {x['rank']} | {x['name']} [{x['location']}] | {x['importance']:.1f} | {x['importance_climate']:.1f} | "
                  f"{x['importance_median']:.1f} | {x['dominant_category']} ({x['dominant_share']:.0%}) | {x['breadth']}/16 | "
                  f"{x['blocks_our_rebuilds']} | {x['evidence']} | {x['recommendation']} |")
    Path("results/replacement_priority.md").write_text("\n".join(md) + "\n")
    print(f"-> {out}, results/replacement_priority.md")
    for x in rows[:15]:
        print(f"{x['rank']:3d} {x['importance']:7.1f} clim {x['importance_climate']:6.1f} (#{x['rank_climate']:<3}) med {x['importance_median']:5.1f} (#{x['rank_median']:<3}) "
              f"breadth {x['breadth']:2d}  {x['name'][:44]:46s} {x['recommendation']}")


if __name__ == "__main__":
    main()
