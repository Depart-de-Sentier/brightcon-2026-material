# Ecospold 2 with structured metadata

The ``ecospold2_export.py`` file uses regular expressions (regex) to extract source-related information about the processes and exchanges that do not have structured metadata (everything is in an unformatted comment).

The functions used to extract the structured metadata are in ``metadata_extractors.py`` and use the regular expressions that are detailed in ``regex.py``.


# EcoSpold 1 import attempt

For the complete mapped import and **EcoSpold 2 export**, run:

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/import_export_ecospold2.py"
```

This creates `BAFU:2026-mapped` in the existing biosphere 3.10 project. It applies all approved migrations, audits and excludes unresolved biosphere exchanges, validates the exported XML, verifies re-import, and checks database readback. Output: `data/processed/ecospold2-biosphere310/`. See [scope, audit files and re-import instructions](../../docs/bafu-2026-ecospold2-export.md). The short baseline import script described below does not apply these mappings.

For a consolidated explanation of each defect and its exact repair, see [BAFU:2026 EcoSpold 1 defects and repairs](../../docs/bafu-2026-ecospold-repair-report.md).

The latest cumulative files are in `data/processed/ecospold1-schema-fixed/`. All 11,947 files pass the installed EcoSpold 1 schema and the inventory-preservation audit. With the local timestamp/date adapters enabled, Brightway extracts all datasets and completes its nine default strategies without exceptions. Linking is still incomplete. See [Complete the schema repairs](#complete-the-schema-repairs) for the current commands, documented fallback values, and import status. Earlier sections record the sequence of failures and fixes.

## Run all repairs from raw files

From `hackathon/lca-lineage/`:

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_all.py"
```

This runs every repair step below in order, followed by `validate_collection.py`, stopping on the first failed step. It leaves raw files unchanged, uses the approved values in `schema_overrides.json`, and produces `data/processed/ecospold1-schema-fixed/` with reports under `reports/generated/`. Identical existing copies are accepted; conflicting copies are refused. It does not run the Brightway import.

Each step shows a `tqdm` progress bar with files processed, percentage, elapsed time, estimated time remaining and processing speed. The schema step has separate catalog-building and repair bars. These bars also appear when running a repair script individually. Keep `--no-capture-output` in the conda command to see updates live; `tqdm` is already included in the `bw` environment.

## Import repaired files with biosphere 3.10

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/import_with_biosphere310.py"
```

This short script downloads Brightway's `ecoinvent-3.10-biosphere` project archive on first use and creates project `bafu-2026-biosphere-310` under `artifacts/brightway/`. Subsequent runs reuse it. It reads `data/processed/ecospold1-schema-fixed/`, enables the local date/timestamp adapters, and runs the standard EcoSpold 1 importer strategies. It writes `BAFU:2026` only when all exchanges link, and refuses to overwrite an existing BAFU database. Exit code `2` means linking remains incomplete; `1` means an exception; `0` means the database was written. First use requires internet access.

Tested in `bw`: the project contains 4,362 biosphere flows, all 11,947 datasets extract, and all nine default strategies complete. Of 420,063 exchanges, 295,213 remain unlinked (293,747 biosphere and 1,466 technosphere), so the BAFU database is not written. A remaining mismatch is compartment vocabulary: for example, BAFU uses `emissions to air`, whereas biosphere 3.10 uses `air`. The installed importer's default strategies do not normalize these category names. The script currently reports this baseline without adding mappings. The run log is `reports/generated/ecospold1-biosphere310-import.log` (ignored by Git).

## Original import diagnostic

Run the standard [`bw2io.SingleOutputEcospold1Importer`](https://docs.brightway.dev/en/latest/content/api/bw2io/importers/ecospold1/index.html) against the original BAFU XML files, followed by its default strategies and import statistics. Brightway's EcoSpold importers are in `bw2io`; `bw2data` manages the project and databases.

From `hackathon/lca-lineage/`, using the existing `bw` conda environment:

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/try_import.py"
```

Defaults resolve relative to the script's repository, so it also works when launched from another working directory. The importer uses a single process to retain a useful traceback when extraction fails.

The attempt records package versions, input file count, project, failure stage, exception traceback, and the offending file when available. It stops at the first exception. A failure does not establish that every file has the same problem.

