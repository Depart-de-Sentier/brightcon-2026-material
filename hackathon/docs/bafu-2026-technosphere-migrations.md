# BAFU 2026 technosphere migration evidence

The initial EcoSpold 1 import had 24 distinct unmatched technosphere signatures, occurring in 1,466 exchange rows. The first five ENTSO-E rules resolved 1,412 rows. This document records the evidence and assumptions used to address the remaining 19 signatures and 54 rows.

The migrations act on the extracted Brightway data. They leave the raw and repaired XML files unchanged. Source amounts and uncertainty parameters are preserved; the current rules contain no multipliers. They do change selected supplier labels, locations, and units, including the documented substitutions below. Successful linking does not establish that a proxy has the same environmental profile as the missing supplier.

## Natural-gas volume labels: 14 signatures, 40 rows

The consuming exchanges use `m3` (normalized by bw2io to `cubic meter`). Each has exactly one supplier with the same name, categories, and geography using `Nm3` (`normal cubic meter`). These 14 exact exchange signatures are relabeled 1:1; amounts and uncertainty are unchanged.

**User decision:** use a documented 1:1 relabeling and preserve amounts. This is a compatibility assumption, not a calculated temperature/pressure conversion. The 2007 natural-gas report's glossary (PDF page 7) treats gas volumes expressed as m³ as normal cubic metres. The 2025 extraction report, PDF page 29 / printed page 21, explicitly retains the label Nm³ for values at 15°C and 1013 mbar, which it identifies as Sm³. The migration does not claim all old and new inventories use identical physical reference conditions.

| Supplier name | Location | Exchange rows |
| --- | --- | ---: |
| Natural gas, at production | NG | 2 |
| Natural gas, at production | QA | 2 |
| Natural gas, at production | DZ | 5 |
| Natural gas, at production | US | 2 |
| Natural gas, at production offshore | NO | 4 |
| Natural gas, at production offshore | NL | 5 |
| Natural gas, at production offshore | GB | 1 |
| Natural gas, at production onshore | DE | 5 |
| Natural gas, at production onshore | RU | 4 |
| Natural gas, at production onshore | NL | 2 |
| Natural gas, liquefied, production DZ, at freight ship | FR | 3 |
| Natural gas, production DZ, at long-distance pipeline | RER | 1 |
| Natural gas, production NG, at long-distance pipeline | RER | 1 |
| Natural gas, production RU, at long-distance pipeline | RER | 3 |

Reports are stored under `data/raw/BAFU-2026 v1 LCI Reports/`: `2007 - Natural gas - Faist-Emmeneger.pdf` and `2025 - LCI crude oil and natural gas extraction - Meili.pdf`. The supplier for LNG delivered to France (`process_3df8f8b8-b7c9-304e-be75-bd3b5356bb11.xml`) also explicitly states that its inventory is normalized to gaseous gas, with 36.0 MJ/Nm³.

## Finnish gas-fired electricity: one signature, one row

Consumer `process_3e049476-cbde-34dd-8779-bfcd53819834.xml` requests `Electricity, natural gas, at power plant`, FI, in kWh. The uniquely matching supplier is `process_c1f04203-96ec-320c-85f5-e56aaa86729b.xml`, whose dataset and production exchange are labeled MJ.

The supplier describes an approximately 25.6% electrical efficiency and consumes 14.07 MJ of `Natural gas, burned in power plant or heat plant` per unit of output. Thus 14.07 × 0.256 = 3.60192 MJ, approximately 1 kWh. The output is inferred to be mislabeled. Two narrowly matched rules change the supplier dataset's and its production exchange's unit from `megajoule` to `kilowatt hour`. Every numerical value, including the consumer's 0.0156738333179065 kWh input, is retained.

Dataset codes remain stable so existing Brightway input references remain valid. The supplier's unit labels change after extraction; its XML is unchanged. The source cited in both files is `2025 - Update LCI electricity from natural gas - Zschokke`.

## Direct-air-capture infrastructure: one signature, one row

Consumer `process_bf3edfd6-d2bc-3885-8acb-5c718d43ae2d.xml` requests the 100 kt CO₂/year sorbent-based infrastructure in CH. Supplier `process_7484b270-e065-46c4-9759-89c4d046dc52.xml` has the same name, categories, unit, and original exchange number 208310, but its geography is RER. Both descriptions refer to the Climeworks/Deutz and Bardow sorbent design, a capacity of 100 kt/year, and a 20-year lifetime.

The mapping links the Swiss capture process to that European infrastructure supplier by changing the exchange location to RER. This is an inferred intended supplier based on the combined identifiers and technology description; it does not change the consuming process's CH location or the infrastructure amount of 5e-10 units.

## Wind electricity: one signature, one row

In `process_729a0dd2-5a2b-3b5e-8960-df2240b7629f.xml`, the exchange name specifies a 100 MW **onshore** farm with 2.3 MW turbines, the location is OCE, and the comment says `Wind Offshore / DE`. The source contains conflicting technology metadata.

