You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `NOx retained, in SCR` [GLO], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~6 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: power plants / unspecified
- includedProcesses: The module describes the operation of a Selective Catalytic Reduction DeNOx. The module includes the ammonia requirement and its transport as well as the disposal of the used catalysator.
- technology: Average installed technology in the 1990s.
- generalComment: The assumed efficiency of the SCR is about 80 %. The waste includes the used catalysator.;
Synonyms: DeNOx; 
UUID: 06e130f9-c6ff-366e-901c-418667fb6f46
- source cited in the metadata: Dones R. | 2007 | 2007 - Coal - Dones
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p140-141.txt` (SHA-256 86d5928bc5c8ff996e87717341b3a7b8710a78d5b85327fba1e4521809d08164), pages 140-141 of `2007 - Coal - Dones.pdf`.

```
9. Kraftwerke

9.5.4       Entstickung
Überblick
Die folgenden Angaben zur Entstickung der Abgase stammen aus der letzten Version der Ökoinventare.
Aufgrund der nicht zu erwartenden Änderungen wurde auf eine Überarbeitung verzichtet.
Bei den DeNOx-Verfahren stehen die primären Massnahmen (Abgasrezirkulation, Stufenverbrennung, Low-
NOx-Brenner) im Vordergrund. Führen diese Massnahmen einzeln oder in Kombination nicht zum
erwünschten Emissionswert, können selektive katalytische oder nichtkatalytische Reduktions-Verfahren
eingesetzt werden.
Für die Entstickung werden meist die primären Massnahmen eingesetzt, welche zusammen die NOx-
Emissionen bis zu 60% reduzieren können. Es sind dazu lediglich bauliche Massnahmen nötig,
Betriebsmittel werden keine eingesetzt. Deshalb erübrigt sich hier eine weitere Behandlung. Die selektive
katalytische Reduktion wird bei grösseren Kohlefeuerungen als sekundäres DeNOx-System eingesetzt und
soll näher beschrieben werden.
Mit feuerungstechnischen Primärmassnahmen lassen sich die Emissionen von Trockenfeuerungen auf
450 mg/m3 und von Schmelzkammerfeuerungen auf 900 mg/m3 senken. Braunkohle-Trockenfeuerungen
erreichen sogar bis zu 200 mg/m3 und können damit auch die schärfsten Grenzwerte ohne sekundäre
Entstickung einhalten.
Selektive katalytische Reduktion (SCR)
Mit dem Reduktionsmittel Ammoniak (NH3) sollen die Stickoxide in Stickstoff und Wasser umgesetzt
werden. Damit diese Reaktionen auch bei tiefen Rauchgastemperaturen genügend schnell ablaufen, braucht
es einen Katalysator aus Metalloxiden, Molekularsieb, Aktivkohle oder -koks. Beim SCR-Verfahren werden
Wirkungsgrade von 80% bis 90% erreicht.

Tab. 9.37: Auslegegrössen für eine SCR-Anlage bei Kohlefeuerungen (IIP 1990)


                                                         Einheit               Kohlefeuerungen
               Space Velocity*                             1/h                  2000 bis 3000
                                                                3
               Katalysatorkosten                         Euro/m                10000 bis 12500
               Katalysatorstandzeit                         a                      2 bis 3
               Molverhältnis NH3/NO                         -                        0.8

* Verhältnis Rauchgasvolumenstrom (m3/h) zu Katalysatorvolumen (m³).

Mit NH3/NOx-Molverhältnissen von ca. 0.8 werden bei grossen Kohlekraftwerken NOx-Minderungsraten bis
zu 85% erreicht (IIP 1990).
Diese SCR-Anlagen können vor (high dust) oder nach (low dust) dem Staubabscheider oder sogar nach der
REA eingebaut werden.
Da die NOx-Konzentration aus dem Kessel schwankt, die Katalysatorleistung bei andauernder Standzeit
zunimmt und die Katalysatorbelastung bei Lastwechsel ändert, muss die SCR-Anlage gut geregelt werden,
damit der NH3-Schlupf nicht zu gross wird. Das NH3 reagiert auch mit dem SO3 zu
Ammoniumhydrogensulfat, welches zur Inaktivierung des Katalysators führen kann (IIP 1990).
Der stöchiometrische Ammoniakbedarf beträgt 0.38 kg pro kg NO. Da mit der NO-Bildung auch noch
Nebenreaktionen ablaufen, werden effektiv 0.45 kg Ammoniak pro kg NO resp. 0.3 kg NH3 pro kg NO2
verbraucht. Das verbrauchte Katalysatorvolumen beträgt bei einer Reduktion von 1000 mg NOx/m3 auf
200 mg/m3 mit den obigen Annahmen rund 0.04 m3/t NOx und verursacht dabei Investitionskosten (inkl.
Montage und Entsorgung) von rund 450 Euro/t NOx. Mit der spezifischen Dichte von 0.66 t/m3
(Marx et al. 1990) resultiert ein spezifischer Bedarf von 26 kg Katalysator pro t NOx. Bei einem spezifischen
Katalysatorgewicht von 0.87 t/MW (Wagner 1989) ergibt sich ein Katalysatorverbrauch von rund
24 kg/t NOx, was gut mit dem obigen Wert übereinstimmt. Gemäss (Franke et al. 1989) werden vornehmlich
TiO2-V2O5 Mischoxide auf keramischen Wabenkörper oder Blechkörpern eingesetzt. Um die unerwünschten
Reaktionen zu Ammoniakhydrogensulfat zu verhindern, werden Spuren von Wolframoxid oder Niob
Ecoinvent-Bericht No.6, Teil VI                       - 128 -
                                                           9. Kraftwerke

