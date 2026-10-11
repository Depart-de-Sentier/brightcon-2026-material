You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Heat, at 30 m2 Cu collector, multiple dwelling, flat roof, for hot water` [CH], reference unit 1 MJ, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~6 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: heat / solar
- includedProcesses: Delivery of heat with a solar system including maintenance and electricity use for operation. Excluding the necessary auxiliary heating.
- technology: Solar collector system for hot water installed on the roof of a house.
- generalComment: Use of a solar system excluding the necessary auxiliary heating. The simulation is made for solar collector systems in the city of Zurich. The annual irradiation amounts to 1249 kWh/m2. 50% solar fraction, 30° inclination, 22° southeast orientation.;
UUID: 77118480-7825-3740-b98e-28aa1e71384a
- source cited in the metadata: Stucki M. | 2012 | 2012 - Update LCI solar collectors - Stucki
- time period: 2010-01-2010-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 MJ):
- Energy, Solar, Converted: 1.144 megajoule (natural resource)

## Report excerpt

Source file: `report-p18-20.txt` (SHA-256 715f64cad2dac6fad6fea014d976a59f700ae592cf5f53b2d11f8b7cb28b8dd1), pages 18-20 of `2012 - Update LCI solar collectors - Stucki.pdf`.

```
3. Life cycle inventories of the operation of solar thermal installations

Tab. 3.1          Collector yield, solar net yield, converted solar energy, and auxiliary energy
                  consumption

                                     Annual      Specific     Annual      Converted    Solar net    Con-
                                     collector   collector    solar net   solar        yield over   sumption
                                     yield       yield        yield       energy       life time    of
                                                                          per MJ                    auxiliary
                                                                          heat                      energy
                                                        2
                                     MJ/a        kWh/m *a     MJ/a        MJ/MJ        GJ           kWh/a
solar system, 5 m2 Cu flat plate     82’22       457          6’404       1.28         160          96
collector, one-family house, hot
water
solar system, 10.5 m2 evacuated      21’962      581          14’549      1.51         291          110
tube collector, one-family house,
combined system
solar system, 12 m2 Cu flat plate    17’366      402          11’027      1.57         276          104
collector, one-family house,
combined system
solar system, 20 m2 Cu flat plate    40’270      559          35’899      1.12         897          145
collector, on slanted roof, hot
water
solar system, 30 m2 Cu flat plate    55’393      513          48’931      1.13         1223         154
collector, on slanted roof, hot
water
solar system, 30 m2 Al flat plate    55’703      513          48’683      1.14         1217         158
collector, on slanted roof, hot
water
solar system, 30 m2 Cu flat plate    55’393      516          48’931      1.13         1223         154
collector, on flat roof, hot water
solar system, 81 m2 Cu flat plate    166’691     572          154’235     1.08         3856         938
collector, multiple dwelling, hot
water


The maintenance of the solar thermal system includes cleaning of the heat storage and the collectors,
as well as controlling of the heat transfer medium. In the life cycle inventory, it is assumed that a
maintenance team travels 50 km every 5 years by van. Other aspects of maintenance are not
considered.
The unit process raw data of the solar thermal systems are displayed in Tab. 3.2. The EcoSpold meta
information is shown in Tab. 3.3.




                                                    - 16 -                                 ESU-services Ltd.
                                                                                                         3. Life cycle inventories of the operation of solar thermal installations

