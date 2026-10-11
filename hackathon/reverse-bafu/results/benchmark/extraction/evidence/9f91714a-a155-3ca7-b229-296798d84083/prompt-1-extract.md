You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Concrete pile, 880mm, piped, Integra L2 Wallisellen` [CH], reference unit 1 m, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~6 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: construction processes / civil engineering
- includedProcesses: This data set includes the material use of deep foundation.
- technology: none
- generalComment: Ortbetonpfähle  d = 880 mm, Verrohrt,Pfahllänge 29 m Integra L2, Wallisellen;
UUID: 9f91714a-a155-3ca7-b229-296798d84083
- source cited in the metadata: Frischknecht R. | 2014 | 2014 - LCA civil eng. works in building const. - Frischknecht
- time period: 2014-01-2014-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 m):
- none

## Report excerpt

Source file: `report-p37-39.txt` (SHA-256 cb275e41d48bac34aab0fe1a5100117aa0e7494e3cde18ac8bb37dd5a9599a4a), pages 37-39 of `2014 - LCA civil eng. works in building const. - Frischknecht.pdf`.

```
Sachbilanzdaten                                                                                                     26




6.3.5 Ortbetonbohrpfähle
Es werden sechs unterschiedliche Ortbetonbohrpfähle mit unterschiedlichen
Durchmessern bilanziert. Tab. 6.17 zeigt eine Übersicht und einen kurzen Beschrieb mit
den wichtigsten Kennzahlen der bilanzierten Ortbetonbohrpfähle.
Tab. 6.17 Übersicht und Beschrieb der bilanzierten Ortbetonbohrpfähle; AVG: Durchschnitt

Bezeichnung                        Gebäude            Durchmesser     Länge in    Zementgehalt       Armierungs-
                                                      in mm           m           in kg/m3           gehalt in kg/m3
Ortbetonbohrpfähle, 700 mm         Alterssiedlung     720             10          320                58
                                   Seefeldstrasse,
                                   Zürich
Ortbetonbohrpfähle, 900 mm         Alterssiedlung     900             10          333                60
                                   Seefeldstrasse,
                                   Zürich
Ortbetonbohrpfähle, 700 mm         Integra L2,        700             29          300                42
                                   Wallisellen
Ortbetonbohrpfähle, 900 mm         Integra L2,        880             29          355                27
                                   Wallisellen
Ortbetonbohrpfähle, 900 mm         Integra L2,        900             29          346                97
                                   Wallisellen
Ortbetonbohrpfähle, 1200 mm        Integra L2,        1200            29          350                50
                                   Wallisellen
Ortbetonbohrpfähle, 700 mm         Durchschnitt       AVG             AVG         AVG                561)

Ortbetonbohrpfähle, 900 mm         Durchschnitt       AVG             AVG         AVG                561)

Ortbetonbohrpfähle, 1200 mm        Durchschnitt       AVG             AVG         AVG                561)

           1)     Entspricht dem durchschnittlichen Armierungsgehalt der Ortbetonpfähle aller Durchmesser



Die Ortbetonbohrpfähle haben einen Durchmesser zwischen 700 und 1200 mm, eine
Längen zwischen 10 und 29 m, einen Zementgehalt zwischen 300 und 355 kg/m3 Beton
und einen Armierungsgehalt zwischen knapp 30 und knapp 100 kg/m3. Je nach
Zementgehalt des Betons wird ein anderer Datensatz für die Modellierung verwendet.
Die Ortbetonbohrpfähle mit einem durchschnittlichen Zementgehalt von ca. 300 kg/m3
und diese mit einem überdurchschnittlichen Zementgehalt von mehr als 340 kg/m3
werden mit den durchschnittlichen Schweizer Datensätzen für Tiefbaubeton und
Bohrpfahlbeton modelliert.
Der Treibstoffverbrauch für das Bohren wird entsprechend der Angaben für die
Bohrung von Rühl- und Bohrpfahlwänden abgeschätzt (siehe Abschnitt 6.2.3 und
6.2.4).
Tab. 6.18 zeigt die Sachbilanzdaten der bilanzierten Ortbetonbohrpfähle pro m Pfahl.




Ökobilanzen von Tiefbauarbeiten bei Hochbauten                                                        treeze Ltd.
Sachbilanzdaten                                                                                                                                                                                                                                                                                              27




Tab. 6.18 Sachbilanzdaten zur Herstellung der bilanzierten Ortbetonbohrpfähle pro m Pfahl




                                                                                                                                                                                                                                            StandardDeviation9
                                                                                           InfrastructureProces




                                                                                                                                                                                                        UncertaintyType
                                                                                                                           bored concrete       bored concrete
                                                                                                                            pile, 720mm,         pile, 900mm,      concrete pile,      concrete pile,




                                                                       Location
                                                                                                                                piped,               piped,       700mm, piped,       880mm, piped,




                                                                                                                   Unit




                                                                                                                                                                                                                                                   5%
                                     Name                                                                                                                                                                                                                               GeneralComment
                                                                                                                           Alterssiedlung       Alterssiedlung      Integra L2          Integra L2
                                                                                                                           Seefeldstrasse       Seefeldstrasse      Wallisellen         Wallisellen
                                                                                                                                Zürich               Zürich

                                 Location                                                                                       CH                   CH                CH                  CH
                      InfrastructureProcess                                                                                      0                    0                 0                   0
                                Unit                                                                                             m                    m                 m                   m
            bored concrete pile, 720mm, piped,