Outputs:

- `reports/generated/ecospold1-import.json`: diagnostic report, replaced on each run.
- `artifacts/brightway/`: local Brightway project storage.

Both output locations are ignored by Git. The script sets `BRIGHTWAY2_DIR` before importing Brightway. It reads source XML unchanged and applies any standard importer strategies in memory. Schema validation is performed by the installed importer's `pyecospold` parser. The script does not write the resulting inventory database. No biosphere database is downloaded; its availability is recorded because missing background data can affect linking after extraction succeeds.

Exit codes are `0` for successful extraction and strategies with no unlinked exchanges, `1` for an exception, and `2` for a completed attempt with unlinked exchanges.

To reproduce a failure on one file:

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/try_import.py" \
  --input "data/raw/ecoSpold files/process_EXAMPLE.xml" \
  --report "reports/generated/ecospold1-single-file.json"
```

Replace `process_EXAMPLE.xml` with a real filename. Use `--help` to see project, database, and storage options.

## Initial result

The first run used `bw2data 4.7`, `bw2io 0.9.17`, `pyecospold 4.0.0`, and `lxml 6.1.1`. Extraction stopped at `process_a76fddbc-05c5-386e-84f3-d4f1ecad697c.xml` with:

```text
XMLSyntaxError: Element 'ecoSpold': No matching global declaration available for the validation root.
```

This file has an unqualified `ecoSpold` root and no namespace declarations. The installed EcoSpold 1 schema uses the namespace `http://www.EcoInvent.org/EcoSpold01`. This identifies the first blocker; later schema or import errors remain untested. The stock importer uses filesystem order, so another machine may encounter a different file first.

## Repair the namespace in copies

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_namespace.py"
conda run --no-capture-output -n bw python "scripts/ecospold importer/try_import.py" \
  --input "data/processed/ecospold1-namespace-fixed" \
  --report "reports/generated/ecospold1-namespace-fixed-import.json"
```

The repair adds `xmlns="http://www.EcoInvent.org/EcoSpold01"` to the actual root start tag of each unqualified file and writes a copy to `data/processed/ecospold1-namespace-fixed/`. All other bytes are preserved. Files already using the expected namespace are copied unchanged; unexpected root elements or namespaces produce errors. Source files are read only.

The repair report, `reports/generated/ecospold1-namespace-repair.json`, records the input and output SHA-256 checksums for each file. The output folder and report are ignored by Git. Repeating the command accepts identical outputs; differing existing files require a new output directory.

All 11,947 source XML files required the namespace declaration, and all 11,947 copies were generated successfully. The next import attempt passed the root-namespace check but stopped on `startDate` value `2000-01`, which is not a complete `xs:date`. Validation of that first file also reports:

- `endDate` value `2000-12` is not a complete date.
- A `source` publisher exceeds the 40-character limit.
- `sourceNumber` is not an allowed `source` attribute.
- A `person` company code exceeds the 7-character limit.

The import report includes the complete XML error log for the failing file. The namespace repair leaves these further issues intact; dates and metadata have not been guessed, truncated, or removed. Successful extraction and database import have not yet been reached.

## Correct partial-date element types

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_dates.py"
conda run --no-capture-output -n bw python "scripts/ecospold importer/try_import.py" \
  --input "data/processed/ecospold1-dates-fixed" \
  --report "reports/generated/ecospold1-dates-fixed-import.json"
```

The EcoSpold 1 schema provides distinct elements for year, year-month, and full-date precision. The repair renames `startDate`/`endDate` containing `YYYY` to `startYear`/`endYear`, and those containing `YYYY-MM` to `startYearMonth`/`endYearMonth`. Date text is unchanged. Existing full dates, time zones, and correctly typed year elements remain unchanged.

The installed `pyecospold` parser interprets these standard elements as the beginning of the stated start period and the end of the stated end period. This includes leap years. The repair itself adds no date precision to the XML.

This step corrected 19,762 date elements in 9,881 files and copied all 11,947 files. All 23,888 existing date elements were checked against their declared schema types. The report is `reports/generated/ecospold1-date-repair.json`, with per-file changes and checksums. After this step, the first import failure moved to the publisher-length constraint.

