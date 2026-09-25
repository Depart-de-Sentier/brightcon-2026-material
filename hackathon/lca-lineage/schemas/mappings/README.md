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
| [Reviewed compartments](bafu-2026-biosphere-compartments.json) | 32 rules: landfill-indicator categories, approved parent compartments, TOC aggregates, and long-term river timing approximations with originals retained | 1,495 | 3,210 |
| [Source inventory review](bafu-2026-biosphere-source-review.json) | 4 CAS-specific rules: source-verified Metam-sodium and approved broader forest/water targets | 13 | 3,197 |
| [Identified source files](bafu-2026-biosphere-context.json) | 15 filename-specific rules: approved railway-land proxies and one source-supported water return | 15 | 3,182 |
| [Plastics source review](bafu-2026-biosphere-plastics-source-review.json) | 4 filename-specific rules: two chloride-to-element conversions, chromium-VI identity, and approved generic-soil PAH | 4 | 3,178 |
| [EPS metal identities](bafu-2026-biosphere-eps-metals.json) | 2 exact-quantity/file rules restoring palladium and rhodium; historical catalog UUIDs retained | 2 | 3,176 |
| [Plastics conversions](bafu-2026-biosphere-plastics-conversions.json) | 32 filename-specific rules: source-defined coal/peat energy-to-mass and approved EPS oxide-to-element conversions | 32 | 3,144 |
| [Plastics chemical identities](bafu-2026-biosphere-plastics-chemicals.json) | 3 filename-specific rules restoring source-defined 1,1,2-trichloroethane | 3 | 3,141 |
| [Historical name correspondence](bafu-2026-biosphere-historical-names.json) | 2 rules for the legacy dichlorobenzene name and an exact N-methyl-2-pyrrolidone synonym, preserving compartments | 83 | 3,058 |
| [Approved NO₂ aggregation](bafu-2026-biosphere-nitrogen-dioxide.json) | 2 source-file rules using NOx-as-NO₂ with original labels, amounts and uncertainty retained | 2 | 3,056 |
| [Mosaic agricultural land](bafu-2026-biosphere-land-mosaic.json) | 18 source-file rules restoring the original mosaic land class as heterogeneous agricultural land | 18 | 3,038 |
| [Approved diesel-carbon approximation](bafu-2026-biosphere-diesel-carbon.json) | 12 source-file rules using fossil CO₂/CO targets, retaining original labels and all numerical fields | 12 | 3,026 |
| [Approved uranium convention](bafu-2026-biosphere-uranium-convention.json) | 7 source-file rules converting MJ to uranium kg using the approved 560,000 MJ/kg convention | 7 | 3,019 |
| [Approved wood density](bafu-2026-biosphere-wood-density.json) | 2 source-file rules converting wood mass/source energy to m³ using 632.5 kg/m³ | 2 | 3,017 |
| [PM10-labeled metal pairs](bafu-2026-biosphere-pm10-metals.json) | 26 exact-quantity/file/pair rules restoring source-defined palladium and rhodium emissions | 26 | 2,991 |

Evidence, assumptions, and verification are documented for the [catalog](../../docs/bafu-2026-biosphere-catalog-migrations.md), [resources](../../docs/bafu-2026-biosphere-resource-migrations.md), [reviewed mappings](../../docs/bafu-2026-biosphere-reviewed-migrations.md), [water/context rules](../../docs/bafu-2026-biosphere-water-context-migrations.md), [chemistry](../../docs/bafu-2026-biosphere-chemistry-migrations.md), [gas-unit assumption](../../docs/bafu-2026-biosphere-gas-unit-migrations.md), [land/resource mappings](../../docs/bafu-2026-biosphere-land-resource-migrations.md), [follow-up mappings](../../docs/bafu-2026-biosphere-followup-migrations.md), [compartment mappings](../../docs/bafu-2026-biosphere-compartment-migrations.md), [source inventory review](../../docs/bafu-2026-biosphere-source-review.md), [identified source files](../../docs/bafu-2026-biosphere-context-migrations.md), [plastics source review](../../docs/bafu-2026-biosphere-plastics-source-review.md), [EPS metal identities](../../docs/bafu-2026-biosphere-eps-metals.md), [plastics conversions](../../docs/bafu-2026-biosphere-plastics-conversions.md), [plastics chemical identities](../../docs/bafu-2026-biosphere-plastics-chemicals.md), [historical name correspondence](../../docs/bafu-2026-biosphere-historical-names.md), and [approved NO₂ aggregation](../../docs/bafu-2026-biosphere-nitrogen-dioxide-proposal.md).

