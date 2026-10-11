You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Ground granulated blast furnace slag, no burdens, at plant` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~27 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: construction materials / binder
- includedProcesses: This inventory for production of GGBFS encompasses the process steps (i) quenching/granulation, (ii) dewatering and/or drying, (iii) crushing, (iv) grinding, and (v) storage in pile and silo. The dataset includes the inert waste generated as a by-product, most important emissions, infrastructure and transport processes
- technology: Industry data.
- generalComment: This dataset represents the treatment of molten blast furnace slag, producing an output of ground granulated blast furnace slag (GGBFS, also referred to as slag cement).\nTechnology: Industry data.\nTime period: Time of publications.\nVersion: 1\nEnergy values: Undefined\nLocal category: Mineralische Baustoffe\nLocal subcategory: Bindemittel\nUVEK 2022 source file:551-Zement-Klinker_v0.13_UVEK2021._GroundgrBFS.xml\n\n
UUID: 7622063d-6d0d-316d-8455-556556b1731a
- source cited in the metadata: Tschuemperlin L. | 2020 | 2020 - LCA selected types of concrete - Tschuemperlin
- time period: 2015-01-2015-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Water: 0.0009193 cubic meter (Resources Resources from water Renewable material resources from water)

## Report excerpt

Source file: `report-p18-19.txt` (SHA-256 f9172ab20033c2b427dce55b5cb19409e7e638db16dc8fa03ec81f3b68bd52a7), pages 18-19 of `2020 - LCA selected types of concrete - Tschuemperlin.pdf`.

```
Sachbilanzdaten und Modellierungsannahmen                                                                                                                                                  14




sion 3 dieses Berichts dokumentierten Bilanz wurden die CO2-Emissionen um einen
Faktor 10 nach unten korrigiert (Fehlerkorrektur).
Tab. 3.8: Sachbilanz von 1 kg Hüttensand, ab Werk




                                                                                                                                          StandardDeviation95
                                                                                                                        UncertaintyType
                                                                                       ground           ground



                                                                Location
                                                                                  granulated blast granulated blast




                                                                           Unit




                                                                                                                                                  %
                                       Name                                                                                                                     GeneralComment
                                                                                  furnace slag, no furnace slag, with
                                                                                  burdens, at plant burdens, at plant


                                    Location                                           RER               RER
                            InfrastructureProcess                                       0                 0
                                      Unit                                              kg                kg
                ground granulated blast furnace slag, no
product                                                        RER         kg         1.00E+0
                burdens, at plant
                ground granulated blast furnace slag, with
product                                                        RER         kg                           1.00E+0
                burdens, at plant
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
technosphere    blast furnace slag, at plant                   RER         kg            0            1.00143E+0          1 1.07 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
technosphere    diesel, burned in building machine             GLO         MJ         4.52E-3           4.52E-3           1 1.07 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
                electricity, medium voltage, production
                                                               ENTSO kWh              9.12E-2           9.12E-2           1 1.07 documentation ground granulated blast furnace slag
                ENTSO, at grid
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
                light fuel oil, at regional storage            RER         kg         1.00E-3           1.00E-3           1 1.07 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
                lubricating oil, at plant                      RER         kg         4.01E-6           4.01E-6           1 1.07 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
                natural gas, high pressure, at consumer        RER         MJ         3.23E-1           3.23E-1           1 1.07 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
                air filter, central unit, 600 m3/h, at plant   RER         unit       8.03E-5           8.03E-5           1 1.07 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:3); entspricht Ecoinvent 3.2 Dataset
                cement plant                                    CH         unit      5.36E-11          5.36E-11           1 3.00 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
                solvents, organic, unspecified, at plant       GLO         kg         8.26E-7           8.26E-7           1 1.07 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
                ethylene glycol, at plant                      RER         kg         1.26E-6           1.26E-6           1 1.07 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
                steel, low-alloyed, at plant                   RER         kg         3.53E-4           3.53E-4           1 1.07 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
emission air,
                Carbon dioxide, fossil                            -        kg         1.97E-2           1.97E-2           1 1.07 documentation ground granulated blast furnace slag
unspecified
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:5); entspricht Ecoinvent 3.2 Dataset
                Carbon monoxide, fossil                           -        kg         5.45E-5           5.45E-5           1 5.00 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.5); entspricht Ecoinvent 3.2 Dataset
                Hydrogen sulfide                                  -        kg         2.70E-4           2.70E-4           1 1.50 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.5); entspricht Ecoinvent 3.2 Dataset
                Methane, fossil                                   -        kg         1.37E-6           1.37E-6           1 1.50 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.5); entspricht Ecoinvent 3.2 Dataset
                Nitrogen oxides                                   -        kg         2.42E-6           2.42E-6           1 1.50 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.5); entspricht Ecoinvent 3.2 Dataset
                NMVOC, non-methane volatile organic
                                                                  -        kg         7.95E-7           7.95E-7           1 1.50 documentation ground granulated blast furnace slag
                compounds, unspecified origin
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:2); entspricht Ecoinvent 3.2 Dataset
                Particulates, > 2.5 um, and < 10um                -        kg         1.53E-6           1.53E-6           1 2.00 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.05); entspricht Ecoinvent 3.2 Dataset
                Sulfur dioxide                                    -        kg         2.31E-4           2.31E-4           1 1.07 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW
                                                                                                                                 (1,1,1,1,1,3,BU:1.5); entspricht Ecoinvent 3.2 Dataset
                Water                                             -        kg         1.38E-1           1.38E-1           1 1.50 documentation ground granulated blast furnace slag
                                                                                                                                 production, RoW




Ökobilanz ausgewählter Betonsorten                                                                                                                                               treeze Ltd.
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
