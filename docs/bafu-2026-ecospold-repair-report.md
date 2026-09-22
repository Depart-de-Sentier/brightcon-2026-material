# BAFU:2026 EcoSpold 1 defects and repairs

This report describes the defects found in the BAFU:2026 XML export, the exact transformations applied, and the assumptions needed where required metadata was missing. Results refer to the local run on **21 September 2026**.

The collection contains **11,947 XML files and 420,063 inventory exchanges**. Validation uses `EcoSpold01Dataset.xsd` and its included files from **pyecospold 4.0.0**. The XSD is unchanged. Repairs are applied to copies; the original files in [`data/raw/ecoSpold files/`](../data/raw/ecoSpold%20files/) remain unchanged.

Final copies: [`data/processed/ecospold1-schema-fixed/`](../data/processed/ecospold1-schema-fixed/). The [script README](../scripts/ecospold%20importer/README.md) contains execution commands and the detailed debugging history.

## 1. Which scripts run, and in what order?

Each stage reads the preceding stage's output. The final script completes the earlier repairs; running it alone on raw files is insufficient.

| Stage | Implementation | Purpose |
| --- | --- | --- |
| 1 | [repair_namespace.py](../scripts/ecospold%20importer/repair_namespace.py) | Add the missing EcoSpold 1 namespace. |
| 2 | [repair_dates.py](../scripts/ecospold%20importer/repair_dates.py) | Use the correct element types for partial dates. |
| 3–5 | [repair_metadata.py](../scripts/ecospold%20importer/repair_metadata.py), with `publisher`, `company-code`, then `source-number` | Preserve incompatible attributes and satisfy their schema constraints. |
| 6 | [repair_administrative_order.py](../scripts/ecospold%20importer/repair_administrative_order.py) | Correct administrative element order. |
| 7 | [repair_exchange_numbers.py](../scripts/ecospold%20importer/repair_exchange_numbers.py) | Give repeated exchange numbers unique dataset-local IDs. |
| 8 | [repair_schema.py](../scripts/ecospold%20importer/repair_schema.py) | Apply the remaining rules below and validate every output. |

Counts below are occurrences of the stated attribute, element, or file. Several defects can occur in one file, so the counts should not be added to estimate affected files.

## 2. Structural and value-format defects

| Original defect / schema requirement | Exact repair | Observed scope |
| --- | --- | ---: |
| The root and descendants had no EcoSpold namespace, producing “No matching global declaration available for the validation root.” | Insert `xmlns="http://www.EcoInvent.org/EcoSpold01"` on the root. Preserve the other bytes at this stage. | 11,947 files |
| `startDate` / `endDate` contained years or year-months, although their `xs:date` type requires a complete date. | Rename `startDate` / `endDate` to `startYear` / `endYear` for `YYYY`, or `startYearMonth` / `endYearMonth` for `YYYY-MM`. Date text and precision are unchanged: `<startDate>2000-01</startDate>` becomes `<startYearMonth>2000-01</startYearMonth>`. | 19,762 elements in 9,881 files |
| Administrative children violated the XSD sequence. | Reorder to `dataEntryBy`, `dataGeneratorAndPublication`, then `person` records. Keep person order, values, and attached comments. Foreign-namespace extensions, if present, follow these elements. | 521 sections/files |
| Process-information children violated the XSD sequence; for example, `timePeriod` appeared first. | Reorder to `referenceFunction`, `geography`, `technology`, `timePeriod`, `dataSetInformation`, then any foreign extensions. | 1,754 sections |
| Modelling/validation children violated the XSD sequence. | Reorder to optional `representativeness`, `source` records, optional `validation`, then any foreign extensions. | 290 sections |
| A second empty `validation` element exceeded the permitted cardinality. | Remove only the extra empty element and preserve its original XML in a comment/log entry. A second nonempty validation raises an error for explicit reconciliation. | 197 elements |
| Repeated `exchange.number` values violated the dataset-local `pkExchangeNumber` uniqueness constraint. Distinct rows sometimes shared a number. | Keep the first occurrence and assign each subsequent occurrence the lowest unused positive integer in that dataset. Reserve all existing IDs before assigning replacements. Preserve every row, its order, and its inventory payload. Original IDs, lexical forms, and row positions remain in comments/logs. | 111,512 ID replacements in 2,134 files |
| One exchange had `number="0"`; `TIndexNumber` requires a positive integer. | Assign an unused positive local ID and record `0` as the original value. | 1 exchange |
| Boolean attributes contained `True` or `False`, which are invalid XML Schema boolean spellings. | Replace with `true` or `false`, preserving the truth value. This rule applies to the known boolean attributes, not arbitrary text. | 33,136 attributes |
| `dataset.timestamp` and `dataSetInformation.timestamp` used a space between date and time. | Replace the separator at position 11 with `T`. For example, `2025-09-04 18:38:44.741718` becomes `2025-09-04T18:38:44.741718`; fractions and offsets are retained. | 1,452 attributes |
| Numeric `representativeness.percent` values did not match the schema's decimal spelling. | Use one decimal place without rounding the numeric value: `100` becomes `100.0`. The rule accepts finite values from 0 to 100 that are exactly representable at this precision. | 1,967 attributes |
| `Europe without Switzerland` exceeded the seven-character location-code limit. | Use the reversible local alias `LBFAC32` consistently for activities and exchanges. Comments and the repair report define it as the complete original label. The alias is `L` plus six uppercase SHA-256 hexadecimal characters, with collision checking against existing codes. | 57 attributes: 26 geography and 31 exchange locations |

