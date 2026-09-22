# Mosaic agricultural land correspondence

The [migration](../schemas/mappings/bafu-2026-biosphere-land-mosaic.json) restores 18 land-use exchanges in six original PlasticsEurope inventories: ethylene, ethylene glycol, PET, pyrolysis gasoline, purified terephthalic acid and xylenes.

| BAFU label | Existing biosphere 3.10 target | Occurrences |
| --- | --- | ---: |
| Occupation, agriculture, mosaic | Occupation, heterogeneous, agricultural | 6 |
| Transformation, from agriculture, mosaic | Transformation, from heterogeneous, agricultural | 6 |
| Transformation, to agriculture | Transformation, to heterogeneous, agricultural | 6 |

The original process records identify all three flows as mosaic agriculture. The six transformation-to labels lost the word “mosaic” during export. Their original flow UUID is `b886560e-7ab8-4ec9-8a0a-802affe63186`; occupation uses `1d443c61-ff6f-419a-99a8-9ff3055f4922`, and transformation-from uses `aeea42cc-4215-465f-981f-ae2ab387fbb9`. All are version 03.00.000. Each BAFU quantity exactly matches its original process quantity, and the flow-property records confirm area-time for occupation and area for transformation.

The correspondence is inferred from matching definitions: the [ecoinvent data-quality guidelines](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Database/Fundamentals/dataqualityguideline_ecoinvent_3_20130506.pdf), Table 6.1, printed page 48, describe heterogeneous agricultural land as crop production intercropped with trees. The [JRC land-use review](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC141945/JRC141945_01.pdf), Table 18, printed page 45, gives the same defining characteristic for agriculture mosaic. This is a correspondence between defined classes, without selecting a crop, irrigation regime or intensity.

Every rule matches the source filename, full flow signature and original CAS field. Only the name, original-label audit metadata and input link change. Amounts, units, compartments, transformation directions, uncertainty and comments remain unchanged. The seven remaining generic agriculture inventories are excluded: their original labels combine agriculture and forest and do not establish mosaic agriculture.

The notebook applies this stage after NO₂ aggregation. It writes `reports/generated/biosphere-unlinked-after-land-mosaic.json`; subsequent stages apply the approved diesel-carbon, uranium and wood mappings, followed by PM10-metal restoration, which writes the final report. NO₂ writes `biosphere-unlinked-after-nitrogen-dioxide.json`. Source rows, UUIDs and artifact hashes are recorded in `reports/generated/biosphere-land-mosaic-evidence.json`.

Run the full import verification in the `bw` environment:

```sh
conda run -n bw python "scripts/ecospold importer/check_land_mosaic.py"
```

This check verifies the mosaic-land and approved diesel-carbon, uranium and wood stages plus the PM10-metal stage. It compares every inventory record against the declared changes, verifies unique targets and source matches, repeats the stage to check idempotence, and refreshes the remaining-flow worklist. It excludes the notebook's inventory-write and LCA cells.

Verification of the mosaic stage passed: **18 new links**, **290,709 linked biosphere exchanges**, and **3,038 unresolved occurrences across 158 signatures**. All 11,947 datasets and 420,063 exchange rows are retained. Every record matches the declared changes, and repeat application is idempotent. Results are in `reports/generated/biosphere-land-mosaic-migration-check.json`.

The carbon stage adds twelve links, leaving **3,026 unresolved occurrences across 158 signatures**, as recorded in `reports/generated/biosphere-diesel-carbon-migration-check.json`. The subsequent approved uranium/wood conversions add nine links; that stage leaves **3,017 unresolved occurrences across 155 signatures**. The subsequent PM10-metal restoration adds 26 links, leaving **2,991** in the combined check. See `reports/generated/biosphere-uranium-wood-migration-check.json`.
