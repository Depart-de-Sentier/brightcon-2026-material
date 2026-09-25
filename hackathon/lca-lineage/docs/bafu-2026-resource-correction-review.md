# Why resource-correction flows remain unresolved

The remaining 363 resource-correction occurrences span 14 full signatures: gravel, sand, eight metals, and biomass energy. They are accounting adjustments for dissipative resource use. They are not ordinary resource extractions or chemical-name aliases.

The supplied report [2014 — Update material data in KBOB list — Wyss](../data/raw/BAFU-2026%20v1%20LCI%20Reports/2014%20-%20Update%20material%20data%20in%20KBOB%20list%20-%20Wyss.pdf), section 3.2, explains credits for anticipated recycling: 90% of concrete aggregates, 50% of wood energy content, and the primary portion of fully recycled metals. It states that these corrections do not affect primary-energy and greenhouse-gas indicators. The [civil-engineering report](https://www.stadt-zuerich.ch/content/dam/web/de/aktuell/publikationen/2014/studien-netto-null/oekobilanzen-tiefbauarbeiten-studie.pdf), section 2.3.7, and the supplied active-glass-façade report, section 2.4, describe the ecological-scarcity scope. The original report's assumptions are recorded here, not re-estimated for 2026.

| Correction resource | Occurrences | Source amount signs |
| --- | ---: | --- |
| Gravel | 85 | 74 negative, 11 positive |
| Sand | 83 | 72 negative, 11 positive |
| Aluminium | 45 | All negative |
| Iron | 30 | All negative |
| Zinc | 23 | All negative |
| Chromium | 16 | All negative |
| Nickel | 4 | All negative |
| Copper | 2 | All negative |
| Tin | 2 | All negative |
| Lead | 1 | Negative |
| Biomass energy | 72 | All negative |

Mapping these rows to ordinary resource flows would allow every LCIA method using those flows to characterize the adjustments. In particular, mapping biomass-energy corrections to ordinary biomass energy would reduce cumulative energy demand, contrary to the documented scope. Matching metal CAS numbers does not preserve this method-specific meaning.

This consequence was checked against the installed `bafu-2026-biosphere-310` project. Method `('Cumulative Energy Demand (CED)', 'energy resources: renewable, biomass', 'energy content (HHV)')` assigns factor **1.0** to ordinary biomass-energy UUID `01c12fca-ad8b-4902-8b48-2d5afe3d3a0f`. Linking the 72 negative correction amounts to that flow would therefore introduce negative CED contributions. This was a read-only factor check; no exchanges or methods were changed.

These rows therefore remain unresolved under the user's decision to retain unsupported flows. No values or signs are changed, no rows are dropped, and no supplementary database is created. A future solution requires an explicitly supported representation for the correction indicators and their intended LCIA factors; ordinary-resource relabeling alone does not provide it.
