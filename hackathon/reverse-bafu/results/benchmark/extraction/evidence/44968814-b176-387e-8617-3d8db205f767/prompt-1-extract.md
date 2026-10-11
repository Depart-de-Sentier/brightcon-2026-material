You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `3kWp slanted-roof installation, single-Si, panel, mounted, on roof` [RER], reference unit 1 p, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~9 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: photovoltaic / production of components
- includedProcesses: All components for the installation of a 3kWp photovoltaic plant, energy use for the mounting, transport of materials and persons to the construction place. Disposal of components after end of life.
- technology: Current technology for mounting of panels or laminates, electric installations and other components.
- generalComment: Photovoltaic installation with a capacity of 3kWp and a life time of 30 years installed in Europe. The efficiency of single-Si PV modules is 17.9% (Fraunhofer ISE Photovoltaics Report 2019). The share of rejected or replaced PV modules is estimated at 3%. The inverter is assumed to be replaced once during the service life of the PV system.;
Synonyms: monocrystalline, single crystalline, silicon; 
UUID: 44968814-b176-387e-8617-3d8db205f767
- source cited in the metadata: Frischknecht R. | 2020 | 2015 - LCI and LCA photovoltaic systems - Frischknecht
- time period: 2000-01-2018-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 p):
- none

## Report excerpt

Source file: `report-p61-62.txt` (SHA-256 ef327d9a8e18e6f3cea46a4b20c34d11718127f12d96390686892ab0830bae20), pages 61-62 of `2015 - LCI and LCA photovoltaic systems - Frischknecht.pdf`.

