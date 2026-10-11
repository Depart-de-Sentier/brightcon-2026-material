You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Ventilation of dwellings, decentralized, 6 x 120 m3/h, PE ducts, without GHE` [CH], reference unit 1 m2a, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~18 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: ventilation / unspecified
- includedProcesses: Materials used for the construction and renewal of the ventilation system. Electricity for the operation of the system on 12 month per year included. Transport of the components to the construction site. Disposal of the components included. Influence of ventilation ducts on building construction not included.
- technology: Electricity demand of ventilator (0.4 Wh/m3) representative for DC- or EC-motors and a system design with low pressure drops. Electricity demand of control unit 10 W. Additional 0.3 kWh/(m2 a) electricity demand for defrosting of heat exchanger. Decentral ventilation system without ground heat exchanger. Air intake on the facade and direct to the 6 decentral ventilation units with a short galvanised steel tube (125 mm diameter). Distribution of fresh- and exhaust-air within the flat with polyethylene tubes (75 mm diameter). Exhaust air from the 6 decentral ventilation units with a short galvanised steel tube (400 mm diameter) direct to the exhaust on the facade.
- generalComment: Life time of system and ducts 50 years. Life time of ventilation unit 20 years. Life time of filters 1 year. Ventilation system for a multi family house. The house considered in the investigation includes 6 flats with 130 m2 floor area each and a ventilation rate of 120 m3/h. The influence of a smaller concrete demand due to embedment of ventilation tubes in the concrete of the floor (-4.86 kg concrete per m2 floor area) is not included.;
UUID: 5975eaf7-68e1-3eef-9a5b-f3002d022649
- source cited in the metadata: Haessig W. | 2007 | 2007 - LCI comfort ventilation in dwellings - Haessig
- time period: 2003-01-2003-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 m2a):
- none

## Report excerpt

Source file: `report-p97-99.txt` (SHA-256 c62f3cee5164480313f03c2badc4df1c76b7a9663d8d2debc9a6d339b20894e8), pages 97-99 of `2007 - LCI comfort ventilation in dwellings - Haessig.pdf`.

```
Ökologische Aspekte der Komfortlüftungen im Wohnbereich – Schlussbericht




Tabelle 10.23                           Entsorgung, Lüftungsgeräte, zentral




                                                                                                                                                                                                                                                  Lüftungsgerät, TWL-




                                                                                                                                                                                                                                                                                      Verkablung, zentral
                                                                                                                                                                                 zentral, 600-1200
                                                                                                                                                                                 Lüftungsgerät,




                                                                                                                                                                                                                  Lüftungsgerät,
                                                                                                                                                                                                                  KWLC 1200
                                                                                                                                                                                 Entsorgung,




                                                                                                                                                                                                                  Entsorgung,




                                                                                                                                                                                                                                                  Entsorgung,




                                                                                                                                                                                                                                                                                      Entsorgung,
                                                                                                                                                                                                                                                                                      Steuerung,
                                                                                                                                                                                 m3/h




                                                                                                                                                                                                                                                  700
                                                                                                                  Name
                                                                                                                  Location CH                                                                                CH                             CH                                  CH
                                                                                                                  Infrastr. *) -                                                                             -                              -                                   -
Input von Technosphäre                                                                              Location I *) Einheit      unit                                                                          unit                           unit                                unit
Entsorgung, Gebäude, Massiveisen ohne Armierungseisen, in
                                                           CH       - kg                                                                                                              1.29E+2                        1.53E+2                            1.09E+2                                                -
Sortieranlage
Entsorgung, Gebäude, Mineralwolle, in Sortieranlage        CH       - kg                                                                                                              1.26E+1                        1.60E+1                            1.00E+1                                                -
Entsorgung, Gebäude, Polyethylen/Polypropylen-Produkte, in
                                                           CH       - kg                                                                                                                                 -                             -                    4.00E-1                                            -