Tab. 3.2                   Unit process raw data of the supply of useful heat from solar thermal systems without considering auxiliary heating




                                                                                                                                                                                                                                                                                      StandardDeviation95%
                                                                        InfrastructureProcess
                                                                                                                                                                                                                               heat, at 10.5 m2 heat, at 10.5 m2




                                                                                                                                                                                                                                                                    UncertaintyType
                                                                                                                         heat, at 12 m2 heat, at 20 m2 heat, at 30 m2 heat, at 30 m2 heat, at 30 m2
                                                                                                                                                                                                              heat, at 81 m2 evacuated tube evacuated tube
                                                                                                     heat, at 5 m2 Cu     Cu collector,   Cu collector,     Cu collector,   Cu collector,   Al-Cu collector,




                                                             Location
                                                                                                                                                                                                               Cu collector,    collector, heat collector, glass-
                                                                                                      collector, one-      one-family       multiple          multiple        multiple          multiple
                                    Name                                                        Unit                                                                                                             multiple      pipe, one-family glass tube, one-                                             GeneralComment
                                                                                                     family house, for     house, for   dwelling, slanted dwelling, slanted dwelling, flat dwelling, slanted
                                                                                                                                                                                                             dwelling, for hot    house, for    family house, for
                                                                                                        hot water          combined       roof, for hot     roof, for hot   roof, for hot     roof, for hot
                                                                                                                                                                                                                  water           combined         combined
                                                                                                                            system            water             water          water             water
                                                                                                                                                                                                                                    system           system


                                  Location                                                                  CH                CH               CH               CH                CH               CH               CH               CH                CH
                           InfrastructureProcess                                                             0                 0                0                0                 0                0                0                0                 0
                                    Unit                                                                    MJ                MJ               MJ               MJ                MJ               MJ               MJ               MJ                MJ
                                                                                                                                                                                                                                                                                                             (2,na,1,1,1,na); Includes
resource, in air   Energy, solar, converted                    -             -                  MJ       1.28E+0           1.57E+0           1.12E+0          1.13E+0          1.14E+0          1.13E+0           1.08E+0          1.51E+0          1.51E+0           1 1.07
                                                                                                                                                                                                                                                                                                             losses in the system
                                                                                                                                                                                                                                                                                                             (2,na,1,1,1,na);
technosphere       electricity, low voltage, at grid         CH 0 kWh                                    1.50E-2            9.46E-3          4.05E-3          3.15E-3          3.25E-3           3.15E-3          6.08E-3          7.58E-3          7.58E-3           1 1.07
                                                                                                                                                                                                                                                                                                             Simulation

                   solar system, 5 m2 Cu flat plate                                                                                                                                                                                                                                                          (2,na,1,1,1,na);
                                                          CH 1 unit                                      6.25E-6               -                 -                -                -                -                -                 -                -             1 3.00
                   collector, one-family house, hot water                                                                                                                                                                                                                                                    Simulation

                   solar system, 12 m2 Cu flat plate
                                                                                                                                                                                                                                                                                                             (2,na,1,1,1,na);
                   collector, one-family house,              CH 1 unit                                       -              3.63E-6              -                -                -                -                -                 -                -             1 3.00
                                                                                                                                                                                                                                                                                                             Simulation
                   combined system
                   solar system, 20 m2 Cu flat plate                                                                                                                                                                                                                                                         (2,na,1,1,1,na);
                                                             CH 1 unit                                       -                 -             1.11E-6              -                -                -                -                 -                -             1 3.00
                   collector, on slanted roof, hot water                                                                                                                                                                                                                                                     Simulation

                   solar system, 30 m2 Cu flat plate                                                                                                                                                                                                                                                         (2,na,1,1,1,na);
                                                             CH 1 unit                                       -                 -                 -            8.17E-7              -                -                -                 -                -             1 3.00
                   collector, on slanted roof, hot water                                                                                                                                                                                                                                                     Simulation

                   solar system, 30 m2 Cu flat plate                                                                                                                                                                                                                                                         (2,na,1,1,1,na);
                                                             CH 1 unit                                       -                 -                 -                -            8.22E-7              -                -                 -                -             1 3.00
                   collector, on flat roof, hot water                                                                                                                                                                                                                                                        Simulation

                   solar system, 30 m2 Al-Cu flat plate                                                                                                                                                                                                                                                      (2,na,1,1,1,na);
                                                             CH 1 unit                                       -                 -                 -                -                -             8.17E-7             -                 -                -             1 3.00
                   collector, on slanted roof, hot water                                                                                                                                                                                                                                                     Simulation

                   solar system, 81 m2 Cu flat plate                                                                                                                                                                                                                                                         (2,na,1,1,1,na);
                                                             CH 1 unit                                       -                 -                 -                -                -                -             2.59E-7              -                -             1 3.00
                   collector, multiple dwelling, hot water                                                                                                                                                                                                                                                   Simulation
                   solar system, 10.5 m2 evacuated
                                                                                                                                                                                                                                                                                                             (2,na,1,1,1,na);
                   tube collector, one-family house,         CH 1 unit                                       -                 -                 -                -                -                -                -             2.75E-6          3.44E-6           1 3.00
                                                                                                                                                                                                                                                                                                             Simulation
                   combined system
                                                                                                                                                                                                                                                                             (2,na,1,1,1,na); 250km
                   transport, van <3.5t                      CH 0 tkm                                    4.22E-4            2.45E-4          7.52E-5          5.52E-5          5.55E-5           5.52E-5          1.75E-5          1.86E-4          1.86E-4           1 3.00 per plant for
                                                                                                                                                                                                                                                                             maintenance
                                                                                                                                                                                                                                                                             (2,na,1,1,1,na);
