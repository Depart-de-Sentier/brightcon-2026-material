"""Regenerate the artifact pages under artifacts/ from the specs, the sandbox and the check reports.

    uv run python scripts/render_pages.py [--project bafu-2026]

Writes artifacts/rebuilt-inventories.html (one tab per spec). The page is static HTML; publish it
with the Artifact tool or open it locally.
"""

from __future__ import annotations

import argparse
import csv
import glob
import html
import json
import re
import warnings
from pathlib import Path

import numpy as np
import bw2data as bd

from reverse_bafu import db, spec as spec_mod
from reverse_bafu.lci import System, contribution_breadth

esc = html.escape


def fmt(x: float) -> str:
    ax = abs(x)
    if ax == 0:
        return "0"
    if ax >= 100:
        return f"{x:,.0f}"
    if ax >= 1e-3:
        return f"{x:.3g}"
    return f"{x:.2e}"


HEADLINE = {  # the check report's headline, so the page shows the numbers results/ and the exports quote
    "top": re.compile(r"the 50 largest kilogram flows: (\d+)/(\d+) within ±10 %"),
    "mass": re.compile(r"kilogram mass covered within ±10 %: ([\d.]+)% of"),
    "scored": re.compile(r"of the (\d+) flows of the target, (\d+) are determined by the solve \((\d+) are round-off"),
    "all": re.compile(r"- (\d+) of those \d+ within ±10 % \(\d+%\), median \|Δ\| ([\d.]+)%, (\d+) missing from the model, (\d+) extra"),
}


def headline(md: str) -> dict:
    m = {k: rx.search(md) for k, rx in HEADLINE.items()}
    return dict(top_within10=int(m["top"].group(1)), top_n=int(m["top"].group(2)), mass_cov=float(m["mass"].group(1)) / 100,
                n_flows=int(m["scored"].group(2)), n_excluded=int(m["scored"].group(3)), within10=int(m["all"].group(1)),
                within10_share=int(m["all"].group(1)) / max(1, int(m["scored"].group(2))), median_delta=float(m["all"].group(2)),
                n_missing=int(m["all"].group(3)), n_extra=int(m["all"].group(4)))


def collect(project: str) -> list[dict]:
    """One record per spec: the original, the rebuilt process and their flow-by-flow agreement.

    No impact assessment — inputs are ranked by the kilogram mass they bring into the inventory and
    by how many of the target's flows they supply, and the deviation chart is per elementary flow."""
    db.set_project(project)
    # the union of the type=2 flag and the structural survey: an input that is an unflagged APME
    # eco-profile (styrene, benzene, butadiene, ...) is just as aggregated as a flagged one
    agg = db.aggregated_codes_all()
    out = []
    for path in sorted(glob.glob("specs/*.json")):
        sp = spec_mod.load(path)
        raw = sp.raw
        code, prefix = sp.target_code, spec_mod.node_prefix(sp)
        t = bd.get_node(database=db.INVENTORY_DB, code=code)
        e = bd.get_node(database=db.SANDBOX_DB, code=f"{prefix}-disagg")
        h = bd.get_node(database=db.SANDBOX_DB, code=f"{prefix}-hybrid")
        md = Path(f"results/checks/{prefix}.md").read_text()
        checks = [dict(ok=c[0] == "✓", msg=c[1]) for c in re.findall(r"^- ([✓✗]) (.+)$", md, re.M)]

        sys_ = System(e)
        ex_in = list(e.technosphere())
        inv = sys_.cumulative([t.id, e.id] + [x.input.id for x in ex_in])
        b_t, b_e = inv[:, 0], inv[:, 1]
        rows_by_unit: dict[str, list[int]] = {}
        for row in np.where(b_t != 0)[0]:
            rows_by_unit.setdefault(sys_.flow_node(int(row)).get("unit", ""), []).append(int(row))
        kg_rows = rows_by_unit.get("kilogram", [])
        kg_mass = float(sum(abs(b_t[r]) for r in kg_rows))

        inputs = []
        for j, (x, si) in enumerate(zip(ex_in, sp.node.inputs), start=2):
            col = inv[:, j] * x["amount"]
            inputs.append(dict(name=x.input["name"], loc=x.input.get("location", ""), amount=x["amount"], unit=x.input["unit"],
                               mass=float(sum(abs(col[r]) for r in kg_rows)),
                               covers=contribution_breadth(b_t, col), free=si.free, bounds=si.bounds, note=si.note,
                               sandbox=bool(si.sandbox), aggregated=x.input["database"] == db.INVENTORY_DB and x.input["code"] in agg))
        direct = [dict(name=x.input["name"], amount=x["amount"], unit=x.input["unit"],
                       cat="/".join(map(str, x.input["categories"][:2]))) for x in e.biosphere()]
        # the chart and the flow table: the largest kilogram flows of the original
        flows = []
        for row in sorted(kg_rows, key=lambda r: -abs(b_t[r]))[:24]:
            node = sys_.flow_node(row)
            cats = node.get("categories") or ()
            flows.append(dict(cat=node["name"], unit=node.get("unit", ""), where="/".join(str(c) for c in cats[:2]),
                              target=float(b_t[row]), explicit=float(b_e[row]),
                              delta=float(100 * (b_e[row] / b_t[row] - 1))))
        tb = sorted(t.biosphere(), key=lambda x: -abs(x["amount"]))
        hb = [x for x in h.biosphere() if "residual" in (x.get("comment") or "")]
        st = raw.get("strategy", {})
        out.append(dict(code=code, key=prefix[:8] + ("-" + sp.variant if sp.variant else ""), name=t["name"], loc=t["location"],
                        unit=t["unit"], variant=sp.variant or "", n_bio=len(tb), n_techno=len(list(t.technosphere())),
                        top_flows=[dict(name=x.input["name"], amount=x["amount"], unit=x.input["unit"],
                                        cat="/".join(map(str, x.input["categories"][:2]))) for x in tb[:6]],
                        strategy=f"{st.get('code', '?')} · {st.get('label', '')}", strategy_note=st.get("note", ""),
                        inputs=inputs, direct=direct, flows=flows, checks=checks, kg_mass=kg_mass,
                        **headline(md),
                        n_residual=len(hb), n_residual_neg=sum(1 for x in hb if x["amount"] < 0),
                        evidence=raw.get("evidence", [])))
    return out


