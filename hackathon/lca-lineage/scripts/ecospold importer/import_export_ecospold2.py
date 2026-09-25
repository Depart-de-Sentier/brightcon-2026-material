#!/usr/bin/env python3
"""Apply all approved mappings, audit exclusions, write Brightway and EcoSpold 2."""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
import math
import os
from pathlib import Path
import shutil
import tempfile

from tqdm import tqdm

from ecospold2_export import (
    CONTEXT,
    SOURCE_INDEX,
    audit_and_exclude,
    dumps,
    export_datasets,
    ids,
    label,
)
from ecospold2_reimport import reimport_ecospold2
from mapped_import import BIOSPHERE_STAGES, counts, import_mapped

ROOT = Path(__file__).resolve().parents[2]


def check_roundtrip(data, directory, biosphere):
    """Compare every retained row after real XML extraction and UUID linking."""
    from bw2io.utils import es2_activity_hash

    reread = reimport_ecospold2(directory, "BAFU-ecospold2-verification", biosphere)
    if any(True for _ in reread.unlinked):
        raise ValueError("The EcoSpold 2 re-import contains unlinked exchanges")
    by_activity = {ds["activity"]: ds for ds in reread.data}
    originals = {(ds["database"], ds["code"]): ds for ds in data}
    if len(by_activity) != len(data):
        raise ValueError("Dataset count changed during re-import")
    checked = 0
    for ds in tqdm(data, desc="Compare re-import", unit="dataset", mininterval=0.5):
        after = by_activity[ids(ds)[0]]
        tags = dict(ds["tags"])
        expected_rows = sorted(ds["exchanges"], key=lambda e: e["type"] == "biosphere")
        if (
            after["name"] != label(ds["name"])
            or after["location"] != ds["location"]
            or after["unit"] != ds["unit"]
            or after["reference product"] != label(ds["reference product"])
            or after["start_date"] != tags["ecoSpold01startDate"]
            or after["end_date"] != tags["ecoSpold01endDate"]
            or len(after["exchanges"]) != len(expected_rows)
        ):
            raise ValueError(f"Dataset changed during re-import: {ds['filename']}")
        for before, actual in zip(expected_rows, after["exchanges"]):
            target = tuple(before["input"])
            expected_input = (
                target
                if before["type"] == "biosphere"
                else (reread.db_name, es2_activity_hash(*ids(originals[target])))
            )
            if (
                tuple(actual["input"]) != expected_input
                or actual["type"] != before["type"]
                or actual["unit"] != before["unit"]
                or actual["amount"] != before["amount"]
                or actual.get("uncertainty type", 0)
                != before.get("uncertainty type", 0)
                or actual.get("negative", False) != before.get("negative", False)
            ):
                raise ValueError(
                    f"Exchange changed during re-import: {ds['filename']} {before[SOURCE_INDEX]}"
                )
            for key in ("loc", "scale", "minimum", "maximum"):
                if key in before and (
                    key not in actual
                    or not math.isclose(
                        before[key], actual[key], rel_tol=1e-12, abs_tol=1e-15
                    )
                ):
                    raise ValueError(
                        f"Uncertainty {key} changed: {ds['filename']} {before[SOURCE_INDEX]}"
                    )
            checked += 1
    return {
        "datasets": len(data),
        "exchanges": checked,
        "unlinked": 0,
        "amounts": "exact float equality",
        "uncertainty_relative_tolerance": 1e-12,
        "strategies": "UUID linking only; preserves uncertainty and negative lognormal flags",
    }


