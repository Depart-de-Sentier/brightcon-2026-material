"""Benchmark the reconstruction on synthetic system processes with known ground truth.

Every BAFU unit process can be turned into a system-process lookalike: its cumulative
inventory B·A⁻¹·e is exactly what an ecoSpold type=2 export of it would contain. The real
inputs are then the ground truth, and the pipeline's calibration step can be scored on how
much of the structure and the amounts it recovers under different evidence levels:

    oracle       the true input list is known, amounts are not (fixed-list NNLS)
    bounded      list known, amounts known to a factor of 2 (report ranges)
    partial      30 % of the inputs are missing from the list (a report that omits minor lines)
    distractors  list known plus 10 plausible wrong candidates (an LLM over-proposing inputs)
    blind        no list: every process used >= 30 times is a candidate (~675)
    blind-all    no list: every dataset in the database is a candidate (~12,000)

Direct elementary flows of the process are given in every scenario except the two blind ones.
Output: results/benchmark/<name>.csv (one row per case and scenario) and <name>.md (summary).
"""

from __future__ import annotations

import csv
import random
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import scipy.optimize as so
import bw2data as bd

from . import db
from .lci import WIDE, System, contribution_breadth, determined_flows, flow_agreement, nnls_working_set, solve_weighted

SCENARIOS = ("oracle", "bounded", "partial", "distractors", "blind", "blind-all")


def pick_cases(n: int, seed: int, min_inputs: int = 3, max_inputs: int = 30) -> list[dict]:
    """Stratified sample of unit processes: round-robin over BAFU top-level categories."""
    rng = random.Random(seed)
    by_cat: dict[str, list[dict]] = defaultdict(list)
    agg = db.aggregated_codes()
    for key, act in bd.Database(db.INVENTORY_DB).load().items():
        if key[1] in agg or act["name"].lower().startswith("xx"):
            continue
        ex = act.get("exchanges", [])
        techno = [e for e in ex if e.get("type") == "technosphere" and tuple(e["input"]) != key]
        bio = [e for e in ex if e.get("type") == "biosphere"]
        if not (min_inputs <= len(techno) <= max_inputs):
            continue
        m = re.search(r"BAFU category: (.+?) /", act.get("comment", ""))
        # sum duplicates: a process may list the same input (or the same elementary flow) on several
        # exchanges - two aluminium profile lines, two land-occupation lines that map to one EF flow.
        # A dict comprehension keeps only the last one and silently loses the rest of the amount.
        inputs_: dict[tuple, float] = defaultdict(float)
        direct_: dict[tuple, float] = defaultdict(float)
        for e in techno:
            inputs_[tuple(e["input"])] += e["amount"]
        for e in bio:
            direct_[tuple(e["input"])] += e["amount"]
        by_cat[m.group(1) if m else "?"].append(
            {"code": key[1], "name": act["name"], "location": act.get("location", ""), "category": m.group(1) if m else "?",
             "inputs": dict(inputs_), "direct": dict(direct_)})
    cats = sorted(by_cat)
    for c in cats:
        by_cat[c].sort(key=lambda x: x["code"])  # database load order is not guaranteed; sort before shuffling
        rng.shuffle(by_cat[c])
    cases: list[dict] = []
    while len(cases) < n and any(by_cat.values()):
        for c in cats:
            if by_cat[c] and len(cases) < n:
                cases.append(by_cat[c].pop())
    return cases