emission air, high
                   Heat, waste                                 -             -                  MJ       1.34E+0           1.61E+0           1.14E+0          1.14E+0          1.16E+0          1.14E+0           1.10E+0          1.54E+0          1.54E+0           1 1.07 Simulation and solar
population density
                                                                                                                                                                                                                                                                             energy




                                                                                                                                                              - 17 -                                                                                                                    ESU-services Ltd.
                                                                                                3. Life cycle inventories of the operation of solar thermal installations

Tab. 3.3                           EcoSpold meta information of the supply of useful heat from solar thermal systems without considering auxiliary heating


                                                                                              heat, at 10.5 m2 evacuated tube
                             heat, at 5 m2 Cu collector,    heat, at 10.5 m2 evacuated tube                                     heat, at 12 m2 Cu collector, heat, at 20 m2 Cu collector, heat, at 30 m2 Cu collector, heat, at 30 m2 Cu collector,                     heat, at 30 m2 Al-Cu         heat, at 81 m2 Cu collector,
                                                                                              collector, glass-glass tube, one-
Name                          one-family house, for hot      collector, heat pipe, one-family                                      one-family house, for      multiple dwelling, slanted   multiple dwelling, slanted   multiple dwelling, flat roof,                collector, multiple dwelling,    multiple dwelling, for hot
                                                                                                family house, for combined
                                        water                 house, for combined system                                             combined system              roof, for hot water          roof, for hot water             for hot water                          slanted roof, for hot water                water
                                                                                                            system
Location                                 CH                                CH                                  CH                                CH                              CH                              CH                              CH                              CH                               CH
InfrastructureProcess                     0                                 0                                   0                                 0                               0                               0                               0                               0                                0
Unit                                     MJ                                MJ                                  MJ                                MJ                              MJ                              MJ                              MJ                              MJ                               MJ
                                                                                               Delivery of heat with a solar
                                                                                               system including maintenance
                            Delivery of heat with a solar                                      and electricity use for operation.   Delivery of heat with a solar   Delivery of heat with a solar   Delivery of heat with a solar   Delivery of heat with a solar   Delivery of heat with a solar    Delivery of heat with a solar
                                                            Delivery of heat with a solar
                            system including                                                   Excluding the necessary              system including                system including                system including                system including                system including                 system including
                                                            system including maintenance
                            maintenance and electricity                                        auxiliary heating. Rough             maintenance and electricity     maintenance and electricity     maintenance and electricity     maintenance and electricity     maintenance and electricity      maintenance and electricity