def file_hash(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def check_database(data, stored):
    """Check the database readback against the exact retained source records."""
    if len(stored) != len(data):
        raise ValueError("Written dataset count differs")
    for ds in tqdm(data, desc="Verify database write", unit="dataset", mininterval=0.5):
        actual = stored[(ds["database"], ds["code"])]
        # Brightway also adds output keys IN PLACE to the importer when writing.
        # Check their meaning, then compare the original inventory dictionaries.
        expected_output = (ds["database"], ds["code"])
        for exc in actual["exchanges"]:
            if tuple(exc.get("output", ())) != expected_output:
                raise ValueError(f"Wrong stored exchange output: {ds['filename']}")
        before_rows = Counter(
            dumps({k: v for k, v in e.items() if k != "output"})
            for e in ds["exchanges"]
        )
        after_rows = Counter(
            dumps({k: v for k, v in e.items() if k != "output"})
            for e in actual["exchanges"]
        )
        if before_rows != after_rows:
            raise ValueError(f"Written exchange records differ: {ds['filename']}")
        for key, value in ds.items():
            if (
                key == "type"
                and value == "process"
                and actual.get(key) == "processwithreferenceproduct"
            ):
                # Brightway 4 normalizes this node label during Database.write.
                continue
            if key != "exchanges" and dumps(actual.get(key)) != dumps(value):
                raise ValueError(
                    f"Written dataset metadata differs: {ds['filename']} {key}"
                )


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input", type=Path, default=ROOT / "data/processed/ecospold1-schema-fixed"
    )
    parser.add_argument(
        "--output", type=Path, default=ROOT / "data/processed/ecospold2-biosphere310"
    )
    parser.add_argument("--project", default="bafu-2026-biosphere-310")
    parser.add_argument("--database", default="BAFU:2026-mapped")
    parser.add_argument("--biosphere", default="ecoinvent-3.10-biosphere")
    parser.add_argument("--storage", type=Path, default=ROOT / "artifacts/brightway")
    parser.add_argument(
        "--reuse-existing",
        action="store_true",
        help="Verify an existing target database matches the rebuilt inventory; never overwrite it",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Export and verify without writing an inventory database",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite output if it already exists",
    )
    return parser.parse_args()


