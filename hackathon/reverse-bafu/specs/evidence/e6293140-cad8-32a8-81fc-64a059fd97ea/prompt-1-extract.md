You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Anthraquinone, at plant` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~1302 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: chemicals / organic
- includedProcesses: This module contains material and energy input, production of waste and emissions for the production of anthrachinone. Transport and infrastructure have been estimated. The input of air is not reported in the data according to the methodology of the study.
- technology: Average technology, representing a mix of 80% chromic acid process and the remaining 20% the synthesis out of phthalic anhydride and benzene.
- generalComment: data based on information from two producers and theoretical information from Ullmann's Enzyclopaedy;
CAS number: 000084-65-1; 
Formula: C14H8O2; 
UUID: e6293140-cad8-32a8-81fc-64a059fd97ea
- source cited in the metadata: Althaus H.-J. | 2007 | 2007 - LCI chemicals - Althaus
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Natural Gas: 120.5 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Water to turbine: 80.19 cubic meter (Resources Resources from water Renewable material resources from water)
- Crude Oil: 76.07 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Uranium: 58.46 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Hard Coal: 34.64 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Brown Coal: 23.18 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Energy, Potential (in Hydropower Reservoir), Converted: 9.487 megajoule (natural resource)
- Calcite: 2.85 kilogram (resources in ground)
- Energy, gross calorific value, in biomass: 2.538 megajoule (resources biotic)
- Gravel: 2.386 kilogram (soil)
- Energy, Kinetic (in Wind), Converted: 0.9835 megajoule (natural resource)
- Sodium chloride: 0.8953 kilogram (resources in ground)

## Report excerpt

Source file: `report-p445-447.txt` (SHA-256 6d1899c288e051fadbd7325d8fe347c4188993c6e8f46d599b3c956f17b12674), pages 445-447 of `2007 - LCI chemicals - Althaus.pdf`.

```
44. Hydrogen Peroxide and Anthraquinone




Fig. 44.1   Reaction scheme from the production of hydrogen peroxide by the anthraquinone process (from Boustead
            & Fawer (1998))




44.4 The anthraquinone production
Anthrachinone (C14H8O2, CAS-No. 84-65-1) is a solid with thin, light yellow needles. It is practically
insoluble in water or in organic solvents. In the latter case, the solubility raises with increasing tem-
perature. Anthraquinone exhibits thereby an extraordinary thermal stablility – also together with oxi-
dizing agents. The most important chemical and physical properties are summarized in Tab. 44.2.

Tab. 44.2   Chemical and physical properties of anthraquinone (Vogel (2000)).


Property                        Value    Unit               Property                   Value    Unit
                                                -1
Molecular weight              208.20     g mol              Melting point              287      °C
Density (at 25°C)               1.438    g cm-3             Boiling point              377      °C


According to Vogel (2000), the production capacity for anthraquinone is about 34'000 t annually.
Thereof, Western Europe produces about 50%, followed by Eastern Europe and Japan.
For the production four different production processes can be distinguished nowadays – with one of
them accounting for almost 85% of the total production: oxidation of anthracene with chromic acid.
The remaining 15% are produced by vapor-phase oxidation of anthracene with air, by naphthalene
process or by synthesis from phthalic anhydride and benzene.


