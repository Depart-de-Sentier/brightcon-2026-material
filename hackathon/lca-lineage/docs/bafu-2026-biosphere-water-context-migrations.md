# BAFU 2026 water names and resource contexts

The [water/context migration](../schemas/mappings/bafu-2026-biosphere-water-context.json) follows the reviewed names and approved aggregations. Its 26 explicit rules resolve 1,045 occurrences. Every changed exchange retains its incoming name, complete categories, and unit in `bafu original biosphere`, plus its region where stated. These are values after the earlier normalization stages; raw XML remains unchanged.

| Correction | Occurrences | Basis |
| --- | ---: | --- |
| Well-water resources → `Water, well, in ground / natural resource / in water` | 276 | Groundwater identity and explicit historical correspondence; includes 22 regional occurrences and 10 with missing resource subcategory |
| Fossil-water resources → `Water, unspecified natural origin / natural resource / fossil well` | 138 | The source explicitly states fossil water; the target retains that distinction in its compartment |
| `Water, OECD` and `Water, Europe` emissions → generic `Water` | 149 | The approved regional-water approach, extended to two labels missed by the earlier short-region-code filter |
| Unspecified-origin process-water withdrawals and redundant `/m3` labels | 336 | General water-resource classification; a stated `in ground` category is retained |
| Mineral, energy, air-source, or land-resource subcategories | 92 | Names explicitly identify the resource class, while the incoming subcategory conflicts with that definition |
| `Water, NO / water / fossilwater` → `Water / water / fossil well` | 54 | Supported compartment correspondence plus the approved regional aggregation; fossil-water status is retained |

## Evidence and interpretation

The [Brightway SimaPro–ecoinvent correspondence](https://github.com/brightway-lca/simapro_ecoinvent_elementary_flows/blob/main/Mapping/Output/Mapped_files/SimaProv94-ecoinventEFv3.7.csv) explicitly maps `Water, well` to `Water, well, in ground` with factor 1 and UUID `67c40aae-d403-464d-9649-c12695e43ad8`. The same UUID exists in the installed biosphere 3.10. The BAFU reference report `2009 - LCI metals - Classen.pdf` also identifies groundwater use with this elementary-flow name. [USGS well definitions](https://www.usgs.gov/water-science-school/science/groundwater-wells) independently support that interpretation.

The [ecoinvent 3.1 change report](https://19913970.fs1.hubspotusercontent-na1.net/hubfs/19913970/Knowledge%20Base/Database/Releases/20140630_report_of_changes_ecoinvent_3.01_to_3.1.pdf), p. 10, classifies well water and unspecified-origin water as `natural resource / in water`. This compartment is a general water-resource class, not an assertion that the source is a river or lake. For the 336 unspecified-origin withdrawals, process-purpose wording remains in the retained source metadata, and the 60 explicitly `in ground` occurrences keep that category. Missing or erroneous `land` categories use the general water-resource definition.

The 138 explicit fossil-water resources use the existing fossil-well resource UUID `2caa889e-8187-459d-963a-fa47a79c5378`. This moves the stated fossil distinction from the name into the target compartment, preserving it rather than treating the source as ordinary renewable groundwater.

Brightway's [context correspondence](https://github.com/brightway-lca/simapro_ecoinvent_elementary_flows#context-mapping) maps water-emission `fossilwater` to `fossil well`. The actual target Water UUID `2256a142-8242-4b4f-b9aa-a167803989ca` exists. Earlier review notes treated the 54 Norwegian water emissions as unsupported; this new evidence establishes a target without removing the fossil-water distinction. The other 75 `Suspended solids, unspecified / water / fossilwater` occurrences still lack a target and remain unresolved.

The 92 resource-class corrections comprise uranium (63), basalt (2), platinum (1), geothermal energy (5), biomass calorific energy (7), explicitly atmospheric CO₂ uptake (8), and industrial land occupation/transformation (6). These preserve each exact flow name and unit and require a unique target in the corresponding ground, biotic, air, or land resource class. They do not move emissions into resources or vice versa.

## Amounts and traceability

337 water exchanges convert from kilograms to cubic metres with factor 0.001, following the already documented catalog water convention. All other amounts remain unchanged. bw2io rescales amount and uncertainty together. Region metadata remains explicit for 225 occurrences; it does not automatically regionalize their LCIA factors.

The helper requires original metadata when changing a stated subcategory and rejects changes between main classes such as resource, air emission, or water emission. Target uniqueness and complete-signature matching remain mandatory. This file is an enumerated set of reviewed rules, not a general fallback to any available compartment.

Local evidence is stored in `reports/generated/biosphere-water-context-evidence.json`. The corresponding verification is `reports/generated/biosphere-water-context-migration-check.json`. The full check in `bw` linked **1,045 additional occurrences**, leaving **6,577 unlinked across 251 signatures**, with **287,170 linked biosphere exchanges**. All 11,947 datasets and 420,063 exchange rows remained. Independent record comparisons verified the declared transformations, uncertainty scaling, unique destinations, unchanged non-biosphere records, and identical results on reapplication. No inventory database was written.

The notebook retains the preceding result in `biosphere-unlinked-after-reviewed.json` and this stage's result in `biosphere-unlinked-after-water-context.json`, under `reports/generated/`.
