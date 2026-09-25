# Carbon, particles, energy, wood and land: reassessment

The September 22 review found a supported correspondence missed by the previous name/CAS candidate search: **18 mosaic-land exchanges can link to heterogeneous agricultural land**. The [scoped rules and source evidence](bafu-2026-biosphere-land-mosaic.md) are now part of the import notebook. Including the twelve approved carbon mappings, nine approved uranium/wood conversions and later [26 PM10 metal corrections](bafu-2026-biosphere-pm10-metals.md), the full `bw` check leaves **2,991 occurrences across 155 signatures** unresolved. The earlier conclusion that no further supported mappings were available was too broad.

## Carbon dioxide and carbon monoxide

The existing generic-air fossil CO₂ and CO targets have the right substances, units and receiving compartment. Their origin classification is the remaining modelling decision.

The user approved **“Use the documented fossil approximation.”** The [active migration](../schemas/mappings/bafu-2026-biosphere-diesel-carbon.json) covers **12 rows in six diesel/demolition-related inventories** and is now applied by the notebook. The original candidate remains as a proposal-history snapshot.

| Inventory | CO₂, kg | CO, kg |
| --- | ---: | ---: |
| Diesel, auxiliary machines at mixed rubble sorting | 3.15 | 0.007419 |
| Diesel, auxiliary machines at concrete crusher | 3.15 | 0.007419 |
| Diesel, hydraulic digger at building deconstruction | 3.15 | 0.007419 |
| Disposal, brick filled with perlite | 0.005177025 | 0.000012193127 |
| Disposal, Baumgartner wood-metal window frame | 0.00053774508 | 0.0000012665177 |
| Production, Baumgartner wood-metal window frame | 0.0000053774508 | 0.000000012665177 |

The three direct diesel inventories explicitly cite hydraulic-digger emissions. All six CO/CO₂ pairs share the same ratio to rounding precision. Inferring a common diesel-emission origin is reasonable, but it does not establish an exact fossil fraction. The current Swiss diesel supplier includes biogenic fuel and separately reports biogenic CO₂. Classifying all twelve quantities as fossil is therefore a documented approximation. The rules preserve amounts, uncertainty, original labels, comments and all other exchange fields.

The migration targets `Carbon dioxide, fossil / air / kilogram` (`349b29d1-3e58-4c66-98b9-9d1a076efd2e`) and `Carbon monoxide, fossil / air / kilogram` (`ba2f3f82-c93a-47a5-822a-37ec97495275`). Target uniqueness, all source rows, the ratio comparison and file hashes are recorded in `reports/generated/biosphere-diesel-carbon-evidence.json`.

The other **11 carbon rows** need a separate decision: seven plastics CO₂ rows use the original ILCD `carbon dioxide` flow `fe0acd60-3ddc-11dd-af54-0050c2490048`, version 02.00.000, which specifies CO₂ mass but no carbon origin. Four CO rows occur in burnt shale, cement, and phenolic/bio-based glass-wool inventories. The approval for the twelve rows above does not extend to these eleven. The full-record check in `biosphere-diesel-carbon-migration-check.json` confirms twelve new links, unchanged amounts and uncertainty, no other exchange changes, unique targets and idempotence.

## Particles

The source check confirms that true PM10 and coarse PM2.5–10 are separate quantities in the original plastics inventories. For example, LDPE has 0.000065181 kg PM10 and 0.000029996 kg coarse particles; its 0.00015466 kg fine-particle amount also comes from the aggregate inventory. These cannot be made equivalent through a simple rename or subtraction.

The later [PM10 pair restoration](bafu-2026-biosphere-pm10-metals.md) resolves 26 additional PM10-labeled palladium/rhodium rows. For example, LDPE has two identical quantities of 6.5835e-11 kg. The helper now restores a verified identical pair as one Pd and one Rh emission, with all quantities and uncertainty preserved. This leaves 94 generic-air PM10-labeled rows requiring a size-distribution basis.

For genuine particles, the [ecoinvent guidelines](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Database/Fundamentals/dataqualityguideline_ecoinvent_3_20130506.pdf), section 5.9.4, recommend source-specific size distributions, then named reference inventories such as CEPMEIP and AP-42. They do not define a universal PM10-to-coarse conversion. A particle proxy would need an explicit distribution/overlap assumption; no such proxy is applied here.

## Energy and wood