def main():
    args = arguments()
    if not args.input.is_dir() or not any(args.input.glob("*.xml")):
        raise FileNotFoundError(f"No repaired XML in {args.input}")
    if args.overwrite:
        shutil.rmtree(args.output)
        args.reuse_existing = True
    if args.output.exists():
            raise FileExistsError(
                f"Output already exists: {args.output}; choose a new --output"
            )
    args.storage.mkdir(parents=True, exist_ok=True)
    os.environ["BRIGHTWAY2_DIR"] = str(args.storage.resolve())
    import bw2data as bd
    import bw2io as bi
    from pyecospold import Defaults

    if args.project not in bd.projects:
        bi.install_project("ecoinvent-3.10-biosphere", project_name=args.project)
    bd.projects.set_current(args.project)
    if args.biosphere not in bd.databases:
        raise ValueError(f"Missing biosphere {args.biosphere}")
    if args.database in bd.databases and not args.reuse_existing:
        raise ValueError(
            f"Database already exists: {args.database}; choose a new --database"
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Failed work is kept for diagnosis; only a complete run gets the final name.
    work = Path(tempfile.mkdtemp(prefix=".ecospold2-building-", dir=args.output.parent))
    report = {
        "status": "running",
        "project": args.project,
        "database": args.database,
        "biosphere": args.biosphere,
        "storage": str(args.storage.resolve()),
        "source": str(args.input.resolve()),
        "output": str(args.output.resolve()),
        "started_at": datetime.now(timezone.utc).isoformat(),
        "versions": {p: version(p) for p in ("bw2data", "bw2io", "pyecospold", "lxml")},
        "exclusion_policy": "Exclude only unlinked biosphere exchanges after approved mappings; retain every occurrence in audit/excluded-exchanges.jsonl",
        "export_context_uuid": str(CONTEXT),
        "schema": Defaults.SCHEMA_V2_FILE,
    }
    try:
        print(
            f"Project: {args.project}; database: {args.database}\nWorking directory: {work}",
            flush=True,
        )
        mapping_dir = ROOT / "schemas/mappings"
        mapping_names = [
            "bafu-2026-technosphere.json",
            "bafu-2026-technosphere-context.json",
        ]
        mapping_names += [f"bafu-2026-biosphere-{s}.json" for s in BIOSPHERE_STAGES]
        report["mappings"] = [
            {
                "file": n,
                "sha256": hashlib.sha256((mapping_dir / n).read_bytes()).hexdigest(),
            }
            for n in mapping_names
        ]
        (work / "audit/mapping-files").mkdir(parents=True)
        for name in mapping_names:
            shutil.copyfile(mapping_dir / name, work / "audit/mapping-files" / name)
        report["schema_files"] = {
            p.name: file_hash(p)
            for p in Path(Defaults.SCHEMA_V2_FILE).parent.glob("*.xsd")
        }
        report["scripts"] = {
            name: file_hash(Path(__file__).with_name(name))
            for name in (
                "import_export_ecospold2.py",
                "ecospold2_export.py",
                "ecospold2_reimport.py",
                "mapped_import.py",
                "biosphere_migrations.py",
                "technosphere_migrations.py",
                "date_compat.py",
                "timestamp_compat.py",
            )
        }
        importer = import_mapped(
            args.input,
            args.database,
            args.biosphere,
            mapping_dir,
            work / "audit/migrations",
        )
        report["before_exclusions"] = counts(importer.data)
        report["excluded"], report["source_files"] = audit_and_exclude(
            importer.data, args.input, work / "audit"
        )
        report["retained"] = counts(importer.data)
        report["preserved_uncertainty"] = {
            "negative_lognormals": sum(
                e.get("uncertainty type") == 2 and e["amount"] < 0
                for d in importer.data
                for e in d["exchanges"]
            ),
            "lognormal_scales_above_default_importer_cutoff": sum(
                e.get("uncertainty type") == 2 and e.get("scale", 0) > 2.5
                for d in importer.data
                for e in d["exchanges"]
            ),
        }
        report["shortened_activity_names"] = [
            {"original": d["name"], "xml_label": label(d["name"])}
            for d in importer.data
            if len(d["name"]) > 120
        ]
        biosphere = bd.Database(args.biosphere).load()
        report["shortened_biosphere_names"] = [
            {"uuid": k[1], "original": v["name"], "xml_label": label(v["name"])}
            for k, v in biosphere.items()
            if len(v["name"]) > 120
        ]
        report["audit_files"] = {
            p.name: file_hash(p) for p in (work / "audit").glob("*.jsonl")
        }
        report["biosphere_catalog_sha256"] = hashlib.sha256(
            dumps(
                sorted(
                    (key[1], value["name"], value["categories"], value["unit"])
                    for key, value in biosphere.items()
                )
            ).encode()
        ).hexdigest()
        report["files"] = export_datasets(
            importer.data, biosphere, args.input, work / "datasets"
        )
        report["roundtrip"] = check_roundtrip(
            importer.data, work / "datasets", args.biosphere
        )
        if not args.check_only:
            # Validate the complete export before creating the new database.
            if args.database in bd.databases:
                if not args.reuse_existing:
                    raise ValueError("Target database was created by another process")
                db = bd.Database(args.database)
                report["database_written"] = False
            else:
                db = importer.write_database(
                    bafu_excluded_biosphere_exchanges=report["excluded"],
                    bafu_export_audit=str(
                        args.output / "audit/excluded-exchanges.jsonl"
                    ),
                    bafu_mappings=report["mappings"],
                )
                report["database_written"] = True
            check_database(importer.data, db.load())
            report["database_readback"] = "passed"
            report["existing_database_verified"] = not report["database_written"]
        else:
            report["database_written"] = False
        report["status"] = "passed"
        report["finished_at"] = datetime.now(timezone.utc).isoformat()
        shutil.copyfile(ROOT / "docs/bafu-2026-ecospold2-export.md", work / "README.md")
        shutil.copyfile(
            Path(__file__).with_name("ecospold2_reimport.py"),
            work / "ecospold2_reimport.py",
        )
        (work / "manifest.json").write_text(json.dumps(report, indent=2) + "\n")
        work.rename(args.output)
    except Exception as error:
        report.update(status="failed", error=f"{type(error).__name__}: {error}")
        (work / "manifest.json").write_text(json.dumps(report, indent=2) + "\n")
        print(f"Failed run retained at {work}", flush=True)
        raise
    print(
        f"Exported {len(importer.data):,} datasets; excluded {report['excluded']:,} audited biosphere exchanges."
    )
    print(f"Output: {args.output}\nManifest: {args.output / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
