You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `SOx retained, in hard coal flue gas desulphurisation` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~47 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: power plants / unspecified
- includedProcesses: The module describes the operation of a wet scrubber. It includes material input, transport of this material, waste water and solid waste.
- technology: Average installed technology in the 1990s.
- generalComment: The efficiency of the desulphurisation is 90 %. All environmental burdens associated with the operation of the scrubber are allocated to the SO2 retained and hence to the power plant. Therefore the produced gypsum is assumed to be burden free, and not explicitly included in the module. The considered input of limestone and quicklime reflects the average use of these materials in European scrubbers.;
UUID: d9b34c0e-fef5-3aba-adca-36022bd418c2
- source cited in the metadata: Dones R. | 2007 | 2007 - Coal - Dones
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p136-138.txt` (SHA-256 f7043221e7dab1186a51b0a887c8f8328cddc69213e5d09a5ddcf5e548daa6ca), pages 136-138 of `2007 - Coal - Dones.pdf`.

```
9. Kraftwerke

Tab. 9.31: Grobbilanz für die grössten Stoffflüsse in einer REA, bei 1% Schwefelgehalt und 85% Entschwefelung für
             Steinkohle-Kraftwerk (nach (Hövelmann 1987), (Taubert 1990) und eigenen Berechnungen).


                                                          ins Kraftwerk        in REA             aus REA
                                                          kg/TJ                kg/TJ              kg/TJ
                                   Vollwertkohle          35'700
                                   Schwefel               357
                                   Schwefeldioxid                              678                102
                                   Kalkstein                                   1085
                                   Gips                                                           1475
                                   Abwasser                                                       5000
                                   Schlamm                                                        36



Tab. 9.32: Verschiedene REA-Bilanzen aus diversen Quellen

Quelle         c)   Hövel- Folg- Hjalmars- Hjalmars- Hjalmars             Hjalmars-      Hjalmars- Hjalmars- Borsch          Taubert        STEAG
                    mann mann son 1992 son 1992        -son               son 1992       son 1992 son 1992    et al.          1990           1988
                    1987 1984                          1992                                                   1992
Kraftwerk                        Voitsberg Avedore Zolling                  Inkoo        Meri-Pori Västhamn                 Bergkamen
                                                                                                    verket
kg/kg SO2 Stk        Stk     Stk       Brk         Stk         Stk           Stk           Stk           Stk        Stk        Stk           Stk
Input                                                                     Eindüsung
Kalk                   0.9    1.1                                                                          0.83                        1        1 a)
Kalkstein  1.9                               2.9         2.3        1.6            4.5           1.4                 1.56                     1.6 a)
Wasser                         37             21          26         18             29           17'           27      19                    4 /9 a)
H2SO4                                                                                                                                0.08      0.09
NaOH                                                                                                                                 0.02      0.03
Output
Gips       2.6                3.3            4.6         3.3        2.7                          3.1                  2.9             2.2       2.7
Abwasser   8.7                                 0         3.4        7.8                          2.6            ?     1.9
Schlamm   0.06                                                                                                                   0.1 b)
     a)     entweder Kalk oder mit Kalkstein (Kalk/Kalkstein)
     b)     30% Trockensubstanz
     c)     aus (Hövelmann 1987), (Taubert 1987), und Tab.9.32

Da sich mittlerweile die Zugabe von Kalkstein in Europa klar durchgesetzt hat, wird der gegenwärtige Anteil
von Entschwefelungsanlagen mit Kalkstein auf 80% abgeschätzt. Damit wird eine mittlere Stoffbilanz aus
Tab. 9.32 abgeschätzt (siehe Tab. 9.33). Für die Braunkohlekraftwerke in den alten Bundesländern
Deutschlands muss aufgrund der Relevanz berücksichtigt werden, dass nur Kalkstein verwendet wird,
welcher offenbar stöchiometrisch höher dosiert wird und dass das REA-Abwasser zur Aschebefeuchtung
benutzt wird und zusammen mit Feuerraumasche und Flugasche deponiert wird (Gebhard et al. 1989). Die
Eluate der Deponie werden dann in Kap. 9.8 bei der Flugaschedeponie verbucht.
Die abwasserfreien Verfahren, welche mit Abwassereindampfung arbeiten, werden nicht berücksichtigt, da
deren Anteil noch unbedeutend ist (Grünewald et al. 1991).
Die Anbindung an die Kraftwerksbilanzierung erfolgt über die abgeschiedene Menge SO2. In Tab. 9.33
wurden deshalb die spezifischen Stoffflüsse pro kg abgeschiedenem SO2 zusammengestellt.




Ecoinvent-Bericht No.6, Teil VI                                - 124 -
                                                           9. Kraftwerke

Tab. 9.33: REA-Massenbilanz pro kg reduziertes SO2, REA-Nass nach Tab.9.33, REA-Nass Brk-D (Nass-Entschwefelung der
            westdeutschen Braunkohlekraftwerke) nach (Gebhard et al. 1989), (Uerpmann 1990)



                                                                    REA-Nass          REA-Nass Brk-D
                        Input
                        Kalk                        kg/kg SO2                   0.2
                        Kalkstein                   kg/kg SO2                   1.3                      2
                        Wasser entkarbonisiert      kg/kg SO2                    20                     10
                        Schwefelsäure H2SO4         kg/kg SO2                  0.08
                        Natronlauge NaOH            kg/kg SO2                  0.02
                        Transport Schiene           tkm/kg SO2                 0.17                    0.2
                        Transport LKW 28t           tkm/kg SO2                0.003
                        Output
                        Gips **                     kg/kg SO2                   2.8                    4.1
                        CO2                         kg/kg SO2                  0.55                    0.7
                        Abwasser                    kg/kg SO2                  5***                   2.4*
                        Schlamm ****                kg/kg SO2                  0.06

                        * Wird zur Aschebefeuchtung benützt und deponiert
                        ** wird in Ecoinvent nicht aufgenommen
                        *** wird mit Tab.9.35/36 verknüpft
                        **** Zusammensetzung siehe Tab. 9.35, wird in Ecoinvent als 'Abfälle in Reststoffdeponie' verbucht

