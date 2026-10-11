You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Laminating, foil, with acrylic binder` [RER], reference unit 1 m2, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~5 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: Others / unspecified
- includedProcesses: Estimation of electricity use for the laminating and cutting of foils. Only glue for laminating process included. Estimaion for waste process of glue overspray included. Materials which are laminated are not included. No transports of raw materials to the plant included. Infrastructure of the production plant not included.
- technology: Approximation from data of lamination of packaging foils. Acrylic glue as binder assumed.
- generalComment: Data derived from: BUWAL 250, Ökoinventare für Verpackungen, Umwelt-Materialien Nr. 250, Bundesamt für Umwelt, Wald und Landschaft (BUWAL), Bern, 1996.;
UUID: b73dd0bf-3974-3459-b0f7-288fa24e7286
- source cited in the metadata: Haessig W. | 2007 | 2007 - LCI comfort ventilation in dwellings - Haessig
- time period: 1996-01-1996-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 m2):
- none

## Report excerpt

Source file: `report-p83-85.txt` (SHA-256 86c0d588b4d79fad0ce780b3cef586796b715edbb86cbff2c5b3e7b57efb0dd2), pages 83-85 of `2007 - LCI comfort ventilation in dwellings - Haessig.pdf`.

```
Ökologische Aspekte der Komfortlüftungen im Wohnbereich – Schlussbericht




   10.2. Sachbilanzen, verwendete Basisdaten
   10.2.1 Energiebedarf für den Herstellungsprozess
   Die für die einzelnen Bauteile verwendeten Materialien und deren Mengenanteile
   wurden aus den Angaben der Hersteller und Lieferanten ermittelt. Während über
   die Produktionsart oft Angaben verfügbar waren, war dies für die dafür
   aufgewendeten Energiemengen nicht der Fall. Um diese Energiemengen ermitteln
   zu können musste auf Literaturangaben zurückgegriffen werden. Die verwendeten
   spezifischen Energiebedarfe sind in Tabelle 10.4 dargestellt:


   Tabelle 10.4              Spezifischer Elektrizitätsbedarfe, mechanische Fertigung
    Prozess                          Einheit          Elektrizitätsbedarf   Bemerkung
                                                 Stahl          Aluminium
    Bearbeiten, mechanisch           kWh/kg      0.11           0.16        Pro kg zerspantes Material
                                             2                                    2
    Trennen, Bandsäge                kWh/m       1.57           0.79        Pro m Trennfläche
                                             2                                    2
    Trennen, Scheren Stanzen         kWh/m       2.36           1.18        Pro m Trennfläche
                                             2                                    2
    Trennen, Laserschneiden          kWh/m       0.63           0.31        Pro m Trennfläche
    Kaltumformen (Biegen)            kWh/kg      0.13           0.19        Pro kg verarbeitetes Material
    Verbinden (Punktschweissen) kWh/kg           0.13           0.19        Pro Verbindungspunkt *)
   Quelle: Kemna 1981
   *) Mittlerer Wert für 1 mm Blechstärke



   Für verschiedene Prozessschritte konnten auch auf in ecoinvent (Datenbestand
   1.0) bilanzierte Verarbeitungsprozesse zurückgegriffen werden. Dies betrifft
   insbesondere die folgenden Verarbeitungsprozesse:
   – Spritzgiessen und Extrudieren von Kunststoff
   – Walzen von Blechen und ziehen von Rohren und Drähten
   – Schweissen (Schweissnähte)
   – Verzinken der Stahlbleche


   Die Produktion laminierter Folien wurde aus Angaben zur Lamination von
   Verpackungsfolien abgeschätzt. Die verwendete Sachbilanz stammt aus (BUWAL,
   1996) und beinhaltet das Laminieren sowie das Zuschneiden der Folie. Es wurde
   ein Bindemittel auf Acrylatbasis angenommen. Die verwendeten Prozessdaten sind
   in Tabelle 10.5 ersichtlich.
   Die Produktionsaufwendungen für die Filtermatten aus Polyethylenterephthalat
   (PET) wurde aus Angaben der Textilgarnherstellung abgeschätzt. Die verwendete
   Sachbilanz stammt aus (Laursen et al, 1997) und beinhaltet die Faserherstellung
   aus PET und das Verspinnen zu einem Garn. Die verwendeten Prozessdaten sind
   in Tabelle 10.6 ersichtlich.
   Die Produktionsaufwendungen für das Pulverbeschichten wurde aus Angaben von
   (Gloor, 1995 bilanziert. Die verwendete Sachbilanz beinhaltet die Energie-
   aufwendungen für die Vorbehandlung, die Beschichtung und die thermische
   Nachbehandlung. In der Sachbilanz wird von einer Auftragseffizienz von 95% (inkl.
   Pulverrecycling) sowie mit 2 Gew.-% Lösemittelemissionen bei der thermischen
   Nachbehandlung gerechnet (Talbert, 1998). Die Beschichtungsstärke wurde mit

   ecoinvent-report No. 25                       66
                                        Ökologische Aspekte der Komfortlüftungen im Wohnbereich – Schlussbericht




                                            70 µm und die Dichte des verwendeten Farbpulvers mit 1300 kg/m3 angenommen.
                                            Die Sachbilanz für den Pulverlack stammt aus (Richter et al., 1996). Die
                                            verwendeten Prozessdaten sind in Tabelle 10.7 ersichtlich.


Tabelle 10.5                     Produktionsprozess, Laminieren von Folien
                                                                                                                               Laminieren, Folie, mit
                                                                                                                  Name         Acrylat-Bindemittel
                                                                                                                  Location RER
                                                                                                                  Infrastr. *) -
