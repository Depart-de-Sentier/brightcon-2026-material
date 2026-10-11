You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Hydrogen cyanide, at plant` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~152 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: chemicals / acids (inorganic)
- includedProcesses: Aggregated data for all processes from raw material extraction until delivery at plant
- technology: production by reaction of methane with ammonia
- generalComment: Data are from the Eco-profiles of the European plastics industry (PlasticsEurope). Not included are the values reported for: recyclable wastes, amount of air / N2 / O2 consumed, unspecified metal emission to air and to water, mercaptan emission to air, unspecified CFC/HCFC emission to air, dioxin to water. The amount of "sulphur (bonded)" is assumed to be included into the amount of raw oil.;
CAS number: 000074-90-8; 
UUID: 0f667d2d-2007-3185-8aeb-0b8e6fbdfb5c
- source cited in the metadata: Althaus H.-J. | 2007 | 2007 - LCI chemicals - Althaus
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Natural Gas: 86.82 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Crude Oil: 13.47 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Uranium: 4.408 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Hard Coal: 2.928 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Energy, Potential (in Hydropower Reservoir), Converted: 0.5375 megajoule (natural resource)
- Energy, gross calorific value, in biomass: 0.3395 megajoule (resources biotic)
- Water To Cooling: 0.07129 cubic meter (Resources Resources from water Renewable material resources from water)
- Sulfur: 0.02206 kilogram (Resources Resources from ground Non-renewable element resources from ground)
- Water: 0.01355 cubic meter (Resources Resources from water Renewable material resources from water)
- Sand: 0.01135 kilogram (soil)
- Sodium chloride: 0.007223 kilogram (resources in ground)
- Phosphorus: 0.002621 kilogram (Resources Resources from ground Non-renewable element resources from ground)

## Report excerpt

Source file: `report-p436-438.txt` (SHA-256 f7af81ba5953b5ff6210cd0672f5288969e8f414d0a6d6f0788ce325f60f6abc), pages 436-438 of `2007 - LCI chemicals - Althaus.pdf`.

```
43. Hydrogen cyanide


    In 1997-2000, European production of toluene was approximately 2.7 million tons; according to
    (European Commission (2002)). Major plants are operated in Germany, the Netherlands, Italy, Spain,
    the UK, the US, Japan, Taiwan, South Korea, among others. Major manufacturers include DeGussa,
    Dow and DuPont.


    43.5 System characterization
    HCN is produced mostly from the so-called Andrussow and Blausäure-Methan-Ammoniak (BMA)
    process, although some HCN is also obtained as a by-product from acrylonitrile production (US-EPA
    (2000)).


    43.5.1 Andrussow process (US-EPA (2000))
    Filtered air, ammonia and natural gas are fed into a reactor and are heated to 2’200 °C in the presence
    of a catalyst. The reactor off-gas in cooled and sent through an ammonia absorption process to remove
    unreacted ammonia. Cold water is then added to capture the HCN. The HCN-water mixture is sent to a
    stripper, where pure HCN is gained. This step produces wastewater.

           2 NH3 + 2 CH4 + 3 O2 Æ 2 HCN + 6 H2O                                                              (1)


    43.5.2 Blausaure-Methan-Ammonia Process (US-EPA (2000))
    The BMA process involves the reaction of ammonia with methane without the presence of air. After
    removal of ammonia and recovery of HCN, the off-gases consist basically of hydrogen. The hydrogen
    can be used in other processes or burnt as a source of energy.

           2 NH3 + 2 CH4 Æ 2 HCN + 6 H2                                                                      (2)


    BMA accounts for 15 % of the total European production.3


    Resource consumption
    Tab. 43.2   Resource consumption for the production of HCN (kg/kg)


                Precursor                                    Amount (kg)
                Ammonia                                        0.76
                Natural gas                                    0.68
                Sulfuric acid (conc.)                          0.26


    In case the hydrogen produced by the BMA process is not combusted, a total of 0.23 kg hydrogen is
    produced per kg HCN.




3
    Personal communication Ramon Mendivil, ETH Zurich Institute for Chemical- and Bioengineering, Safety & Environmental
    Technology Group, May/June 2003.

    ecoinvent report No. 8                                 - 355 -
                                                     43. Hydrogen cyanide


    Energy consumption
    Tab. 43.3   Energy consumption for the production of HCN (kg/kg)


                Precursor                     Hydrogen             Hydrogen
                                             export route         combustion
                                                                     route
                Natural gas                       0.78                0.51


    A total of 31 MJ is required per kg of HCN.


    Air emissions (BMA process)
    Tab. 43.4   Air emissions from the production of HCN (g/kg)


                Substance                                     Amount (g)
                Dust (SPM)                                    1.01
                SOx                                           18.82
                CH4                                           0.98
                NOx                                           9.30
                CO2                                           2473.52


    These figures – numbers from 4 – are calculated values based on the combustion of hydrogen gas in
    the process as a fuel that replaces part of the natural gas burned as a fuel.


    Wastewater / Liquid wastes
    No values available.


    Solid wastes (BMA process)
    0.34 kg of ammonium sulfate (Na2SO4) are produced per kg of HCN, as well as 0.02 kg of sodium
    cyanide. The ammonium sulfate is sold as a fertilizer.4


    43.6 Life cycle Inventory for HCN
    The production process for hydrogen cyanide was assessed with data from PlasticsEurope (Boustead
    (2005-07)), that is based on the years 1992 – 1993 and accounts for about 63’000 tons of HCN pro-
    duced at three sites in Europe. It cannot be ascertained which processes were used by the companies
    providing the data – the hydrogen emissions that are listed are no indicator of the actual processes, as
    hydrogen stemming from the BMA process may be captured and used in other processes and still
    cause emissions.
    Due to the fact that the PlasticsEurope dataset is cumulated it was not possible to use the other proc-
    esses modelled in econvent to obtain a transparent process chain. The data was nevertheless used be-
    cause it represents a high share of the European production of this type of chemicals. The transforma-




4
    Personal communication Ramon Mendivil, ETH Zurich Institute for Chemical- and Bioengineering, Safety & Environmental
    Technology Group, May/June 2003.

    ecoinvent report No. 8                                  - 356 -
                                           43. Hydrogen cyanide


tion for the data as given in Boustead (2005-07) to the data format in ecoinvent is described in detail in
the methodology part of the plastics part in Hischier (2007).
Within the module assessed here there are only the resources and emissions considered which are
given in the data source. Therefore no land use could be included and no direct soil emissions within
the process chain are stated. For each waste type used in the original dataset, an appropriate waste
process from the ecoinvent modules was included.


43.7 Data quality considerations
Tab. 43.5 and Tab. 43.7 summarize the resulting data of the HCN production in Europe. According to
the methodological remarks in Hischier (2007), these data contain no uncertainty information. Addi-
tionally, the most important fields of the ecospold meta information from this dataset are listed in
chapter 43.11.




ecoinvent report No. 8                            - 357 -
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