Beseitigung
Entsorgung, Gebäude, Anstrich auf Metall, in Sortieranlage CH       - kg                                                                                                               4.53E-1                        5.64E-1                                              -                                   -
Entsorgung, Kabel-Kunststoff, 3.55% Wasser, in
                                                           CH       - kg                                                                                                                                 -                             -                                   -              2.69E+0
Kehrichtverbrennung
Entsorgung, Elektronik für Steuerung                       RER      - kg                                                                                                               6.00E-1                        6.00E-1                               6.00E-1                        6.00E-1
Entsorgung, Gummi, unspezifisch, 0% Wasser, in
                                                           CH       - kg                                                                                                               6.00E-1                        6.00E-1                               6.00E-1                                            -
Kehrichtverbrennung
Transport, Lkw 28t                                         CH       - tkm                                                                                                              6.00E-3                        6.00E-3                               6.00E-3                        2.69E-2
*) Infrastrukturprozess (1= ja, - = nein)
Location: Geographischer Bezug für Prozess (RER = Europa; CH = Schweiz)


                                                 10.3.7 Lüftungsanlage komplett, ecoinvent Datensatz
                                                 Da die Entsorgung der in Tabelle 10.24 aufgeführten Bauteile jeweils nur aus
                                                 einem Entsorgungsprozess bestehen werden diese für die in ecoinvent zu
                                                 verwendenden Datensätze zusammengefasst. Die entsprechend modifizierte
                                                 Sachbilanz ist in Tabelle 10.25 zu finden.


Tabelle 10.24                           Entsorgungsprozesse mit nur einer Position
                                                                                                     Zulufteinlass, Stahl /




                                                                                                                                   Erdregisterrohr, PE,
                                                                         Stahl / Alu, 85x365




                                                                                                                                                                                                                                       Entsorgung, Bogen




                                                                                                                                                                                                                                                                  Verbindungsstück,
                                                                                                                                                                                                                                       90°, Stahl, 100x50




                                                                                                                                                                                                                                                                  Stahl, 100x50 mm
                                                                                                                                                                                                              Entsorgung, Mini




                                                                                                                                                                                                                                                                                            Lüftungsrohr, PE
                                                                                                                                                                                                                                                                                            Wellrohr, DN 75
                                                                         Fortluftauslass,




                                                                                                                                                               Wickelfalzrohr,




                                                                                                                                                                                       Wickelfalzrohr,
                                                                                                                                                               Stahl, DN 400




                                                                                                                                                                                       Stahl, DN 125



                                                                                                                                                                                                              Kanal, Stahl,
                                                                         Entsorgung,




                                                                                                     Entsorgung,




                                                                                                                                   Entsorgung,




                                                                                                                                                               Entsorgung,




                                                                                                                                                                                       Entsorgung,




                                                                                                                                                                                                                                                                  Entsorgung,




                                                                                                                                                                                                                                                                                            Entsorgung,
                                                                                                                                                                                                              100x50 mm
                                                                                                     SS, DN 75




                                                                                                                                   DN 200
                                                                         mm




                                                                                                                                                                                                                                       mm




                                                            Name
                                                            Location CH                            CH                             CH                          CH                      CH                     CH                      CH                         CH                        CH
                                                            Infrastr. *) -                         -                              -                           -                       -                      -                       -                          -                         -
Input von Technosphäre                      Location   I *) Einheit      unit                      unit                           m                           m                       m                      m                       unit                       unit                      m
Entsorgung, Gebäude, Massiveisen ohne
                                            CH          -   kg                  2.50E+0                   2.20E+0                                         -        6.00E+0                 1.90E+0                 1.50E+0                  2.70E-1                    2.00E-1                                 -
Armierungseisen, in Sortieranlage

Entsorgung, Gebäude,
Polyethylen/Polypropylen-Produkte, in       CH          -   kg                                 -                              -        3.00E+0                                    -                      -                       -                          -                         -         3.30E-1
Beseitigung




                                                 ecoinvent-report No. 25                                                                                  80
                                       Ökologische Aspekte der Komfortlüftungen im Wohnbereich – Schlussbericht