class Bench:
    def __init__(self, sys_: System, ids: dict[tuple, int], used: Counter):
        self.sys = sys_
        self.ids = ids
        self.used = used
        self._col: dict[int, np.ndarray] = {}
        self._det: dict[str, np.ndarray] = {}
        # sorted: the pool is built from a Counter over Database.load(), whose order is not
        # guaranteed. Unsorted, rng.sample draws a different distractor set on every run and the
        # `distractors` scenario stops being reproducible (as pick_cases already guards against).
        self.blind_pool = sorted(k for k, n in used.items() if n >= 30)
        # every dataset of the database that the factorised system holds (~12,000)
        self.all_pool = sorted(k for k, i in ids.items() if i in sys_.lca.dicts.activity)

    def determined(self, code: str) -> np.ndarray:
        if code not in self._det:
            self._det[code] = determined_flows(self.sys, self.ids[(db.INVENTORY_DB, code)])
        return self._det[code]

    def col(self, act_id: int) -> np.ndarray:
        if act_id not in self._col:
            self._col[act_id] = self.sys.cumulative([act_id])[:, 0]
        return self._col[act_id]

    def prefetch(self, act_ids: list[int], batch: int = 500) -> None:
        """Compute missing cumulative columns in batches: one solve per column is slow for ~12,000."""
        todo = [i for i in dict.fromkeys(act_ids) if i not in self._col]
        for a in range(0, len(todo), batch):
            chunk = todo[a:a + batch]
            C = self.sys.cumulative(chunk)
            for j, i in enumerate(chunk):
                self._col[i] = C[:, j]

    def direct_vector(self, direct: dict) -> np.ndarray:
        v = np.zeros(self.sys.n_flows)
        for key, amt in direct.items():
            row = self.sys.lca.dicts.biosphere.get(bd.get_node(database=key[0], code=key[1]).id)
            if row is not None:
                v[row] += amt
        return v

    def fit(self, target: np.ndarray, cand: list[tuple], lo: np.ndarray, hi: np.ndarray, direct: np.ndarray,
            determined: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray]:
        self.prefetch([self.ids[k] for k in cand])
        M = np.column_stack([self.col(self.ids[k]) for k in cand])
        # relative weights; the model side of the weight is first the unweighted NNLS solution, so
        # flows the target lacks but a candidate would bring count by their own size, then the fit
        # itself - two passes, as calibrate does
        scale = np.linalg.norm(M, axis=0); scale[scale == 0] = 1.0
        x = (so.nnls(M / scale, target - direct, maxiter=20000)[0] if M.shape[1] <= WIDE
             else nnls_working_set(M / scale, target - direct)) / scale
        for _ in range(2):
            w = self.sys.fit_weights(target, M @ x + direct, determined)
            rows = np.where(w > 0)[0]
            x = solve_weighted(w[rows, None] * M[rows], w[rows] * (target - direct)[rows], lo, hi)
        return x, M

    def run_case(self, case: dict, scenario: str, rng: random.Random) -> dict:
        truth = case["inputs"]
        keys = list(truth)
        target = self.sys.cumulative([self.ids[(db.INVENTORY_DB, case["code"])]])[:, 0]
        direct = np.zeros(self.sys.n_flows) if scenario.startswith("blind") else self.direct_vector(case["direct"])
        det = self.determined(case["code"])
        if scenario in ("oracle", "bounded"):
            cand = keys
        elif scenario == "partial":
            # drop the 30 % of inputs that explain the least of the inventory (what a report omits):
            # ranked by the share of determined target flows to which the input supplies >= 1 %
            contrib = {k: contribution_breadth(target, self.col(self.ids[k]) * truth[k], mask=det) for k in keys}
            keep = sorted(keys, key=lambda k: -contrib[k])[: max(1, round(0.7 * len(keys)))]
            cand = keep
        elif scenario == "distractors":
            pool = [k for k in self.blind_pool if k not in truth and k != (db.INVENTORY_DB, case["code"])]
            cand = keys + rng.sample(pool, min(10, len(pool)))
        elif scenario == "blind":
            cand = [k for k in self.blind_pool if k != (db.INVENTORY_DB, case["code"])]
        else:  # blind-all
            cand = [k for k in self.all_pool if k != (db.INVENTORY_DB, case["code"])]
        n = len(cand)
        lo, hi = np.zeros(n), np.full(n, np.inf)
        if scenario == "bounded":
            # a "known to a factor of 2" range is [0.5a, 2a] for a positive amount but [2a, 0.5a]
            # for a negative one (a credit line, e.g. the scrap credit on a zinc-coated duct), and
            # it collapses to a point for an amount of exactly 0. lsq_linear wants lo < hi
            # strictly, so order the pair and widen a degenerate interval by a hair.
            a = np.array([truth[k] for k in cand], dtype=float)
            lo, hi = np.minimum(0.5 * a, 2.0 * a), np.maximum(0.5 * a, 2.0 * a)
            hi = np.where(hi > lo, hi, lo + 1e-12)
        t0 = time.time()
        x, M = self.fit(target, cand, lo, hi, direct, det)
        explicit = M @ x + direct
        ag = flow_agreement(target, explicit, det)
        # structure: judged by the inventory, not by coefficient size. An input is "material" when its
        # true contribution reaches 1 % of the target amount of some determined flow; a candidate
        # counts as chosen when its fitted contribution does. Round-off flows are left out here as in
        # the flow score: a speck of a wrong input can exceed 1 % of a 1e-21 noise value. An input
        # left off the list (partial) is judged the same way, with its own column.
        def material(col: np.ndarray, amount: float) -> bool:
            return contribution_breadth(target, col * amount, mask=det) > 0
        cols = {k: M[:, i] for i, k in enumerate(cand)}
        true_material = {k for k in truth if material(cols[k] if k in cols else self.col(self.ids[k]), truth[k])}
        chosen = {k for i, k in enumerate(cand) if material(cols[k], x[i])}
        tp = len(chosen & true_material); fp = len(chosen - set(truth)); fn = len(true_material - chosen)
        ratios = [x[i] / truth[k] for i, k in enumerate(cand) if k in true_material and truth[k]]
        within20 = sum(1 for r in ratios if 0.8 <= r <= 1.2)
        return {
            "code": case["code"], "name": case["name"], "category": case["category"], "n_true_inputs": len(truth), "n_material_inputs": len(true_material),
            "scenario": scenario, "n_candidates": n, "n_chosen": len(chosen), "true_positives": tp, "false_positives": fp, "false_negatives": fn,
            "amounts_within_20pct": f"{within20}/{len(ratios)}", "amount_ratio_median": float(np.median(ratios)) if ratios else float("nan"),
            "n_target_flows": ag["n_target"], "n_scored_flows": ag["n_scored"], "n_excluded_flows": ag["n_excluded"],
            "flows_within_10pct": ag["within_10pct"], "flows_within_10pct_share": round(ag["within_10pct"] / max(1, ag["n_scored"]), 4),
            "flow_median_abs_delta_pct": round(100 * ag["median_abs_delta"], 3), "flows_missing": ag["n_missing"], "flows_extra": ag["n_extra"],
            "seconds": round(time.time() - t0, 2),
        }