The current verified result is **290,756 linked of 293,747 biosphere exchanges**; **2,991 remain across 155 signatures**. All technosphere exchanges link. The final diagnostic report is `reports/generated/biosphere-unlinked.json`; each preceding stage writes a separate `biosphere-unlinked-after-<stage>.json` report.

Regional water and the approved Swiss rail exchanges retain their original name, unit, categories, and region in `bafu original biosphere` exchange metadata. The approved broader land classes likewise retain original detailed labels. Generic LCIA does not automatically use these retained distinctions. Genuinely unsupported flows remain unresolved pending a supported target, as requested; no placeholder biosphere database is created. All migration stages preserve exchange rows, and unit conversions rescale uncertainty through bw2io. Rerun extraction and all migration cells after editing any mapping.

Compound-to-element rules retain the original labels and the formula/atomic-weight basis in exchange metadata; bw2io rescales amounts and uncertainty together. The gas rules instead retain `bafu unit assumption` and omit `multiplier`, keeping every numerical field exactly unchanged. This documented 1:1 assumption is restricted to the four approved source signatures.

The compartment rules correct two landfill indicators to the official `inventory indicator / waste` class and apply the approved generic-air targets for nine high-altitude signatures. Original categories remain in exchange metadata. No amount or uncertainty is changed. The additional approved parent-compartment mappings cover 14 urban-air/surface-water/industrial-soil rows, 75 fossil-water suspended-solids rows, and 38 indoor TCDD rows. Generic LCIA does not automatically use the retained altitude, exposure, or receiving-environment distinctions.

The same stage adds five reviewed surface-water chemical aliases, 112 approved TOC → Organic carbon aggregate mappings, and 200 approved long-term river → surface-water mappings. TOC targets had no factors in the 668 installed method components checked. Original long-term categories remain in audit metadata, but standard LCIA can now include those emissions in `no LT` methods. The notebook produces `biosphere-remaining-worklist.json` and `.csv` from the live importer; candidate matches are review leads, not automatic mappings.

The source-file stage uses temporary `_migration_source_file` matching through bw2io, in addition to the complete source signature and CAS. It applies 14 approved railway-land proxies while leaving seven sealed-soil exchanges in plastics unresolved, and one documented deionised-water return correction while leaving other wastewater unresolved. All amounts and uncertainty values are unchanged; the temporary filename field is removed after migration.

The subsequent plastics source-review stage recovers the mass basis of two EPS chloride resources from their original ILCD flow records and uses documented elemental factors. It also restores the chromium-VI identity of a mislabelled industrial-soil row by comparison with the original inventory and its neighbouring rows. A fourth rule restores PAH identity and applies the approved generic-soil target while retaining the original label and industrial-soil compartment. All four rules are scoped to the EPS file.

The EPS metal stage distinguishes two mislabelled metal emissions from genuine PM10 by their exact source quantities and filename. `_migration_source_amount` contains canonical float text only during bw2io matching; duplicate matches are rejected and both temporary fields are removed afterwards. The original labels remain in metadata. Historical generic-metal UUIDs identify the current Palladium II and Rhodium III targets; no measured oxidation state is inferred and no quantity is rescaled.

The final plastics conversion stage converts 28 coal resources using source-defined net calorific values (11.9 and 26.3 MJ/kg), retained with the source flow UUID in `bafu energy conversion`. Three approved oxide emissions use contained-element masses and existing metal-ion air targets, preserving their oxide labels and chemical mass basis. LCIA loses the oxide-form distinction. Amounts and uncertainty scale together; all compartments are preserved.

The [targeted reassessment](../../docs/bafu-2026-biosphere-targeted-reassessment.md) records the source-defined mosaic correspondence and the approved carbon approximation, and the approved uranium and wood conversions. Those nine rules retain `bafu conversion assumption` metadata with their factor, interpreted source quantity unit, limitation and documentation link. Candidate files remain historical proposal snapshots and are not loaded automatically.

The [PM10 pair review](../../docs/bafu-2026-biosphere-pm10-metals.md) restores 26 mislabeled metals using the existing catalog correspondence. `_migration_pair_member` only distinguishes a verified pair of identical dictionaries; the helper requires exactly two complete matching source records, preserves all numerical fields, and removes the temporary marker. The remaining 94 generic-air PM10-labeled rows still need a size-distribution basis.