Tabelle 10.25                   Lüftungsanlage komplett, Sachbilanz für ecoinvent




                                                                                      m3/h, Stahlrohre, mit




                                                                                                                                    m3/h, Stahlrohre, mit
                                                                                                              m3/h, PE-Rohre, mit




                                                                                                                                                            m3/h, PE-Rohre, mit
                                                                                      dezentral, 6 x 120




                                                                                                              dezentral, 6 x 120




                                                                                                                                                                                  dezentral, 6 x 120




                                                                                                                                                                                                           dezentral, 6 x 120
                                                                                                                                                                                  m3/h, Stahlrohre,




                                                                                                                                                                                                           m3/h, PE-Rohre,
                                                                                                                                                                                  ohne Erdregister




                                                                                                                                                                                                           ohne Erdregister
                                                                                      Lüftungsanlage,




                                                                                                              Lüftungsanlage,




                                                                                                                                    Lüftungsanlage,




                                                                                                                                                            Lüftungsanlage,




                                                                                                                                                                                  Lüftungsanlage,




                                                                                                                                                                                                           Lüftungsanlage,
                                                                                                                                    zentral, 1 x 720




                                                                                                                                                            zentral, 1 x 720
                                                                                      Erdregister




                                                                                                              Erdregister




                                                                                                                                    Erdregister




                                                                                                                                                            Erdregister
                                                                            Name
                                                                            Location CH               CH           CH           CH           CH           CH
                                                                            Infrastr. *) 1            1            1            1            1            1
Input von Technosphäre                                      Location   I *) Einheit      unit         unit         unit         unit         unit         unit
Aussenluftfassung, Edelstahl, DN 370, ab Werk               RER          - unit               1.00E+0      1.00E+0      1.00E+0      1.00E+0            -            -
Dachdurchführung, Stahl, DN 400, ab Werk                    CH           - unit               1.00E+0      1.00E+0      1.00E+0      1.00E+0            -            -
Fortluftauslass, Stahl / Alu, 85x365 mm, ab Werk            CH           - unit                     -            -            -            -      1.20E+1      1.20E+1
Zulufteinlass, Stahl / SS, DN 75, ab Werk                   RER          - unit               3.00E+1      3.00E+1      3.00E+1      3.00E+1      3.00E+1      3.00E+1
Abluftventil, UP-Gehäuse, Kunststoff / Stahl, DN 125, ab Werk CH        -   unit             1.80E+1                1.80E+1                1.80E+1                1.80E+1               1.80E+1                  1.80E+1
AP-Luftverteilkasten, Stahl, 120 m3/h, ab Werk               CH      - unit             1.20E+1       1.20E+1       1.20E+1         1.20E+1                                             1.20E+1                  1.20E+1
Überströmelement, Stahl, ca. 40 m3/h, ab Werk                RER     - unit            1.80E+1        1.80E+1       1.80E+1         1.80E+1                                             1.80E+1                  1.80E+1
Erdregisterrohr, PE, DN 200, ab Werk                         RER     - m                1.20E+2       1.20E+2       1.20E+2         1.20E+2                                                   -                        -
Wickelfalzrohr, Stahl, DN 400, ab Werk                       RER     - m                4.00E+1       4.00E+1       4.50E+1         4.50E+1                                                   -                        -
Dämmung Wickelfalzrohr, Steinwolle, DN 400, 30 mm, ab
                                                             RER     - m                4.00E+1       4.00E+1       2.00E+1         2.00E+1                                                            -                        -
