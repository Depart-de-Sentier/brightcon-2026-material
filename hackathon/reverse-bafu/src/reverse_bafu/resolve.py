"""Step 1 - terminate on the database: map every spec input to a BAFU unit process.

An input resolves to one of three states:
  unit        an existing unit process - link and stop
  aggregated  an existing dataset that is itself a system process (type=2 flag or found by
              structure, db.aggregated_codes_all) - link, but flag the dependency
  missing     nothing in BAFU - needs a nested ``node`` in the spec (or a different name)
"""

from __future__ import annotations

import sys

import bw2data as bd

from . import db
from .spec import Node, Spec, walk


def resolve_node(node: Node, prefer_location: str, report: list[str], depth: int = 0) -> bool:
    ok = True
    pad = "  " * depth
    report.append(f"{pad}node: {node.name} [{node.location or prefer_location}] ({node.unit})")
    for i in node.inputs:
        if i.node:
            report.append(f"{pad}  + {i.amount:.4g} {i.unit:9s} {i.name}  -> NEW NODE")
            ok &= resolve_node(i.node, i.node.location or prefer_location, report, depth + 2)
            continue
        if i.sandbox:
            try:
                node_ = bd.get_node(database=db.SANDBOX_DB, code=i.sandbox)
                i.code = i.sandbox
                report.append(f"{pad}  ✓ {i.amount:.4g} {i.unit:9s} {i.name} -> SANDBOX {node_['name'][:50]} (rebuilt earlier)")
            except Exception:
                ok = False
                report.append(f"{pad}  ✗ {i.amount:.4g} {i.unit:9s} {i.name} -> sandbox node {i.sandbox} not built yet")
            continue
        hit, sugg = db.resolve_activity(i.name, i.location, prefer=node.location or prefer_location)
        if hit is None:
            ok = False
            report.append(f"{pad}  ✗ {i.amount:.4g} {i.unit:9s} {i.name}  -> MISSING; close names: {sugg}")
            continue
        i.code, i.location = hit["code"], hit["location"]
        state = "system process!" if hit["aggregated"] else f"unit ({hit['n_inputs']} inputs)"
        unit_warn = "" if hit["unit"].startswith(i.unit[:4]) else f"  UNIT MISMATCH spec={i.unit} db={hit['unit']}"
        report.append(f"{pad}  ✓ {i.amount:.4g} {i.unit:9s} {i.name} [{hit['location']}] -> {state}{unit_warn}")
    for flows, kind in ((node.emissions, "emission"), (node.resources, "resource")):
        for f in flows:
            hit, sugg = db.resolve_flow(f.name, f.category)
            if hit is None:
                ok = False
                report.append(f"{pad}  ✗ {kind} {f.name} -> MISSING; close names: {sugg}")
                continue
            f.code, f.database = hit["code"], hit["database"]
            unit_warn = "" if hit["unit"].startswith(f.unit[:4]) else f"  UNIT MISMATCH spec={f.unit} db={hit['unit']}"
            report.append(f"{pad}  ✓ {kind} {f.amount:.4g} {f.unit:9s} {f.name} -> {hit['database']} {'/'.join(hit['categories'][:2])}{unit_warn}")
    return ok


def run(spec: Spec) -> bool:
    report: list[str] = []
    ok = resolve_node(spec.node, spec.node.location, report)
    print("\n".join(report))
    n_nodes = sum(1 for _ in walk(spec.node))
    print(f"\n{'resolved' if ok else 'UNRESOLVED inputs remain'}; {n_nodes} node(s) to build", file=sys.stderr)
    return ok
