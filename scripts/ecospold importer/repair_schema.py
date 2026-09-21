#!/usr/bin/env python3
"""Repair remaining EcoSpold 1 metadata defects and validate every output file.

Each mutation is reversible from the JSON log. Original attribute values and
removed elements also remain in adjacent XML comments. Inventory amounts are
never changed. Missing required facts need explicit, documented overrides.
"""

import argparse
from collections import Counter, defaultdict
from copy import deepcopy
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
import re

from lxml import etree
from pyecospold import Defaults

from repair_metadata import COMMENT_PREFIX
from repair_namespace import NAMESPACE, REPO_ROOT

NS = f"{{{NAMESPACE}}}"
BOOL_ATTRIBUTES = {
    "impactAssessmentResult",
    "dataValidForEntirePeriod",
    "copyright",
    "datasetRelatesToProduct",
    "infrastructureProcess",
    "infrastructureIncluded",
}
ORDERS = {
    "processInformation": [
        "referenceFunction",
        "geography",
        "technology",
        "timePeriod",
        "dataSetInformation",
    ],
    "modellingAndValidation": ["representativeness", "source", "validation"],
}


def canonical(root):
    return etree.tostring(root, method="c14n", with_comments=True)


class Editor:
    def __init__(self, root):
        self.root = root
        self.changes = []

    def path(self, element):
        return element.getroottree().getpath(element)

    def record(self, element, change):
        change["repair_id"] = f"schema-{len(self.changes) + 1}"
        self.changes.append(change)
        payload = json.dumps(change, ensure_ascii=True, sort_keys=True).replace(
            "-", "\\u002d"
        )
        comment = etree.Comment(f"{COMMENT_PREFIX}{payload} ")
        element.addprevious(comment)

    def attribute(self, element, attribute, value, reason, **evidence):
        old = element.get(attribute)
        if old == value:
            return
        change = {
            "action": "attribute",
            "path": self.path(element),
            "attribute": attribute,
            "original_value": old,
            "replacement_value": value,
            "reason": reason,
            **evidence,
        }
        if value is None:
            del element.attrib[attribute]
        else:
            element.set(attribute, value)
        self.record(element, change)

    def remove(self, element, reason):
        parent = element.getparent()
        change = {
            "action": "remove_element",
            "parent_path": self.path(parent),
            "index": parent.index(element),
            "original_xml": etree.tostring(
                element, encoding="unicode", with_tail=False
            ),
            "original_tail": element.tail,
            "reason": reason,
        }
        self.record(element, change)
        parent.remove(element)

    def append(self, parent, element, reason, **evidence):
        parent.append(element)
        change = {
            "action": "add_element",
            "path": self.path(element),
            "reason": reason,
            **evidence,
        }
        self.record(element, change)

    def reorder(self, parent, names):
        children = list(parent)
        groups, pending = [], []
        for index, child in enumerate(children):
            pending.append(index)
            if isinstance(child.tag, str):
                tag = etree.QName(child)
                if tag.namespace == NAMESPACE:
                    if tag.localname not in names:
                        raise ValueError(f"Unexpected child {child.tag}")
                    rank = names.index(tag.localname)
                else:
                    rank = len(names)
                groups.append((rank, pending))
                pending = []
        order = [
            index
            for _, indices in sorted(groups, key=lambda item: item[0])
            for index in indices
        ] + pending
        if order == list(range(len(children))):
            return
        change = {
            "action": "reorder",
            "path": self.path(parent),
            "new_order": order,
            "reason": f"{etree.QName(parent).localname}_sequence",
        }
        parent[:] = [children[index] for index in order]
        self.record(parent, change)


def reverse_changes(root, changes):
    """Restore the complete input tree; used as a mandatory per-file integrity gate."""
    root = deepcopy(root)
    for change in reversed(changes):
        repair_id = change["repair_id"]
        matches = []
        for comment in root.xpath("//comment()"):
            if (comment.text or "").startswith(COMMENT_PREFIX):
                payload = json.loads(comment.text[len(COMMENT_PREFIX) :])
                if payload.get("repair_id") == repair_id:
                    matches.append(comment)
        if len(matches) != 1:
            raise ValueError(f"Missing/ambiguous audit comment: {repair_id}")
        comment = matches[0]
        comment.getparent().remove(comment)
        action = change["action"]
        if action == "attribute":
            (element,) = root.xpath(change["path"])
            old = change["original_value"]
            if old is None:
                del element.attrib[change["attribute"]]
            else:
                element.set(change["attribute"], old)
        elif action == "add_element":
            (element,) = root.xpath(change["path"])
            element.getparent().remove(element)
        elif action == "remove_element":
            (parent,) = root.xpath(change["parent_path"])
            element = etree.fromstring(change["original_xml"].encode())
            element.tail = change["original_tail"]
            parent.insert(change["index"], element)
        elif action == "reorder":
            (parent,) = root.xpath(change["path"])
            current = list(parent)
            original = [None] * len(current)
            for index, previous_index in enumerate(change["new_order"]):
                original[previous_index] = current[index]
            parent[:] = original
        else:
            raise ValueError(f"Unknown change action: {action}")
    return root