Input von Technosphäre                                                                       Location **)    I *) Einheit      m2
Strom, Mittelspannung, Produktion UCTE, ab Netz                                                 UCTE           - kWh                          1.83E-02
Acrylat-Bindemittel, 54% in H2O, ab Werk                                                         RER           - kg                           1.40E-03
Entsorgung, Anstrichstoff Reste, 0% Wasser, in Sonderabfallverbrennung                            CH           - kg                           2.00E-04
Emissionen in Luft                                                                            Compart. **)
Abwärme                                                                                          Stadt        -   MJ                         6.59E-02
*) Infrastrukturprozess (1= ja, - = nein)
**) Location: Herkunftsort (RER = Europa; CH = Schweiz); Compartiment: Ort der Emission (Stadt, Land, ..)
                                                                                                             2
Quelle: BUWAL, 1996; Beinhaltet Laminieren verkleben und Zuschneiden einer Folie mit 113 g/m .


Tabelle 10.6                     Produktionsprozess, Filtermatten aus Polyethylenterephthalat
                                                                                                                               Vliesherstellung,
                                                                                                                  Name         Polyethylenterephthalat
                                                                                                                  Location RER
                                                                                                                  Infrastr. *) -
Input von Technosphäre                                                                       Location **)    I *) Einheit      kg
Strom, Mittelspannung, Produktion UCTE, ab Netz                                                 UCTE           - kWh                          8.33E+00
Heizöl EL, in Industriefeuerung 1MW, nicht-modulierend                                           RER           - MJ                           1.36E+01
Emissionen in Luft                                                                            Compart. **)
Abwärme                                                                                          Stadt        -   MJ                        3.00E+01
*) Infrastrukturprozess (1= ja, - = nein)
**) Location: Herkunftsort (RER = Europa; CH = Schweiz); Compartiment: Ort der Emission (Stadt, Land, ..)
Quelle: Laursen et al, 1997; Beinhaltet Faserherstellung aus PET und das Verspinnen.


Tabelle 10.7                     Produktionsprozess, Pulverbeschichten von Stahl

                                                                                                                  Name         Pulverbeschichten, Stahl
                                                                                                                  Location RER
                                                                                                                  Infrastr. *) -