## Preserve incompatible metadata, one field at a time

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_metadata.py" publisher
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_metadata.py" company-code
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_metadata.py" source-number
```

Each command reads the preceding step's copies and creates a new directory containing all 11,947 files:

| Rule | Input directory under `data/processed/` | Output directory | Changes |
| --- | --- | --- | --- |
| `publisher` | `ecospold1-dates-fixed` | `ecospold1-publisher-fixed` | Remove 1,124 `source.publisher` attributes longer than 40 characters |
| `company-code` | `ecospold1-publisher-fixed` | `ecospold1-company-code-fixed` | Replace 2,165 overlong `person.companyCode` values with an empty string |
| `source-number` | `ecospold1-company-code-fixed` | `ecospold1-source-number-fixed` | Remove 6,909 unsupported `source.sourceNumber` attributes |

Every affected attribute's complete original value is preserved in an adjacent XML comment and the corresponding JSON repair report. Comments contain JSON records prefixed with `BAFU schema repair:`. The record identifies the element, its `number`, the attribute, the original value, and the action. Short valid values and all other attributes are preserved.

`person.companyCode` is required by the schema, so it cannot simply be removed. Its type permits an empty string; the full code remains in the comment and report. No substitute organization code is invented. The standard importer does not carry these comments into its structured metadata fields; the original metadata remains available in the repaired XML and repair reports.

Reports are `reports/generated/ecospold1-publisher-repair.json`, `ecospold1-company-code-repair.json`, and `ecospold1-source-number-repair.json`. They include per-file changes and input/output checksums. Repeated runs accept identical outputs. Use a new output directory, or explicitly pass `--overwrite`, to regenerate differing metadata-repair outputs. Raw files are protected from output writes.

Round-trip verification restored all 10,198 affected attributes from the XML comments and recovered the complete pre-metadata-repair XML content for every file. Inventory values, exchange links, and unaffected metadata are unchanged.

## Import with the installed timestamp parser

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/try_import.py" \
  --input "data/processed/ecospold1-source-number-fixed" \
  --report "reports/generated/ecospold1-source-number-fixed-import.json"
```

Import checks were run after each step. The first file, `process_a76fddbc-05c5-386e-84f3-d4f1ecad697c.xml`, now passes the full installed EcoSpold 1 schema. Extraction proceeds to reading its timestamp, where `pyecospold 4.0.0` fails with `ValueError: unconverted data remains: .534+02:00` for `2023-03-29T18:04:18.534+02:00`.

This timestamp is accepted by the schema; the next blocker is the parser's handling of fractional seconds and time zones. Timestamp values have not been changed. Full-release schema validation and successful extraction/import have not yet been achieved.

## Timestamp parser compatibility

The optional `--iso-timestamps` flag enables the repository's [timestamp adapter](timestamp_compat.py) during extraction:

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/try_import.py" \
  --input "data/processed/ecospold1-source-number-fixed" \
  --iso-timestamps \
  --report "reports/generated/ecospold1-iso-timestamps-import.json"
```

The installed `pyecospold 4.0.0` datetime converter expects `%Y-%m-%dT%H:%M:%S`. The adapter uses Python's ISO parser for the observed BAFU forms, including fractional seconds, UTC offsets, and the space separator found in some dataset-level timestamps. It preserves offsets, supports up to six fractional digits, and rejects finer precision explicitly to avoid silently truncating it. Schema validation remains enabled.

The converter is replaced only in the running process, during the single-process extraction step, and restored even if extraction raises an exception. Installed package files and XML data are unchanged. Runs without the flag retain the installed parser for reproducing the baseline failure. The JSON report records which parser was used.

Validation covered all 23,894 timestamp values in the repaired collection and confirmed that the 11,947 file checksums remained unchanged. The first file extracts with timestamp `2023-03-29T18:04:18.534000+02:00`, preserving the original milliseconds and offset. Regression tests cover offsets, microseconds, naive timestamps, UTC `Z`, the space separator, invalid dates, excessive precision, and converter restoration:

```bash
conda run --no-capture-output -n bw python -m unittest discover \
  -s "scripts/ecospold importer" -p "test_timestamp_compat.py" -v
