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

## 1. Download the BAFU source files and accept the terms

**The BAFU database, reports, and generated EcoSpold 2 files are not distributed in
the current repository tree. Each participant must obtain the source files from Nexus.**

1. Open the [BAFU database page on openLCA Nexus](https://nexus.openlca.org/database/BAFU).
2. Sign in or create a Nexus account if requested. Select **BAFU:2026 version 1**,
   the release used for this workflow, and its **EcoSpold 1** source download.
   The `.zolca` openLCA database and LCIA results spreadsheet are not inputs to these scripts.
3. Read and accept the applicable terms through the Nexus download process before
   downloading or using the data. The [BAFU terms of use](https://www.bafu.admin.ch/dam/fr/sd-web/-9ZObeMCZy8A/BAFU-20XY%20Terms%20of%20Use_EN%201.pdf)
   are also available for reference. Cloning this repository does not record acceptance.
4. Extract the download and copy the **11,947 original `process_*.xml` files directly
   into `data/raw/ecoSpold files/`**. Do not leave another archive directory between
   this folder and the XML files. Keep their names and contents unchanged.
5. Optionally download the corresponding documentation from Nexus and place its
   114 inventory reports in `data/raw/BAFU-2026 v1 LCI Reports/`. The repair and export
   commands use the XML files and do not require these PDFs.

See [the raw-data README](data/raw/README.md) for the expected layout. Downloads,
intermediate copies, exported datasets, and generated audits are ignored by Git;
do not force-add them. Use the same source release and repository revision when
comparing results; later BAFU releases can change the file count and mappings.

## 2. Prepare the Python environment

Use an existing `bw` conda environment with the packages below, or create one:

```bash
conda create -n bw python=3.11 pip -y
conda run -n bw python -m pip install "bw2data==4.7" "bw2io==0.9.17" "pyecospold==4.0.1" "lxml==4.9.3" numpy babel tqdm python-dateutil
```

These four package pins match the recorded verified export. Transitive dependencies
are not locked. The command-line repair/export workflow does not require Jupyter.
To use the notebooks, also run:

```bash
conda run -n bw python -m pip install jupyterlab ipykernel nbformat
conda run -n bw python -m ipykernel install --user --name bw --display-name "Python (bw)"
```

All following commands run from `hackathon/lca-lineage/`. First check the extraction:

```bash
conda run -n bw python -c 'from pathlib import Path; files = list(Path("data/raw/ecoSpold files").glob("process_*.xml")); print(f"{len(files):,} source files"); assert len(files) == 11947, "Check the BAFU release and extraction directory"'
```

## 3. Repair and validate the raw EcoSpold files

Run:

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_all.py"
```

The runner applies all eight repair steps to `data/raw/ecoSpold files/`, then validates the final XML against the EcoSpold 1 schema and checks inventory preservation. It uses the documented fallback values in [schema_overrides.json](scripts/ecospold%20importer/schema_overrides.json) and stops if any step fails.

Each step displays a file progress bar with counts, processing speed and estimated time remaining, including the final validation.

- **Repaired files:** `data/processed/ecospold1-schema-fixed/`
- **Intermediate copies:** separate directories under `data/processed/`
- **Repair and validation reports:** `reports/generated/`

Raw files remain unchanged. Reruns accept identical existing copies, refuse conflicting copies, and refresh the reports. This command repairs and validates XML; the Brightway import is a separate step described in the [script instructions](scripts/ecospold%20importer/README.md). See the [repair report](docs/bafu-2026-ecospold-repair-report.md) for each defect and its exact fix.

## Optional: import and review links in Brightway

Run [the import notebook](scripts/import_fixed_ecospold.ipynb) with the `bw` kernel. It imports the repaired files against biosphere 3.10 and applies the [documented technosphere and biosphere migrations](schemas/mappings/README.md). Rerun extraction and the migration cells after editing a mapping.

The latest full check links all technosphere exchanges and 290,756 of 293,747 biosphere exchanges. The remaining 2,991 biosphere occurrences are listed in `reports/generated/biosphere-unlinked.json`. Flows without a supported target remain unresolved. A notebook guard stops Run All before the existing drop/write/LCA cells while any exchange remains unlinked. See the [remaining review work](docs/bafu-2026-biosphere-unresolved-review.md).

## 4. Write the mapped database and reproduce the EcoSpold 2 files

After step 3 succeeds, run:

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/import_export_ecospold2.py"
```

This applies all approved mappings, saves every unlinked biosphere exchange in a separate audit file, and excludes those exchanges from the written database and XML export. It creates **`BAFU:2026-mapped`** in project **`bafu-2026-biosphere-310`** and writes **`data/processed/ecospold2-biosphere310/`**, including EcoSpold 2 files with biosphere 3.10 UUIDs, the exclusion audit, retained metadata, and a verification manifest.

The script checks the XML schema, re-imports every file, compares links/amounts/uncertainty, and verifies the written database. Existing databases and output directories are refused. See the [export instructions](docs/bafu-2026-ecospold2-export.md) for reruns and the bundled re-import helper that preserves uncertainty.

On first use, the script downloads Brightway's `ecoinvent-3.10-biosphere` project
archive, so internet access is required. It does not require an ecoinvent
technosphere database or a separate baseline import.

A successful run produces `datasets/*.spold`, `MasterData/`, the audit files,
`manifest.json`, and `ecospold2_reimport.py` under the output directory. For the
documented BAFU:2026 v1 release, expect **11,947 datasets, 417,072 retained exchanges,
and 2,991 audited biosphere exclusions**. The export is a modified BAFU dataset;
those exclusions mean it is not the complete original inventory. Keep the generated
audits and the [mapping documentation](schemas/mappings/README.md) with it.

For reruns, choose both a new database name and an unused output directory:

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/import_export_ecospold2.py" \
  --database "BAFU:2026-mapped-rebuilt" \
  --output data/processed/ecospold2-biosphere310-rebuilt
```

Older checkouts may still have a local export at the default path; it is not
overwritten. See the [export instructions](docs/bafu-2026-ecospold2-export.md) for
verification, `--reuse-existing`, and `--check-only`. This reproduces the transformation
and its checks; timestamps, local paths, and environment metadata can differ between runs.

## 5. Import the generated EcoSpold 2 files

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

This repository contains the project structure, repair/export code, mappings, and
assessment documentation. BAFU source files and generated database payloads stay
local; only the data-folder instructions are tracked. Cite the source as
“Life Cycle Inventory database of the Swiss Federal Administration, BAFU:2026”.
Any sharing of modified data must follow the applicable BAFU terms, including
attribution, clear modification labels, and accompanying change documentation.
