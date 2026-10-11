You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Vermiculite, at mine` [ZA], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~16 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: minerals / unspecified
- includedProcesses: includes excavation by digger, blasting, transportation within mine, the land-use for quarrying, the recultivation
- technology: High level of technology used in one of the biggest vermiculite mines in the world, in South-Africa.
- generalComment: For a lack of data the dust emissions for bauxite mining are used as proxy. No recultivation is assumed. To account for the phosphate mined together with the vermiculite, the resource "phosphorus, 18% in apatite, 12% in crude ore, in ground" is inventoried. Since the apatite is dumped but afterwards used by other companies it is neither considered co-product nor waste. The paraffin fueled heating system is approximated with "light fuel oil, burned in industrial furnace 1 MW, non-modulating". For the electricity mix the UCPTE-mix has been used.;
Synonyms: Glimmer; 
UUID: 96da7ab9-3f6d-3b4c-847a-113818353957
- source cited in the metadata: Kellenberger D. | 2007 | 2007 - LCI building products - Kellenberger
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Vermiculite: 1 kilogram (soil)
- Phosphorus: 0.3 kilogram (Resources Resources from ground Non-renewable element resources from ground)

## Report excerpt

Source file: `report-p683-685.txt` (SHA-256 1339dbe3216c6a93d9c21b60463961cf9e3abd33020525e801504b8dfe704438), pages 683-685 of `2007 - LCI building products - Kellenberger.pdf`.

```
Part XXI: Lightweight Products and its Preliminary Products and Processes


    6.1        Vermiculite, at mine
    The ecoinvent database meta information of “vermiculite, at mine” (Tab. 6.1) includes all important
    and necessary information to use the data correctly.

    Tab. 6.1   Ecoinvent database meta information for the product “vermiculite, at mine”


      Name                                vermiculite, at mine

      Location                            ZA
      Infrastructure Process              0
      Unit                                kg
      Data Set Version                    2.0
      Included Processes                  includes excavation by digger, blasting, transportation within mine, the
                                          land-use for quarrying, the recultivation
      Amount                              1
      Local Name                          Vermiculit, ab Mine
      Synonyms                            Glimmer
      General Comment to reference        For a lack of data the dust emissions for bauxite mining are used as
      function                            proxy. For the recultivation process the module "recultivation, lime-
                                          stone mine" has been used as proxy. To account for the phosphate
                                          mined together with the vermiculite, the resource "phosphorus, 18% in
                                          apatite, 12% in crude ore, in ground" is inventoried. Since the apatite
                                          is dumped but afterwards used by other companies it is neither con-
                                          sidered co-product nor waste. The paraffin fueled heating system is
                                          approximated with "light fuel oil, burned in industrial furnace 1 MW,
                                          non-modulating". For the electricity mix the UCPTE-mix has been
                                          used.
      Start Date                          2000
      End Date                            2000
      Data Valid For Entire Period        1
      Other Period Text
      Geography text                      For the exchanges, RER, GLO and CH modules have been used as
                                          proxy.
      Technology text                     High level of technology used in one of the biggest vermiculite mines
                                          in the world, in South-Africa.
      Representativeness [%]
      Production Volume                   2'390'000 tons (2001)
      Sampling Procedure                  Data from questionnaire from one company called Parabora mining
                                          company ltd. in South-Africa.
      Extrapolations                      data which are only available for GLO, RER and CH have been used
                                          as proxy for ZA
      Uncertainty Adjustments             none


    Fig. 6.1 shows the system of the module “vermiculite, at mine”. It shows all in- and output flows, the
    allocation to the modules in the ecoinvent database, the sources (mainly personal communication 3 ,
    Künniger et al. (2001), Süd-Chemie (1999) and estimations) and the standard deviation for each data.
    Most of the vermiculite used in Europe comes from South Africa. and therefore the data in this study
    are based on information from Palabora Mining Company Ltd. in South Africa. 4



3
    personal communication: Mr. Gabe van den Berg, Palabora Mining Company Limited, South Africa, August 13th 2002
    ecoinvent-report No. 7                                     -9-
                              Part XXI: Lightweight Products and its Preliminary Products and Processes


    “Vermiculite mining and concentration in the Republic of South Africa was started in the 1940's. The
    industry was established primarily to satisfy European demand and later extended to North America
    and Australia. Most of Palabora's vermiculite production is exported. At Palabora vermiculite ore is
    derived from three sources:

    -    The vermiculite pit which is mined as an open cast truck and loader operation. The pit is roughly
         1600 m long on the north-south axis and 1400 m wide on the east-west axis. Overall depth is 50 m
         below average surface elevation.
    -    The original plant dump of plant tailings has become economically more significant due to an ever
         increasing demand for the finer grades of vermiculite. The dump is reclaimed using trucks and
         front-end loaders.
    -    Palabora Phosphate and Vermiculite (PP&V) mine. A deposit mined as an open cast truck and
         loader operation similar to the original pit.”




