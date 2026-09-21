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

The local verification report, including rule counts and each newly linked consumer/supplier pair, is `reports/generated/technosphere-migration-check.json`. No inventory database was written during verification. Biosphere matching was outside this technosphere check; its 293,747 exchanges were unlinked at that stage, before the category step below.

## BAFU 2026 biosphere categories

[`bafu-2026-biosphere-categories.json`](bafu-2026-biosphere-categories.json) contains 26 category-only rules for biosphere exchanges. It translates labels such as `emissions to air / low. pop.` to `air / non-urban air or from high stacks`, preserving names, units, amounts, and uncertainty. The notebook applies it after the technosphere migrations and matches against biosphere 3.10 using the full name/category/unit combination.

The [biosphere migration notes](../../docs/bafu-2026-biosphere-migrations.md) list every rule, its source, and remaining limitations. The category helper saves its intermediate unresolved signatures, occurrence counts, and example XML files in `reports/generated/biosphere-unlinked-after-categories.json`.

Category-only verification in `bw`: **170,259 biosphere exchanges link; 123,488 remain across 1,342 signatures**. All 420,063 inventory rows and their numerical values were retained, with no changes to technosphere links. Remaining names, units, and compartments require a separate review.

## BAFU 2026 biosphere names and units

[`bafu-2026-biosphere-flows.json`](bafu-2026-biosphere-flows.json) adds 339 explicit rules matching `type`, `name`, `categories`, and `unit` after category normalization. These cover reviewed chemical synonyms, particulate and biogenic labels, redundant `/m3` suffixes, Bq → kBq (×0.001), and waste-heat kWh → MJ (×3.6). Every target must be unique, and compartments stay unchanged. Unit-conversion multipliers use bw2io's amount/uncertainty rescaling support.

The notebook applies this file through `apply_biosphere_flow_migration` in the existing biosphere helper. See the [flow evidence and validation](../../docs/bafu-2026-biosphere-flow-migrations.md) for every alias and the conversion checks. Rerun extraction and all migration cells after editing either biosphere JSON file.

Tested on the full collection: **30,563 additional exchanges link**, for **200,822 linked biosphere exchanges** in total. **92,925 remain across 1,003 signatures**, recorded in `reports/generated/biosphere-unlinked-after-flows.json`. All exchange rows and non-biosphere links were preserved; only 3,134 amounts change numerically, through exact unit conversions. Repeating this migration does not rescale them twice.

## Subsequent biosphere mappings

Apply these files in notebook order, after the initial names/units pass:

| Migration | Scope | Additional links | Unlinked occurrences after this step |
| --- | --- | ---: | ---: |
| [Historical catalog](bafu-2026-biosphere-catalog.json) | 464 CAS-specific rules following historical UUID correspondence and official synonyms | 68,318 | 24,607 |
| [Resource names and water units](bafu-2026-biosphere-resources.json) | 52 rules: elemental resource labels and water kg → m³ | 5,799 | 18,808 |
| [Additional reviewed mappings](bafu-2026-biosphere-reviewed.json) | 308 rules: spelling/synonyms, missing resource subcategories, and approved regional water emissions/withdrawals and broader land classes | 11,186 | 7,622 |
| [Water names and resource contexts](bafu-2026-biosphere-water-context.json) | 26 rules: well/fossil/process-water definitions, remaining supported regional water, and resource classes | 1,045 | 6,577 |
| [Chemical aliases and elemental mass](bafu-2026-biosphere-chemistry.json) | 9 rules: approved TiO₂/KCl/barite mass conversions and reviewed chemical aliases | 541 | 6,036 |
| [Resource-gas unit assumption](bafu-2026-biosphere-gas-units.json) | 4 rules: approved 1:1 relabeling to standard cubic metres, with unknown source reference conditions | 363 | 5,673 |
| [Land and resource mappings](bafu-2026-biosphere-land-resources.json) | 18 rules: historical land/graphite renames, approved broader rainforest/organic classes, peat category, and European water aliases | 910 | 4,763 |
| [Reviewed follow-up](bafu-2026-biosphere-followup.json) | 8 rules: approved Swiss rail and unspecified used-land classes, caesium Bq → kBq, reviewed quicklime CO₂ origin, and an exact chlorophenol synonym | 58 | 4,705 |
| [Reviewed compartments](bafu-2026-biosphere-compartments.json) | 21 rules: exact landfill-indicator categories and approved generic air/water/soil targets with original compartments retained | 1,178 | 3,527 |

Evidence, assumptions, and verification are documented for the [catalog](../../docs/bafu-2026-biosphere-catalog-migrations.md), [resources](../../docs/bafu-2026-biosphere-resource-migrations.md), [reviewed mappings](../../docs/bafu-2026-biosphere-reviewed-migrations.md), [water/context rules](../../docs/bafu-2026-biosphere-water-context-migrations.md), [chemistry](../../docs/bafu-2026-biosphere-chemistry-migrations.md), [gas-unit assumption](../../docs/bafu-2026-biosphere-gas-unit-migrations.md), [land/resource mappings](../../docs/bafu-2026-biosphere-land-resource-migrations.md), [follow-up mappings](../../docs/bafu-2026-biosphere-followup-migrations.md), and [compartment mappings](../../docs/bafu-2026-biosphere-compartment-migrations.md).

The current verified result is **290,220 linked of 293,747 biosphere exchanges**; **3,527 remain across 191 signatures**. All technosphere exchanges link. The final diagnostic report is `reports/generated/biosphere-unlinked.json`; each preceding stage writes a separate `biosphere-unlinked-after-<stage>.json` report.

Regional water and the approved Swiss rail exchanges retain their original name, unit, categories, and region in `bafu original biosphere` exchange metadata. The approved broader land classes likewise retain original detailed labels. Generic LCIA does not automatically use these retained distinctions. Genuinely unsupported flows remain unresolved pending a supported target, as requested; no placeholder biosphere database is created. All migration stages preserve exchange rows, and unit conversions rescale uncertainty through bw2io. Rerun extraction and all migration cells after editing any mapping.

Compound-to-element rules retain the original labels and the formula/atomic-weight basis in exchange metadata; bw2io rescales amounts and uncertainty together. The gas rules instead retain `bafu unit assumption` and omit `multiplier`, keeping every numerical field exactly unchanged. This documented 1:1 assumption is restricted to the four approved source signatures.

The compartment rules correct two landfill indicators to the official `inventory indicator / waste` class and apply the approved generic-air targets for nine high-altitude signatures. Original categories remain in exchange metadata. No amount or uncertainty is changed. The additional approved parent-compartment mappings cover 14 urban-air/surface-water/industrial-soil rows, 75 fossil-water suspended-solids rows, and 38 indoor TCDD rows. Generic LCIA does not automatically use the retained altitude, exposure, or receiving-environment distinctions.