product                                                           CH                          0                    m             1                    0                 0                   0
            Alterssiedlung Seefeldstrasse Zürich
            bored concrete pile, 900mm, piped,
                                                                  CH                          0                    m             0                    1                 0                   0
            Alterssiedlung Seefeldstrasse Zürich
            concrete pile, 700mm, piped, Integra L2
                                                                  CH                          0                    m             0                    0                 1                   0
            Wallisellen
            concrete pile, 880mm, piped, Integra L2
                                                                  CH                          0                    m             0                    0                 0                   1
            Wallisellen
                                                                                                                                                                                                                                                                        (3,3,1,3,1,4,BU:1.05); company data;
            reinforcing steel, secondary production,
                                                                  CH                          0                    kg          2.90E+1             4.50E+1           2.10E+1             2.10E+1            1                                 1.16                      APT Ingenieure 2014, pers.
            (100% Rec.)
                                                                                                                                                                                                                                                                        communication Andreas Lutz
            concrete, concrete for underground                                                                                                                                                                                                                          (3,3,1,3,1,4,BU:1.05); company data;
            construction, average cement                          CH                          0                    kg          1.20E+3             1.80E+3           1.20E+3                0               1                                 1.16                      APT Ingenieure 2014, pers.
            Switzerland, at plant                                                                                                                                                                                                                                       communication Andreas Lutz
                                                                                                                                                                                                                                                                        (3,3,1,3,1,4,BU:1.05); company data;
            concrete, concrete for drilled piles,
                                                                  CH                          0                    kg            0                    0                 0                1.82E+3            1                                 1.16                      APT Ingenieure 2014, pers.
            average cement Switzerland, at plant
                                                                                                                                                                                                                                                                        communication Andreas Lutz
                                                                                                                                                                                                                                                                        (3,3,1,3,1,4,BU:1.05); company data;
            diesel, burned in building machine                  GLO                           0                    MJ          2.43E+2             2.13E+2           2.43E+2             2.13E+2            1                                 1.16                      Marti AG, 2014, pers. communication
                                                                                                                                                                                                                                                                        Roger Hartmann
                                                                                                                                                                                                                                                                        (3,3,1,3,1,4,BU:2); 20 km for
            transport, lorry >28t, fleet average                  CH                          0                   tkm          2.55E+1             3.83E+1           2.51E+1             3.75E+1            1                                 2.03                      concrete, 50 km for steel; standard
                                                                                                                                                                                                                                                                        distances ecoinvent v2.2

                                                                                                                                                                                                                                                                        (3,3,1,3,1,4,BU:2); 600 km for steel;
            transport, freight, rail                              CH                          0                   tkm          1.74E+1             2.70E+1           1.26E+1             1.26E+1            1                                 2.03
                                                                                                                                                                                                                                                                        standard distances ecoinvent v2.2