```

The import now completes extraction of three files before stopping at `process_da132188-4772-389f-b13f-79ccb0f6451c.xml`. Its `administrativeInformation` contains `dataGeneratorAndPublication`, two `person` elements, `dataEntryBy`, and another `person`; the schema requires `dataEntryBy` first. The same validation log reports an unresolved `proofReadingValidator` reference to person `137485`. These are the next issues to investigate. Full-release import has not yet succeeded.

## Correct administrative-element order

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_administrative_order.py"
conda run --no-capture-output -n bw python "scripts/ecospold importer/try_import.py" \
  --input "data/processed/ecospold1-administrative-order-fixed" \
  --iso-timestamps \
  --report "reports/generated/ecospold1-administrative-order-fixed-import.json"
```

This step reads `ecospold1-source-number-fixed/` and copies all 11,947 files into `ecospold1-administrative-order-fixed/`. It corrects 521 administrative sections in 521 files to match the installed schema's sequence: `dataEntryBy`, `dataGeneratorAndPublication`, `person` records, then any foreign-namespace extensions.

The script moves complete byte blocks, including each element's preceding comments, and keeps the relative order of person records. Values, references, and preserved metadata comments are unchanged. The repair report, `reports/generated/ecospold1-administrative-order-repair.json`, records file checksums, the original and resulting orders, and hashes of the moved blocks.

Verification checked all 11,947 copies for unchanged content outside these sections, unchanged child records and comment associations, and the resulting order. All 11,947 reviewer references point to an existing person in the same dataset. Person `137485` was already present in the previously failing file; correcting the sequence resolves its reported key-reference error without modifying the reference or adding a person. That file now passes full EcoSpold 1 schema validation.

Regression checks cover comment associations, stable person order, explicit end tags, foreign extensions, multiple datasets, and idempotence. Run all current checks with:

```bash
conda run --no-capture-output -n bw python -m unittest discover \
  -s "scripts/ecospold importer" -p "test_*.py" -v
```

At this stage, extraction reached a further parser limitation in that same fourth file: `ParserError: Unknown string format: 2023-12-31+01:00`. This is a schema-valid calendar date carrying a time-zone offset. The timestamp adapter addresses datetime attributes; it does not change `pyecospold`'s separate time-period date parser.

## Calendar-date parser compatibility

Use both parser options with the latest repaired copies:

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/try_import.py" \
  --input "data/processed/ecospold1-administrative-order-fixed" \
  --iso-timestamps --iso-dates \
  --report "reports/generated/ecospold1-iso-dates-import.json"
```

The optional `--iso-dates` flag enables [date_compat.py](date_compat.py). XML Schema [permits timezone offsets on calendar dates](https://www.w3.org/TR/xmlschema-2/#date), but the installed EcoSpold 1 model's date parser rejects them. The adapter reads complete dates at local midnight with their original offset, then lets the model's existing `.date()` conversion keep the stated calendar day. It does not convert dates to UTC or add time-of-day precision to XML. Year-only and year-month inputs still use the installed parser and its start/end boundary rules.

The standard Brightway extractor stores these values as `YYYY-MM-DD` tags, so offsets remain available in the source XML rather than in those imported date tags. The adapter supports BAFU's four-digit AD years, validates calendar dates and offset bounds, and retains schema validation. It temporarily replaces only the EcoSpold 1 model's parser reference during extraction, restores it on success or failure, and leaves the `dateutil` package and installed files unchanged. Without `--iso-dates`, the original date failure remains reproducible. The JSON report records the selected date parser separately from the timestamp parser.

Verification checked all 23,888 existing date elements across 11,944 time periods, including 460 complete dates with timezone offsets. All retained their expected calendar days and period boundaries. Three other files contain time periods with no start/end dates; these remain unresolved and are listed in `reports/generated/ecospold1-date-parser-audit.json`. All 11,947 XML checksums still match the preceding repair manifest. No further XML copies are needed for this parser-only change.

The previously failing file now extracts successfully, with start date `2021-01-01` and end date `2023-12-31`. All 22 regression tests pass, including actual `pyecospold.TimePeriod` access, leap-year boundaries, offsets, and restoration of both adapters after an exception.

At this stage, the full import attempt completed five files before stopping at `process_78f8fd8d-3b59-4189-bd30-430525726fb8.xml`. Schema validation reported duplicate exchange numbers `563077` and `185969` (`pkExchangeNumber`).

## Make exchange numbers unique within each dataset

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_exchange_numbers.py"
conda run --no-capture-output -n bw python "scripts/ecospold importer/try_import.py" \
  --input "data/processed/ecospold1-exchange-numbers-fixed" \
  --iso-timestamps --iso-dates \
  --report "reports/generated/ecospold1-exchange-numbers-fixed-import.json"
```