def build_catalog(files):
    """Collect identical source identities and reserve all existing regional codes."""
    sources = defaultdict(list)
    locations = set()
    for path in files:
        tree = etree.parse(str(path))
        for element in tree.findall(f".//{NS}source"):
            sources[element.get("number")].append((dict(element.attrib), path.name))
        for element in tree.iter():
            if isinstance(element.tag, str) and "location" in element.attrib:
                locations.add(element.get("location"))
    aliases = {}
    reserved = {value for value in locations if len(value) <= 7}
    for location in sorted(value for value in locations if len(value) > 7):
        alias = "L" + hashlib.sha256(location.encode()).hexdigest()[:6].upper()
        if alias in reserved:
            raise ValueError(f"Location alias collision: {alias}")
        reserved.add(alias)
        aliases[location] = alias
    return sources, aliases


def repair_schema(data, filename, catalog, aliases, overrides):
    root = etree.fromstring(
        data, etree.XMLParser(resolve_entities=False, no_network=True)
    )
    if root.tag != NS + "ecoSpold" or root.getroottree().docinfo.doctype:
        raise ValueError("Expected namespaced EcoSpold 1 without a DTD")
    before = canonical(root)
    editor = Editor(root)
    unresolved = []
    for element in list(root.iter()):
        if not isinstance(element.tag, str):
            continue
        tag = etree.QName(element).localname
        for attribute in sorted(BOOL_ATTRIBUTES.intersection(element.attrib)):
            if element.get(attribute) in ("True", "False"):
                editor.attribute(
                    element,
                    attribute,
                    element.get(attribute).lower(),
                    "boolean_lexical_form",
                )
            elif element.get(attribute) == "":
                field = f"{tag}.{attribute}"
                override = overrides.get("empty_booleans", {}).get(field)
                if override:
                    if override["value"] not in ("true", "false"):
                        raise ValueError(f"Invalid boolean override for {field}")
                    editor.attribute(
                        element,
                        attribute,
                        override["value"],
                        "documented_unknown_boolean_fallback",
                        evidence=override["evidence"],
                    )
                else:
                    unresolved.append({"kind": "missing_boolean", "field": field})
        if tag == "referenceFunction" and "text" in element.attrib:
            editor.attribute(
                element, "text", None, "unsupported_referenceFunction_text"
            )
        if tag in ("dataset", "dataSetInformation"):
            value = element.get("timestamp", "")
            if len(value) > 10 and value[10] == " ":
                editor.attribute(
                    element,
                    "timestamp",
                    value[:10] + "T" + value[11:],
                    "datetime_separator",
                )
        if tag == "exchange":
            value = element.get("CASNumber")
            if value is not None and not re.fullmatch(
                r"[0-9]{2,7}-[0-9]{2}-[0-9]", value
            ):
                editor.attribute(
                    element, "CASNumber", None, "invalid_optional_CASNumber"
                )
        if tag in ("exchange", "geography") and element.get("location") in aliases:
            value = element.get("location")
            editor.attribute(
                element,
                "location",
                aliases[value],
                "reversible_local_region_alias",
                alias_definition=value,
            )
        if tag == "representativeness" and "percent" in element.attrib:
            value = element.get("percent")
            try:
                number = Decimal(value)
                if (
                    not number.is_finite()
                    or not 0 <= number <= 100
                    or number != number.quantize(Decimal("0.1"))
                ):
                    raise ValueError("Unrepresentable percentage")
                replacement = f"{number:.1f}"
            except (InvalidOperation, ValueError):
                replacement = None
            editor.attribute(
                element,
                "percent",
                replacement,
                (
                    "percentage_lexical_form"
                    if replacement
                    else "invalid_optional_percentage"
                ),
            )
        if tag == "person":
            if len(element.get("name", "")) > 40:
                editor.attribute(
                    element, "name", "", "overlong_required_name_preserved_in_comment"
                )
            if "address" not in element.attrib:
                editor.attribute(
                    element,
                    "address",
                    "",
                    "missing_required_address_empty_not_invented",
                )
            if not element.get("countryCode"):
                override = overrides.get("person_countries", {}).get(
                    element.get("number")
                )
                if override:
                    editor.attribute(
                        element,
                        "countryCode",
                        override["value"],
                        "documented_country_override",
                        evidence=override["evidence"],
                    )
                else:
                    unresolved.append(
                        {"kind": "missing_country", "person": element.get("number")}
                    )
        if tag == "source":
            if not element.get("year"):
                source_text = re.sub(r"\\+n", "\n", element.get("text", ""))
                years = set(re.findall(r"\bYear:\s*([0-9]{4})\b", source_text))
                if len(years) == 1:
                    editor.attribute(
                        element, "year", years.pop(), "year_explicit_in_source_text"
                    )
                else:
                    override = (
                        overrides.get("source_years", {})
                        .get(filename, {})
                        .get(element.get("number"))
                    )
                    if override:
                        editor.attribute(
                            element,
                            "year",
                            str(override["value"]),
                            "documented_unknown_source_year_fallback",
                            evidence=override["evidence"],
                        )
                    else:
                        unresolved.append(
                            {
                                "kind": "missing_source_year",
                                "source": element.get("number"),
                            }
                        )
            volume = element.get("volumeNo")
            if volume is not None and not re.fullmatch(r"[0-9]{1,3}", volume):
                editor.attribute(element, "volumeNo", None, "invalid_optional_volumeNo")
        if tag == "timePeriod" and not any(
            isinstance(child.tag, str) for child in element
        ):
            override = overrides.get("periods", {}).get(filename)
            if override:
                for side in ("start", "end"):
                    child = etree.Element(NS + side + "Year")
                    child.text = str(override[side + "_year"])
                    editor.append(
                        element,
                        child,
                        "documented_period_override",
                        evidence=override["evidence"],
                    )
            else:
                unresolved.append({"kind": "missing_period"})

    for dataset in root.findall(NS + "dataset"):
        exchanges = dataset.findall(f"{NS}flowData/{NS}exchange")
        numbers = {int(element.get("number")) for element in exchanges}
        # Allocation pointers would make an invalid number ambiguous; require review.
        for element in exchanges:
            old = int(element.get("number"))
            if old > 0:
                continue
            if dataset.findall(f"{NS}flowData/{NS}allocation"):
                raise ValueError("Invalid exchange ID with allocation references")
            number = 1
            while number in numbers:
                number += 1
            numbers.add(number)
            editor.attribute(element, "number", str(number), "nonpositive_exchange_id")

        modelling = dataset.find(f"{NS}metaInformation/{NS}modellingAndValidation")
        validations = modelling.findall(NS + "validation")
        if len(validations) > 1:
            for validation in validations[1:]:
                if (
                    validation.attrib
                    or len(validation)
                    or (validation.text or "").strip()
                ):
                    raise ValueError(
                        "Multiple nonempty validations require explicit reconciliation"
                    )
                editor.remove(validation, "empty_duplicate_validation")
        present_sources = {
            source.get("number") for source in modelling.findall(NS + "source")
        }
        publication = dataset.find(
            f"{NS}metaInformation/{NS}administrativeInformation/{NS}dataGeneratorAndPublication"
        )
        reference = publication.get("referenceToPublishedSource")
        if reference and reference not in present_sources:
            choices = catalog.get(reference, [])
            identities = {
                tuple(
                    attrs.get(key)
                    for key in ("firstAuthor", "additionalAuthors", "title", "year")
                )
                for attrs, _ in choices
            }
            if choices and len(identities) == 1:
                attrs, origin = max(
                    choices,
                    key=lambda item: (len(item[0]), len(item[0].get("text", ""))),
                )
                editor.append(
                    modelling,
                    etree.Element(NS + "source", attrib=attrs),
                    "restore_referenced_source_from_collection",
                    source_file=origin,
                    source_number=reference,
                )
            else:
                unresolved.append(
                    {"kind": "ambiguous_missing_source", "number": reference}
                )

    for name, order in ORDERS.items():
        for parent in root.findall(f".//{NS}{name}"):
            editor.reorder(parent, order)
    if canonical(reverse_changes(root, editor.changes)) != before:
        raise AssertionError(f"Repair log does not restore complete input: {filename}")
    repaired = (
        etree.tostring(root, encoding="UTF-8", xml_declaration=True)
        if editor.changes
        else data
    )
    return repaired, editor.changes, unresolved


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=REPO_ROOT / "data/processed/ecospold1-exchange-numbers-fixed",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "data/processed/ecospold1-schema-fixed",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=REPO_ROOT / "reports/generated/ecospold1-schema-repair.json",
    )
    parser.add_argument(
        "--overrides",
        type=Path,
        default=Path(__file__).with_name("schema_overrides.json"),
    )
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    source, output, report_path = (
        value.expanduser().resolve() for value in (args.input, args.output, args.report)
    )
    raw = (REPO_ROOT / "data/raw").resolve()
    if (
        not source.is_dir()
        or output.is_relative_to(source)
        or source.is_relative_to(output)
    ):
        parser.error("Input and output must be separate, non-nested directories")
    if output.is_relative_to(raw) or report_path.is_relative_to(raw):
        parser.error("Raw data is read-only")
    if report_path.is_relative_to(source) or report_path.is_relative_to(output):
        parser.error("Keep reports outside the XML directories")
    files = sorted(source.glob("*.xml"))
    if not files:
        parser.error("No input XML files")
    if output.exists() and {p.name for p in output.iterdir()} - {p.name for p in files}:
        parser.error("Output contains extra files; use an empty directory")
    overrides = (
        json.loads(args.overrides.read_text()) if args.overrides.exists() else {}
    )
    catalog, aliases = build_catalog(files)
    schema = etree.XMLSchema(file=Defaults.SCHEMA_V1_FILE)
    output.mkdir(parents=True, exist_ok=True)
    counts = Counter()
    report = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "input": str(source),
        "output": str(output),
        "schema": str(Defaults.SCHEMA_V1_FILE),
        "overrides": overrides,
        "location_aliases": aliases,
        "files": [],
        "errors": [],
        "schema_invalid_files": [],
    }
    for path in files:
        try:
            original = path.read_bytes()
            repaired, changes, unresolved = repair_schema(
                original, path.name, catalog, aliases, overrides
            )
            dest = output / path.name
            if dest.is_symlink():
                raise ValueError("Refusing output symlink")
            if dest.exists() and dest.read_bytes() != repaired and not args.overwrite:
                raise FileExistsError(
                    "Output differs; use --overwrite or a new directory"
                )
            if not dest.exists() or dest.read_bytes() != repaired:
                dest.write_bytes(repaired)
            valid = schema.validate(etree.fromstring(repaired))
            errors = [
                {"line": error.line, "type": error.type_name, "message": error.message}
                for error in schema.error_log
            ]
            if not valid:
                report["schema_invalid_files"].append(
                    {"file": path.name, "errors": errors}
                )
            counts.update(change["reason"] for change in changes)
            report["files"].append(
                {
                    "file": path.name,
                    "input_sha256": hashlib.sha256(original).hexdigest(),
                    "output_sha256": hashlib.sha256(repaired).hexdigest(),
                    "changes": changes,
                    "unresolved": unresolved,
                    "schema_valid": valid,
                    "reversal_verified": True,
                }
            )
        except Exception as exc:
            report["errors"].append(
                {"file": path.name, "type": type(exc).__name__, "message": str(exc)}
            )
    report.update(
        {
            "input_file_count": len(files),
            "output_file_count": len(report["files"]),
            "schema_valid_file_count": sum(
                item["schema_valid"] for item in report["files"]
            ),
            "change_counts": dict(counts),
            "finished_at": datetime.now(timezone.utc).isoformat(),
            "status": (
                "complete"
                if not report["errors"] and not report["schema_invalid_files"]
                else "incomplete"
            ),
        }
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    print(
        json.dumps(
            {
                k: v
                for k, v in report.items()
                if k not in ("files", "errors", "schema_invalid_files")
            },
            indent=2,
        )
    )
    print(
        f"Repair errors: {len(report['errors'])}; schema-invalid files: {len(report['schema_invalid_files'])}"
    )
    return int(report["status"] != "complete")


if __name__ == "__main__":
    raise SystemExit(main())