Input von Technosphäre                                                                       Location **)    I *) Einheit      m2
Strom, Mittelspannung, Produktion UCTE, ab Netz                                                 UCTE           - kWh                          7.33E-01
Erdgas, in Industriefeuerung Low-NOx>100kW                                                       RER           - MJ                          1.56E+01
Polyester Pulverlack, für Beschichtung, ab Werk                                                  RER           - kg                           9.60E-02
Entsorgung, Anstrichstoff Reste, 0% Wasser, in Sonderabfallverbrennung                            CH           - kg                           4.80E-03
Emissionen in Luft                                                                            Compart. **)
Abwärme                                                                                          Stadt        -   MJ                        2.64E+00
NMVOC, Flüchtige organische Verbindungen                                                         Stadt        -   kg                        1.82E-03
*) Infrastrukturprozess (1= ja, - = nein)
**) Location: Herkunftsort (RER = Europa; CH = Schweiz); Compartiment: Ort der Emission (Stadt, Land, ..)
Quelle: Gloor, 1995; Auftragseffizienz 95%, 2 Gew.-% Lösemittelemissionen (Talbert, 1998).
Beschichtungsstärke 70 µm; Pulverdichte 1300 kg/m3.


                                            10.2.2 Anteil an Produktionsabfall bei der Herstellung
                                            Die für die einzelnen Materialarten wurden aufgrund fehlender bauteilspezifischer
                                            Angaben der Anteil Produktionsabfall abgeschätzt. In Tabelle 10.8 sind die
                                            verwendeten Anteile für die einzelnen Materialgruppen aufgelistet.




                                            ecoinvent-report No. 25                        67
Ökologische Aspekte der Komfortlüftungen im Wohnbereich – Schlussbericht




   Tabelle 10.8              Anteil an Produktionsabfall in der Herstellung
    Produktionsabfall                                                         Anteil
    Bleche, Stahl, Aluminium                                                   10%
    Kupferdraht                                                                10%
    Kunststoff, Spritzguss                                                     10%
    Kunststoff, Extrusion                                                       5%
    Gummi                                                                       5%
    Dämmstoffe                                                                 10%
    Karton und Verpackungsfolien                                                2%


   Für die Entsorgung dieser Produktionsabfälle wird für die Metalle (Stahl,
   Aluminium, Kupfer) von einem Recycling ausgegangen. Für die Produktionsabfälle
   aus Kunststoff, Gummi, kunststoffbasierte Dämmstoffe (z.B. EPS) und Karton wird
   eine Entsorgung in einer Kehrichtsverbrennungsanlage angenommen. Bei der
   Spritzgussfertigung und Extrusion wird nur der nicht intern rezyklierbare Anteil der
   Produktionsabfälle berücksichtigt.


   10.2.3 Basisinventare
   Für alle Basisinventare wurden die Sachbilanzdaten aus der Datenbank ecoinvent
   (Datenbestand 1.01) bezogen. Die Sachbilanzen für Glaswolle und
   Unterlagsboden wurden mit den Sachbilanzdaten aus (Weibel & Stritz, 1995) und
   den Sachbilanzdaten aus ecoinvent berechnet, da die ecoinvent Inventare noch
   nicht zur Verfügung standen.
   Für die Bauteile aus Stahlblech wurde ein Konsummix von 37% Sekundär- und
   63% Primärstahl verwendet (gemäss Althaus et al., 2003). Für einzelne Bauteile
   (z.B. Transformatorbleche) wird von 100% Primärstahl ausgegangen.

   10.2.4 Strommix auf Niederspannungsniveau
   Für    die   Diskussion   der   Resultate    unter   Einbezug     verschiedener
   Stromproduktionsarten, wurde der Stromprozess ab Gaskombikraftwerk und ab
   Wasserkraftwerk aus der Datenbank ecoinvent (Datenbestand 1.01) mit den
   Prozessdaten für Stromtransport und Transformation auf Niederspannung
   erweitert. In Tabelle 10.9 sind die verwendeten Sachbilanzen für diese
   Anpassungen ersichlich. Die Daten dieser Sachbilanz basieren auf den Daten zum
   Schweizer Strommix ab Niederspannung. Für den Strombezug ab Photovoltaik
   wurden kein Stromtransport und Transformation berücksichtigt, da angenommen
   wurde, dass der Strom direkt auf dem Dach des Gebäudes produziert wird. Für
   den Strom aus Photovoltaik wurde daher folgender, Prozess direkt aus der
   Datenbank ecoinvent (Datenbestand 1.01) verwendet:
   – Strommix, Photovoltaik, ab Anlage, CH




   ecoinvent-report No. 25                       68
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
