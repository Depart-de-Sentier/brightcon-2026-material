You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Electricity, low voltage, production from hard coal, at grid` [CH], reference unit 1 kWh, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~7 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: energy supply, kbob recommendation / electricity, delivered via network
- includedProcesses: Included are the electricity production in 0, the transmission network as well as direct SF6-emissions to air. Electricity losses during low-voltage transmission and transformation from medium-voltage are accounted for.
- technology: Average technology used to distribute electricity. Includes underground and overhead lines, as well as air- and SF6-insulated medium-to-low voltage switching stations. Electricity production according to related datasets
- generalComment: This dataset describes the transformation from medium to low voltage as well as the distribution of electricity at low voltage.;
UUID: 02fd8be4-a33b-3cb5-a1ca-40bcbddb251a
- source cited in the metadata: Frischknecht R. | 2007 | 2007 - Electricy mix and grid - Frischknecht
- time period: 2004-01-2004-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kWh):
- Waste Heat: 0.163 megajoule (soil)

## Report excerpt

Source file: `report-p114-116.txt` (SHA-256 b55b40673db59d413f36be1b72aa8f42276ef2efcd330144e066f137d9cd7986), pages 114-116 of `2007 - Electricy mix and grid - Frischknecht.pdf`.

```
5. Kumulierte Resultate


     ten Stranglänge (siehe Tab. 4.5) errechnet sich ein Bedarf an Übertragungs- bzw. Verteilnetz von
     0.29mm/kWh, 0.032mm/kWh bzw. 0.0084mm/kWh auf Nieder-, Mittel- bzw. Hochspannungsebene.
     Da keine neuen Daten zur Stromverteilung in der Schweiz vorliegen, ist eine Aktualisierung der Infra-
     struktur-Berechnung nicht sinnvoll. Somit werden weiterhin die im Jahr 2000 berechnete Infrastruktu-
     raufwände pro transportierte Kilowattstunde benutzt.
     Der Bedarf an Infrastruktur Übertragungsnetz für 50km Ferntransport im Hochspannungsbereich wird
     bezogen auf eine Leitung mit 1GW Kapazität, 60% Auslastung und 30 Jahren Einsatzdauer berechnet.
     Entsprechend werden pro kWh zusätzlich 0.32µm Übertragungsnetz benötigt. Der mit den 50km Fern-
     transport verbundene Verlust beträgt zusätzlich 0.5% im Hochspannungsnetz.

     Tab. 4.24     Zusammenfassung der Eingabedaten für die Datensätze "Strom, Niederspannung, ab Netz", "Strom, Mittel-
                   spannung, an Netz", "Strom, Hochspannung, ab Netz"; Angaben für die regionale und lokale Stromver-
                                                                                        33
                   teilung basierend auf der Situation in der Schweiz im Jahr 2004


     Bezüger -->                                               Einheit        Niederspannung Mittelspannung Hochspannung

     Input:
     Strom, Mittelspannung, ab Netz                            kWh               1.104 2)
     Strom, Hochspannung, ab Netz                              kWh                             1.01
     Strom-Mix Schweiz                                         kWh                                              1.01 3)
     Schwefelhexafluorid                                       kg                3.80E-09      4.40E-08
     Übertragungsnetz, Strom, Niederspannung                   km                 2.94E-07
     Übertragungsnetz, Strom, Mittelspannung                   km                              3.24E-08
     Übertragungsnetz, Strom, Hochspannung                     km                                               8.44E-09
     Übertragungsnetz, Ferntransport (Tab. 4.22)               km                                               3.17E-10
     Emissionen Luft:
     Abwärme in Luft 1)                                        MJ                      0.087       0.019            0.033
     Ozon in Luft                                              kg                                               4.50E-06
     N2O in Luft                                               kg                                               5.00E-06
     SF6 in Luft                                               kg                2.19E-09      3.73E-08
     Emissionen Boden:
     Abwärme in Boden 1)                                       MJ                      0.262       0.015            0.002
     Output:
     Strom, Niederspannung, ab Netz                            kWh                1
     Strom, Mittelspannung, ab Netz                            kWh                             1
     Strom, Hochspannung, ab Netz                              kWh                                              1
                   1
                   ): Niederspannung: 25% der Abwärme in Luft, 75% in Boden; Mittelspannung: rund 55% der Abwärme in Luft, 45%
                     in Boden; Hochspannung: 95% der Abwärme in Luft, 5% in Boden; Verluste siehe Tab. 4.3.
                   2
                   ): inklusive Verteilverluste in Gebäuden (0.4%), siehe Tab. 4.12.
                   3
                   ): inklusive Verluste durch 50km Ferntransport (0.5%), siehe Tab. 4.21.




     Nachfolgend werden beispielhaft die Datensätze für die Strombereitstellung auf Ebene Hoch-, Mittel-
     und Niederspannung des Versorgungsmixes der Schweiz dargestellt. Für die anderen Länder bzw. die
     Erzeugungsmixe ändern sich die Verlustmengen und Höhe der SF6-Emissionen (gemäss Tab. 4.27)
     und die Nachfrage der Datensätze der entsprechenden Länder. Die Datensätze der Strombereitstellung




