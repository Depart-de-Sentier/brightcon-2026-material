You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Methyl ester, from biogenic oils, mix, at regional storage` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~7 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: biomass / fuels
- includedProcesses: This dataset includes the mix of methyl ester used as biofuels for the European supply mix.
- technology: No technology modelled
- generalComment: Inventory refers to 1 kg biodiesel used as transport fuel for blending of diesel.;
UUID: 4290d583-d2ec-3572-b130-a8708c33f8b6
- source cited in the metadata: Jungbluth N. | 2018 | 2018 - LCI oil products distribution - Jungbluth
- time period: 9999-01-9999-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p16-17.txt` (SHA-256 141202902e1820e51817b0d730d3ad4d28b6114a30dc5d34449fb43d422c8268), pages 16-17 of `2018 - LCI oil products distribution - Jungbluth.pdf`.

```
Market mixes                                            Life cycle inventories of oil products distribution

Eurostat (amounts of biodiesel, other liquid biofuels and biogasoline consumed in the EU) and
data from the feedstock mix from USDA FAS 2016 and industry data.
Non –EU bioethanol feedstock is imported from Ukraine (maize, wheat), Canada (wheat),
Russia and Moldova (barley, ray), and Serbia (sugar beet). The largest exporters of biodiesel
feedstock to the EU were Indonesia and Malaysia (palm oil), Brazil and the US (soybean). The
majority of rapeseed oil is of EU origin. Feedstock potential for advanced renewable fuels is
large, but production facilities at commercial scale are still limited.

Tab. 2.5     Share (by weight) of domestic and imported feedstocks for biofuel production in Europe in
             2014 (European Commission 2017)




Fig. 2.2     Share (by volume) of European renewable ethanol produced from each feedstock type 8

The above information has been used to model unit process raw data in Tab. 2.6 for the mix of
biofuels used in Europe.


8    http://epure.org/media/1610/2016-industry-statistics.pdf

© ESU-services Ltd.                                8
Market mixes                                                                          Life cycle inventories of oil products distribution

Tab. 2.6           Unit process raw data for the mix of raw materials used for biofuels in Europe. For ethanol the distillation from 95% to 99.7% purity is included in
                   the inventory




                                                                                                      Infrastructur




                                                                                                                                                                    uncertainty

                                                                                                                                                                    StandardD
                                                                                                                                                                    eviation95
                                                                                                                              ethanol, 99.7%       methyl ester,




                                                                                                       e-Process
                                                                                           Location
                                                                                                                                                                                                                                               Shares




                                                                                                                                                                       Type
                                                                                                                               in H2O, from       from biogenic                                                                                             Shares b iomass




                                                                                                                       Unit




                                                                                                                                                                        %
Explanations                                         Name                                                                                                                         GeneralComment                                              b iomass
                                                                                                                                biomass, at         oils, mix, at                                                                                              feedstock
                                                                                                                                                                                                                                             feedstock
                                                                                                                                 distillation   regional storage
                                                        Location                                                                   RER                RER                                                                                      RER               RER
                                                InfrastructureProcess                                                                0                  0                                                                                      2014              2016
                                                          Unit                                                                      kg                 kg                                                                                       %                 %
Outputs             ethanol, 99.7% in H2O, from biomass, at distillation                   RER            0            kg        1.00E+0                0
product             methyl ester, from biogenic oils, mix, at regional storage             RER            0            kg            0              1.00E+0
Technosphere        heat, natural gas, at industrial furnace >100kW                        RER            0            MJ        1.02E+0                0            1   1.21     (1,2,1,1,1,5); etha+ project Alcosuisse, industrial data
                    electricity, low voltage, production ENTSO, at grid                   ENTSO           0           kWh        9.15E-3                0            1   1.21     (1,2,1,1,1,5); etha+ project Alcosuisse, industrial data
                    ethanol fermentation plant                                             CH             1           unit       5.30E-11               0            1   3.05     (1,2,1,1,1,5); etha+ project Alcosuisse, industrial data

                    treatment, sewage, from residence, to wastewater treatment, class 2    CH             0           m3         4.96E-5               0             1   1.21     (1,2,1,1,1,5); etha+ project Alcosuisse, industrial data
                    ethanol, 95% in H2O, from rye, at distillery                          RER             0           kg           32%                  0            1   1.00     (1,1,1,1,1,1); Wheat                                                22%               32%
                    ethanol, 95% in H2O, from corn, at distillery                         US              0           kg           31%                  0            1   1.05     (1,1,1,1,1,1); Corn                                                 47%               31%
                    ethanol, 95% in H2O, from rye, at distillery                          RER             0           kg            4%                  0            1   1.05     (1,1,1,1,1,1); Barley                                                4%                4%
                    ethanol, 95% in H2O, from sugar beets, at fermentation plant          CH              0           kg           24%                  0            1   1.05     (1,1,1,1,1,1); Sugar beet                                           20%               24%
                    ethanol, 95% in H2O, from rye, at distillery                          RER             0           kg            4%                  0            1   1.05     (1,1,1,1,1,1); Rye                                                   6%                4%
                    ethanol, 95% in H2O, from wood, at distillery                          SE             0           kg            5%                  0            1   1.05     (1,1,1,1,1,1); Cellulosic biomass                                    1%                5%
                    rape methyl ester, at esterification plant                            RER             0           kg             0                52%            1   1.05     (1,1,1,1,1,1); Rape oil                                             52%
                    vegetable oil methyl ester, at esterification plant                    FR             0           kg             0                15%            1   1.05     (1,1,1,1,1,1); UCO (waste oils)                                     15%
                    palm methyl ester, at esterification plant                             MY             0           kg             0                13%            1   1.05     (1,1,1,1,1,1); Palm oil                                             13%
                    soybean methyl ester, at esterification plant                         BR              0           kg             0                 8%            1   1.05     (1,1,1,1,1,1); Soybean oil                                           8%
                    vegetable oil methyl ester, at esterification plant                    FR             0           kg             0                 8%            1   1.05     (1,1,1,1,1,1); Animal fat                                            8%
                    soybean methyl ester, at esterification plant                         BR              0           kg             0                 3%            1   1.05     (1,1,1,1,1,1); Sunflower                                             3%
air, high population                                                                                                                                                              (2,4,1,3,1,3); ecoinvent guidelines, calculation from
                     Heat, waste                                                                                      MJ         3.29E-2               0             1   1.14
density                                                                                                                                                                           electricity consumption and energy balance

                                                                                                                                                                                                                                                            www.epure.org/
                                                                                                                                                                                                                                             European
                                                                                                                                                                                                                                                            media/1610/201
                                                                                                                                                                                                                                             Comission
                                                                                                                                                                                                                                                              6-industry-
                                                                                                                                                                                                                                               2017
                                                                                                                                                                                                                                                             statistics.pdf




© ESU-services Ltd.                                                              9
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