verwendet, welche die Selektivität verbessern. Gemäss (Lange et al. 1991) besteht die Beschichtung dabei
mehr als zu 90% aus TiO2, 0.5% bis 5% aus V2O5 und 5% bis 10% aus WO3. Die Entsorgung der
Katalysatormasse, welche mit Schwermetallen angereichert ist, erfolgt durch Einbindung in Baumaterialien
oder durch Ablagerung als Sondermüll. Es wird davon ausgegangen, dass bei steigendem Anfall von
Altkatalysatoren eine Aufarbeitung möglich ist. Die Produktion der Katalysatorbeschichtung wird nicht
weiter bilanziert und die 25 kg/t NOx Katalysatorgewicht werden hier als Sondermüll betrachtet.
Durch den Druckverlust über den Katalysator entstehen zudem zusätzliche Eigenverbräuche (ca. 0.35% der
Nettoleistung (Wagner 1989)). Der zusätzliche Eigenverbrauch an Elektrizität wird beim Nettowirkungsgrad
direkt berücksichtigt.
Der Ammoniakschlupf beträgt bei einem Molverhältnis NH3/NOx von 0.8 unter 2 bis 10 ppm oder rund
1 kg/TJ (0.003 kg/kg NOx) (Hjalmarsson 1992), (Voos 1985).
Das Ammoniak werde 200 km per Bahn antransportiert, Bauaufwendungen für Lagertanks etc. wurden
bereits beim Bau des Kraftwerkes berücksichtigt.
Die vollständige Zusammenstellung der Eingabedaten für das SCR-Modul, das mit der Menge
zurückgehaltenem NOx an die Kraftwerke angeschlossen wird, findet man im Kap. 9.10.3.

Tab. 9.38: Bilanzierungsdaten für die Umwandlung von 1 kg NOx in N2


                                                                              SCR-Abscheidung
                             Input
                             Ammoniak                       kg/kg NOx                 0.3
                             TiO2                           kg/kg NOx                0.025
                             Transport Bahn                tkm/kg NOx                 0.06
                             Output
                             NH3 p (in Luft)                kg/kg NOx                0.003
                             Sonderabfall in Deponie*       kg/kg NOx                0.025

* Gesamte Masse des Katalysators als TiO2 bilanziert, da für die anderen Bestandteile in der Datenbank nicht verfügbar sind
** enthält TiO2, V2O5 und WO3

Selektive nicht-katalytische Reduktion (SNCR)
Bei Kohlekraftwerken wird die SNCR-Technologie bisher selten eingesetzt, da die baulichen Voraus-
setzungen oft nicht optimal und die Regelung schwieriger ist. (Voje et al. 1991) berichten von erfolgreichen
Nachrüstungen in einem besonders geeigneten Kraftwerk. Entgegen dem SCR-Verfahren werden hier keine
Katalysatoren eingesetzt. Als Reduktionsmittel wird ebenfalls Ammoniak eingesetzt. Damit die Reduktion
auch ohne Katalysator abläuft, muss bei wesentlich höheren Temperaturen (optimal zwischen 1010 und
1030°C) Ammoniak eingedüst werden. Das Molverhältnis NH3/NOx liegt wesentlich höher als beim
SCR-Verfahren (1.8 bis 3.5) und die Gefahr erhöhter Ammoniak-Emissionen stellt sich schon bei kleinen
Temperaturänderungen im Rauchgas.
(Voje et al. 1991) berichten von einem Kraftwerk mit NOx-Konzentrationen im Rohgas von bis zu
1500 mg/m3 und Konzentrationen nach dem SNCR von 150 bis 180 mg/m3, was einer Reduktion um rund
90% entspricht. Der NH3-Schlupf konnte auf 5 bis 7 mg/m3 begrenzt werden, was rund Faktor 2 über jenem
bei SCR-Anlagen liegt.
Da keine Katalysatorkosten anfallen, ist dieses Verfahren trotz dem höheren Ammoniakverbrauch gegenüber
dem SCR-Verfahren konkurrenzfähig, falls die baulichen Voraussetzungen vorhanden sind und die
Regelung beherrscht wird.
Mangels Relevanz innerhalb des UCTE-Raumes wird dieses Verfahren nicht bilanziert.




Ecoinvent-Bericht No.6, Teil VI                            - 129 -
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
