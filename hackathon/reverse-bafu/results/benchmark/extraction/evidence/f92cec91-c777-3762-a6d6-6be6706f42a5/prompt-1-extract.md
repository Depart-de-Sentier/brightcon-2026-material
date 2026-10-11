You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Yarn, cotton, at plant` [GLO], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~5 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: textiles / unspecified
- includedProcesses: The inventories only put together the cotton production and the yarn production
- technology: Avarage data for yarn production are considered
- generalComment: Inventory refers to 1 kg yarn produced from cotton lint;
UUID: f92cec91-c777-3762-a6d6-6be6706f42a5
- source cited in the metadata: Althaus H.-J. | 2007 | 2007 - LCI renewable materials - Althaus
- time period: 1995-01-1999-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p88-90.txt` (SHA-256 20572eb7d4ee281758a99a0ddee69197b766d17a28bc11962d06e3da6dd40d51), pages 88-90 of `2007 - LCI renewable materials - Althaus.pdf`.

```
Part I: Life Cycle Inventories of Renewable Fibres


Tab. 2.2        Unit process of ‘yarn production, cotton fibres’




                                                                                                                                                                  Standard Deviation
                                                                                                                                               UncertaintyType
                                                                            Location
                                                                                                         yarn production,




                                                                                                                                                                        95%
                                                                                              Unit
                                            Name                                                                                                                                       GeneralComment
                                                                                                           cotton fibres



                                         Location                                                               GLO
                                  InfrastructureProcess                                                           0
                                           Unit                                                                  kg
                             yarn production, cotton
product                                                              GLO                      kg                  1
                             fibres

                             electricity, low voltage, at                                                                                                                              (2,2,3,1,1,4); Öko-Institut, Baumwoll Datendokumentation
technosphere                                                            CN                    kWh              5.10E+0                           1                1.16
                             grid                                                                                                                                                      (Wiegmann K., 2002)

                             electricity, low voltage, at                                                                                                                              (2,2,3,1,1,5); Öko-Institut, Baumwoll Datendokumentation
technosphere                                                            US                    kWh              3.40E+0                           1                1.24
                             grid                                                                                                                                                      (Wiegmann K., 2002)


emission air, unspecified    Heat, waste                                      -               MJ               3.06E+1                           1                1.24                 (2,2,3,1,1,5); Heat waste derived from electricity consumption



                                                                                                                                                                                       (2,2,3,3,1,4); Distance from report Öko-Institut, Baumwoll
                             transport, lorry 16-32t,
technosphere                                                        RER                       tkm              4.50E-1                           1                2.03                 Datendokumentation (Wiegmann K., 2002). Assumption
                             EURO3
                                                                                                                                                                                       vehicle type Carbotech AG



                                                                                                                                                                                       (5,1,1,3,4,5); Estimation infrastructure comparable to
                             packaging box production                                                                                                                                  packaging plant (buidling, equipment, electronics).
technosphere                                                        RER                       unit             1.00E-9                           1                3.50
                             unit                                                                                                                                                      Assumption life time 50 years with output of 20' 000 t of yarn
                                                                                                                                                                                       per year. Totally max. 5% of impacts.




Tab. 2.3        Unit process of ‘weaving, cotton’
                                                                                                                                           Standard Deviation
                                                                                                                         UncertaintyType
                                                                 Location




                                                                                                                                                 95%
                                                                                       Unit




                                      Name                                                           weeving, cotton                                             GeneralComment




                                    Location                                                              GLO
                             InfrastructureProcess                                                         0
                                      Unit                                                                 kg

product           weeving, cotton                               GLO                    kg                  1


technosphere      electricity, low voltage, at grid             CN                     kWh              7.08E+0            1               1.16                  (2,2,3,1,1,4); Öko-Institut, Baumwoll Datendokumentation (Wiegmann K., 2002)



                  electricity, low voltage, production RER,                                                                                                      (2,2,3,1,1,5); Öko-Institut, Baumwoll Datendokumentation (Wiegmann K., 2002),
technosphere                                                    RER                    kWh              3.03E+0            1               1.24
                  at grid                                                                                                                                        Czech Republic electricity mix considered representing GUS.



emission air,
                  Heat, waste                                      -                   MJ               3.64E+1            1               1.24                  (2,2,3,1,1,5); Heat waste derived from electricity consumption
unspecified



                                                                                                                                                                 (2,2,3,3,1,4); Assumption Carbotech AG, all cotton at least transport of about 250
technosphere      transport, lorry 16-32t, EURO3                RER                    tkm              3.50E-1           1                2.03                  km to next factory or harbour for shipping to China/Eastern Europe. Distance
                                                                                                                                                                 oversea transport counted twice as in ecoinvent guidelines


                                                                                                                                                                 (2,2,3,3,1,4); Assumption Öko-Institut Baumwoll Datendokumentation (Wiegmann
technosphere      transport, transoceanic freight ship          OCE                    tkm              4.80E+0            1               2.03                  K., 2002). USA 40% of production for processing transport of 10% to China and
                                                                                                                                                                 30% to Eastern Europe, Assumption average distance 12'000 km by Carbotech AG


                                                                                                                                                                 (5,1,1,3,4,5); Estimation infrastructure comparable to packaging plant (buidling,
technosphere      packaging box production unit                 RER                    unit             1.00E-9           1                3.50                  equipment, electronics). Assumption life time 50 years with an output of 20' 000 t of
                                                                                                                                                                 yarn per year. Totally max. 5% of impacts.




ecoinvent-report No. 21                                                                                           - 10 -
                                                                   Part I: Life Cycle Inventories of Renewable Fibres


Tab. 2.4           Unit process of ‘‘textile refinement, cotton’




                                                                                                                                          UncertaintyType



                                                                                                                                                                              Deviation 95%
                                                                                  Infrastructure




                                                                                                                                                                                Standard
                                                                       Location




                                                                                     Process
                                                                                                                    textile refinement,




                                                                                                          Unit
                                              Name                                                                                                                                                    GeneralComment
                                                                                                                           cotton



                                             Location                                                                     GLO
                                      InfrastructureProcess                                                                0
                                               Unit                                                                        kg
product                     textile refinement, cotton                 GLO             0                  kg                1
                                                                                                                                                                                                      (2,3,3,1,1,5); Öko-Institut, Baumwoll Datendokumentation (Wiegmann
technosphere                electricity, low voltage, at grid          CN              0                  kWh            7.76E-1            1                                 1.25
                                                                                                                                                                                                      K., 2002)
                            electricity, low voltage, production IT,                                                                                                                                  (2,3,3,1,1,5); Öko-Institut, Baumwoll Datendokumentation (Wiegmann
                                                                       IT              0                  kWh            3.33E-1            1                                 1.25
                            at grid                                                                                                                                                                   K., 2002)
emission air, unspecified   Heat, waste                                  -             -                  MJ             3.99E+0            1                                 1.25                    (2,3,3,1,1,5); Heat waste derived from electricity consumption

                            heat, light fuel oil, at industrial                                                                                                                                       (2,3,3,1,1,5); Öko-Institut, Baumwoll Datendokumentation (Wiegmann
technosphere                                                           RER             0                  MJ             3.05E+1            1                                 1.25
                            furnace 1MW                                                                                                                                                               K., 2002). China heat production from 100% oil and Italy 50%

                            heat, natural gas, at industrial                                                                                                                                          (2,3,3,1,1,5); Öko-Institut, Baumwoll Datendokumentation (Wiegmann
                                                                       RER             0                  MJ             5.39E+0            1                                 1.25
                            furnace >100kW                                                                                                                                                            K., 2002). Italy heat production from 50% gas

                                                                                                                                                                                                      (2,3,3,1,1,5); Transport distance from to Italy between processing steps
                            transport, lorry >16t, fleet average       RER             0                  tkm            2.50E-1            1                                 2.07
                                                                                                                                                                                                      from Öko-Institut, Baumwoll Datendokumentation (Wiegmann K., 2002)


                                                                                                                                                                                                      (2,3,3,1,1,5); Öko-Institut, Baumwoll Datendokumentation (Wiegmann
                            tap water, at user                         RER             0                  kg             1.38E+2            1                                 1.25
                                                                                                                                                                                                      K., 2002)

                                                                                                                                                                                                      (2,3,3,1,1,5); Öko-Institut, Baumwoll Datendokumentation (Wiegmann
                            sodium chloride, powder, at plant          RER             0                  kg             5.47E-1            1                                 1.25
                                                                                                                                                                                                      K., 2002)


                                                                                                                                                                                                      (2,3,3,1,1,5); Amount of auxiliaries from Öko-Institut, Baumwoll
                            chemicals organic, at plant                GLO             0                  kg             1.30E-1            1                                 1.25                    Datendokumentation (Wiegmann K., 2002). Assumption Carbotech AG
                                                                                                                                                                                                      regarding mixture about 120 g organic compounds for dyeing

                                                                                                                                                                                                      (2,3,3,1,1,5); Amount of auxiliaries from Öko-Institut, Baumwoll
                            fatty alcohol sulfonate, mix, at plant     RER             0                  kg             1.00E-2            1                                 1.25                    Datendokumentation (Wiegmann K., 2002). Assumption Carbotech AG
                                                                                                                                                                                                      regarding mixture about 10 g washing agent
                                                                                                                                                                                                      (2,3,3,1,1,5); Amount of auxiliaries from Öko-Institut, Baumwoll
                            sodium perborate, tetrahydrate,
                                                                       RER             0                  kg             1.00E-2            1                                 1.25                    Datendokumentation (Wiegmann K., 2002). Assumption Carbotech AG
                            powder, at plant
                                                                                                                                                                                                      regarding mixture about 10 g bleaching agent

                                                                                                                                                                                                      (2,3,3,1,1,5); Amount of auxiliaries from Öko-Institut, Baumwoll
                            alkylbenzene sulfonate, linear,
                                                                       RER             0                  kg             1.00E-2            1                                 1.25                    Datendokumentation (Wiegmann K., 2002). Assumption Carbotech AG
                            petrochemical, at plant
                                                                                                                                                                                                      regarding mixture about 10 g finishing agent

                                                                                                                                                                                                      (2,3,3,1,1,5); Amount of auxiliaries from Öko-Institut, Baumwoll
                            carboxymethyl cellulose, powder, at
                                                                       RER             0                  kg             1.00E-2            1                                 1.25                    Datendokumentation (Wiegmann K., 2002). Assumption Carbotech AG
                            plant
                                                                                                                                                                                                      regarding mixture about 10 g finishing agent

                                                                                                                                                                                                      (5,3,3,1,4,5); Estimation infrastructure comparable to small sized
                                                                                                                                                                                                      chemical plant (10% of buidling, equipment). Assumption life time 50
                            chemical plant, organics                   RER             1                  unit          1.00E-10            1                                 3.52
                                                                                                                                                                                                      years with about 20' 000 t of refined yarn or textile per year. Totally max
                                                                                                                                                                                                      5% of impacts.
                            treatment, sewage, to wastewater                                                                                                                                          (5,3,3,1,4,5); Assumptions Carbotech AG, total water consumption in
                                                                       CH              0                  m3             1.38E-1            1                                 1.85
                            treatment, class 5                                                                                                                                                        waste water treatment.




Tab. 2.5           Unit process of ‘yarn, cotton, at plant’
                                                                                                                                                                                          Standard Deviation
                                                                                                                                                            UncertaintyType
                                                                                               Location




                                                                                                                       yarn, cotton, at
                                                                                                                                                                                                95%
                                                                                                             Unit




                                                       Name                                                                                                                                                    GeneralComment
                                                                                                                            plant



                                                   Location                                                                  GLO
                                            InfrastructureProcess                                                              0
                                                     Unit                                                                     kg

product                       yarn, cotton, at plant                                       GLO               kg                 1

                                                                                                                                                                                                               (2,2,3,1,1,4); Öko-Institut, Baumwoll
technosphere                  cotton fibres, ginned, at farm                                CN               kg            6.60E-1                            1                           1.16                 Datendokumentation (Wiegmann K., 2002),
                                                                                                                                                                                                               assumption 10% fibres loss
                                                                                                                                                                                                               (2,2,3,1,1,4); Öko-Institut, Baumwoll
technosphere                  cotton fibres, at farm                                         US              kg            4.40E-1                            1                           1.16                 Datendokumentation (Wiegmann K., 2002),
                                                                                                                                                                                                               assumption 10% fibres loss

                                                                                                                                                                                                               (2,2,3,3,1,4); Öko-Institut, Baumwoll
technosphere                  yarn production, cotton fibres                               GLO               kg            1.00E+0                            1                           1.17                 Datendokumentation (Wiegmann K., 2002),
                                                                                                                                                                                                               assumption 10% fibres loss


                              disposal, paper, 11.2% water, to sanitary
technosphere                                                                                CH               kg            1.00E-1                            1                           1.17                 (2,2,3,3,1,4); the fibre residues goes to landfill
                              landfill




ecoinvent-report No. 21                                                                                             - 11 -
                                                   Part I: Life Cycle Inventories of Renewable Fibres


Tab. 2.6       Unit process of ‘textile, woven cotton, at plant’




                                                                                                                    Standard Deviation
                                                                                                  UncertaintyType
                                                             Location
                                                                                textile, woven




                                                                                                                          95%
                                                                        Unit
                                        Name                                                                                             GeneralComment
                                                                               cotton, at plant



                                      Location                                      GLO
                               InfrastructureProcess                                  0
                                        Unit                                         kg

product               textile, woven cotton, at plant       GLO         kg            1

                                                                                                                                         (2,2,3,3,1,4); Öko-Institut, Baumwoll Datendokumentation
technosphere          yarn, cotton, at plant                GLO         kg        1.02E+0           1               1.17
                                                                                                                                         (Wiegmann K., 2002)

                                                                                                                                         (2,2,3,3,1,4); Öko-Institut, Baumwoll Datendokumentation
                      weeving, cotton                       GLO         kg        1.00E+0           1               1.17
                                                                                                                                         (Wiegmann K., 2002)

                      disposal, paper, 11.2% water, to
                                                             CH         kg        2.00E-2           1               1.17                 (2,2,3,3,1,4); the fibre residues goes to landfill
                      sanitary landfill




2.5            Data Quality Considerations
Tab. 2.2 to Tab. 2.6 show the standard deviation for the inventory of cotton processing and resulting
products yarn and textiles. The simplified approach with a pedigree matrix has been used for calculat-
ing the standard deviation. The inventory is based on published data and completed by assumptions
for infrastructure, transport distances and waste water treatment. Nevertheless in general the data qual-
ity is quite reliable.




ecoinvent-report No. 21                                                        - 12 -
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
