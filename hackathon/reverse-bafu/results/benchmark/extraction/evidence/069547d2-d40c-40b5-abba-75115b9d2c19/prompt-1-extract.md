You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Nuclear spent fuel, in conditioning, at plant` [CH], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~9 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: nuclear waste / unspecified
- includedProcesses: It includes transport of spent fuel elements and steel for canister, requirement of steel for canisters, steel welding, electricity consumption, and infrastructure requirement.
- technology: Estimation of current technologies
- generalComment: Complying with the current Swiss project for repository of high active waste, a distance of 70 km for transport of spent fuel elements from the intermediate repository (or power plant) to the conditioning plant is assumed. This plant is hypothesized at the same site of the repository, although the final place is not yet established. As first approximation the welding of lid and bottom of the canister is described with the ecoinvent module with double lenght. Electricity use is estimated hypothesizing 50 m total movement of the canister within the plant. The total spent fuel to condition is assumed to be 1800 t heavy metal, complying with the current Swiss scenario.;
UUID: 069547d2-d40c-40b5-abba-75115b9d2c19
- source cited in the metadata: Dones R. | 2009 | 2009 - Nuclear energy - Dones
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p295-297.txt` (SHA-256 d92c428bcda6785901167df3aec1d8effe0d70865f038ce1c266b4b88657116f), pages 295-297 of `2009 - Nuclear energy - Dones.pdf`.

