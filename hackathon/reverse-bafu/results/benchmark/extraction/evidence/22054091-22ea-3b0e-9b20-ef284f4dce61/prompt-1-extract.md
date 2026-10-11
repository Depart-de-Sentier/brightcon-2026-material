You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Bored pile wall, overlapped, strutted apart, Alterssiedlung Seefeldstrasse Zürich` [CH], reference unit 1 m2, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~9 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: construction processes / civil engineering
- includedProcesses: This data set includes the material use of construction pit supporting structures.
- technology: none
- generalComment: überschnittene Borhpfahlwand, Pfahldurchmesser 720 mm, jeder zweite Pfahl bewehrt, einfach gespriesst, Pfahllängen 10 bis 14 m, tragende Pfähle 21 m, Höhe 3.05 m,: SpriessungEinbau/Rückbau diverse Profile;
UUID: 22054091-22ea-3b0e-9b20-ef284f4dce61
- source cited in the metadata: Frischknecht R. | 2014 | 2014 - LCA civil eng. works in building const. - Frischknecht
- time period: 2014-01-2014-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 m2):
- Gravel, resource correction: -1903 kilogram (resources in ground)
- Sand, resource correction: -1070 kilogram (resources in ground)

## Report excerpt

Source file: `report-p29-30.txt` (SHA-256 9c8ce0c904c02ff503f9890589da87ed2c5ec612fcde63b3aa2df633435240ac), pages 29-30 of `2014 - LCA civil eng. works in building const. - Frischknecht.pdf`.

```
Sachbilanzdaten                                                                                                   18




Tab. 6.5 Übersicht und Beschrieb der bilanzierten Bohrpfahlwände; d = Durchmesser der Bohrung, L =
         Länge des Bohrpfahls, T = Tiefe der Baugrube, n.a. = keine Angabe

Bezeichnung          Gebäude              Beschrieb
überschnittene       Altersiedlung        überschnittene Bohrpfahlwand, gespriesst: d = 720 mm, L = 10 bis 21 m,
Bohrpfahlwand,       Seefeldstrasse,      T = 3.05 m, Überschneidung = 20 %, Zementgehalt = 351 kg/m3 /
gespriesst           Zürich               Spriessung: diverse Profile / Verankerung: keine
überschnittene       Stadtspital          überschnittene Bohrpfahlwand, verankert: d = 750 mm, L = 9 bis 22.5
Bohrpfahlwand,       Triemli              m, T = 7.73 bis 8.73m, Überschneidung = 20 % , Zementgehalt =
verankert                                 315 kg/m3 / Spriessung: keine / Longarine: diverse Profile /
                                          Verankerung: vierfach
überschnittene       Durchschnitt         basierend auf überschnittener Bohrpfahlwand, gespriesst
Bohrpfahlwand,
unverankert



Die Bohrpfähle der gespriessten Bohrpfahlwand haben einen Durchmesser von 720 mm
und eine Länge von 10 bis 21 m für eine Baugrube mit einer Tiefe von 3.05 m. Für die
Spriessung werden diverse Profile verwendet.
Die Bohrpfähle für die verankerte Bohrpfahlwand haben einen Durchmesser von
750 mm und eine Länge zwischen 9 und 22.5 m für eine Baugrube mit einer Tiefe von
7.73 bis 8.73 m. Die Verankerung basiert auf den Angaben zur Verankerung der
Rühlwand.
Der Material- und Treibstoffverbrauch der unverankerten Bohrpfahlwand entspricht der
gespriessten Bohrpfahlwand ohne Einbezug des Materialverbrauchs für die Spriessung.
In diesem Fall wird angenommen, dass die Bohrpfahlwand durch Geschosse des
Gebäudes stabilisiert wird und keine Aufwendung für Verankerungen oder
Spriessungen nötig sind. Die Bohrpfähle überschneiden sich zu 20 %.3
Der für die Bohrpfähle eingesetzte Beton wird entsorgt und rezykliert. Darum wird eine
Ressourcenkorrektur in Höhe von 90 % des Kies- und Sandanteils im Beton
vorgenommen.
Für die Bohrung wird mit einem Dieselverbrauch zwischen 6 und 7 Liter pro Meter
gerechnet in Abhängigkeit des Durchmessers der Bohrung.5 In den vorliegenden
Bilanzen wird mit einem Dieselverbrauch von 6.5 Litern pro Meter gerechnet.
Für die verankerte Bohrpfahlwand wird ein Beton mit einem tiefen Zementgehalt
verwendet (315 kg/m3), entsprechend wird der Betonbedarf mit dem durchschnittlichen
Schweizer Tiefbaubeton modelliert. Für die gespriesste Bohrpfahlwand wird der
durchschnittliche Schweizer Bohrpfahlbeton mit einem höheren Zementgehalt
verwendet.
Tab. 6.6 zeigt die Sachbilanzdaten der beiden bilanzierten Bohrpfahlwände.




Ökobilanzen von Tiefbauarbeiten bei Hochbauten                                                      treeze Ltd.
Sachbilanzdaten                                                                                                                                                                                                                                      19




