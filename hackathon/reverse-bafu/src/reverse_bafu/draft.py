"""Draft a spec from evidence, reproducibly.

Four steps per dataset, each leaving files under ``specs/evidence/<code>/``:

0. ``locate``    one model prompt: every table and figure caption of the cited report (with its
                 PDF page) is listed; the model names the pages holding the dataset's inventory.
1. ``evidence``  deterministic: those pages as text (pdftotext -layout), the target's ecoSpold
                 metadata, its direct-resource candidates, and a manifest with SHA-256s.
2. ``draft``     two model prompts with fixed templates (``prompts/``): extraction (report excerpt
                 -> line items with quotes) and mapping (line items + keyword-search candidates ->
                 BAFU dataset names). The rendered prompts, the raw responses, model, effort and
                 hashes are all saved. ``--dry-run`` writes the prompts only, for running the model
                 elsewhere; ``--from-response`` ingests such a response.
3. ``assemble``  deterministic: line items + mapping -> ``specs/<code8>-<slug>.draft.json`` with a
                 ``derivation`` on every input and a ``provenance`` block.

When no report prints the inventory, ``draft_all`` continues with two more routes (``fallback``):
a template transfer from a same-product unit process (prompt 3, ``assemble_template``) and a model
from the dataset's own metadata and chemistry (prompts 4 and 5, ``assemble_metadata``).

The model never returns byte-identical JSON; what is reproducible is the evidence, the exact
prompt, the pinned model, and an audit trail from every number to a quoted line.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import html
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from . import db
from .spec import slug

PROMPTS = Path("prompts")
EVIDENCE_ROOT = Path("specs/evidence")   # the benchmark re-points these two
SPEC_ROOT = Path("specs")
MODEL = "claude-opus-5"
EFFORT = "high"

# ---------------------------------------------------------------- schemas (structured output)
LINE_ITEM = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "kind": {"type": "string", "enum": ["input", "emission", "resource", "product", "co-product", "ignore"]},
        "quote": {"type": "string"},
        "raw_value": {"type": "number"},
        "raw_min": {"type": ["number", "null"]},
        "raw_max": {"type": ["number", "null"]},
        "raw_unit": {"type": "string"},
        "per": {"type": "string"},
        "factor": {"type": "number"},
        "factor_unit": {"type": "string"},
        "factor_source": {"type": "string"},
        "search": {"type": "string"},
        "compartment": {"type": "string", "enum": ["air", "water", "soil", "resources", ""]},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "note": {"type": "string"},
    },
    "required": ["name", "kind", "quote", "raw_value", "raw_min", "raw_max", "raw_unit", "per", "factor", "factor_unit",
                 "factor_source", "search", "compartment", "confidence", "note"],
    "additionalProperties": False,
}
EXTRACTION_SCHEMA = {
    "type": "object",
    "properties": {
        "basis": {"type": "string", "description": "the excerpt's reference basis, e.g. 'per t burnt shale, 71.3 % allocation column'"},
        "basis_amount": {"type": "number", "description": "how many target units one basis corresponds to, e.g. 1000 for per-t values of a per-kg target"},
        "allocation": {"type": "string"},
        "mass_sum": {"type": ["number", "null"], "description": "if the excerpt states that the composition items add up to a mass per basis (e.g. 'adds up to 1.00 kg'), that mass; else null"},
        "items": {"type": "array", "items": LINE_ITEM},
        "gaps": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["basis", "basis_amount", "allocation", "mass_sum", "items", "gaps"],
    "additionalProperties": False,
}
MAPPING_SCHEMA = {
    "type": "object",
    "properties": {
        "mappings": {"type": "array", "items": {
            "type": "object",
            "properties": {
                "item": {"type": "string"},
                "chosen": {"type": ["string", "null"]},
                "location": {"type": "string"},
                "compartment": {"type": "string", "description": "for emissions/resources: the chosen flow's compartment as listed"},
                "dependency": {"type": "boolean"},
                "reason": {"type": "string"},
            },
            "required": ["item", "chosen", "location", "compartment", "dependency", "reason"],
            "additionalProperties": False,
        }},
    },
    "required": ["mappings"],
    "additionalProperties": False,
}


LOCATE_SCHEMA = {
    "type": "object",
    "properties": {
        "found": {"type": "boolean"},
        "first_page": {"type": ["integer", "null"]},
        "last_page": {"type": ["integer", "null"]},
        "captions": {"type": "array", "items": {"type": "string"}},
        "reason": {"type": "string"},
    },
    "required": ["found", "first_page", "last_page", "captions", "reason"],
    "additionalProperties": False,
}
# `2.1`, `2-1`, `2.1.3` - some reports number with hyphens, and some put the label on its own line
# with the caption text on the next one (2017 - LCI wood and wood based products - Werner: 255 pages,
# zero captions before this was widened). LABEL_ONLY_RX catches that second form.
CAPTION_RX = re.compile(
    r"^\s*((?:Tab\.?|Table|Tabelle|Tableau|Fig\.?|Figure|Abb\.)\s*\d+(?:[.\-]\d+)*\s*[:.]?\s+.{6,140})", re.M)
LABEL_ONLY_RX = re.compile(
    r"^\s*((?:Tab\.?|Table|Tabelle|Tableau|Fig\.?|Figure|Abb\.)\s*\d+(?:[.\-]\d+)*\s*[:.]?)\s*$", re.M)
CACHE = Path(".cache/pdftext")


def pdf_pages(pdf: Path) -> list[str]:
    """Text of every page (pdftotext -layout), cached under .cache/pdftext/<sha256>/."""
    d = CACHE / sha256(pdf)
    if not (d / "n").exists():
        d.mkdir(parents=True, exist_ok=True)
        n = int(next(l for l in subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout.splitlines() if l.startswith("Pages:")).split()[1])
        for i in range(1, n + 1):
            subprocess.run(["pdftotext", "-layout", "-f", str(i), "-l", str(i), str(pdf), str(d / f"{i}.txt")], check=True)
        (d / "n").write_text(str(n))
    n = int((d / "n").read_text())
    return [(d / f"{i}.txt").read_text() for i in range(1, n + 1)]


def captions_index(pdf: Path) -> list[dict]:
    """Every table/figure caption with its PDF page - deterministic, language-neutral in form."""
    out, seen = [], set()
    for i, text in enumerate(pdf_pages(pdf), 1):
        # a label alone on its line: pull the next non-empty line up so it reads as one caption
        lines = text.splitlines()
        merged, skip = [], False
        for j, line in enumerate(lines):
            if skip:
                skip = False
                continue
            if LABEL_ONLY_RX.match(line):
                nxt = next((lines[k] for k in range(j + 1, min(j + 3, len(lines))) if lines[k].strip()), "")
                if nxt and not LABEL_ONLY_RX.match(nxt):
                    merged.append(f"{line.strip()} {nxt.strip()}")
                    skip = True
                    continue
            merged.append(line)
        for m in CAPTION_RX.finditer("\n".join(merged)):
            cap = re.sub(r"\s+", " ", m.group(1)).strip()
            if cap not in seen:
                seen.add(cap)
                out.append({"page": i, "caption": cap})
    return out


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------- layer 1: evidence
def evidence(code: str, report: Path, pages: str, ecospold_dir: Path, project: str) -> Path:
    """Write specs/evidence/<code>/: report text, target metadata, direct-resource candidates, manifest."""
    out = EVIDENCE_ROOT / code
    out.mkdir(parents=True, exist_ok=True)
    first, last = (pages.split("-") + [pages])[:2]
    txt = out / f"report-p{first}-{last}.txt"
    subprocess.run(["pdftotext", "-layout", "-f", first, "-l", last, str(report), str(txt)], check=True)
    xml = write_target(out, code, ecospold_dir, project)
    manifest = {
        "code": code, "created": _now(),
        "report": {"file": report.name, "sha256": sha256(report), "pages": pages},
        "report_text": {"file": txt.name, "sha256": sha256(txt), "tool": subprocess.run(["pdftotext", "-v"], capture_output=True, text=True).stderr.splitlines()[0]},
        "ecospold": {"file": xml.name, "sha256": sha256(xml)},
        "brightway_project": project,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1))
    print(f"evidence -> {out}/ ({txt.name}, target.json, manifest.json)")
    return out


def write_target(out: Path, code: str, ecospold_dir: Path, project: str) -> Path:
    """target.json: the dataset's ecoSpold metadata and its direct-resource candidates. Shared by the
    report route (``evidence``) and the two routes for datasets without a report table."""
    xml = ecospold_dir / f"process_{code}.xml"
    ds = ET.parse(xml).getroot().find("dataset")
    pi = ds.find("metaInformation/processInformation")
    rf = pi.find("referenceFunction")
    src = ds.find("metaInformation/modellingAndValidation/source")
    tp = pi.find("timePeriod")
    meta = {
        "name": rf.get("name"), "unit": rf.get("unit"), "location": pi.find("geography").get("location"),
        "category": f"{rf.get('category')} / {rf.get('subCategory')}",
        "includedProcesses": rf.get("includedProcesses", ""), "generalComment": rf.get("generalComment", ""),
        "technology": pi.find("technology").get("text", "") if pi.find("technology") is not None else "",
        "source": " | ".join(x for x in (src.get("firstAuthor"), src.get("year"), src.get("title")) if x) if src is not None else "",
        "timePeriod": f"{tp.findtext('startYear') or tp.findtext('startDate') or ''}-{tp.findtext('endYear') or tp.findtext('endDate') or ''}" if tp is not None else "",
        "n_flows": len(ds.find("flowData").findall("exchange")),
    }
    # direct-resource candidates: resource flows of the target vector, largest first
    import bw2data as bd
    db.set_project(project)
    t = bd.get_node(database=db.INVENTORY_DB, code=code)
    res = []
    for e in t.biosphere():
        cats = " ".join(map(str, e.input.get("categories", ())))
        if "esource" in cats or cats.strip() in ("soil",):
            res.append({"name": e.input["name"], "amount": e["amount"], "unit": e.input["unit"], "categories": cats})
    res.sort(key=lambda r: -abs(r["amount"]))
    (out / "target.json").write_text(json.dumps({**meta, "direct_resource_candidates": res[:12]}, indent=1, ensure_ascii=False))
    return xml


# ---------------------------------------------------------------- layer 2: prompts + LLM
def render(template: Path, **kw) -> str:
    text = template.read_text()
    for k, v in kw.items():
        text = text.replace("{{" + k + "}}", str(v))
    missing = re.findall(r"\{\{(\w+)\}\}", text)
    if missing:
        raise SystemExit(f"unfilled placeholders in {template}: {missing}")
    return text


def target_meta(code: str, ecospold_dir: Path) -> dict:
    ds = ET.parse(ecospold_dir / f"process_{code}.xml").getroot().find("dataset")
    pi = ds.find("metaInformation/processInformation")
    rf = pi.find("referenceFunction")
    return {"name": rf.get("name"), "unit": rf.get("unit"), "location": pi.find("geography").get("location"),
            "category": f"{rf.get('category')} / {rf.get('subCategory')}", "includedProcesses": rf.get("includedProcesses", ""),
            "generalComment": rf.get("generalComment", ""),
            "technology": pi.find("technology").get("text", "") if pi.find("technology") is not None else ""}


def locate_prompt(code: str, pdf: Path, ecospold_dir: Path) -> tuple[str, list[dict]]:
    meta = target_meta(code, ecospold_dir)
    caps = captions_index(pdf)
    listing = "\n".join(f"- p.{c['page']}: {c['caption']}" for c in caps) or "- (no captions found)"
    n_pages = len(pdf_pages(pdf))
    return render(PROMPTS / "locate_pages.md", target_name=meta["name"], target_location=meta["location"], target_unit=meta["unit"],
                  target_category=meta["category"], included_processes=(meta["includedProcesses"] or "—")[:300],
                  technology=(meta["technology"] or "—")[:200], general_comment=(meta["generalComment"] or "—")[:300],
                  report_name=pdf.name, n_pages=n_pages, captions=listing), caps


def locate(code: str, pdf: Path, ecospold_dir: Path, dry_run: bool, from_response: Path | None, by: str) -> dict | None:
    """Pass 0: which PDF pages hold the dataset's inventory. Returns the validated response or None (dry run)."""
    ev = EVIDENCE_ROOT / code
    ev.mkdir(parents=True, exist_ok=True)
    prompt, caps = locate_prompt(code, pdf, ecospold_dir)
    (ev / "prompt-0-locate.md").write_text(prompt)
    (ev / "schema-0-locate.json").write_text(json.dumps(LOCATE_SCHEMA, indent=1))
    (ev / "captions-0-locate.json").write_text(json.dumps({"pdf": pdf.name, "sha256": sha256(pdf), "captions": caps}, indent=1, ensure_ascii=False))
    if from_response:
        resp = _load_response(from_response, LOCATE_SCHEMA, "locate")
        prov = {"model": "manual", "by": by, "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(), "at": _now()}
    elif dry_run:
        return None
    else:
        resp, prov = call_model(prompt, LOCATE_SCHEMA, "locate")
    (ev / "response-0-locate.json").write_text(json.dumps(resp, indent=1, ensure_ascii=False))
    (ev / "provenance-0-locate.json").write_text(json.dumps(prov, indent=1))
    return resp


def extraction_prompt(ev: Path) -> str:
    man = json.loads((ev / "manifest.json").read_text())
    meta = json.loads((ev / "target.json").read_text())
    cands = "\n".join(f"- {r['name']}: {r['amount']:.4g} {r['unit']} ({r['categories']})" for r in meta["direct_resource_candidates"]) or "- none"
    return render(PROMPTS / "draft_spec.md",
                  target_name=meta["name"], target_location=meta["location"], target_unit=meta["unit"], n_flows=meta["n_flows"],
                  target_category=meta["category"], included_processes=meta["includedProcesses"] or "—", technology=meta["technology"] or "—",
                  general_comment=meta["generalComment"] or "—", source=meta["source"] or "—", time_period=meta["timePeriod"] or "—",
                  direct_candidates=cands, evidence_file=man["report_text"]["file"], evidence_sha256=man["report_text"]["sha256"],
                  evidence_pages=man["report"]["pages"], report_name=man["report"]["file"],
                  evidence_text=(ev / man["report_text"]["file"]).read_text().strip())


def _matched(words: list[str], name: str) -> int:
    """Words matched at a word start ('particulate' matches 'particulates', 'dust' not 'industrial')."""
    return sum(1 for w in words if re.search(r"(?<![a-z0-9])" + re.escape(w), name))


def candidates_for(search: str, prefer_location: str = "", k: int = 8) -> list[dict]:
    """Deterministic keyword search over the BAFU name index. Rank: number of search words in the
    name (desc), then location preference (the target's, then RER/CH/DE/GLO), then name length."""
    words = [w for w in re.findall(r"[a-z0-9%]+", search.lower()) if len(w) > 2]
    order: dict[str, int] = {}
    for loc in [prefer_location, *db.LOCATION_PREFERENCE]:
        order.setdefault(loc, len(order))  # the target's location first, without being overwritten
    need = max(1, len(words) - 1)  # all words, or all but one
    hits = []
    for norm, entries in db.activity_index().items():
        n = _matched(words, norm)
        if n < need:
            continue
        for e in entries:
            hits.append((-n, order.get(e["location"], 99), len(e["name"]), e["name"], e["location"], e["code"], e))
    hits.sort(key=lambda t: t[:6])  # full key: ties never fall back to database iteration order
    return [t[6] for t in hits[:k]]


def flow_candidates_for(name: str, compartment: str, search: str = "", k: int = 8) -> list[dict]:
    """Deterministic search over the two biosphere databases: every word of the search phrase (or
    the name) matched at a word start; the hinted compartment first; one entry per (name, top-2
    categories)."""
    words = [w for w in re.findall(r"[a-z0-9]+", (search or name).lower()) if len(w) > 1 and w not in ("fossil", "geogenic", "carbonate", "to")]
    need = max(1, len(words) - 1)
    hits = []
    for norm, entries in db.flow_index().items():
        n = _matched(words, norm)
        if n < need:
            continue
        for e in entries:
            cats = " / ".join(e["categories"][:2])
            hits.append((-n, 0 if compartment and compartment in cats.lower() else 1, 0 if "unspecified" in cats.lower() else 1,
                         len(e["name"]), e["name"], cats, " / ".join(e["categories"]), e["database"], e["code"], {**e, "cats": cats}))
    hits.sort(key=lambda t: t[:9])  # full key, then dedupe: the representative of a (name, compartment) is fixed
    seen, out = set(), []
    for t in hits:
        key = (t[4], t[5])
        if key in seen:
            continue
        seen.add(key)
        out.append(t[9])
        if len(out) == k:
            break
    return out


def mapping_prompt(extraction: dict, target_location: str) -> tuple[str, dict]:
    lines, cand_record = [], {}
    for it in extraction["items"]:
        if it["kind"] == "input":
            cands = candidates_for(it["search"], target_location)
            cand_record[it["name"]] = cands
            c = "\n".join(f"    - {e['name']} [{e['location']}] ({e['unit']}, {e['n_inputs']} inputs{', aggregated' if e['aggregated'] else ''})" for e in cands) or "    - (no candidate found)"
            lines.append(f"- item: {it['name']}  (input)\n  quote: {it['quote']}\n  search: {it['search']}\n  candidates:\n{c}")
        elif it["kind"] in ("emission", "resource"):
            cands = flow_candidates_for(it["name"], it["compartment"], it["search"])
            cand_record[it["name"]] = cands
            c = "\n".join(f"    - {e['name']}  [{e['cats']}] ({e['unit']}, {e['database']})" for e in cands) or "    - (no candidate found)"
            lines.append(f"- item: {it['name']}  ({it['kind']} to {it['compartment'] or '?'})\n  quote: {it['quote']}\n  candidates (flow name [compartment]):\n{c}")
    return render(PROMPTS / "map_inputs.md", target_location=target_location, items="\n".join(lines)), cand_record


def call_model(prompt: str, schema: dict, label: str) -> tuple[dict, dict]:
    """One structured-output call; returns (parsed JSON, provenance)."""
    try:
        import anthropic
    except ImportError:
        raise SystemExit("the anthropic SDK is not installed: uv sync --extra llm   (or use --dry-run / --from-response)")
    client = anthropic.Anthropic()
    with client.messages.stream(
        model=MODEL, max_tokens=32000,
        thinking={"type": "adaptive"}, output_config={"effort": EFFORT, "format": {"type": "json_schema", "schema": schema}},
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        msg = stream.get_final_message()
    if msg.stop_reason == "refusal":
        raise SystemExit(f"{label}: the model declined ({msg.stop_details})")
    text = next(b.text for b in msg.content if b.type == "text")
    prov = {"model": msg.model, "requested_model": MODEL, "effort": EFFORT, "message_id": msg.id, "stop_reason": msg.stop_reason,
            "usage": {"input_tokens": msg.usage.input_tokens, "output_tokens": msg.usage.output_tokens},
            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(), "at": _now(), "by": f"llm:{msg.model}"}
    return json.loads(text), prov


def _load_response(path: Path, schema: dict, label: str) -> dict:
    """A response obtained outside the API (Claude Code, claude.ai, by hand) is validated against
    the same schema the API would have enforced."""
    import jsonschema

    data = json.loads(path.read_text())
    try:
        jsonschema.validate(data, schema)
    except jsonschema.ValidationError as exc:
        raise SystemExit(f"{label}: {path} does not match the schema: {exc.message} (at {'/'.join(map(str, exc.absolute_path))})")
    return data


def draft(code: str, dry_run: bool, from_response: dict[str, Path] | None, project: str, variant: str = "draft") -> None:
    ev = EVIDENCE_ROOT / code
    if not (ev / "manifest.json").exists():
        raise SystemExit(f"no evidence for {code}: run `reverse-bafu evidence` first")
    meta = json.loads((ev / "target.json").read_text())
    db.set_project(project)

    # pass 1 — extraction
    p1 = extraction_prompt(ev)
    (ev / "prompt-1-extract.md").write_text(p1)
    (ev / "schema-1-extract.json").write_text(json.dumps(EXTRACTION_SCHEMA, indent=1))
    if from_response and "extract" in from_response:
        ext = _load_response(from_response["extract"], EXTRACTION_SCHEMA, "extraction")
        prov1 = {"model": "manual", "by": from_response.get("by", "manual"), "prompt_sha256": hashlib.sha256(p1.encode()).hexdigest(), "at": _now()}
    elif dry_run:
        print(f"dry run: extraction prompt -> {ev}/prompt-1-extract.md (schema beside it). Run it, save the JSON as response-1-extract.json, then rerun with --from-response")
        return
    else:
        ext, prov1 = call_model(p1, EXTRACTION_SCHEMA, "extraction")
    (ev / "response-1-extract.json").write_text(json.dumps(ext, indent=1, ensure_ascii=False))
    (ev / "provenance-1-extract.json").write_text(json.dumps(prov1, indent=1))

    # pass 2 — mapping (deterministic candidates + one call)
    p2, cands = mapping_prompt(ext, meta["location"])
    (ev / "prompt-2-map.md").write_text(p2)
    (ev / "candidates-2-map.json").write_text(json.dumps(cands, indent=1, ensure_ascii=False))
    (ev / "schema-2-map.json").write_text(json.dumps(MAPPING_SCHEMA, indent=1))
    if from_response and "map" in from_response:
        mp = _load_response(from_response["map"], MAPPING_SCHEMA, "mapping")
        prov2 = {"model": "manual", "by": from_response.get("by", "manual"), "prompt_sha256": hashlib.sha256(p2.encode()).hexdigest(), "at": _now()}
    elif dry_run or (from_response and "map" not in from_response):
        print(f"mapping prompt -> {ev}/prompt-2-map.md (candidates from a deterministic name search beside it). Run it, save as response-2-map.json, rerun with --from-response")
        return
    else:
        mp, prov2 = call_model(p2, MAPPING_SCHEMA, "mapping")
    (ev / "response-2-map.json").write_text(json.dumps(mp, indent=1, ensure_ascii=False))
    (ev / "provenance-2-map.json").write_text(json.dumps(prov2, indent=1))
    assemble(code, project, variant)


# ---------------------------------------------------------------- batch: every row of the CSV
def _route_of(code: str) -> str:
    """Which route produced the draft spec of `code`, read from the responses on disk."""
    ev = EVIDENCE_ROOT / code
    if (ev / "response-2-map.json").exists():
        return "report"
    r3 = ev / "response-3-template.json"
    if r3.exists() and json.loads(r3.read_text()).get("chosen_code"):
        return "template"
    return "metadata" if (ev / "response-5-map.json").exists() else ""


def advance(code: str, name: str, pdf: Path, ecospold_dir: Path, project: str, dry_run: bool, by: str,
            rec: dict, variant: str = "draft", fallbacks: bool = True) -> None:
    """Take one dataset as far as its on-disk state allows: locate -> evidence -> extract -> map ->
    assemble. Fills rec["status"] / rec["note"] / rec["pages"]; never overwrites an existing spec.
    When the report prints no inventory, hands over to the template and metadata routes (`fallback`)."""
    existing = SPEC_ROOT / f"{code[:8]}-{slug(name)}.{variant}.json"
    ev = EVIDENCE_ROOT / code
    if existing.exists():
        rec["status"], rec["route"], rec["note"] = "drafted", _route_of(code), f"{existing} exists (kept; delete it to re-assemble)"
        ev0 = ev / "response-0-locate.json"
        if ev0.exists():
            r0 = json.loads(ev0.read_text())
            rec["pages"] = f"{r0.get('first_page')}-{r0.get('last_page')}" if r0.get("found") else ""
        return
    try:
        if (ev / "response-0-locate.json").exists():
            resp0 = json.loads((ev / "response-0-locate.json").read_text())
        else:
            resp0 = locate(code, pdf, ecospold_dir, dry_run, None, by)
        if resp0 is None:
            rec["status"], rec["note"] = "prompt-0-written", "answer prompt-0-locate.md, save as response-0-locate.json, rerun"
            return
        if not resp0["found"]:
            rec["status"], rec["note"] = "pages-not-found", resp0["reason"]
            if fallbacks:
                fallback(code, ecospold_dir, project, dry_run, by, rec, f"{pdf.name}: {resp0['reason']}", variant)
            return
        pages = f"{resp0['first_page']}-{resp0['last_page']}"
        rec["pages"] = pages
        if not (ev / "manifest.json").exists():
            evidence(code, pdf, pages, ecospold_dir, project)
        fr = {}
        if (ev / "response-1-extract.json").exists():
            fr["extract"] = ev / "response-1-extract.json"
        if (ev / "response-2-map.json").exists():
            fr["map"] = ev / "response-2-map.json"
        fr["by"] = by
        if dry_run and "extract" not in fr:
            draft(code, True, None, project, variant)
            rec["status"], rec["note"] = "prompt-1-written", "answer prompt-1-extract.md, save as response-1-extract.json, rerun"
            return
        if dry_run and "map" not in fr:
            draft(code, False, fr, project, variant)  # renders prompt 2 from the extract response, stops
            rec["status"], rec["note"] = "prompt-2-written", "answer prompt-2-map.md, save as response-2-map.json, rerun"
            return
        draft(code, False, fr if len(fr) > 1 else None, project, variant)
        rec["status"], rec["route"], rec["note"] = "drafted", "report", str(existing)
    except SystemExit as exc:
        rec["status"], rec["note"] = "error", str(exc)[:200]


def cited_reports(code: str, csv_source: str, pdf_by_title: dict, ecospold_dir: Path) -> list[str]:
    """Every report PDF this dataset cites that is present in the bundle.

    A dataset can cite more than one source, and the extra ones are only in the ecoSpold XML -
    results/system_terminated.csv carries a single "author | year | title" string. Taking just
    that one hid the 2025 plastics report behind all 14 PlasticsEurope datasets, the family with
    the largest downstream reach, which were recorded as having no report at all.
    """
    titles: list[str] = []
    if csv_source:
        titles.append(csv_source.split(" | ")[-1])
    xml = ecospold_dir / f"process_{code}.xml"
    if xml.exists():
        text = xml.read_text(encoding="utf-8", errors="replace")
        head = text[: text.find("<flowData")] if "<flowData" in text else text[:30000]
        titles += [html.unescape(t) for t in re.findall(r'<source\b[^>]*\btitle="([^"]*)"', head)]
    out: list[str] = []
    for t in dict.fromkeys(x for x in titles if x):
        pdf = pdf_by_title.get(t, "")
        if pdf and pdf not in out:
            out.append(pdf)
    return out


def draft_all(project: str, ecospold_dir: Path, reports: Path, dry_run: bool, only: set[str] | None, by: str,
              status_path: Path = Path("results/drafting_status.csv"),
              datasets: Path = Path("results/system_terminated_extended.csv"), fallbacks: bool = True) -> None:
    """One entry point for all system processes: find the report, locate the pages, extract,
    map, assemble - recording per dataset how far it got and why it stopped. Where no report prints
    the inventory, the template route and then the metadata route take over (``fallbacks``). With
    ``only``, just those rows of the status CSV are replaced."""
    import csv

    rows = list(csv.DictReader(open(datasets)))
    pdf_by_title = {r["title"]: r["pdf"] for r in csv.DictReader(open("results/sources.csv"))}
    status: list[dict] = []
    for r in rows:
        code, name = r["code"], r["name"]
        if only and code not in only and code[:8] not in only:
            continue
        rec = {"code": code, "name": name, "family": r.get("family", "") or r.get("detected_by", ""), "pdf": "", "pages": "",
               "status": "", "route": "", "note": ""}
        status.append(rec)
        title = r["source"].split(" | ")[-1] if r["source"] else ""
        candidates = [p for p in cited_reports(code, r["source"], pdf_by_title, ecospold_dir) if (reports / p).exists()]
        pdf_name = candidates[0] if candidates else ""
        if not pdf_name:
            existing = SPEC_ROOT / f"{code[:8]}-{slug(name)}.draft.json"
            reason = f"no report in the documentation bundle for '{title or 'no source'}'"
            if existing.exists():
                rec["status"], rec["route"], rec["note"] = "drafted", _route_of(code), f"{existing} exists (kept; delete it to re-assemble)"
            elif fallbacks:
                rec["status"], rec["note"] = "no-pdf", reason
                fallback(code, ecospold_dir, project, dry_run, by, rec, reason)
            else:
                rec["status"], rec["note"] = "no-pdf", f"family {r.get('family','') or r.get('detected_by','')}: {reason}"
            continue
        rec["pdf"] = pdf_name
        advance(code, name, reports / pdf_name, ecospold_dir, project, dry_run, by, rec, fallbacks=fallbacks)
    status_path.parent.mkdir(parents=True, exist_ok=True)
    rows_out = status
    if only and status_path.exists():  # a partial run replaces its own rows and keeps the rest
        done = {x["code"]: x for x in status}
        old = list(csv.DictReader(status_path.open()))
        rows_out = [done.pop(x["code"], x) for x in old] + list(done.values())
    fields = list(dict.fromkeys(k for x in rows_out for k in x))
    with status_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, restval="")
        w.writeheader(); w.writerows(rows_out)
    from collections import Counter
    print(f"\n{len(status)} datasets -> {status_path}")
    for k, n in Counter(x["status"] for x in status).most_common():
        print(f"  {n:3d}  {k}")


# ---------------------------------------------------------------- layer 3: assemble the spec
UNITS = {"kg": "kilogram", "MJ": "megajoule", "kWh": "kilowatt hour", "m3": "cubic meter", "tkm": "ton kilometer", "l": "litre",
         "unit": "unit", "m2": "square meter", "m": "meter", "t": "ton", "kBq": "kilo Becquerel"}



def _rebuilt_node(cands: dict, item: str, name: str, location: str) -> str:
    """If the chosen dataset is itself a system process and a rebuilt node of it exists in the sandbox,
    its code: "terminate on the database" prefers a unit process to a system process."""
    import bw2data as bd
    for e in cands.get(item, []):
        if e.get("name") == name and e.get("aggregated") and (not location or e.get("location") == location):
            for suffix in ("-disagg", "-draft-disagg"):
                try:
                    bd.get_node(database=db.SANDBOX_DB, code=e["code"] + suffix)
                    return e["code"] + suffix
                except Exception:
                    continue
    return ""


def _write_spec(code: str, meta: dict, variant: str, spec: dict) -> Path:
    SPEC_ROOT.mkdir(parents=True, exist_ok=True)
    out = SPEC_ROOT / f"{code[:8]}-{slug(meta['name'])}.{variant}.json"
    out.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")
    return out


def drafted_strategy(inputs: list[dict], ext: dict) -> dict:
    """Classify a drafted spec by what the report actually gave, not by the fact that a report was read.

    S1 (transcription, exports/README.md) means every input carries one printed number. A printed range
    ("Mischgranulat 15-30 %") is not enough: the fit picks the amount inside it, so the input list is
    the report's and some amounts are the calibrator's - that is S3, the same as an input the report
    names without any number ("an average European medium voltage mix (UCTE-mix) is used"). S2 is
    template transfer from an existing unit process and cannot arise here: this route starts from a
    report. Whether a printed table is this dataset's inventory or only comparison data cannot be told
    from the numbers; such drafts are relabelled S3 by hand (titanium dioxide, hydrogen cyanide).
    """
    fitted = [i for i in inputs if i.get("free")]
    untraceable = [i for i in fitted if not re.search(r"\d", ((i.get("derivation") or {}).get("quote") or ""))]
    counts = (f"{len(inputs) - len(fitted)} of {len(inputs)} inputs carry a printed amount, "
              f"{len(fitted) - len(untraceable)} a printed range, {len(untraceable)} no number in the report")
    if untraceable:
        counts += " (" + ", ".join(i["name"] for i in untraceable) + ")"
    if fitted:
        code, label = "S3", "top-down model drafted from the report excerpt by the LLM pipeline (reverse-bafu draft)"
    else:
        code, label = "S1", "transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft)"
    return {"code": code, "label": label,
            "note": f"basis: {ext['basis']}; allocation: {ext['allocation'] or 'none stated'}; {counts}. "
                    "Review every derivation; unreviewed entries have reviewed_by = null."}


def assemble(code: str, project: str, variant: str = "draft") -> Path:
    db.set_project(project)
    ev = EVIDENCE_ROOT / code
    meta = json.loads((ev / "target.json").read_text())
    man = json.loads((ev / "manifest.json").read_text())
    ext = json.loads((ev / "response-1-extract.json").read_text())
    mp = json.loads((ev / "response-2-map.json").read_text())
    prov1 = json.loads((ev / "provenance-1-extract.json").read_text())
    prov2 = json.loads((ev / "provenance-2-map.json").read_text())
    chosen = {m["item"]: m for m in mp["mappings"]}
    cands = json.loads((ev / "candidates-2-map.json").read_text()) if (ev / "candidates-2-map.json").exists() else {}
    scale = 1.0 / float(ext["basis_amount"] or 1.0)  # per basis -> per 1 target unit

    inputs, emissions, resources, skipped = [], [], [], []
    for it in ext["items"]:
        amount = it["raw_value"] * it["factor"] * scale
        deriv = {"evidence": man["report_text"]["file"], "quote": it["quote"], "raw_value": it["raw_value"], "raw_unit": it["raw_unit"],
                 "per": it["per"], "factor": it["factor"], "factor_unit": it["factor_unit"], "factor_source": it["factor_source"],
                 "scale_to_unit": scale, "confidence": it["confidence"], "by": prov1.get("by", "llm"), "reviewed_by": None}
        unit = UNITS.get(it["factor_unit"] or it["raw_unit"], it["factor_unit"] or it["raw_unit"])
        if it["kind"] == "input":
            m = chosen.get(it["name"])
            if not m or not m["chosen"]:
                skipped.append(f"{it['name']}: no dataset chosen ({m['reason'] if m else 'not mapped'})")
                continue
            entry = {"name": m["chosen"], "amount": amount, "unit": unit, "location": m["location"], "note": it["note"],
                     "derivation": {**deriv, "search": it["search"], "mapping_reason": m["reason"], "mapping_by": prov2.get("by", "llm")}}
            sb = _rebuilt_node(cands, it["name"], m["chosen"], m["location"]) if m.get("dependency") else ""
            if sb:
                entry["sandbox"] = sb
                entry["derivation"]["linked_rebuilt_node"] = sb
            if it["raw_min"] is not None and it["raw_max"] is not None and it["raw_min"] != it["raw_max"]:
                entry["free"] = True
                entry["bounds"] = [it["raw_min"] * it["factor"] * scale, it["raw_max"] * it["factor"] * scale]
            inputs.append(entry)
        elif it["kind"] in ("emission", "resource"):
            m = chosen.get(it["name"])
            if not m or not m["chosen"]:
                skipped.append(f"{it['name']}: no flow chosen ({m['reason'] if m else 'not mapped'})")
                continue
            entry = {"name": m["chosen"], "category": (m.get("compartment") or it["compartment"] or "air").split("/")[0].strip().lower().replace("emissions to ", ""),
                     "amount": amount, "unit": unit, "note": it["note"],
                     "derivation": {**deriv, "mapping_reason": m["reason"], "mapping_by": prov2.get("by", "llm")}}
            (emissions if it["kind"] == "emission" else resources).append(entry)
        else:
            skipped.append(f"{it['name']}: {it['kind']} — {it['note']}")
    spec = {
        "target": {"code": code, "name": meta["name"], "location": meta["location"]},
        "variant": variant,  # sandbox nodes get <code>-<variant>-disagg so a hand-written rebuild of the same target is kept
        "strategy": drafted_strategy(inputs, ext),
        "evidence": [{"source": man["report"]["file"], "where": f"pages {man['report']['pages']} -> {man['report_text']['file']}",
                      "note": f"report sha256 {man['report']['sha256'][:16]}…, text sha256 {man['report_text']['sha256'][:16]}…"}],
        "provenance": {"pipeline": "reverse-bafu draft", "evidence_manifest": str(ev / "manifest.json"), "extraction": prov1, "mapping": prov2,
                       "gaps_reported_by_model": ext["gaps"], "skipped_items": skipped, "assembled_at": _now()},
        "node": {"name": f"{meta['name']}, disaggregated", "unit": meta["unit"], "location": meta["location"],
                 "comment": f"drafted from {man['report']['file']} pp. {man['report']['pages']}",
                 **({"mass_sum": ext["mass_sum"] * scale} if ext.get("mass_sum") else {}),
                 "inputs": inputs, "emissions": emissions, "resources": resources},
    }
    out = _write_spec(code, meta, variant, spec)
    print(f"assembled -> {out}: {len(inputs)} inputs, {len(emissions)} emissions, {len(resources)} resources; skipped {len(skipped)}; gaps: {len(ext['gaps'])}")
    for s in skipped:
        print("  skipped:", s)
    return out


# ---------------------------------------------------------------- routes for datasets without a report table
# Most system processes have no report that prints their inventory (`pages-not-found`, `no-pdf`).
# The specs written in interactive sessions for them used two other kinds of evidence, and these two
# routes make that reproducible with the same audit trail as the report route:
#   3-template  S2: a unit process of the same product already in BAFU (other location, vintage or
#               grade). Candidates come from a deterministic name search; the model only picks one and
#               says which amounts may differ. The structure is copied, the main amounts are fitted
#               within 0.5-2x of the template.
#   4-metadata  S3: the dataset's own ecoSpold metadata and name name the inputs ("out of phosgene and
#   5-map       bisphenol A"); amounts come from the reaction equation or a mass balance, or are left
#               free. The inputs are then mapped to BAFU datasets with the report route's mapping prompt.
# `draft-all` tries them in that order when the report route stops.

TEMPLATE_SCHEMA = {
    "type": "object",
    "properties": {
        "chosen_code": {"type": ["string", "null"], "description": "the full code of the chosen candidate, or null"},
        "reason": {"type": "string"},
        "differences": {"type": "array", "items": {"type": "string"}},
        "free_inputs": {"type": "array", "items": {"type": "string"}, "description": "template input names, exactly as listed"},
        "electricity_location": {"type": ["string", "null"]},
        "gaps": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["chosen_code", "reason", "differences", "free_inputs", "electricity_location", "gaps"],
    "additionalProperties": False,
}
METADATA_ITEM = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "field": {"type": "string", "enum": ["name", "technology", "includedProcesses", "generalComment"]},
        "quote": {"type": "string"},
        "basis": {"type": "string", "enum": ["stoichiometry", "mass-balance", "composition-split", "named-only", "implied"]},
        "amount": {"type": ["number", "null"], "description": "per 1 unit of product; null for composition-split and named-only"},
        "unit": {"type": "string"},
        "equation": {"type": "string"},
        "calculation": {"type": "string"},
        "search": {"type": "string"},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "note": {"type": "string"},
    },
    "required": ["name", "field", "quote", "basis", "amount", "unit", "equation", "calculation", "search", "confidence", "note"],
    "additionalProperties": False,
}
METADATA_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {"type": "array", "items": METADATA_ITEM},
        "mass_sum": {"type": ["number", "null"]},
        "utility_block": {"type": "boolean"},
        "gaps": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["items", "mass_sum", "utility_block", "gaps"],
    "additionalProperties": False,
}
# The five-line utility block every ecoinvent-v2 organic-chemical unit process in BAFU-2026 carries
# (checked exchange by exchange on Cumene and Ethyl benzene, at plant). Added as free inputs, starting
# at these values: a template, not evidence. (name, location, unit, amount, per, bounds); "precursor"
# means per kilogram of the fixed kilogram inputs.
UTILITY_BLOCK = (
    ("Electricity, medium voltage, production ENTSO-E, at grid", "ENTSO-E", "kilowatt hour", 0.333, "product", None),
    ("Heat, natural gas, at industrial furnace 1MW", "CH", "megajoule", 2.0, "product", None),
    ("Transport, freight, rail", "RER", "ton kilometer", 0.6, "precursor", None),
    ("Transport, freight, lorry, fleet average", "RER", "ton kilometer", 0.1, "precursor", None),
    ("Chemical plant, organics", "RER", "unit", 4.0e-10, "product", (0.0, 4.0e-10)),
)


