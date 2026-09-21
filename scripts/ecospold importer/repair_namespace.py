#!/usr/bin/env python3
"""Copy EcoSpold 1 files and add their missing default XML namespace."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from xml.parsers import expat


REPO_ROOT = Path(__file__).resolve().parents[2]
NAMESPACE = "http://www.EcoInvent.org/EcoSpold01"


def add_namespace(data):
    """Insert one declaration into the actual root start tag, preserving bytes."""
    parser = expat.ParserCreate(namespace_separator="}")
    root = []

    def start_element(name, attributes):
        if not root:
            root.append((name, parser.CurrentByteIndex))

    parser.StartElementHandler = start_element
    parser.Parse(data, True)
    name, offset = root[0]
    if name == f"{NAMESPACE}}}ecoSpold":
        return data, False
    if name != "ecoSpold":
        raise ValueError(f"Unexpected root element or namespace: {name!r}")
    token = b"<ecoSpold"
    if data[offset : offset + len(token)] != token:
        raise ValueError("Root tag is not encoded in an ASCII-compatible encoding")
    end = offset + len(token)
    declaration = f' xmlns="{NAMESPACE}"'.encode("ascii")
    # A root with an explicit empty xmlns needs a replacement, not a duplicate.
    # This is not present in the BAFU input; fail rather than rewrite attributes.
    start_tag_end = data.index(b">", end)
    if b"xmlns" in data[end:start_tag_end]:
        raise ValueError("Unqualified root already has a namespace declaration")
    repaired = data[:end] + declaration + data[end:]
    expat.ParserCreate(namespace_separator="}").Parse(repaired, True)
    return repaired, True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input", type=Path, default=REPO_ROOT / "data/raw/ecoSpold files"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "data/processed/ecospold1-namespace-fixed",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=REPO_ROOT / "reports/generated/ecospold1-namespace-repair.json",
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
    if output.exists():
        extra = {p.name for p in output.iterdir()} - {p.name for p in files}
        if extra:
            parser.error("Output contains extra files; choose an empty directory")
    output.mkdir(parents=True, exist_ok=True)
    report = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "input": str(source),
        "output": str(output),
        "namespace": NAMESPACE,
        "repair": "add_missing_default_namespace",
        "files": [],
        "errors": [],
    }
    for path in files:
        try:
            original = path.read_bytes()
            repaired, changed = add_namespace(original)
            destination = output / path.name
            if destination.is_symlink():
                raise ValueError("Refusing to write through an output symlink")
            if destination.exists():
                if destination.read_bytes() != repaired:
                    raise FileExistsError("Existing output differs; use a new directory")
            else:
                destination.write_bytes(repaired)
            report["files"].append({
                "file": path.name,
                "namespace_added": changed,
                "input_sha256": hashlib.sha256(original).hexdigest(),
                "output_sha256": hashlib.sha256(repaired).hexdigest(),
            })
        except Exception as exc:
            report["errors"].append({
                "file": path.name, "type": type(exc).__name__, "message": str(exc)
            })
    report["input_file_count"] = len(files)
    report["output_file_count"] = len(report["files"])
    report["namespace_added_count"] = sum(
        item["namespace_added"] for item in report["files"]
    )
    report["status"] = "failed" if report["errors"] else "complete"
    report["finished_at"] = datetime.now(timezone.utc).isoformat()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"Copied {report['output_file_count']}/{len(files)} files; "
        f"added namespace to {report['namespace_added_count']}; "
        f"errors: {len(report['errors'])}."
    )
    print(f"Output: {output}\nReport: {report_path}")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
