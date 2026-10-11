You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Canning of legumes` [CH], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~4 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: food industry / processing
- includedProcesses: nan
- technology: nan
- generalComment: The inventory applies to the canning of 1kg of legumes.
- source cited in the metadata: Kaegi T. | 2021 | 2021 - LCA tomatoes and green beans production - Kaegi
- time period: 2014-01-2020-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p49-50.txt` (SHA-256 d93302ef1b62ab86d7b7e22e378c07ee4b33c299ceeabe30ed9140a77c5d0182), pages 49-50 of `2021 - LCA tomatoes and green beans production - Kaegi.pdf`.

```
ReferenceFunction     401    Name                                         Canning of legumes
Geography             662    Location                                             CH
ReferenceFunction     493    InfrastructureProcess                                0
ReferenceFunction     403    Unit                                                 kg
DataSetInformation    201    Type                        1
                      202    Version                     1.0
                      203    energyValues                0
                      205    LanguageCode                en
                      206    LocalLanguageCode           de
DataEntryBy           302    Person                      107
                      304    QualityNetwork              1
ReferenceFunction     400    DataSetRelatesToProduct     1
                                                         The inveontory includes all
                                                         processes from washing,
                      402    IncludedProcesses
                                                         blanching to filling, but without
                                                         the tincan itself.

                      490    LocalName

                      491    Synonyms
                                                         The inventory applies to the
                      492    GeneralComment
                                                         processing of 1kg of legumes.
                      494    InfrastructureIncluded      1
                      495    Category                    food industry
                      496    SubCategory                 processing
                      497    LocalCategory               Lebensmittel
                      498    LocalSubCategory            Verarbeitung
                      499    Formula
                      501    StatisticalClassification
                      502    CASNumber
TimePeriod            601    StartDate                   2014
                      602    EndDate                     2020
                      603    DataValidForEntirePeriod    1
                      611    OtherPeriodText
                                                         The inventory is modelled for
Geography             663    Text
                                                         Switzerland
Technology            692    Text
Representativeness    722    Percent
                      724    ProductionVolume
                      725    SamplingProcedure
                      726    Extrapolations              none
                      727    UncertaintyAdjustments      none



Figure 19: Metadata of canning of food
                                                                                                                                                            Standard Deviation 95%
                                                                                  Infrastructure Process




                                                                                                                                         Uncertainty Type
                                                               Location




                                                                                                           Unit




                                      Name                                                                        Canning of legumes                                                 General Comment




                                    Location                                                                             CH

                            Infrastructure Process                                                                        0
                                      Unit                                                                               kg
product              Canning of legumes                     CH                        0                    kg            1.0                   0

technosphere         electricity, low voltage, at grid      CH                        0                    kWh         7.08E-01        1.00E+00 1.25E+00 (2,3,3,2,1,5,BU:1.05); ;


                     chemical plant, organics              RER                        1                    unit        1.00E-10        1.00E+00 3.06E+00 (2,3,3,2,1,5,BU:3); ;


                     tap water, at user                     CH                        0                    kg         1.20E+00         1.00E+00 1.25E+00 (2,3,3,2,1,5,BU:1.05); ;




Figure 20: Unit process raw data of canning of food




Life cycle assessment of tomatoes and green beans production| December 2021                                                                                                                    page 49 of 64
ReferenceFunction     401    Name                                                           Drying of food, 1 kg water
Geography             662    Location                                                                   CH
ReferenceFunction     493    InfrastructureProcess                                                       0
ReferenceFunction     403    Unit                                                                       kg
DataSetInformation    201    Type                        1
                      202    Version                     1.0
                      203    energyValues                0
                      205    LanguageCode                en
                      206    LocalLanguageCode           de
DataEntryBy           302    Person                      107
                      304    QualityNetwork              1
ReferenceFunction     400    DataSetRelatesToProduct     1
                                                         The inventory includes the energy needed to evaporate 1 kg
                      402    IncludedProcesses
                                                         of water
                      404    Amount                      1
                      490    LocalName
                      491    Synonyms
                                                         The inventory refers to an average drying machine with a
                      492    GeneralComment
                                                         yield of 30 to 40 kg of dried products per day.
                      494    InfrastructureIncluded      1
                      495    Category                    food industry
                      496    SubCategory                 processing
                      497    LocalCategory               Lebensmittel
                      498    LocalSubCategory            Verarbeitung
                      499    Formula
                      501    StatisticalClassification
                      502    CASNumber
TimePeriod            601    StartDate                   2020
                      602    EndDate                     2020
                      603    DataValidForEntirePeriod    1
                      611    OtherPeriodText
Geography             663    Text                        The inventory is modelled for Switzerland
Technology            692    Text
Representativeness    722    Percent
                      724    ProductionVolume
                                                         data ist based on data sheets from producer of drying
                      725    SamplingProcedure
                                                         machines
                      726    Extrapolations              none
                      727    UncertaintyAdjustments      none



Figure 21: Metadata of drying of food


                                                                                                                                                             Standard Deviation 95%
                                                                        Infrastructure Process




                                                                                                                                          Uncertainty Type
                                                            Location




                                                                                                  Unit




                                      Name                                                                 Drying of food, 1 kg water                                                 General Comment




                                    Location                                                                             CH

                            Infrastructure Process                                                                        0
                                      Unit                                                                               kg
product              Drying of food, 1 kg water             CH              0                     kg                     1.0                    0

technosphere         electricity, low voltage, at grid      CH              0                    kWh                8.80E-01            1.00E+00 2.07E+00 (3,3,1,1,5,5,BU:1.05); ;


                     steel, low-alloyed, at plant          RER              0                     kg                2.04E-03            1.00E+00 2.07E+00 (3,3,1,1,5,5,BU:1.05); ;

emission water,
                     Water, CH                                 -               -                  m3                1.00E+00            1.00E+00 2.29E+00 (3,3,1,1,5,5,BU:1.5); ;
unspecified



Figure 22: Unit process raw data of drying of food




Life cycle assessment of tomatoes and green beans production| December 2021                                                                                                                        page 50 of 64
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
