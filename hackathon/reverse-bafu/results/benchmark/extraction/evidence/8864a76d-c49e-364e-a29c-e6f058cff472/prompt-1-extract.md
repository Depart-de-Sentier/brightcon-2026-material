You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Crude oil, at production onshore` [GQ], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~33 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: oil / production
- includedProcesses: Production of crude oil including energy use, infrastructure and emissions.
- technology: 100 % offshore and  0 % onshore production
- generalComment: The onshore oil production delivers the product crude oil. The values are derived from a multioutput-process "combined onshore gas and oil production" by allocation based on heating values for crude oil and natural gas UUID=8864a76d-c49e-364e-a29c-e6f058cff472
- source cited in the metadata: Meili C. | 2025 | 2025 - LCI crude oil and natural gas extraction - Meili
- time period: 2023-2025

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Crude Oil: 43.4 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Ground Water: 0.0001767 cubic meter (Resources Resources from water Renewable material resources from water)
- Water: 7.526e-05 cubic meter (Resources Resources from water Renewable material resources from water)

## Report excerpt

Source file: `report-p76-79.txt` (SHA-256 9eee17db8fd5b30856613b36d2675549d6f4b257160aeb15d8ef91c5bca3544f), pages 76-79 of `2025 - LCI crude oil and natural gas extraction - Meili.pdf`.

```
Summary of life cycle inventory data      Life cycle inventories of crude oil and natural gas extraction


Tab. 12.2   Unit process raw data, example for crude oil and natural gas production in CA, part 1




© ESU-services Ltd.                                - 68 -
Summary of life cycle inventory data       Life cycle inventories of crude oil and natural gas extraction


Unit process raw data, example for crude oil and natural gas production in the CA, part 2




© ESU-services Ltd.                                 - 69 -
Summary of life cycle inventory data       Life cycle inventories of crude oil and natural gas extraction


Unit process raw data, example for crude oil and natural gas production in the CA, part 3




© ESU-services Ltd.                                 - 70 -
Summary of life cycle inventory data                                      Life cycle inventories of crude oil and natural gas extraction


Unit process raw data, example for crude oil and natural gas production in the CA, part 4




                                                                                                                                                                                                                                            StandardDeviation95%
                                                                                                           InfrastructureProcess




                                                                                                                                                                                                                          UncertaintyType
                                                                                                                                          Combined Crude oil,     Natural  Combined Crude oil,    Natural




                                                                                             SubCategory
                                                                                                                                                                                                            Combined




                                                                           Category
                                                                                                                                          gas and oil     at      gas , at gas and oil    at       gas, at




                                                           Location
   CA
                                                                                                                                                                                                            gas and oil




                                                                                                                                   Unit
                                      Name                                                                                                production production production production production production                                                        GeneralComment
                                                                                                                                                                                                            production
                                                                                                                                           offshore   offshore   offs hore  onshore    onshore    onshore
                                                                                                                                                                                                              {CA} U
                                                                                                                                            {CA} U     {CA} U     {CA} U     {CA} U     {CA} U     {CA} U


            2023                      Location                                                                                               CA         CA        CA          CA         CA        CA           CA
data available                Infras tructureProcess                                                                                          -          -         -           -          -         -            -
                                        Unit                                                                                                  a         kg        Nm3          a         kg        Nm3           a
                                                                      emis sions to
emission to water,Oils,
                   riverunspecified                           -                     river                           -              kg              0     63.8%      36.2%    1.19E+6      63.8%      36.2%      1.19E+6 1                   1.56 (2,1,1,3,3,BU:1.5); Average 2021 to 2023, IOGP 2024
                                                                      water
                                                                      emis sions to
                   BOD5, Biological Oxygen Demand             -                     river                           -              kg              0     63.8%      36.2%    3.75E+6      63.8%      36.2%      3.75E+6 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   COD, Chemical Oxygen Demand                -                     river                           -              kg              0     63.8%      36.2%    3.75E+6      63.8%      36.2%      3.75E+6 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   DOC, Dissolved Organic Carbon              -                     river                           -              kg              0     63.8%      36.2%    1.03E+6      63.8%      36.2%      1.03E+6 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   TOC, Total Organic Carbon                  -                     river                           -              kg              0     63.8%      36.2%    1.03E+6      63.8%      36.2%      1.03E+6 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   AOX, Adsorbable Organic Halogen as Cl      -                     river                           -              kg              0     63.8%      36.2%    1.23E+1      63.8%      36.2%      1.23E+1 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   Nitrogen                                   -                     river                           -              kg              0     63.8%      36.2%    9.19E+2      63.8%      36.2%      9.19E+2 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   Sulfur                                     -                     river                           -              kg              0     63.8%      36.2%    3.19E+3      63.8%      36.2%      3.19E+3 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
