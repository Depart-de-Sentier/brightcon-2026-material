# Mapped BAFU:2026 database and EcoSpold 2 export

The database inputs and generated export are not included in the current repository
tree. Download **BAFU:2026 version 1 in EcoSpold 1 format** from
[openLCA Nexus](https://nexus.openlca.org/database/BAFU), read and accept the applicable
terms there, and put the original XML files directly in `data/raw/ecoSpold files/`.
See the [raw-data layout](../data/raw/README.md) and
[environment setup](../README.md#2-prepare-the-python-environment) for prerequisites.

Run from `hackathon/lca-lineage/` in the prepared `bw` environment, in this order:

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_all.py"
conda run --no-capture-output -n bw python "scripts/ecospold importer/import_export_ecospold2.py"
```

The repair runner creates and validates `data/processed/ecospold1-schema-fixed/`.
No separate baseline Brightway import is required before the export command.

The script uses project `bafu-2026-biosphere-310` under `artifacts/brightway/`, creates
**`BAFU:2026-mapped`**, and exports to **`data/processed/ecospold2-biosphere310/`**.
The original inputs and the notebook's preservation workflow remain available.
The existing biosphere is reused; creating a missing project downloads Brightway's
`ecoinvent-3.10-biosphere` archive.

It applies both approved technosphere mappings and all 24 biosphere migration
stages in the notebook's order. Candidate mappings are excluded. Every remaining
unlinked **biosphere** exchange is saved in an audit file and then excluded from
the mapped database and XML, as requested. An unlinked technosphere or production
exchange stops the script. The reduced inventory therefore omits impacts from
the excluded exchanges; these exclusions are not new flow correspondences.

The XML is validated and re-imported before writing the new database. Database
readback is compared with the retained records represented by the export. The
comparison accounts for Brightway's added `output` references and its normalization
of the node label `process` to `processwithreferenceproduct`.
The final output directory appears only after all checks pass. Progress bars cover
extraction, migrations, auditing, XML export/validation, re-import and comparison;
Brightway also displays its database-write progress.

## Output bundle

| File or folder | Contents |
| --- | --- |
| `datasets/*.spold` | One schema-valid EcoSpold 2 XML file per BAFU dataset |
| `audit/excluded-exchanges.jsonl` | Every excluded occurrence, full exchange dictionary, source dataset, zero-based source-row index, source XML exchange and file checksum |
| `audit/retained-inventory.jsonl` | Full retained Brightway records, including original labels, conversion assumptions, comments and uncertainty |
| `audit/source-metadata.jsonl` | Source XML metadata, including schema-repair comments, contacts and references |
| `audit/mapping-files/` | Exact migration JSON files used |
| `audit/migrations/` | Linking report after each biosphere stage |
| `manifest.json` | Counts, exclusions, file and mapping checksums, versions, label aliases, verification results and destination project/database |
| `ecospold2_reimport.py` | Portable Brightway re-import helper preserving the exported uncertainty |

JSONL has one JSON record per line. Duplicate exchanges remain separate occurrences.
The complete bundle, including the audit files and the mapping/repair documentation,
should accompany exports whenever sharing is permitted by the applicable BAFU terms.
Identify it as modified data and cite “Life Cycle Inventory database of the Swiss
Federal Administration, BAFU:2026”. The original downloads, repaired copies, and
entire generated export stay local and are ignored by Git. Do not force-add them.

## Local storage and optional compression

The export script produces uncompressed JSONL audits; no decompression step is
needed for a freshly generated export. If desired, compress the retained inventory
locally while preserving the original:

```bash
gzip -nk data/processed/ecospold2-biosphere310/audit/retained-inventory.jsonl
```

The manifest's checksum and XML audit references refer to the original uncompressed
file. Keep it alongside the export, or restore it from a local `.gz` copy using:

```bash
gzip -dk data/processed/ecospold2-biosphere310/audit/retained-inventory.jsonl.gz
```

Restoration refuses to overwrite an existing decompressed file. Compression does
not rerun repairs or change inventory values. Neither the archive nor the generated
database files belong in Git.

## EcoSpold 2 conventions

- Each elementary exchange uses its actual biosphere 3.10 flow UUID and target
  unit/compartment. The biosphere database itself and LCIA methods are not exported.
- Activity, product, exchange, unit, geography, person and compartment identifiers
  use deterministic UUIDs in the local BAFU export context, declared in the XML.
  These supporting identifiers are not claimed to be ecoinvent master-data IDs.
  Names and units are included inline; no ecoinvent technosphere database is needed.
- Supplier links use activity and product UUIDs. Amounts retain Python's full
  floating-point representation; signs, uncertainty distributions and parameters
  are retained. Standard deviations are represented as variances in EcoSpold 2.
- Names longer than EcoSpold 2's 120-character limit use a stable, hash-suffixed
  display alias. Complete names are retained in comments, audit records and the
  manifest; UUIDs determine linking. Overlong exchange comments remain complete in
  the audit, with a pointer in the XML.
- Source unit-process versus aggregated-inventory types and validity dates are
  retained. `specialActivityType=0` and an explicitly unspecified economic scenario
  are export conventions; no new system model, allocation or future scenario is
  inferred. Original documentation is retained in `audit/source-metadata.jsonl`.

The [EcoSpold 2 specification](https://support.ecoinvent.org/ecospold2) defines the
UUID-based format. XML validation uses the installed `pyecospold` 2.0.14 XSD set;
its file checksums are recorded in the manifest.

## Re-import the export

Use the bundled helper with the `bw` environment and an existing project containing
`ecoinvent-3.10-biosphere`. From `hackathon/lca-lineage/`:

```python
import os
import sys
from pathlib import Path

ROOT = Path.cwd()
EXPORT = ROOT / "data/processed/ecospold2-biosphere310"
os.environ["BRIGHTWAY2_DIR"] = str(ROOT / "artifacts/brightway")
sys.path.insert(0, str(EXPORT))

import bw2data as bd
from ecospold2_reimport import reimport_ecospold2

bd.projects.set_current("bafu-2026-biosphere-310")
importer = reimport_ecospold2(
    EXPORT / "datasets", "BAFU:2026-reimported", "ecoinvent-3.10-biosphere"
)
importer.statistics()
if any(True for _ in importer.unlinked):
    raise RuntimeError("Re-import contains unlinked exchanges")
if importer.db_name in bd.databases:
    raise RuntimeError("Target database already exists")
importer.write_database()
```

This uses `bw2io.SingleOutputEcospold2Importer` and its product/UUID-linking strategies.
It does not reapply BAFU migrations or ecoinvent-specific cleanup heuristics. The
standard full EcoSpold 2 strategy list can replace high lognormal uncertainties;
the extractor also omits the negative-lognormal flag, which the helper restores
from the signed amount. Use the helper when preserving those uncertainties matters.
Other software can read the standard `.spold` files, but has not been tested.
Arbitrary Brightway audit fields are retained in comments and sidecars, rather than
automatically reconstructed as structured fields during ordinary EcoSpold import.

## Reruns and verification

Existing output directories and databases are refused. To create a new version,
choose a new `--database` and `--output`. Alternatively, `--reuse-existing` checks
the existing target database against the freshly rebuilt inventory and fails if
they differ; it never overwrites the database. Use a fresh `--output` directory.
`--check-only` performs the export and
re-import checks without writing an inventory database. `--help` lists the source,
storage, project and biosphere options. A failed run keeps its `.ecospold2-building-*`
directory and failure manifest for diagnosis.

The checks require zero unlinked exchanges, identical activity and exchange counts,
exact amount equality, identical supplier/biosphere targets, and matching uncertainty
parameters within floating-point tolerance. Retained database records are checked
against database readback. Regression tests cover duplicate exclusions, refusal to
exclude technosphere exchanges, signed uncertainty, zero bounds, schema validation,
stable supplier IDs, name aliases and agreement with the notebook's migration order.

Verified on the current repaired release in `bw`: 11,947 datasets, 417,072 retained
exchanges (11,947 production, 114,369 technosphere, 290,756 biosphere), and 2,991
audited exclusions. All XML files validate and all retained exchanges re-import
with their original targets, amounts and uncertainty. Database readback also
matches. The six regression tests pass. The export retains 493 negative lognormal
exchanges and 324 lognormal scales that the default importer would otherwise cap;
255 activity names require display aliases.

These counts describe the documented BAFU:2026 v1 source and approved mappings.
The recorded verified export used `bw2data 4.7`, `bw2io 0.9.17`, `pyecospold 4.0.1`,
and `lxml 4.9.3`. Preserve your generated manifest and repair reports to record input
checksums, package versions, and checks for your run. Manifest timestamps and local
paths vary, so reproduction does not imply a byte-identical output directory.