The two wood rows have an existing standing-wood target in m³. Its official master-data entry carries 550 kg dry mass and 632.5 kg wet mass per m³, including 82.5 kg water. The user approved the 632.5 kg/m³ default as an assumption; it does not establish the source moisture content. The EPS quantity first needs its source-confirmed MJ basis restored and conversion using 14.7 MJ/kg. The recycling-paper quantity is already wood mass. Both conversions are now applied with that assumption recorded on the exchange.

Seven uranium-energy rows now use the uranium mass target with the approved 560,000 MJ/kg convention, explicitly marked as an assumption. The two oil-energy rows concern oil shale and cannot simply use a crude-oil calorific value. The one hydro-labelled EPS row is source-defined wave energy; the remaining waste-heat resource row is an input. The 72 biomass-energy resource corrections are method-specific recycling adjustments. These are distinct modelling questions, rather than one energy-name correction. See the [source definitions](bafu-2026-biosphere-resource-followup.md) and [recycling-adjustment review](bafu-2026-resource-correction-review.md).

## Other occupation and transformation

After the 18 corrected mosaic exchanges, **82 land exchanges** remain: 34 urban, 20 traffic, 21 originally combining agriculture and forest, and seven sealed-soil exchanges in plastics. Existing generic unspecified-land targets provide a possible broader representation, while specific urban, road/rail or crop targets require corresponding assumptions. Original occupation units (m²·year), transformation units (m²), and from/to direction must be retained in either approach.

## Approved uranium and wood conversions

The user approved **“Use the documented 560,000 MJ/kg convention”** and **“Use the documented catalog density assumption.”** Two active migration files are now loaded after the carbon stage:

- [Seven uranium-energy rules](../schemas/mappings/bafu-2026-biosphere-uranium-convention.json) divide MJ by **560,000 MJ/kg**, using the documented GaBi/ecoinvent convention as an explicit assumption. [openLCA’s method implementation report](https://nexus.openlca.org/ws/files/10505), printed page 42, gives this convention and notes the alternative ILCD value of 544,284 MJ/kg. The original flow defines an energy resource but does not establish which mass conversion its model used.
- [Two wood rules](../schemas/mappings/bafu-2026-biosphere-wood-density.json) use the target master-data mass basis of **632.5 kg/m³** (550 kg dry matter and 82.5 kg water). This assumes 15% moisture on a dry-mass basis despite unknown source moisture. Recycling-paper wood uses `kg / 632.5`; the EPS quantity uses `source MJ / 14.7 / 632.5`, first correcting its exported kg label. Both target `Wood, unspecified, standing / natural resource, biotic / cubic meter`.

Each rule is scoped to the source filename and complete signature. Original labels, units and compartments remain in `bafu original biosphere`; `bafu conversion assumption` records the factor, interpreted source quantity unit, assumption and documentation link. Original quantities, source hashes, target UUIDs and both decisions are recorded in `reports/generated/biosphere-uranium-wood-evidence.json`. The candidate files and proposal evidence remain historical snapshots. These conventions do not measure the original inventories’ unknown energy-per-mass factors or moisture.

The nine lognormal exchanges retain their distribution type and log-space scale. For positive conversion factor `f`, amounts and any bounds multiply by `f`, and log-space location shifts by `ln(f)`. No uncertainty is added for the chosen convention itself. Paper wood converts 0.04994 kg to 0.00007895652173913044 m³; EPS wood converts the source quantity 1.8889e-11 MJ to 2.031566776908392e-15 m³.

At the uranium/wood stage, the full `bw` check verifies **nine new links**, unique targets, one source occurrence per rule, the expected numerical transformations, unchanged other records and repeat-application idempotence. It leaves **290,730 linked biosphere exchanges and 3,017 unresolved across 155 signatures**. All 11,947 datasets and 420,063 exchange rows remain; all technosphere exchanges link. Results, including complete before/after records for the nine conversions, are in `reports/generated/biosphere-uranium-wood-migration-check.json`. The notebook writes separate post-carbon and post-uranium reports; wood writes `biosphere-unlinked-after-wood-density.json`. The subsequent PM10-metal stage writes the final `biosphere-unlinked.json`, with 2,991 unresolved exchanges.

Reproduce the import check without writing an inventory database:

```sh
conda run -n bw python "scripts/ecospold importer/check_land_mosaic.py"
```