Tab. 6.6 Sachbilanzdaten zur Herstellung der bilanzierten Bohrpfahlwände pro m2 Ansichtsfläche




                                                                                                                                                                                              StandardDeviation95
                                                                                     InfrastructureProcess




                                                                                                                                                                            UncertaintyType
                                                                                                                    bored pile wall,
                                                                                                                                       bored pile wall,
                                                                                                                      overlapped,




                                                                          Location
                                                                                                                                        overlapped,      bored pile wall,
                                                                                                                     strutted apart,




                                                                                                             Unit
                                                                                                                                                                                                                    GeneralComment




                                                                                                                                                                                                      %
                                               Name                                                                                      anchored,      overlapped, non-
                                                                                                                    Alterssiedlung
                                                                                                                                         Stadtspital       anchored
                                                                                                                    Seefeldstrasse
                                                                                                                                       Triemli Zürich
                                                                                                                         Zürich


                                              Location                                                                    CH                CH                CH
                                   InfrastructureProcess                                                                   0                 0                 0
                                             Unit                                                                         m2                m2                m2
                   bored pile wall, overlapped, strutted apart,
                                                                          CH            0                    m2            1                 0                 0
                   Alterssiedlung Seefeldstrasse Zürich
                   bored pile wall, overlapped, anchored, Stadtspital
                                                                          CH            0                    m2            0                 1                 0
                   Triemli Zürich
                   bored pile wall, overlapped, non-anchored              CH            0                    m2            0                 0                 1
                                                                                                                                                                                                                    (3,3,1,3,1,4,BU:1.05); company
technosphere       rolled steel, at regional storage                      CH            0                    kg        5.33E+1            2.13E+1              0                1               1.16                data; APT Ingenieure 2014, pers.
                                                                                                                                                                                                                    communication Andreas Lutz
                                                                                                                                                                                                                    (3,3,1,3,1,4,BU:1.05); company
                   reinforcing steel, secondary production, (100% Rec.)   CH            0                    kg        6.40E+1            1.13E+2           6.40E+1             1               1.16                data; APT Ingenieure 2014, pers.
                                                                                                                                                                                                                    communication Andreas Lutz
                                                                                                                                                                                                                    (3,3,1,3,1,4,BU:1.05); company
                   concrete, concrete for underground construction,
                                                                          CH            0                    kg            0              3.12E+3              0                1               1.16                data; APT Ingenieure 2014, pers.
                   average cement Switzerland, at plant
                                                                                                                                                                                                                    communication Andreas Lutz
                                                                                                                                                                                                                    (3,3,1,3,1,4,BU:1.05); company
                   concrete, concrete for drilled piles, average cement
                                                                          CH            0                    kg        4.92E+3            9.60E+1           4.92E+3             1               1.16                data; APT Ingenieure 2014, pers.
                   Switzerland, at plant
                                                                                                                                                                                                                    communication Andreas Lutz
                                                                                                                                                                                                                    (3,3,1,3,1,4,BU:1.05); company
                   diesel, burned in building machine                     GLO           0                    MJ        1.81E+3            7.44E+2           1.81E+3             1               1.16                data; Marti AG, 2014, pers.
                                                                                                                                                                                                                    communication Roger Hartmann
                                                                                                                                                                                                                    (3,3,1,3,1,4,BU:2); 20 km for
                   transport, lorry >28t, fleet average                   CH            0                    tkm       1.04E+2            7.11E+1           1.02E+2             1               2.03                concrete, 50 km for steel; standard
                                                                                                                                                                                                                    distances ecoinvent v2.2
                                                                                                                                                                                                                    (3,3,1,3,1,4,BU:2); 600 km for steel;
                   transport, freight, rail                               CH            0                    tkm       7.04E+1            8.08E+1           3.84E+1             1               2.03
                                                                                                                                                                                                                    standard distances ecoinvent v2.2

emission resource,                                                                                                                                                                                                  (3,3,1,3,1,4,BU:1.05); calculated;
                   Gravel, resource correction                              -             -                  kg        -2.12E+3          -1.49E+3           -2.12E+3            1               1.16
in ground                                                                                                                                                                                                           based on material use
                                                                                                                                                                                                                    (3,3,1,3,1,4,BU:1.05); calculated;
                   Sand, resource correction                                -             -                  kg        -1.30E+3          -8.41E+2           -1.30E+3            1               1.16
                                                                                                                                                                                                                    based on material use




6.2.5 Schlitzwände
Es werden drei verschiedene Schlitzwände von unterschiedlicher Dicke und
unterschiedlichen Bauunternehmen bilanziert. Tab. 6.7 zeigt eine Übersicht der
bilanzierten Schlitzwände inklusive einer Beschreibung der Bauweise.
Tab. 6.7 Übersicht und Beschrieb der bilanzierten Schlitzwände; L = Länge der Schlitzwand, T = Tiefe
         der Baugrube

Bezeichnung                                   Bauunternehmung                                                Beschrieb
Schlitzwand, 400mm                            Implenia                                                       Schlitzwand: Dicke = 400 mm, Zementgehalt = 380 kg/m3,
                                                                                                             Armierungsgehalt = 100 kg/m3, L = 12.5 m, T = 5 m
Schlitzwand, 800mm                            Implenia                                                       Schlitzwand: Dicke = 800 mm, Zementgehalt = 380 kg/m3,
                                                                                                             Armierungsgehalt = 100 kg/m3, L = 12.5 m, T = 5 m
Schlitzwand, 800mm                            Bauer Schweiz                                                  Schlitzwand: Dicke = 800 mm, Zementgehalt = 375 kg/m3,
                                                                                                             Armierungsgehalt = 100 kg/m3, L = 12.5 m, T = 5 m
Schlitzwand, 800mm                            Durchschnitt                                                   Durchschnitt Schlitzwand Dicke = 800mm



Der Armierungsgehalt und der Zementgehalt des verwendeten Betons sind unabhängig
von der Dicke für alle Schlitzwände identisch, ebenso wie das Verhältnis der Tiefe der
Schlitzwand zur Tiefe der Baugrube.


Ökobilanzen von Tiefbauarbeiten bei Hochbauten                                                                                                                                                                                   treeze Ltd.
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 m2.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