IncludedProcesses                                           and electricity use for operation.
                            use for operation. Excluding                                       assumption for a glass-glass         use for operation. Excluding    use for operation. Excluding    use for operation. Excluding    use for operation. Excluding    use for operation. Excluding     use for operation. Excluding
                                                            Excluding the necessary
                            the necessary auxiliary                                            tube collector system by             the necessary auxiliary         the necessary auxiliary         the necessary auxiliary         the necessary auxiliary         the necessary auxiliary          the necessary auxiliary
                                                            auxiliary heating.
                            heating.                                                           considering a heat pipe system       heating.                        heating.                        heating.                        heating.                        heating.                         heating.
                                                                                               correcting the life time from 25
                                                                                               years to 20 years.
                                                            Nutzwärme, ab 10.5 m2              Nutzwärme, ab 10.5 m2                                                Nutzwärme, ab 20 m2 Cu-         Nutzwärme, ab 30 m2 Cu-         Nutzwärme, ab 30 m2 CU-         Nutzwärme, ab 30 m2 Al-Cu-
                            Nutzwärme, ab 5 m2                                                                                      Nutzwärme, ab 12 m2 Cu-                                                                                                                                    Nutzwärme, ab 81 m2 Cu-
                                                            Vakuumröhrenkollektoranlage,       Vakuumröhrenkollektoranlage,                                         Kollektoranlage, auf            Kollektoranlage, auf            Kollektoranlage, auf            Kollektoranl., auf
LocalName                   Kollektoranlage, EFH, für                                                                               Kollektoranlage, EFH, für                                                                                                                                  Kollektoranlage, MFH, für
                                                            Wärmeröhren, EFH, für              Sidneyröhren, EFH, für                                               Schrägdach, für                 Schrägdach, für                 Flachdach, für                  Schrägdach, für
                            Warmwasserspeicher                                                                                      Wärmespeicher                                                                                                                                              Warmwasserspeicher
                                                            Wärmespeicher                      Wärmespeicher                                                        Warmwasserspeicher              Warmwasserspeicher              Warmwasserspeicher              Warmwasserspeicher
Synonyms                                                                                       Sidney collector, China collector

                            Use of a solar system                                                                                   Use of a solar system           Use of a solar system           Use of a solar system           Use of a solar system           Use of a solar system            Use of a solar system
                                                            Use of a solar system with heat Use of a solar system with glass-
                            excluding the necessary                                                                                 excluding the necessary         excluding the necessary         excluding the necessary         excluding the necessary         excluding the necessary          excluding the necessary
                                                            pipes excluding the necessary      glass pipes excluding the
                            auxiliary heating. The                                                                                  auxiliary heating. The          auxiliary heating. The          auxiliary heating. The          auxiliary heating. The          auxiliary heating. The           auxiliary heating. The
                                                            auxiliary heating. The simulation necessary auxiliary heating. The
                            simulation is made for solar                                                                            simulation is made for solar    simulation is made for solar    simulation is made for solar    simulation is made for solar    simulation is made for solar     simulation is made for solar
                                                            is made for solar collector        simulation is made for heat pipe
                            collector systems in the city                                                                           collector systems in the city   collector systems in the city   collector systems in the city   collector systems in the city   collector systems in the city    collector systems in the city
GeneralComment                                              systems in the city of Zurich. The solar collector systems in the city
                            of Zurich. The annual                                                                                   of Zurich. The annual           of Zurich. The annual           of Zurich. The annual           of Zurich. The annual           of Zurich. The annual            of Zurich. The annual
                                                            annual irradiation amounts to      of Zurich. The annual irradiation
                            irradiation amounts to 1249                   2                                               2         irradiation amounts to 1249     irradiation amounts to 1249     irradiation amounts to 1249     irradiation amounts to 1249     irradiation amounts to 1249      irradiation amounts to 1249
                                                            1249 kWh/m . 33% solar             amounts to 1249 kWh/m . 33%
                            kWh/m2. 65% solar fraction,                                                                             kWh/m2. 28% solar fraction,     kWh/m2. 37% solar fraction,     kWh/m2. 50% solar fraction,     kWh/m2. 50% solar fraction,     kWh/m2. 50% solar fraction,      kWh/m2. 40% solar fraction,
                                                            fraction, 35° inclination, 22°     solar fraction, 35° inclination, 22°
                            30° inclination, 22°                                                                                    35° inclination, 22°            30° inclination, 22°            30° inclination, 22°            30° inclination, 22°            30° inclination, 22°             30° inclination, 22°
                                                            southeast orientation.             southeast orientation.
                            southeast orientation.                                                                                  southeast orientation.          southeast orientation.          southeast orientation.          southeast orientation.          southeast orientation.           southeast orientation.
