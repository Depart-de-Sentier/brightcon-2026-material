#!/usr/bin/env python
"""Export every rebuilt unit process to a self-describing, version-controlled JSON (+ a flat CSV).

    uv run python scripts/export_disaggregated.py --project bafu-2026 [--out exports]

What it writes
--------------
``exports/disaggregated_bafu2026.json``   the exchange-level export, documented in exports/README.md
``exports/disaggregated_bafu2026_exchanges.csv``  the same exchanges, one per row, for eyeballing

Where the content comes from
----------------------------
The *specs* are the source of truth: after ``reverse-bafu run-all --apply`` every spec carries the
resolved supplier code of each input, the resolved EF 3.1 / residual flow code of each elementary
flow, and the calibrated amounts - plus, for specs produced by the drafting pipeline, a per-entry
``derivation`` (report, quoted line, raw value, conversion factor, mapping reason, author).

Two things the spec does not hold and that are read from the Brightway sandbox instead:

* the residual block of the hybrid node - the flow-by-flow difference between the original
  system process and the explicit model, which is what makes the hybrid reproduce the original
  exactly. It exists only as exchanges on ``<prefix>-hybrid``.
* the ``categories`` of each elementary flow, for readability.

The export therefore needs the Brightway project the rebuild ran in. Nothing is recomputed here;
if a number is not in the spec or in the sandbox it is not in the export.
"""

from __future__ import annotations

import argparse
import csv
import datetime as _dt
import json
import subprocess
from pathlib import Path

import bw2data as bd

from reverse_bafu import db, spec as specmod

SCHEMA_VERSION = "1.0"
DEFAULT_OUT = Path("exports")
JSON_NAME = "disaggregated_bafu2026.json"
CSV_NAME = "disaggregated_bafu2026_exchanges.csv"

CITATION = ("Source: Life Cycle Inventory database of the Swiss Federal Administration, BAFU:2026. "
            "The disaggregated unit processes in this file are a reconstruction by the reverse-bafu "
            "project from the public LCI reports of the BAFU-2026 documentation bundle; they are not "
            "part of BAFU-2026 and carry no endorsement by BAFU.")

QUALITY_FIELDS = ("status", "top_flows_within_10pct", "top_flow_median_abs_delta_pct", "kg_mass_covered_pct",
                  "flows_within_10pct", "flows_within_10pct_share", "flow_median_abs_delta_pct",
                  "flows_missing", "report")


def _git_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return ""


def _flow_meta(database: str, code: str) -> dict:
    """name / categories / unit of an elementary flow, as the biosphere database has them."""
    try:
        n = bd.get_node(database=database, code=code)
    except Exception:
        return {}
    return {"flow_name": n.get("name", ""), "categories": list(n.get("categories") or []), "unit": n.get("unit", "")}


def _supplier_meta(code: str) -> dict:
    try:
        n = bd.get_node(database=db.INVENTORY_DB, code=code)
    except Exception:
        return {}
    return {"supplier_name": n.get("name", ""), "supplier_location": n.get("location", ""),
            "supplier_unit": n.get("unit", "")}


def _derivation(raw: dict) -> dict | None:
    d = raw.get("derivation")
    if not d:
        return None
    keep = ("evidence", "quote", "raw_value", "raw_unit", "per", "factor", "factor_unit", "factor_source",
            "scale_to_unit", "search", "mapping_reason", "confidence", "by", "reviewed_by",
            "linked_rebuilt_node")
    return {k: d[k] for k in keep if k in d}


