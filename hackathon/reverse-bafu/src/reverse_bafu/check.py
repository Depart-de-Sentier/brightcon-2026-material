"""Step 4 - the harness: flow-by-flow agreement, the largest flows, residual and structural checks.

Inventory agreement is necessary, not sufficient (with every dataset as a candidate the benchmark
fit matches 100 % of the flows with mostly wrong inputs), so the structural section is not optional. No impact assessment: the target and the
rebuilt process are compared per elementary flow."""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import bw2data as bd

from . import db
from .lci import System, determined_flows, flow_agreement, mass_coverage, top_flow_agreement
from .spec import Spec, node_prefix, walk

POWER_PLANT = re.compile(r"at power plant|power plant$|at run-of-river|at reservoir", re.I)
BUCKETS = (("≤ 10 %", 0.10), ("10–20 %", 0.20), ("20–50 %", 0.50), ("50–100 %", 1.0), ("> 100 %", np.inf))


def summary_line(ag: dict, top: dict, mass_cov: float) -> str:
    return (f"flows: {top['within_10pct']}/{top['n']} of the largest kg flows within ±10 % (median |Δ| {top['median_abs_delta']:.1%}); "
            f"{mass_cov:.0%} of the kg mass; "
            f"{ag['within_10pct']}/{ag['n_scored']} of the determined flows within ±10 % ({ag['within_10pct'] / max(1, ag['n_scored']):.0%}"
            + (f", {ag['n_excluded']} round-off excluded" if ag['n_excluded'] else "") + "), "
            f"median |Δ| {ag['median_abs_delta']:.1%}, {ag['n_missing']} missing, {ag['n_extra']} extra")


