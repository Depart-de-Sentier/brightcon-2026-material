You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Diesel, burned in diesel-electric generating set` [GLO], reference unit 1 MJ, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~23 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: mechanical / other energy
- includedProcesses: Diesel consumption, emissions and infrastructure for the use of diesel in electric generating sets. Transport to site not included.
- technology: On site generation of electricity in diesel motor generators.
- generalComment: Generic module to estimate emissions due to the use of diesel during crude oil exploration.;
32865dd1-13be-378f-a2cb-8da075b9e203
- source cited in the metadata: Meili C. | 2021 | 2021 - LCI crude oil and natural gas extraction - Meili
- time period: 1985-01-2020-01

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 MJ):
- none

## Report excerpt

Source file: `report-p47-48.txt` (SHA-256 fe272d520776d0207e5eda6f538f74334841bfb316cc630258bdc57a705ac4f0), pages 47-48 of `2021 - LCI crude oil and natural gas extraction - Meili.pdf`.

```
Emissions to air                                                 Life cycle inventories of crude oil and natural gas extraction


h. To take the generator into account, the demand is increased by 50%. Furthermore, a share of
5% of high alloy steel and 10% copper is assumed.

Tab. 9.6           Life cycle inventory data for a 10MW diesel-electric generating set




                                                                                                                         StandardDeviation95
                                                                                                       UncertaintyType
                                                                                     diesel-electric




                                                                 Location


                                                                            Unit
                                          Name                                       generating set                                            GeneralComment




                                                                                                                                 %
                                                                                   production 10MW



                                     Location                                           RER
                            Infras tructureProces s                                       1
                                       Unit                                              unit
product      diesel-electric generating set production 10MW      RER        unit       1.00E+0
technosphere copper, at regional storage                         RER        kg         1.80E+4             1                3.05 (na,5,na,1,na,BU:1.05); Estimation
             chromium steel 18/8, at plant                       RER        kg         9.00E+3             1                3.05 (na,5,na,1,na,BU:1.05); Estimation
             steel, low-alloyed, at plant                        RER        kg         1.80E+5             1                3.05 (na,5,na,1,na,BU:1.05); Estimation
             transport, freight, lorry 16-32 metric ton, fleet                                                                   (5,5,na,na,na,BU:2); Standard distance
                                                                 RER        tkm        2.07E+4             1                3.95
             average                                                                                                             100km
                                                                                                                                 (5,5,na,na,na,BU:2); Standard distance
               transport, freight, rail                          RER        tkm        1.24E+5             1                3.95
                                                                                                                                 600km




9.3.2 Direct emissions
Direct emissions are estimated as shown in Tab. 9.7 and mainly explained in a former study
(Jungbluth 2007). To avoid double counting, emissions of CH 4, SO2 and NOx were removed as
they are assessed separately for overall extraction of crude oil and natural gas according to
chapter 9.5. Other emissions are assessed in analogy to the engines of trucks. Benzene is as-
sumed to be emitted with 0.02 kg/TJIn and Benzo(a)pyrene with 0.1E-3 kg/TJIn and heavy metal
emissions corresponding to the content in diesel. For chromium VI, a share of 0.2% of overall
chromium is assumed.




© ESU-services Ltd.                                                          - 39 -
Emissions to air                                                           Life cycle inventories of crude oil and natural gas extraction


Tab. 9.7          Life cycle inventory for diesel, burned in diesel-electric generating set, without CH4, SO2
                  and NOx-emissions




                                                                                                                                         StandardDeviation
                                                                      InfrastructureProce
                                                                                                   Diesel, burned in




                                                                                                                       UncertaintyType
                                                                                                    diesel-electric




                                                           Location
                                                                                                    generating set,




                                                                                                                                               95%
                                                                                            Unit
                                      Name                                                                                                                   GeneralComment
                                                                                                   without SO2, Nox
                                                                                                       and CH4-
                                                                                                       emissions

                                     Location                                                            GLO
                              InfrastructureProcess                                                       0

                                       Unit                                                               MJ

                   Diesel, burned in diesel-electric
