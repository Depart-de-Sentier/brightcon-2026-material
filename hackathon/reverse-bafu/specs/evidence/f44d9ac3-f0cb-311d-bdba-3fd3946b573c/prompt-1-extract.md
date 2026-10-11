You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Acetone, liquid, at plant` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~152 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: chemicals / organic
- includedProcesses: Aggregated data for all processes from raw material extraction until delivery at plant
- technology: production by oxidation of cumene
- generalComment: Data are from the Eco-profiles of the European plastics industry (PlasticsEurope). Not included are the values reported for: recyclable wastes, amount of air / N2 / O2 consumed, unspecified metal emission to air and to water, mercaptan emission to air, unspecified CFC/HCFC emission to air, dioxin to water. The amount of "sulphur (bonded)" is assumed to be included into the amount of raw oil.;
CAS number: 000067-64-1; 
UUID: f44d9ac3-f0cb-311d-bdba-3fd3946b573c
- source cited in the metadata: Althaus H.-J. | 2007 | 2007 - LCI chemicals - Althaus
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Natural Gas: 33.92 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Crude Oil: 25.51 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Uranium: 2.254 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Hard Coal: 1.641 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Energy, Potential (in Hydropower Reservoir), Converted: 0.1375 megajoule (natural resource)
- Energy, gross calorific value, in biomass: 0.1131 megajoule (resources biotic)
- Water To Cooling: 0.07867 cubic meter (Resources Resources from water Renewable material resources from water)
- Sodium chloride: 0.07547 kilogram (resources in ground)
- Calcite: 0.003589 kilogram (resources in ground)
- Water: 0.0031 cubic meter (Resources Resources from water Renewable material resources from water)
- Sulfur: 0.002392 kilogram (Resources Resources from ground Non-renewable element resources from ground)
- Peat: 0.001925 megajoule (Resources Resources from ground Non-renewable energy resources from ground)

## Report excerpt

Source file: `report-p98-99.txt` (SHA-256 3d1e65fc1ab8cd34367ba38e89b6e67aee1f8d42da8cc07a6e14f8ce98b5b5ad), pages 98-99 of `2007 - LCI chemicals - Althaus.pdf`.

```
3. Acetone



3         Acetone
           Author:    Mike Chudacoff, Chudacoff Oekoscience, Zurich
                      Roland Hischier, Empa, St. Gallen (Changes 2007)
           Review:    Heiko Kunst, TU Berlin
           Last Changes:                                                          2007


3.1      Introduction
This chapter describes the production of acetone. This chemical is used primarily for the production of
methylmethacrylate and methyl acrylate (polymers for reins, glazing panels etc.).
Synonyms for acetone: 2-propanone, dimethyl ketone


3.2      Reserves and resources of acetone
Acetone is an organic chemical compound. It is produced primarily from cumene by oxidation.


3.3      Characterisation of acetone
Acetone, C3H6O, is a colorless volatile liquid with a sweetish odor. Its molecular weight is 58.08
g/mol. Acetone melts at -94.7 °C, and boils just above 56°C. It is soluble in water, ethyl alcohol and
ether. Acetone is flammable and its vapor may cause flash fires when ignited. Acetone will react
strongly with oxidizing agents (Wells (1999)).


3.4      Production and use of acetone
Worldwide production of acetone in 2001 was 4.1 million tonnes, valued at about $2 billion, accord-
ing to www.manufacturing.net. According to the same source, world consumption of acetone in 2001
was 3.8 million tonnes, reports SRI. The U.S. and Western Europe accounted for around 60% of this
amount; Japan and other Asian countries accounted for 27%. The global average annual growth rate in
acetone consumption between 2001 and 2006 is estimated to be ca. 4 %.
According to Wells (1999), just over a quarter of acetone consumption is used for methyl methacrylate
and methyl acrylate. Roughly another quarter is used for surface coatings and in the manufacture of
cellulose acetate fiber. The third most important use is for the production of chemical solvents such as
methyl isobutyl ketone, diacetone alcohol and others. A growing outlet is for the production of
Bisphenol A.
Major plants are located in Germany, the Netherlands, Italy, the US, South Africa, Japan and Taiwan.
Major producers include Shell Chemical, Enichem and Sasol, among others.


3.5      System characterization
Acetone and phenol are co-products and their production and demand are intertwined. Both chemicals
are produced primarily via the oxidation of cumene, according to Wells (1999). Cumene, also known
as isopropyl benzene, is produced from benzene and propylene.


3.5.1 Production of cumene (Wells, 1999)
Propylene and benzene are mixed and reacted using a catalyst. Reaction temperature is kept at 200 –
250 °C, with a pressure range of 15-35 bar. A high benzene concentration suppresses side reactions.


ecoinvent report No. 8                           - 17 -
                                                3. Acetone


The reactor gases are used to heat incoming feed. Cumene is distilled; heavy bottoms contain di- and
triisopropylbenzene,

       C6H6 + CH2=CHCH3 Æ C6H5CH(CH3)2                                                         (1)


Cumene has basically only one outlet, the manufacture of acetone and phenol.


1.5.2 Production of acetone by oxidation of cumene (Wells (1999))
Cumene is oxidised to cumene hydroperoxide (2) which is split to form phenol and acetone (3), using
sulphuric acid. The reaction mixture is cooled and residual acid is neutralized. Acetone, together with
some alpha-methylstyrene and cumene is recovered, the acetone is then purified by distillation.

       C6H5CH(CH3)2 + O2 Æ C6H5C(CH3)2OOH                                                      (2)

       C6H5C(CH3)2OOH Æ C6H5OH (phenol) + CH3COCH3 (acetone)                                   (3)


Wells (1999) indicates that 2300 kg of cumene are required to produce 1000 kg of acetone with a yield
of 90%. The production of the co-product phenol is not included in this figure.


3.5.2 Production of acetone by dehydrogenation of isopropyl alcohol (Wells
      (1999))
Another major production route for acetone, is by dehydrogenation of isopropyl alcohol. Isopropyl
alcohol or isopropanol, can be produced by two production routes, both of which entail the hydration
of propylene.

       CH3CH=CH2 + H2O Æ (CH3)2CHOH                                                            (4)
The isopropyl is heated until it is in the vaport phase and then reacted via catalyst. The reaction takes
place at 300-450°C and at 2-3 bar. The exit gases containing isopropyl alcohol, acetone and hydrogen
are cooled. Acetone is obtained by distillation.

        (CH3)2CHOH Æ CH3COCH3 + H2                                                             (5)


The yield is reported to be 90 – 95% (Wells (1999))


3.6      Life cycle Inventory for acetone
The production process for acetone was assessed with data from PlasticsEurope (Boustead (2005-07)),
which assumes that acetone stems from the oxidation of cumene, i.e. the isopropyl alcohol production
route is not included in this inventory. The data stem from 1992 to 2001 and account for three produc-
tion sites in Europe. Due to the fact that this dataset is cumulated it was not possible to use the other
processes modelled in econvent to obtain a transparent process chain. The data was nevertheless used
because it represents a high share of the European production of this type of chemicals. The transfor-
mation for the data as given in Boustead (2005-07) to the data format in ecoinvent is described in de-
tail in the methodology part of the plastics part in Hischier (2007).
Within the module assessed here there are only the resources and emissions considered which are
given in the data source. Therefore no land use could be included and no direct soil emissions within


ecoinvent report No. 8                            - 18 -
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