def run(n: int, seed: int, scenarios: list[str], name: str, out_dir: Path = Path("results/benchmark"),
        shard: tuple[int, int] | None = None) -> Path:
    """``shard=(i, k)`` runs every k-th case starting at i and writes only <name>.shard<i>of<k>.csv;
    ``merge_shards`` then joins the k files into <name>.csv and writes the summary. For blind-all,
    whose cases take minutes each."""
    rng = random.Random(seed)
    cases = pick_cases(n, seed)
    if shard:
        cases = cases[shard[0]::shard[1]]
        name = f"{name}.shard{shard[0]}of{shard[1]}"
    print(f"{len(cases)} cases over {len(set(c['category'] for c in cases))} categories", file=sys.stderr)
    acts = bd.Database(db.INVENTORY_DB).load()
    ids = {k: bd.get_node(database=k[0], code=k[1]).id for k in acts}
    used: Counter = Counter()
    for key, act in acts.items():
        for e in act.get("exchanges", []):
            if e.get("type") == "technosphere" and tuple(e["input"]) != key:
                used[tuple(e["input"])] += 1
    sys_ = System(bd.get_node(database=db.INVENTORY_DB, code=cases[0]["code"]))
    bench = Bench(sys_, ids, used)
    rows = []
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / f"{name}.csv"
    for i, case in enumerate(cases, 1):
        for sc in scenarios:
            rows.append(bench.run_case(case, sc, rng))
        print(f"  {i}/{len(cases)} {case['name'][:50]} [{case['category']}] {sum(r['seconds'] for r in rows[-len(scenarios):]):.0f} s", file=sys.stderr)
        # written after every case, so a long run (blind-all) keeps what it has if it stops
        with csv_path.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]))
            w.writeheader(); w.writerows(rows)
    if shard:
        return csv_path
    return write_summary(rows, len(cases), seed, scenarios, name, out_dir, csv_path)