33
     Die Transportdistanzen wurden mit den Angaben und den Strombezügen aus dem Jahr 2000 berechnet.

     ecoinvent-Bericht Nr. 6                                        - 106 -
                                                                        5. Kumulierte Resultate


der übrigen Länder können dem ecoinvent Datenbestand via Internet (www.ecoinvent.ch) entnommen
werden.

Tab. 4.25        Sachbilanzdaten für das Modul " Strom, Hochspannung / Mittelspannung / Niederspannung, ab Netz (CH)"




                                                                                                                                                                  UncertaintyTyp

                                                                                                                                                                                   StandardDevia
                                                                                    InfrastructureP
                                                                                                             electricity, high   electricity,  electricity, low




                                                                         Location




                                                                                                                                                                                      tion95%
                                                                                                                voltage,       medium voltage,    voltage,




                                                                                                      Unit
                                               Name                                                                                                                                                GeneralComment




                                                                                                                                                                        e
                                                                                                             production CH, production CH, production CH,
                                                                                                                 at grid           at grid         at grid

                                               Location                                                            CH               CH                CH
                                        InfrastructureProcess                                                       0                0                 0
                                                 Unit                                                             kWh              kWh               kWh
product           electricity, high voltage, production CH, at grid     CH              0 kWh                       1
                  electricity, medium voltage, production CH, at grid   CH              0 kWh                                        1
                  electricity, low voltage, production CH, at grid      CH              0 kWh                                                         1
                                                                                                                                                                                                   (1,1,1,1,1,1); specific losses of
technosphere     electricity, production mix CH                         CH              0 kWh                   1.01E+0                                                1            1.05           network estimated based on
                                                                                                                                                                                                   statistics
                                                                                                                                                                                                   (1,1,1,1,1,1); specific losses of
                  electricity, high voltage, production CH, at grid     CH              0 kWh                                    1.01E+0                               1            1.05           network estimated based on
                                                                                                                                                                                                   statistics
                                                                                                                                                                                                   (1,1,1,1,1,1); specific losses of
                  electricity, medium voltage, production CH, at grid   CH              0 kWh                                                      1.10E+0             1            1.05
                                                                                                                                                                                                   network estimated based on
                  sulphur hexafluoride, liquid, at plant                RER             0             kg                          3.73E-8          2.19E-9             1            1.08           (1,1,2,1,1,3); based on emission data
                                                                                                                                                                                                   (3,1,4,1,3,5); based on consumption
                  transmission network, long-distance                   UCTE 1                        km       3.17E-10                                                1            3.15
                                                                                                                                                                                                   statistics
                                                                                                                                                                                                   (3,1,4,1,3,5); based on consumption
                  transmission network, electricity, high voltage       CH              1             km        8.44E-9                                                1            3.15
                                                                                                                                                                                                   statistics
                                                                                                                                                                                                   (3,1,4,1,3,5); based on consumption
                  transmission network, electricity, medium voltage     CH              1             km                          3.24E-8                              1            3.15
                                                                                                                                                                                                   statistics
                                                                                                                                                                                                   (3,1,4,1,3,5); based on consumption
                  distribution network, electricity, low voltage        CH              1             km                                           2.94E-7             1            3.15
                                                                                                                                                                                                   statistics
