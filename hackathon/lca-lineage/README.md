# LCA data lineage hackathon

Workspace for the Brightcon 2026 hackathon on traceable datapoints and lineage in life cycle assessment (LCA) databases.

The hackathon will explore a proposed traceability standard, establish data lineage, and assess the BAFU LCA database against the requirements developed by participants.

Project context: [Brightcon 2026 hackathon issue #42](https://github.com/Depart-de-Sentier/brightcon-2026-material/issues/42).

## Working directory

These materials now live in `hackathon/lca-lineage/` in the Brightcon 2026 material repository.
From the repository root, enter this directory before running the commands below:

```bash
cd hackathon/lca-lineage
```

Paths in the lineage documentation are relative to `hackathon/lca-lineage/`. Start Jupyter
from this directory or `hackathon/lca-lineage/scripts/` so the import notebooks can find the data.

## lineage of lineage projects
- 2024: https://github.com/Depart-de-Sentier/brightcon-2024-material/tree/main/hackathon/data-lineage
- 2025: 
    - https://github.com/Depart-de-Sentier/brightcon-2025-material/issues/2
    - https://github.com/Depart-de-Sentier/brightcon-2025-material/issues/1
        - https://github.com/TimoDiepers/trailpack

## Repair the raw EcoSpold files

From `hackathon/lca-lineage/`, run this single command using the existing `bw` conda environment (with `lxml`, `pyecospold` and `tqdm` installed):

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_all.py"
```

The runner applies all eight repair steps to `data/raw/ecoSpold files/`, then validates the final XML against the EcoSpold 1 schema and checks inventory preservation. It uses the documented fallback values in [schema_overrides.json](scripts/ecospold%20importer/schema_overrides.json) and stops if any step fails.

Each step displays a file progress bar with counts, processing speed and estimated time remaining, including the final validation.

- **Repaired files:** `data/processed/ecospold1-schema-fixed/`
- **Intermediate copies:** separate directories under `data/processed/`
- **Repair and validation reports:** `reports/generated/`

Raw files remain unchanged. Reruns accept identical existing copies, refuse conflicting copies, and refresh the reports. This command repairs and validates XML; the Brightway import is a separate step described in the [script instructions](scripts/ecospold%20importer/README.md). See the [repair report](docs/bafu-2026-ecospold-repair-report.md) for each defect and its exact fix.

## Import and review links in Brightway

Run [the import notebook](scripts/import_fixed_ecospold.ipynb) with the `bw` kernel. It imports the repaired files against biosphere 3.10 and applies the [documented technosphere and biosphere migrations](schemas/mappings/README.md). Rerun extraction and the migration cells after editing a mapping.

The latest full check links all technosphere exchanges and 290,756 of 293,747 biosphere exchanges. The remaining 2,991 biosphere occurrences are listed in `reports/generated/biosphere-unlinked.json`. Flows without a supported target remain unresolved. A notebook guard stops Run All before the existing drop/write/LCA cells while any exchange remains unlinked. See the [remaining review work](docs/bafu-2026-biosphere-unresolved-review.md).

## Write the mapped database and export EcoSpold 2

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/import_export_ecospold2.py"
```

This applies all approved mappings, saves every unlinked biosphere exchange in a separate audit file, and excludes those exchanges from the written database and XML export. It creates **`BAFU:2026-mapped`** in project **`bafu-2026-biosphere-310`** and writes **`data/processed/ecospold2-biosphere310/`**, including EcoSpold 2 files with biosphere 3.10 UUIDs, the exclusion audit, retained metadata, and a verification manifest.

The script checks the XML schema, re-imports every file, compares links/amounts/uncertainty, and verifies the written database. Existing databases and output directories are refused. See the [export instructions](docs/bafu-2026-ecospold2-export.md) for reruns and the bundled re-import helper that preserves uncertainty.

The verified export is committed in this repository. To rebuild it, add `--output data/processed/ecospold2-biosphere310-rebuilt` (or another unused directory) to the command above. Its retained-inventory audit is stored losslessly as `audit/retained-inventory.jsonl.gz` to fit GitHub's file-size limit; the [export instructions](docs/bafu-2026-ecospold2-export.md#git-storage) explain how to restore and verify it. No decompression is needed to import the `.spold` files.

To import the exported files into a separate project, run [the EcoSpold 2 import notebook](scripts/import_ecospold2.ipynb) with the `bw` kernel. It creates a project with biosphere 3.10 and writes the imported database once all exchanges link.

## Data lineage tracking

One idea to integrate better lineage documentation was this: Any job runs (data transformations like parsing, repair, mapping, export) can be logged and streamed to a running [OpenLineage](https://openlineage.io/) instance specific to sentier.dev, so every transformation is visible as a dataset/job graph as it happens.

See [How to set up OpenLineage](docs/how_to_openlineage.md) for local setup (including Codespaces-specific fixes) and example `START`/`COMPLETE` events.

## Repository structure

| Folder | Purpose |
| --- | --- |
| [schemas/candidates/](schemas/candidates/) | Candidate schemas |
| [schemas/mappings/](schemas/mappings/) | Mappings between schemas and data formats |
| [scripts/](scripts/) | Extraction, transformation, validation, and analysis scripts |
| [prototypes/](prototypes/) | Experiments and proof-of-concept implementations |
| [examples/](examples/) | Example datapoints and lineage records |
| [assessment/bafu/](assessment/bafu/) | BAFU assessment materials and findings |
| [data/raw/](data/raw/) | Original database files and source documents |
| [data/processed/](data/processed/) | Derived data and metadata extracts |
| [docs/](docs/) | Project documentation and notes |
| [docs/decisions/](docs/decisions/) | Agreed scope and design decisions |
| [reports/](reports/) | Hackathon reports and presentations |

This repository contains the initial project structure and the BAFU 2026 raw dataset: 11,947 EcoSpold XML files and 114 PDF inventory reports. Participants will add the schemas, code, and assessment criteria.

Raw files under `data/raw/` and the verified export under `data/processed/ecospold2-biosphere310/` are tracked in Git. Other derived data payloads are ignored by default; folder READMEs are tracked.
