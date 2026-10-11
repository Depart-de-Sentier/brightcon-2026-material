You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `PIR insulation with PVC cladding, insulation thickness 40mm` [CH], reference unit 1 m2, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~6 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: heating / production of components
- includedProcesses: Materials used for the production. Energy use for the different production steps. Transport of raw materials to the plant.
- technology: Typical technology, materials and components used for pipe insulation of heating systems in appartment and commercial buildings
- generalComment: Production of a thermal insulation of pipes for heating systems;
UUID: 8fbb543c-4f07-3a5c-944c-1313990c05ba
- source cited in the metadata: Klingler M. | 2014 | 2014 - LCA ventilation and heating systems - Klingler
- time period: 1994-01-2008-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 m2):
- none

## Report excerpt

Source file: `report-p172-174.txt` (SHA-256 b8bb22e607dc13847d7b23b0b4e9b2b1c7c995b2aea59499c91bc95171db350f), pages 172-174 of `2014 - LCA data ventilation and heating systems - Klingler.pdf`.

```
Ökobilanzdaten für Lüftungs- und Wärmeanlagen                                                          ARGE LW-Bilanzen


Tabelle 109: Bilanzierung Herstellung Dämmung Mineralwolle mit Alufolie gitterverstärkt Umhüllung

           ecoinvent-            Dämmung            Dämmung           Dämmung            Dämmung           Dämmung
           Datensatz             Mineralwolle       Mineralwolle      Mineralwolle       Mineralwolle      Mineralwolle
                                 mit Alufolie       mit Alufolie      mit Alufolie       mit Alufolie      mit Alufolie
                                 gitterverstärkt    gitterverstärkt   gitterverstärkt    gitterverstärkt   gitterverstärkt
                                 Umhüllung,         Umhüllung,        Umhüllung,         Umhüllung,        Umhüllung,
                                 Dämmstärke         Dämmstärke        Dämmstärke         Dämmstärke        Dämmstärke
                                 40mm [m2]          50mm [m2]         60mm [m2]          80mm [m2]         100mm [m2]
           HERSTELLUNG
           rock wool, at         1.530E+00          1.913E+00         2.295E+00          3.060E+00         3.825E+00
           plant, CH, [kg]
           glass wool mat,       1.530E+00          1.913E+00         2.295E+00          3.060E+00         3.825E+00
           at plant, CH, [kg]
           aluminium,            1.080E-01          1.080E-01         1.080E-01          1.080E-01         1.080E-01
           production mix,
           at plant, RER,
           [kg]
           sheet rolling,        1.080E-01          1.080E-01         1.080E-01          1.080E-01         1.080E-01
           aluminium, RER,
           [kg]
           polyethylene,         5.433E-02          5.433E-02         5.433E-02          5.433E-02         5.433E-02
           LDPE, granulate,
           at plant, RER,
           [kg]
           injection moul-       5.433E-02          5.433E-02         5.433E-02          5.433E-02         5.433E-02
           ding, RER, [kg]
           transport, freight,   3.385E-01          4.150E-01         4.915E-01          6.445E-01         7.975E-01
           rail, CH, [tkm]
           transport, lorry      6.932E-02          8.462E-02         9.992E-02          1.305E-01         1.611E-01
           20-28t, fleet
           average, CH,
           [tkm]


Tabelle 110: Bilanzierung Entsorgung Dämmung Mineralwolle mit Alufolie gitterverstärkt Umhüllung

           ecoinvent-Datensatz         Dämmung           Dämmung          Dämmung          Dämmung          Dämmung
                                       Mineralwolle      Mineralwolle     Mineralwolle     Mineralwolle     Mineralwolle
                                       mit Alufolie      mit Alufolie     mit Alufolie     mit Alufolie     mit Alufolie
                                       gitterver-        gitterver-       gitterver-       gitterver-       gitterver-
                                       stärkt            stärkt           stärkt           stärkt           stärkt
                                       Umhüllung,        Umhüllung,       Umhüllung,       Umhüllung,       Umhüllung,
                                       Dämmstärke        Dämmstärke       Dämmstärke       Dämmstärke       Dämmstärke
                                       40mm [m2]         50mm [m2]        60mm [m2]        80mm [m2]        100mm [m2]
           ENTSORGUNG
           disposal, building,         3.060E+00         3.825E+00        4.590E+00        6.120E+00        7.650E+00
           mineral wool, to sorting
           plant, CH, [kg]
           disposal, building, bulk    1.080E-01         1.080E-01        1.080E-01        1.080E-01        1.080E-01
           iron (excluding rein-
           forcement), to sorting
           plant, CH, [kg]




BFE Forschungsprojekt Schlussbericht, August 2014                                                                   172
Ökobilanzdaten für Lüftungs- und Wärmeanlagen                                                       ARGE LW-Bilanzen



           ecoinvent-Datensatz         Dämmung           Dämmung         Dämmung        Dämmung         Dämmung
                                       Mineralwolle      Mineralwolle    Mineralwolle   Mineralwolle    Mineralwolle
                                       mit Alufolie      mit Alufolie    mit Alufolie   mit Alufolie    mit Alufolie
                                       gitterver-        gitterver-      gitterver-     gitterver-      gitterver-
                                       stärkt            stärkt          stärkt         stärkt          stärkt
                                       Umhüllung,        Umhüllung,      Umhüllung,     Umhüllung,      Umhüllung,
                                       Dämmstärke        Dämmstärke      Dämmstärke     Dämmstärke      Dämmstärke
                                       40mm [m2]         50mm [m2]       60mm [m2]      80mm [m2]       100mm [m2]
           disposal, building,         5.433E-02         5.433E-02       5.433E-02      5.433E-02       5.433E-02
           polyeth-
           ylene/polypropylene
           products, to final dis-
           posal, CH, [kg]


Tabelle 111: Bilanzierung Herstellung Dämmung PIR mit PVC Umhüllung

           ecoinvent-            Dämmung            Dämmung          Dämmung         Dämmung           Dämmung
           Datensatz             PIR mit PVC        PIR mit PVC      PIR mit PVC     PIR mit PVC       PIR mit PVC
                                 Umhüllung,         Umhüllung,       Umhüllung,      Umhüllung,        Umhüllung,
                                 Dämmstärke         Dämmstärke       Dämmstärke      Dämmstärke        Dämmstärke
                                 30mm [m2]          40mm [m2]        50mm [m2]       60mm [m2]         80mm [m2]
           HERSTELLUNG
           polyurethane,         9.000E-01          1.200E+00        1.500E+00       1.800E+00         2.400E+00
           rigid foam, at
           plant, RER, [kg]
           polyvinylchloride,    4.273E-01          4.273E-01        4.273E-01       4.273E-01         4.273E-01
           at regional
           storage, RER,
           [kg]
           extrusion, plastic    4.273E-01          4.273E-01        4.273E-01       4.273E-01         4.273E-01
           film, RER, [kg]
           transport, freight,   2.655E-01          3.255E-01        3.855E-01       4.455E-01         5.655E-01
           rail, CH, [tkm]
           transport, lorry      6.636E-02          8.136E-02        9.636E-02       1.114E-01         1.414E-01
           20-28t, fleet
           average, CH,
           [tkm]


Tabelle 112: Bilanzierung Entsorgung Dämmung PIR mit PVC Umhüllung

           ecoinvent-            Dämmung            Dämmung          Dämmung         Dämmung           Dämmung
           Datensatz             PIR mit PVC        PIR mit PVC      PIR mit PVC     PIR mit PVC       PIR mit PVC
                                 Umhüllung,         Umhüllung,       Umhüllung,      Umhüllung,        Umhüllung,
                                 Dämmstärke         Dämmstärke       Dämmstärke      Dämmstärke        Dämmstärke
                                 30mm [m2]          40mm [m2]        50mm [m2]       60mm [m2]         80mm [m2]
           ENTSORGUNG
           disposal, build-      9.000E-01          1.200E+00        1.500E+00       1.800E+00         2.400E+00
           ing, polyure-
           thane foam, to
           final disposal,
           CH, [kg]




BFE Forschungsprojekt Schlussbericht, August 2014                                                              173
Ökobilanzdaten für Lüftungs- und Wärmeanlagen                                                    ARGE LW-Bilanzen



           ecoinvent-           Dämmung              Dämmung         Dämmung       Dämmung          Dämmung
           Datensatz            PIR mit PVC          PIR mit PVC     PIR mit PVC   PIR mit PVC      PIR mit PVC
                                Umhüllung,           Umhüllung,      Umhüllung,    Umhüllung,       Umhüllung,
                                Dämmstärke           Dämmstärke      Dämmstärke    Dämmstärke       Dämmstärke
                                30mm [m2]            40mm [m2]       50mm [m2]     60mm [m2]        80mm [m2]
           disposal, build-     4.273E-01            4.273E-01       4.273E-01     4.273E-01        4.273E-01
           ing, polyvi-
           nylchloride
           products, to final
           disposal, CH,
           [kg]




           Andere Komponenten Wärmeanlagen
Neben den oben beschriebenen Datensätzen wurde ein generischer Datensatz für alle übrigen
Systemkomponenten, ausser den oben beschriebenen, pro Kilogramm erarbeitet. Dazu gehören
unter anderem Komponenten wie: Schaltschrank Elektrotableau, Heizkreisverteiler, Verteilerkas-
ten, Druckexpansionsgefässe, Montagegarnitur Wärmezähler, Strangregulierventile, Heizungs-
speicher und Luftflaschen. Die Inputs ergeben sich aus den Mittelwerten der Materialbilanzen
der untersuchten Gebäude. Neben den Rohstoffen wurden durchschnittliche Daten für die Me-
tall- und Kunststoffverarbeitung verwendet. Die Transporte für die Bereitstellung der Rohstoffe
wurden wie bei den anderen Datensätzen mit ecoinvent – Standarddistanzen berücksichtigt. Die
Bilanzierung mit Datensätzen aus ecoinvent sind in Tabelle 113 und Tabelle 114 dargestellt.

Tabelle 113: Bilanzierung Herstellung Andere Komponenten Wärmeanlagen

           ecoinvent-Datensatz                           Andere Komponenten Wärme-      Geom. Std.-Abw.
                                                         anlagen [kg]                   Basisunsicherheit
                                                                                        (Pedigree-Matrix)
           HERSTELLUNG
           steel, low-alloyed, at plant, RER, [kg]       3.686E-01                      1.067
                                                                                        1.05 (2,2,3,2,1,3)
           cast iron, at plant, RER, [kg]                7.153E-02                      1.067
                                                                                        1.05 (2,2,3,2,1,3)
           chromium steel 18/8, at plant, RER, [kg]      3.519E-01                      1.067
                                                                                        1.05 (2,2,3,2,1,3)
           brass, at plant, CH, [kg]                     5.064E-02                      1.067
                                                                                        1.05 (2,2,3,2,1,3)
           aluminium, production mix, at plant,          2.149E-02                      1.067
           RER, [kg]                                                                    1.05 (2,2,3,2,1,3)
           copper, at regional storage, RER, [kg]        4.400E-03                      1.067
                                                                                        1.05 (2,2,3,2,1,3)
           metal product manufacturing, average          8.686E-01                      1.126
           metal working, RER, [kg]                                                     1.05 (2,2,3,2,3,4)
           synthetic rubber, at plant, RER, [kg]         4.488E-02                      1.067
                                                                                        1.05 (2,2,3,2,1,3)
           polyvinylchloride, at regional storage,       2.305E-03                      1.067
           RER, [kg]                                                                    1.05 (2,2,3,2,1,3)
           polycarbonate, at plant, RER, [kg]            1.344E-03                      1.067
                                                                                        1.05 (2,2,3,2,1,3)



BFE Forschungsprojekt Schlussbericht, August 2014                                                            174
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
