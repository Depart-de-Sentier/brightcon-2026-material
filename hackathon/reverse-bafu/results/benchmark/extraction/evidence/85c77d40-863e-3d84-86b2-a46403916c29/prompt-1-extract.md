You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Sanitary ceramics, at regional storage` [CH], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~27 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: ceramics / unspecified
- includedProcesses: gate to gate production of sanitary ceramics, including transports of raw materials to factory and of product to Switzerland
- technology: large scale production in Europe. Gas fired kiln
- generalComment: Data from one producer only. Composition of ceramic might differ from case to case. This dataset refers to oxidic ceramics.;
UUID: 85c77d40-863e-3d84-86b2-a46403916c29
- source cited in the metadata: Kellenberger D. | 2007 | 2007 - LCI building products - Kellenberger
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Ground Water: 0.0106 cubic meter (Resources Resources from water Renewable material resources from water)

## Report excerpt

Source file: `report-p207-209.txt` (SHA-256 08e496c3e938f457652d3a2db0843c519e8cf121bebcb06f3c9b8a434092fb5f), pages 207-209 of `2007 - LCI building products - Kellenberger.pdf`.

```
Part VI: Ceramics


Tab. 4.3   ecoinvent meta information for the ceramic production processes


                            sanitary ceramics, at            ceramic tiles, at regio-
Name                                                                                        ceramic plant
                            regional storage                 nal storage
Location                    CH                               CH                             CH
Infrastructure Process      0                                0                              1
Unit                        kg                               kg                             unit
DataSet Version             2.0                              2.0                            2.0
                            Gate to gate production of       Gate to gate production of
                                                                                            Includes land use and ma-
                            sanitary ceramics, includ-       ceramic tiles, including
                                                                                            terials used in buildings
Included Processes          ing transports of raw mate-      transports of raw materials
                                                                                            and machinery as well as
                            rials to factory and of prod-    to factory and of product to
                                                                                            their disposal
                            uct to Switzerland               Switzerland
Amount                      1                                1                              1
                            Sanitärkeramik, ab Re-           Keramikplatten, ab Re-
Local Name                                                                                  Keramikwerk
                            gionallager                      gionallager
                            China
Synonyms                                                     Steinzeug//stoneware
                            //Chinaware//Porzellan
                                                                                            Life time of 50 years for
                            Data from one producer           Data from one producer
                                                                                            buildings and of 25 years
                            only. Composition of ce-         only. Composition of ce-
General Comment to ref-                                                                     for machines is assumed.
                            ramic might differ from          ramic might differ from
erence function                                                                             Dataset refers to a factory
                            case to case. This dataset       case to case. This dataset
                                                                                            with yearly output of 5'000 t
                            refers to oxidic ceramics.       refers to oxidic ceramics.
                                                                                            of ceramic products.
StartDate                   1998                             1998                           2001
EndDate                     2002                             2002                           2002
Data Valid For Entire Pe-
                            1                                1                              1
riod
Other Period Text
                            Data from two factories of                                      Data from two factories of
Geography text                                               Data from Italy
                            one producer in Austria                                         one producer in Austria
                                                             Large scale, single fired
                            Large scale production in                                       Large scale production
Technology text                                              production in Europe. Gas
                            Europe. Gas fired kiln                                          plant in Europe.
                                                             fired kiln
Representativeness [%]
Production Volume           Unknown                          Unknown                        Unknown
Sampling Procedure          Environmental report             Publication                    Environmental report
Extrapolations              See Geography                    See Geography                  See Geography
Uncertainty Adjustments     None                             None                           None