def product_stem(name: str) -> str:
    """The product part of a dataset name: without the 'xx' marks and the ', at plant' / ', at regional
    storage' / ', production mix' segments."""
    s = re.sub(r"^\s*x+\s+", "", name, flags=re.I)
    keep = [p.strip() for p in s.split(",") if p.strip() and not re.match(r"(at|production mix|from|to)\b", p.strip(), re.I)]
    return ", ".join(keep) or s.strip()


def template_candidates(code: str, meta: dict, k: int = 8) -> list[dict]:
    """Unit processes of the same product: the first segment of the product name must be the target's
    exactly. Deterministic; ranked by how much of the rest of the product name they share (grade,
    colour), then the reference unit, then location preference."""
    import bw2data as bd

    stem = product_stem(meta["name"])
    head = [w for w in re.findall(r"[a-z0-9]+", stem.split(",")[0].lower()) if len(w) > 1]
    rest = set(re.findall(r"[a-z0-9]+", stem.lower())) - set(head)
    if not head:
        return []
    order = {loc: i for i, loc in enumerate(dict.fromkeys([meta["location"], *db.LOCATION_PREFERENCE]))}
    hits = []
    for norm, entries in db.activity_index().items():
        if _matched(head, norm) < len(head):
            continue
        for e in entries:
            if e["code"] == code or e["aggregated"] or not e["n_inputs"]:
                continue
            # the same product, not a longer name that contains it ("Propylene glycol" for "Propylene")
            if re.findall(r"[a-z0-9]+", product_stem(e["name"]).split(",")[0].lower()) != head:
                continue
            words = set(re.findall(r"[a-z0-9]+", e["name"].lower()))
            hits.append((len(rest - words), 0 if e["unit"] == meta["unit"] else 1, order.get(e["location"], 99),
                         e["name"], e["location"], e["code"], e))
    hits.sort(key=lambda t: t[:6])
    out = []
    for t in hits[:k]:
        e = dict(t[6])
        node = bd.get_node(database=db.INVENTORY_DB, code=e["code"])
        ins = [x for x in node.technosphere() if x.input.key != node.key]
        e["inputs"] = [{"name": x.input["name"], "location": x.input.get("location", ""), "amount": x["amount"], "unit": x.input.get("unit", "")}
                       for x in ins]
        out.append(e)
    return out