Die Reaktionsgleichung des Kalsteinverfahrens sieht wie folgt aus:

        CaCO3 + 2H2O + SO2 + _O2 -> CaSO4•2H2O + CO2
Daraus kann direkt abgeleitet werden, dass stöchiometrisch 1.56 kg Kalkstein gebraucht und 0.69 kg CO2 pro
kg SO2 produziert werden. Bei Kalk-Verfahren sind stöchiometrisch nur knapp 0.9 kg Kalk pro kg SO2 nötig
und es fällt kein zusätzliches CO2 an, da dieses bereits beim Kalkbrennen entwichen ist.
Das REA-Wasser muss keine erhöhten Ansprüche erfüllen und entspricht deshalb der Kühlwasserqualität.
Der Gips gilt als Nebenprodukt des Kraftwerkbetriebes und steht deshalb frei Kraftwerk zur Verfügung (kein
Abtransport). Der Schlamm muss behandelt resp. deponiert werden. Es wird hier vom Deponiefall mit 50 km
LKW-Transport ausgegangen. Schwefelsäure und Natronlauge werden im Durchschnitt 200 km mit der
Bahn transportiert. Kalk und Kalkstein werden im Durchschnitt 100 km per Bahn transportiert. Der Grund
für den hohen Bahnanteil liegt in den grossen Tonnagen an Betriebsstoffen, die aus dem REA-Betrieb
resultieren.
Die Abwasseremissionen der REA werden in Tab. 9.34 aus verschiedenen Quellen zusammengestellt.
Obwohl die meisten Informationen und auch die Einleitgrenzwerte aus Deutschland stammen, dürfen diese
Angaben für Europa verwendet werden, da die anderen grossen REA-Betreiber (Österreich, Niederlande)
ähnliche Umweltstandards einhalten müssen.
Die letzte Kolonne wird weiterverwendet für das Modul “SOx zurückgehalten in REA”, das für die
allgemeinen Steinkohlekraftwerke verwendet wird. Für die Braunkohlekraftwerke werden keine
Abwasseremissionen berücksichtigt (wird zusammen mit der Aschedeponie in Kap. 9.8.1, Tab. 9.70
berücksichtigt).




Ecoinvent-Bericht No.6, Teil VI                           - 125 -
                                                           9. Kraftwerke

Tab. 9.34: Konzentrationen von Ionen des REA-Abwassers vor und nach Reinigung mit ARA und für dieses Projekt gewählte
             Werte


     Ionen           REA-Abwasser            REA-         Grenzwerte       Grenzwerte      diese Studie     mit 5 l
     von                aus Stk-           Abwasser       nach ARA in      nach ARA in          für       Abwasser/
                       Kraftwerk            aus Brk-      Deutschland         Berlin        Steinkohle     kg SO2 **
                                           Kraftwerk
     pH                   1-6.5                              8.5/10            6.5-8            9              9
                           mg/l               mg/l            mg/l             mg/l            mg/l        g/kg SO2
     Ca*               1'500-18'000                                             0             10000           50
     Mg                 300-3500                                                0             2000            10
     Na                 400-1000                                                               500            2.5
     Cl                5000-40000            10000                              60            5000            250
     SO3                200-6000                -              20                              20             0.1
     SO4                1300-5000             4000            2000             150            2000            10
     NH4                                      180
     NO3                500-1500              3000                              5             1000             5
     NH3                                                                        0.5            0.5           0.003
     F                   30-1250               30              30                              30             0.15
     SiO2*               150-300                                                               300            1.5
     COD                  40-500              130          801)/1502)           20             150            0.75
     ungelöste          15-10000              3000          0.31)/0.5)                         0.5           0.003
     Feststoffe
     BSB5                                      13                               5               5            0.025
     Hg                     <2                0.13            0.05            0.001            0.05         0.0003
     Cd                     <2                0.15            0.05             0.01            0.05         0.0003
     Pb                    <30                 2.5             0.1             0.05            0.1          0.0005
     Zn                    1-39                 8               1               0.5             1            0.005
     Cr                    <20                 2.7             0.5             0.05            0.5           0.003
     Cu                   0.2-26               2.1             0.5             0.05            0.5           0.003
     Ni                   0.2-5                 2              0.5             0.05            0.5           0.003
     As                     10               0.001                             0.03            0.1           0.005
     Phosphat                                                                   0.3            0.3           0.002
     K                     130                                                  10             10             0.05
     Al                   18-160                                                0.2            0.5           0.003
     B                      72                                                                 66             0.33
     Fe                   37-140                                                               0.5           0.003
     Mn                   40-450                                                                1            0.005
     Mo                     16                                                                 0.5           0.003
     V                     4.2                                                 0.05            0.5           0.003
     Sb                     2                                                                  0.5           0.003
     Se                     7                                                                  0.1          0.0005
     Sn                    1.3                                                                 0.5           0.003
                       (Hövelmann          (Bambauer      (Hövelmann       (Grünewald et   diese Studie   diese Studie
                       1987, Syring        et al. 1988)      1987)            al.1991)
                     1990, Grünewald
                     et al. 1991, Kyte
                            1991)

    1) Branntkalk
    2) Kalkstein
    * wird in Ecoinvent nicht bilanziert
    ** siehe Tab.9.34




Ecoinvent-Bericht No.6, Teil VI                           - 126 -
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
