You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Epoxy resin, liquid, at plant` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~117 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: chemicals / organic
- includedProcesses: Aggregated data for all processes from raw material extraction until delivery at plant
- technology: Production from epichlorohydrin and bisphenol-A
- generalComment: All data are based on Eco-profiles of the European plastics industry;
CAS number: 025928-94-3; 
UUID: c80b8e9e-8a0d-36f6-a4a2-1509d03e42c2
- source cited in the metadata: Althaus H.-J. | 2007 | 2007 - LCI chemicals - Althaus
- time period: 1999-01-1999-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Natural Gas: 76.28 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Crude Oil: 29.08 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Uranium: 12.43 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Hard Coal: 6.383 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Brown Coal: 1.976 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Sodium chloride: 1.8 kilogram (resources in ground)
- Energy, Potential (in Hydropower Reservoir), Converted: 1.3 megajoule (natural resource)
- Calcite: 0.71 kilogram (resources in ground)
- Water To Cooling: 0.384 cubic meter (Resources Resources from water Renewable material resources from water)
- Energy, gross calorific value, in biomass: 0.206 megajoule (resources biotic)
- Potassium chloride: 0.029 kilogram (resources in ground)
- Water: 0.0191 cubic meter (Resources Resources from water Renewable material resources from water)

## Report excerpt

Source file: `report-p358-358.txt` (SHA-256 bb4176808c83800336d34f6a5f7e2974c13b770e157a1bf3ba2fa6304e257596), pages 358-358 of `2007 - LCI chemicals - Althaus.pdf`.

```
31. Epoxy Resins


Tab. 31.2   Disaggregated life cycle inventory for the production of liquid epoxy resin (modified from Boustead 1999).




                                                                                                Locatio


                                                                                                          Infrastr
                                                                                                                                epoxy resin, liquid,
                                                        Name                                                         Unit




                                                                                                  n
                                                                                                                            disaggregated data, at plant
                                                            Location                                                                   RER
                                                     InfrastructureProcess                                                               0
                                                              Unit                                                                       kg
output                    epoxy resin, liquid, disaggregated data, at plant                       RER     0           kg             1.00E+0
resource, in ground       Calcite, in ground                                                       -      -           kg             7.10E-1
                          Gas, natural, in ground                                                  -      -          Nm3             6.78E-1
                          Oil, crude, in ground                                                    -      -           kg             3.55E-1
                          Sand, unspecified, in ground                                             -      -           kg             1.20E+3
                          Sodium chloride, in ground                                               -      -           kg             1.80E+0
                          sylvite, 25 % in sylvinite, in ground                                    -      -           kg             2.90E-2
resource, in water        Water, well, in ground                                                   -      -           m3             1.40E-5
                          Water, river                                                             -      -           m3             9.20E-5
                          Water, salt, ocean                                                       -      -           m3             9.50E-4
                          Water, cooling, unspecified natural origin                               -      -           m3             3.84E-1
                          Water, unspecified natural origin                                        -      -           m3             6.10E-3
technosphere              electricity, medium voltage, production UCTE, at grid                  UCTE     0          kWh             2.19E+0
                          heavy fuel oil, burned in power plant                                   RER     0           MJ             1.10E+1
                          natural gas, burned in industrial furnace >100kW                        RER     0           MJ             5.77E+1
                          tap water, at user                                                      RER     0           kg             1.30E+1
                          disposal, municipal solid waste, 22.9% water, to sanitary landfill      CH      0           kg             2.98E-1
                          disposal, municipal solid waste, 22.9% water, to municipal incineration CH      0           kg             5.80E-3
                          chemical plant, organics                                                RER     1          unit            4.00E-10
                          transport, freight, rail                                                RER     0          tkm             1.74E+0
                          transport, lorry 32t                                                    RER     0          tkm             6.06E+1
emission air, unspecified Acetaldehyde                                                             -      -           kg             4.70E-5
                          Ammonia                                                                  -      -           kg             4.00E-6
                          Carbon dioxide, fossil                                                   -      -           kg             6.50E-1
                          Carbon monoxide, fossil                                                  -      -           kg             2.60E-4
                          Halogenated hydrocarbons, chlorinated                                    -      -           kg             1.10E-5
                          Heat, waste                                                              -      -           MJ             7.87E+0
                          Hydrocarbons, aromatic                                                   -      -           kg             2.80E-5
                          Hydrogen chloride                                                        -      -           kg             2.30E-4
                          Hydrogen fluoride                                                        -      -           kg             5.00E-7
                          Hydrogen sulfide                                                         -      -           kg             3.00E-6
                          Lead                                                                     -      -           kg             5.00E-7
                          Mercury                                                                  -      -           kg             5.00E-7
                          Methane, fossil                                                          -      -           kg             2.00E-4
                          Methane, chlorotrifluoro-, CFC-13                                        -      -           kg              8.00E-6
                          Nitrogen oxides                                                          -      -           kg             2.70E-3
                          Particulates, > 2.5 um, and < 10um                                       -      -           kg             7.10E-3
                          Sulfur dioxide                                                           -      -           kg             1.70E-3
                          NMVOC, non-methane volatile organic compounds, unspecified origin        -      -           kg             4.94E-4
emission water, river     Ammonium, ion                                                            -      -           kg             3.00E-6
                          Arsenic, ion                                                             -      -           kg             5.00E-7
                          BOD5, Biological Oxygen Demand                                           -      -           kg             1.10E-3
                          Calcium, ion                                                             -      -           kg             5.40E-2
                          Carboxylic acids, unspecified                                            -      -           kg             5.90E-5
                          Chloride                                                                 -      -           kg             9.80E-1
                          Chlorinated solvents, unspecified                                        -      -           kg             1.13E-4
                          Chromium VI                                                              -      -           kg             5.00E-7
                          COD, Chemical Oxygen Demand                                              -      -           kg              5.10E-2
                          Copper, ion                                                              -      -           kg             5.00E-7
                          Cyanide                                                                  -      -           kg             5.00E-7
                          DOC, Dissolved Organic Carbon                                            -      -           kg              1.70E-2
                          Fluoride                                                                 -      -           kg             1.00E-6
                          Oils, unspecified                                                        -      -           kg              6.90E-5
                          Hydrocarbons, unspecified                                                -      -           kg             6.40E-5
                          Iron, ion                                                                -      -           kg             1.00E-6
                          Magnesium                                                                -      -           kg             1.70E-5
                          Mercury                                                                  -      -           kg             1.00E-6
                          Nickel, ion                                                              -      -           kg             5.00E-7
                          Nitrate                                                                  -      -           kg             1.00E-6
                          Nitrogen                                                                 -      -           kg             1.00E-5
                          Phenol                                                                   -      -           kg             6.00E-6
                          Phosphate                                                                -      -           kg             2.20E-4
                          Potassium, ion                                                           -      -           kg             8.20E-4
                          Sodium, ion                                                              -      -           kg             3.80E-1
                          Sulfate                                                                  -      -           kg             8.10E-3
                          Sulfide                                                                  -      -           kg             1.00E-6
                          Suspended solids, unspecified                                            -      -           kg             8.30E-2
                          VOC, volatile organic compounds, unspecified origin                      -      -           kg             5.20E-3
                          Zinc, ion                                                                -      -           kg             5.00E-7



ecoinvent report No. 8                                           - 277 -
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 kg.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