ecoinvent report No. 7                                      -7-
                                                                                                                                                         Part VI: Ceramics



                                                                             General Flow information                                                                             Representation in ecoinvent                                             Uncertainty information
                                                                                                                                                                        Infra
                            Process                                                                                                                                              Loca                                                      Source mean          StDv      General
             Input                                                                       Output                   Remarks               Cate gory     Sub category      struc            Modul name in ecoinvent Mean value       Unit                   Type
                             Name                                                                                                                                                tion                                                         value             95%      Comment
                                                                                                                                                                        ture

                                                                                                                                      construction
      feldspar          Î                                                                           for ceramic mass                                 others                 No   RER    feldspar, at plant             3.79E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
                                                                                                                                      materials
      recycled
                                                                                                    for ceramic mass (from in-house
      production        Î                                                                                                                                                                                              8.97E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
                                                                                                    production)
      waste
      kaolin            Î   sanitary ceramics, at regional storage; inputs                          for ceramic mass                  chemicals      inorganics             No   RER    kaolin, at plant               4.08E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
                                                                                                                                      construction
      clay              Î                                                                           for ceramic mass                                 additives              No   CH     clay, at mine                  4.25E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
                                                                                                                                      materials
      silica meal,
                                                                                                                                      construction
      porcelain meal,   Î                                                                           for ceramic mass                                 additives              No    DE    silica sand, at plant          2.20E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
                                                                                                                                      materials
      refractories
      ancillary                                                                                                                                                                         chemicals inorganic, at
                        Î                                                                           for ceramic mass                  chemicals      inorganics             No   GLO                                   2.75E-03   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
      materials                                                                                                                                                                         plant
                                                                                                                                      construction
      oxydic minerals   Î                                                                           for glazing                                      additives              No    DE    silica sand, at plant          3.17E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
                                                                                                                                      materials
                                                                                                                                                                                        chemicals inorganic, at
      pigments          Î                                                                           for glazing                       chemicals      inorganics             No   GLO                                   2.87E-04   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
                                                                                                                                                                                        plant
      kaolin
      refractories,     Î                                                                           for glazing                       chemicals      inorganics             No   RER    kaolin, at plant               3.63E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
      silica meal
                                                                                                                                      construction
      gypsum            Î                                                                           for mould                                        binder                 No   CH     stucco, at plant               1.25E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,4)
                                                                                                                                      materials
                                                                                                                                                                                        polyethylene, HDPE,
      plastic forms     Î                                                                           for mould                         plastics       polymers               No   RER                                   1.51E-03   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,4)
                                                                                                                                                                                        granulate, at plant
                                                                                                                                                                                        natural gas, burned in
      natural gas       Î                                                                           for heating                       natural gas    heating systems        No   RER                                   2.41E+01   MJ     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,1)
                                                                                                                                                                                        industrial furnace >100kW
                                                                                                                                                                                        electricity, medium voltage,
      electricity       Î                                                                           total consumption                 electricity    production mix         No   UCTE                                  8.78E-01   kWh    ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,2)
                                                                                                                                                                                        production UCTE, at grid
      well water        Î                                                                           total consumption                 resource       in water                           Water, well, in ground         1.06E-02   m3     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,4)
      tap water         Î                                                                           total consumption                 water supply production               No   RER    tap water, at user             5.41E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,4)

                                                                                                    of final product to Switzerland: transport                                                                                                                         (4,5,n.A.,n.A.,
      transport         Î                                                                                                                            train                  No   CH     transport, freight, rail       6.00E-01   tkm    estimated        1     2.09
                                                                                                    600 km assumed                   systems                                                                                                                           n.A.,n.A.,5)
                                                                                                    of raw materials to fabrication: transport                                          transport, lorry >16t, fleet                                                   (4,5,n.A.,n.A.,
      transport         Î                                                                                                                            road                   No   RER                                   8.14E-02   tkm    estimated        1     2.09
                                                                                                    50 km assumed                    systems                                            average                                                                        n.A.,n.A.,5)
                                                                                                    Life time: 50 a; production      construction
      infrastructure    Î                                                                                                                            others             Yes      CH     ceramic plant                  4.00E-09   unit   ÖSPAG (2002)     1     3.02   (1,3,1,3,1,4,9)
                                                                                                    volume: 5000000 kg/a             materials


Fig. 4.1       Flows for "sanitary ceramics, at regional storage" and its representation in the ecoinvent database