def _node_payload(sp: specmod.Spec, node: specmod.Node, node_code: str, self_codes: set[str]) -> dict:
    """One rebuilt unit process as plain JSON."""
    techno = []
    for i in node.inputs:
        if i.node:                                   # a nested node this same spec builds
            target_code, role = f"{specmod.node_prefix(sp)}-{specmod.slug(i.node.name)}", "this-export"
        elif i.sandbox:                              # a node an earlier spec rebuilt
            target_code, role = i.sandbox, "this-export"
        else:
            target_code, role = i.code, "bafu"
        entry = {
            "supplier_code": target_code,
            "supplier_database_role": role,          # "bafu" = the user's bafu-2026; "this-export" = a node in this file
            "supplier_name_in_spec": i.name,
            "supplier_location": i.location,
            "amount": i.amount,
            "unit": i.unit,
            "calibrated": bool(i.free),              # True: the amount was fitted, not read off the report
            "bounds": list(i.bounds) if i.bounds else None,
            "comment": i.note,
        }
        if role == "bafu":
            entry.update(_supplier_meta(i.code))
        prov = _derivation(i.raw)
        if prov:
            entry["provenance"] = prov
        techno.append(entry)

    bio = []
    for f, kind in [(f, "emission") for f in node.emissions] + [(f, "resource") for f in node.resources]:
        entry = {
            "flow_code": f.code,
            "flow_database": f.database,
            "flow_name_in_spec": f.name,
            "compartment_hint": f.category,
            "kind": kind,
            "amount": f.amount,
            "unit": f.unit,
            "comment": f.note,
        }
        entry.update(_flow_meta(f.database, f.code))
        prov = _derivation(f.raw)
        if prov:
            entry["provenance"] = prov
        bio.append(entry)

    return {
        "node_code": node_code,
        "name": node.name,
        "location": node.location or sp.node.location,
        "unit": node.unit,
        "reference_product": node.name,
        "comment": node.comment,
        "technosphere": techno,
        "biosphere": bio,
    }


def _residual(prefix: str) -> dict | None:
    """The hybrid node's residual flows, read back from the sandbox (they exist nowhere else)."""
    try:
        hyb = bd.get_node(database=db.SANDBOX_DB, code=f"{prefix}-hybrid")
    except Exception:
        return None
    flows = []
    for ex in hyb.exchanges():
        if ex.get("type") != "biosphere" or "residual" not in (ex.get("comment") or ""):
            continue
        inp = ex.input
        flows.append({"flow_code": inp["code"], "flow_database": inp["database"], "flow_name": inp.get("name", ""),
                      "categories": list(inp.get("categories") or []), "amount": ex["amount"],
                      "unit": inp.get("unit", "")})
    flows.sort(key=lambda f: -abs(f["amount"]))
    return {
        "node_code": f"{prefix}-hybrid",
        "name": hyb["name"],
        "unit": hyb.get("unit", ""),
        "location": hyb.get("location", ""),
        "n_flows": len(flows),
        "note": ("Hybrid node: the explicit exchanges above plus these residual elementary flows, so that the "
                 "cumulative inventory of the hybrid node equals the original BAFU system process exactly. "
                 "The residual is what the explicit model does NOT yet explain."),
        "flows": flows,
    }


