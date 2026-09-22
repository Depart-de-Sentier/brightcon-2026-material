#!/usr/bin/env python3
"""Preserve schema-incompatible metadata in XML comments and a JSON log."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from xml.parsers import expat

from tqdm import tqdm

from repair_namespace import NAMESPACE, REPO_ROOT

RULES = {
    "publisher": ("source", "publisher", 40, "ecospold1-dates-fixed"),
    "company-code": ("person", "companyCode", 7, "ecospold1-publisher-fixed"),
    "source-number": ("source", "sourceNumber", None, "ecospold1-company-code-fixed"),
}
ATTRIBUTE = re.compile(rb"""\s+([^\s=<>/]+)\s*=\s*(["'])(.*?)\2""", re.DOTALL)
COMMENT_PREFIX = " BAFU schema repair: "


def start_tag_end(data, start):
    quote = None
    for index in range(start, len(data)):
        char = data[index]
        if quote is not None:
            if char == quote:
                quote = None
        elif char in (34, 39):
            quote = char
        elif char == 62:
            return index + 1
    raise ValueError("Unterminated XML start tag")


def repair_metadata(data, rule):
    element, attribute, limit, _ = RULES[rule]
    parser = expat.ParserCreate(namespace_separator="}")
    patches, changes = [], []

    def start_element(name, attributes):
        if name != f"{NAMESPACE}}}{element}" or attribute not in attributes:
            return
        value = attributes[attribute]
        if limit is not None and len(value) <= limit:
            return
        start = parser.CurrentByteIndex
        tag = data[start : start_tag_end(data, start)]
        matches = [
            m for m in ATTRIBUTE.finditer(tag) if m.group(1) == attribute.encode()
        ]
        if len(matches) != 1:
            raise ValueError(f"Cannot locate unique {attribute!r} attribute")
        match = matches[0]
        change = {
            "element": element,
            "number": attributes.get("number"),
            "attribute": attribute,
            "original_value": value,
            "reason": "unsupported_attribute" if limit is None else "max_length",
            "limit": limit,
            "action": "move_to_xml_comment",
        }
        if rule == "company-code":
            # person.companyCode is required; TCompanyCode permits an empty value.
            change["action"] = "move_value_to_xml_comment"
            change["replacement_value"] = ""
        # Escape hyphens in JSON so arbitrary values cannot create '--' in XML comments.
        payload = json.dumps(change, ensure_ascii=True, sort_keys=True).replace(
            "-", "\\u002d"
        )
        comment = f"<!--{COMMENT_PREFIX}{payload} -->".encode("ascii")
        if rule == "company-code":
            patches.append((start + match.start(3), start + match.end(3), b""))
        else:
            patches.append((start + match.start(), start + match.end(), b""))
        patches.append((start, start, comment))
        changes.append(change)

    parser.StartElementHandler = start_element
    parser.Parse(data, True)
    repaired = data
    for start, end, replacement in sorted(patches, reverse=True):
        repaired = repaired[:start] + replacement + repaired[end:]
    expat.ParserCreate(namespace_separator="}").Parse(repaired, True)
    return repaired, changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rule", choices=RULES)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace differing generated XML copies in the output directory.",
    )
    args = parser.parse_args()
    source = (
        (args.input or REPO_ROOT / "data/processed" / RULES[args.rule][3])
        .expanduser()
        .resolve()
    )
    output = (
        (args.output or REPO_ROOT / f"data/processed/ecospold1-{args.rule}-fixed")
        .expanduser()
        .resolve()
    )
    report_path = (
        (
            args.report
            or REPO_ROOT / f"reports/generated/ecospold1-{args.rule}-repair.json"
        )
        .expanduser()
        .resolve()
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
        "rule": args.rule,
        "files": [],
        "errors": [],
    }
    for path in tqdm(
        files, desc=args.rule, unit="file", dynamic_ncols=True, mininterval=0.5
    ):
        try:
            original = path.read_bytes()
            repaired, changes = repair_metadata(original, args.rule)
            destination = output / path.name
            if destination.is_symlink():
                raise ValueError("Refusing to write through an output symlink")
            if destination.exists():
                if destination.read_bytes() != repaired:
                    if not args.overwrite:
                        raise FileExistsError(
                            "Existing output differs; use a new directory or --overwrite"
                        )
                    destination.write_bytes(repaired)
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
    report["changed_attribute_count"] = sum(
        len(item["changes"]) for item in report["files"]
    )
    report["status"] = "failed" if report["errors"] else "complete"
    report["finished_at"] = datetime.now(timezone.utc).isoformat()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"{args.rule}: copied {report['output_file_count']}/{len(files)} files; "
        f"preserved {report['changed_attribute_count']} invalid attributes in comments; "
        f"errors: {len(report['errors'])}."
    )
    print(f"Output: {output}\nReport: {report_path}")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