The installed EcoSpold 1 schema defines `exchange.number` as a dataset-local identifier and requires it to be unique within that dataset. The duplicates include distinct inventory rows, such as different pieces of equipment with different amounts and comments. Merging or deleting these rows would change the inventory or lose its detail.

[repair_exchange_numbers.py](repair_exchange_numbers.py) retains the first occurrence of each number and assigns subsequent occurrences the lowest unused positive integer in that dataset. It reserves all existing numbers before assigning replacements and compares integer values, so `7` and `007` count as duplicates. Every changed number is preserved in an adjacent XML comment, including its exact original XML attribute text, dataset and exchange positions, and replacement number. Only the number attribute and the new comment are changed. Exchange order, amounts, uncertainty fields, names, categories, units, groups, and existing comments are unchanged.

The collection contains no allocation records or foreign extensions. The script nevertheless checks allocation references and refuses to renumber an ID referenced ambiguously; it also rejects foreign extensions in affected datasets because their reference semantics are unknown. Unambiguous references remain untouched. The installed single-output importer's linking strategies match flow/activity fields rather than these local integer IDs. Original IDs remain available in comments and the log for other consumers. Unique out-of-range IDs are left for a separate repair; this includes one existing `number="0"` in `process_05a10e4b-a919-33b6-b017-7c0bf7f7a7f9.xml`.

This step copied all 11,947 files from `ecospold1-administrative-order-fixed/` to `ecospold1-exchange-numbers-fixed/` and reassigned 111,512 repeated IDs in 2,134 files. The report is `reports/generated/ecospold1-exchange-number-repair.json`, with per-exchange changes and input/output SHA-256 hashes. Repeated runs accept identical copies; differing outputs require a new directory.

Verification covered every file and confirmed unique exchange numbers within all datasets, preservation of all 420,063 exchange rows, and exact byte recovery of every input by reversing the changes from the comments. Input hashes still match the preceding repair manifest. All 33 regression tests pass, including ambiguity rejection, numeric identity, dataset-local scope, idempotence, and exact recovery. Raw files are unchanged.

The audit report, `reports/generated/ecospold1-exchange-number-audit.json`, also records full schema validation: 4,981 files pass, while 6,966 retain other schema defects. No duplicate-exchange identity errors remain. The previously failing file now passes full schema validation.

At this stage, the import attempt completed eight files before stopping at `process_85a14157-f786-30dc-9dc1-ac4f0c233fc3.xml`. Its `processInformation` began with `timePeriod` before the required `referenceFunction`; the same file had uppercase `True`/`False` boolean values. These defects and the missing date periods are addressed by the final stage below.

## Complete the schema repairs

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_schema.py"
conda run --no-capture-output -n bw python "scripts/ecospold importer/validate_collection.py"
conda run --no-capture-output -n bw python "scripts/ecospold importer/try_import.py" \
  --input "data/processed/ecospold1-schema-fixed" \
  --iso-timestamps --iso-dates \
  --report "reports/generated/ecospold1-schema-fixed-import.json"
