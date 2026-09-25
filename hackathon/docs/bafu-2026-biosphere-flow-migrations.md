# BAFU 2026 biosphere flow names and units

This second pass follows the [category migration](bafu-2026-biosphere-migrations.md). It uses [`bafu-2026-biosphere-flows.json`](../schemas/mappings/bafu-2026-biosphere-flows.json), a standard bw2io migration matching the complete `type`, `name`, `categories`, and `unit`. Its 339 explicit rules cover 68 name aliases and two exact unit conversions. Every rule preserves the full compartment and selects exactly one flow in the installed `ecoinvent-3.10-biosphere` database.

## Basis for the name corrections

- **Chemical synonyms and spelling:** explicitly reviewed name pairs, checked against the CAS identifiers in the source exchanges and target biosphere. Leading zero padding in CAS numbers was ignored for comparison. For each mapped source signature with a stated CAS number, it agrees with the target. Missing CAS values remain missing; the rule uses the reviewed name, category, and unit rather than assigning chemicals automatically from a CAS lookup.
- **Biogenic labels:** CO₂, CO, methane, and oils use `non-fossil` in the target. These same aliases are included in bw2io 0.9.17's `data/simapro-biosphere.json`. Their origin distinction is retained.
- **Particulate matter:** `Particulates` becomes `Particulate Matter`; the three particle-size ranges are unchanged.
- **NMVOC:** the unspecified-origin aggregate maps to the target's generic NMVOC aggregate, without assigning fossil or biogenic origin.
- **Redundant unit suffixes:** `/m3` is removed only where the exchange already has unit `cubic meter` and the resulting full signature matches an existing target. This covers specific water and standing-wood labels; it is not a mass-to-volume conversion.

No fuzzy name matching is used. A CAS match alone was not sufficient: proposals involving different oxidation states, isomers, hydration, mixtures, resource grades, land-use detail, or regional water qualifiers were excluded from this pass.

The table below aggregates mappings across the explicitly listed compartments. Counts include isotope aliases that also need Bq-to-kBq conversion. A name appearing here does not authorize mapping it in other compartments or units.

