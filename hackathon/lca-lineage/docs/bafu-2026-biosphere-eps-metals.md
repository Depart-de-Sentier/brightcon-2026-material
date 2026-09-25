# Restore two EPS metal emissions

The [EPS metal migration](../schemas/mappings/bafu-2026-biosphere-eps-metals.json) corrects two rows labelled `Particulates, < 10 um` in `process_05a10e4b-a919-33b6-b017-7c0bf7f7a7f9.xml`, **Polystyrene, expandable, at plant / RER**. The original inventory identifies them as palladium and rhodium emissions to unspecified air. A third, genuine PM10 row in the same file remains unchanged and unresolved.

## Source evidence

The [original PlasticsEurope EPS inventory, version 09.00.000](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=b60b30bf-991d-41b8-a295-5d0b2e5f2bb5&version=09.00.000) and its referenced flow records establish the identities and mass basis:

| Source exchange | Original identity | Original quantity (kg) | BAFU quantity (kg) | Original flow UUID |
| --- | --- | ---: | ---: | --- |
| 396 | Palladium, unspecified air | 8.19273020521738 × 10⁻¹⁷ | 8.1927 × 10⁻¹⁷ | `08a91e70-3ddc-11dd-a056-0050c2490048` |
| 438 | Rhodium, unspecified air | 7.90871446373845 × 10⁻¹⁷ | 7.9087 × 10⁻¹⁷ | `fe0acd60-3ddc-11dd-abb5-0050c2490048` |

The [palladium flow](https://plasticseurope.lca-data.com/resource/flows/08a91e70-3ddc-11dd-a056-0050c2490048?format=xml&version=03.00.000) has CAS 7440-05-3; the [rhodium flow](https://plasticseurope.lca-data.com/resource/flows/fe0acd60-3ddc-11dd-abb5-0050c2490048?format=xml&version=03.00.000) has CAS 7440-16-6. Both use Mass as the reference property.

Source order and neighbouring quantities support these identifications independently of amount alone. Palladium follows oxygen and precedes para-cresol and coarse particles. Rhodium follows radium-228 and radon-222 and precedes the two ruthenium-106 rows. The BAFU sequence and quantities agree within rounding precision. The genuine PM10 row instead matches original exchange 401, at 2.93783289618035 × 10⁻⁷ kg, rounded to 2.9378 × 10⁻⁷ kg in BAFU.

## Historical catalog correspondence

The installed bw2io `ecoinvent 35 new biosphere.json` records these generic-air flows as **Palladium** and **Rhodium**. Their exact UUIDs persist in the official 3.9 elementary-flow catalog and the installed biosphere 3.10 database under the names below. The current official synonyms still include the generic metal names.

| Historical name | Current target | Target UUID |
| --- | --- | --- |
| Palladium | Palladium II / air / kilogram | `51377cff-3c04-5717-8961-6819901a3e90` |
| Rhodium | Rhodium III / air / kilogram | `7c651713-83f5-56e1-a67f-37b828684f3d` |

This follows catalog continuity for the source's generic metal emissions. It does not establish measured oxidation states. Current target CAS identifiers are ionic and differ from the original elemental identifiers; the original missing BAFU CAS fields are left unchanged. No chemical mass conversion is made.

## Exact selection and retained data

All three PM10-labelled BAFU rows share the same name, categories, unit, CAS, filename and exchange code. The two rules therefore also select the **exact original BAFU quantity**, represented as canonical float text in temporary `_migration_source_amount`. There is no tolerance-based selection. A nearby quantity or a quantity in another file cannot match; duplicate exact source matches raise an error before migration.

The helper supplies the amount and filename markers, delegates the replacements to bw2io `importer.migrate`, and removes both markers even if migration fails. It checks unique target signatures and rejects already-linked source rows. Reapplication is idempotent.

Only the name, `bafu original biosphere` metadata and input link change. Amount, uncertainty, original comments, missing CAS and generic-air compartment are retained. The mapping file and evidence identify each reviewed source row; the unchanged quantity remains on the exchange.

## Verification

At this stage, the full `bw` check passed: **two new links**, **290,571 linked of 293,747 biosphere exchanges**, and **3,176 unresolved occurrences across 171 signatures**. All 11,947 datasets and 420,063 exchange rows remain; all technosphere exchanges link. Independent complete-record comparison verified the two target UUIDs, every retained numeric field, the genuine PM10 row, unchanged unrelated records, repeat application, and audit consistency. The 22 biosphere regression tests also pass. No inventory database was written. Results are recorded in `reports/generated/biosphere-eps-metals-migration-check.json`. Source XML, catalog records, neighbouring rows and hashes are recorded in `reports/generated/biosphere-eps-metals-evidence.json`.

This stage follows the four-rule plastics source review. It writes `biosphere-unlinked-after-eps-metals.json`; the preceding stage writes `biosphere-unlinked-after-plastics-source-review.json`. The notebook's optional drop/write/LCA cells are excluded from verification.
