#!/usr/bin/env python
"""Add the exported disaggregated BAFU-2026 unit processes to an existing Brightway project.

    python scripts/import_disaggregated.py --project my-project \
        [--file exports/disaggregated_bafu2026.json] \
        [--database bafu-2026-disaggregated] \
        [--bafu-db bafu-2026] [--biosphere ef-3.1-biosphere --biosphere bafu-2026-residual] \
        [--include explicit|hybrid|both] [--dry-run] [--overwrite]

It writes ONE new database. Nothing in the project is modified: the original aggregated BAFU
datasets stay exactly as they are, and the new unit processes link *to* them for their supply chain.

Linking is by code, never by name:
  * every technosphere exchange carries the BAFU-2026 code of its supplier;
  * every elementary flow carries its code and the biosphere database it came from;
  * exchanges between two rebuilt datasets stay inside the new database.

If any referenced code is missing in the target project the import stops before writing anything
and prints every missing reference, with the dataset and exchange that wanted it.

What lands in the database (``--include``)
  explicit  only the ``*-disagg`` nodes: the evidence-based model, and nothing else. Its
            cumulative inventory is NOT equal to the original - see exports/README.md.
  hybrid    the ``*-hybrid`` nodes: the same exchanges plus the residual elementary flows, so the
            cumulative inventory reproduces the original system process exactly. Any explicit
            node another node links to is imported too, because it is needed as a link target.
  both      (default) both, so you can compare them.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import bw2data as bd

DEFAULT_FILE = Path("exports/disaggregated_bafu2026.json")
DEFAULT_DB = "bafu-2026-disaggregated"


class MissingReferences(SystemExit):
    pass


def _code_index(database: str) -> set[str]:
    """Every code in a database. Fast enough (one .load()) and avoids a query per exchange."""
    return {k[1] for k in bd.Database(database).load()}


def load_export(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"export file not found: {path}\nRun scripts/export_disaggregated.py first.")
    payload = json.loads(path.read_text())
    if payload.get("schema") != "reverse-bafu/disaggregated-bafu-2026":
        raise SystemExit(f"{path} is not a reverse-bafu disaggregation export (schema={payload.get('schema')!r})")
    major = str(payload.get("schema_version", "0")).split(".")[0]
    if major != "1":
        raise SystemExit(f"{path} has schema_version {payload.get('schema_version')!r}; this importer reads 1.x")
    return payload


def plan(payload: dict, target_db: str, bafu_db: str, biosphere_dbs: list[str], include: str) -> tuple[dict, list[str]]:
    """Build the bw2data dict and collect every reference that does not exist. Writes nothing."""
    bafu_codes = _code_index(bafu_db)
    bio_codes = {name: _code_index(name) for name in biosphere_dbs}
    # an exported flow names the database it came from; accept it there, else anywhere the user gave us
    def find_flow(code: str, preferred: str) -> str | None:
        if preferred in bio_codes and code in bio_codes[preferred]:
            return preferred
        for name, codes in bio_codes.items():
            if code in codes:
                return name
        return None

    want_explicit = include in ("explicit", "both")
    want_hybrid = include in ("hybrid", "both")

    exported_node_codes = {n["node_code"] for d in payload["datasets"] for n in d["nodes"]}
    # nodes another node links to ("this-export"): they must exist even when only hybrids are wanted
    referenced = {e["supplier_code"]
                  for d in payload["datasets"] for n in d["nodes"] for e in n["technosphere"]
                  if e["supplier_database_role"] == "this-export"}
    data: dict = {}
    missing: list[str] = []

    for d in payload["datasets"]:
        label = f"{d['bafu_name']} ({d['bafu_code'][:8]})"
        base_comment = (f"reverse-bafu rebuild of BAFU-2026 dataset {d['bafu_code']} "
                        f"({d['bafu_name']}), strategy {d['strategy'].get('code', '?')}. "
                        + "; ".join(f"{e.get('source', '')} {e.get('where', '')}".strip() for e in d["evidence"]))

        def exchanges_for(node: dict, own_code: str) -> list[dict]:
            ex = [{"input": (target_db, own_code), "amount": 1.0, "type": "production",
                   "unit": node["unit"]}]
            for e in node["technosphere"]:
                code = e["supplier_code"]
                if e["supplier_database_role"] == "this-export":
                    if code not in exported_node_codes:
                        missing.append(f"{label}: technosphere -> rebuilt node {code!r} is not in this export file")
                        continue
                    key = (target_db, code)
                else:
                    if code not in bafu_codes:
                        missing.append(f"{label}: technosphere -> {bafu_db} code {code!r} "
                                       f"({e.get('supplier_name') or e['supplier_name_in_spec']}) not found")
                        continue
                    key = (bafu_db, code)
                ex.append({"input": key, "amount": e["amount"], "type": "technosphere", "unit": e["unit"],
                           "comment": e.get("comment", "")})
            for e in node["biosphere"]:
                found = find_flow(e["flow_code"], e["flow_database"])
                if not found:
                    missing.append(f"{label}: {e['kind']} -> flow {e['flow_code']!r} "
                                   f"({e.get('flow_name') or e['flow_name_in_spec']}) not found in "
                                   + ", ".join(biosphere_dbs))
                    continue
                ex.append({"input": (found, e["flow_code"]), "amount": e["amount"], "type": "biosphere",
                           "unit": e["unit"], "comment": e.get("comment", "")})
            return ex

        for node in d["nodes"]:
            if not want_explicit and node["node_code"] not in referenced:
                continue
            data[(target_db, node["node_code"])] = {
                "name": node["name"], "unit": node["unit"], "location": node["location"], "type": "process",
                "reference product": node["reference_product"],
                "comment": base_comment + (f" {node['comment']}" if node.get("comment") else ""),
                "reverse_bafu": {"bafu_code": d["bafu_code"], "strategy": d["strategy"].get("code", ""),
                                 "kind": "explicit", "quality": d["quality"]},
                "exchanges": exchanges_for(node, node["node_code"]),
            }

        res = d.get("residual")
        if want_hybrid and res:
            main = next(n for n in d["nodes"] if n["node_code"] == d["main_node_code"])
            ex = exchanges_for(main, res["node_code"])
            for f in res["flows"]:
                found = find_flow(f["flow_code"], f["flow_database"])
                if not found:
                    missing.append(f"{label}: residual -> flow {f['flow_code']!r} ({f['flow_name']}) not found in "
                                   + ", ".join(biosphere_dbs))
                    continue
                ex.append({"input": (found, f["flow_code"]), "amount": f["amount"], "type": "biosphere",
                           "unit": f["unit"], "comment": "residual (target minus explicit model)"})
            # the hybrid's own sub-nodes are the explicit ones; import them too so it can be linked
            for node in d["nodes"]:
                if node["node_code"] == d["main_node_code"] or (target_db, node["node_code"]) in data:
                    continue
                data[(target_db, node["node_code"])] = {
                    "name": node["name"], "unit": node["unit"], "location": node["location"], "type": "process",
                    "reference product": node["reference_product"], "comment": base_comment,
                    "reverse_bafu": {"bafu_code": d["bafu_code"], "strategy": d["strategy"].get("code", ""),
                                     "kind": "explicit", "quality": d["quality"]},
                    "exchanges": exchanges_for(node, node["node_code"]),
                }
            data[(target_db, res["node_code"])] = {
                "name": res["name"], "unit": res["unit"], "location": res["location"], "type": "process",
                "reference product": res["name"],
                "comment": base_comment + " HYBRID: " + res["note"],
                "reverse_bafu": {"bafu_code": d["bafu_code"], "strategy": d["strategy"].get("code", ""), "kind": "hybrid",
                                 "quality": d["quality"]},
                "exchanges": ex,
            }
    return data, missing


def run(project: str, file: Path, target_db: str, bafu_db: str, biosphere_dbs: list[str], include: str,
        dry_run: bool, overwrite: bool) -> dict:
    if project not in bd.projects:
        raise SystemExit(f"Brightway project {project!r} not found. Existing projects: "
                         + ", ".join(sorted(p.name for p in bd.projects)))
    bd.projects.set_current(project)

    for name in [bafu_db, *biosphere_dbs]:
        if name not in bd.databases:
            raise SystemExit(f"database {name!r} not found in project {project!r}. "
                             f"Present: {', '.join(sorted(bd.databases))}\n"
                             "Use --bafu-db / --biosphere to name the databases you actually have.")
    if target_db in bd.databases and not overwrite and not dry_run:
        raise SystemExit(f"database {target_db!r} already exists in {project!r}. "
                         "Pass --overwrite to replace it, or --database to pick another name.")

    payload = load_export(file)
    data, missing = plan(payload, target_db, bafu_db, biosphere_dbs, include)

    if missing:
        agg = defaultdict(int)
        for m in missing:
            agg[m] += 1
        print(f"\nIMPORT ABORTED - {len(missing)} reference(s) could not be resolved in project "
              f"{project!r}. Nothing was written.\n", file=sys.stderr)
        for m in sorted(agg):
            print(f"  missing: {m}" + (f"  (x{agg[m]})" if agg[m] > 1 else ""), file=sys.stderr)
        print("\nMost likely cause: the target project's BAFU-2026 or EF 3.1 biosphere is a different "
              "release from the one the export was made against. Check --bafu-db and --biosphere.",
              file=sys.stderr)
        raise MissingReferences(2)

    n_ex = sum(len(v["exchanges"]) for v in data.values())
    print(f"export {file} ({payload['n_datasets']} datasets, generated {payload['generated_at']})")
    print(f"resolved every reference: {len(data)} nodes, {n_ex} exchanges -> {target_db!r} in {project!r}")
    if dry_run:
        print("--dry-run: nothing written")
        return data

    if target_db in bd.databases:
        del bd.databases[target_db]
    newdb = bd.Database(target_db)
    newdb.register(depends=[bafu_db, *biosphere_dbs],
                   comment=f"reverse-bafu disaggregated BAFU-2026 unit processes, imported from {file.name} "
                           f"(generated {payload['generated_at']}, commit {payload.get('git_commit', '')[:12]}). "
                           + payload["citation"])
    newdb.write(data)
    print(f"wrote {len(newdb)} nodes to {target_db!r}")
    return data


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project", required=True, help="the Brightway project to add the datasets to")
    ap.add_argument("--file", type=Path, default=DEFAULT_FILE)
    ap.add_argument("--database", default=DEFAULT_DB, help="name of the new database to create")
    ap.add_argument("--bafu-db", default="bafu-2026", help="the existing BAFU-2026 database to link against")
    ap.add_argument("--biosphere", action="append", default=None,
                    help="biosphere database to resolve elementary flows in (repeatable)")
    ap.add_argument("--include", choices=("explicit", "hybrid", "both"), default="both")
    ap.add_argument("--dry-run", action="store_true", help="resolve everything and report, but write nothing")
    ap.add_argument("--overwrite", action="store_true", help="replace the target database if it exists")
    a = ap.parse_args()
    bios = a.biosphere or ["ef-3.1-biosphere", "bafu-2026-residual"]
    run(a.project, a.file, a.database, a.bafu_db, bios, a.include, a.dry_run, a.overwrite)


if __name__ == "__main__":
    main()
