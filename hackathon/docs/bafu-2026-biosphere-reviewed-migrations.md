# BAFU 2026 additional reviewed biosphere mappings

The [reviewed migration](../schemas/mappings/bafu-2026-biosphere-reviewed.json) follows the historical catalog and resource/unit passes. Its 308 explicit rules address 11,186 exchange occurrences. Each source includes the full type, name, categories, and unit; every destination must exist uniquely in biosphere 3.10.

## Regional water: approved aggregation

The user approved mapping **4,961 regional water emissions** to generic `Water`, while retaining their original region. The user then approved **2,298 regional withdrawals** to their corresponding generic targets: 2,065 unspecified-origin water, 197 cooling water, 17 lake water, and 19 river water. Withdrawal type, compartment, and cubic-metre unit are retained. These have an existing target in the same complete air or water compartment. The 54 regional water emissions in the unsupported `water / fossilwater` compartment remain unresolved.

Each mapped exchange receives `bafu original biosphere` metadata containing its original name, categories, unit, and region. This metadata survives in the importer's exchange record and can be stored with a later database import. It is also present in the migration and evidence report. The region is not assigned to the consuming activity: the flow's region can differ from that activity's location.

**Generic LCIA factors do not automatically use the retained region.** This is an explicitly approved aggregation for linking, not a claim that regional water impacts are interchangeable. Future regional characterization must use the saved metadata or revisit the target mapping.

Of the regional emission exchanges, 2,358 use kilograms and are converted to cubic metres with the documented water inventory factor 0.001. The others already use cubic metres. bw2io scales amounts and uncertainty together; the converted rows comprise 188 nonzero lognormal exchanges and 2,170 exchanges with undefined uncertainty, including six zeros. Compartments remain unchanged.

## Broader land classes: approved aggregation

The user approved 18 rules covering **1,959 land-use exchanges**: 1,333 industrial-area occurrences with built-up or vegetation qualifiers, and 626 intensive-forest occurrences with normal, short-cycle, or clear-cutting qualifiers. They map to the corresponding broader industrial-area or intensive-forest class, retaining occupation versus transformation and transformation direction.

Every affected exchange retains its original name, categories, and unit in `bafu original biosphere`. Eighty occurrences also lack the resource subcategory, which is restored to `land`. Amounts and uncertainty are unchanged. These metadata are captured immediately before this reviewed migration, after the earlier category/unit normalization; the raw XML preserves the original source representation.

LCIA uses the broader class's factors. Retaining the original detail supports later refinement but does not make those generic factors specific to vegetation, built-up area, or forest-management practice. This approval excludes industrial benthos, tropical rainforest, organic arable land, and other classifications not enumerated in the 18 rules.

## Supported names and missing resource subcategories

- **1,254 chemical-name occurrences:** reviewed punctuation variants of names or synonyms in the official ecoinvent 3.9 master data, retaining the current target UUID, complete compartment, and unit. These include the old dioxin spelling, o-chlorotoluene, 2,4-dichlorophenol, monochloroethane, quintozene, arsenic ion, two aromatic compounds, and nitric oxide. The dioxin rule follows the explicit catalog synonym `dioxin, 2,3,7,8-tetrachlorodibenzo-p-`; no new toxic-equivalency calculation is inferred from an arbitrary CAS match. The catalog's Metiram → Zineb synonym is still excluded because it identifies different chemicals.
- **107 Metaldehyde (tetramer) occurrences:** source and target CAS 108-62-3 agree. The [NIST Chemistry WebBook](https://webbook.nist.gov/cgi/cbook.cgi?ID=108-62-3) identifies metaldehyde as acetaldehyde tetramer. The parenthetical qualifier does not require multiplying or dividing the inventory amount by four.
- **280 bulk mineral occurrences:** unqualified `Sand` and `Clay` map to `Sand, unspecified` and `Clay, unspecified`. No grade, composition, or specific clay mineral is inferred.
- **326 missing resource subcategories:** explicit land occupation/transformation flows receive `land`; `Carbon dioxide, in air` receives `in air`; biomass calorific energy receives `biotic`; uranium, shale, iridium, and platinum receive `in ground`. Names and units remain exact. These are enumerated flow definitions, not a general fallback that assigns any missing compartment to the only available target.
- **One zinc occurrence:** another explicit ore-composition label maps to elemental `Zinc`, following the [ecoinvent 3.10 change report](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Database/Releases/Change%20Report%20v3.10%20-%2020231214.pdf?hsLang=en), p. 18. Its kilogram amount already represents the element; no ore-grade multiplier applies.

The chlorotoluene and dichlorophenol identities are also independently supported by the [NIST chlorotoluene record](https://webbook.nist.gov/cgi/cbook.cgi?ID=95-49-8) and [NIST dichlorophenol record](https://webbook.nist.gov/cgi/cbook.cgi?ID=120-83-2).

## Evidence and limits

`reports/generated/biosphere-reviewed-evidence.json` records each source, replacement, occurrence count, source CAS values, example files, target UUID/CAS, and available historical master-data synonyms. The preceding result is `reports/generated/biosphere-unlinked-after-resources.json`; this stage's unresolved result is `reports/generated/biosphere-unlinked-after-reviewed.json`.

The helper checks that retained regional-water metadata agrees with its source signature. This stage fills enumerated missing resource subcategories. Later water/context rules can correct stated subcategories within the same main class only when the original source metadata is retained; resource/emission transfers are rejected. All original comments and CAS metadata are retained. Raw and repaired XML are unchanged.

Per the user's decision, genuinely missing flows remain unresolved pending a supported target. No new biosphere database or placeholder flows are created. The migration helpers do not drop exchanges or write the inventory database. A notebook guard stops Run All before the existing drop/write/LCA cells while any exchange remains unlinked; those later cells are outside this validation workflow.

## Full-collection verification

The notebook was executed in a fresh `bw` process through this migration, including every preceding migration. It linked **11,186 additional exchanges**, producing **286,125 linked biosphere exchanges** and **7,622 unresolved occurrences across 277 signatures**. All 11,947 datasets and 420,063 inventory rows remained, with zero unlinked technosphere exchanges.

An independent complete-record comparison checked every declared replacement, the 2,358 water conversions and their uncertainty parameters, unique target links, and unchanged non-biosphere records. All 7,259 approved water exchanges retain their original regional metadata, and all 1,959 approved land exchanges retain their original detailed classifications. Reapplying the migration produced identical records. No inventory database was written. The local result is `reports/generated/biosphere-reviewed-migration-check.json`.
