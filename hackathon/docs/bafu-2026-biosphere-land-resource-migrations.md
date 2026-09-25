# BAFU 2026 land and resource mappings

The [land/resource migration](../schemas/mappings/bafu-2026-biosphere-land-resources.json) adds 18 complete-signature rules after the gas-unit stage. Every affected exchange retains its incoming name, categories, and unit in `bafu original biosphere`; regional water also retains `region: Europe`. All amounts, units, uncertainty parameters, CAS metadata, and comments stay unchanged.

| Source class or resource | Target | Occurrences | Basis |
| --- | --- | ---: | --- |
| Industrial area, benthos | Seabed, infrastructure | 274 | Documented historical name change; includes occupation and both transformation directions |
| Annual crop, non-irrigated, diverse-intensive | Annual crop, non-irrigated, extensive | 72 | Documented historical name change |
| Annual crop, non-irrigated, fallow | Cropland fallow (non-use) | 88 | Documented historical name change |
| Tropical rain forest | Forest, extensive | 103 | User-approved broader class, also present in the historical correspondence |
| Organic annual crop / arable land | Annual crop | 272 | User-approved broader class without assigning irrigation or intensity |
| Organic pasture / pasture and meadow | Pasture, man made | 7 | User-approved broader class without assigning intensity |
| Metamorphous rock, graphite containing | Graphite | 89 | Explicit ecoinvent 3.9 rename and unchanged historical UUID |
| Peat, resource / in ground | Peat, resource / biotic | 1 | Official peat resource compartment |
| Water, unspecified, Europe | Water, unspecified natural origin | 3 | Approved regional-water approach; source origin remains unspecified |
| Helium | Helium, in natural gas | 1 | The source dataset explicitly identifies extraction from natural gas |

## Historical land correspondence

The [ecoinvent 2.2 → 3.0 change report](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Database/Releases/report_of_changes_ecoinvent_2.2_to_3.0_20130904.pdf), section 8.2 and Table 8.1 (printed p. 38), explicitly documents the benthos, crop, fallow, and forest correspondences above. BAFU's two crop labels already replace the old word `arable` with `annual crop`, while retaining the old qualifiers. The rules complete those historical renames. They do not infer present-day farming intensity from the word “diverse.”

The report's correspondences describe historical ecoinvent usage, not universal relationships between land types. Rules are restricted to the enumerated BAFU source signatures. The benthos mapping retains an aquatic setting. An older correspondence workbook bundled with bw2io suggests ordinary industrial area but lacks a destination UUID for this label; the published report and existing seabed targets provide the more specific supported correspondence.

For rainforest and organic agriculture, the user explicitly approved using the broader classes and retaining original labels. Their LCIA factors do not automatically account for the retained tropical/organic distinctions. Occupation remains occupation; transformation direction remains unchanged. All land rules retain `natural resource / land` and their original area or area-time unit.

## Other resources

The [ecoinvent 3.9 change report](https://support.ecoinvent.org/hubfs/Change-Report-v3.9.pdf), printed p. 16, explicitly renames the old graphite-containing-rock flow to `Graphite`. Its historical correspondence UUID, `5666353e-2db2-41d3-8414-404709151422`, matches the installed 3.9 and 3.10 catalogs. This resolves the previous uncertainty about whether an ore-grade conversion was needed: this rule follows the catalog rename, with no invented grade factor. The source has no CAS value; none is added to the exchange.

The correspondence workbook `ecoinvent elementary flows 2-3.xlsx` and official 3.9 master data bundled with bw2io classify peat UUID `c5035ce2-5ee5-431f-a287-4b25da42be74` under `natural resource / biotic`, in kilograms. The single incoming `in ground` category is corrected to that definition, with its original category retained. This does not convert energy quantities or change fossil-carbon accounting.

The three European water withdrawals retain their full resource compartment and cubic-metre unit. The target does not assign a river, lake, groundwater, or other specific origin.

The sole helium-resource exchange belongs to `process_30d17e0e-4d9a-36fc-92a8-10ec495219ac.xml` (helium gas production). Its general and technology comments explicitly describe extraction from natural gas. The source and target CAS identify helium, and the category/unit agree. This supports the more specific target for this reviewed source; it is not inferred solely from its CAS.

## Verification

The notebook reads this mapping after the gas stage and requires one target per full target signature. Local rule evidence, UUIDs, counts, and example source files are recorded in `reports/generated/biosphere-land-resource-evidence.json`. The full-collection check is `biosphere-land-resource-migration-check.json`. The preceding unresolved report is `biosphere-unlinked-after-gas-units.json`; this stage writes `biosphere-unlinked-after-land-resources.json`.

The full `bw` check resolved **910 additional occurrences**, yielding **288,984 linked biosphere exchanges** and **4,763 unresolved across 220 signatures**. All 11,947 datasets and 420,063 exchange rows remained. Independent complete-record comparison verified the declared name/category/metadata changes and unique links, with every amount and uncertainty field unchanged. Non-biosphere records and links were unchanged, reapplication was idempotent, and no inventory database was written.
