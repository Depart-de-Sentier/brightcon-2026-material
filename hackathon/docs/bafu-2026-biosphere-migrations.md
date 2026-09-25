# BAFU 2026 biosphere category migrations

The first pass fixes category labels before matching against `ecoinvent-3.10-biosphere`. The default EcoSpold 1 import exposes 293,747 biosphere exchange rows with 2,679 distinct name/category/unit signatures. Their BAFU category labels differ from the target database, so none initially link.

## Exact changes

[`bafu-2026-biosphere-categories.json`](../schemas/mappings/bafu-2026-biosphere-categories.json) is a standard bw2io migration with fields `type` and `categories`. Its 26 rules select only `type: biosphere` and replace only `categories`. They leave names, units, amounts, uncertainty, comments, production exchanges, and technosphere exchanges unchanged. Raw and repaired XML are unchanged.

The category aliases follow the installed bw2io 0.9.17 compatibility tables, `bw2io.compatibility.SIMAPRO_BIOSPHERE` and `SIMAPRO_BIO_SUBCATEGORIES`. BAFU uses these SimaPro-style labels inside EcoSpold files. The general `normalize_biosphere_categories` strategy targets different EcoSpold 2-to-3 aliases and does not cover all these BAFU labels directly. Explicit rules make this import's changes reviewable and independent of future changes to the installed tables.

| Original categories | Replacement categories | Exchange rows |
| --- | --- | ---: |
| economic issues | economic | 13 |
| emissions to air | air | 27,741 |
| emissions to air / high. pop. | air / urban air close to ground | 65,624 |
| emissions to air / indoor | air / indoor | 38 |
| emissions to air / low. pop. | air / non-urban air or from high stacks | 66,717 |
| emissions to air / low. pop., long-term | air / low population density, long-term | 3,505 |
| emissions to air / stratosphere + troposphere | air / lower stratosphere + upper troposphere | 2,610 |
| emissions to soil | soil | 4,065 |
| emissions to soil / agricultural | soil / agricultural | 11,401 |
| emissions to soil / forestry | soil / forestry | 179 |
| emissions to soil / industrial | soil / industrial | 2,645 |
| emissions to water | water | 11,029 |
| emissions to water / fossilwater | water / fossilwater | 129 |
| emissions to water / groundwater | water / ground- | 6,807 |
| emissions to water / groundwater, long-term | water / ground-, long-term | 9,586 |
| emissions to water / lake | water / surface water | 2,897 |
| emissions to water / ocean | water / ocean | 10,616 |
| emissions to water / river | water / surface water | 36,160 |
| emissions to water / river, long-term | water / river, long-term | 200 |
| non material emissions | non-material | 1,423 |
| resources | natural resource | 663 |
| resources / biotic | natural resource / biotic | 1,191 |
| resources / in air | natural resource / in air | 711 |
| resources / in ground | natural resource / in ground | 11,716 |
| resources / in water | natural resource / in water | 5,509 |
| resources / land | natural resource / land | 10,572 |

An absent subcategory remains absent. River and lake emissions map to the target's shared `surface water` compartment. `groundwater, long-term` and `low. pop., long-term` retain their time horizon.

Three unsupported subcategories are deliberately retained after translating their top-level compartment: `indoor`, `river, long-term`, and `fossilwater`. In particular, bw2io's generic SimaPro table maps `river, long-term` to ordinary surface water; this migration does **not** apply that temporal approximation. The later [reviewed compartment stage](bafu-2026-biosphere-compartment-migrations.md) now applies the explicitly approved long-term river → surface-water approximation while retaining the original timing category in audit metadata. Unspecified resources are not assigned to land, water, air, or ground by name alone. `non-material` and `economic` labels are normalized without inventing target flows for noise or water embodied in products.

## Notebook and remaining-flow report

The [import notebook](../scripts/import_fixed_ecospold.ipynb) calls [`apply_biosphere_category_migration`](../scripts/ecospold%20importer/biosphere_migrations.py) after the technosphere migrations. It loads the JSON, registers it in the current Brightway project, applies it, and matches biosphere exchanges on **name, complete categories, and unit**. Internal technosphere matching is restricted to technosphere exchanges.

The helper writes `reports/generated/biosphere-unlinked-after-categories.json`, grouping unresolved exchanges by name/category/unit with occurrence counts and up to three source-file examples. Its diagnostic groups distinguish missing names, unit mismatches, and category mismatches; these labels are investigation aids, not approved mappings. It retains every unresolved exchange and does not write an inventory database.

Rerun extraction and both migration steps after editing the mapping files. The helper also supports repeating the category step without changing already-normalized data or established links.

The [second pass](bafu-2026-biosphere-flow-migrations.md) reviews explicit name aliases and exact unit conversions against the original flow definitions. Examples include `Particulates` versus `Particulate Matter`, biogenic versus non-fossil labels, metals with explicit oxidation states in the target, and water expressed in kilograms versus cubic metres. Straightforward cases now have separate flow-migration rules; metal speciation and water density still require further review. Ignoring categories or units would risk linking different elementary flows.

## Full-collection verification

The notebook was executed in a fresh `bw` Python process through the biosphere category migration, without executing the later exchange-dropping, database-writing, or LCA cells.

| Result | Exchange occurrences |
| --- | ---: |
| Biosphere exchanges before migration, all unlinked | 293,747 |
| Linked after category correction | 170,259 |
| Still unlinked | 123,488 |

The remaining flows form **1,342 distinct name/category/unit signatures** (some former river/lake signatures now share the same surface-water category). All 11,947 datasets and 420,063 total exchange rows were retained. Every newly linked biosphere exchange matched exactly one target. A complete record comparison verified that only the declared categories and new `input` links changed: names, units, amounts, uncertainty, comments, all production exchanges, and all technosphere exchanges were preserved. Repeating the category migration produced identical data and links. Zero unlinked technosphere exchanges remain.

The verification report is `reports/generated/biosphere-migration-check.json`. The unresolved-flow report remains the input for the next pass; the inventory is not yet fully linked.

| Remaining diagnostic group | Signatures | Exchange occurrences |
| --- | ---: | ---: |
| Same name and unit, different or unavailable categories | 403 | 65,400 |
| Name absent from biosphere 3.10 | 789 | 52,332 |
| Same name and categories, different unit | 150 | 5,756 |

The results above describe the category-only stage. The subsequent [name and unit migration](bafu-2026-biosphere-flow-migrations.md) links another 30,563 exchanges, leaving 92,925 across 1,003 signatures. Its final unresolved report is `reports/generated/biosphere-unlinked.json`.
