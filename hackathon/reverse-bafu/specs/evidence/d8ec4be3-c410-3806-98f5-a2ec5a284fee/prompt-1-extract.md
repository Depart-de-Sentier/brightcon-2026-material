You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Burnt shale, at plant` [DE], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~1660 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: construction materials / concrete
- includedProcesses: <null>
- technology: Unspecified
- generalComment: na;
UUID: d8ec4be3-c410-3806-98f5-a2ec5a284fee
- source cited in the metadata: Tschuemperlin L. | 2020 | 2020 - LCA selected types of concrete - Tschuemperlin
- time period: 2015-01-2015-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Crude Oil: 3.658 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Shale: 0.9626 kilogram (soil)
- Crude Oil: 0.2639 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Natural Gas: 0.02925 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Water to turbine: 0.01026 cubic meter (Resources Resources from water Renewable material resources from water)
- Uranium: 0.007218 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Hard Coal: 0.004381 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Brown Coal: 0.002425 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Energy, Potential (in Hydropower Reservoir), Converted: 0.001665 megajoule (natural resource)
- Energy, gross calorific value, in biomass: 0.0009582 megajoule (resources biotic)
- Gravel: 0.0008402 kilogram (soil)
- Waste mass, total, placed in landfill: 0.0004453 kilogram (resources in ground)

## Report excerpt

Source file: `report-p19-21.txt` (SHA-256 8f862e61970465b04a6f46c27a3881e545da1b2fead22851111c8521cc8b9a94), pages 19-21 of `2020 - LCA selected types of concrete - Tschuemperlin.pdf`.

```
Sachbilanzdaten und Modellierungsannahmen                                                                                                                                                                            15




Tab. 3.8: Sachbilanz von 1 kg Hüttensand, ab Werk (Fortsetzung)




                                                                                                                                       StandardDeviation95
                                                                                                                     UncertaintyType
                                                                                    ground           ground




                                                             Location
                                                                               granulated blast granulated blast




                                                                        Unit




                                                                                                                                               %
                                      Name                                                                                                                   GeneralComment
                                                                               furnace slag, no furnace slag, with
                                                                               burdens, at plant burdens, at plant


                                     Location                                       RER               RER
                             InfrastructureProcess                                   0                 0
                                       Unit                                          kg                kg
                                                                                                                               (1,1,1,1,1,3,BU:1.5); entspricht Ecoinvent 3.2 Dataset
emission water,
                Water                                          -        kg         4.29E-1           4.29E-1            1 1.50 documentation ground granulated blast furnace slag
