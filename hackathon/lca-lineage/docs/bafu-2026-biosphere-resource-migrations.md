# BAFU 2026 resource labels and water units

The [resource migration](../schemas/mappings/bafu-2026-biosphere-resources.json) follows the historical catalog step. It has 52 complete name/category/unit rules, covering 3,017 mineral-resource exchanges and 2,782 water-emission exchanges. Full compartments and all source rows are retained.

## Mineral resources

The [official ecoinvent 3.10 change report](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Database/Releases/Change%20Report%20v3.10%20-%2020231214.pdf?hsLang=en), section 2.2.3, p. 18, explicitly explains that old mineral-resource labels containing ore composition describe the amount of the element, not the amount of ore. It directs replacement by the element-only flow names. Consequently, these name corrections use **no concentration multiplier**.

The rules are restricted to kilogram inputs from `natural resource / in ground`. Each source was checked against an exact old master-data entry or an explicit ore-composition label with consistent source and target elemental CAS identifiers. Each resulting target is unique in biosphere 3.10. This does not apply to oxides such as TiO₂, generic rock, resource corrections, or gas volumes.

| Target element | Exchange occurrences |
| --- | ---: |
| Copper | 408 |
| Fluorine | 88 |
| Gold | 718 |
| Lead | 1 |
| Molybdenum | 374 |
| Nickel | 226 |
| Palladium | 190 |
| Phosphorus | 88 |
| Platinum | 190 |
| Rhodium | 190 |
| Silver | 544 |

## Water inventory convention

Eight rules convert `Water` emissions in air/water compartments from kilograms to cubic metres with a multiplier of **0.001**. This uses the target catalog's water inventory convention of 1,000 kg per m³, also used by bw2io's standard water migration. It is not a calculation of vapour volume at local temperature and pressure.

The installed `ecoinvent elementary flows 3.9.xml` contains the unchanged UUIDs for the target water flows and records mass properties of 1,000 per cubic metre; for example, Water / air UUID `075e433b-4be4-448e-9510-9a5029c1ce94`. `bw2io.data.get_biosphere_2_3_name_migration_data` also defines the 0.001 water conversion for air-emission compartments. The migration extends the same catalog convention to the matching water-emission compartments, preserving source compartment detail.

Of the 2,782 affected rows, 2,350 have lognormal uncertainty and 432 have undefined uncertainty (including six zeros). bw2io scales their amounts and uncertainty parameters together. Lognormal scale parameters remain unchanged, while `loc` shifts by ln(0.001); bounds, if present, scale with the amount. Negative quantities retain their sign. No probability distribution is assigned to rows with undefined uncertainty.

## Traceability and limits

`reports/generated/biosphere-resource-evidence.json` records each source signature, replacement, target metadata, reference master-data properties where available, source CAS identifiers, and occurrence count. Raw/repaired XML, original comments, and original CAS metadata remain unchanged.

The notebook applies this file through the existing bw2io migration helper and writes `reports/generated/biosphere-unlinked-after-resources.json`. The catalog-only result is kept at `reports/generated/biosphere-unlinked-after-catalog.json`. Per the user's decision, flows without a supported target remain unresolved; no supplementary biosphere database or placeholder target is created.

## Full-collection verification

In the `bw` environment, this pass linked **5,799 additional exchanges**, leaving **18,808 unlinked occurrences across 585 signatures**, with **274,939 linked biosphere exchanges**. All 11,947 datasets and 420,063 inventory rows remained. An independent complete-record comparison checked declared replacements, water scaling and lognormal uncertainty, unique targets, unchanged non-biosphere records, and idempotence. No inventory database was written. Results are recorded in `reports/generated/biosphere-resource-migration-check.json`.
