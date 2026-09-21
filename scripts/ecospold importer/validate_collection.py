#!/usr/bin/env python3
"""Validate all repaired XML and compare every inventory row with the raw release."""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

from lxml import etree
from pyecospold import Defaults

from repair_namespace import REPO_ROOT
from repair_schema import BOOL_ATTRIBUTES


def semantic_attributes(element, aliases, exchange=False):
    attrs = dict(element.attrib)
    for name in BOOL_ATTRIBUTES.intersection(attrs):
        attrs[name] = attrs[name].lower()
    if "location" in attrs:
        attrs["location"] = aliases.get(attrs["location"], attrs["location"])
    if exchange:
        # The repair changes local IDs, not the ordered inventory rows they label.
        attrs.pop("number", None)
        cas = attrs.get("CASNumber")
        if cas is not None and not re.fullmatch(r"[0-9]{2,7}-[0-9]{2}-[0-9]", cas):
            del attrs["CASNumber"]
    else:
        # Unsupported referenceFunction.text is retained in audit comments.
        attrs.pop("text", None)
    return attrs


def exchange_signature(element, aliases):
    children = [
        (etree.QName(child).localname, (child.text or "").strip(), dict(child.attrib))
        for child in element
        if isinstance(child.tag, str)
    ]
    return semantic_attributes(element, aliases, exchange=True), children


def verify_inventory(raw, repaired, aliases):
    original_datasets = raw.findall("{*}dataset")
    repaired_datasets = repaired.findall("{*}dataset")
    if len(original_datasets) != len(repaired_datasets):
        raise AssertionError("Dataset count changed")
    exchanges_checked = 0
    for original, result in zip(original_datasets, repaired_datasets):
        original_exchanges = original.findall("{*}flowData/{*}exchange")
        result_exchanges = result.findall("{*}flowData/{*}exchange")
        if len(original_exchanges) != len(result_exchanges):
            raise AssertionError("Exchange count changed")
        numbers = [int(element.get("number")) for element in result_exchanges]
        if len(numbers) != len(set(numbers)):
            raise AssertionError("Duplicate exchange IDs remain")
        for index, (before, after) in enumerate(
            zip(original_exchanges, result_exchanges), 1
        ):
            if exchange_signature(before, aliases) != exchange_signature(
                after, aliases
            ):
                raise AssertionError(f"Inventory payload changed at exchange {index}")
        for element_name in ("referenceFunction", "geography"):
            before = original.find(
                f"{{*}}metaInformation/{{*}}processInformation/{{*}}{element_name}"
            )
            after = result.find(
                f"{{*}}metaInformation/{{*}}processInformation/{{*}}{element_name}"
            )
            if element_name == "geography":
                before_attrs, after_attrs = dict(before.attrib), dict(after.attrib)
                after_attrs["location"] = aliases.get(
                    after_attrs.get("location"), after_attrs.get("location")
                )
            else:
                before_attrs = semantic_attributes(before, aliases)
                after_attrs = semantic_attributes(after, aliases)
            if before_attrs != after_attrs:
                raise AssertionError(f"{element_name} payload changed")
        exchanges_checked += len(result_exchanges)
    return len(repaired_datasets), exchanges_checked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=REPO_ROOT / "data/processed/ecospold1-schema-fixed",
    )
    parser.add_argument(
        "--raw", type=Path, default=REPO_ROOT / "data/raw/ecoSpold files"
    )
    parser.add_argument(
        "--repair-report",
        type=Path,
        default=REPO_ROOT / "reports/generated/ecospold1-schema-repair.json",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=REPO_ROOT / "reports/generated/ecospold1-final-validation.json",
    )
    args = parser.parse_args()
    manifest = json.loads(args.repair_report.read_text())
    expected = {item["file"]: item["output_sha256"] for item in manifest["files"]}
    aliases = {
        alias: original for original, alias in manifest["location_aliases"].items()
    }
    files = {path.name: path for path in args.input.glob("*.xml")}
    raw_files = {path.name: path for path in args.raw.glob("*.xml")}
    report = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "input": str(args.input.resolve()),
        "raw": str(args.raw.resolve()),
        "schema": str(Defaults.SCHEMA_V1_FILE),
        "files": [],
        "errors": [],
        "inventory_comparison": "All ordered exchange attributes/children and reference-function/geography metadata; only recorded local IDs, invalid CAS attributes, boolean spelling, unsupported referenceFunction.text, and reversible location aliases may differ.",
    }
    counts = Counter()
    if set(files) != set(raw_files) or set(files) != set(expected):
        report["errors"].append(
            {
                "type": "file_set_mismatch",
                "output": len(files),
                "raw": len(raw_files),
                "manifest": len(expected),
            }
        )
    schema = etree.XMLSchema(file=Defaults.SCHEMA_V1_FILE)
    for name, path in sorted(files.items()):
        try:
            payload = path.read_bytes()
            checksum = hashlib.sha256(payload).hexdigest()
            if checksum != expected[name]:
                raise AssertionError("Output changed since repair manifest")
            tree = etree.fromstring(payload)
            schema.assertValid(tree)
            raw_payload = raw_files[name].read_bytes()
            datasets, exchanges = verify_inventory(
                etree.fromstring(raw_payload), tree, aliases
            )
            counts.update(files=1, datasets=datasets, exchanges=exchanges)
            report["files"].append(
                {
                    "file": name,
                    "sha256": checksum,
                    "raw_sha256": hashlib.sha256(raw_payload).hexdigest(),
                    "schema_valid": True,
                    "inventory_unchanged": True,
                }
            )
        except Exception as exc:
            report["errors"].append(
                {"file": name, "type": type(exc).__name__, "message": str(exc)}
            )
    report.update(
        {
            "counts": dict(counts),
            "status": "passed" if not report["errors"] else "failed",
            "finished_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(
        json.dumps(
            {
                key: value
                for key, value in report.items()
                if key not in ("files", "errors")
            },
            indent=2,
        )
    )
    print(f"Errors: {len(report['errors'])}; report: {args.report}")
    return int(bool(report["errors"]))


if __name__ == "__main__":
    raise SystemExit(main())