Werk
Wickelfalzrohr, Stahl, DN 125, ab Werk                       RER     - m               1.20E+1        1.20E+1       1.20E+1         1.20E+1                                             1.20E+1                  1.20E+1
Mini Kanal, Stahl, 100x50 mm, ab Werk                        RER     - m                6.00E+2                -    6.00E+2                -                                            6.00E+2                        -
Bogen 90°, Stahl, 100x50 mm, ab Werk                         RER     - unit             2.28E+2                -    2.28E+2                -                                            2.28E+2                        -
Verbindungsstück, Stahl, 100x50 mm, ab Werk                  RER     - unit             1.50E+2                -    1.50E+2                -                                            1.50E+2                        -
Lüftungsrohr, PE Wellrohr, DN 75, ab Werk                    RER     - m                       -      4.00E+2               -       4.00E+2                                                   -                  4.00E+2
Flex Rohr, Alu / PET, DN 125, ab Werk                        RER     - m                2.00E+1       1.00E+1       2.00E+1         1.00E+1                                             2.00E+1                  1.00E+1
Schalldämpfer, Stahl, DN 315, 50 mm, ab Werk                 CH      - unit                    -               -    2.00E+0         2.00E+0                                                   -                        -
Schalldämpfer, Stahl, DN 125, ab Werk                        CH      - unit             2.40E+1       2.40E+1       1.20E+1         1.20E+1                                             2.40E+1                  2.40E+1
Zu- Abluftfilter, dezentral, 180-250 m3/h, ab Werk           RER     - unit            1.20E+1        1.20E+1               -              -                                            1.20E+1                  1.20E+1
Abluftfilter, in Abluftventil, ab Werk                       RER     - unit             1.80E+1       1.80E+1       1.80E+1         1.80E+1                                             1.80E+1                  1.80E+1
Zu- Abluftfilter, zentral, 600 m3/h, ab Werk                 RER     - unit                    -               -    2.00E+0         2.00E+0                                                   -                        -
Kaltschrumpfband, Alu/ PE, 50 mm breit, ab Werk              RER     - m               7.00E+2        2.00E+2       7.00E+2         2.00E+2                                             7.00E+2                  2.00E+2
Steuerung, Verkablung, dezentral, ab Werk                    RER     - unit             6.00E+0       6.00E+0               -              -                                            6.00E+0                  6.00E+0
Steuerung, Verkablung, zentral, ab Werk                      RER     - unit                    -               -    1.00E+0         1.00E+0                                                   -                        -
Lüftungsgerät, dezentral, 180-250 m3/h, ab Werk              RER     - unit             6.00E+0       6.00E+0               -              -                                            6.00E+0                  6.00E+0
Lüftungsgerät, zentral, 600-1200 m3/h, ab Werk               RER     - unit                    -               -    1.00E+0         1.00E+0                                                   -                        -
Entsorgung, Gebäude, Massiveisen ohne Armierungseisen, in
                                                             CH      - kg               1.32E+3       3.29E+2       1.35E+3         3.59E+2                                             1.11E+3                  1.19E+2
Sortieranlage
Entsorgung, Gebäude, Polyethylen/Polypropylen-Produkte, in
                                                             CH      - kg               3.60E+2       4.92E+2       3.60E+2         4.92E+2                                                            -         1.32E+2
Beseitigung
Entsorgung, Aussenluftfassung, Edelstahl, DN 370             CH      - unit             1.00E+0       1.00E+0       1.00E+0         1.00E+0                                                            -                        -
Entsorgung, Dachdurchführung, Stahl, DN 400                  CH      - unit             1.00E+0       1.00E+0       1.00E+0         1.00E+0                                                            -                        -
Entsorgung, Abluftventil, UP-Gehäuse, Kunststoff / Stahl, DN
                                                             CH      - unit             1.80E+1       1.80E+1       1.80E+1         1.80E+1                                             1.80E+1                  1.80E+1