emission soil,                                                                                                                                                                                     (4,1,3,1,1,5); estimations based on
                  Heat, waste                                               -            -            MJ        1.78E-3           1.65E-2          2.81E-1             1            1.32
unspecified                                                                                                                                                                                        losses
emission air,                                                                                                                                                                                      (4,1,3,1,1,5); estimations based on
                  Heat, waste                                               -            -            MJ        3.39E-2           2.01E-2          9.37E-2             1            1.32
unspecified                                                                                                                                                                                        losses
                                                                                                                                                                                                   (-,-,-,-,-,-); standard deviation based
                  Ozone                                                     -            -            kg        4.50E-6                                                1            5.00
                                                                                                                                                                                                   on variation reported in literature
                                                                                                                                                                                                   (-,-,-,-,-,-); standard deviation based
                  Dinitrogen monoxide                                       -            -            kg        5.00E-6                                                1            4.60
                                                                                                                                                                                                   on variation reported in literature
                  Sulfur hexafluoride                                       -            -            kg                          3.73E-8          2.19E-9             1            1.51           (1,1,2,1,1,3); national statistics




4.3.4            Stromverteilung in den europäischen Ländern
Übersicht
Für die ecoinvent Datenbank wird die Strombereitstellung nicht nur für die Schweiz, sondern auch für
andere europäische Länder bilanziert. Sowohl die vorgelagerten Energieketten, als auch Produktions-
prozesse für Materialien und Anlagen beziehen Strom in verschiedenen Ländern Europas, des Nahen
Ostens, Asiens etc.. Auf der Produktionsseite wird in den einzelnen Berichtsteilen der Energieträger
Erdöl, Erdgas, Kohle, Kernenergie, Wasserkraft, Windenergie, Holzenergie und Photovoltaik die
Stromproduktion in Kraftwerken der Länder des UCTE-, des NORDEL- und des CENTREL-
Verbundes beschrieben. In diesem Kapitel werden sowohl die Anbindung des schweizerischen Ver-
teilnetzes an das europäische Stromnetz als auch Stromtransport und Stromverteilung in anderen eu-
ropäischen Ländern berücksichtigt. Wegen mangelnder Informationen müssen Vereinfachungen ge-
troffen werden.
Für das durchschnittliche regionale Verteilnetz werden in erster Näherung die Angaben aus der Inven-
tarisierung des Schweizer Netzes verwendet. Inwiefern ist dies zulässig? Die Schweiz, mit ländlichen
Regionen (niedrige Anschlussdichte) und mit einem zentralen Ballungsgebiet (Mittelland mit hoher
Anschlussdichte), dürfte nicht allzu atypisch für west- und mitteleuropäische Verhältnisse sein.
Die Angaben für die Schweiz beruhen auf dem schweizerischen Bezugsmodell von Tab. 4.1. In Tab.
4.26 wird das Bezugsmodell für den UCTE-Verbund skizziert. Genaue Angaben über die Spannungs-
höhe des Strombezugs lagen nicht vor. Pauschal werden 80 % des Dienstleistungssektors den Nieder-
spannungsbezügern und 80 % des industriellen Verbrauchs den Hoch-/Mittelspannungsbezügern zu-
geordnet. Daraus resultiert, dass ca. 58% des Stromes als Niederspannung bezogen wird, die restlichen
42% als Mittelspannung und Hochspannung (siehe Tab. 4.26). Dieses Bild weicht nur schwach von



