"""Step 3 - write the node(s) into the sandbox database, children first, then the hybrid.

Two nodes per spec end up in the sandbox:
  <code>-disagg   explicit inputs + direct flows only (the model)
  <code>-hybrid   the same plus a residual block of elementary flows so that the cumulative
                  inventory equals the original system process exactly
"""

from __future__ import annotations

import numpy as np
import bw2data as bd

from . import db
from .lci import System
from .spec import Node, Spec, node_prefix, slug, walk

RESIDUAL_MIN = 1e-15  # drop residual entries below this (numerical noise)


def _node_code(spec: Spec, node: Node) -> str:
    return f"{node_prefix(spec)}-disagg" if node is spec.node else f"{node_prefix(spec)}-{slug(node.name)}"


def _exchanges(spec: Spec, node: Node, code: str) -> list[dict]:
    ex = [{"input": (db.SANDBOX_DB, code), "amount": 1.0, "type": "production", "unit": node.unit}]
    for i in node.inputs:
        if i.node:
            key = (db.SANDBOX_DB, _node_code(spec, i.node))
        elif i.sandbox:
            key = (db.SANDBOX_DB, i.sandbox)
        else:
            key = (db.INVENTORY_DB, i.code)
        ex.append({"input": key, "amount": i.amount, "type": "technosphere", "unit": i.unit, "comment": i.note})
    for f in node.emissions + node.resources:
        ex.append({"input": (f.database, f.code), "amount": f.amount, "type": "biosphere", "unit": f.unit, "comment": f.note})
    return ex


def _write(sandbox, data: dict) -> None:
    """Merge into the sandbox: keep other specs' nodes, replace ours."""
    existing = sandbox.load() if len(sandbox) else {}
    existing.update(data)
    sandbox.write(existing)


def run(spec: Spec, hybrid: bool = True) -> dict:
    sandbox = db.sandbox()
    data = {}
    for node in walk(spec.node):
        code = _node_code(spec, node)
        data[(db.SANDBOX_DB, code)] = {
            "name": node.name, "unit": node.unit, "location": node.location or spec.node.location,
            "type": "process", "reference product": node.name,
            "comment": f"reverse-bafu rebuild of {spec.target_name} ({spec.target_code}). "
                       + "; ".join(f"{e.get('source', '')} {e.get('where', '')}".strip() for e in spec.evidence),
            "exchanges": _exchanges(spec, node, code),
        }
    _write(sandbox, data)
    codes = {"disagg": f"{node_prefix(spec)}-disagg"}
    print(f"wrote {len(data)} node(s) to {db.SANDBOX_DB}: " + ", ".join(k[1] for k in data))
    if not hybrid:
        return codes

    # residual = target cumulative - explicit cumulative, as direct flows on a copy of the node
    explicit = bd.get_node(database=db.SANDBOX_DB, code=codes["disagg"])
    target = bd.get_node(database=db.INVENTORY_DB, code=spec.target_code)
    sys_ = System(explicit)
    b_t, b_e = sys_.cumulative([target.id, explicit.id]).T
    r = b_t - b_e
    hyb_code = f"{node_prefix(spec)}-hybrid"
    # bw2data's write() consumes the exchange lists it is given, so rebuild from the spec
    hyb = dict(explicit.as_dict())
    hyb.pop("id", None)
    hyb["code"] = hyb_code
    hyb["name"] = spec.node.name + ", hybrid"
    hyb["reference product"] = hyb["name"]
    hyb["exchanges"] = _exchanges(spec, spec.node, hyb_code)
    n_explicit = len(hyb["exchanges"])
    n_neg = 0
    for row in np.where(np.abs(r) > RESIDUAL_MIN)[0]:
        n_neg += r[row] < 0
        hyb["exchanges"].append({"input": sys_.flow_key(int(row)), "amount": float(r[row]), "type": "biosphere",
                                 "comment": "residual (target minus explicit model)"})
    _write(sandbox, {(db.SANDBOX_DB, hyb_code): hyb})
    codes["hybrid"] = hyb_code
    print(f"wrote {hyb_code}: {len(hyb['exchanges']) - n_explicit} residual flows, {n_neg} negative")
    return codes