Category                    solar collector systems         solar collector systems            solar collector systems              solar collector systems         solar collector systems         solar collector systems         solar collector systems         solar collector systems          solar collector systems
SubCategory                 systems                         systems                            systems                              systems                         systems                         systems                         systems                         systems                          systems
LocalCategory               Sonnenkollektoranlagen          Sonnenkollektoranlagen             Sonnenkollektoranlagen               Sonnenkollektoranlagen          Sonnenkollektoranlagen          Sonnenkollektoranlagen          Sonnenkollektoranlagen          Sonnenkollektoranlagen           Sonnenkollektoranlagen
LocalSubCategory            Kollektorsysteme                Kollektorsysteme                   Kollektorsysteme                     Kollektorsysteme                Kollektorsysteme                Kollektorsysteme                Kollektorsysteme                Kollektorsysteme                 Kollektorsysteme
Formula
StatisticalClassification
CASNumber
StartDate                   2010                            2010                               2010                                 2010                            2010                            2010                            2010                            2010                             2010
EndDate                     2010                            2010                               2010                                 2010                            2010                            2010                            2010                            2010                             2010
OtherPeriodText             Time of simulation.             Time of simulation.                Time of simulation.                  Time of simulation.             Time of simulation.             Time of simulation.             Time of simulation.             Time of simulation.              Time of simulation.

                            Solar collector system          Solar collector system operated Solar collector system operated Solar collector system                  Solar collector system          Solar collector system          Solar collector system          Solar collector system           Solar collector system
Text
                            operated in CH.                 in CH.                          in CH.                          operated in CH.                         operated in CH.                 operated in CH.                 operated in CH.                 operated in CH.                  operated in CH.


                            Solar collector system for      Solar collector system for hot     Solar collector system for hot       Solar collector system for      Solar collector system for      Solar collector system for      Solar collector system for      Solar collector system for       Solar collector system for
Text                        hot water installed on the      water installed on the roof of a   water installed on the roof of a     hot water installed on the      hot water installed on the      hot water installed on the      hot water installed on the      hot water installed on the       hot water installed on the
                            roof of a house.                house.                             house.                               roof of a house.                roof of a house.                roof of a house.                roof of a house.                roof of a house.                 roof of a house.

Percent

                            Total heat delivered by flat    Total solar heat delivered by      Total solar heat delivered by        Total heat delivered by flat    Total heat delivered by flat    Total heat delivered by flat    Total heat delivered by flat    Total heat delivered by flat     Total heat delivered by flat
ProductionVolume            plate collectors in CH in       evacuated tube collectors in       evacuated tube collectors in         plate collectors in CH in       plate collectors in CH in       plate collectors in CH in       plate collectors in CH in       plate collectors in CH in        plate collectors in CH in
                            2008 was 213'500 MWh.           2001 was 2.3TJ.                    2001 was 2.3TJ.                      2008 was 213'500 MWh.           2008 was 213'500 MWh.           2008 was 213'500 MWh.           2008 was 213'500 MWh.           2008 was 213'500 MWh.            2008 was 213'500 MWh.


SamplingProcedure           Own simulation.                 Own simulation.                    Own simulation.                      Own simulation.                 Own simulation.                 Own simulation.                 Own simulation.                 Own simulation.                  Own simulation.

Extrapolations              none                            none                               none                                 none                            none                            none                            none                            none                             none




                                                                                                                                                                    - 18 -                                                                                                                               ESU-services Ltd.
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 MJ.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
