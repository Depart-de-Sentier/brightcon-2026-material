#!/usr/bin/env python3
"""Use EcoSpold 1 year/month elements for partial dates, preserving their values."""

import argparse
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from xml.parsers import expat

from repair_namespace import NAMESPACE, REPO_ROOT


def repair_dates(data):
    """Rename partial-date tags without reserializing XML or adding precision."""
    parser = expat.ParserCreate(namespace_separator="}")
    stack, patches, changes = [], [], []
    active = None

    def start_element(name, attributes):
        nonlocal active
        if active is not None:
            raise ValueError("Unexpected nested element inside a date")
        if (
            stack
            and stack[-1] == f"{NAMESPACE}}}timePeriod"
            and name in (f"{NAMESPACE}}}startDate", f"{NAMESPACE}}}endDate")
        ):
            active = {
                "start": parser.CurrentByteIndex,
                "tag": name.split("}")[-1],
                "text": [],
            }
        stack.append(name)

    def characters(text):
        if active is not None:
            active["text"].append(text)

    def end_element(name):
        nonlocal active
        if active is not None:
            value = "".join(active["text"]).strip()
            match = re.fullmatch(r"(\d{4})(?:-(\d{2}))?", value)
            if match:
                year, month = match.groups()
                date(int(year), int(month or 1), 1)  # Reject invalid years/months.
                old = active["tag"]
                new = old.removesuffix("Date") + ("YearMonth" if month else "Year")
                start, end = active["start"], parser.CurrentByteIndex
                if not data[start:].startswith(f"<{old}".encode()):
                    raise ValueError(
                        "Expected an unprefixed, ASCII-compatible date tag"
                    )
                if not data[end:].startswith(f"</{old}".encode()):
                    raise ValueError("Expected an explicit date end tag")
                patches.extend(
                    [
                        (start + 1, start + 1 + len(old), new.encode()),
                        (end + 2, end + 2 + len(old), new.encode()),
                    ]
                )
                changes.append(
                    {"element_before": old, "element_after": new, "value": value}
                )
            active = None
        stack.pop()

    parser.StartElementHandler = start_element
    parser.CharacterDataHandler = characters
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
        default=REPO_ROOT / "data/processed/ecospold1-namespace-fixed",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "data/processed/ecospold1-dates-fixed",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=REPO_ROOT / "reports/generated/ecospold1-date-repair.json",
    )
    args = parser.parse_args()
    source = args.input.expanduser().resolve()
    output = args.output.expanduser().resolve()
    report_path = args.report.expanduser().resolve()
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
        "repair": "use_year_or_year_month_elements_for_partial_dates",
        "files": [],
        "errors": [],
    }
    for path in files:
        try:
            original = path.read_bytes()
            repaired, changes = repair_dates(original)
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
    report["changed_date_count"] = sum(len(item["changes"]) for item in report["files"])
    report["status"] = "failed" if report["errors"] else "complete"
    report["finished_at"] = datetime.now(timezone.utc).isoformat()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"Copied {report['output_file_count']}/{len(files)} files; "
        f"corrected {report['changed_date_count']} date elements in "
        f"{report['changed_file_count']} files; errors: {len(report['errors'])}."
    )
    print(f"Output: {output}\nReport: {report_path}")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
