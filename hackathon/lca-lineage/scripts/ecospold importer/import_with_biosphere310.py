#!/usr/bin/env python3
"""Create a project with biosphere 3.10 and try importing the repaired BAFU files."""

import os
from pathlib import Path

from date_compat import xml_date_parser
from timestamp_compat import iso_timestamp_parser

ROOT = Path(__file__).resolve().parents[2]
PROJECT = "bafu-2026-biosphere-310"
DATABASE = "BAFU:2026"


def main():
    source = ROOT / "data/processed/ecospold1-schema-fixed"
    if not any(source.glob("*.xml")):
        raise FileNotFoundError(f"No repaired XML files found in {source}")

    # Set storage before importing Brightway; this directory is ignored by Git.
    storage = ROOT / "artifacts/brightway"
    storage.mkdir(parents=True, exist_ok=True)
    os.environ["BRIGHTWAY2_DIR"] = str(storage)
    import bw2data as bd
    import bw2io as bi

    if PROJECT not in bd.projects:
        bi.install_project("ecoinvent-3.10-biosphere", project_name=PROJECT)
    bd.projects.set_current(PROJECT)
    if DATABASE in bd.databases:
        raise RuntimeError(f"{DATABASE} already exists; refusing to overwrite it")
    if bd.config.biosphere not in bd.databases:
        raise RuntimeError("The project has no default biosphere database")
    print(f"Project: {PROJECT}; storage: {storage}", flush=True)
    print(f"Biosphere: {bd.config.biosphere} ({len(bd.Database(bd.config.biosphere))} flows)")

    # These local adapters handle valid ISO dates/timestamps without editing XML.
    with iso_timestamp_parser(), xml_date_parser():
        importer = bi.SingleOutputEcospold1Importer(
            str(source), DATABASE, use_mp=False
        )
    importer.apply_strategies()
    if len(importer.applied_strategies) != len(importer.strategies):
        raise RuntimeError("Some importer strategies failed; see console output")
    _, _, unlinked, *_ = importer.statistics()
    if unlinked:
        print(f"{unlinked:,} exchanges remain unlinked; BAFU database not written.")
        return 2
    importer.write_database()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