def merge_shards(n: int, seed: int, scenarios: list[str], name: str, k: int, out_dir: Path = Path("results/benchmark")) -> Path:
    order = {c["code"]: i for i, c in enumerate(pick_cases(n, seed))}
    rows = []
    for i in range(k):
        with (out_dir / f"{name}.shard{i}of{k}.csv").open() as fh:
            rows += list(csv.DictReader(fh))
    assert len({r["code"] for r in rows}) == n, "not every case is in the shards"
    rows.sort(key=lambda r: (order[r["code"]], scenarios.index(r["scenario"])))
    for r in rows:
        for f, v in r.items():
            if f not in ("code", "name", "category", "scenario", "amounts_within_20pct"):
                r[f] = float(v) if v not in ("", "nan") else float("nan")
    csv_path = out_dir / f"{name}.csv"
    with csv_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    return write_summary(rows, n, seed, scenarios, name, out_dir, csv_path)


def write_summary(rows: list[dict], n_cases: int, seed: int, scenarios: list[str], name: str, out_dir: Path, csv_path: Path) -> Path:
    L = [f"# Benchmark `{name}`: {n_cases} synthetic system processes, seed {seed}", "",
         "Ground truth = BAFU unit processes (3-30 inputs, stratified over categories); target = their cumulative inventory.", "",
         "| scenario | flows within ±10 % | median \\|Δ flow\\| | flows missing | material amounts within ±20 % | material inputs chosen / true | false pos. | false neg. |",
         "|---|---|---|---|---|---|---|---|"]
    for sc in scenarios:
        R = [r for r in rows if r["scenario"] == sc]
        w20 = [tuple(map(int, r["amounts_within_20pct"].split("/"))) for r in R]
        L.append(f"| {sc} | {np.median([r['flows_within_10pct_share'] for r in R]):.0%} | {np.median([r['flow_median_abs_delta_pct'] for r in R]):.1f} % | "
                 f"{np.median([r['flows_missing'] for r in R]):.0f} | {sum(a for a, _ in w20)}/{sum(b for _, b in w20)} | "
                 f"{np.median([r['n_chosen'] for r in R]):.0f} / {np.median([r['n_material_inputs'] for r in R]):.0f} | {np.median([r['false_positives'] for r in R]):.0f} | "
                 f"{np.median([r['false_negatives'] for r in R]):.0f} |")
    L += ["", "Medians over cases; no impact assessment — agreement is counted per elementary flow of the target's cumulative inventory, "
          "over the flows the solve determines (about 120 of ~1,790 per process come out of the sparse solve as round-off and are not scored; "
          "see lci.determined_flows). "
          "'Material' inputs are those whose true contribution reaches 1 % of the target amount of some determined flow (round-off flows are left out, as in the flow score). `partial` removes the 30 % of inputs that explain the fewest flows before fitting; "
          "`distractors` adds 10 random frequently-used processes; `blind` offers every process used ≥ 30 times and no direct flows; `blind-all` offers every dataset in the database and no direct flows.", ""]
    md_path = out_dir / f"{name}.md"
    md_path.write_text("\n".join(L) + "\n")
    print("\n".join(L[4:4 + 2 + len(scenarios)]))
    print(f"\n-> {csv_path}, {md_path}")
    return md_path


# ---------------------------------------------------------------- extraction mode: the whole route
def pick_extraction_cases(n: int, seed: int, ecospold_dir: Path, reports: Path, only: set[str] | None = None) -> list[dict]:
    """Unit processes (as pick_cases) whose cited report has a PDF in the bundle; sampled the same
    stratified way, skipping those without a report until n are found."""
    import csv
    import xml.etree.ElementTree as ET

    pdf_by_title = {r["title"]: r["pdf"] for r in csv.DictReader(open("results/sources.csv"))}
    pool = pick_cases(10 ** 6, seed)  # every eligible unit process, in the seeded round-robin order
    out = []
    for c in pool:
        if only and c["code"] not in only and c["code"][:8] not in only:
            continue
        src = ET.parse(ecospold_dir / f"process_{c['code']}.xml").getroot().find("dataset/metaInformation/modellingAndValidation/source")
        pdf = pdf_by_title.get(src.get("title", ""), "") if src is not None else ""
        if not pdf or not (reports / pdf).exists():
            continue
        out.append({**c, "pdf": pdf})
        if len(out) >= n:
            break
    return out