`LBFAC32` is a repository-defined code for the original region. It is not an official geographic identifier or a change to the region's definition. Downstream applications need the alias mapping if they interpret geographic codes.

No allocation records were present in this collection. The duplicate-ID script nevertheless checks allocation references and refuses to guess when they point ambiguously to a duplicated ID; it also rejects foreign extensions in affected datasets whose reference semantics it cannot establish.

## 3. Metadata that did not fit the schema

For removed or replaced attribute values, the complete original is preserved in an adjacent `BAFU schema repair:` XML comment and the JSON repair log. Required string attributes are kept with an empty value where their type allows this.

| Original defect / constraint | Exact repair | Occurrences |
| --- | --- | ---: |
| `source.publisher` exceeded 40 characters. | Preserve its full value and remove the optional attribute. | 1,124 |
| `person.companyCode` exceeded 7 characters. | Preserve its full value and set the required attribute to `""`. | 2,165 |
| `source.sourceNumber` is not an allowed attribute. | Preserve the full value and remove that attribute; retain the valid `source.number`. | 6,909 |
| `person.name` exceeded 40 characters. | Preserve the full name and set the required attribute to `""`; do not truncate it or invent an abbreviated identity. | 235 |
| Required `person.address` was absent. | Add `address=""`, recording that no address was supplied. | 98 |
| `exchange.CASNumber` was empty or failed the required hyphenated pattern. | Preserve the original value and remove the optional attribute. Do not infer a chemical identity or invent a CAS number. | 15,019 |
| `referenceFunction.text` is not an allowed attribute. | Preserve its complete value and remove it. Keep any existing `generalComment` unchanged. | 33 |
| A percentage contained `unknown.0`. | Preserve the text and remove the optional `percent` attribute. | 1 |
| `source.volumeNo` contained `nan`. | Preserve the text and remove the optional attribute. | 1 |
| Required `source.year` was empty but a `Year: YYYY` field existed in the citation text. | Recover the year only when the text supplies one distinct explicit year. Escaped newline markers are interpreted for this lookup. | 127 |
| `referenceToPublishedSource="141100"` had no corresponding source in the same dataset. | Copy the matching source record from elsewhere in the collection, requiring agreement on first author, additional authors, title, and year. Choose the richest compatible record and log the source filename. Preserve the reference itself. | 2 source records added |

The initially reported missing reviewer reference to person `137485` required no identity change: that person already existed in the dataset. Correcting administrative element order resolved the validation error. All reviewer references were checked against their dataset-local person records.

## 4. Missing facts requiring approved fallbacks

These choices are distinct from formatting corrections. They are stored, with evidence and the original unknown status, in [schema_overrides.json](../scripts/ecospold%20importer/schema_overrides.json). The user approved each fallback on 21 September 2026.

| Missing required metadata | Approved replacement and meaning | Scope |
| --- | --- | ---: |
| Country for anonymized contacts `137242` (`default`) and `165052` (`Not reviewed`). | `CH`, explicitly recorded as a selected fallback rather than recovered country information. | 351 fields |
| Validity dates for ENTSO-E electricity from natural gas. | Add `startYear=2024` and `endYear=2024`, using the dataset's ENTSO-E 2024 statistics reference. | 1 dataset |
| Validity dates for GB and ES natural-gas heat/power datasets. | Add start/end year `2025`, using “Time of publications” and the cited 2025 report. This does not assert that all underlying inventory data are from 2025. | 2 datasets |
| Empty `timePeriod.dataValidForEntirePeriod`. | `false`, so whole-period validity is not asserted. Preserve the original unknown value. | 197 fields |
| Empty `dataGeneratorAndPublication.copyright`. | `true` as a conservative schema fallback. This does not verify licensing rights. | 5 fields |
| No publication year or citation text for the compatibility source in the concrete-disposal dataset. | `2026` solely as a BAFU release-year fallback. The actual publication year remains unknown. | 1 source |