def run(spec: Spec, out_dir: Path = Path("results/checks")) -> Path:
    target = bd.get_node(database=db.INVENTORY_DB, code=spec.target_code)
    explicit = bd.get_node(database=db.SANDBOX_DB, code=f"{node_prefix(spec)}-disagg")
    try:
        hybrid = bd.get_node(database=db.SANDBOX_DB, code=f"{node_prefix(spec)}-hybrid")
    except Exception:
        hybrid = None
    sys_ = System(explicit)
    ids = [target.id, explicit.id] + ([hybrid.id] if hybrid else [])
    inv = sys_.cumulative(ids)
    b_t, b_e = inv[:, 0], inv[:, 1]
    det = determined_flows(sys_, target.id)
    ag = flow_agreement(b_t, b_e, det)
    delta = ag["delta"]
    r = b_t - b_e
    units: dict[str, list[int]] = {}
    for row in np.where(b_t != 0)[0]:
        units.setdefault(sys_.flow_node(int(row)).get("unit", ""), []).append(int(row))
    top = top_flow_agreement(b_t, b_e, units.get("kilogram", []), 50)
    mass_cov = mass_coverage(b_t, b_e, units.get("kilogram", []))
    # the hybrid must reproduce the target flow for flow; the tolerance is float round-off in the
    # solve, relative plus a floor (build drops residual entries below 1e-15, and flows absent from
    # the target carry the explicit model's own round-off)
    hyb_off = int((np.abs(inv[:, 2] - b_t) > 1e-6 * np.abs(b_t) + 1e-9 * np.abs(b_t).max()).sum()) if hybrid else None

    st = spec.strategy
    L = [f"# Check: {spec.target_name} ({spec.target_code})", "",
         f"target `{db.INVENTORY_DB}` vs explicit model `{explicit['code']}`" + (f" and hybrid `{hybrid['code']}`" if hybrid else ""), "",
         f"**Strategy:** {st.get('code', '?')} — {st.get('label', 'not recorded in the spec')}" + (f". {st['note']}" if st.get('note') else ""),
         f"**Calibrated inputs:** " + (", ".join(f"{i.name}" + (f" [{i.bounds[0]:.3g}–{i.bounds[1]:.3g}]" if i.bounds else "") for n in walk(spec.node) for i in n.inputs if i.free) or "none")
         + (f"; mass sum {spec.node.mass_sum}" if spec.node.mass_sum is not None else ""),
         f"**Links to rebuilt nodes:** " + (", ".join(i.name for n in walk(spec.node) for i in n.inputs if i.sandbox) or "none"), "",
         "## Flow agreement (explicit vs target, per elementary flow)", "",
         f"- the 50 largest kilogram flows: {top['within_10pct']}/{top['n']} within ±10 %, median |Δ| {top['median_abs_delta']:.1%}",
         f"- kilogram mass covered within ±10 %: {mass_cov:.1%} of the target's total kg mass",
         f"- of the {ag['n_target']} flows of the target, {ag['n_scored']} are determined by the solve "
         f"({ag['n_excluded']} are round-off and are not scored; see lci.determined_flows)",
         f"- {ag['within_10pct']} of those {ag['n_scored']} within ±10 % ({ag['within_10pct'] / max(1, ag['n_scored']):.0%}), median |Δ| {ag['median_abs_delta']:.1%}, {ag['n_missing']} missing from the model, {ag['n_extra']} extra",
         f"- hybrid vs target: {'identical on every flow' if hyb_off == 0 else f'{hyb_off} flows differ'}" if hybrid else "- no hybrid node", "",
         "| \\|Δ\\| bucket | flows | share of target flows |", "|---|---|---|"]
    d = np.abs(delta[b_t != 0])
    lo = 0.0
    for label, hi in BUCKETS:
        n = int(((d > lo) & (d <= hi)).sum()) if lo > 0 else int((d <= hi).sum())
        L.append(f"| {label} | {n} | {n / max(1, ag['n_target']):.0%} |")
        lo = hi
    L.append(f"| missing (0 in model) | {ag['n_missing']} | {ag['n_missing'] / max(1, ag['n_target']):.0%} |")

    # the largest flows by amount, per unit: what a reader would look at first
    L += ["", "## Largest target flows (by amount, per unit) and their agreement", ""]
    for unit, rows in sorted(units.items(), key=lambda kv: -len(kv[1])):
        largest = sorted(rows, key=lambda i: -abs(b_t[i]))[: 20 if unit == "kilogram" else 5]
        L += [f"### {unit} ({len(rows)} flows)", "", "| flow | target | explicit | Δ | residual |", "|---|---|---|---|---|"]
        for row in largest:
            L.append(f"| {sys_.flow_label(row)} | {b_t[row]:.3g} | {b_e[row]:.3g} | {delta[row]:+.1%} | {r[row]:+.3g} |")
        L.append("")

    L += ["## Worst deviations among the 50 largest kilogram flows", "", "| flow | target | explicit | Δ |", "|---|---|---|---|"]
    big = sorted(units.get("kilogram", []), key=lambda i: -abs(b_t[i]))[:50]
    for row in sorted(big, key=lambda i: -abs(delta[i]))[:10]:
        L.append(f"| {sys_.flow_label(row)} | {b_t[row]:.3g} | {b_e[row]:.3g} | {delta[row]:+.1%} |")

    L += ["", "## Structural checks", ""]
    nodes = list(walk(spec.node))
    n_inputs = sum(len(n.inputs) for n in nodes)
    agg = db.aggregated_codes_all()
    deps = [i.name for n in nodes for i in n.inputs if i.code in agg]
    plants = [i.name for n in nodes for i in n.inputs if POWER_PLANT.search(i.name)]
    kg_in = sum(i.amount for i in spec.node.inputs if i.unit.startswith("kilo") and not i.name.lower().startswith(("disposal", "transport")))
    kg_res = sum(f.amount for f in spec.node.resources if f.unit.startswith("kilo"))
    checks = [
        (n_inputs <= 30, f"{n_inputs} explicit input(s) over {len(nodes)} node(s)"),
        (not plants, "no decomposed grid mixes" if not plants else f"inputs are individual power plants: {plants}"),
        (not deps, "no dependency on another system process" if not deps else f"depends on system processes (rebuild those first): {deps}"),
        (True, f"mass in: {kg_in:.3g} kg technosphere + {kg_res:.3g} kg resources per 1 {spec.node.unit} product (informational)"),
        (all(i.code or i.node for n in nodes for i in n.inputs), "all inputs resolved"),
    ]
    for ok, msg in checks:
        L.append(f"- {'✓' if ok else '✗'} {msg}")
    n_neg = int((r < 0).sum()); n_pos = int((r > 0).sum())
    L += ["", f"residual: {n_pos} flows under-explained, {n_neg} over-explained (negative residual)", ""]
    L += ["## Evidence", ""] + [f"- {e.get('source', '')} — {e.get('where', '')} {e.get('note', '')}".rstrip() for e in spec.evidence]

    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{node_prefix(spec)}.md"
    out.write_text("\n".join(L) + "\n")
    print(summary_line(ag, top, mass_cov))
    for ok, msg in checks:
        print(f"  {'✓' if ok else '✗'} {msg}")
    print(f"report -> {out}")
    return out
