"""Per-candidate detail JSON for a calibration benchmark run.

Re-runs the same fits as `benchmark.run` (same rng stream, so `distractors` draws the same
candidates) and stores, per case and scenario, every candidate with its truth/fitted amount plus
the largest flows of the target. Usage:

    uv run python scripts/dump_calibration_detail.py [-n N] [--seed S] [--project P] [-o OUT]
                                                     [--top-flows K] [--scenarios a,b,c]

Defaults reproduce results/benchmark/flow-n100-seed7-detail.json (the four panels of the deck's
benchmark slide and artifacts/calibration-benchmark.html); the no-list panel comes from
``--scenarios blind-all -o results/benchmark/blind-all-n100-seed7-detail.json``. The file grows roughly linearly
with N (~45 kB per case at --top-flows 40); lower --top-flows if it gets unwieldy.
"""

import argparse, json, random, time, warnings
from collections import Counter
from pathlib import Path
import numpy as np
import bw2data as bd
warnings.filterwarnings("ignore")

from reverse_bafu import db, benchmark
from reverse_bafu.benchmark import Bench, pick_cases
from reverse_bafu.lci import System, determined_flows, flow_agreement, contribution_breadth

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("-n", "--n", type=int, default=100, help="number of synthetic cases (default 100)")
ap.add_argument("--seed", type=int, default=7, help="same seed as the benchmark run (default 7)")
ap.add_argument("--project", default="bafu-2026", help="Brightway project (default bafu-2026)")
ap.add_argument("--scenarios", default="oracle,bounded,partial,distractors",
                help="comma-separated; must match the benchmark run so the rng stream lines up")
ap.add_argument("--top-flows", type=int, default=40, help="largest target flows stored per scenario (default 40)")
ap.add_argument("-o", "--out", default=None,
                help="output path (default results/benchmark/flow-n<N>-seed<SEED>-detail.json)")
args = ap.parse_args()

N, SEED = args.n, args.seed
SCEN = [s.strip() for s in args.scenarios.split(",") if s.strip()]
TOP_FLOWS = args.top_flows
OUT = Path(args.out or f"results/benchmark/flow-n{N}-seed{SEED}-detail.json")
db.set_project(args.project)

rng = random.Random(SEED)                      # same stream as benchmark.run
cases = pick_cases(N, SEED)
acts = bd.Database(db.INVENTORY_DB).load()
ids = {k: bd.get_node(database=k[0], code=k[1]).id for k in acts}
used = Counter()
for key, act in acts.items():
    for e in act.get("exchanges", []):
        if e.get("type") == "technosphere" and tuple(e["input"]) != key:
            used[tuple(e["input"])] += 1
sys_ = System(bd.get_node(database=db.INVENTORY_DB, code=cases[0]["code"]))
bench = Bench(sys_, ids, used)
print(f"{len(cases)} cases, blind pool = {len(bench.blind_pool)} processes", flush=True)

meta = {}
def info(key):
    if key not in meta:
        n = bd.get_node(database=key[0], code=key[1])
        meta[key] = {"name": n["name"], "location": n.get("location", ""), "unit": n.get("unit", ""), "code": key[1]}
    return meta[key]