| Source name | Target name | Target CAS where available | Exchange occurrences |
| --- | --- | --- | ---: |
| NMVOC, non-methane volatile organic compounds, unspecified origin | NMVOC, non-methane volatile organic compounds | — | 3,986 |
| Particulates, < 2.5 um | Particulate Matter, < 2.5 um | — | 3,449 |
| Propene | Propylene | 000115-07-1 | 1,652 |
| Ethene | Ethylene | 000074-85-1 | 1,623 |
| Carbon dioxide, biogenic | Carbon dioxide, non-fossil | 000124-38-9 | 1,477 |
| Particulates, > 2.5 um, and < 10um | Particulate Matter, > 2.5 um and < 10um | — | 1,058 |
| Particulates, > 10 um | Particulate Matter, > 10 um | — | 1,049 |
| Ammonium, ion | Ammonium | 014798-03-9 | 840 |
| Benzene, ethyl- | Ethyl benzene | 000100-41-4 | 796 |
| Methane, biogenic | Methane, non-fossil | 000074-82-8 | 734 |
| Ethane, 1,1,1,2-tetrafluoro-, HFC-134a | 1,1,1,2-Tetrafluoroethane | 000811-97-2 | 699 |
| Water, cooling, unspecified natural origin/m3 | Water, cooling, unspecified natural origin | 007732-18-5 | 683 |
| Carbon monoxide, biogenic | Carbon monoxide, non-fossil | 000630-08-0 | 532 |
| Benzene, hexachloro- | Hexachlorobenzene | 000118-74-1 | 506 |
| Water, unspecified natural origin/m3 | Water, unspecified natural origin | 007732-18-5 | 433 |
| Phenol, pentachloro- | Pentachlorophenol | 000087-86-5 | 415 |
| Methane, dichloro-, HCC-30 | Dichloromethane | 000075-09-2 | 390 |
| Ethane, 1,2-dichloro- | Ethylene dichloride | 000107-06-2 | 386 |
| Ethene, chloro- | Vinyl chloride | 000075-01-4 | 363 |
| Ethyne | Acetylene | 000074-86-2 | 337 |
| Methane, trifluoro-, HFC-23 | Trifluoromethane | 000075-46-7 | 319 |
| Hydrogen-3, Tritium | Tritium | 010028-17-8 | 315 |
| Cesium-137 | Caesium-137 | 010045-97-3 | 306 |
| Ethene, tetrachloro- | Tetrachloroethylene | 000127-18-4 | 296 |
| Methane, dichlorodifluoro-, CFC-12 | Dichlorodifluoromethane | 000075-71-8 | 276 |
| 1-Butanol | Butanol | 000071-36-3 | 250 |
| Oils, biogenic | Oils, non-fossil | — | 246 |
| 2-Propanol | Isopropanol | 000067-63-0 | 242 |
| 2-Methyl-1-propanol | Isobutanol | 000078-83-1 | 235 |
| Benzene, 1,2-dichloro- | o-Dichlorobenzene | 000095-50-1 | 226 |
| 1-Propanol | Propanol | 000071-23-8 | 215 |
| Cesium-134 | Caesium-134 | 013967-70-9 | 214 |
| Methane, monochloro-, R-40 | Methylchloride | 000074-87-3 | 197 |
| Ethane, 1,1,1-trichloro-, HCFC-140 | 1,1,1-Trichloroethane | 000071-55-6 | 195 |
| Methane, chlorodifluoro-, HCFC-22 | Chlorodifluoromethane | 000075-45-6 | 195 |
| Methane, tetrachloro-, CFC-10 | Carbon tetrachloride | 000056-23-5 | 195 |
| Ethane, hexafluoro-, HFC-116 | Hexafluoroethane | 000076-16-4 | 193 |
| Methane, tetrafluoro-, CFC-14 | Tetrafluoromethane | 000075-73-0 | 191 |
| 2-Butene, 2-methyl- | 2-Methyl-2-butene | 000513-35-9 | 189 |
| Benzene, pentachloro- | Pentachlorobenzene | 000608-93-5 | 165 |
| Ethane, 1,1,2-trichloro-1,2,2-trifluoro-, CFC-113 | 1,1,2-Trichloro-1,2,2-trifluoroethane | 000076-13-1 | 160 |
| Ethane, 1,1-difluoro-, HFC-152a | 1,1-Difluoroethane | 000075-37-6 | 156 |
| Wood, unspecified, standing/m3 | Wood, unspecified, standing | — | 134 |
| Benzene, chloro- | Monochlorobenzene | 000108-90-7 | 106 |
| Benzene, 1-methyl-2-nitro- | o-Nitrotoluene | 000088-72-2 | 102 |
| Ethane, 1,2-dichloro-1,1,2,2-tetrafluoro-, CFC-114 | 1,2-Dichloro-1,1,2,2-tetrafluoroethane | 000076-14-2 | 102 |
| Methane, dichlorofluoro-, HCFC-21 | Dichlorofluoromethane | 000075-43-4 | 101 |
| Methane, trichlorofluoro-, CFC-11 | Trichlorofluoromethane | 000075-69-4 | 98 |
| Ethane, 2-chloro-1,1,1,2-tetrafluoro-, HCFC-124 | 2-Chloro-1,1,1,2-tetrafluoroethane | 002837-89-0 | 74 |
| Chlortoluron | Chlorotoluron | 015545-48-9 | 65 |
| 2-Methyl-4-chlorophenoxyacetic acid | MCPA | 000094-74-6 | 61 |
| Ethane, pentafluoro-, HFC-125 | Pentafluoroethane | 000354-33-6 | 60 |
| Methane, difluoro-, HFC-32 | Difluoromethane | 000075-10-5 | 59 |
| Dimethenamid | Dimethenamide | 087674-68-8 | 58 |
| Dithianone | Dithianon | 003347-22-6 | 56 |
| Oxydemeton methyl | Oxydemeton-methyl | 000301-12-2 | 56 |
| Tebupirimphos | Tebupirimfos | 096182-53-5 | 55 |
| Monosodium acid methanearsonate | MSMA | 002163-80-6 | 4 |
| Ethanol, 2-ethoxy- | Ethylene glycol monoethyl ether | 000110-80-5 | 2 |
| Fosetyl-aluminium | Fosetyl-Al | 039148-24-8 | 2 |
| Methane, chlorotrifluoro-, CFC-13 | Chlorotrifluoromethane | 000075-72-9 | 2 |
| N-(2,3-dichloro-4-hydroxyphenyl)-1-methylcyclohexane-1-carboxamide | Fenhexamid | 126833-17-8 | 2 |
| Dipropylthiocarbamic acid S-ethyl ester | EPTC | 000759-94-4 | 1 |
| Pentane, 2-methyl- | Isohexane | 000107-83-5 | 1 |
| Pentane, perfluoro- | Perfluoropentane | 000678-26-2 | 1 |
| Prohexadione-calcium | Prohexadione calcium | 127277-53-6 | 1 |
| Quizalofop ethyl ester | Quizalofop-ethyl | 76578-14-8 | 1 |
| Water/m3 | Water | 007732-18-5 | 1 |