44.4.1 Process data
Main data source for this study is the information used at EMPA for the former inventories of hydro-
gen peroxide (Boustead & Fawer (1998); Dall'Acqua et al. (1999)), representing the last of the above
mentioned production processes. Besides, information from Vogel (2000) about all four processes is
used. Tab. 44.3 summarizes the information from Vogel (2000) – the respective information from
EMPA is not shown here due to confidentiality reasons.




ecoinvent report No. 8                                  - 364 -
                                            44. Hydrogen Peroxide and Anthraquinone


Tab. 44.3       Input and output data for the production of anthraquinone (information from Vogel (2000))

                                                           chromic     oxidation      naphtha-     phthalic
                                                             acid       with air        lene      anhydride
                  Input
                  water                            kg        9000
                  air (flow rate)                 m 3/h                  2150            x
                  anthracene                       kg        2600       20 g/m 3
                  sulphuric acid, 48%              kg       10200
                  sodium dichromate, 20%           kg       23500
                  naphthalene                      kg                                    x
                  xylene                           kg                                    x
                  butadiene                        kg                                    x

                  Output
                  anthraquinone                    kg        3000           x            x


For this study, due to the fact that this second source allows no quantification of the process in three of
the four cases, an average process from the chromic acid process in Tab. 44.3 and the information at
EMPA from the former studies is established – with an amount of 80% chromic acid process. There-
fore the following assumptions and approximations are used:

-   Material input: It is assumed that the chromic acid process does not need any further substances
    than the ones mentioned in Tab. 44.3. The input of sulphuric acid and of sodium dichromate is ex-
    pressed as amount of active substance only. As then the above listed amount of sulphuric acid is
    not sufficient for the process equation, instead the stoechiometric value based on an efficiency of
    95% is used here. The amount of air consumed is not shown in the ecoinvent dataset according to
    Frischknecht et al. (2007). Three of the input materials (anthracene as well as chlorobenzene and
    aluminiumchloride from the information at EMPA) are not within the database ecoinvent. There-
    fore the following assumptions are used, based on information in Häussinger et al. (2000):

            -    Anthracene: Produced by continuous distillation of tar coal, containing about 1.5% of an-
                 thracene - a process with several distillation and further purification steps. Therefore, the
                 amount of anthracene used for the production of anthrachinone is shown in this study here
                 as "chemiacal organics, unspecified".

            -    Chlorobenzene: As chlorobenzenes are prepared industrially by reaction of liquid benzene
                 with gaseous chlorine in the presence of a catalyst at moderate temperature and atmos-
                 pheric pressure, in this study the amount of chlorobenzene is shown as benzene and chlo-
                 rine, assuming a yield of 95%. Further environmental loads of the chlorbenzene production
                 are not taken into account.

            -    Aluminiumchloride: Today most anhydrous aluminium chloride is made by chlorinating
                 aluminium, a highly exothermix reaction. Similar like for chlorobenzene, aluminium chlo-
                 ride is also shown here as pure aluminium and chlorine, again assuming a yield of 95%.
                 Again, further loads are not taken into account.

-   Energy input: In case of the chromic acid process no information about energy production is
    given. Therefore, it is assumed that the energy consumption is similar like in the other dataset. For
    the electricity consumed, an average European medium voltage mix (UCTE-mix) is used. The used
    steam is shown as "steam, for chemical processes, at plant (RER)" according to the description in
    Zah & Hischier (2007).

-   Infrastructure and Transport: In the examined sources, no information about average transport
    distances for the raw materials used are indicated. Therefore, standard distances according to

ecoinvent report No. 8                                       - 365 -
                                    44. Hydrogen Peroxide and Anthraquinone


    Frischknecht et al. (2007) are used within this dataset. Concerning the infrastructure, due to a lack
    of more specific information, the module "chemical plant, organics (RER)" is used here.

-   Emissions to air and water: The values for air emissions in the EMPA data indicated refer to
    process emissions. For the dust emissions, it is assumed in a conservative sense that they are 100%
    PM2.5-emissions. In case of chromic acid process no such information is available. Thus, its emis-
    sions are estimated according to the following steps:

    -   Emissions to air: 1% of the sulphuric acid input into the chromic acid process (as this is emitted
        easily into air) and 0.2% of the sodium dichromate input (assumption);

    -   Emission to water: the remaining input (that means “total input” minus “stoechiometric amount
        for product” minus “air emissions”). Further it was assumed that all the waste water is treated in
        a internal waste water plant. No removal efficiency for sulphuric acid was assumed, leading to
        emissions of 220 g sulphuric acid per kg product in the treated water. The remaining amount of
        sodium dichromate is approximated by an emission of about 1 mol of sodium, e.g. 23 g/kg –
        and of 0.5 mol (due to a removal efficiency of 50%) of chromium ions, e.g. of 26 g/kg.


Due to confidentiality reasons, only the cumulated data from this dataset are available for the user of
the database ecoinvent – the respective unit process is not accessible and therefore no table with data is
shown here. Nevertheless, a uncertainty score is established according to the method used in this study
(see Frischknecht et al. 2007) include reliability, completeness, temporal correlation, geographical cor-
relation, further technological correlation and sample size. The data for one of the two production
processes used is based on some few information from the literature, while the other part is the aver-
age from several producers. Accordingly the uncertainty is not so low, especially due to the fact that
the producer data represents less than 20% of the established module. As the infrastructure and the
transports of the input materials are based on very rough estimation, their respective uncertainty is
high.
Nevertheless, the most important fields of the ecospold meta information from this dataset are listed in
chapter 44.8.


44.5 The hydrogen peroxide production
44.5.1 Process data
Main data source is the information provided by eight hydrogen peroxide producer that has been the
database used at EMPA for the former inventories of hydrogen peroxide (Boustead & Fawer (1998);
Dall'Acqua et al. (1999)). As these data are confidential, they are not shown in details here in this
study, but an average process is calculated of them and Tab. 44.4 shows this summarized process.




ecoinvent report No. 8                              - 366 -
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
