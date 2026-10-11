"""``reverse-bafu run-all``: resolve -> calibrate -> build -> check for every spec in specs/.

Specs are ordered so that a spec linking a rebuilt node (an input with ``"sandbox"``) runs after
the spec that builds that node. Per spec the outcome lands in results/rebuild_status.csv: status
(rebuilt / unresolved / error), flows within +-10 % of the target, the median flow deviation,
flows missing from the model, a note and the report path. ``--apply`` lets calibrate write the fitted amounts into the specs.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

from . import spec as spec_mod
from .spec import node_prefix, walk


def _deps(sp: spec_mod.Spec) -> set[str]:
    """Target codes of the specs this one depends on, from its sandbox links (code[-variant]-disagg)."""
    out = set()
    for n in walk(sp.node):
        for i in n.inputs:
            if i.sandbox:
                out.add(i.sandbox.split("-disagg")[0].split("-draft")[0])
    return out


def ordered(paths: list[Path]) -> list[spec_mod.Spec]:
    specs = [spec_mod.load(p) for p in paths]
    by_prefix = {node_prefix(s): s for s in specs}
    done: list[spec_mod.Spec] = []
    pending = list(specs)
    while pending:
        progressed = False
        for s in list(pending):
            deps = _deps(s)
            if all(any(node_prefix(d).startswith(dep) for d in done) or not any(node_prefix(x).startswith(dep) for x in specs) for dep in deps):
                done.append(s); pending.remove(s); progressed = True
        if not progressed:  # a cycle or a dependency with no spec: run the rest in file order
            done.extend(pending); break
    return done


def _summary(report: Path) -> dict:
    text = report.read_text()
    top = re.search(r"the 50 largest kilogram flows: (\d+)/(\d+) within ±10 %, median \|Δ\| ([\d.]+)%", text)
    mass = re.search(r"kilogram mass covered within ±10 %: ([\d.]+)% of", text)
    allf = re.search(r"- (\d+) of those (\d+) within ±10 % \((\d+)%\), median \|Δ\| ([\d.]+)%, (\d+) missing", text)
    if not (top and allf and mass):
        return {}
    return {"top_flows_within_10pct": f"{top.group(1)}/{top.group(2)}", "top_flow_median_abs_delta_pct": top.group(3), "kg_mass_covered_pct": mass.group(1),
            "flows_within_10pct": f"{allf.group(1)}/{allf.group(2)}", "flows_within_10pct_share": f"{allf.group(3)}%",
            "flow_median_abs_delta_pct": allf.group(4), "flows_missing": allf.group(5)}


def run_all(project: str, apply: bool, status_path: Path = Path("results/rebuild_status.csv")) -> None:
    from . import build, calibrate, check, db, resolve

    db.set_project(project)
    paths = sorted(p for p in Path("specs").glob("*.json"))
    if not paths:
        sys.exit("no specs in specs/")
    rows = []
    for sp in ordered(paths):
        rec = {"spec": str(sp.path), "code": sp.target_code, "name": sp.target_name, "variant": sp.variant or "",
               "strategy": sp.strategy.get("code", ""), "status": "", "top_flows_within_10pct": "", "top_flow_median_abs_delta_pct": "", "kg_mass_covered_pct": "", "flows_within_10pct": "", "flows_within_10pct_share": "", "flow_median_abs_delta_pct": "", "flows_missing": "", "note": "", "report": ""}
        rows.append(rec)
        print(f"\n=== {sp.path} ===", file=sys.stderr)
        try:
            if not resolve.run(sp):
                rec["status"] = "unresolved"; continue
            spec_mod.save(sp)
            calibrate.run(sp, apply=apply)
            sp = spec_mod.load(sp.path)
            build.run(sp, hybrid=True)
            report = check.run(spec_mod.load(sp.path))
            rec.update(_summary(report)); rec["status"] = "rebuilt"; rec["report"] = str(report)
        except SystemExit as exc:
            rec["status"], rec["note"] = "error", str(exc)[:160]
    status_path.parent.mkdir(parents=True, exist_ok=True)
    with status_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(f"\n{len(rows)} specs -> {status_path}")
    for r in rows:
        print(f"  {r['status']:10s} {r['name'][:32]:32s} {r['variant'] or '-':6s} top flows ±10 % {r['top_flows_within_10pct'] or '—':>6} mass {r['kg_mass_covered_pct'] or '—':>5}% all {r['flows_within_10pct'] or '—':>10} ({r['flows_within_10pct_share'] or '—':>4}) median |Δ| {r['flow_median_abs_delta_pct'] or '—':>5}% {r['note'][:60]}")
