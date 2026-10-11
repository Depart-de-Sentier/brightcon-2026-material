You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Gravel, crushed, market mix, at regional storage` [CH], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~5 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: construction materials / others
- includedProcesses: This data set accounts for 1 kg of gravel at the regional storage. 19% are from import, 81% are produced in Switzerland. The imported goods are delievered to Switzerland to 36% from Germany, 26% from Italy 23% from France and 14% from Austria. 13% are delievered by freight train, 78% by lorry and 8% by barge.
- technology: undefined
- generalComment: pipeline transport is modelled as freight train transport.;
UUID: 1d5b4602-52cb-388e-87df-703f4eb37e6f
- source cited in the metadata: Kasser U. | 2016 | 2016 - Renewal and exp. of LCA data in KBOB - Kasser
- time period: 2014-01-2014-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p46-48.txt` (SHA-256 0f5a06cb1eab847503da0f60a1fc1f3040db5e3efac8cee9f58b04fc03251534), pages 46-48 of `2016 - Renewal and expansion of LCA data in KBOB - Kasser.pdf`.

```
Projekt QualiBOB – Teilbericht A Marktsituation ausgewählter Baustoffe




           produzierte, die importierte und die in der Schweiz verbrauchte Menge an Kies und
           Sand gemäss der Gesamtumweltrechnung vom BfS (2014). Dabei steht offen wie
           viel davon rezyklierter und wie viel primärer Kies und Sand ist.


           Tabelle 2: Tonnagen an Kies und Sand, welche in der Schweiz durchschnittlich in den Jahren
           2000 bis 2011 pro Jahr produziert, importiert und verbraucht wurden
                                    Produktion                                 Verbrauch
                                                           Import                            Anteil Import
               Material             Schweiz                                    Schweiz
                                    t/a                    t/a                 t/a           %
               Kies und Sand        31'499'000             7'495'000           38‘994'000    19%



           Kies und Sand werden aus den umliegenden Ländern importiert. Da die Aussen-
           handelsstatistik keine Unterscheidung zwischen gebrochenem Kies, Rundkies und
           Sand zulässt, wird davon ausgegangen, dass die Herkunftsanteile gemäss Aussen-
           handelsstatistik für gebrochenen Kies, Rundkies und Sand gleichermassen zutref-
           fend sind.
           Tabelle 3 zeigt die Ursprungsländer, aus welchen Sand und Kies in die Schweiz im-
           portiert werden sowie deren Transportdistanzen auf. Die Importanteile der Her-
           kunftsländer stammen aus der Aussenhandelsstatistik. Ausländische Abbaustellen
           von Gesteinskörnungen liegen in der Regel unmittelbar hinter der Grenze. Dabei
           importieren nur Schweizer Betriebe nahe der Grenze zum jeweiligen Herkunftsland
           Kies und Sand aus diesem Land3. Aufgrund der dezentralen Versorgung ist eine
           durchschnittliche Transportdistanz von 20 km vorauszusetzen für primären Kies und
           Sand3. Für rezyklierte Gesteinskörnung müsste die Transportdistanz verdoppelt
           werden, da diese grossmehrheitlich an zentralen Standorten und selten direkt vor
           Ort aufbereitet wird4.


           Tabelle 3: Herkunftsland sowie prozentuale Anteile und Transportdistanz aus dem Herkunfts-
           land nach Bern für die in die Schweiz importierte Menge an Kies und Sand (Eidgenössische-
           Zollverwaltung-EZV 2012)
                                    Importanteil                         Distanz
               Herkunftsland
                                    %                                    km
               Deutschland          36%                                  20
               Italien              26%                                  20
               Frankreich           23%                                  20
               Österreich           14%                                  20
               Durchschnittliche, gewichtete Transportdistanz            20




           3
                Persönliche Mitteilung, Ernst Honegger, Leiter Technik beim FSKB, vom 28. Oktober 2015
           4
                Persönliche Mitteilung, Ernst Honegger, Leiter Technik beim FSKB, vom 13. Oktober 2015




BFE Forschungsprojekt Schlussbericht, Januar 2016                                                            A-5
Projekt QualiBOB – Teilbericht A Marktsituation ausgewählter Baustoffe




           Tabelle 4 zeigt die Aufteilung der Transportmittel gemäss Aussenhandelsstatistik,
           mit welchen die Güter in die Schweiz transportiert werden. Berücksichtigt wird dabei
           die Kategorie SITC-273, Steine, Sand und Kies‘. Die Pipeline-Transporte werden als
           Transport mit dem Güterzug modelliert, da wohl weder Kies noch Sand per Pipeline
           in die Schweiz eingeführt werden. Der FSKB (Fachverband der Schweizerischen
           Kies- und Betonindustrie) stimmt dieser Aufteilung der Transportarten für die impor-
           tierten Gesteinskörnungen zu4.


           Tabelle 4: Transportmittel mit welchen Kies und Sand in die Schweiz importiert werden, gemäss
           Aussenhandelsstatistik, SITC-Nummer 273 (Eidgenössische-Zollverwaltung-EZV 2012)

                                                        Bahnver-                        Strassen-                                     Luftver-                                                                                Schiffs-
              Transportmittel                                                                                                                                      Pipeline                                                              Total
                                                        kehr                            verkehr                                       kehr                                                                                    verkehr

              Anteil                                    1%                              78%                                           0%                           12%                                                        8%         100%



           Die Sachbilanzdaten zur Modellierung der aktuellen Marktsituation von primärem
           Kies und Sand sind in Tabelle 5 festgehalten.


           Tabelle 5: Sachbilanzdaten zur Bilanzierung von 1 kg der Baustoffe ‚Kies gebrochen‘, ‚Rund-
           kies‘ und ‚Sand‘ für den Schweizer Markt
                                                                                                                                                                                                StandardDeviation95%
                                                                                        InfrastructureProcess




                                                                                                                                                                              UncertaintyType
                                                                             Location




                                                                                                                       gravel, crushed, gravel, round,      sand, market
                                                                                                                Unit




                                                     Name                                                               market mix, at   market mix, at    mix, at regional                                            GeneralComment
                                                                                                                       regional storage regional storage       storage




                                                 Location                                                                    CH               CH                 CH
                                         InfrastructureProcess                                                                0                0                  0
                                                   Unit                                                                      kg               kg                 kg

            product       gravel, crushed, market mix, at regional storage   CH            0                    kg            1                0                  0
                          gravel, round, market mix, at regional storage     CH            0                    kg            0                1                  0
                          sand, market mix, at regional storage              CH            0                    kg            0                0                  1
            technosphere gravel, crushed, at mine                            CH            0                    kg         1.00E+0                                                1 1.05 (1,1,1,1,1,1,BU:1.05); 1 kg Kies;

                          gravel, round, at mine                             CH            0                    kg                          1.00E+0                               1 1.05 (1,1,1,1,1,1,BU:1.05); 1 kg Kies;

                          sand, at mine                                      CH            0                    kg                                            1.00E+0             1 1.05 (1,1,1,1,1,1,BU:1.05); 1 kg Sand;
                                                                                                                                                                                         (4,5,na,na,na,na,BU:2); Gewichtete Durchschnittsdistanz für
                          transport, lorry >16t, fleet average               RER           0                    tkm        3.02E-3          3.02E-3           3.02E-3             1 2.09
                                                                                                                                                                                         Sand und Kies beträgt 20 km;
                                                                                                                                                                                         (4,5,na,na,na,na,BU:2); Gewichtete Durchschnittsdistanz für
                          transport, freight, rail                           RER           0                    tkm        5.05E-4          5.05E-4           5.05E-4             1 2.09
                                                                                                                                                                                         Sand und Kies beträgt 20 km;
                                                                                                                                                                                         (4,5,na,na,na,na,BU:2); Gewichtete Durchschnittsdistanz für
                          transport, barge                                   RER           0                    tkm        3.23E-4          3.23E-4           3.23E-4             1 2.09
                                                                                                                                                                                         Sand und Kies beträgt 20 km;




A.3.2.2 Resultate
           Die Umweltbelastungen von Kies und Sand ab Regionallager sind in Tabelle 6 auf-
           geführt. Diese weichen bis zu 18 % von den bisherigen, in der KBOB-Empfehlung
           aufgeführten Umweltbelastungen ab (siehe auch Abbildung 1).




BFE Forschungsprojekt Schlussbericht, Januar 2016                                                                                                                                                                                                 A-6
Projekt QualiBOB – Teilbericht A Marktsituation ausgewählter Baustoffe




           Tabelle 6: Umweltbelastungen pro kg Kies beziehungsweise Sand für den Schweizer Markt ge-
           messen als Gesamtumweltbelastung, Primärenergie gesamt und nicht erneuerbar sowie als
           Treibhausgasemissionen
                                                                    Primär-    Primär-         Treibhaus-
                                                 UBP‘2013           energie    energie nicht   gasemissio-
             Baustoff / -element      Bezug                         gesamt     erneuerbar      nen
                                                 UBP                MJ Öl-eq   MJ Öl-eq        kg CO2-eq
             Sand                     kg         35.9               0.067      0.062           0.0028
             Kies, gebrochen          kg         40.0               0.151      0.136           0.0048
             Kies, rund               kg         35.9               0.067      0.062           0.0028



           Die relativen Änderungen der Umweltbelastung von Sand und Kies des Schweizer
           Datensatzes zum Marktmix sind in Abbildung 1 dargestellt. Die Linie in dunkelrot bei
           100 % steht für die Umweltbelastung von Sand und Kies ab Schweizer Werk, wäh-
           rend die orangen Balken das relative Verhältnis des Marktmixes dazu aufzeigen.
           Bei allen drei Baustoffen nehmen die Umweltbelastungen ab Regionallager (um bis
           zu 18 % bei den Treibhausgasemissionen) zu. Die Umweltbelastung der Gewinnung
           von Sand und Kies überwiegt den Transport vom Ausland in die Schweiz. Am ge-
           ringsten schlägt der zusätzliche Transport beim Indikator Gesamtumweltbelastung
           zu Buche, weil bei dieser Methode zusätzlich noch die Ressourcenentnahme be-
           rücksichtigt wird.




           Abbildung 1: Relative Umweltbelastungen von Sand und Kies ab Regionallager im Vergleich zu
           den Umweltbelastungen der Schweizer Produkte ab Werk (gemessen als Gesamtumweltbelas-
           tung, Primärenergie gesamt und nicht erneuerbar sowie Treibhausgasemissionen). UBP‘2013:
           Gesamtumweltbelastung; PE: Primärenergie gesamt; PE nr: Primärenergie nicht erneuerbar;
           THG: Treibhausgasemissionen



           In Abbildung 2 wird für jeden Baustoff die Umweltbelastung des Marktmixes (die
           entsprechenden orangen Balken in Abbildung 1 wurden nun auf 100 % skaliert)
           aufgezeigt, welcher sich aus dem Anteil der Umweltbelastung der Schweizer Pro-
           dukte ab Werk (= (1-Importanteil) * Umweltbelastung Datensatz Schweiz / Umwelt-
           belastung Marktmix) und dem Anteil der Umweltbelastung der importierten Produkte
           (Kehrwert von Anteil Belastung Schweiz) zusammensetzt. Die dunkelroten Balken,
           welche der dunkelroten Linie aus Abbildung 1 entsprechen, zeigen den relativen An-
           teil der Umweltbelastung der Schweizer und die blauen Balken den relativen Anteil
           der Umweltbelastung der importierten Produkte (inklusive deren Herstellung) auf.


BFE Forschungsprojekt Schlussbericht, Januar 2016                                                          A-7
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
