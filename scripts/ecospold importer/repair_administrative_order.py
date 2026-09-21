#!/usr/bin/env python3
"""Reorder EcoSpold 1 administrative elements, retaining complete original blocks."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from xml.parsers import expat

from repair_metadata import start_tag_end
from repair_namespace import NAMESPACE, REPO_ROOT

ORDER = {"dataEntryBy": 0, "dataGeneratorAndPublication": 1, "person": 2}
ADMIN = f"{NAMESPACE}}}administrativeInformation"
DATASET = f"{NAMESPACE}}}dataset"


def repair_administrative_order(data):
    """Move byte-exact child blocks, with preceding comments, into schema order."""
    parser = expat.ParserCreate(namespace_separator="}")
    stack, patches, changes = [], [], []
    active = None

    def start_element(name, attributes):
        nonlocal active
        stack.append((name, attributes))
        start = parser.CurrentByteIndex
        if name == ADMIN:
            if active is not None:
                raise ValueError("Unexpected nested administrativeInformation")
            dataset_number = next(
                (
                    attrs.get("number")
                    for tag, attrs in reversed(stack)
                    if tag == DATASET
                ),
                None,
            )
            active = {
                "depth": len(stack),
                "dataset_number": dataset_number,
                "content_start": start_tag_end(data, start),
                "children": [],
            }
        elif active is not None and len(stack) == active["depth"] + 1:
            namespace, _, local = name.rpartition("}")
            if namespace == NAMESPACE and local in ORDER:
                rank = ORDER[local]
            elif namespace and namespace != NAMESPACE:
                rank = 3  # Schema permits foreign-namespace extensions at the end.
            else:
                raise ValueError(f"Unexpected administrative child: {name!r}")
            open_end = start_tag_end(data, start)
            active["children"].append(
                {
                    "element": name,
                    "number": attributes.get("number"),
                    "rank": rank,
                    "open_end": open_end,
                    "self_closing": data[open_end - 2 : open_end] == b"/>",
                }
            )

    def end_element(name):
        nonlocal active
        if active is not None and len(stack) == active["depth"] + 1:
            child = active["children"][-1]
            child["end"] = (
                child["open_end"]
                if child["self_closing"]
                else start_tag_end(data, parser.CurrentByteIndex)
            )
        elif active is not None and name == ADMIN and len(stack) == active["depth"]:
            children = active["children"]
            indices = list(range(len(children)))
            ordered = sorted(indices, key=lambda index: children[index]["rank"])
            if indices != ordered:
                previous = active["content_start"]
                blocks = []
                for child in children:
                    blocks.append(data[previous : child["end"]])
                    previous = child["end"]
                patches.append(
                    (
                        active["content_start"],
                        previous,
                        b"".join(blocks[index] for index in ordered),
                    )
                )
                describe = lambda index: {
                    "element": children[index]["element"],
                    "number": children[index]["number"],
                    "block_sha256": hashlib.sha256(blocks[index]).hexdigest(),
                }
                changes.append(
                    {
                        "dataset_number": active["dataset_number"],
                        "order_before": [describe(index) for index in indices],
                        "order_after": [describe(index) for index in ordered],
                    }
                )
            active = None
        stack.pop()

    parser.StartElementHandler = start_element
    parser.EndElementHandler = end_element
    parser.Parse(data, True)
    repaired = data
    for start, end, replacement in sorted(patches, reverse=True):
        repaired = repaired[:start] + replacement + repaired[end:]
    expat.ParserCreate(namespace_separator="}").Parse(repaired, True)
    return repaired, changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=REPO_ROOT / "data/processed/ecospold1-source-number-fixed",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "data/processed/ecospold1-administrative-order-fixed",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=REPO_ROOT
        / "reports/generated/ecospold1-administrative-order-repair.json",
    )
    args = parser.parse_args()
    source, output, report_path = (
        value.expanduser().resolve() for value in (args.input, args.output, args.report)
    )
    raw = (REPO_ROOT / "data/raw").resolve()
    if not source.is_dir():
        parser.error(f"Input directory does not exist: {source}")
    if source.is_relative_to(output) or output.is_relative_to(source):
        parser.error("Input and output directories must be separate and non-nested")
    if output.is_relative_to(raw) or report_path.is_relative_to(raw):
        parser.error("Outputs and reports must be outside data/raw")
    if report_path.is_relative_to(source) or report_path.is_relative_to(output):
        parser.error("Keep the report outside both XML directories")
    files = sorted(
        p for p in source.iterdir() if p.is_file() and p.suffix.lower() == ".xml"
    )
    if not files:
        parser.error(f"No XML files found in {source}")
    if output.exists() and not output.is_dir():
        parser.error(f"Output is not a directory: {output}")
    if output.exists() and {p.name for p in output.iterdir()} - {p.name for p in files}:
        parser.error("Output contains extra files; choose an empty directory")
    output.mkdir(parents=True, exist_ok=True)
    report = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "input": str(source),
        "output": str(output),
        "repair": "administrative_element_order",
        "files": [],
        "errors": [],
    }
    for path in files:
        try:
            original = path.read_bytes()
            repaired, changes = repair_administrative_order(original)
            destination = output / path.name
            if destination.is_symlink():
                raise ValueError("Refusing to write through an output symlink")
            if destination.exists():
                if destination.read_bytes() != repaired:
                    raise FileExistsError(
                        "Existing output differs; use a new directory"
                    )
            else:
                destination.write_bytes(repaired)
            report["files"].append(
                {
                    "file": path.name,
                    "changes": changes,
                    "input_sha256": hashlib.sha256(original).hexdigest(),
                    "output_sha256": hashlib.sha256(repaired).hexdigest(),
                }
            )
        except Exception as exc:
            report["errors"].append(
                {"file": path.name, "type": type(exc).__name__, "message": str(exc)}
            )
    report["input_file_count"] = len(files)
    report["output_file_count"] = len(report["files"])
    report["changed_file_count"] = sum(
        bool(item["changes"]) for item in report["files"]
    )
    report["reordered_section_count"] = sum(
        len(item["changes"]) for item in report["files"]
    )
    report["status"] = "failed" if report["errors"] else "complete"
    report["finished_at"] = datetime.now(timezone.utc).isoformat()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"Copied {report['output_file_count']}/{len(files)} files; "
        f"reordered {report['reordered_section_count']} sections in "
        f"{report['changed_file_count']} files; errors: {len(report['errors'])}."
    )
    print(f"Output: {output}\nReport: {report_path}")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