out = []
for case in cases:
    truth = case["inputs"]
    target = bench.sys.cumulative([bench.ids[(db.INVENTORY_DB, case["code"])]])[:, 0]
    det = determined_flows(bench.sys, bench.ids[(db.INVENTORY_DB, case["code"])])
    rec = {"code": case["code"], "name": case["name"], "category": case["category"],
           "location": case["location"], "unit": bd.get_node(database=db.INVENTORY_DB, code=case["code"]).get("unit", ""),
           "n_true_inputs": len(truth), "n_target_flows": int((target != 0).sum()),
           "original": {
               "inputs": sorted([{**info(k), "amount": v} for k, v in truth.items()], key=lambda r: -abs(r["amount"])),
               "biosphere": sorted([{**info(k), "amount": v,
                                     "categories": [str(c) for c in (bd.get_node(database=k[0], code=k[1]).get("categories") or [])][:2]}
                                    for k, v in case["direct"].items()], key=lambda r: -abs(r["amount"]))},
           "scenarios": {}}

    for sc in SCEN:
        direct = np.zeros(bench.sys.n_flows) if sc.startswith("blind") else bench.direct_vector(case["direct"])
        keys = list(truth)
        if sc in ("oracle", "bounded"):
            cand = keys
        elif sc == "partial":
            contrib = {k: contribution_breadth(target, bench.col(bench.ids[k]) * truth[k], mask=det) for k in keys}
            cand = sorted(keys, key=lambda k: -contrib[k])[: max(1, round(0.7 * len(keys)))]
        elif sc == "distractors":  # consumes rng exactly as benchmark.run does
            pool = [k for k in bench.blind_pool if k not in truth and k != (db.INVENTORY_DB, case["code"])]
            cand = keys + rng.sample(pool, min(10, len(pool)))
        elif sc == "blind":  # every process used >= 30 times, no direct flows
            cand = [k for k in bench.blind_pool if k != (db.INVENTORY_DB, case["code"])]
        else:  # blind-all: every dataset in the database, no direct flows
            cand = [k for k in bench.all_pool if k != (db.INVENTORY_DB, case["code"])]
        n = len(cand)
        lo, hi = np.zeros(n), np.full(n, np.inf)
        if sc == "bounded":
            a = np.array([truth[k] for k in cand], dtype=float)   # same ordering/widening as Bench.run_case
            lo, hi = np.minimum(0.5 * a, 2.0 * a), np.maximum(0.5 * a, 2.0 * a)
            hi = np.where(hi > lo, hi, lo + 1e-12)
        t0 = time.time()
        x, M = bench.fit(target, cand, lo, hi, direct, det)
        secs = time.time() - t0
        model = M @ x + direct
        ag = flow_agreement(target, model, det)

        cols = {k: M[:, i] for i, k in enumerate(cand)}
        mat = lambda col, amt: contribution_breadth(target, col * amt, mask=det) > 0   # determined flows only, as Bench.run_case
        true_material = {k for k in truth if mat(cols[k] if k in cols else bench.col(bench.ids[k]), truth[k])}
        chosen = {k for i, k in enumerate(cand) if mat(cols[k], x[i])}

        rows = []
        for i, k in enumerate(cand):
            t = truth.get(k)
            if sc.startswith("blind") and t is None and x[i] <= 0:
                continue   # most blind candidates end at zero (~600 of 675, ~11,900 of 11,946); storing them adds only size
            rows.append({**info(k),
                         "role": "true input" if k in truth else ("distractor" if sc == "distractors" else "candidate"),
                         "truth": t, "fitted": float(x[i]),
                         "ratio": (float(x[i]) / t) if t else None,
                         "lo": float(lo[i]) if sc == "bounded" else None,
                         "hi": float(hi[i]) if sc == "bounded" else None,
                         "material_true": k in true_material, "material_fitted": k in chosen})
        for k in truth:                                   # true inputs never offered (partial)
            if k not in cols:
                rows.append({**info(k), "role": "withheld", "truth": truth[k], "fitted": None, "ratio": None,
                             "lo": None, "hi": None, "material_true": k in true_material, "material_fitted": False})
        rows.sort(key=lambda r: -(abs(r["truth"]) if r["truth"] else 0))

        ratios = [x[i] / truth[k] for i, k in enumerate(cand) if k in true_material and truth[k]]
        nz = np.where(target != 0)[0]
        top = sorted(nz, key=lambda r: -abs(target[r]))[:TOP_FLOWS]
        frows = []
        for r in top:
            fn = bench.sys.flow_node(int(r))
            cats = fn.get("categories") or ()
            frows.append({"name": fn["name"], "unit": fn.get("unit", ""),
                          "compartment": " / ".join(str(c) for c in cats[:2]),
                          "target": float(target[r]), "model": float(model[r]),
                          "delta": float(model[r] / target[r] - 1) if target[r] else None})

        rec["scenarios"][sc] = {
            "n_candidates": n, "n_chosen": len(chosen), "n_material_true": len(true_material),
            "true_positives": len(chosen & true_material),
            "false_positives": len(chosen - set(truth)), "false_negatives": len(true_material - chosen),
            "amounts_within_20pct": sum(1 for r in ratios if 0.8 <= r <= 1.2), "amounts_scored": len(ratios),
            "amount_ratio_median": None if not ratios else float(np.median(ratios)),
            "flows_within_10pct": ag["within_10pct"], "flows_within_20pct": ag["within_20pct"],
            "n_target_flows": ag["n_target"], "n_scored_flows": ag["n_scored"], "flows_missing": ag["n_missing"], "flows_extra": ag["n_extra"],
            "median_abs_delta": None if np.isnan(ag["median_abs_delta"]) else float(ag["median_abs_delta"]),
            "seconds": round(secs, 3), "candidates": rows, "top_flows": frows}
    out.append(rec)
    print("done", case["name"][:45], flush=True)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, ensure_ascii=False))
print(f"-> {OUT} ({OUT.stat().st_size:,} bytes)")