unspecified
                                                                                                                               production, RoW
                                                                                                                               (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
               Heat, waste                                     -        MJ         6.93E-1           6.93E-1            1 1.07 documentation ground granulated blast furnace slag
                                                                                                                               production, RoW
emission                                                                                                                       (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
resource, in   Water, unspecified, Europe                      -        m3         9.19E-4           9.19E-4            1 1.07 documentation ground granulated blast furnace slag
water                                                                                                                          production, RoW
                                                                                                                               (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
               disposal, inert waste, 5% water, to inert
technosphere                                                 CH         kg         1.12E-3           1.12E-3            1 1.07 documentation ground granulated blast furnace slag
               material landfill
                                                                                                                               production, RoW
                                                                                                                               (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
               treatment, concrete production effluent, to
                                                             CH         m3         3.52E-4           3.52E-4            1 1.07 documentation ground granulated blast furnace slag
               wastewater treatment, class 3
                                                                                                                               production, RoW
                                                                                                                                                             (2,1,1,1,1,5,BU:2); hinzugefügt, da in ecoinvent v3.2 nicht
               transport, lorry 16-32t, EURO4                RER        tkm        3.59E-5           5.01E-2            1 2.05
                                                                                                                                                             berücksichtigt;

                                                                                                                                                             (2,1,1,1,1,5,BU:2); hinzugefügt, da in ecoinvent v3.2 nicht
               transport, freight, rail                      RER        tkm        7.43E-5           7.43E-5            1 2.05
                                                                                                                                                             berücksichtigt;




3.6            Herstellung von gebranntem Ölschiefer
Gebrannter Ölschiefer wird vor allem in CEM II/B Zementen und im Zement CEM
ZN/D eingesetzt. Bei der Herstellung von gebranntem Ölschiefer wird auch Strom pro-
duziert. Die Herstellung von einer Tonne gebranntem Ölschiefer führt zur Produktion
von 183.8 kWh Strom, welcher im benachbarten Zementwerk eingesetzt beziehungs-
weis an Dritte verkauft wird. Die Umweltkennwerte des gebrannten Ölschiefers basie-
ren auf einer Sachbilanz von Werner (2013) mit einer ökonomischen Allokation zwi-
schen den Co-Produkten Strom (28.7%) und gebranntem Ölschiefer (71.3%) gemäss
Werner (2018). Die Sachbilanz des gebrannten Ölschiefers gemäss der Allokation aus
Werner (2018) ist in Tab. 3.9 dargestellt. Für die Transportdistanzen wurden die Stan-
darddistanzen gemäss Frischknecht et al. (2007a) verwendet (siehe Tab. 3.10).




Ökobilanz ausgewählter Betonsorten                                                                                                                                                                       treeze Ltd.
Sachbilanzdaten und Modellierungsannahmen                                                        16




Tab. 3.9: Sachbilanz von 1 kg gebranntem Ölschiefer (GÖS), ab Werk (Werner 2013), angepasst gemäss
          Allokation aus Werner (2018).

                                                 Zuordnung zu GÖS
                                                100 %       71.30 %
Input                                Einheit    pro t        pro t
Energie und Betriebsmittel
Sprengstoff                          kg        9.45E-02     6.74E-02
Diesel Abbaugerät                    l         5.40E-01     3.85E-01
Stromverbrauch Brecher               kWh       1.62E+00    1.16E+00
Stromverbrauch Förderbänder          kWh       7.02E-01     5.01E-01
Stromverbrauch Zerkleinern           kWh       4.86E+00    3.47E+00
Heizöl EL, Mühle                     l         2.00E-01     1.43E-01
Stromverbrauch GÖS-Produktion        kWh       4.30E+01    3.07E+01
Stromverbrauch Stromerzeugung        kWh       1.60E+01    1.14E+01
Wasserverbrauch                      m3        7.00E-01     4.99E-01
Laugen/Säuren
Salzsäure                            kg        1.00E-01     7.13E-02
Natronlauge                          kg        1.00E-01     7.13E-02
Chlorbleichlauge                     kg        1.00E-01     7.13E-02
Chemikalien, org.                    kg        8.00E-02     5.70E-02
Stromverbrauch Mahlen                kWh       3.00E+01    2.14E+01
Emissionen
Staub                                kg        1.33E-03     9.48E-04
Nox                                  kg        7.28E-01     5.19E-01
SO2                                  kg        6.37E-01     4.54E-01
CO2                                  kg        5.92E+02    4.22E+02
davon fossil                         kg        3.59E+02    2.56E+02
davon geogen                         kg        2.33E+02    1.66E+02
CO                                   kg        5.73E-01     4.09E-01
Outputs
Abwasser, unbelastet                 m3        1.50E-01     1.07E-01




Ökobilanz ausgewählter Betonsorten                                                       treeze Ltd.
Sachbilanzdaten und Modellierungsannahmen                                                            17




Tab. 3.10: Transportdistanzen für die Produktion von gebranntem Ölschiefer

Material                                     Einheit        Distanz Bahn     Distanz LKW
Heizöl                                       km                 600               0
Salzsäure                                    km                 200              100
Natronlauge                                  km                 600              100
Chlorbleichlauge                             km                 600              100



Aufgrund der eingesehenen Unterlagen sind die Autoren der Ansicht, dass dem Strom
keine Umweltauswirkungen zugeteilt werden dürften. Diese Ansicht wird vom Ersteller
der Ökobilanz von gebranntem Ölschiefer jedoch nicht geteilt. Im Anhang A sind die
Umweltkennwerte von gebranntem Ölschiefer einmal mit ökonomischer Allokation und
einmal mit 100 % Zuordnung auf gebranntem Ölschiefer aufgeführt. Im Betonrechner
werden die Umweltkennwerte des Ölschiefers gemäss Variante „ökonomische Allokati-
on“ verwendet.


3.7      Herstellung von Hochofenzement
Hüttensand wird in grösseren Mengen vor allem den Hochofenzementen (CEM III) bei-
gefügt. Bei den Hochofenzementen wird zwischen drei verschiedenen Hüttensandgehal-
ten unterschieden5. CEM III/A enthält 36 M.-% bis 65 M.-% Hüttensand und CEM
III/B enthält 66 M.-% bis 80 M.-% Hüttensand5. Des Weiteren gibt es noch CEM III C
mit einem noch höheren Hüttensandgehalt, welcher aber im Rahmen dieser Arbeit nicht
betrachtet wird. Bei einem Hüttensandanteil über 20 M.-% im Zement reicht die Ab-
wärme des Mahlprozesses alleine nicht aus, den Hüttensand mit einer Restfeuchte von
10 % vollständig zu trocknen (Boesch & Hellweg 2010). Der Hüttensand für die
CEM III Herstellung muss deshalb vor dem Mahlprozess vollständig getrocknet wer-
den. Die Sachbilanz der Herstellung von CEM III/A und CEM III/B Zementen ist eben-
falls bereits im ecoinvent Datenbestand v3.2 enthalten und bildet eine durchschnittliche
Herstellung von Hochofenzement in der Schweiz ab (Boesch & Hellweg 2010). Die
Daten stammen aus dem Jahr 2009 und wurden für das Jahr 2015 extrapoliert.
Im Betonrechner sind die Hochofenzemente mit der Variante „Hüttensand, ohne Auf-
wendungen“ implementiert.
Tab. 3.11 gibt die Sachbilanz in der für die KBOB-Empfehlung relevanten Umgebung
wider.




5
    http://www.beton-informationen.de/huettensandhaltige_zemente/, abgerufen am 14.01.2016




Ökobilanz ausgewählter Betonsorten                                                           treeze Ltd.
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