```
IEA-PVPS-TASK 12                                                 Life Cycle Inventories and Life Cycle Assessments of Photovoltaic Systems



5.5                 Mounting Structures of PV Modules
Tab. 5.3.1 shows the unit process data of PV mounting systems in Europe. The data correspond to the life cycle inventory data of mounting
systems published by Jungbluth et al. (2012) [38]. Data includes materials, packaging, and transport of mounting structures and disposal of
packaging materials.
Tab. 5.5.1 Unit process data of different PV mounting systems




                                                                                                                                                                                                                                                                 StandardDev
                                                                                                                                                                                                                                                                 UncertaintyT
                                                                                Infrastructure
                                                                                                           facade                  facade                                                                                                  slanted-roof




                                                                                                                                                                                                                                                                  iation95%
                                                                     Location
                                                                                                                                                       flat roof      s lanted-roof           slanted-roof        open ground
                                                                                                        cons truction,         cons truction,                                                                                              construction,




                                                                                                 Unit
                                       Name                                                                                                        cons truction, on  construction,          cons truction,      construction, on                                               GeneralComment
                                                                                                         mounted, at           integrated, at                                                                                            mounted, on roof,
                                                                                                                                                          roof       mounted, on roof     integrated, on roof        ground
                                                                                                          building                building                                                                                               Stade de Suis s e

                                      Location                                                              RER                    RER                  RER               RER                   RER                   RER                      CH
                           Infras tructureProcess                                                            1                      1                     1                1                      1                     1                       1
                                      Unit                                                                   m2                     m2                   m2                m2                    m2                    m2                      m2
               aluminium, production mix, wrought alloy, at
 technos phere                                                       RER         0               kg       2.64E+0                3.27E+0              2.52E+0           2.84E+0                2.25E+0              3.98E+0                  2.30E+0             1 2.05 (1,2,1,1,1,na); Literature and own es timations
               plant
               corrugated board, mixed fibre, single wall, at
                                                                     RER         0               kg       4.03E-2                    -                1.83E-2           1.33E-1                1.14E-1               8.64E-2                 1.33E-1             1 2.18 (3,4,3,1,3,5); Schwarz et al. 1992
               plant
                                                                                                                                                                                                                                                                        (1,2,1,1,1,na); Literature and own es timations , recycled
                polyethylene, HDPE, granulate, at plant              RER         0               kg       7.32E-4                    -                1.92E+0           1.40E-3                2.82E-2               9.09E-4                 1.40E-3             1 2.05
                                                                                                                                                                                                                                                                        PE
                polys tyrene, high impact, HIPS, at plant            RER         0               kg       3.66E-3                    -                8.30E-3           7.02E-3                6.02E-3               4.55E-3                 7.02E-3             1 2.18 (3,4,3,1,3,5); Schwarz et al. 1992

                polyurethane, flexible foam, at plant                RER         0               kg           -                      -                    -                 -                  1.84E-2                  -                        -               1 2.05 (1,2,1,1,1,na); Literature and own es timations

                synthetic rubber, at plant                           RER         0               kg           -                      -                    -                 -                  1.24E+0                  -                        -               1 2.05 (1,2,1,1,1,na); Literature and own es timations

                steel, low-alloyed, at plant                         RER         0               kg       1.80E+0                    -                2.67E-1           1.50E+0                2.00E-1                  -                        -               1 2.05 (1,2,1,1,1,na); Literature and own es timations

                chromium steel 18/8, at plant                        RER         0               kg           -                      -                    -                 -                      -                 2.47E-1                 6.50E-2             1 2.10 (2,3,1,1,1,5); Literature and own estimations

                reinforcing s teel, at plant                         RER         0               kg           -                      -                    -                 -                      -                7.21E+0                      -               1 2.10 (2,3,1,1,1,5); Literature and own estimations

                concrete, normal, at plant                           CH          0               m3           -                      -                    -                 -                      -                5.37E-4                      -               1   2.18 (3,4,3,1,3,5); Fence foundation
                section bar extrus ion, aluminium                    RER         0               kg       2.64E+0                3.27E+0              2.52E+0           2.84E+0                2.25E+0              3.98E+0                  2.30E+0             1   2.18 (3,4,3,1,3,5); Es timation
                sheet rolling, s teel                                RER         0               kg       1.10E-1                    -                2.67E-1           1.50E+0                    -                    -                        -               1   2.18 (3,4,3,1,3,5); Es timation
                section bar rolling, steel                           RER         0               kg       1.69E+0                    -                    -                 -                  2.00E-1              6.15E+0                      -               1   2.18 (3,4,3,1,3,5); Brunschweiler 1993
                wire drawing, s teel                                 RER         0               kg           -                      -                    -                 -                      -                1.06E+0                      -               1   2.18 (3,4,3,1,3,5); Mes h wire fence
                zinc coating, pieces                                 RER         0               m2           -                      -                    -                 -                      -                1.56E-1                      -               1   2.18 (3,4,3,1,3,5); Es timation
                zinc coating, coils                                  RER         0               m2           -                      -                    -                 -                      -                1.09E-1                      -               1   2.18 (3,4,3,1,3,5); Fence

 trans port     transport, lorry >16t, fleet average                 RER         0               tkm      2.24E-1                1.64E-1              2.56E-1           2.25E-1                2.07E-1               2.17E-1                 1.27E-1             1 2.14 (4,5,na,na,na,na); Standard dis tance 50km

                transport, freight, rail                             RER         0               tkm      1.61E+0                6.54E-1              1.05E+0           1.50E+0                8.52E-1              5.14E+0                  5.26E-1             1 2.14 (4,5,na,na,na,na); Standard dis tances 200km , 600km

                transport, van <3.5t                                 RER         0               tkm      4.44E-1                3.27E-1              4.72E-1           4.34E-1                3.75E-1              1.14E+0                  2.37E-1             1 2.18 (3,4,3,1,3,5); 100km to construction place
                dispos al, packaging cardboard, 19.6% water,
 disposal                                                            CH          0               kg       4.03E-2                    -                1.83E-2           1.33E-1                1.14E-1               8.64E-2                 1.33E-1             1 2.18 (3,4,3,1,3,5); Calculated with us e
                to municipal incineration
                dispos al, building, polyethylene/polypropylene
                                                                     CH          0               kg       7.32E-4                    -                1.92E+0           1.40E-3                1.29E+0               9.09E-4                 1.40E-3             1 2.18 (3,4,3,1,3,5); Dispos al of plas tics parts at end of life
                products , to final dis pos al

                dispos al, building, polystyrene isolation, flame-
                                                                     CH          0               kg       3.66E-3                    -                8.30E-3           7.02E-3                6.02E-3               4.55E-3                 7.02E-3             1 2.18 (3,4,3,1,3,5); Dispos al of plas tics parts at end of life
                retardant, to final dispos al
                Trans formation, from pas ture and m eadow              -          -             m2           -                      -                    -                 -                      -                4.72E+0                      -               1 2.18 (3,4,3,1,3,5); Tucs on Electric Power

                Trans formation, to indus trial area, built up          -          -             m2           -                      -                    -                 -                      -                1.50E+0                      -               1 2.15 (1,3,2,3,3,5); Literature and own estimations

                Trans formation, to indus trial area, vegetation        -          -             m2           -                      -                    -                 -                      -                3.22E+0                      -               1 2.16 (3,3,2,3,3,5); Literature and own estimations
                Occupation, indus trial area, built up                -         - m2a                         -                      -                    -                 -                      -                4.50E+1                     -                1 2.16 (3,3,2,3,3,5); Ass um ed life time: 30 a
                Occupation, indus trial area, vegetation              -         - m2a                         -                      -                    -                 -                      -                9.66E+1                     -                1 2.16 (3,3,2,3,3,5); Ass um ed life time: 30 a
 product        facade cons truction, mounted, at building           RER        1 m2                      1.00E+0                   0                    0                 0                      0                    0                        0
                facade cons truction, integrated, at building        RER        1 m2                          -                  1.00E+0                 0                 0                      0                    0                        0
                flat roof cons truction, on roof                     RER        1 m2                          -                      -                1.00E+0              0                      0                    0                        0
                slanted-roof cons truction, mounted, on roof         RER        1 m2                          -                      -                    -             1.00E+0                   0                    0                        0
                slanted-roof cons truction, integrated, on roof      RER        1 m2                          -                      -                    -                 -                  1.00E+0                 0                        0
                open ground cons truction, on ground                 RER        1 m2                          -                      -                    -                 -                     0                 1.00E+0                     0
                slanted-roof cons truction, mounted, on roof,
                                                                     CH         1                m2           -                      -                    -                 -                     0                     0                    1.00E+0
                Stade de Suiss e

 information    total weight, materials                                                          kg                  4.5                    3.3                4.7                 4.5                    3.9                  11.5                    2.5                      Sum from the inventory
                total weight, s tructure                                                         kg                  4.4                    3.3                4.7                 4.3                    3.7                  11.4                    2.4                      Sum from the inventory
                panel area                                                                       m2                  1.0                    1.0                1.0                 1.0                    1.0                   1.0                    1.0
                minimum weight, construction                                                     kg                                         1.5                1.5                 1.0                    1.0                      -                      -                     Siemer 2008
                maxim um, cons truction                                                          kg                                        12.5               20.0                20.0                   15.0                      -                      -                     Siemer 2008
                number, examples                                                                 1                                          10                 34                  35                     10                      -                      -                      Siemer 2008
                mean, cons truction, 2008, weighted with the
                                                                                                 kg                      4.5                3.3                 4.7                4.5                    3.7                       -                        -                  Siemer 2008
                installed capacity
                standard deviation                                                               kg                                          1.2                3.1                 1.2                    2.0                       -                    -                     Siemer 2008
                correction factor                                                                %                  0.81                   0.96               0.40                1.54                   1.32                       -                    -                      Calculated for this study
                mean, cons truction, 2007, ecoinvent v2.0
                mean, cons truction, 2003, ecoinvent v1.0
                                                                                                 kg
                                                                                                 kg
                                                                                                                     4.5
                                                                                                                     4.9
                                                                                                                                            4.0                7.0
                                                                                                                                                               6.2
                                                                                                                                                                                   4.5
                                                                                                                                                                                   4.4
                                                                                                                                                                                                            57
                                                                                                                                                                                                          4.0                       -
                                                                                                                                                                                                                                    -
                                                                                                                                                                                                                                                         -
                                                                                                                                                                                                                                                         -
                                                                                                                                                                                                                                                                                Siemer 2007
                                                                                                                                                                                                                                                                                Siemer 2003
 IEA-PVPS-TASK 12            Life Cycle Inventories and Life Cycle Assessments of Photovoltaic Systems




 5.6. Electrical Components

 5.6.1 Roof Top Installations

Name                          Electrical cabling for module interconnection and AC-interface
Time period                   2006
Geography                     Europe, Western
Technology                    Average technology
Representativeness            Mixed data
Date                          11/6/2006
Collection method             For roof top systems: 4 rows of 13 SolarWorld SW220 poly module with 6 x 10 multicrystalline cells of 156 mm x 156 mm.
Data treatment                Scaled to 1 m2 of module area
Comment                       For systems with modules in 150-170 Wp range and dimension of about 1 x 1.3 m2, connected to a
                              4.6 kW inverter. See ref 1.

Table 5.6.1.1: LCI of DC Cable (1)
Type of system                       on-roof or in-roof     ground                      ground
                                                            PhönixSonnenstrom           Springerville
Products                    Unit Amount                     Amount                      Amount       Comment
DC Cabling                  m2                          1                          1               1 per m2 module area
Materials/fuels
copper                      kg                      0.10                       0.62             0.64 2.2 m DC cable and 0.1 m AC cable
TPE = Thermoplastic
elastomer                   kg                      0.06                       0.25             0.48
Electricity
electricity, medium
voltage                     kWh                       0.0                        0.0             0.0 unknown
Emissions                                                                                            unknown
Waste to treatment                                                                                   Unknown
 Note
 1) Typical cable lengths for a roof top system are: 2.2 m DC cable and 0.1 m AC cable per m2 of module/array area
                                                                          58
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