emission to water,Oils,
                   oceanunspecified                           -                     ocean                           -              kg       1.87E+5      63.8%      36.2%           0     63.8%      36.2%      1.87E+5 1                   1.56 (2,1,1,3,3,BU:1.5); Average 2021 to 2023, IOGP 2024
                                                                      water
                                                                      emis sions to
                   BOD5, Biological Oxygen Demand             -                     ocean                           -              kg       5.89E+5      63.8%      36.2%           0     63.8%      36.2%      5.89E+5 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   COD, Chemical Oxygen Demand                -                     ocean                           -              kg       5.89E+5      63.8%      36.2%           0     63.8%      36.2%      5.89E+5 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   DOC, Dissolved Organic Carbon              -                     ocean                           -              kg       1.62E+5      63.8%      36.2%           0     63.8%      36.2%      1.62E+5 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   TOC, Total Organic Carbon                  -                     ocean                           -              kg       1.62E+5      63.8%      36.2%           0     63.8%      36.2%      1.62E+5 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   AOX, Adsorbable Organic Halogen as Cl      -                     ocean                           -              kg       1.92E+0      63.8%      36.2%           0     63.8%      36.2%      1.92E+0 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   Nitrogen                                   -                     ocean                           -              kg       1.44E+2      63.8%      36.2%           0     63.8%      36.2%      1.44E+2 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
                   Sulfur                                     -                     ocean                           -              kg       5.00E+2      63.8%      36.2%           0     63.8%      36.2%      5.00E+2 1                   1.56 (2,1,1,3,3,BU:1.5); Extrapolation for sum parameter
                                                                      water
                                                                      emis sions to
emission to soil Oils, unspecified                            -                     unspecified                     -              kg              0     63.8%      36.2%    3.87E+5      63.8%      36.2%      3.87E+5 1                   1.56 (2,1,1,3,3,BU:1.5); Average 2021 to 2023, IOGP 2024
                                                                      s oil
                                                                      emis sions to                                                                                                                                                              (2,1,1,3,3,BU:1.5); Weighted average 2021 to 2023,
emission to air, low
                   Sulfur
                     population
                          dioxidedensity                      -                     low. pop.                       -              kg       9.89E+5      63.8%      36.2%    1.26E+7      63.8%      36.2%      1.35E+7 1                   1.56
                                                                      air                                                                                                                                                                        IOGP 2024
                                                                      emis sions to                                                                                                                                                              (2,1,1,3,3,BU:1.5); Weighted average 2021 to 2023,
                   Nitrogen oxides                            -                     low. pop.                       -              kg       1.07E+7      63.8%      36.2%    1.36E+8      63.8%      36.2%      1.47E+8 1                   1.56
                                                                      air                                                                                                                                                                        IOGP 2024
                                                                      emis sions to                                                                                                                                                              (3,3,1,3,3,BU:1.5); ass uming 20% halon compared
                   Methane, bromotrifluoro-, Halon 1301       -                     low. pop.                       -              kg       3.82E+2      63.8%      36.2%           0     63.8%      36.2%      3.82E+2 1                   1.58
                                                                      air                                                                                                                                                                        to Jungbluth 2007
                                                                                                                                                                                                                                                 (3,3,1,3,3,BU:1.5); Ass uming 80% replacement of
                                                                      emis sions to
                   Methane, trifluoro-, HFC-23                -                     low. pop.                       -              kg       1.54E+3      63.8%      36.2%           0     63.8%      36.2%      1.54E+3 1                   1.58 halon 1301 with HFC-23 (amount according to
                                                                      air
                                                                                                                                                                                                                                                 Jungbluth 2007)




© ESU-services Ltd.                                                                         - 71 -
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