def score_extraction(case: dict, spec_path: Path) -> dict:
    """Compare the drafted (and resolved, calibrated) spec with the unit process's real exchanges."""
    from . import spec as spec_mod
    from .spec import walk

    sp = spec_mod.load(spec_path)
    truth_in = {k[1]: v for k, v in case["inputs"].items()}           # code -> amount
    truth_bio = {k: v for k, v in case["direct"].items()}             # (db, code) -> amount
    drafted_in: dict[str, float] = {}
    for node in walk(sp.node):
        for i in node.inputs:
            if i.code:
                base = i.code.split("-disagg")[0].split("-bench")[0]
                drafted_in[base] = drafted_in.get(base, 0.0) + i.amount
    import bw2data as bd

    def flow_key(database: str, code: str) -> tuple:
        """(name, top category): EF 3.1 carries the same substance in several sub-compartment
        flows (two 'Waste Heat [air]' codes), which a report cannot distinguish."""
        f = bd.get_node(database=database, code=code)
        cats = f.get("categories") or ()
        return (f["name"].lower(), str(cats[0]).lower().replace("emissions to ", "") if cats else "")

    drafted_bio: dict[tuple, float] = {}
    for f in sp.node.emissions + sp.node.resources:
        if f.code:
            k = flow_key(f.database, f.code)
            drafted_bio[k] = drafted_bio.get(k, 0.0) + f.amount
    truth_bio_named: dict[tuple, float] = {}
    for (database, code), amt in truth_bio.items():
        k = flow_key(database, code)
        truth_bio_named[k] = truth_bio_named.get(k, 0.0) + amt
    hit = set(truth_in) & set(drafted_in)
    ratios = [drafted_in[c] / truth_in[c] for c in hit if truth_in[c]]
    bio_hit = set(truth_bio_named) & set(drafted_bio)
    bio_ratios = [drafted_bio[k] / truth_bio_named[k] for k in bio_hit if truth_bio_named[k]]
    return {
        "true_inputs": len(truth_in), "drafted_inputs": len(drafted_in), "inputs_matched": len(hit),
        "inputs_missed": len(set(truth_in) - hit), "inputs_extra": len(set(drafted_in) - hit),
        "input_amounts_within_20pct": f"{sum(1 for r in ratios if 0.8 <= r <= 1.2)}/{len(ratios)}",
        "input_amount_ratio_median": float(np.median(ratios)) if ratios else float("nan"),
        "true_direct_flows": len(truth_bio_named), "drafted_direct_flows": len(drafted_bio), "direct_flows_matched": len(bio_hit),
        "direct_amounts_within_20pct": f"{sum(1 for r in bio_ratios if 0.8 <= r <= 1.2)}/{len(bio_ratios)}",
        "gaps_reported": len(sp.raw.get("provenance", {}).get("gaps_reported_by_model", [])),
    }