Tab. 6.18 Sachbilanzdaten zur Herstellung der bilanzierten Ortbetonbohrpfähle pro m Pfahl (Fortset-
          zung)
                                                                                                                                                                                                                                                   StandardDeviation9
                                                                InfrastructureProces




                                                                                                                                                                                                                          UncertaintyType




                                                                                                                   concrete pile, concrete pile,
                                                     Location




                                                                                                                                                  concrete pile,        concrete pile, concrete pile,
                                                                                                                  900mm, piped, 1200mm, piped,
                                                                                       Unit




                                                                                                                                                                                                                                                          5%




                              Name                                                                                                               700mm, piped,         900mm, piped, 1200mm, piped,                                                                      GeneralComment
                                                                                                                    Integra L2     Integra L2
                                                                                                                                                    average               average        average
                                                                                                                    Wallisellen    Wallisellen



                             Location                                                                                     CH              CH                 CH              CH                 CH
                    InfrastructureProcess                                                                                 0                0                 0                0                 0
                              Unit                                                                                        m                m                 m                m                 m
          concrete pile, 900mm, piped, Integra L2
                                                     CH            0                   m                                  1                 0                0                 0                0
          Wallisellen
          concrete pile, 1200mm, piped, Integra L2
                                                     CH            0                   m                                  0                 1                0                 0                0
          Wallisellen
          concrete pile, 700mm, piped, average       CH            0                   m                                  0                 0                1                 0                0
          concrete pile, 900mm, piped, average       CH            0                   m                                  0                 0                0                 1                0
          concrete pile, 1200mm, piped, average      CH            0                   m                                  0                 0                0                 0                1
                                                                                                                                                                                                                                                                         (3,3,1,3,1,4,BU:1.05); company data;
          reinforcing steel, secondary production,
                                                     CH            0                   kg                            7.60E+1             6.00E+1          2.79E+1           4.26E+1          6.70E+1                          1                      1.16                APT Ingenieure 2014, pers.
          (100% Rec.)
                                                                                                                                                                                                                                                                         communication Andreas Lutz
          concrete, concrete for underground                                                                                                                                                                                                                             (3,3,1,3,1,4,BU:1.05); company data;
          construction, average cement               CH            0                   kg                                 0                 0             1.20E+3           6.00E+2             0                             1                      1.16                APT Ingenieure 2014, pers.
          Switzerland, at plant                                                                                                                                                                                                                                          communication Andreas Lutz
                                                                                                                                                                                                                                                                         (3,3,1,3,1,4,BU:1.05); company data;
          concrete, concrete for drilled piles,
                                                     CH            0                   kg                            1.87E+3             2.88E+3             0              1.23E+3          2.88E+3                          1                      1.16                APT Ingenieure 2014, pers.
          average cement Switzerland, at plant
                                                                                                                                                                                                                                                                         communication Andreas Lutz
                                                                                                                                                                                                                                                                         (3,3,1,3,1,4,BU:1.05); company data;
          diesel, burned in building machine         GLO           0                   MJ                            2.13E+2             2.13E+2          2.43E+2           2.13E+2          2.13E+2                          1                      1.16                Marti AG, 2014, pers. communication
                                                                                                                                                                                                                                                                         Roger Hartmann
                                                                                                                                                                                                                                                                         (3,3,1,3,1,4,BU:2); 20 km for concrete,
          transport, lorry >28t, fleet average       CH            0                   tkm                           4.12E+1             6.06E+1          2.54E+1           3.88E+1          6.10E+1                          1                      2.03                50 km for steel; standard distances
                                                                                                                                                                                                                                                                         ecoinvent v2.2

                                                                                                                                                                                                                                                                         (3,3,1,3,1,4,BU:2); 600 km for steel;
          transport, freight, rail                   CH            0                   tkm                           4.56E+1             3.60E+1          1.68E+1           2.56E+1          4.02E+1                          1                      2.03
                                                                                                                                                                                                                                                                         standard distances ecoinvent v2.2




6.3.6 Ortbetonverdrängungspfähle
Es werden vier unterschiedliche Ortbetonverdrängungspfähle bilanziert mit zwei
verschiedenen Durchmessern und unterschiedlichen Armierungsgehalten. Tab. 6.19




Ökobilanzen von Tiefbauarbeiten bei Hochbauten                                                                                                                                                                                                                                       treeze Ltd.
Sachbilanzdaten                                                                                          28




zeigt eine Übersicht der bilanzierten Ortbetonverdrängungspfähle mit den wichtigsten
Kennzahlen.
Tab. 6.19 Übersicht und Beschrieb der bilanzierten Ortbetonverdrängungspfähle; AVG: Durchschnitt

Bezeichnung                   Gebäude            Durchmesser   Länge /    Zement-     Armierungsgehalt
                                                 in mm         Tiefe in   gehalt in   in kg/m3
                                                               m          kg/m3
Ortbetonverdrängungspfähle,   Integra Wohnen,    660/580       23         350         155
660 / 580                     Wallisellen
Ortbetonverdrängungspfähle,   Integra Wohnen,    660/580       23         350         95
660 / 580                     Wallisellen
Ortbetonverdrängungspfähle,   Durchschnitt       AVG           AVG        AVG         AVG
660 / 580
Ortbetonverdrängungspfähle,   Integra Wohnen,    560/480       23         357         179
560 / 480 mm                  Wallisellen
Ortbetonverdrängungspfähle,   Integra Wohnen,    560/480       23         357         100
560 / 480 mm                  Wallisellen
Ortbetonverdrängungspfähle,   Durchschnitt       AVG           AVG        AVG         AVG
560 / 480 mm



Für Ortbetonverdrängungspfähle wird Beton mit einem hohen Zementgehalt von mehr
als 350 kg pro m3 verwendet. Entsprechend wird der Betonverbrauch mit dem
durchschnittlichen Schweizer Datensatz für Bohrpfahlbeton modelliert. Dieser
entspricht einem Beton für hohe Anforderungen mit einem hohen Zementgehalt.
Die bilanzierten Ortbetonverdrängungspfähle sind 23 m lang.
Der Armierungsgehalt der Ortbetonverdrängungspfähle variiert zwischen 95 und
179 kg/m3.
Der Treibstoffverbrauch wird entsprechend der Angaben für die Bohrung von Rühl- und
Bohrpfahlwand abgeschätzt (siehe Abschnitt 6.2.3 und 6.2.4) und beträgt somit 6.8 Liter
pro m Verdrängungspfahl.
Tab. 6.20 zeigt die Sachbilanzdaten der bilanzierten Ortbetonverdrängungspfähle pro m
Pfahl.




Ökobilanzen von Tiefbauarbeiten bei Hochbauten                                             treeze Ltd.
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 m.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