```
Wiederaufarbeitung und Konditionierung


Tab. 10.30 Zusammenstellung der Eingabedaten für die Wiederaufbereitungsanlage.




                                                                                                                                            Deviation 95%
                                                                                                                              Uncertainty




                                                                                                                                                                                 Comment
                                                                                                                                              Standard
                                                                                     Location




                                                                                                                                                                                  General
                                                                                                        nuclear spent fuel,




                                                                                                                                Type
                                                                                                 Unit
                                      Name                                                              in reprocessing, at
                                                                                                               plant


                                                                          Location                            RER
                                                                              Unit                             kg
electricity, high voltage, at grid                                                    FR        kWh         2.55E+02             1           1.1            data from operator
heavy fuel oil, burned in industrial furnace 1MW, non-modulating                     RER         MJ         9.57E+02             1           1.1            data from operator
diesel, burned in diesel-electric generating set                                     GLO         MJ         4.81E+00             1           1.1            data from operator
water, decarbonised, at plant                                                        RER        kg          3.60E+02             1           1.1            data from operator
chemicals inorganic, at plant                                                        GLO        kg          4.60E+00             1           1.1            data from operator
chemicals organic, at plant                                                          GLO        kg          1.70E-02             1           1.1            data from operator
flat glass, uncoated, at plant                                                       RER        kg          3.60E-01             1            2             own calculation
formaldehyde, production mix, at plant                                               RER        kg          2.33E+00             1           1.1            data from operator
nitric acid, 50% in H2O, at plant                                                    RER         kg         4.36E+00             1           1.1            data from operator
sodium hydroxide, 50% in H2O, production mix, at plant                               RER         kg         5.42E+00             1           1.1            data from operator
welding, arc, steel                                                                  RER         m          2.30E-01             1            3             estimation
chromium steel 18/8, at plant                                                        RER         kg         6.60E+00             1           1.2            own calculation
cement, unspecified, at plant                                                        CH          kg         4.00E+00             1            2             estimation
transport, lorry 32t                                                                 RER        tkm         3.05E+00             1            2             standard
transport, freight, rail                                                             RER        tkm         3.73E+01             1           1.7            estimation
nuclear spent fuel reprocessing plant                                                RER        unit        2.78E-08             1           1.3            estimation
radioactive waste, in interim storage, for final repository LLW                      CH         m3          3.65E-03             1           1.5            estimation, based on old assessment
radioactive waste, in interim storage, for final repository SF, HLW, and ILW         CH         m3          4.47E-03             1           1.5            estimation, based on old assessment
low active radioactive waste                                                         CH         m3          7.00E-04             1            3             estimation
disposal, municipal solid waste, 22.9% water, to municipal incineration              CH         kg          7.65E+00             1           1.1            data from operator
disposal, inert waste, 5% water, to inert material landfill                          CH         kg          2.29E+00             1           1.1            data from operator
disposal, plastics, mixture, 15.3% water, to sanitary landfill                       CH         kg          2.59E-01             1           1.1            data from operator
disposal, hazardous waste, 25% water, to hazardous waste incineration                CH         kg          6.17E-01             1           1.1            data from operator
Heat, waste                                                                                     MJ          9.16E+02             1           1.1            same as electricity
Ammonia                                                                                          kg         5.86E-05             1            2             extrapolation
Cadmium                                                                                          kg         2.64E-05             1            2             extrapolation
Carbon monoxide, fossil                                                                          kg         5.89E-02             1            2             extrapolation
Dinitrogen monoxide                                                                              kg         3.70E-02             1            2             extrapolation
Hydrogen chloride                                                                                kg         2.81E-04             1            2             extrapolation
Hydrogen fluoride                                                                                kg         1.56E-05             1            2             extrapolation
Methane, fossil                                                                                  kg         6.20E-05             1            2             extrapolation
NMVOC, non-methane volatile organic compounds, unspecified origin                                kg         6.10E-04             1            2             extrapolation
Particulates, > 2.5 um, and < 10um                                                               kg         6.51E-04             1            2             extrapolation
Sulfur dioxide                                                                                   kg         2.63E-03             1            2             extrapolation
Carbon-14                                                                                       kBq         1.66E+04             1            2             extrapolation
Hydrogen-3, Tritium                                                                             kBq         4.49E+04             1           1.5            presumed uncertainty of measurements
Iodine-129                                                                                      kBq         1.73E+01             1            3             lower release in 2002 compared to 1996/1997
Aerosols, radioactive, unspecified                                                              kBq         1.53E-02             1            3             higher release in 2002 compared to 1996/1997
Noble gases, radioactive, unspecified                                                           kBq         1.66E+08             1           1.5            presumed uncertainty of measurements
Plutonium-238                                                                                   kBq         2.36E-06             1            3             old reference
Plutonium-alpha                                                                                 kBq         5.41E-06             1            3             old reference
Aluminum                                                                                         kg         1.79E-04             1           1.1            data from operator
Ammonium, ion                                                                                    kg         1.25E-04             1           1.1            data from operator
Barium                                                                                           kg         6.00E-05             1           1.1            data from operator
Cobalt                                                                                           kg         9.70E-05             1           1.1            data from operator
Nickel, ion                                                                                      kg         9.70E-05             1           1.1            data from operator
Nitrate                                                                                          kg         2.10E+00             1           1.1            data from operator
Nitrite                                                                                          kg         4.36E-02             1           1.1            data from operator
Oils, unspecified                                                                                kg         3.04E-03             1           1.1            data from operator
Phosphorus                                                                                       kg         8.36E-04             1           1.1            data from operator
Sulfide                                                                                          kg         3.63E-03             1           1.1            data from operator
Actinides, radioactive, unspecified                                                             kBq         2.81E+01             1           1.5            presumed uncertainty of measurements
Cesium-137                                                                                      kBq         3.22E+03             1            3             lower release in 2002 compared to 1996/1997
Hydrogen-3, Tritium                                                                             kBq         6.69E+06             1           1.5            presumed uncertainty of measurements
Radioactive species, Nuclides, unspecified                                                      kBq         1.68E+04             1           1.5            presumed uncertainty of measurements
Strontium-90                                                                                    kBq         3.58E+02             1            3             lower release in 2002 compared to 1996/1997
emissions to "air, low population density"
emissions to "water, ocean"




ecoinvent-Bericht No. 6 - Teil VII                                                   - 269 -
                                                                Wiederaufarbeitung und Konditionierung


                                                                                                                                                                                                                                                            76
     Tab. 10.31 Zusammenstellung der Eingabedaten für die Infrastruktur und den Betrieb der Konditionierungsanlage.




                                                                                                                               Standard Deviation 95%




                                                                                                                                                                                                                 Standard Deviation 95%
                                                                                                                                                         General Comment




                                                                                                                                                                                                                                          General Comment
                                                                                                            Uncertainty Type




                                                                                                                                                                                              Uncertainty Type
                                                                                            nuclear spent                                                                   nuclear spent




                                                                          Location
                                                                                                 fuel                                                                          fuel, in




                                                                                     Unit
                                   Name
                                                                                            conditioning                                                                   conditioning, at
                                                                                                plant                                                                           plant



                                                               Location                         CH                                                                               CH
                                                                   Unit                         unit                                                                             kg
     Transformation, from unknown                                             m2             2.25E+04              1   2 own estimation
     Transformation, to industrial area, built up                             m2             1.80E+04              1   2 own estimation
     Transformation, to industrial area, vegetation                           m2             4.50E+03              1   2 own estimation
     Transformation, from industrial area                                     m2             2.25E+04              1   2 own estimation
     Transformation, to unknown                                               m2             2.25E+04              1   2 own estimation
     Occupation, industrial area, built up                                    m2a            3.60E+05              1 2.5 own estimation
     Occupation, industrial area, vegetation                                  m2a            9.00E+04              1 2.5 own estimation
     building, multi-storey                                               RER m3             1.30E+05              1   2 own assumption
     Industrial machine, heavy, unspecified, at plant                     RER kg             5.00E+04              1   3 own assumption
     electricity, medium voltage, at grid                                 CH kWh                                                                                             2.40E-03                1    2 own assumption
     welding, arc, steel                                                  RER m                                                                                              8.00E-03                1    3 own assumption
     chromium steel 18/8, at plant                                        RER kg             5.00E+03              1                             3 own assumption            1.57E+01                1 1.15 variation in lenght of canister
     concrete, normal, at plant                                           CH m3              2.50E+02              1                             3 own assumption
     transport, lorry 28t                                                 CH tkm             2.68E+04              1                             3 own assumption            7.80E-01                1              2.1 standard for transports
     transport, lorry 32t                                                 RER tkm                                                                                            1.23E+00                1              2.1 standard for transports
     transport, freight, rail                                             RER tkm            3.30E+04              1                             3 own assumption            9.40E+00                1              2.1 standard for transports
     disposal, building, concrete, not reinforced, to final disposal      CH kg              6.00E+05              1                             3 own assumption
     nuclear spent fuel conditioning plant                                CH unit                                                                                             5.56E-07               1    2 uncertainty in the scenario
     radioactive waste, in final repository for nuclear waste SF, HLW,                                                                                                                                      container & content of U in heavy
     and ILW                                                           CH            m3                                                                                       2.30E-03               1 1.15 metal




76
     Die Tabelle zeigt die in Version v1.01 der ecoinvent Datenbank enthaltenen Eingabedaten. Die Bilanzierung von
     „radioactive waste, in final repository fornuclear waste, SF, HLW and ILW“ ist nicht korrekt, der richtige Wert beträgt
     2.4 m3/kg. Die korrekten Eingabedaten sind im Text beschrieben. Die Fehler werden in v.1.1 korrigiert.

     ecoinvent-Bericht No. 6 - Teil VII                                                              - 270 -
                                          Wiederaufarbeitung und Konditionierung


     10.11 Datenqualität
     Wiederaufarbeitung
     Für diese Studie wurden der gesamte Bedarf an Materialien und Energie sowie alle Emissionen dem
     Abfallstrom zugeordnet. Eine entsprechende Zuordnung unter Berücksichtigung aller vier
     Wiederaufarbeitungs-Produkte Uran, Plutonium, kommerzielle Isotope, und konditionierten Abfälle
     konnte im Rahmen dieser Studie vorgenommen nicht werden.
     Im Vergleich zur vorigen Ausgabe dieser Studie (1996) wurden Betriebsdaten aus dem Umwelt-
     bericht 1997 der Anlagen La Hague UP2 und UP3 verwendet. Diese Daten ersetzen oder ergänzen
     Werte, welche auf hypothetischen Anlagen, theoretischen Berechnungen auf Basis der Verfahrens-
     fliessbilder, oder Emissionsgrenzwerten beruhen und daher eine substanzielle Verbesserung der
     Beschreibung der realen Prozesse darstellen.
     Die Wertangaben für die radioaktiven Luft- und Wasseremissionen sind von der UP2+UP3 Betrieber
     Cogema nur als Emissionsklassen wiedergegeben. Es konnten nur eine Reihe von Extrapolationen auf
     spezifischere Isotope (C-14 sowie Pu-238 und Pu-239) vorgenommen werden, und zwar auf Basis
     qualifizierter Annahmen, welche auf verfügbaren Emissionsdaten aus älterer Literatur beruhen. Es
     muss daran erinnert werden, dass sich das Spektrum der einzelnen emittierten radioaktiven Isotope,
     welche in Klassen zusammengefasst sind, in Abhängigkeit von der Anlage ändern könnte (La Hague
     vs. THORP), aber auch mit dem Prozessschritt innerhalb der Nuklearkette. Beispielsweise wurde die
     Emissionskategorie „Radioactive species, Nuclides, unspecified“ für die Kernkraftwerksemissionen
     und jene der Wiederaufbereitungsanlagen verwendet, da keine detaillierteren Daten zum Spektrum zur
     Verfügung standen. Es könnten jedoch grosse Unterschiede hinsichtlich der Zusammensetzung der
     emittierten Spektren bestehen. Bei einer Anwendung von Bewertungsmethoden (LCIA-Methoden) auf
     das Inventar steigen die Unsicherheiten weiter an.77 Die Unsicherheitsfaktoren, welche in den Tabellen
     enthalten sind, widerspiegeln diese Aspekte nicht, sondern lediglich die möglichen Abweichungen der
     emittierten Mengen. Ideal wäre eine Verfügbarkeit von Emissionsdaten für jedes einzelne Isotop,
     wodurch die Definition von Emissionsklassen vermieden werden könnte. Dies ist jedoch angesichts
     der zur Verfügung stehenden Informationen nicht realistisch. In einer ausgeweiteten Datenbank
     könnten in Abhängigkeit von den einzelnen Schritten der nuklearen Energiekette neue Definitionen
     von radioaktiven Emissionsklassen zum Einsatz kommen.
     Teilweise mussten Datensätze, basierend auf verschiedenen Referenzanlagen, kombiniert werden, was
     sich auf die Konsistenz auswirkte. Es bestehen jedoch trotz unterschiedlicher Herkunftsländer der
     Projekte (DOE: USA, abgestützt auf Erfahrungen militärischer Anlagen) und zeitlich verschiedener
     Projektbearbeitungsperioden, bezüglich der einzelnen Daten, zumindest in der Grössenordnung gute
     Übereinstimmungen, was auf die Anwendung gleicher oder ähnlicher chemischer Hauptprozesse zu-
     rückzuführen ist. Grössere Abweichungen in den radioaktiven Emissionen begründen sich in der
     Anwendung unterschiedlicher Behandlungsprozesse der gasförmigen und flüssigen Abfallstoffe, aber
     auch in einem Vergleich von tatsächlichen mit berechneten Emissionen.
     Bezüglich Baumaterialien und Flächenbeanspruchungen lagen teilweise unterschiedliche Werte vor.
     Einige davon wurden für die Moduleinführung durch Extrapolationen angepasst.
     Die vorliegende Datenzusammenstellung ist eine vereinfachte, aber recht komplett Beschreibung der
     Massenströme der Wiederaufarbeitungsaktivitäten. Als solche können die gezeigten Daten unter
     Berücksichtigung der Komplexität der Prozessabläufe, der relativ wenigen zur Verfügung stehenden
     Daten sowie der Informationszurückhaltung seitens der Betreiber der Wiederaufarbeitungsanlagen als
     genügend gut angesehen werden, wenn man das Ziel dieser Studie, eine Analyse der vollständigen
     nuklearen Energiekette, in Betracht zieht. Zukünftige Aktualisierungen sollten jedoch tatsächliche


77
     Es ist anzunehmen, dass die Entwickler der LCIA-Methoden eine Zusammensetzung der Emissionen in jeder Klasse
     definieren.

     ecoinvent-Bericht No. 6 - Teil VII                   - 271 -
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