def run_extraction(n: int, seed: int, name: str, project: str, ecospold_dir: Path, reports: Path, dry_run: bool, by: str,
                   only: set[str] | None = None, out_dir: Path = Path("results/benchmark")) -> Path:
    """The whole route on unit processes with a report: locate -> evidence -> extract -> map ->
    assemble -> resolve -> calibrate -> build -> check, then scored against the real exchanges.
    Same on-disk state machine and model routes as draft-all; files under out_dir/extraction/."""
    import csv

    from . import build, calibrate, check, draft as draft_mod, resolve, spec as spec_mod
    from .spec import node_prefix

    root = out_dir / "extraction"
    draft_mod.EVIDENCE_ROOT, draft_mod.SPEC_ROOT = root / "evidence", root / "specs"
    db.set_project(project)
    cases = pick_extraction_cases(n, seed, ecospold_dir, reports, only)
    print(f"{len(cases)} unit processes with a report in the bundle", file=sys.stderr)
    rows = []
    for i, case in enumerate(cases, 1):
        rec = {"code": case["code"], "name": case["name"], "category": case["category"], "pdf": case["pdf"], "pages": "",
               "status": "", "note": "", "flows_within_10pct": "", "flows_within_10pct_share": "", "flow_median_abs_delta_pct": "", "flows_missing": ""}
        rows.append(rec)
        draft_mod.advance(case["code"], case["name"], reports / case["pdf"], ecospold_dir, project, dry_run, by, rec, variant="bench", fallbacks=False)
        print(f"  {i}/{len(cases)} {case['name'][:50]} -> {rec['status']}", file=sys.stderr)
        if rec["status"] != "drafted":
            continue
        spec_path = draft_mod.SPEC_ROOT / f"{case['code'][:8]}-{draft_mod.slug(case['name'])}.bench.json"
        try:
            sp = spec_mod.load(spec_path)
            if not resolve.run(sp):
                rec["status"], rec["note"] = "unresolved", "an input or flow of the drafted spec has no BAFU counterpart"
                continue
            spec_mod.save(sp)
            calibrate.run(sp, apply=True)
            sp = spec_mod.load(spec_path)
            build.run(sp, hybrid=True)
            report = check.run(spec_mod.load(spec_path), out_dir=root / "checks")
            from .runall import _summary
            rec.update(_summary(report))
            rec.update(score_extraction(case, spec_path))
            rec["status"] = "scored"
        except SystemExit as exc:
            rec["status"], rec["note"] = "error", str(exc)[:200]
    root.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / f"extraction-{name}.csv"
    fields = ["code", "name", "category", "pdf", "pages", "status", "note", "top_flows_within_10pct", "top_flow_median_abs_delta_pct", "kg_mass_covered_pct",
              "flows_within_10pct", "flows_within_10pct_share", "flow_median_abs_delta_pct", "flows_missing",
              "true_inputs", "drafted_inputs", "inputs_matched", "inputs_missed", "inputs_extra", "input_amounts_within_20pct",
              "input_amount_ratio_median", "true_direct_flows", "drafted_direct_flows", "direct_flows_matched", "direct_amounts_within_20pct", "gaps_reported"]
    with csv_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, restval="", extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    scored = [r for r in rows if r["status"] == "scored"]
    L = [f"# Extraction benchmark `{name}`: {len(cases)} unit processes with a report, seed {seed}", "",
         "The whole route (locate → evidence → extract → map → assemble → resolve → calibrate → build → check) on unit processes whose "
         "report is in the bundle, scored against their real exchanges.", "",
         "| status | n |", "|---|---|"] + [f"| {k} | {v} |" for k, v in Counter(r["status"] for r in rows).most_common()]
    if scored:
        rec_in = sum(r["inputs_matched"] for r in scored) / max(1, sum(r["true_inputs"] for r in scored))
        prec_in = sum(r["inputs_matched"] for r in scored) / max(1, sum(r["drafted_inputs"] for r in scored))
        w20 = [tuple(map(int, r["input_amounts_within_20pct"].split("/"))) for r in scored]
        rec_bio = sum(r["direct_flows_matched"] for r in scored) / max(1, sum(r["true_direct_flows"] for r in scored))
        L += ["", f"Scored cases: {len(scored)}. Inputs: recall {rec_in:.0%}, precision {prec_in:.0%}, amounts within ±20 % "
              f"{sum(a for a, _ in w20)}/{sum(b for _, b in w20)} of matched; direct flows: recall {rec_bio:.0%}; "
              f"rebuilt inventory: flows within ±10 % median {np.median([float(r['flows_within_10pct_share'].rstrip('%')) for r in scored if r['flows_within_10pct_share']]):.0f} %, "
              f"median |Δ flow| median {np.median([float(r['flow_median_abs_delta_pct']) for r in scored if r['flow_median_abs_delta_pct']]):.1f} %."]
    md_path = out_dir / f"extraction-{name}.md"
    md_path.write_text("\n".join(L) + "\n")
    print("\n".join(L[4:]))
    print(f"\n-> {csv_path}, {md_path}")
    return md_path