The date overrides are scoped to these files:

- ENTSO-E electricity: `process_6e6e5583-44b7-38c8-8f92-8dc8f85dbf1e.xml`.
- GB heat/power: `process_76f8d21b-a86c-3531-b5cc-145cb6cf96aa.xml`.
- ES heat/power: `process_f6b4f830-ce92-35f2-bf8f-9a9a2e289445.xml`.

The publication-year override is scoped to source `136635` in `process_09984ab6-a49a-46a6-801a-ddcbc3b881bc.xml`. That source number is reused elsewhere for other compatibility citations, so the replacement is deliberately not applied globally by source number.

## 5. Parser limitations requiring runtime adapters

Some schema-valid XML values also exposed limitations in the installed parser. The following adapters run only during the single-process extraction step and restore the original parser references afterward. Installed package files are unchanged.

| Valid input rejected by the installed parser | Adapter behavior |
| --- | --- |
| Datetimes with fractional seconds and offsets, such as `2023-03-29T18:04:18.534+02:00`. | [`timestamp_compat.py`](../scripts/ecospold%20importer/timestamp_compat.py), enabled with `--iso-timestamps`, preserves the offset and fractional seconds up to Python's six-digit microsecond precision. It rejects finer precision rather than silently truncating it. |
| Calendar dates with offsets, such as `2023-12-31+01:00`. | [`date_compat.py`](../scripts/ecospold%20importer/date_compat.py), enabled with `--iso-dates`, retains the stated calendar day without converting it to UTC. Year/month boundary handling stays with the installed parser. |

Brightway's date tags contain `YYYY-MM-DD`, so those tags do not retain the original date timezone. The full XML values remain available. Separately, the space-to-`T` timestamp repair in section 2 changes invalid XML Schema spelling in the files themselves.

## 6. Verification, audit trail, and remaining work

The final run used the `bw` conda environment with **bw2data 4.7, bw2io 0.9.17, pyecospold 4.0.0, and lxml 6.1.1**.

| Check | Result / evidence |
| --- | --- |
| Full XSD validation, complete file set, and output hashes | **11,947 / 11,947 files pass**, with no unresolved schema defects. See [final validation report](../reports/generated/ecospold1-final-validation.json). |
| Inventory comparison against raw XML | **All 420,063 rows preserved**, including amounts, units, uncertainty fields, inventory names, categories, and flow directions. Ordered exchange payloads, reference-function metadata, and geography are compared, allowing only the explicitly documented schema repairs. Implemented in [validate_collection.py](../scripts/ecospold%20importer/validate_collection.py). |
| Reversibility of the final schema stage | Every file's repair log reconstructs its full input canonical XML, including existing comments. See [schema repair report](../reports/generated/ecospold1-schema-repair.json). |
| Brightway extraction and default strategies | **11,947 datasets extracted; all nine strategies completed without exceptions**, using both adapters. See [import report](../reports/generated/ecospold1-schema-fixed-import.json). |
| Regression tests | **48 pass**, including tests that deliberately corrupt amounts, uncertainty fields, and directions to check that the inventory audit rejects them. |

Earlier per-file reports are also stored in `reports/generated/`: namespace, date, publisher, company-code, source-number, administrative-order, and exchange-number repair reports. They contain input/output SHA-256 hashes and the applicable change records. The final schema stage changed 6,966 files; earlier stages had already repaired the rest of the issues described above.

Metadata retained in XML comments is not automatically copied into Brightway's structured metadata fields. Keep the repaired XML, repair logs, alias mapping, and override file alongside downstream imports. In particular, names and company codes that were too long remain fully recoverable there, while their schema-constrained fields are empty.

The final stage serializes changed XML with `lxml`, so whitespace, attribute formatting, and the XML declaration can differ. The guarantees are the documented preservation checks, not byte-identical output to the raw files. The original raw files remain available and unchanged.

**Linking is still incomplete:** the import report records **295,213 unlinked exchanges**, and the isolated test project has no `biosphere3` database. The check therefore returns exit code `2` (`status: unlinked`) despite successful extraction and strategies. No inventory database was written. The stock extractor also emits a divide-by-zero warning for zero-valued lognormal exchanges; the original amounts and uncertainty fields were retained.

Generated XML, logs, and JSON reports are ignored by Git and must be regenerated or shared separately. This report and the implementation/override files provide the reviewable explanation and reproduction instructions. Successful schema validation establishes structural conformity; it does not verify the scientific correctness of the source inventory or turn the approved fallbacks into measured facts.