def render(inv: list[dict]) -> str:
    tabs = "".join(f'<button class="tab" data-k="{o["key"]}" id="tab-{o["key"]}" aria-selected="{"true" if i == 0 else "false"}">{esc(o["name"])}<span class="loc">{o["loc"]}{" · " + o["variant"] if o["variant"] else ""}</span></button>' for i, o in enumerate(inv))
    ov = ""
    for o in inv:
        n_free = sum(1 for i in o["inputs"] if i["free"])
        deps = [i["name"] for i in o["inputs"] if i["aggregated"]]
        ov += (f'<tr><td class="n"><b>{esc(o["name"])}</b><span class="loc">{o["loc"]}</span><br><span class="muted">{esc(o["strategy"])}</span></td>'
               f'<td class="num">{o["n_techno"]} → {len(o["inputs"])}</td><td class="num">{o["n_bio"]:,} → {len(o["direct"])}</td><td class="num">{n_free}</td>'
               f'<td class="num">{o["top_within10"]} / {o["top_n"]}</td><td class="num">{o["mass_cov"]:.0%}</td>'
               f'<td class="num">{o["within10"]} / {o["n_flows"]:,}</td><td class="num">{o["n_residual_neg"]} / {o["n_residual"]}</td>'
               f'<td>{"—" if not deps else "depends on system processes: " + esc(", ".join(deps))}</td></tr>')
    panels = ""
    for i, o in enumerate(inv):
        mx = max(x["mass"] for x in o["inputs"]) or 1
        rows = ""
        for x in sorted(o["inputs"], key=lambda x: -x["mass"]):
            flags = ""
            if x["sandbox"]:
                flags += '<span class="tag blue">rebuilt node</span>'
            if x["aggregated"]:
                flags += '<span class="tag warn">system process</span>'
            if x["free"]:
                b = x["bounds"]; at = ""
                if b:
                    if abs(x["amount"] - b[0]) <= 1e-6 * max(1, abs(b[0])):
                        at = " · at lower bound"
                    elif abs(x["amount"] - b[1]) <= 1e-6 * max(1, abs(b[1])):
                        at = " · at upper bound"
                flags += f'<span class="tag">calibrated{esc(at)}</span>'
            note = f'<div class="note">{esc(x["note"])}</div>' if x["note"] else ""
            rows += (f'<tr><td class="n">{esc(x["name"])}<span class="loc">{esc(x["loc"] or "sandbox")}</span>{flags}{note}</td>'
                     f'<td class="num">{fmt(x["amount"])}</td><td class="u">{esc(x["unit"])}</td>'
                     f'<td class="num">{x["covers"]:.0%}</td>'
                     f'<td class="bar"><span class="fill" style="width:{max(0.5, 100 * x["mass"] / mx):.1f}%"></span><span class="v">{fmt(x["mass"])}</span></td></tr>')
        drows = "".join(f'<tr><td class="n">{esc(f["name"])}<span class="loc">{esc(f["cat"])}</span></td><td class="num">{fmt(f["amount"])}</td><td class="u">{esc(f["unit"])}</td></tr>' for f in o["direct"]) or '<tr><td colspan="3" class="muted">none — the report prints no direct emissions for this step</td></tr>'
        top = "".join(f'<li><span class="num">{fmt(f["amount"])}</span> <span class="u">{esc(f["unit"])}</span> {esc(f["name"])} <span class="loc">{esc(f["cat"].split("/")[-1])}</span></li>' for f in o["top_flows"])
        checks = "".join(f'<li><span class="{"ok" if c["ok"] else "bad"}">{"✓" if c["ok"] else "✗"}</span><span>{esc(c["msg"])}</span></li>' for c in o["checks"])
        ev = "".join(f'<li><b>{esc(e["source"])}</b> — {esc(e["where"])}<br><span class="muted">{esc(e.get("note", ""))}</span></li>' for e in o["evidence"])
        sum_mass = sum(x["mass"] for x in o["inputs"]); direct_kg = sum(f["amount"] for f in o["direct"] if f["unit"] == "kilogram")
        panels += f'''<section class="panel" id="panel-{o["key"]}" {"" if i == 0 else "hidden"}>
<div class="flow">
 <div class="box orig"><div class="eyebrow">Original · bafu‑2026</div><div class="big">{o["n_techno"]} inputs<br>{o["n_bio"]:,} flows</div><div class="muted">{esc(o["name"])} · {o["loc"]} · per 1 {esc(o["unit"])}</div><ul>{top}</ul></div>
 <div class="arrow">→</div>
 <div class="box new"><div class="eyebrow">Rebuilt · {esc(o["strategy"].split(" ")[0])}</div><div class="big">{len(o["inputs"])} inputs<br>{len(o["direct"])} direct flows</div><div class="muted">{esc(o["strategy_note"])}</div></div>
 <div class="arrow">→</div>
 <div class="box"><div class="eyebrow">Hybrid</div><div class="big">+ {o["n_residual"]:,} residual</div><div class="muted">{o["n_residual_neg"]} negative (over‑explained), {o["n_residual"] - o["n_residual_neg"]} positive; every flow equals the original by construction</div></div>
</div>
<h3>Technosphere inputs <span class="muted">· per 1 {esc(o["unit"])} · “covers” = share of the original’s flows this input supplies ≥ 1 % of · bar = kilogram mass it brings in</span></h3>
<div class="tbl"><table><thead><tr><th>Input</th><th style="text-align:right">Amount</th><th>Unit</th><th style="text-align:right">Covers</th><th>kg in the inventory</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="muted small">Inputs together carry {fmt(sum_mass)} kg of the original’s {fmt(o["kg_mass"])} kg of elementary flows{f" · direct flows add {fmt(direct_kg)} kg" if direct_kg else ""}.</p>
<h3>Direct elementary flows</h3>
<div class="tbl"><table><thead><tr><th>Flow</th><th style="text-align:right">Amount</th><th>Unit</th></tr></thead><tbody>{drows}</tbody></table></div>
<h3>Deviation from the original <span class="muted">· explicit model, per elementary flow — the 24 largest kilogram flows · symmetric‑log axis · band ±10 %</span></h3>
<p class="muted small">Over the {o["n_flows"]:,} flows of the original the solve determines ({o["n_excluded"]:,} round-off flows are not scored): {o["within10"]} within ±10 % ({o["within10_share"]:.0%}), median |Δ| {o["median_delta"]:.0f} %, {o["n_extra"]:,} flows the model adds that the original does not have. The large flows are the ones a report can name; the long tail comes from background chains the rebuilt process does not carry.</p>
<div class="chart" data-k="{o["key"]}"></div>
<h3>Structural checks</h3><ul class="checks">{checks}</ul>
<h3>Evidence</h3><ul class="ev">{ev}</ul>
</section>'''
    tmpl = Path("scripts/templates/rebuilt-inventories.tmpl.html").read_text()
    data = json.dumps({o["key"]: o["flows"] for o in inv})
    total = sum(1 for _ in csv.DictReader(open("results/system_terminated_extended.csv")))
    return (tmpl.replace("{{N}}", str(len(inv))).replace("{{D}}", str(len({o["code"] for o in inv})))
                .replace("{{T}}", str(total)).replace("{{OVERVIEW}}", ov).replace("{{TABS}}", tabs)
                .replace("{{PANELS}}", panels).replace("{{DATA}}", data))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--project", default="bafu-2026")
    args = p.parse_args()
    warnings.filterwarnings("ignore")
    inv = collect(args.project)
    Path("artifacts").mkdir(exist_ok=True)
    Path("artifacts/rebuilt-inventories.html").write_text(render(inv))
    for o in inv:
        print(f"{o['name'][:36]:36s} {o['variant'] or '-':6s} {o['strategy'][:4]}  inputs {o['n_techno']}→{len(o['inputs'])}  "
              f"large flows ±10 % {o['top_within10']}/{o['top_n']}  kg mass {o['mass_cov']:.0%}  all flows {o['within10']}/{o['n_flows']:,}")
    print("-> artifacts/rebuilt-inventories.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