def export(project: str, out_dir: Path, status_csv: Path, with_residual: bool = True) -> Path:
    db.set_project(project)
    rows = [r for r in csv.DictReader(status_csv.open()) if r.get("status") == "rebuilt"]
    if not rows:
        raise SystemExit(f"no rebuilt datasets in {status_csv}")

    datasets, missing = [], []
    self_codes: set[str] = set()
    for r in rows:
        sp = specmod.load(r["spec"])
        prefix = specmod.node_prefix(sp)
        self_codes.add(f"{prefix}-disagg")

    for r in rows:
        sp = specmod.load(r["spec"])
        prefix = specmod.node_prefix(sp)
        nodes = []
        for node in specmod.walk(sp.node):
            code = f"{prefix}-disagg" if node is sp.node else f"{prefix}-{specmod.slug(node.name)}"
            nodes.append(_node_payload(sp, node, code, self_codes))
        main = nodes[-1] if nodes and nodes[-1]["node_code"].endswith("-disagg") else nodes[0]
        for n in nodes:
            for e in n["technosphere"]:
                if not e["supplier_code"]:
                    missing.append(f"{sp.target_code}: input {e['supplier_name_in_spec']!r} has no resolved code")
            for e in n["biosphere"]:
                if not e["flow_code"]:
                    missing.append(f"{sp.target_code}: flow {e['flow_name_in_spec']!r} has no resolved code")
        datasets.append({
            "bafu_code": sp.target_code,
            "bafu_name": sp.target_name,
            "replaces": {"database": db.INVENTORY_DB, "code": sp.target_code, "name": sp.target_name,
                         "note": "the aggregated ('system terminated') BAFU-2026 dataset this unit process rebuilds"},
            "variant": sp.variant,
            "spec": str(sp.path),
            "strategy": sp.strategy,
            "evidence": sp.evidence,
            "quality": {k: r.get(k, "") for k in QUALITY_FIELDS},
            "provenance": {k: v for k, v in (sp.raw.get("provenance") or {}).items()
                           if k in ("pipeline", "extraction", "mapping", "gaps_reported_by_model",
                                    "skipped_items", "assembled_at", "evidence_manifest")},
            "note": sp.raw.get("note", ""),
            "nodes": nodes,
            "main_node_code": main["node_code"],
            "residual": _residual(prefix) if with_residual else None,
        })

    if missing:
        raise SystemExit("refusing to export - unresolved references:\n  " + "\n  ".join(missing))

    payload = {
        "schema": "reverse-bafu/disaggregated-bafu-2026",
        "schema_version": SCHEMA_VERSION,
        "generated_at": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "generated_by": "scripts/export_disaggregated.py",
        "git_commit": _git_commit(),
        "source_project": project,
        "links_against": {
            "inventory_database": db.INVENTORY_DB,
            "biosphere_databases": list(db.BIOSPHERE_DBS),
            "note": ("Every technosphere exchange names the BAFU-2026 code of its supplier; every elementary "
                     "flow names its code AND the database it came from. The importer resolves those codes in "
                     "the target project and refuses to write anything if one is missing."),
        },
        "strategies": {
            "S1": "transcription - the report prints this dataset's own inventory, one printed number per technosphere input",
            "S2": "template transfer - a unit process of the same product exists (another site, grade or version); its structure reused, amounts calibrated",
            "S3": "top-down model - the evidence names the inputs but not every amount; feedstock from the reaction equation, the rest calibrated",
        },
        "citation": CITATION,
        "n_datasets": len(datasets),
        "datasets": datasets,
    }

    out_dir.mkdir(parents=True, exist_ok=True)
    out_json = out_dir / JSON_NAME
    out_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=False) + "\n")

    with (out_dir / CSV_NAME).open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["bafu_code", "bafu_name", "strategy", "node_code", "node_name", "node_unit", "node_location",
                    "exchange_type", "target_code", "target_database_role", "target_name", "target_location",
                    "amount", "unit", "calibrated", "quote"])
        for d in payload["datasets"]:
            for n in d["nodes"]:
                for e in n["technosphere"]:
                    w.writerow([d["bafu_code"], d["bafu_name"], d["strategy"].get("code", ""), n["node_code"],
                                n["name"], n["unit"], n["location"], "technosphere", e["supplier_code"],
                                e["supplier_database_role"], e.get("supplier_name", e["supplier_name_in_spec"]),
                                e["supplier_location"], e["amount"], e["unit"], e["calibrated"],
                                (e.get("provenance") or {}).get("quote", "")])
                for e in n["biosphere"]:
                    w.writerow([d["bafu_code"], d["bafu_name"], d["strategy"].get("code", ""), n["node_code"],
                                n["name"], n["unit"], n["location"], e["kind"], e["flow_code"], e["flow_database"],
                                e.get("flow_name", e["flow_name_in_spec"]),
                                "/".join(e.get("categories") or []), e["amount"], e["unit"], "",
                                (e.get("provenance") or {}).get("quote", "")])
            # the residual blocks are deliberately NOT in the CSV: ~31,000 rows of BAFU flow amounts
            # would bury the 300 explicit exchanges this file exists to make readable. They are in the JSON.

    n_ex = sum(len(n["technosphere"]) + len(n["biosphere"]) for d in datasets for n in d["nodes"])
    n_res = sum(d["residual"]["n_flows"] for d in datasets if d["residual"])
    print(f"{len(datasets)} datasets, {sum(len(d['nodes']) for d in datasets)} nodes, "
          f"{n_ex} explicit exchanges, {n_res} residual flows")
    print(f"-> {out_json}")
    print(f"-> {out_dir / CSV_NAME}")
    return out_json


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project", default="bafu-2026", help="Brightway project the rebuild ran in")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--status", type=Path, default=Path("results/rebuild_status.csv"))
    ap.add_argument("--no-residual", action="store_true",
                    help="omit the residual blocks. They are the original BAFU inventory vector minus the "
                         "explicit model, i.e. they carry BAFU-2026 numbers; leave them out if you may not "
                         "redistribute those. Without them only the explicit nodes can be imported.")
    a = ap.parse_args()
    export(a.project, a.out, a.status, with_residual=not a.no_residual)


if __name__ == "__main__":
    main()
