"""The spec: one JSON file per system process, holding the evidence-derived unit process.

Minimal example::

    {
      "target": {"code": "d8ec4be3-...", "name": "Burnt shale, at plant"},
      "strategy": {"code": "S1", "label": "transcription from the report table",
                   "note": "one amount calibrated because ..."},
      "evidence": [{"source": "2020 - LCA selected types of concrete - Tschuemperlin.pdf", "where": "Tab. 3.9"}],
      "node": {
        "name": "Burnt shale, at plant, disaggregated", "unit": "kilogram", "location": "DE",
        "inputs":    [{"name": "Blasting", "amount": 6.74e-5, "unit": "kilogram", "note": "0.0674 kg/t"}],
        "emissions": [{"name": "Nitrogen Oxides", "category": "air", "amount": 5.19e-4, "unit": "kilogram"}],
        "resources": [{"name": "Shale", "amount": 0.9626, "unit": "kilogram"}]
      }
    }

An input may carry ``"node": {...}`` (a nested new unit process, built first and linked),
``"sandbox": "<code>-disagg"`` (link to a node rebuilt by an earlier spec instead of the BAFU
dataset), or ``"free": true`` with optional ``"bounds": [lo, hi]`` (its amount may be adjusted by
``calibrate`` within the report's range). A node-level ``"mass_sum": 1.0`` constrains the free
kilogram inputs to add up to that mass. ``resolve`` writes back
``code``/``location`` for every matched input and flow.

``strategy.code`` is the route (S1 transcription, S2 template transfer, S3 top-down model; see
exports/README.md). Specs made by ``reverse-bafu draft-all`` also carry ``"variant": "draft"`` (their
sandbox nodes get a ``-draft`` infix, so they never collide with an interactive spec of the same
dataset), a ``derivation`` on every input (quote, raw value, factor, mapping reason, author,
``reviewed_by``) and a top-level ``provenance`` block (model, prompt hashes, gaps the model reported).
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Flow:
    name: str
    amount: float
    unit: str
    category: str = ""          # "air", "water", "soil", "resources" - top-level hint
    code: str = ""              # filled by resolve: (database, code)
    database: str = ""
    note: str = ""
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class Input:
    name: str
    amount: float
    unit: str
    location: str = ""
    code: str = ""
    sandbox: str = ""           # link to a node rebuilt earlier (its sandbox code), not to bafu-2026
    free: bool = False
    bounds: tuple[float, float] | None = None  # for free inputs: [lo, hi] from the report's ranges
    node: Node | None = None    # nested new node
    note: str = ""
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class Node:
    name: str
    unit: str
    location: str
    inputs: list[Input]
    emissions: list[Flow]
    resources: list[Flow]
    comment: str = ""
    mass_sum: float | None = None  # if set: the free kilogram inputs must add up to this (per unit of product)


@dataclass
class Spec:
    path: Path
    target_code: str
    target_name: str
    strategy: dict          # {"code": "S1", "label": ..., "note": ...}
    variant: str            # "" or e.g. "draft": suffix for the sandbox node codes
    evidence: list[dict]
    node: Node
    raw: dict[str, Any]


def _node(d: dict) -> Node:
    return Node(
        name=d["name"], unit=d.get("unit", "kilogram"), location=d.get("location", ""),
        inputs=[
            Input(name=i["name"], amount=float(i["amount"]), unit=i.get("unit", ""), location=i.get("location", ""),
                  code=i.get("code", ""), sandbox=i.get("sandbox", ""), free=bool(i.get("free", False)),
                  bounds=tuple(i["bounds"]) if i.get("bounds") else None,
                  node=_node(i["node"]) if i.get("node") else None, note=i.get("note", ""), raw=i)
            for i in d.get("inputs", [])
        ],
        emissions=[Flow(name=f["name"], amount=float(f["amount"]), unit=f.get("unit", "kilogram"),
                        category=f.get("category", "air"), code=f.get("code", ""), database=f.get("database", ""),
                        note=f.get("note", ""), raw=f) for f in d.get("emissions", [])],
        resources=[Flow(name=f["name"], amount=float(f["amount"]), unit=f.get("unit", "kilogram"),
                        category=f.get("category", "resources"), code=f.get("code", ""), database=f.get("database", ""),
                        note=f.get("note", ""), raw=f) for f in d.get("resources", [])],
        comment=d.get("comment", ""),
        mass_sum=d.get("mass_sum"),
    )


def load(path: str | Path) -> Spec:
    path = Path(path)
    raw = json.loads(path.read_text())
    return Spec(path=path, target_code=raw["target"]["code"], target_name=raw["target"].get("name", ""),
                strategy=raw.get("strategy", {}), variant=raw.get("variant", ""), evidence=raw.get("evidence", []),
                node=_node(raw["node"]), raw=raw)


def save(spec: Spec) -> None:
    """Write resolved codes / calibrated amounts back into the JSON, keeping everything else."""
    def sync_node(n: Node, d: dict) -> None:
        for i, di in zip(n.inputs, d.get("inputs", [])):
            di["amount"] = i.amount
            if i.code:
                di["code"], di["location"] = i.code, i.location
            if i.node:
                sync_node(i.node, di["node"])
        for flows, key in ((n.emissions, "emissions"), (n.resources, "resources")):
            for f, df in zip(flows, d.get(key, [])):
                if f.code:
                    df["code"], df["database"] = f.code, f.database
    sync_node(spec.node, spec.raw["node"])
    spec.path.write_text(json.dumps(spec.raw, indent=2, ensure_ascii=False) + "\n")


def node_prefix(spec: "Spec") -> str:
    """<target code>[-<variant>] - the stem of every sandbox node code this spec writes."""
    return spec.target_code + (f"-{spec.variant}" if spec.variant else "")


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:60]


def walk(node: Node):
    """Yield nested nodes depth-first, children before parents (build order)."""
    for i in node.inputs:
        if i.node:
            yield from walk(i.node)
    yield node