product            generating set, without SO2, Nox and   GLO 0                             MJ         1.00E+0
                   CH4-emissions
technosphere       diesel, at regional storage            RER 0                             kg         2.34E-2              1              1.24              (3,3,3,3,1,BU:1.05); Calculation
                                                                                                                                                             (3,5,1,3,5,BU:1.05); Rough estimation with data for
                   lubricating oil, at plant              RER 0                             kg         6.70E-5              1              2.06
                                                                                                                                                             cogen 200kWe
                   diesel-electric generating set production
                                                             RER 1                          unit       1.85E-10             1              3.12              (3,5,3,3,3,BU:3); Estimation
                   10MW
                   disposal, used mineral oil, 10% water, to
Disposal                                                     CH 0                           kg         6.70E-5              1              2.06              (3,5,1,3,5,BU:1.05); Rough estimation
                   hazardous waste incineration
emission air, low
                   Benzene                                    -               -             kg         2.00E-8              1              3.03              (3,3,3,3,1,BU:3); Extrapolation
population density
                   Benzo(a)pyrene                             -               -             kg         1.00E-10             1              3.03              (3,3,3,3,1,BU:3); Extrapolation
                   Carbon dioxide, fossil                     -               -             kg         7.30E-2              1              1.10              (2,3,2,3,1,BU:1.05); Literature
                   Carbon monoxide, fossil                    -               -             kg         6.80E-4              1              5.03              (3,3,3,3,1,BU:5); Literature
                   Dinitrogen monoxide                        -               -             kg         6.00E-6              1              1.54              (3,3,3,3,1,BU:1.5); Literature
                   Mercury                                    -               -             kg         4.67E-10             1              5.08              (3,3,3,3,3,BU:5); Literature on content in diesel
                                                                                                                                                             (2,3,1,3,1,BU:1.5); Set 0 as assessed in overall
                   Methane, fossil                            -               -             kg              0               1              1.51
                                                                                                                                                             emissions for extraction
                                                                                                                                                             (2,3,1,3,1,BU:1.5); Set 0 as assessed in overall
                   Nitrogen oxides                            -               -             kg              0               1              1.51
                                                                                                                                                             emissions for extraction
                   NMVOC, non-methane volatile organic
                                                              -               -             kg         9.24E-5              1              1.51              (2,3,1,3,1,BU:1.5); Environmental report
                   compounds, unspecified origin
                   Particulates, < 2.5 um                     -               -             kg         1.70E-4              1              3.03              (3,3,3,3,1,BU:3); Literature
                                                                                                                                                             (2,3,1,3,1,BU:1.05); Set 0 as assessed in overall
                   Sulfur dioxide                             -               -             kg              0               1              1.09
                                                                                                                                                             emissions for extraction
                   Cadmium                                    -               -             kg         2.34E-10             1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions
                   Copper                                     -               -             kg         3.97E-8              1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions
                   Chromium                                   -               -             kg         1.17E-9              1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions
                                                                                                                                                             (2,3,1,1,3,BU:5); Literature for automobile emissions,
                   Chromium VI                                -               -             kg         2.34E-12             1              5.06
                                                                                                                                                             0.2% share of Cr is Cr VI
                   Nickel                                     -               -             kg         1.64E-9              1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions
                   Selenium                                   -               -             kg         2.34E-10             1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions
                   Zinc                                       -               -             kg         2.34E-8              1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions




9.4        Natural gas burned in gas turbine
In this study, only the existing dataset for the combustion of sweet gas is adjusted as presented
in Tab. 9.8. Emissions of methane, SO2 and NOx were removed as they are assessed separately
for overall extraction of crude oil and natural gas according to chapter 9.5 .




© ESU-services Ltd.                                                                                - 40 -
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 MJ.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
