You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Heat distribution, hydronic radiant floor heating, 150m2` [CH], reference unit 1 p, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~12 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: energy, obsolete / heat, obsolete\heat pumps, obsolete\infrastructure
- includedProcesses: The module includes the most important materials and transport needed for production.
- technology: Underfloor heating.
- generalComment: Average infrastructure.;
Synonyms: floor radiation heating, radiant floor heating, hydronic radiant floor heating; 
UUID: d4f0b20e-20b9-322f-a0a8-71083885972b
- source cited in the metadata: Heck T. | 2007 | 2007 - Heat pumps - Heck
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 p):
- Water: 0.45 cubic meter (Resources Resources from water Renewable material resources from water)

## Report excerpt

Source file: `report-p27-29.txt` (SHA-256 e389669a5dbb4e804338592a203b13b1a28cfb7fd809ce491e60f371db330ee3), pages 27-29 of `2007 - Heat pumps - Heck.pdf`.

```
5. Sachbilanz der Wärmepumpen




           2.       Lastwagen (11 t Gesamtgewicht):            100 km
                    Modul: Transport LKW 16 t
                    durchschnittliche Zuladung: 3.4 t
           3.       Lastwagen (3.5 t Gesamtgewicht):           160 km
                    Modul: Transport Lieferwagen < 3.5 t
                    durchschnittliche Zuladung 0.63 t
Aus der durchschnittlichen Zuladung in Tonnen und der zurückgelegten Distanz lassen sich die tkm
(Tonnen*Kilometer) errechnen.
Da der Kalziumbentonit in Süddeutschland abgebaut wird, muss der Transport dieses Materials separat
berücksichtigt werden. Als mittlere Transportdistanz werden 300 km angenommen. Der Transport erfolgt mit
Lastwagen bis zu 16 t (Rasch 1993).
Als Abfall fallen während des Bohrprozesses (Spülung) ca. 1 m3 Gesteinsmaterial und Bentonitsuspension
an. Die durchschnittliche Dichte dieses Materials beträgt 2500 kg/m3. Es wird auf einer Inertstoffdeponie
abgelagert. Nach Ende des Betriebes wird die Erdwärmesonde im Boden belassen. Die Wasser-
Ethylenglykolmischung aus dem Wärmequellenkreislauf wird nach Rückgabe an den Lieferanten speziell
behandelt, dies wird durch das Modul "Behandlung, Wärmeträgerflüssigkeit, 40% C3H8O2, in
Abwasserreinigung, Gr.Kl. 2" berücksichtigt.
In Tab. 5.2 sind die Eingabedaten für den Bau der Erdsonde zusammengestellt.



Tab. 5.2    Eingabedaten des Moduls "Erdwärmesonde 150 m".


                  Erdwärmesonde 150 m                                     [Stk]
                  INPUT
                  Basismaterialien:
                  Stahl unlegiert                                 33      kg
                  Polyethylen (LD) 1)                            180      kg
                  Bentonit                                         8      kg
                  Zement                                          33      kg
                  Ethylenglykol                                  102      kg
                  Ressourcen:
                  Wasser                                          10.2    m3
                  Allg. Dienstleistung/Energie:
                  Diesel in Baumaschine                         5'900     MJ
                  Transporte:
                  Transport Lieferwagen < 3.5 t                  100      tkm
                  Transport LKW 16 t                             712      tkm
                  OUTPUT
                  Abfälle:
                  Abfälle in Inertstoffdeponie                  2'500     kg
                  Behandlung, Wärmeträgerflüssigkeit,               0.3   m3
                  40% C3H8O2, in Abwasserreinigung,
                  Gr.Kl. 2 2)
                  1) eigentlich PE (MD)




ecoinvent-Bericht No. 6 – Teil X                        -19-
                                         5. Sachbilanz der Wärmepumpen




5.1.3 Wärmeverteilsystem
Als Wärmeverteilsystem (WVS) wird eine Fussbodenheizung (Niedertemperatur) mit 40 ˚C Vorlauf-
temperatur und 30-35 ˚C Rücklauftemperatur angenommen. Die Energiebezugsfläche misst 165 m2, die zu
beheizende Nettogeschossfläche 150 m2.


Materialeinsatz und Bauaufwand
Von den 150 m2 Nettogeschossfläche sind 75 m2 von unten beheizt, 75 m2 sind von unten nicht beheizt
(Kellergeschoss). Die Isolation besteht aus 2 cm Polystyrol (Toschi 1993). Die Dichte von Polystyrol beträgt
22 kg/m3 (Recknagel et al. 1988/89). Als Fussbodenheizung wird ein System mit Kunststoffrohren und
Aluminiumwärmeleitlamellen zur besseren Wärmeübertragung gewählt. Bei diesem System werden die
Heizrohre (VPE-Rohr, Durchmesser 20 mm, Wandstärke 2 mm) auf die Isolation verlegt. Die Rohrabstände
betragen 30 cm. Die verlegten Rohre und Wärmeleitlamellen werden mit einem Bauplastik (PE (LD)
0.2 mm) abgedeckt, bevor der Zementestrich mit einer Dicke von 8 cm (6 cm über dem Rohr) aufgetragen
wird. Der Zementestrich besteht aus etwa 300 kg Zement, 1550 kg Sand und 150 kg Wasser pro m3
Frischmörtel (2000 kg/m3) (Toschi 1993). Für ecoinvent wird lediglich der Unterschied zum Aufbau eines
gewöhnlichen Bodens (Dicke 6 cm) aufgeführt.
Auf den Einbau eines Pufferspeichers wird bei Einfamilienhäusern, meist aus Kostengründen, verzichtet. In
diesem Fall ist es jedoch sehr wichtig, dass die drei Kreisläufe mit Hilfe der Drosselorgane so aufeinander
abgestimmt werden, dass eine optimale Wärmeübertragung jederzeit möglich ist (Keel 1993).
Aus transportiertem Material (5900 kg pro Wärmeverteilsystem) und Standarddistanzen ergeben sich
folgende Transportleistungen: 160 tkm Schiene, 128 tkm LKW 28 t.
Beim Abbruch des Wärmeverteilnetzes wird davon ausgegangen, dass ein grosser Teil der Materialien auf
einer Inertstoffdeponie abgelagert wird. Es wird angenommen, dass Kunststoff in einer Verbrennungsanlage
verbrannt wird.
Die Daten der Infrastruktur für die Wärmeverteilung sind in Tab. 5.3 zusammengestellt.