ecoinvent-Bericht Nr. 6                                                                                  - 107 -
                                               5. Kumulierte Resultate


der Situation der Schweiz ab (Niederspannung: 60%, Mittelspannung: 30%, Hochspannung: 10%,
siehe Tab. 4.1)
Im Bewusstsein, dass es sich um eine grobe Näherung handelt, werden deshalb die Angaben aus dem
schweizerischen Netzinventar zur Beschreibung durchschnittlicher länderspezifischer UCTE-Verteil-
netze verwendet. Einzig für Finnland wird mit einer anderen Absatzstruktur gerechnet (siehe unten).

Tab. 4.26   Bezugsmodell für IEA-Länder von Europa (OECD/IEA 2006, p.107)


                               Verbrauch               Bezug Hoch- oder     Bezug Nieder-
                                                       Mittelspannung       spannung
                               TWh                     TWh                  TWh
  Industrie                    1150                    920 (80%)            230
  Haushalte                    807                                          807
  Dienstleistungen             696                     139                  557 (80%)
  Transport, Rest              126                     101                  25
  Summe                        2779                    1160 (42%)           1619 (58%)



Sachbilanz des Strombezugs, Netzverluste und SF6-Emissionen
Die nachfolgenden Tabellen beschreiben die Infrastrukturaufwendungen und die Verluste, die mit
dem Bezug von 1kWh im jeweiligen Spannungsbereich verbunden sind. Die Verluste sind je nach
Spannungsniveau unterschiedlich; je tiefer das Niveau, desto höher werden die Verluste. Die SF6-
Emissionen dagegen werden hauptsächlich durch die Hochspannungs-Schaltanlagen verursacht, die
dem Mittelspannungsstrombezüger zugeordnet sind. Die Datensätze für die jeweiligen Länder unter-
scheiden sich hauptsächlich durch die Herkunft des bezogenen Stroms.
Nachfolgend werden für alle Länder Angaben zu den Netzverlusten und den SF6-Emissionen gemacht.
Sind keine länderspezifischen Angaben verfügbar, werden die für die Schweiz, Deutschland, Däne-
mark bzw. Grossbritannien geltenden Werte übernommen (siehe Tab. 4.27).
Die Netzverluste sind einerseits abhängig von der Siedlungsdichte eines Landes und anderseits vom
technischen Stand der Infrastruktur. Tab. 4.27 zeigt Angaben über Netzverluste für die bilanzierten
Länder. Die Aufteilung auf die drei Spannungsebenen wurde mit Ausnahme von Finnland gemäss den
Grundlagen für die Schweiz vorgenommen. Für Finnland, das einen sehr hohen Anteil Strombedarf
im zweiten Sektor aufweist (Aufteilung Verbrauch: 40% Hoch-, 30% Mittel-, und 30% Niederspan-
nung), werden die (vergleichsweise tiefen durchschnittlichen) Verluste zu 5% auf Hoch-, 10% auf
Mittel- und 85% auf Niederspannungsebene angenommen.
Für Länder die keine Angaben machen, werden mit Ausnahme von Luxemburg und Holland die An-
gaben zu den Netzverlusten aus OECD/IEA (2006) übernommen. Für Luxemburg und Holland wer-
den näherungsweise die Werte der Schweiz verwendet. Für die Datensätze der Netzverbunde UCTE
und NORDEL werden mit dem Produktionsvolumen gewichtete Durchschnittswerte verwendet.
Für die SF6-Emissionen liegen nur wenige länderspezifische Werte vor. Für die übrigen UCTE- und
CENTREL-Länder wird die Emissionsrate Deutschlands verwendet, für die NORDEL Staaten der
Wert Dänemarks und für Irland der Wert Grossbritanniens. Die Einsatzmenge SF6 pro kWh Strom ist
in allen Datensätzen identisch und entspricht dem Wert des schweizerischen Netzes.




ecoinvent-Bericht Nr. 6                                - 108 -
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 kWh.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
