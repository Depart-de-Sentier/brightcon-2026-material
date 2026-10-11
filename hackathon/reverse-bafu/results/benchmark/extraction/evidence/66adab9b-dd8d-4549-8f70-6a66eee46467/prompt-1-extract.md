You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Disposal, branch connections and fittings, steel` [CH], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~7 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: waste management / building demolition
- includedProcesses: Transport to dismantling facilities, machines for handling in sorting plant, electricity demand for sorting plant, final disposal of waste material. Cut-off to recycling for metals.
- technology: Disposal to a sorting plant assumed. Metal parts are recycled, plastic parts are incinerated, paint on metal to final disposal.
- generalComment: Disposal of steel branch connections and fittings;
UUID: 66adab9b-dd8d-4549-8f70-6a66eee46467
- source cited in the metadata: Klingler M. | 2014 | 2014 - LCA ventilation and heating systems - Klingler
- time period: 1994-01-2008-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p161-163.txt` (SHA-256 d32efcf6d6b09196f257e5909ea95eb081910fc29184b0edba259ba0931ba3ac), pages 161-163 of `2014 - LCA data ventilation and heating systems - Klingler.pdf`.

```
Ökobilanzdaten für Lüftungs- und Wärmeanlagen                                                  ARGE LW-Bilanzen



                                                                 Geom. Std.-Abw.       Kommentar
                                           Stahlrohre schwarz,   Basisunsicherheit
           ecoinvent - Datensatz           grundiert [kg]        (Pedigree-Matrix)
           epoxy resin, liquid, at         6.272E-04             1.067                 Zinkstaubfarbe
           plant, RER, [kg]                                      1.05 (2,2,3,2,1,3)
           zinc, primary, at regional      7.629E-03             1.067                 Zinkstaubfarbe
           storage, RER, [kg]                                    1.05 (2,2,3,2,1,3)
           limestone, milled, loose, at    1.217E-04             1.067                 Zinkstaubfarbe
           plant, CH, [kg]                                       1.05 (2,2,3,2,1,3)
           solvents, organic, un-          8.706E-04             1.067                 Zinkstaubfarbe
           specified, at plant, GLO,                             1.05 (2,2,3,2,1,3)
           [kg]
           chemicals organic, at           1.123E-04             1.067                 Zinkstaubfarbe
           plant, GLO, [kg]                                      1.05 (2,2,3,2,1,3)
           transport, freight, rail, CH,   5.999E-01             1.442
           [tkm]                                                 2 (3,3,2,2,3,4)
           transport, lorry 20-28t,        5.000E-02             1.442
           fleet average, CH, [tkm]                              2 (3,3,2,2,3,4)


Tabelle 87: Bilanzierung Entsorgung Stahlrohre

                                                                 Geom. Std.-Abw.       Kommentar
                                           Stahlrohre schwarz,   Basisunsicherheit
           ecoinvent - Datensatz           grundiert [kg]        (Pedigree-Matrix)
           Entsorgung
           disposal, building, bulk        9.906E-01             1.126                 Entsorgung Metall
           iron (excluding reinforce-                            1.05 (2,2,3,2,3,4)
           ment), to sorting plant,
           CH, [kg]
           disposal, building, paint on    9.361E-03             1.126                 Entsorgung Zinkstaubfar-
           metal, to sorting plant,                              1.05 (2,2,3,2,3,4)    be
           CH, [kg]
           disposal, building, paint on    9.361E-03             1.126                 Entsorgung Zinkstaubfar-
           metal, to final disposal,                             1.05 (2,2,3,2,3,4)    be
           CH, [kg]


Tabelle 88: Bilanzierung Herstellung Abzweigungen und Formstücke aus Stahl

                                           Abzweigungen und       Geom. Std.-Abw.      Kommentar
                                           Formstücke Stahl,      Basisunsicherheit
           ecoinvent - Datensatz           grundiert [kg]         (Pedigree-Matrix)
           Herstellung
           steel, low-alloyed, at          9.906E-01              1.067                Stahl
           plant, RER, [kg]                                       1.05 (2,2,3,2,1,3)
           drawing of pipes, steel,        9.906E-01              1.126                Verarbeitung
           RER, [kg]                                              1.05 (2,2,3,2,3,4)
           epoxy resin, liquid, at         6.272E-04              1.067                Zinkstaubfarbe
           plant, RER, [kg]                                       1.05 (2,2,3,2,1,3)
           zinc, primary, at regional      7.629E-03              1.067                Zinkstaubfarbe
           storage, RER, [kg]                                     1.05 (2,2,3,2,1,3)
           limestone, milled, loose,       1.217E-04              1.067                Zinkstaubfarbe
           at plant, CH, [kg]                                     1.05 (2,2,3,2,1,3)


BFE Forschungsprojekt Schlussbericht, August 2014                                                          161
Ökobilanzdaten für Lüftungs- und Wärmeanlagen                                                         ARGE LW-Bilanzen



                                            Abzweigungen und          Geom. Std.-Abw.         Kommentar
                                            Formstücke Stahl,         Basisunsicherheit
           ecoinvent - Datensatz            grundiert [kg]            (Pedigree-Matrix)
           solvents, organic, unspec-       8.706E-04                 1.067                   Zinkstaubfarbe
           ified, at plant, GLO, [kg]                                 1.05 (2,2,3,2,1,3)
           chemicals organic, at            1.123E-04                 1.067                   Zinkstaubfarbe
           plant, GLO, [kg]                                           1.05 (2,2,3,2,1,3)
           transport, freight, rail, CH,    5.999E-01                 1.442
           [tkm]                                                      2 (3,3,2,2,3,4)
           transport, lorry 20-28t,         5.000E-02                 1.442
           fleet average, CH, [tkm]                                   2 (3,3,2,2,3,4)


Tabelle 89: Bilanzierung Entsorgung Abzweigungen und Formstücke aus Stahl

                                            Abzweigungen und          Geom. Std.-Abw.         Kommentar
                                            Formstücke Stahl,         Basisunsicherheit
           ecoinvent - Datensatz            grundiert [kg]            (Pedigree-Matrix)
           Entsorgung
           disposal, building, bulk         9.906E-01                 1.126                   Entsorgung Metall
           iron (excluding reinforce-                                 1.05 (2,2,3,2,3,4)
           ment), to sorting plant,
           CH, [kg]
           disposal, building, paint        9.361E-03                 1.126                   Entsorgung Zinkstaubfar-
           on metal, to sorting plant,                                1.05 (2,2,3,2,3,4)      be
           CH, [kg]
           disposal, building, paint        9.361E-03                 1.126                   Entsorgung Zinkstaubfar-
           on metal, to final disposal,                               1.05 (2,2,3,2,3,4)      be
           CH, [kg]


Tabelle 90: Bilanzierung Herstellung Edelstahlrohre

                                                                                           Geom. Std.-Abw.
                                                                                           Basisunsicherheit (Pe-
           ecoinvent - Datensatz                    Edelstahlrohre [kg]                    digree-Matrix)
           Herstellung
           chromium steel 18/8, at plant, RER,      1.000E+00                              1.067
           [kg]                                                                            1.05 (2,2,3,2,1,3)
           drawing of pipes, steel, RER, [kg]       1.000E+00                              1.126
                                                                                           1.05 (2,2,3,2,3,4)
           transport, freight, rail, CH, [tkm]      6.000E-01                              1.442
                                                                                           2 (3,3,2,2,3,4)
           transport, lorry 20-28t, fleet           5.000E-02                              1.442
           average, CH, [tkm]                                                              2 (3,3,2,2,3,4)




BFE Forschungsprojekt Schlussbericht, August 2014                                                                 162
Ökobilanzdaten für Lüftungs- und Wärmeanlagen                                                         ARGE LW-Bilanzen


Tabelle 91: Bilanzierung Entsorgung Edelstahlrohre

                                                                                           Geom. Std.-Abw.
                                                                                           Basisunsicherheit (Pe-
           ecoinvent - Datensatz                       Edelstahlrohre [kg]                 digree-Matrix)
           Entsorgung
           disposal, building, bulk iron (exclud-      1.000E+00                           1.126
           ing reinforcement), to sorting plant,                                           1.05 (2,2,3,2,3,4)
           CH, [kg]


Tabelle 92: Bilanzierung Herstellung Abzweigungen und Formstücke aus Edelstahl

                                                                                           Geom. Std.-Abw.
                                                       Abzweigungen und Formstücke         Basisunsicherheit (Pe-
           ecoinvent - Datensatz                       aus Edelstahl [kg]                  digree-Matrix)
           Herstellung
           chromium steel 18/8, at plant, RER,         1.000E+00                           1.067
           [kg]                                                                            1.05 (2,2,3,2,1,3)
           drawing of pipes, steel, RER, [kg]          1.000E+00                           1.126
                                                                                           1.05 (2,2,3,2,3,4)
           transport, freight, rail, CH, [tkm]         6.000E-01                           1.442
                                                                                           2 (3,3,2,2,3,4)
           transport, lorry 20-28t, fleet              5.000E-02                           1.442
           average, CH, [tkm]                                                              2 (3,3,2,2,3,4)


Tabelle 93: Bilanzierung Entsorgung Abzweigungen und Formstück aus Edelstahl

                                                                                           Geom. Std.-Abw.
                                                       Abzweigungen und Formstücke         Basisunsicherheit (Pe-
           ecoinvent - Datensatz                       aus Edelstahl [kg]                  digree-Matrix)
           Entsorgung
           disposal, building, bulk iron (exclud-      1.000E+00                           1.126
           ing reinforcement), to sorting plant,                                           1.05 (2,2,3,2,3,4)
           CH, [kg]



           Technische Daten Rohrleitungen, Abzweigungen und Formstücke
In Tabelle 94 bis Tabelle 97 sind die Dimensionen und durchschnittlichen Gewichte von Rohrlei-
tungen, Abzweigungen und Formstücken aus Stahl und Edelstahl aufgeführt.

Tabelle 94: Dimensionen Rohrleitungen und Gewicht pro Laufmeter

           Nennweite DN           Zoll                   Aussendurchmesser        Innendurchmesser    Gewicht (kg/m)
                                                         da (mm)                  di (mm)
                            10                                           13.5                   9.9              0.522
                                                 3/8                     17.2                  13.6                 0.89
                            15                                               20                  16                 0.89
                                                 1/2                     21.3                  17.3              0.962
                            20                                               25                  21                 1.13
                                                 3/4                     26.9                  22.3                 1.41
                            25                                               30                24.8                 1.77


BFE Forschungsprojekt Schlussbericht, August 2014                                                                163
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