Tab. 5.3    Eingabedaten des Moduls "Wärmeverteilung, Fussbodenheizung, 150 m2".


                  Wärmeverteilung, Fussbodenheizung, 150 m2               [Stk]
                  INPUT
                  Basismaterialien:
                  Aluminium, Produktionsmix, ab Werk          126         kg
                  Polystyrol schlagfest                        66         kg
                  Polyethylen (LD)                            101         kg
                  Zement                                      900         kg
                  Sand für Bau                              4'650         kg
                  Ressourcen:
                  Wasser                                        0.45      m3
                  Transporte:
                  Transport Schiene                           160         tkm
                  Transport LKW 28 t                          128         tkm
                  OUTPUT
                  Abfälle:
                  Abfall in Inertstoffdeponie               5'730         kg
                  Kunststoff in Verbrennungsanlage            167         kg




ecoinvent-Bericht No. 6 – Teil X                      -20-
                                      5. Sachbilanz der Wärmepumpen




5.2       Lebensdauern
Zur Verknüpfung der Infrastrukturmodule mit den Nutzwärmemodulen wird eine Abschätzung der
Lebensdauern benötigt.


5.2.1 Lebensdauer der Wärmepumpe
Eine aktuelle amerikanische Studie zur Lebensdauer von Wärmepumpen kommt zu folgenden Ergebnissen
(Lovvorn, 2001a; Lovvorn, 2001b):
     •    Der Median der Lebensdauer („Median service life“) liegt bei ungefähr 20 Jahren. Dies stimmt mit
          den Ergebnissen einer älteren Studie aus dem Jahr 1984 überein (Lovvorn 2001a).
     •    Mehr als die Hälfte der Wärmepumpen war zum Zeitpunkt der Auswechslung noch funktionsfähig.
Der Austausch der WP erfolgte laut der genannten Studie nicht nur deshalb, weil die alte WP defekt war,
sondern auch aus vorsorglichen Gründen wegen Alterung und auf Empfehlung von Anbietern. Für die
Umlegung der Aufwendungen zur Herstellung auf ein MJ erzeugter Wärme kommt es auf die reale
Nutzungsdauer an. Es spielt im Prinzip keine Rolle, aus welchen Gründen das Gerät ausser Betrieb
genommen und durch ein neues ersetzt wird. Allerdings beeinflusst der Unterschied zwischen „technisch
möglicher Lebensdauer“ und „realer Betriebsdauer“ die Übertragbarkeit der Lebensdauerergebnisse auf
andere Länder. Bei gleicher Technologie kann die reale Lebensdauer aufgrund unterschiedlicher
Gewohnheiten je nach Land oder Kulturkreis variieren.
Für die Wärmepumpen wird hier gemäss den genannten Studien (Lovvorn, 2001a; Lovvorn, 2001b) eine
Lebensdauer von 20 Jahren angenommen. Dies stimmt auch mit anderen Quellen überein (Hess 1993).
Unsicherheit: Als Bereich für die Lebensdauer wird 16 bis mehr als 20 Jahre angegeben (Lovvorn 2001b).
Die Bereichsangabe beruht auf einer älteren Studie, neuere Werte sind nicht angegeben. In Anlehnung daran
wird hier ein Unsicherheitsfaktor von 1.5 für die Lebensdauer der Wärmepumpe abgeschätzt.


5.2.2 Lebensdauer der Erdwärmesonde
Für die Lebensdauer der Erdwärmesonde schwanken die Angaben zwischen 30 Jahren (Rohner 1993) und
100 Jahren (für Sonden aus Polyethylen PE 100, (Luder 2003)).
In Anlehnung an diese Spanne wird hier eine Lebensdauer von 50 Jahren mit einer Unsicherheit von SDg2=2
angenommen.


5.2.3 Lebensdauer des Wärmeverteilsystems
Für die übrigen Komponenten werden die gleichen Annahmen wie für die Wärmepumpe gemacht, d.h. die
Lebensdauer wird mit 20 Jahren angenommen.




5.3       Betrieb
5.3.1 Gemessene Jahresarbeitszahlen
Für Wärmepumpenanlagen in der Schweiz liegt eine umfangreiche Feldanalyse vor (Erb et al. 2000).
Demnach ergaben Hochrechnungen aus Messungen im Schweizer Durchschnitt eine Jahresarbeitszahl (JAZ
2) von 3.2 für 1998 erstellte Anlagen. 1994/1995 lag die Jahresarbeitszahl im Schweizer Durchschnitt erst
bei 2.6 (Erb&Hubacher 2001a). Bei Messungen über mehrere Jahre konnte keine signifikante
Verschlechterung der Jahresarbeitszahl mit zunehmendem Alter der Wärmepumpe festgestellt werden. Es

ecoinvent-Bericht No. 6 – Teil X                  -21-
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 p.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