125
Entsorgung, AP-Luftverteilkasten, Stahl, 120 m3/h            CH      - unit             1.20E+1       1.20E+1       1.20E+1         1.20E+1                                             1.20E+1                  1.20E+1
Entsorgung, Überströmelement, Stahl, ca. 40 m3/h             CH      - unit             1.80E+1       1.80E+1       1.80E+1         1.80E+1                                             1.80E+1                  1.80E+1
Entsorgung, Dämmung Wickelfalzrohr, Steinwolle, DN 400, 30
                                                             CH      - m                4.00E+1       4.00E+1       2.00E+1         2.00E+1                                                            -                        -
mm
Entsorgung, Flex Rohr, Alu / PET, DN 125                     CH      - m                2.00E+1       1.00E+1       2.00E+1         1.00E+1                                             2.00E+1                  1.00E+1
Entsorgung, Schalldämpfer, Stahl, DN 315, 50 mm              CH      - unit                    -               -    2.00E+0         2.00E+0                                                   -                        -
Entsorgung, Schalldämpfer, Stahl, DN 125                     CH      - unit             2.40E+1       2.40E+1       1.20E+1         1.20E+1                                             2.40E+1                  2.40E+1
Entsorgung, Zu- Abluftfilter, dezentral, 180-250 m3/h        CH      - unit             1.20E+1       1.20E+1               -              -                                            1.20E+1                  1.20E+1
Entsorgung, Abluftfilter, in Abluftventil                    CH      - unit             1.80E+1       1.80E+1       1.80E+1         1.80E+1                                             1.80E+1                  1.80E+1
Entsorgung, Zu- Abluftfilter, zentral, 600 m3/h              CH      - unit                    -               -    2.00E+0         2.00E+0                                                   -                        -
Entsorgung, Kaltschrumpfband, Alu/ PE, 50 mm breit           CH      - m                7.00E+2       2.00E+2       7.00E+2         2.00E+2                                             7.00E+2                  2.00E+2
Entsorgung, Steuerung, Verkablung, dezentral                 CH      - unit             6.00E+0       6.00E+0               -              -                                            6.00E+0                  6.00E+0
Entsorgung, Steuerung, Verkablung, zentral                   CH      - unit                    -               -    1.00E+0         1.00E+0                                                   -                        -
Entsorgung, Lüftungsgerät, dezentral, 180-250 m3/h           CH      - unit             6.00E+0       6.00E+0               -              -                                            6.00E+0                  6.00E+0
Entsorgung, Lüftungsgerät, zentral, 600-1200 m3/h            CH      - unit                    -               -    1.00E+0         1.00E+0                                                   -                        -
Aushub Hydraulikbagger                                       RER     - m3               1.37E+2       1.37E+2       1.37E+2         1.37E+2                                                   -                        -
Transport, Lkw 32t                                           RER     - tkm              5.72E+2       3.33E+2       5.32E+2         2.92E+2                                             3.31E+2                  9.21E+1
Transport, Lkw 28t                                           CH      - tkm              8.76E+0       8.76E+0       8.84E+0         8.84E+0                                             9.43E+0                  9.43E+0
Transport, Lieferwagen <3.5t                                 CH      - tkm              1.26E+2       8.16E+1       1.15E+2         7.05E+1                                             8.86E+1                  4.41E+1
*) Infrastrukturprozess (1= ja, - = nein)
Location: Geographischer Bezug für Prozess (RER = Europa; CH = Schweiz, UCTE = Union for the Co-ordination of Transmission of Electricity)




                                          ecoinvent-report No. 25                                     81
                                   Ökologische Aspekte der Komfortlüftungen im Wohnbereich – Schlussbericht




                                        10.4. Resultattabellen
                                        10.4.1 Lüftungsanlage, komplett
                                        Die in Tabelle 10.26 präsentierten Resultate der Inventarberechnungen beziehen
                                        sich auf die Herstellung und Entsorgung der Bauteile der Lüftungsanlage (1 unit).
                                        In diesem Inventar sind keine Aufwendungen für Erneuerung und Betrieb der
                                        Anlage enthalten. Im weiteren sind keine Aufwendungen aus der Verlegung der
                                        Lüftungsrohre enthalten (verringerter Betonbedarf, bzw. erhöhter Materialbedarf im
                                        Unterlagsboden).
