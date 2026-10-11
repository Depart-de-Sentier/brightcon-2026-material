"""Re-derive every claim behind lci.determined_flows, from scratch.

Backs README §6, "What the flow score counts". Nothing here is imported by the pipeline; it
exists so a reviewer can check the argument instead of trusting it.

    uv run python scripts/verify_determined_flows.py [--project bafu-2026]

Prints, in order:
  1. why some flows are not determined  - the range of the scaling vector vs the solve's error floor
  2. the separation                     - how far kept and excluded flows move under refinement
  3. the rejected alternative           - what a magnitude cutoff does to trace pollutants
  4. does exclusion hide real errors    - inject a known error, see where it shows up
"""

from __future__ import annotations

import argparse
import re
import warnings
from collections import Counter, defaultdict

import numpy as np

warnings.filterwarnings("ignore")

import bw2data as bd  # noqa: E402

from reverse_bafu import db  # noqa: E402
from reverse_bafu.benchmark import Bench, pick_cases  # noqa: E402
from reverse_bafu.lci import System, determined_flows  # noqa: E402

TRACE = re.compile(r"dioxin|benzo|mercury|hexachloro|arsenic|cadmium", re.I)


def build(project: str, n: int = 10, seed: int = 7):
    db.set_project(project)
    cases = pick_cases(n, seed)
    acts = bd.Database(db.INVENTORY_DB).load()
    ids = {k: bd.get_node(database=k[0], code=k[1]).id for k in acts}
    used: Counter = Counter()
    for key, a in acts.items():
        for e in a.get("exchanges", []):
            if e.get("type") == "technosphere" and tuple(e["input"]) != key:
                used[tuple(e["input"])] += 1
    bench = Bench(System(bd.get_node(database=db.INVENTORY_DB, code=cases[0]["code"])), ids, used)
    return cases, acts, bench


def truth(acts, case):
    """Ground truth with duplicate exchanges SUMMED (see Finding 1 in the handover)."""
    a = acts[(db.INVENTORY_DB, case["code"])]
    ti: dict = defaultdict(float)
    di: dict = defaultdict(float)
    for e in a.get("exchanges", []):
        k = tuple(e["input"])
        if e.get("type") == "technosphere" and k != (db.INVENTORY_DB, case["code"]):
            ti[k] += e["amount"]
        elif e.get("type") == "biosphere":
            di[k] += e["amount"]
    return dict(ti), dict(di)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--project", default="bafu-2026")
    args = p.parse_args()
    cases, acts, bench = build(args.project)
    sys_ = bench.sys
    case = next(c for c in cases if c["name"].startswith("Ceramic"))
    aid = bench.ids[(db.INVENTORY_DB, case["code"])]

    # ---- 1. why some flows are not determined -----------------------------------------------
    D = np.zeros(sys_.A.shape[1])
    D[sys_.lca.dicts.activity[aid]] = 1.0
    s = sys_.lu.solve(D)
    eps = np.finfo(float).eps
    floor = eps * np.abs(s).max()
    nzs = s != 0
    print(f"\n1. THE SCALING VECTOR  ({case['name']})")
    print(f"   largest |s| {np.abs(s).max():.3e}   smallest non-zero {np.abs(s[nzs]).min():.3e}"
          f"   spread {np.abs(s).max() / np.abs(s[nzs]).min():.1e}")
    print(f"   solve error floor = eps * max|s| = {floor:.3e}")
    print(f"   entries of s below that floor: {int((np.abs(s) < floor).sum() - (~nzs).sum())} of {int(nzs.sum())}")

    # ---- 2. the separation under refinement -------------------------------------------------
    s2 = s + sys_.lu.solve(D - sys_.A @ s)
    t1, t2 = sys_.B @ s, sys_.B @ s2
    with np.errstate(divide="ignore", invalid="ignore"):
        move = np.where(np.abs(t1) > 0, np.abs(t2 - t1) / np.maximum(np.abs(t1), 1e-300), 0.0)
    ok = determined_flows(sys_, aid)
    nz = t1 != 0
    print("\n2. ONE STEP OF ITERATIVE REFINEMENT")
    print(f"   kept     {int((nz & ok).sum()):5d} flows, median move {np.median(move[nz & ok]):.2e}")
    print(f"   excluded {int((nz & ~ok).sum()):5d} flows, median move {np.median(move[nz & ~ok]):.2e}")

    # ---- 3. the rejected alternative: a magnitude cutoff -------------------------------------
    cut = np.zeros(t1.shape, bool)
    for rows in sys_.groups.values():
        r = np.array(rows)
        m = np.abs(t1[r]).max()
        if m > 0:
            cut[r] = np.abs(t1[r]) >= 1e3 * eps * m
    tox = [r for r in np.where(nz)[0] if TRACE.search(sys_.flow_node(int(r))["name"])]
    print("\n3. REJECTED ALTERNATIVE - cutoff at 1000*eps of each (unit, compartment) group max")
    print(f"   named trace pollutants: {len(tox)} present, "
          f"{sum(1 for r in tox if not cut[r])} DROPPED by the magnitude cutoff, "
          f"{sum(1 for r in tox if not ok[r])} dropped by refinement")
    noise = [r for r in np.where(nz)[0] if abs(t1[r]) < 1e-24]
    print(f"   flows below 1e-24 (pure noise): {len(noise)} present, "
          f"{sum(1 for r in noise if cut[r])} KEPT by the magnitude cutoff, "
          f"{sum(1 for r in noise if ok[r])} kept by refinement")

    # ---- 4. can exclusion hide a real error? -------------------------------------------------
    print("\n4. INJECT A KNOWN ERROR INTO A PERFECT MODEL")
    print(f"   {'case / injected':46s} {'score':>7s} {'recoverable in excluded set':>30s}")
    for c in cases[:5]:
        ti, di = truth(acts, c)
        a_id = bench.ids[(db.INVENTORY_DB, c["code"])]
        Dc = np.zeros(sys_.A.shape[1]); Dc[sys_.lca.dicts.activity[a_id]] = 1.0
        sc_ = sys_.lu.solve(Dc)
        wobble = np.abs(sys_.B @ (sc_ + sys_.lu.solve(Dc - sys_.A @ sc_)) - sys_.B @ sc_)
        t = sys_.B @ sc_
        okc = determined_flows(sys_, a_id)
        direct = bench.direct_vector(di)
        keys = list(ti)
        M = np.column_stack([bench.col(bench.ids[k]) for k in keys])
        x0 = np.array([ti[k] for k in keys])
        biggest = int(np.argmax(np.abs(M @ np.diag(x0)).sum(axis=0)))
        m0 = M @ x0 + direct
        for label, fac in (("biggest input x2", 2.0), ("biggest input x1.1", 1.1)):
            x = x0.copy(); x[biggest] *= fac
            m = M @ x + direct
            nzc = t != 0; scored = nzc & okc
            with np.errstate(divide="ignore", invalid="ignore"):
                score = (np.abs(m[scored] / t[scored] - 1) <= 0.10).mean()
            effect = np.abs(m - m0)
            rec = nzc & ~okc & (effect > wobble) & (effect > 0)
            rel = (effect[rec] / np.abs(t).max()).max() if rec.any() else 0.0
            print(f"   {(c['name'][:24] + ' | ' + label):46s} {score:6.1%} "
                  f"{int(rec.sum()):5d} flows, largest {rel:.1e} x biggest flow")
    print("\n   (a x1.1 error leaving the score at 100 % is the +-10 % threshold, not the exclusion:")
    print("    an error that moves flows by <=10 % cannot trip a '>10 %' test.)\n")


if __name__ == "__main__":
    main()