```

These commands use the preceding `ecospold1-exchange-numbers-fixed/` copies. To regenerate from the raw release, first run the namespace, date, three metadata, administrative-order, and exchange-number repair commands above, in that order. All repair scripts leave raw data unchanged. The final repair accepts identical existing outputs; `--overwrite` explicitly regenerates differing copies from its input when documented overrides change.

[repair_schema.py](repair_schema.py) applies the remaining rules to all files and records each edit in XML comments and `reports/generated/ecospold1-schema-repair.json`. Before accepting each output, it reverses every change using that log and checks that the complete canonical XML, including pre-existing comments, matches the input. This final stage serializes changed XML with `lxml`, so formatting and XML declaration spelling can change. Inventory values remain intact.

The final stage corrected 6,966 files:

| Repair | Changes |
| --- | ---: |
| Correct process-information and modelling/validation element order | 1,754 and 290 sections |
| Normalize `True`/`False` to `true`/`false` | 33,136 attributes |
| Normalize timestamp space separators to `T`, preserving fractions and offsets | 1,452 attributes |
| Format numeric percentages to one decimal without rounding their values | 1,967 attributes |
| Preserve invalid optional CAS numbers in comments and remove those attributes | 15,019 attributes |
| Preserve overlong required person names in comments and use an empty field | 235 attributes |
| Supply empty required addresses without inventing an address | 98 attributes |
| Recover years explicitly stated in citation text | 127 source records |
| Remove empty duplicate validation elements, preserving their XML in comments | 197 elements |
| Preserve unsupported `referenceFunction.text` in comments | 33 attributes |
| Recover a referenced source from matching source identities elsewhere in the collection | 2 source records |
| Give the single exchange numbered `0` an unused positive local ID | 1 exchange |
| Remove an invalid optional percentage and volume number, preserving originals | 1 attribute each |

`Europe without Switzerland` exceeds the schema's seven-character location limit. It is represented by the local alias `LBFAC32` in 57 geography/exchange attributes. This is an opaque repository-defined code, not a newly inferred region or an official geographic code. Every affected XML comment and the report map it back to the full original label; both activities and exchanges use the same alias. The inventory audit resolves that alias when comparing against the raw data.

The explicit user decisions are stored in [schema_overrides.json](schema_overrides.json), with reasons and their original unknown status:

- `CH` for 351 empty country fields belonging to anonymized contacts `137242` and `165052`.
- Year `2024` for the ENTSO-E natural-gas electricity dataset, derived from its stated statistics source.
- Year `2025` for the GB and ES natural-gas heat/power datasets, using the cited publication year as requested. These are publication-year fallbacks, not claims that all underlying inventory data are from 2025.
- `false` for 197 unknown whole-period validity flags and `true` for 5 unknown copyright flags. The latter is a conservative schema fallback, not verified licensing information.
- Year `2026` for the otherwise empty compatibility citation in `process_09984ab6-a49a-46a6-801a-ddcbc3b881bc.xml`. Its publication year remains unknown; the value records the BAFU release-year fallback.

The original missing values and all substituted metadata remain in comments and the JSON log. As with earlier repairs, the standard importer does not automatically carry these comments into its structured metadata fields; retain the XML, overrides, and reports alongside any imported database.

[validate_collection.py](validate_collection.py) independently checks the complete file set, output hashes, schema validity, unique exchange IDs, and all ordered exchange attributes and group elements against the raw release. It also compares reference-function and geography metadata. Only the recorded ID changes, boolean spelling, invalid CAS attributes, unsupported reference-function text, and reversible region aliases are allowed to differ. Numeric inventory fields, units, uncertainty fields, names, categories, flow directions, and row counts must match.

The resulting `reports/generated/ecospold1-final-validation.json` confirms **11,947 schema-valid files, 11,947 datasets, and all 420,063 inventory exchanges preserved**. There are no unresolved schema defects. Regression tests include intentionally corrupted amounts, uncertainty fields, and flow directions to verify that the integrity check detects them.

The final import run in `bw` used `bw2data 4.7`, `bw2io 0.9.17`, `pyecospold 4.0.0`, and `lxml 6.1.1`. It extracted **all 11,947 datasets and 420,063 exchanges**, completed all nine default strategies, and reached statistics without an exception. The full report is `reports/generated/ecospold1-schema-fixed-import.json`; its console output is recorded in the adjacent `.log` file. All **48 regression tests pass**.

The report has `stage: complete` and `status: unlinked`, with **295,213 unlinked exchanges**. The isolated test project has no `biosphere3` database. This is an error-free parsing/strategy run, not a fully linked LCA-ready database; the check intentionally retains exit code `2` for that distinction. Conda may print a nonzero-exit message for this status even though the importer raised no exception. No database was written and no background database was downloaded. The stock extractor also emits a divide-by-zero warning for zero-valued lognormal exchanges; their inventory amounts and uncertainty fields were preserved rather than altered to suppress the warning.