ecoinvent report No. 7                                                                                                                                                -8-
                                                                                                                                                                 Part VI: Ceramics


                                                                                   General Flow information                                                                               Representation in ecoinvent                                              Uncertainty information
                                                                                                                                                                                 Infra
                         Process                                                                                                                                                          Loca                                                      Source mean          StDv      General
           Input                                                                               Output                   Remarks                  Cate gory     Sub category      struc            Modul name in ecoinvent Mean value       Unit                   Type
                          Name                                                                                                                                                            tion                                                         value             95%      Comment
                                                                                                                                                                                 ture

                                                                                        waste ceramic        internally recycled (substitutes
                                                                                      Î                                                                                                                                         8.97E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)




                         sanitary ceramics, at regional storage; outputs, part 1
                                                                                        (not sanded)         feldspar)
                                                                                      Î paper                recycled                                                                                                           7.59E-03   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                          waste ceramic      contamination from sanding.        waste                                            disposal, inert material, 0%
                                                                                      Î                                                                    sanitary landfill         No   CH                                    9.40E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                          (sanded)           Cannot be recycled                 management                                       water, to sanitary landfill

                                                                                                                                                waste                                            disposal, inert material, 0%
                                                                                      Î rumble                                                             sanitary landfill         No   CH                                    3.19E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                                                                                management                                       water, to sanitary landfill
                                                                                                                                                                                                 disposal, inert waste, 5%
                                                                                          filter material                                       waste      inert material
                                                                                      Î                                                                                              No   CH     water, to inert material       1.64E-03   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                          (inert)                                               management landfill
                                                                                                                                                                                                 landfill
                                                                                      Î gypsum               recycled in cement plants                                                                                          1.33E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                      Î clay suspension      recycled in brick fabrication                                                                                      1.85E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                                                                                                                                 disposal, municipal solid
                                                                                                                                                waste      municipal
                                                                                      Î municipal waste                                                                              No   CH     waste, 22.9% water, to         3.86E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                                                                                management incineration
                                                                                                                                                                                                 municipal incineration
                                                                                                                                                                                                 disposal, hazardous waste,
                                                                                          metal containers                                      waste      underground
                                                                                      Î                                                                                              No   DE     0% water, to underground       6.85E-05   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                          (soiled)                                              management deposit
                                                                                                                                                                                                 deposit
                                                                                      Î refrigerators        neglected (for consistency                                                                                         5.49E-05   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                      Î lead batteries       neglected (for consistency                                                                                         2.97E-04   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                        fluorescent
                                                                                      Î                      neglected (for consistency                                                                                         2.06E-05   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                        lamps
                                                                                                                                                                                                 disposal, solvents mixture,
                                                                                          developing                                            waste      hazardous waste
                                                                                      Î                                                                                              No   CH     16.5% water, to hazardous      2.39E-06   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                          agent                                                 management incineration
                                                                                                                                                                                                 waste incineration
                                                                                                                                                                                                 disposal, used mineral oil,
                                                                                                                                                waste      hazardous waste
                                                                                      Î used oil                                                                                     No   CH     10% water, to hazardous        1.88E-04   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                                                                                management incineration
                                                                                                                                                                                                 waste incineration
                                                                                                                                                                                                 disposal, used mineral oil,
                                                                                                                                                waste      hazardous waste
                                                                                      Î fat                                                                                          No   CH     10% water, to hazardous        1.58E-06   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                                                                                management incineration
                                                                                                                                                                                                 waste incineration
                                                                                                                                                                                                 disposal, bilge oil, 90%
                                                                                          oil-water                                             waste      hazardous waste
                                                                                      Î                                                                                              No   CH     water, to hazardous waste      6.61E-05   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
                                                                                          mixtures                                              management incineration
                                                                                                                                                                                                 incineration


Fig. 4.1    Flows for "sanitary ceramics, at regional storage" and its representation in the ecoinvent database (cont.)




ecoinvent report No. 7                                                                                                                                                         -9-
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
