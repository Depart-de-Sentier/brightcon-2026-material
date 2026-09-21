# Schema mappings

Add mappings between candidate schemas, existing standards, and source data formats here.

## BAFU 2026 technosphere migrations

Two standard bw2io migration files address supplier mismatches after the repaired EcoSpold 1 import and its default strategies:

- [`bafu-2026-technosphere.json`](bafu-2026-technosphere.json): 24 rules matching `type`, `name`, `categories`, `unit`, and `location`. These cover ENTSO-E geography, gas volume labels, Finnish electricity output units, direct-air-capture infrastructure, wind geography, and a concrete-disposal proxy.
- [`bafu-2026-technosphere-context.json`](bafu-2026-technosphere-context.json): 10 electricity-mix rules adding `_migration_source_file` to distinguish exchanges with identical labels in different consuming datasets. Their destinations are SE, RER, ENTSO-E, or IN.

Most rules select `type: technosphere`. Two rules instead correct the Finnish supplier's dataset (`process`) and production-exchange unit from MJ to kWh, based on its stated fuel input and electrical efficiency. Dataset codes remain stable to preserve existing links. Biosphere exchanges are excluded.

The [evidence and decisions](../../docs/bafu-2026-technosphere-migrations.md) document each correction and proxy. In particular, the gas conversion is an approved **1:1 unit relabeling**, with no temperature/pressure conversion; the onshore wind name is retained despite its contradictory offshore comment; and the concrete, Indian electricity, and unidentified Swiss electricity-import substitutions are approved proxies. All amounts, uncertainty parameters, and original comments remain unchanged. Linking a proxy does not establish environmental equivalence.

## Use in the notebook

The [import notebook](../../scripts/import_fixed_ecospold.ipynb) applies both files in its **Apply the technosphere migrations** cell, immediately after extraction and the default strategies:

```python
from technosphere_migrations import apply_technosphere_migrations

apply_technosphere_migrations(importer, ROOT / "schemas/mappings")
```

The notebook setup adds `scripts/ecospold importer/` to Python's import path. The helper reads both JSON files on every run, checks for duplicate matching rules, registers them in the current Brightway project, and applies them through `importer.migrate`. It temporarily supplies each exchange's source filename for the contextual migration and removes that marker afterwards. It then relinks technosphere exchanges using `name`, `categories`, `unit`, and `location`. bw2io compares matching fields case-insensitively.

After editing either JSON, rerun the extraction cell and subsequent cells to start from fresh importer data. Migration registration is stored in the current project; corrections affect the importer's in-memory data. Raw and repaired XML files remain unchanged. The baseline Python import scripts still run without these migrations.

## Initial ENTSO-E corrections

The first five rules resolve 1,412 exchange occurrences. Their names explicitly identify ENTSO-E, and each identifies exactly one supplier with the same name, categories, and unit in this release.

| Voltage | Original location | Replacement | Exchange occurrences |
| --- | --- | --- | ---: |
| High | Empty | `ENTSO-E` | 22 |
| High | `ENTSO` | `ENTSO-E` | 9 |
| Low | Empty | `ENTSO-E` | 238 |
| Medium | Empty | `ENTSO-E` | 1,129 |
| Medium | `ENTSO` | `ENTSO-E` | 14 |

The other rules address the remaining 19 signatures across 54 exchange occurrences. Their source files, target suppliers, and reasoning are listed in the [evidence document](../../docs/bafu-2026-technosphere-migrations.md).

## Validation

Tested on the full collection in `bw` by executing the notebook through its migration cell: **zero unlinked technosphere exchanges remain**. All 24 initially unmatched signatures (1,466 occurrences) link, including the 19 signatures (54 occurrences) remaining after the initial ENTSO-E rules.

The check retained all 11,947 datasets and 420,063 exchange rows, verified a unique supplier for every newly linked exchange, and compared every record against only the declared metadata replacements and new links. Amounts, uncertainty parameters, comments, dataset codes, and existing links were preserved. All 34 migration rules matched their intended record types, and the temporary source-file field was removed.

The local verification report, including rule counts and each newly linked consumer/supplier pair, is `reports/generated/technosphere-migration-check.json`. No inventory database was written during verification. Biosphere matching was outside this check; its 293,747 exchanges remain unlinked at this notebook stage.