Tabelle 10.26                  Resultate, Lüftungsanlage komplett, Herstellung und Entsorgung




                                                                                                                                                                                             m3/h, PE-Rohre, ohne
                                                                                                                      zentral, 1 x 720 m3/h,




                                                                                                                                               zentral, 1 x 720 m3/h,
                                                                       m3/h, Stahlrohre, mit




                                                                                                m3/h, PE-Rohre, mit
                                                                       dezentral, 6 x 120




                                                                                                dezentral, 6 x 120




                                                                                                                                                                        dezentral, 6 x 120




                                                                                                                                                                                             dezentral, 6 x 120
                                                                                                                                                                        m3/h, Stahlrohre,
                                                                                                                                                                        ohne Erdregister
                                                                       Lüftungsanlage,




                                                                                                Lüftungsanlage,




                                                                                                                      Lüftungsanlage,




                                                                                                                                               Lüftungsanlage,




                                                                                                                                                                        Lüftungsanlage,




                                                                                                                                                                                             Lüftungsanlage,
                                                                                                                      Stahlrohre, mit




                                                                                                                                               PE-Rohre, mit
                                                                       Erdregister




                                                                                                Erdregister




                                                                                                                      Erdregister




                                                                                                                                               Erdregister




                                                                                                                                                                                             Erdregister
