You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Wood preservative, organic salt, Cr-free, at plant` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~1302 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: chemicals / pesticides
- includedProcesses: Includes the inputs to the production processes and transports of those inputs. No process emission data are available. 
- technology: Mixing of ingredients
- generalComment: Data for one specific product. Material Input data are confidential.;
UUID: 1b7a81dc-1797-3c93-ae60-f239501da3c3
- source cited in the metadata: Werner F. | 2007 | 2007 - LCI wood as fuel and const. mat. - Werner
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Crude Oil: 20.29 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Natural Gas: 20.18 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Water to turbine: 16.29 cubic meter (Resources Resources from water Renewable material resources from water)
- Uranium: 13.35 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Hard Coal: 6.68 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Brown Coal: 5.414 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Energy, Potential (in Hydropower Reservoir), Converted: 1.892 megajoule (natural resource)
- Sodium chloride: 1.092 kilogram (resources in ground)
- Energy, gross calorific value, in biomass: 0.7123 megajoule (resources biotic)
- Gravel: 0.5127 kilogram (soil)
- Energy, Kinetic (in Wind), Converted: 0.2353 megajoule (natural resource)
- Water To Cooling: 0.1635 cubic meter (Resources Resources from water Renewable material resources from water)

## Report excerpt

Source file: `report-p142-143.txt` (SHA-256 d524eed8723d014c55315292b260c6ac90ba31b35cd4e504c200d227b0cc078b), pages 142-143 of `2007 - LCI wood as fuel and const. mat. - Werner.pdf`.

```
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
                                                                                                                                                     14 Impregnation: Agents and processes



                                                                            General Flow information                                                                                                     Representation in ecoinvent                                                                       Uncertainty information

                                                                                                                                                                                          Infra
        Input               Process Name                                             Output                            Remarks                           Cate gory     Sub category               Loca tion      Modul name in ecoinvent          Mean value          Unit     Source mean value    Type       StDv 95% General Comment
                                                                                                                                                                                       struc ture

                                                                                                   Quantities (Application in Switzerland): hazard
                                                                                                   class 4 => 3 kg wood preservative for 1m3 wood;                                                            boric acid, anhydrous, powder,



                             wood preservative, organic salt, Cr-free, at
Boric acid (H3BO3)      Î                                                                                                                           chemicals        inorganics        No        RER                                             confidential    kg          Künniger et al. 2000          1        1.32 (4,4,1,3,1,5,4)
                                                                                                   hazard class 3 => 2 kg wood preservative for 1m3                                                           at plant
                                                                                                   wood
Ethylenediamine         Î                                                                                                                          chemicals         organics          No        RER          ethylenediamine, at plant          confidential    kg          Künniger et al. 2000          1        1.32 (4,4,1,3,1,5,4)

Copper (II) carbonate   Î                                                                                                                          chemicals         inorganics        No        RER          copper carbonate, at plant         confidential    kg          Künniger et al. 2000          1        1.32 (4,4,1,3,1,5,4)
                                                                                                   Total Copper-HDO 0.061 kg. Balanced as
Copper-HDO              Î                                                                                                                          chemicals         organics          No        RER          triethanolamine, at plant          confidential    kg          Künniger et al. 2000          1        1.32 (4,4,1,3,1,5,4)
                                                                                                   ethanolmanine and copperoxide
Copper-HDO              Î                                                                                                                          chemicals         inorganics        No        RER          copper oxide, at plant             confidential    kg          Künniger et al. 2000          1        1.32 (4,4,1,3,1,5,4)

Electricity medium                                                                                                                                                                                            electricity, medium voltage,
                                               plant




                       Î                                                                                                                           electricity       production mix    No        UCTE                                            confidential    kWh         Künniger et al. 2000          1        1.24 (1,4,1,3,1,5,2)
voltage - at grid UCTE                                                                                                                                                                                        production UCTE, at grid
                                                                                                                                                                                                                                                                                                                         (4,5,nA,nA,nA,nA,5
Transport rail          Î                                                                          Chemicals: 600 km                               transport systems train             No        RER          transport, freight, rail                  3.84E-01 tkm         estimated                     1        2.09
                                                                                                                                                                                                                                                                                                                         )
                                                                                                                                                                                                              transport, lorry >16t, fleet                                                                               (4,5,nA,nA,nA,nA,5
Transport lorry                                                                                    Chemicals: 100 km                               transport systems road              No        RER                                                    6.39E-02 tkm         estimated                     1        2.09
                                                                                                                                                                                                              average                                                                                                    )
Tap water               Î                                                                                                                          water supply      production        No        RER          tap water, at user                 confidential    kg          Künniger et al. 2000          1        1.24 (1,4,1,3,1,5,4)

plant                   Î                                                                          organic plant as proxy                          chemicals         organics          Yes       RER          chemical plant, organics                  4.00E-10 unit        estimated                     1        3.79 (5,5,5,5,4,5,9)
                                                                                 Wood
                                                                                 preservative                                                                                                                 wood preservative, organic salt,
                                                                            Î                                                                      paintings         production        No        RER                                                   1.00E+00 kg
                                                                                 chrome-free, at                                                                                                              Cr-free, at plant
                                                                                 plant
                                                                                 Waste heat into
                                                                            Î                                                                      air               unspecified                              Heat, waste                               7.20E-02 MJ          calculated                    1        1.24 (1,4,1,3,1,5,13)
                                                                                 air



Fig. 14.3         Flows for "wood preservative, organic salt, Cr-free, at plant" and its representation in the ecoinvent database




ecoinvent-report No. 9                                                                                                                                                             - 132 -
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