def _step(ev: Path, tag: str, prompt: str, schema: dict, dry_run: bool, by: str) -> tuple[dict | None, dict | None]:
    """One model step: write the prompt and schema; ingest response-<tag>.json if it is there (answered
    outside the API), else call the model, else (dry run) stop."""
    (ev / f"prompt-{tag}.md").write_text(prompt)
    (ev / f"schema-{tag}.json").write_text(json.dumps(schema, indent=1))
    rp, pp = ev / f"response-{tag}.json", ev / f"provenance-{tag}.json"
    if rp.exists():
        resp = _load_response(rp, schema, tag)
        if pp.exists():
            prov = json.loads(pp.read_text())
        else:
            prov = {"model": "manual", "by": by, "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(), "at": _now()}
            pp.write_text(json.dumps(prov, indent=1))
        return resp, prov
    if dry_run:
        return None, None
    resp, prov = call_model(prompt, schema, tag)
    rp.write_text(json.dumps(resp, indent=1, ensure_ascii=False))
    pp.write_text(json.dumps(prov, indent=1))
    return resp, prov


def _meta_fields(meta: dict, reason: str) -> dict:
    return {"target_name": meta["name"], "target_location": meta["location"], "target_unit": meta["unit"], "n_flows": meta["n_flows"],
            "target_category": meta["category"], "included_processes": meta["includedProcesses"] or "—",
            "technology": meta["technology"] or "—", "general_comment": meta["generalComment"] or "—",
            "no_report_reason": " ".join(reason.split())[:700] or "no report in the documentation bundle"}


def fallback(code: str, ecospold_dir: Path, project: str, dry_run: bool, by: str, rec: dict, reason: str, variant: str = "draft") -> None:
    """Routes 3 (template) and 4-5 (metadata) for a dataset whose reports print no inventory. Fills rec
    like `advance`."""
    ev = EVIDENCE_ROOT / code
    ev.mkdir(parents=True, exist_ok=True)
    db.set_project(project)
    if not (ev / "target.json").exists():
        xml = write_target(ev, code, ecospold_dir, project)
        (ev / "manifest-meta.json").write_text(json.dumps({"code": code, "created": _now(), "ecospold": {"file": xml.name, "sha256": sha256(xml)},
                                                           "brightway_project": project, "no_report_reason": reason}, indent=1))
    meta = json.loads((ev / "target.json").read_text())
    fields = _meta_fields(meta, reason)
    try:
        cands = template_candidates(code, meta)
        (ev / "candidates-3-template.json").write_text(json.dumps(cands, indent=1, ensure_ascii=False))
        if cands:
            listing = "\n".join(
                f"- code: {c['code']}\n  {c['name']} [{c['location']}], 1 {c['unit']}, {c['n_inputs']} technosphere inputs\n"
                + "\n".join(f"    · {i['name']} [{i['location']}]: {i['amount']:.4g} {i['unit']}" for i in c["inputs"][:30])
                + (f"\n    · … {len(c['inputs']) - 30} more" if len(c["inputs"]) > 30 else "")
                for c in cands)
            r3, _ = _step(ev, "3-template", render(PROMPTS / "draft_from_template.md", **fields, candidates=listing), TEMPLATE_SCHEMA, dry_run, by)
            if r3 is None:
                rec["status"], rec["route"], rec["note"] = "prompt-3-written", "template", "answer prompt-3-template.md, save as response-3-template.json, rerun"
                return
            if r3["chosen_code"]:
                if r3["chosen_code"] not in {c["code"] for c in cands}:
                    raise SystemExit(f"template: {r3['chosen_code']} is not one of the listed candidates")
                out = assemble_template(code, project, variant)
                rec["status"], rec["route"], rec["note"] = "drafted", "template", str(out)
                return
        r4, _ = _step(ev, "4-metadata", render(PROMPTS / "draft_from_metadata.md", **fields), METADATA_SCHEMA, dry_run, by)
        if r4 is None:
            rec["status"], rec["route"], rec["note"] = "prompt-4-written", "metadata", "answer prompt-4-metadata.md, save as response-4-metadata.json, rerun"
            return
        if not r4["items"]:
            rec["status"], rec["route"], rec["note"] = "no-usable-evidence", "", "; ".join(r4["gaps"])[:300] or "the metadata names no input"
            return
        p5, cands5 = mapping_prompt({"items": [{**it, "kind": "input"} for it in r4["items"]]}, meta["location"])
        (ev / "candidates-5-map.json").write_text(json.dumps(cands5, indent=1, ensure_ascii=False))
        r5, _ = _step(ev, "5-map", p5, MAPPING_SCHEMA, dry_run, by)
        if r5 is None:
            rec["status"], rec["route"], rec["note"] = "prompt-5-written", "metadata", "answer prompt-5-map.md, save as response-5-map.json, rerun"
            return
        out = assemble_metadata(code, project, variant)
        rec["status"], rec["route"], rec["note"] = "drafted", "metadata", str(out)
    except SystemExit as exc:
        rec["status"], rec["note"] = "error", str(exc)[:200]


def assemble_template(code: str, project: str, variant: str = "draft") -> Path:
    """Route 3: copy the chosen template's inputs and direct flows; free the named main inputs within
    0.5-2x of the template amount. Direct flows keep the template's exact compartment path as their
    resolve hint, so they land on the template's own sub-compartment."""
    import bw2data as bd

    db.set_project(project)
    ev = EVIDENCE_ROOT / code
    meta = json.loads((ev / "target.json").read_text())
    r3 = json.loads((ev / "response-3-template.json").read_text())
    prov = json.loads((ev / "provenance-3-template.json").read_text())
    tpl = bd.get_node(database=db.INVENTORY_DB, code=r3["chosen_code"])
    free, switch = set(r3["free_inputs"]), r3["electricity_location"]
    idx = db.activity_index()
    inputs, emissions, resources = [], [], []
    for x in tpl.technosphere():
        a = x.input
        if a.key == tpl.key:
            continue
        name, loc, unit, amt = a["name"], a.get("location", ""), a.get("unit", ""), float(x["amount"])
        note = f"template {name} [{loc}]"
        if switch and name.lower().startswith("electricity") and loc != switch and any(e["location"] == switch for e in idx.get(db._norm(name), [])):
            note += f", switched to {switch}"
            loc = switch
        entry = {"name": name, "amount": amt, "unit": unit, "location": loc, "note": note,
                 "derivation": {"evidence": f"template {tpl['name']} [{tpl.get('location', '')}] ({r3['chosen_code']})", "template_amount": amt,
                                "by": prov.get("by", "llm"), "reviewed_by": None}}
        if name in free and amt:
            lo, hi = sorted((0.5 * amt, 2.0 * amt))
            entry.update(free=True, bounds=[lo, hi])
        inputs.append(entry)
    for x in tpl.biosphere():
        f = x.input
        cats = " / ".join(str(c) for c in (f.get("categories") or ()))
        entry = {"name": f["name"], "category": cats, "amount": float(x["amount"]), "unit": f.get("unit", ""), "note": "direct flow of the template"}
        (resources if f.get("type") == "natural resource" or cats.lower().startswith(("natural resource", "resource")) else emissions).append(entry)
    unmatched = sorted(free - {i["name"] for i in inputs})
    spec = {
        "target": {"code": code, "name": meta["name"], "location": meta["location"]},
        "variant": variant,
        "strategy": {"code": "S2", "label": f"template transfer drafted by the LLM pipeline from {tpl['name']} [{tpl.get('location', '')}]",
                     "note": f"{r3['reason']} Differences: {' '.join(r3['differences']) or 'none stated'} "
                             f"{sum(1 for i in inputs if i.get('free'))} of {len(inputs)} amounts free within 0.5-2x of the template. "
                             "Review the choice of template; unreviewed entries have reviewed_by = null."},
        "evidence": [{"source": f"bafu-2026: {tpl['name']} [{tpl.get('location', '')}] (unit process, {len(inputs)} inputs)", "where": "template transfer (S2)",
                      "note": f"{EVIDENCE_ROOT / code}/prompt-3-template.md and response-3-template.json"}],
        "provenance": {"pipeline": "reverse-bafu draft-all, template route", "template_code": r3["chosen_code"], "choice": prov,
                       "gaps_reported_by_model": r3["gaps"], "free_inputs_not_in_template": unmatched, "assembled_at": _now()},
        "node": {"name": f"{meta['name']}, disaggregated", "unit": meta["unit"], "location": meta["location"],
                 "comment": "Structure taken from the template unit process; amounts calibrated against the aggregated vector within bounds.",
                 "inputs": inputs, "emissions": emissions, "resources": resources},
    }
    out = _write_spec(code, meta, variant, spec)
    print(f"assembled (template) -> {out}: {len(inputs)} inputs ({sum(1 for i in inputs if i.get('free'))} free), {len(emissions)} emissions, {len(resources)} resources")
    for u in unmatched:
        print("  free input not in the template:", u)
    return out


def assemble_metadata(code: str, project: str, variant: str = "draft") -> Path:
    """Routes 4-5: the inputs the metadata names, mapped to BAFU datasets. Amounts fixed by chemistry
    or a mass balance stay fixed; a composition split is fitted under the mass constraint; inputs named
    without an amount, and the standard utility block, are fitted freely."""
    db.set_project(project)
    ev = EVIDENCE_ROOT / code
    meta = json.loads((ev / "target.json").read_text())
    r4 = json.loads((ev / "response-4-metadata.json").read_text())
    r5 = json.loads((ev / "response-5-map.json").read_text())
    prov4 = json.loads((ev / "provenance-4-metadata.json").read_text())
    prov5 = json.loads((ev / "provenance-5-map.json").read_text())
    cands = json.loads((ev / "candidates-5-map.json").read_text()) if (ev / "candidates-5-map.json").exists() else {}
    chosen = {m["item"]: m for m in r5["mappings"]}
    split = [it for it in r4["items"] if it["basis"] == "composition-split"]
    mass_sum = (r4["mass_sum"] or 1.0) if split else None
    inputs, skipped, notes = [], [], []
    precursor_kg = mass_sum or 0.0
    for it in r4["items"]:
        m = chosen.get(it["name"])
        if not m or not m["chosen"]:
            skipped.append(f"{it['name']}: no dataset chosen ({m['reason'] if m else 'not mapped'})")
            continue
        unit = UNITS.get(it["unit"], it["unit"]) or "kilogram"
        entry = {"name": m["chosen"], "unit": unit, "location": m["location"], "note": it["note"],
                 "derivation": {"evidence": f"ecoSpold metadata, {it['field']}", "quote": it["quote"], "basis": it["basis"],
                                "equation": it["equation"], "calculation": it["calculation"], "confidence": it["confidence"],
                                "by": prov4.get("by", "llm"), "reviewed_by": None, "search": it["search"],
                                "mapping_reason": m["reason"], "mapping_by": prov5.get("by", "llm")}}
        if it["basis"] in ("stoichiometry", "mass-balance", "implied") and it["amount"] is not None:
            entry["amount"] = float(it["amount"])
            if unit == "kilogram":
                precursor_kg += float(it["amount"])
        elif it["basis"] == "composition-split":
            entry.update(amount=mass_sum / len(split), free=True, bounds=[0.0, mass_sum])
        else:
            entry.update(amount=0.0, free=True)
            if unit == "kilogram" and split:
                notes.append(f"{it['name']} is a free kilogram input and falls under the mass constraint of the composition split; check it")
        sb = _rebuilt_node(cands, it["name"], m["chosen"], m["location"]) if m.get("dependency") else ""
        if sb:
            entry["sandbox"] = sb
            entry["derivation"]["linked_rebuilt_node"] = sb
        inputs.append(entry)
    per_kg = UNITS.get(meta["unit"], meta["unit"]) == "kilogram"   # the ecoSpold XML says "kg"
    if r4["utility_block"]:
        if per_kg:
            for name, loc, unit, amt, per, bounds in UTILITY_BLOCK:
                start = amt * (precursor_kg if per == "precursor" else 1.0)
                entry = {"name": name, "amount": start, "unit": unit, "location": loc, "free": True,
                         "note": f"standard ecoinvent-v2 chemical utility block: starting value {amt:g} {unit} per "
                                 f"{'kg of precursor' if per == 'precursor' else 'kg of product'}; a template, not evidence, and fitted",
                         "derivation": {"evidence": "utility block of the ecoinvent-v2 organic chemicals in BAFU-2026", "basis": "template",
                                        "by": "reverse-bafu draft-all", "reviewed_by": None}}
                if bounds:
                    entry["bounds"] = list(bounds)
                inputs.append(entry)
        else:
            notes.append(f"utility block requested but the product unit is {meta['unit']}, not kilogram; not added")
    counts = {b: sum(1 for it in r4["items"] if it["basis"] == b) for b in ("stoichiometry", "mass-balance", "composition-split", "named-only", "implied")}
    spec = {
        "target": {"code": code, "name": meta["name"], "location": meta["location"]},
        "variant": variant,
        "strategy": {"code": "S3", "label": "top-down model drafted from the dataset's own metadata by the LLM pipeline (reverse-bafu draft-all, metadata route)",
                     "note": "No report prints this dataset's inventory; the input list comes from its ecoSpold metadata and name. Amount basis: "
                             + ", ".join(f"{n} {b}" for b, n in counts.items() if n)
                             + (f"; mass constraint {mass_sum:g} {meta['unit']}" if mass_sum else "")
                             + ("; standard utility block added, fitted" if r4["utility_block"] and per_kg else "")
                             + ". Review every derivation; unreviewed entries have reviewed_by = null."},
        "evidence": [{"source": "BAFU-2026 ecoSpold metadata of the target", "where": "name, processInformation/technology, referenceFunction/includedProcesses",
                      "note": f"{EVIDENCE_ROOT / code}/prompt-4-metadata.md and response-4-metadata.json"}],
        "provenance": {"pipeline": "reverse-bafu draft-all, metadata route", "extraction": prov4, "mapping": prov5,
                       "gaps_reported_by_model": r4["gaps"], "skipped_items": skipped, "warnings": notes, "assembled_at": _now()},
        "node": {"name": f"{meta['name']}, disaggregated", "unit": meta["unit"], "location": meta["location"],
                 "comment": "drafted from the dataset's own ecoSpold metadata",
                 **({"mass_sum": mass_sum} if mass_sum else {}),
                 "inputs": inputs, "emissions": [], "resources": []},
    }
    out = _write_spec(code, meta, variant, spec)
    print(f"assembled (metadata) -> {out}: {len(inputs)} inputs ({sum(1 for i in inputs if i.get('free'))} free); skipped {len(skipped)}; gaps: {len(r4['gaps'])}")
    for s in skipped + notes:
        print("  ", s)
    return out