Bewertungsmethode                                        Einheit
Eco-indicator 99, (H,A), Total                           Punkte/unit     1.77E+03                   1.01E+03            1.63E+03                 8.66E+02                 1.28E+03             5.15E+02
Ökologische Knappheit 1997, Total                        UBP/unit        2.44E+07                   1.34E+07            2.25E+07                 1.15E+07                 1.81E+07             7.06E+06
Kumulierter Energieaufwand, nicht-erneuerbar             MJ-Eq./unit     1.88E+05                   1.38E+05            1.66E+05                 1.16E+05                 1.18E+05             6.82E+04
Kumulierter Energieaufwand, erneuerbar                   MJ-Eq./unit     1.56E+04                   1.02E+04            1.35E+04                 8.08E+03                 1.10E+04             5.57E+03
Bewertungsmethode, Schutzgutkategorie                    Einheit
Eco-indicator 99, (H,A), Ökosystemqualität               Punkte/unit     3.60E+02                   1.60E+02            3.43E+02                 1.43E+02                 2.82E+02             8.25E+01
Eco-indicator 99, (H,A), Menschliche Gesundheit          Punkte/unit     9.28E+02                   4.96E+02            8.62E+02                 4.29E+02                 6.95E+02             2.62E+02
Eco-indicator 99, (H,A), Ressourcen                      Punkte/unit     4.80E+02                   3.51E+02            4.23E+02                 2.94E+02                 2.99E+02             1.70E+02
Bewertungsmethode, Schadenskategorie                     Einheit
Eco-indicator 99, (H,A), Versauerung & Eutrophierung     Punkte/unit     1.02E+02                   4.34E+01            9.85E+01                 4.01E+01                 7.99E+01             2.15E+01
Eco-indicator 99, (H,A), Ökotoxizität                    Punkte/unit     2.43E+02                   1.07E+02            2.31E+02                 9.58E+01                 1.91E+02             5.58E+01
Eco-indicator 99, (H,A), Landnutzung                     Punkte/unit     1.52E+01                   9.15E+00            1.34E+01                 7.35E+00                 1.12E+01             5.09E+00
Eco-indicator 99, (H,A), Krebserregende Stoffe           Punkte/unit     1.57E+02                   8.02E+01            1.45E+02                 6.81E+01                 1.28E+02             5.06E+01
Eco-indicator 99, (H,A), Klimawandel                     Punkte/unit     5.87E+01                   4.38E+01            5.13E+01                 3.64E+01                 3.65E+01             2.16E+01
Eco-indicator 99, (H,A), Radioaktive Strahlung           Punkte/unit     1.75E+00                   1.12E+00            1.57E+00                 9.31E-01                 1.25E+00             6.19E-01
Eco-indicator 99, (H,A), Ozonabbau                       Punkte/unit     2.60E-02                   1.38E-02            2.33E-02                 1.11E-02                 2.01E-02             7.91E-03
Eco-indicator 99, (H,A), Atemwegserkrankungen            Punkte/unit     7.11E+02                   3.71E+02            6.64E+02                 3.24E+02                 5.30E+02             1.89E+02
Eco-indicator 99, (H,A), Fossile Brennstoffe             Punkte/unit     3.76E+02                   2.95E+02            3.30E+02                 2.48E+02                 2.20E+02             1.39E+02
Eco-indicator 99, (H,A), Mineralien                      Punkte/unit     1.06E+02                   5.72E+01            9.55E+01                 4.68E+01                 8.04E+01             3.17E+01
Bewertungsmethode, Schadenskategorie                     Einheit
Ökologische Knappheit 1997, Deponierte Abfälle           UBP/unit        1.01E+06                   7.13E+05            8.87E+05                 5.91E+05                 6.50E+05             3.55E+05
Ökologische Knappheit 1997, Emissionen in die Luft       UBP/unit        1.87E+07                   9.79E+06            1.75E+07                 8.58E+06                 1.38E+07             4.94E+06
Ökologische Knappheit 1997, Emissionen in Boden und
Grundwasser                                              UBP/unit        1.76E+06                   1.11E+06            1.46E+06                 8.05E+05                 1.41E+06             7.56E+05
Ökologische Knappheit 1997, Emissionen in die
Oberflächengewässer                                      UBP/unit        9.98E+05                   5.01E+05            9.40E+05                 4.42E+05                 8.03E+05             3.05E+05
Ökologische Knappheit 1997, Radioaktive Abfälle          UBP/unit        1.78E+06                   1.13E+06            1.59E+06                 9.44E+05                 1.27E+06             6.26E+05
Ökologische Knappheit 1997, Verbrauch von Energie-
Ressourcen                                               UBP/unit        2.02E+05                   1.47E+05            1.78E+05                 1.23E+05                 1.28E+05             7.29E+04
Bewertungsmethode, Energieträger                         Einheit
Kumulierter Energieaufwand, Fossil                       MJ-Eq./unit     1.53E+05                   1.14E+05            1.35E+05                 9.59E+04                 9.46E+04             5.56E+04
Kumulierter Energieaufwand, Nuklear                      MJ-Eq./unit     3.50E+04                   2.38E+04            3.13E+04                 2.01E+04                 2.37E+04             1.26E+04
Kumulierter Energieaufwand, Biomasse                     MJ-Eq./unit     1.65E+03                   1.28E+03            1.38E+03                 1.01E+03                 9.72E+02             6.04E+02
Kumulierter Energieaufwand, Wind, Sonne, Geothermie      MJ-Eq./unit     7.47E+02                   4.53E+02            6.86E+02                 3.92E+02                 5.35E+02             2.41E+02
Kumulierter Energieaufwand, Wasser                       MJ-Eq./unit     1.32E+04                   8.46E+03            1.14E+04                 6.68E+03                 9.48E+03             4.72E+03



                                        10.4.2 Wohnraumlüftung, Anlage inkl. Erneuerung
                                        Die nachfolgend präsentierten Resultate der Inventarberechnungen beziehen sich
                                        auf 1 m2 Energiebezugsfläche und ein Betriebsjahr. In diesen Resultaten sind
                                        keine Aufwendungen aus der Verlegung der Lüftungsrohre enthalten (verringerter
                                        Betonbedarf, bzw. erhöhter Materialbedarf im Unterlagsboden).




                                        ecoinvent-report No. 25                                82
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 m2a.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
