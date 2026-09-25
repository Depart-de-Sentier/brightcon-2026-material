#!/usr/bin/env python3
"""Assign dataset-local IDs to duplicate exchanges without merging inventory rows."""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from xml.parsers import expat

from lxml import etree
from tqdm import tqdm

from repair_metadata import ATTRIBUTE, COMMENT_PREFIX, start_tag_end
from repair_namespace import NAMESPACE, REPO_ROOT

NS = f"{{{NAMESPACE}}}"
MAX_INDEX = 2**31 - 1


def index_number(value):
    """Compare integer identities, leaving separate range defects unchanged.

    A unique ID of zero occurs in BAFU. It must not prevent the other duplicate
    IDs in that dataset from being repaired or cause the file to be omitted.
    Newly assigned IDs always satisfy TIndexNumber's positive 32-bit range.
    """
    if value is None or not re.fullmatch(r"[+-]?[0-9]+", value.strip()):
        raise ValueError(f"Invalid exchange/reference number: {value!r}")
    return int(value)


def repair_exchange_numbers(data):
    """Keep first occurrences and replace later duplicates with unused local IDs.

    All original IDs are reserved before assigning the lowest available positive
    integers. Ambiguous allocation references or foreign extensions in an affected
    dataset cause an error, rather than a guessed reference mapping.
    """
    root = etree.fromstring(
        data, etree.XMLParser(resolve_entities=False, no_network=True)
    )
    if root.getroottree().docinfo.doctype:
        raise ValueError("DOCTYPE declarations are not supported by this repair")
    if root.tag != NS + "ecoSpold":
        raise ValueError("Expected a namespaced EcoSpold 1 root")
    plans = {}
    for dataset_index, dataset in enumerate(root.findall(NS + "dataset"), 1):
        exchanges = dataset.findall(f"{NS}flowData/{NS}exchange")
        numbers = [index_number(exc.get("number")) for exc in exchanges]
        duplicates = {number for number, count in Counter(numbers).items() if count > 1}
        if not duplicates:
            continue
        for node in dataset.iter():
            if not isinstance(node.tag, str):
                continue
            if etree.QName(node).namespace != NAMESPACE or any(
                name.startswith("{") for name in node.attrib
            ):
                raise ValueError(
                    f"Dataset {dataset_index}: cannot audit foreign extension references"
                )
        references = set()
        for allocation in dataset.findall(f"{NS}flowData/{NS}allocation"):
            references.add(index_number(allocation.get("referenceToCoProduct")))
            references.update(
                index_number(element.text)
                for element in allocation.findall(NS + "referenceToInputOutput")
            )
        if references & duplicates:
            raise ValueError(
                f"Dataset {dataset_index}: ambiguous allocation references to duplicate "
                f"exchange numbers {sorted(references & duplicates)}"
            )

        # Reserve references too: a new ID must not accidentally resolve a dangling ref.
        used = set(numbers) | references
        seen = set()
        candidate = 1
        for exchange_index, (exchange, number) in enumerate(zip(exchanges, numbers), 1):
            if number not in seen:
                seen.add(number)
                continue
            while candidate in used:
                candidate += 1
            if candidate > MAX_INDEX:
                raise ValueError("No unused TIndexNumber available")
            plans[dataset_index, exchange_index] = {
                "element": "exchange",
                "dataset_index": dataset_index,
                "dataset_number": dataset.get("number"),
                "exchange_index": exchange_index,
                "attribute": "number",
                "number": str(candidate),
                "original_value": exchange.get("number"),
                "replacement_value": str(candidate),
                "reason": "duplicate_number_within_dataset",
                "action": "reassign_number_preserving_inventory_row",
            }
            used.add(candidate)

    if not plans:
        return data, []

    parser = expat.ParserCreate(namespace_separator="}")
    stack, patches, changes = [], [], []
    dataset_index = exchange_index = 0
    prefix = (f"{NAMESPACE}}}ecoSpold", f"{NAMESPACE}}}dataset")

    def start_element(name, attributes):
        nonlocal dataset_index, exchange_index
        stack.append(name)
        if tuple(stack) == prefix:
            dataset_index += 1
            exchange_index = 0
        elif tuple(stack) == prefix + (
            f"{NAMESPACE}}}flowData",
            f"{NAMESPACE}}}exchange",
        ):
            exchange_index += 1
            change = plans.get((dataset_index, exchange_index))
            if change is None:
                return
            start = parser.CurrentByteIndex
            tag = data[start : start_tag_end(data, start)]
            matches = [m for m in ATTRIBUTE.finditer(tag) if m.group(1) == b"number"]
            if len(matches) != 1:
                raise ValueError("Cannot locate unique exchange number attribute")
            match = matches[0]
            # Preserve lexical forms too, e.g. leading zeroes or character references.
            change["original_xml_value"] = match.group(3).decode("ascii")
            payload = json.dumps(change, ensure_ascii=True, sort_keys=True).replace(
                "-", "\\u002d"
            )
            comment = f"<!--{COMMENT_PREFIX}{payload} -->".encode("ascii")
            patches.extend(
                [
                    (start, start, comment),
                    (
                        start + match.start(3),
                        start + match.end(3),
                        change["replacement_value"].encode("ascii"),
                    ),
                ]
            )
            changes.append(change)

    parser.StartElementHandler = start_element
    parser.EndElementHandler = lambda name: stack.pop()
    parser.Parse(data, True)
    if len(changes) != len(plans):
        raise ValueError("Not all planned exchange numbers were located")
    chunks, previous = [], 0
    for start, end, replacement in sorted(patches):
        chunks.extend((data[previous:start], replacement))
        previous = end
    chunks.append(data[previous:])
    repaired = b"".join(chunks)
    expat.ParserCreate(namespace_separator="}").Parse(repaired, True)
    return repaired, changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=REPO_ROOT / "data/processed/ecospold1-administrative-order-fixed",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "data/processed/ecospold1-exchange-numbers-fixed",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=REPO_ROOT / "reports/generated/ecospold1-exchange-number-repair.json",
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
        "repair": "duplicate_exchange_numbers",
        "files": [],
        "errors": [],
    }
    for path in tqdm(
        files, desc="Exchange numbers", unit="file", dynamic_ncols=True, mininterval=0.5
    ):
        try:
            original = path.read_bytes()
            repaired, changes = repair_exchange_numbers(original)
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
    report["renumbered_exchange_count"] = sum(
        len(item["changes"]) for item in report["files"]
    )
    report["status"] = "failed" if report["errors"] else "complete"
    report["finished_at"] = datetime.now(timezone.utc).isoformat()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"Copied {report['output_file_count']}/{len(files)} files; "
        f"renumbered {report['renumbered_exchange_count']} exchanges in "
        f"{report['changed_file_count']} files; errors: {len(report['errors'])}."
    )
    print(f"Output: {output}\nReport: {report_path}")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