**User decision:** preserve the onshore name and change only the location to RER. It links to `process_79a7b7d6-d0eb-48f2-bae7-da98facdae0f.xml`. The original amount, uncertainty, and contradictory offshore comment remain unchanged. This documented choice resolves linking, not the underlying onshore/offshore inconsistency.

## Concrete disposal: one signature, one row

The offshore-platform dataset `process_adb3bfb7-7eb5-31ca-b34d-fad5194d0c92.xml` requests CH disposal of concrete containing 5% water to an inert material landfill. The exact-name GLO supplier (`process_09984ab6-a49a-46a6-801a-ddcbc3b881bc.xml`) contains only a production exchange and no treatment inventory.

**User decision:** use the populated CH dataset `Disposal, concrete, 5% water, to construction waste landfill` (`process_19c2ddb6-68b0-4d8a-97e0-a8aa9a4d8ca0.xml`) as a documented proxy. Its description explicitly recommends it for concrete waste going to landfill and specifies 5% water. The mapping changes the name and categories to that supplier; CH, kilograms, the amount of 1,351,400 kg, and uncertainty remain unchanged. Landfill infrastructure and emissions are now represented through the selected proxy.

## Electricity production mixes without location: one signature, ten rows

These exchanges have identical matching fields, including an empty location, but occur in different consuming datasets. They therefore use a second standard bw2io migration file whose fields also include the source XML filename. The helper supplies this field temporarily and removes it after applying the migration.

| Consuming XML file | Interpretation | Supplier location |
| --- | --- | --- |
| `process_4543c411-9d71-31fa-bdc0-19cfba9b0863.xml` | Swedish metals refinery | SE |
| `process_5f686814-2c54-3909-892a-a03e25e211e5.xml` | Swedish metals refinery | SE |
| `process_8bae4793-9741-3fc4-ba34-c3458ab8e372.xml` | Swedish metals refinery | SE |
| `process_974cc78c-46b9-391e-b253-14555c9c488a.xml` | Swedish metals converter | SE |
| `process_ceb8aefd-b53f-3d2a-a5e2-57dd8e57af7d.xml` | Swedish secondary-lead plant | SE |
| `process_b5cd8fc8-fb6e-3a58-b36d-7a2a6bf90773.xml` | Global mischmetal process explicitly approximates electricity with European data | RER |
| `process_b38528d2-cb70-3658-8404-120f40105b30.xml` | Dataset name identifies ENTSO electricity imports | ENTSO-E |
| `process_10004d2b-e7b0-3584-b73f-69a240182122.xml` | Indian bast-fibre yarn production; user-approved grid-mix proxy | IN |
| `process_3208d237-7666-3858-a8fb-ae8a951bcc92.xml` | Indian bast-fibre weaving; user-approved grid-mix proxy | IN |
| `process_c386d9c0-b050-3c17-a4a3-7f603b6e5d7c.xml` | Unidentified import component in the Swiss BFE 2005 consumer mix; user-approved European proxy | RER |

The five SE choices are derived from the Swedish consuming-plant geography. The RER choice follows the explicit European approximation in the consuming dataset's geography description. The ENTSO-E choice follows the import dataset's name. These are documented geographic derivations, not recovered exchange-level country codes. All target name/category/unit/location combinations identify exactly one available supplier.

**User decision:** use IN for the two Indian textile exchanges and RER for the unidentified Swiss import component as documented proxies, preserving their `Electricity, production mix` names. The Indian comments mention diesel generation; an Indian grid mix does not reproduce that technology. Their amounts remain 2.7278000000000002 and 0.74444 kWh. The Swiss description gives several possible import origins without assigning one to the 0.20709 kWh exchange. Its RER mapping is a regional approximation, not a recovered source location. All original comments and numerical values are retained.

The selected production-mix suppliers are `process_ac4949f6-1e94-3f9f-a692-540f1a788a91.xml` (SE), `process_9810926e-492f-30d9-9e88-29a4afff3bb6.xml` (RER), `process_290844ec-8f4e-45b2-b4f8-845a777e83a7.xml` (ENTSO-E), and `process_9eab59b7-6fc4-3c7b-acd4-72be64861840.xml` (IN).

## Full-collection verification

The notebook's setup, extraction, default strategies, and migration cells were executed in a fresh Python process using the `bw` environment. The import contained 11,947 datasets and 420,063 exchanges before and after migration. All 114,369 technosphere exchanges now link: the original 24 unmatched signatures / 1,466 occurrences are resolved, including the final 19 signatures / 54 occurrences covered here.

Each newly linked exchange was checked against exactly one supplier. A complete record comparison allowed only the declared name/category/unit/location changes and new `input` links; all amounts, uncertainty parameters, comments, dataset codes, and existing links were preserved. Every migration rule was exercised, and no temporary filename markers remained. The machine-readable report records migration-file hashes, rule occurrence counts, and all newly linked consumer/supplier pairs in `reports/generated/technosphere-migration-check.json`.

The later notebook cells that drop exchanges, write the database, and calculate LCA were not run during this check. Biosphere linking is a separate task; all 293,747 biosphere exchanges are still unlinked at the tested migration stage. Successful technosphere linking alone does not establish a complete or validated LCA model.
