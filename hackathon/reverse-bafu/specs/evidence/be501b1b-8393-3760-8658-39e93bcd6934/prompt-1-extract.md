You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Wood preservative, inorganic salt, containing Cr, at plant` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~1302 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: chemicals / pesticides
- includedProcesses: Includes the inputs to the production processes and transports of those inputs. No process emission data are available. 
- technology: Mixing of ingredients
- generalComment: Data for one specific product. Material Input data are confidential.;
UUID: be501b1b-8393-3760-8658-39e93bcd6934
- source cited in the metadata: Werner F. | 2007 | 2007 - LCI wood as fuel and const. mat. - Werner
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Natural Gas: 13.4 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Water to turbine: 10.59 cubic meter (Resources Resources from water Renewable material resources from water)
- Crude Oil: 6.753 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Hard Coal: 4.132 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Uranium: 3.827 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Brown Coal: 1.391 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Energy, Potential (in Hydropower Reservoir), Converted: 1.112 megajoule (natural resource)
- Calcite: 0.9305 kilogram (resources in ground)
- Gravel: 0.6322 kilogram (soil)
- Energy, gross calorific value, in biomass: 0.3399 megajoule (resources biotic)
- Chromium: 0.2602 kilogram (Resources Resources from ground Non-renewable element resources from ground)
- Sodium chloride: 0.2096 kilogram (resources in ground)

## Report excerpt

Source file: `report-p141-142.txt` (SHA-256 207d840fb9d1bcd41d2176e4428093b00d6f6b428ebf3aff8f7f6ba46699d195), pages 141-142 of `2007 - LCI wood as fuel and const. mat. - Werner.pdf`.

```
14 Impregnation: Agents and processes




                                                                      General Flow information                                                                                                         Representation in ecoinvent                                                                  Uncertainty information

                                                                                                                                                                                        Infra
         Input             Process Name                                          Output                          Remarks                               Cate gory     Sub category               Loca tion      Modul name in ecoinvent        Mean value        Unit     Source mean value   Type       StDv 95% General Comment
                                                                                                                                                                                     struc ture


                                                                                             For the destillation of the coal tar to creosote,
                                                                                             data is used from 1992 stemming from an english
                                                                                             company (LCA "Creosote treated distribution
Fuel oil high sulfur                                                                         poles case study" , Hillier 1997); it is estimated                                                             heavy fuel oil, burned in
content Euro, in       Î                                                                     that 35% of the raw tar can be used for the        oil                heating systems   No        RER          industrial furnace 1MW, non-          4.20E+00 MJ          Hillier 1997                 1        1.16 (1,4,3,3,1,1,1)
boiler 1 MW                                                                                  production of creosote; allocation is made by                                                                  modulating
                              wood preservative, creosote, at plant

                                                                                             mass; estimate of airbourne emissions 2% HC;
                                                                                             emissions into water are taken from an
                                                                                             Anonymous 1990
                                                                                             Starting material coal tar is inventoried as coal
Coal tar coke          Î                                                                                                                         hard coal         fuels             No        RER          hard coal coke, at plant              2.92E+01 MJ          Hillier 1997                 1        1.16 (1,4,3,3,1,1,3)
                                                                                             tar coke (source: ESU)
Electricity medium                                                                                                                                                                                          electricity, medium voltage,
                       Î                                                                                                                         electricity       production mix    No        UCTE                                               1.11E+00 kWh         Hillier 1997                 1        1.16 (1,4,3,3,1,1,2)
voltage - at grid UCTE                                                                                                                                                                                      production UCTE, at grid

plant                  Î                                                                     organic plant as proxy                              chemicals         organics          Yes       RER          chemical plant, organics              4.00E-10 unit        estimated                    1        3.79 (5,5,5,5,4,5,9)
                                                                           Wood
                                                                           preservative,                                                                                                                    wood preservative, creosote, at
                                                                      Î                                                                          paintings         production        No        RER                                                1.00E+00 kg
                                                                           creosote, at                                                                                                                     plant
                                                                           plant
                                                                           Waste heat into
                                                                      Î                                                                          air               unspecified                              Heat, waste                           3.99E+00 MJ          calculated                   1        1.16 (1,4,3,3,1,1,13)
                                                                           air
                                                                                                                                                                                                            NMVOC, non-methane volatile
                                                                      Î    NMVOC                                                                 air               unspecified                              organic compounds, unspecified        2.05E-02 kg          estimated                    1        2.11 (4,3,3,3,1,5,23)
                                                                                                                                                                                                            origin
                                                                      Î    COD               calculated from BOD, assuming C6H12O6               water             unspecified                              COD, Chemical Oxygen Demand           1.00E-03 kg          calculated                   1        1.75 (3,5,4,5,3,5,32)

                                                                      Î    DOC               calculated from BOD, assuming C6H12O6               water             unspecified                              DOC, Dissolved Organic Carbon         3.92E-04 kg          calculated                   1        1.75 (3,5,4,5,3,5,32)

                                                                      Î    TOC               calculated from BOD, assuming C6H12O6               water             unspecified                              TOC, Total Organic Carbon             3.92E-04 kg          calculated                   1        1.75 (3,5,4,5,3,5,32)

                                                                      Î    BOD                                                                   water             unspecified                              BOD5, Biological Oxygen Demand        1.00E-03 kg          Anonymous 1990               1        1.75 (3,5,4,5,3,5,32)




Fig. 14.1          Flows for "wood preservative, creosote, at plant" and its representation in the ecoinvent database




ecoinvent-report No. 9                                                                                                                                                           - 130 -
                                                                                                                                             14 Impregnation: Agents and processes



                                                                 General Flow information                                                                                                        Representation in ecoinvent                                                                     Uncertainty information

                                                                                                                                                                                  Infra
        Input              Process Name                                   Output                             Remarks                             Cate gory     Sub category               Loca tion      Modul name in ecoinvent         Mean value         Unit     Source mean value    Type       StDv 95% General Comment
                                                                                                                                                                               struc ture

                                                                                         Quantities (Application in Switzerland): hazard
                                                                                         class 4 => 12 kg wood preservative for 1m3                                                                   boric acid, anhydrous, powder,
Boric acid (H3BO3)   Î                                                                                                                     chemicals         inorganics        No        RER                                           confidential    kg          Künniger et al. 2000          1        1.32 (4,4,1,3,1,5,4)
                                                                                         wood; hazard class 3 => 7.5 kg kg wood                                                                       at plant

                            wood preservative, inorganic salt,
                                                                                         preservative for 1m3 wood
Chromium acid        Î                                                                                                                     chemicals         inorganics        No        RER          chromium oxide, flakes, at plant confidential    kg          Künniger et al. 2000          1        1.32 (4,4,1,3,1,5,4)
                                 containing Cr, at plant
Copper(II)oxide (CuO) Î                                                                                                                    chemicals         inorganics        No        RER          copper oxide, at plant           confidential    kg          Künniger et al. 2000          1        1.32 (4,4,1,3,1,5,4)

Electricity medium                                                                                                                                                                                    electricity, medium voltage,
                       Î                                                                                                                   electricity       production mix    No        UCTE                                          confidential    kWh         Künniger et al. 2000          1        1.24 (1,4,1,3,1,5,2)
voltage - at grid UCTE                                                                                                                                                                                production UCTE, at grid
                                                                                                                                                                                                                                                                                                               (4,5,nA,nA,nA,nA,5
Transport rail       Î                                                                   Chemicals: 600 km                                 transport systems train             No        RER          transport, freight, rail                2.94E-01 tkm         estimated                     1        2.09
                                                                                                                                                                                                                                                                                                               )
                                                                                                                                                                                                      transport, lorry >16t, fleet                                                                             (4,5,nA,nA,nA,nA,5
Transport lorry                                                                          Chemicals: 100 km                                 transport systems road              No        RER                                                  4.90E-02 tkm         estimated                     1        2.09
                                                                                                                                                                                                      average                                                                                                  )
Tap water            Î                                                                                                                     water supply      production        No        RER          tap water, at user               confidential    kg          Künniger et al. 2000          1        1.24 (1,4,1,3,1,5,4)

plant                Î                                                                   organic plant as proxy                            chemicals         organics          Yes       RER          chemical plant, organics                4.00E-10 unit        estimated                     1        3.79 (5,5,5,5,4,5,9)

                                                                      Wood
                                                                      preservative                                                                                                                    wood preservative, inorganic
                                                                 Î                                                                         paintings         production        No        RER                                                  1.00E+00 kg
                                                                      containing                                                                                                                      salt, containing Cr, at plant
                                                                      chrome, at plant
                                                                      Waste heat into
                                                                 Î                                                                         air               unspecified                              Heat, waste                             1.30E-01 MJ          calculated                    1        1.24 (1,4,1,3,1,5,13)
                                                                      air



Fig. 14.2         Flows for "wood preservative, inorganic salt, containing Cr, at plant" and its representation in the ecoinvent database




ecoinvent-report No. 9                                                                                                                                                     - 131 -
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