4    ecoinvent-report No. 7                                    - 10 -
    http://www.palabora.co.za, access date: February 2004
                                                                                                         Part XXI: Lightweight Products and its Preliminary Products and Processes



                                                            General Flow information                                                                             Representation in ecoinvent                                                                         Uncertainty Information
                                                                                                                                                                        Infra-
                            Process                                                                                                                     Sub-                   Loca-          Modul name in                   Mean                                          StDv        General
        Input                                                                 Output                   Remarks                         Category                         struc-                                                          Unit         Source          Type
                             Name                                                                                                                     category                  tion            ecoinvent                     value                                         95%        Comment
                                                                                                                                                                         ture

                                                                                       total mined amount of vermiculite ore in


                             excavation of vermiculite from nature (part 1)
                                                                                       Palabora mine in 2001: 2'390'000 tons, total                                                                                                            After questionaire
vermiculite in ground   Î                                                              amount of waste (mainly phosphate) in        resource        in ground                          Vermiculite, in ground                 1.00E+00 kg      Palabora Mining         1     1.24   (1,4,1,1,1,5);
                                                                                       2001: 710'000 tons, no losses taken into                                                                                                                Company Ltd. (2002)
                                                                                       account as no data available

                                                                                       total amount of secondary product (mainly
                                                                                                                                                                                                                                               After questionaire
                                                                                       phosphate) mined in 2001: 710'000 tons,                                                         Phosphorus, 18% in apatite, 12%
phosphate in ground     Î                                                                                                            resource       in ground                                                                 3.00E-01 kg      Palabora Mining         1     2.06   (1,4,1,1,5,5);
                                                                                       module "Phosphorus, 18% in apatite, 12% in                                                      in crude ore, in ground
                                                                                                                                                                                                                                               Company Ltd. (2002)
                                                                                       crude ore, in ground" used as proxy
                                                                                       transformation = mining area, assumed
occupation mineral
                                                                                       occupation time: 50 years; assumed density                                                      Occupation, mineral extraction
extraction site (mine) Î                                                                                                          resource          land                                                                      6.50E-04 m2a     estimation              1     1.58   (1,4,1,1,1,5);
                                                                                       of mining material: 2'000 kg/m3; mining                                                         site
[m2a]
                                                                                       depth: 50 m
land transformation                                                                    transformation = mining area; assumed
                                                                                                                                                                                       Transformation, to mineral
to mineral extraction   Î                                                              density: 2'000 kg/m3 of mining material;      resource       land                                                                      1.30E-05 m2      estimation              1     2.06   (1,4,1,1,1,5);
                                                                                                                                                                                       extraction site
site (mine) [m2]                                                                       mining depth: 50 m
                                                                                       transformation = mining area; assumed
land transformation
                        Î                                                              density: 2'000 kg/m3 of mining material;      resource       land                               Transformation, from unknown           1.30E-05 m2      estimation              1     2.06   (1,4,1,1,1,5);
mine from unknown
                                                                                       mining depth: 50 m
                                                                                                                                                                                                                                               After questionaire
                                                                                       total diesel consumption for in 2001: 601'000 construction                                      diesel, burned in building
diesel (mine)           Î                                                                                                                           machinery            No     GLO                                           6.97E-03 MJ      Palabora Mining         1     1.24   (1,4,1,1,1,5);
                                                                                       liter (=504'840 kg)                           processes                                         machine
                                                                                                                                                                                                                                               Company Ltd. (2002)
                                                                                       paraffin is used as heating fuel, yearly                                                                                                                After questionaire
heating - drying of                                                                                                                                                                    light fuel oil, burned in industrial
                       Î                                                               amount 2001: 450'000 liter, heating oil EL    oil            heating systems      No     RER                                           5.32E-03 MJ      Palabora Mining         1     2.06   (1,4,1,1,5,5);
feed material to plant                                                                                                                                                                 furnace 1MW, non-modulating
                                                                                       (used as proxy; 0.86 kg/l, 42.6 kg/MJ)                                                                                                                  Company Ltd. (2002)
                                                                                       includes crusher (0.1 kWh/ton crushed                                                                                                                   After questionaire
electricity                                                                                                                                                                            electricity, medium voltage,
                        Î                                                              material) and winnowing machine (0.0045       electricity    production mix       No    UCTE                                           1.05E-04 kWh     Palabora Mining         1     1.24   (1,4,1,1,1,5);
consumption                                                                                                                                                                            production UCTE, at grid
                                                                                       kWh/ton)                                                                                                                                                Company Ltd. (2002)
lubricating oil         Î                                                              amount copied from bentonite mining           chemicals      organics             No     RER    lubricating oil, at plant              8.06E-05 kg      Süd-Chemie (1999)       1     5.00   estimation
                                                                                                                                                                                                                                               After questionaire
                                                                                       Type of explosive used: HEF 100 Explosive;    construction
blasting                Î                                                                                                                           civil engineering    No     RER    blasting                               1.66E-04 kg      Palabora Mining         1     2.06   (1,4,1,1,5,5);
                                                                                       "Tovex" used as proxy                         processes
                                                                                                                                                                                                                                               Company Ltd. (2002)
                                                                                                                                                                                                                                               After questionaire
                                                                                       total production amount for the year 2001:    construction
vermiculite mine        Î                                                                                                                           additives            Yes    ZA     mine, vermiculite                      6.45E-12 unit    Palabora Mining         1     3.73   (1,4,1,1,5,5);
                                                                                       3'100'000 tons, assumed life time: 50 years   materials
                                                                                                                                                                                                                                               Company Ltd. (2002)



Fig. 6.1           Flows for “vermiculate, at mine” and their representation in the ecoinvent database




ecoinvent-report No. 7                                                                                                                                          - 11 -
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