## Exact unit conversions

| Source unit | Target unit | Amount multiplier | Exchange occurrences |
| --- | --- | ---: | ---: |
| Becquerel | kilo Becquerel | 0.001 | 3,131 |
| kilowatt hour, for `Heat, waste` to air | megajoule | 3.6 | 3 |

These conversions preserve physical quantities: 1,000 Bq = 1 kBq, and 1 kWh = 3.6 MJ. The migration changes the numerical amount together with its unit. bw2io's `multiplier` mechanism calls `rescale_exchange`, which also adjusts uncertainty parameters as appropriate. All 3,134 converted rows in this collection have `uncertainty type: 0` (undefined uncertainty); their `amount` and `loc` are scaled consistently. The original zero uncertainty type is retained. No uncertainty distribution is invented.

All other numerical values and uncertainty parameters remain unchanged. No change is made to biosphere categories, source CAS metadata, comments, technosphere exchanges, production exchanges, or raw/repaired XML.

## Workflow and reports

The [notebook](../scripts/import_fixed_ecospold.ipynb) calls `apply_biosphere_flow_migration` from the existing [biosphere helper](../scripts/ecospold%20importer/biosphere_migrations.py) after category normalization. The helper uses `bw2io.Migration`, `importer.migrate`, and `importer.match_database`; it requires unique targets, rejects duplicate rules or unit changes without multipliers, and keeps existing links consistent.

Rerun extraction and all migration cells after changing the JSON. The unit is part of each source signature, so reapplying a completed migration does not convert it again.

- `reports/generated/biosphere-unlinked-after-categories.json`: category-only intermediate result.
- `reports/generated/biosphere-unlinked-after-flows.json`: intermediate result after this name/unit pass; subsequent stages write the final `biosphere-unlinked.json`.
- `reports/generated/biosphere-flow-mapping-evidence.json`: every source signature, replacement, target UUID/CAS, stated source CAS values, occurrence count, and example source files used for this mapping review.
- `reports/generated/biosphere-flow-migration-check.json`: full-collection verification and conversion counts.

## Scope of this pass

| Change | Migration rules | Exchange occurrences |
| --- | ---: | ---: |
| Name only | 189 | 27,429 |
| Unit only | 142 | 2,974 |
| Name and unit | 8 | 160 |

Groups left unresolved by this pass include historical metal labels, water mass/volume conversions and regional water labels, detailed land/resource descriptions, and unsupported compartments or noise indicators. Subsequent [catalog](bafu-2026-biosphere-catalog-migrations.md), [resource](bafu-2026-biosphere-resource-migrations.md), and [reviewed](bafu-2026-biosphere-reviewed-migrations.md) passes document which could be resolved using further evidence or approved assumptions. No unresolved exchanges are dropped by either biosphere helper, and neither helper writes an inventory database.

## Full-collection verification

Executed the notebook in a fresh `bw` process through the new flow migration, with all preceding extraction and migration cells. The later cells that drop exchanges, write the database, and calculate LCA were not executed.

- **30,563 additional biosphere exchanges linked**, reducing the remaining count from 123,488 to **92,925**, across **1,003 signatures**.
- **200,822 of 293,747 biosphere exchanges now link** after both passes.
- All **11,947 datasets and 420,063 exchange rows** were retained; zero unlinked technosphere exchanges remain.
- An independent complete-record comparison allowed only the declared name/unit changes, exact numerical scaling, and new links to unique targets. All other fields, existing links, and non-biosphere exchanges were preserved.
- All 339 rules were exercised. Reapplying the flow migration produced identical records, confirming that the 3,134 converted rows cannot be scaled twice by these rules.

The remaining exchanges are still included in the importer. These results establish linking and transformation consistency, not complete inventory validity or LCIA readiness.
