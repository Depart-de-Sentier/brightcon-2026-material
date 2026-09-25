#!/usr/bin/env python3
"""Try the standard Brightway EcoSpold 1 importer on original or repaired files."""

import argparse
from contextlib import nullcontext
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
import json
import os
from pathlib import Path
import sys
from time import perf_counter
import traceback

from date_compat import xml_date_parser
from timestamp_compat import iso_timestamp_parser

REPO_ROOT = Path(__file__).resolve().parents[2]


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=REPO_ROOT / "data/raw/ecoSpold files",
        help="Directory of XML files, or a single XML file.",
    )
    parser.add_argument("--project", default="bafu-2026-ecospold1-import-check")
    parser.add_argument("--database", default="BAFU:2026")
    parser.add_argument(
        "--iso-timestamps",
        action="store_true",
        help="Temporarily enable ISO timestamp parsing with fractional seconds and offsets.",
    )
    parser.add_argument(
        "--iso-dates",
        action="store_true",
        help="Temporarily parse XML dates with offsets, keeping their stated calendar day.",
    )
    parser.add_argument(
        "--brightway-dir",
        type=Path,
        default=REPO_ROOT / "artifacts/brightway",
        help="Brightway project storage (overrides BRIGHTWAY2_DIR for this process).",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=REPO_ROOT / "reports/generated/ecospold1-import.json",
        help="JSON report path; an existing report at this path is replaced.",
    )
    return parser.parse_args()


def source_file_from_traceback(tb):
    """Read the input path from importer frames without changing its extractor."""
    source = None
    for frame, _ in traceback.walk_tb(tb):
        if frame.f_globals.get("__name__", "").startswith("bw2io.extractors"):
            for key in ("filepath", "filename"):
                value = frame.f_locals.get(key)
                if isinstance(value, (str, Path)) and Path(value).is_file():
                    source = str(Path(value).resolve())
    return source


def main():
    args = parse_args()
    source = args.input.expanduser().resolve()
    storage = args.brightway_dir.expanduser().resolve()
    report_path = args.report.expanduser().resolve()
    started = perf_counter()
    report = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "python_executable": sys.executable,
        "importer": "bw2io.SingleOutputEcospold1Importer",
        "input": str(source),
        "project": args.project,
        "database": args.database,
        "brightway_dir": str(storage),
        "use_multiprocessing": False,
        "timestamp_parser": (
            "iso8601_compat" if args.iso_timestamps else "installed_default"
        ),
        "date_parser": "xml_schema_compat" if args.iso_dates else "installed_default",
        "database_written": False,
        "versions": {},
        "status": "failed",
        "stage": "input_check",
    }
    exit_code = 1
    try:
        if source.is_dir():
            files = [
                p
                for p in source.iterdir()
                if p.is_file()
                and p.suffix.lower() == ".xml"
                and p.name != "ElementaryFlows.xml"
            ]
        elif source.is_file() and source.suffix.lower() == ".xml":
            files = [source]
        else:
            raise ValueError(f"Expected an XML file or directory: {source}")
        if not files:
            raise ValueError(f"No importable XML files found in {source}")
        report["input_file_count"] = len(files)

        report["stage"] = "environment_setup"
        for package in ("bw2data", "bw2io", "pyecospold", "lxml"):
            try:
                report["versions"][package] = version(package)
            except PackageNotFoundError:
                report["versions"][package] = None
        storage.mkdir(parents=True, exist_ok=True)
        # Set this before importing Brightway, which initializes project storage.
        os.environ["BRIGHTWAY2_DIR"] = str(storage)
        import bw2data as bd
        import bw2io as bi

        report["stage"] = "project_setup"
        bd.projects.set_current(args.project)
        report["biosphere_database"] = bd.config.biosphere
        report["biosphere_database_present"] = bd.config.biosphere in bd.databases

        print(f"Input: {source} ({len(files)} XML files)", flush=True)
        print(f"Versions: {report['versions']}", flush=True)
        report["stage"] = "extraction"
        timestamp_context = (
            iso_timestamp_parser() if args.iso_timestamps else nullcontext()
        )
        date_context = xml_date_parser() if args.iso_dates else nullcontext()
        with timestamp_context, date_context:
            importer = bi.SingleOutputEcospold1Importer(
                str(source), args.database, use_mp=False
            )
        report["extracted_dataset_count"] = len(importer.data)
        if not importer.data:
            raise ValueError("The importer extracted no datasets")

        report["stage"] = "strategies"
        importer.apply_strategies()
        report["applied_strategies"] = importer.applied_strategies
        # bw2io prints and suppresses StrategyError; detect incomplete execution.
        if len(importer.applied_strategies) != len(importer.strategies):
            raise RuntimeError("Some importer strategies failed; see console output")

        report["stage"] = "statistics"
        datasets, exchanges, unlinked, *_ = importer.statistics()
        report["statistics"] = {
            "datasets": datasets,
            "exchanges": exchanges,
            "unlinked_exchanges": unlinked,
        }
        report["stage"] = "complete"
        report["status"] = "unlinked" if unlinked else "import_check_passed"
        exit_code = 2 if unlinked else 0
    except Exception as exc:
        report["error"] = {
            "type": type(exc).__name__,
            "message": str(exc),
            "source_file": source_file_from_traceback(exc.__traceback__),
            "traceback": traceback.format_exc(),
        }
        if hasattr(exc, "error_log"):
            report["error"]["xml_errors"] = [
                {
                    "line": entry.line,
                    "column": entry.column,
                    "type": entry.type_name,
                    "message": entry.message,
                }
                for entry in exc.error_log
            ]
        print(f"Import attempt failed during {report['stage']}:", file=sys.stderr)
        traceback.print_exc()
    finally:
        report["elapsed_seconds"] = round(perf_counter() - started, 3)
        report["finished_at"] = datetime.now(timezone.utc).isoformat()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"Status: {report['status']}; report: {report_path}", flush=True)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
