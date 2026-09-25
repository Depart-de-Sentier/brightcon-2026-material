# BAFU 2026 mappings for identified source files

The [context migration](../schemas/mappings/bafu-2026-biosphere-context.json) adds 15 rules after the source-review stage. Rules match type, name, complete categories, unit, source CAS, and the exact consuming XML filename. The helper temporarily supplies `_migration_source_file` to bw2io's migration strategies and removes it afterwards, including on failure. It rejects missing or ambiguous source filenames and requires a unique target.

Every original name, category, and unit remains in `bafu original biosphere`. Amounts, uncertainty parameters, source CAS values, comments, dataset locations, and existing links remain unchanged. The raw and repaired XML files are not edited.

## Approved railway-land proxies

Fourteen exchanges in seven railway datasets use `Occupation, sealed soil` or `Transformation, to sealed soil`. The [2024 railway infrastructure report](../data/raw/BAFU-2026%20v1%20LCI%20Reports/2024%20-%20LCA%20railway%20infrastructure%20-%20Kaegi.pdf) and XML comments identify bridge foundations, platforms, and pedestrian access ramps. The report distinguishes sealed structures from railway trackbed; these are explicitly approved proxies, rather than evidence of an incorrect source label.

The user approved: **“Use documented railway-land proxies.”** Each source maps to the corresponding `traffic area, rail network` occupation or transformation target, keeping `natural resource / land` and its unit:

| Dataset | Source filename | Occupation (m²·year) | Transformation to (m²) |
| --- | --- | ---: | ---: |
| Railway track, with overpass construction, double track | `process_3f0401dd-f30d-3992-9fb8-a8ee07038625.xml` | 1,100 | 11.7 |
| Railway track, on bridge, single track | `process_5b98ffcb-442f-39b6-b5c7-c01ea562abff.xml` | 700 | 7.4468 |
| Railway track, with overpass construction, single track | `process_0aa0d299-066a-3591-88a1-514d49213737.xml` | 700 | 7.4468 |
| Pedestrian overpass, over 2 tracks | `process_e66e9555-cf47-33e9-9ed4-1a7d343c84bc.xml` | 1 | 0.0128 |
| Railway track, on bridge, double track | `process_f549a675-eaf1-3d02-8f45-73fd785d7851.xml` | 1,100 | 11.7 |
| Platform, standard | `process_6ae02038-e9af-3cf0-9db0-eb4c0fde9cc3.xml` | 1 | 0.0128 |
| Pedestrian underpass, underneath 2 tracks | `process_cc35c5b9-2d9d-3972-a31c-a8b23a4055bb.xml` | 1 | 0.012813 |

The source report discusses ramps/platforms on PDF pages 41, 43, and 45, bridges on pages 48–49, and overpass construction on pages 53–54. XML comments identify 11 m double-track or 7 m single-track widths with 10% attributed to bridge foundations; the pedestrian-overpass occupation comment specifies ramps only.

The biosphere 3.10 targets are:

- `Occupation, traffic area, rail network`, square meter-year: `062a6faf-b1a5-4a6a-aa02-47ae3ec566a8`.
- `Transformation, to traffic area, rail network`, square meter: `0abf9db7-b5a2-4c18-8ec6-aca3a7fb5579`.

Standard LCIA uses general railway-land factors and loses the sealing distinction; retaining the original label does not restore this distinction automatically. **Seven sealed-soil occupation exchanges in aggregated plastics inventories remain unresolved.** Their source context does not justify a railway proxy.

## One source-supported water return

`process_e1108fba-40a1-3c02-b715-f190d916bc74.xml`, **Water, deionised, water balance according to MoeK 2013, at plant / RER**, contains one `Waste water/m3` emission of **0.00011 m³** to generic water.

The cited [2017 water-footprint report](../data/raw/BAFU-2026%20v1%20LCI%20Reports/2017%20-%20Water%20footprint%20euro.%20rooftop%20PV%20electricity%20-%20Stolz.pdf), section A.1.1 (PDF page 31), identifies the added water emissions as returns to the original basin. Table A.3 (PDF page 33) records the same 1.10 × 10⁻⁴ m³ as `Water, CN`, with the same 1.11 kg tap-water input per kilogram of deionised water and separate chloride/sodium emissions. Section A.1.2 states that regional variants differ only in water geography and electricity mix.

This evidence supports correcting the label to `Water`, category `water`, cubic meter, UUID `2404b41a-2eed-4e9d-8ab6-783946fdf5d6`, under the already approved generic-water convention. There is no mass conversion. The original label remains on the exchange, and the dataset retains its RER location; no region is inferred from the exchange name. **The rule applies only to this file.** The other 60 `Waste water/m3` occurrences remain unresolved.

The 84 `Chemically polluted water` occurrences also remain unresolved. Section 10.1.4, printed page 58, of the [2025 oil/gas extraction report](../data/raw/BAFU-2026%20v1%20LCI%20Reports/2025%20-%20LCI%20crude%20oil%20and%20natural%20gas%20extraction%20-%20Meili.pdf) separates excess produced water from balanced freshwater returns and excludes that excess from water-scarcity assessment. Mapping it to ordinary Water could introduce unintended freshwater credits.

## Verification and evidence

The full `bw` notebook check links **15 additional exchanges**: 14 railway proxies and one water correction. It reaches **290,565 linked of 293,747 biosphere exchanges**, with **3,182 unresolved across 175 signatures**. All 11,947 datasets and 420,063 exchange rows remain, and all technosphere exchanges link.

Independent complete-record comparison checks that only the declared names, audit metadata, and unique input links change. Every rule matches once. All numerical and uncertainty fields are unchanged, the seven plastics exchanges remain unlinked, and temporary matching fields are removed. Reapplication changes nothing. The final audit agrees with the live importer and does not modify it. No inventory database is written.

Source-document and raw XML hashes, original XML attributes, target UUIDs, and decision bases are in `reports/generated/biosphere-context-evidence.json`. Verification is in `biosphere-context-migration-check.json`; this stage’s unresolved report is `biosphere-unlinked-after-context.json`. The preceding stage now writes `biosphere-unlinked-after-source-review.json`.

The focused tests use the installed bw2io migration strategies and cover filename isolation, cleanup on errors, source CAS restrictions, stale links, and idempotence. Run them in `bw` from `hackathon/`:

```bash
BRIGHTWAY2_DIR="$PWD/artifacts/brightway" conda run --no-capture-output -n bw python -m unittest discover -s "scripts/ecospold importer" -p "test_biosphere_*.py"
```
