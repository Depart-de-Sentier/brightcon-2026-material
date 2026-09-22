# Remaining particle and missing-substance review

This historical review examined 120 PM10-labeled rows. The subsequent [metal-pair restoration](bafu-2026-biosphere-pm10-metals.md) links 26 of them as source-defined palladium/rhodium, leaving **94** in that signature. The overlap count falls from 91 to **65**. The particle-size and other-substance limitations below remain; no size proxy is applied.

## PM10 is not the coarse particle fraction

The then-remaining **120 `Particulates, < 10 um` occurrences** include the fine and coarse size ranges in their names. Biosphere 3.10 instead provides separate targets below 2.5 µm, between 2.5 and 10 µm, and above 10 µm. A split needs a source-supported size distribution.

In **91 of these 120 rows**, the same inventory and receiving compartment contain a PM2.5 quantity larger than the PM10 quantity. Subtracting that PM2.5 amount from PM10 would yield a negative coarse fraction. These aggregated rows therefore cannot be assumed to describe one shared particle total. The review does not perform that subtraction or assume a universal split.

The two former PM10-labelled EPS rows already restored to palladium/rhodium are excluded from these 120 occurrences. The genuine EPS PM10 row remains unresolved.

## Black carbon and carbon black

The **38 `Black carbon` and 28 `Carbon black` occurrences** have no corresponding target in the installed biosphere or the official 3.9 elementary-flow master. Their source inventories also contain particle-size exchanges: this is true for all 66 records checked. Mapping these carbon-specific rows to ordinary particulate matter could duplicate particulate mass already represented elsewhere and would discard their carbon identity.

The natural-gas XML comments cite EMEP/EEA emission factors. The [2023 solid-fossil-fuel report](../data/raw/BAFU-2026%20v1%20LCI%20Reports/2023%20-%20LCI%20solid%20fossil%20fuel%20-%20Itten.pdf) explicitly reports carbon-black rows separately from the particle size classes. No particulate substitution is applied.

## Other missing emission targets

| Flow | Remaining occurrences | Finding |
| --- | ---: | --- |
| Perfluorocyclobutane, PFC-318 | 64 | CAS 115-25-3 has no matching installed target. Another greenhouse gas is not an identity-preserving substitute. |
| Perfluorocyclopropane | 64 | No corresponding target was found. Quantities matching the PFC-318 rows do not establish that these different labels are duplicates. |
| Kerosene to urban air | 64 | No matching emission target. A pure constituent or technosphere fuel product would not preserve the mixture and exchange meaning. |
| Petrol to surface water | 64 | No matching emission target; the mixture composition is not established. |

All findings and original exchange attributes are recorded in `reports/generated/biosphere-particles-missing-chemical-review.json`, with consuming filenames, neighbouring particle quantities, citations and source hashes. This review does not modify XML, importer exchanges or databases.
