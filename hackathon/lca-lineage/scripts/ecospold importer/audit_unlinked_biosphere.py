"""Create a review worklist; never infer or apply a migration.

Call with the live importer after refreshing the notebook's unresolved report.
Uses the current project's biosphere, the installed official elementary-flow
catalog, and the reviewed mapping files. Does not modify the importer.
"""

import csv
import hashlib
import importlib.util
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from lxml import etree
import bw2data as bd


def normalized(value):
    return re.sub(r"[^a-z0-9]", "", (value or "").lower())


def signature(row):
    return row["name"], tuple(row["categories"]), row["unit"]


def review_group(row):
    name, categories = row["name"], row["categories"]
    if categories[0] in ("non-material", "economic"):
        return "missing indicator type"
    if "resource correction" in name:
        return "method-specific recycling correction"
    if any("long-term" in category for category in categories):
        return "unsupported long-term receiving compartment"
    if name.startswith(("Occupation,", "Transformation,")):
        return "land class requires correspondence or more detail"
    if name in ("Carbon dioxide", "Carbon monoxide"):
        return "carbon origin unresolved"
    if name.startswith("Particulates"):
        return "particle size or aggregate definition unresolved"
    if name.startswith("Radioactive species"):
        return "unspecified radionuclide or emitter type"
    if name in ("Waste water", "Waste water/m3", "Chemically polluted water"):
        return "wastewater composition or definition unresolved"
    if categories[0] == "natural resource":
        return "resource identity, basis, or compartment review"
    return "chemical identity or compartment review"


def audit_unlinked_biosphere(importer, biosphere, root):
    root = Path(root)
    report_path = root / "reports/generated/biosphere-unlinked.json"
    report = json.loads(report_path.read_text())
    if report["biosphere_database"] != biosphere:
        raise ValueError("Unlinked report belongs to a different biosphere database")
    targets = sorted(
        [
            {
                "name": flow["name"],
                "categories": list(flow["categories"]),
                "unit": flow["unit"],
                "code": flow["code"],
                "type": flow.get("type"),
                "CAS number": flow.get("CAS number", ""),
            }
            for flow in bd.Database(biosphere)
        ],
        key=lambda row: row["code"],
    )
    by_code = {row["code"]: row for row in targets}

    source_cas = defaultdict(Counter)
    source_counts = Counter()
    for dataset in importer.data:
        for exchange in dataset["exchanges"]:
            if exchange["type"] != "biosphere" or exchange.get("input"):
                continue
            key = signature(exchange)
            source_counts[key] += 1
            source_cas[key][exchange.get("CAS number") or ""] += 1
    expected_counts = Counter(
        {signature(row): row["occurrences"] for row in report["unlinked"]}
    )
    if source_counts != expected_counts:
        raise ValueError(
            "Live importer and unresolved report have different signatures or counts"
        )

    names = defaultdict(set)
    for row in targets:
        names[normalized(row["name"])].add(row["code"])
    package = Path(importlib.util.find_spec("bw2io").origin).parent
    official_path = package / "data/lci/ecoinvent elementary flows 3.9.xml"
    ns = {"e": "http://www.EcoInvent.org/EcoSpold02"}
    for entry in etree.parse(str(official_path)).getroot():
        code = entry.get("id")
        if code not in by_code:
            continue
        for name in entry.findall("e:name", ns) + entry.findall("e:synonym", ns):
            names[normalized(name.text)].add(code)

    aliases = defaultdict(set)
    for path in (root / "schemas/mappings").glob("bafu-2026-biosphere-*.json"):
        mapping = json.loads(path.read_text())
        if "name" not in mapping["fields"]:
            continue
        for source, replacement in mapping["data"]:
            if "name" in replacement:
                record = dict(zip(mapping["fields"], source))
                aliases[record["name"]].add(replacement["name"])

    rows = []
    for source in report["unlinked"]:
        key = signature(source)
        source_ids = {value.lstrip("0") for value in source_cas[key] if value}
        candidate_reasons = defaultdict(set)
        for code in names[normalized(source["name"])]:
            candidate_reasons[code].add("catalog name or synonym")
        for alias in aliases[source["name"]]:
            for code in names[normalized(alias)]:
                candidate_reasons[code].add("name used in another reviewed rule")
        for target in targets:
            cas = (target.get("CAS number") or "").lstrip("0")
            if cas and cas in source_ids:
                candidate_reasons[target["code"]].add("CAS match")
        candidates = []
        for code, reasons in sorted(candidate_reasons.items()):
            target = by_code[code]
            candidates.append(
                {
                    **target,
                    "candidate_basis": sorted(reasons),
                    "same_unit": target["unit"] == source["unit"],
                    "same_compartment": target["categories"] == source["categories"],
                    "same_main_class": target["categories"][:1]
                    == source["categories"][:1],
                }
            )
        rows.append(
            {
                **source,
                "source_cas_counts": dict(source_cas[key]),
                "review_group": review_group(source),
                "candidate_targets": candidates,
                "status": "unresolved; candidates are not approved mappings",
            }
        )

    count = sum(row["occurrences"] for row in rows)
    assert count == report["after"]["unlinked"]
    assert len(rows) == report["after"]["unlinked_signatures"]
    group_counts = Counter()
    for row in rows:
        group_counts[row["review_group"]] += row["occurrences"]
    output = {
        "unlinked_report_sha256": hashlib.sha256(report_path.read_bytes()).hexdigest(),
        "project": bd.projects.current,
        "biosphere_database": biosphere,
        "catalog_sha256": hashlib.sha256(
            json.dumps(targets, sort_keys=True).encode()
        ).hexdigest(),
        "official_catalog_sha256": hashlib.sha256(
            official_path.read_bytes()
        ).hexdigest(),
        "occurrences": count,
        "signatures": len(rows),
        "groups": dict(group_counts.most_common()),
        "limitation": (
            "Candidate searches do not prove equivalence. CAS can conflate isotope, "
            "hydration, carbon origin, or other bases; catalog synonyms can be ambiguous. "
            "A name used in another rule can be a context-specific or approved proxy. "
            "No candidate is automatically applied."
        ),
        "rows": rows,
    }
    output_path = root / "reports/generated/biosphere-remaining-worklist.json"
    output_path.write_text(json.dumps(output, indent=2) + "\n")
    with output_path.with_suffix(".csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            (
                "name",
                "categories",
                "unit",
                "occurrences",
                "review_group",
                "source_cas",
                "candidate_count",
                "same_unit_and_compartment_candidates",
            )
        )
        for row in rows:
            matching = [
                c["name"]
                for c in row["candidate_targets"]
                if c["same_unit"] and c["same_compartment"]
            ]
            writer.writerow(
                (
                    row["name"],
                    " / ".join(row["categories"]),
                    row["unit"],
                    row["occurrences"],
                    row["review_group"],
                    json.dumps(row["source_cas_counts"]),
                    len(row["candidate_targets"]),
                    " | ".join(matching),
                )
            )
    return {key: output[key] for key in ("occurrences", "signatures", "groups")}
