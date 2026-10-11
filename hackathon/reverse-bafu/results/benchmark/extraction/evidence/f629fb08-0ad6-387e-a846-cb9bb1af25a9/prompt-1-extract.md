You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Compressed air, average generation, <30kW, 10 bar gauge, at compressor` [RER], reference unit 1 m3, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~8 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: compressed air / generation
- includedProcesses: This dataset includes the compressor, operating materials (lubricating oil), the electricity consumption as well as the transports of the compressor and the lubricant to the installation site. The installation at the site is not included.
- technology: Average technology
- generalComment:  As there is some variation from factory to factory with regard to the LCI, it is advised that in case this dataset becomes important in the results, it is recommended to investigated further if the assumptions made for this dataset are applicable or not. ;
UUID: f629fb08-0ad6-387e-a846-cb9bb1af25a9
- source cited in the metadata: Steiner R. | 2007 | 2007 - LCI metal proc. and comp. air supply - Steiner
- time period: 2006-01-2007-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 m3):
- none

## Report excerpt

Source file: `report-p88-90.txt` (SHA-256 f63b09c007cb424c0093d99dddcf356c40c9105f86735b1144c0bc4ddc47997f), pages 88-90 of `2007 - LCI metal proc. and comp. air supply - Steiner.pdf`.

```
10. Compressed Air Supply


Tab. 10.12: Electricity consumption and leakage rate used in this study for compressed air installations <30kW


         Installations with <30kW                                                         This Study                                           This Study                                               This Study
                                                                                     at 8 bar gauge                                       at 10 bar gauge                                            at 12 bar gauge
Average Industry Values
Leakage Rate                                                 %                                        50%                                          50%                                                       50%
Electricity Consumption per air                              kWh/m3                                   0.157                                        0.181                                                     0.207
volume at compressor
Remarks                                                                             Deduced from the 10 Average value of                                                                    Deduced from the 10
                                                                                    bar pressure level  four installations                                                                  bar pressure level
                                                                                    assuming a          (Tab. 10.10)                                                                        assuming an
                                                                                    reduction of 7%/bar                                                                                     increase of 7%/bar
Optimised Industry Values
Leakage Rate                                                 %                                         5%                                           5%                                                        5%
Electricity Consumption per air                              kWh/m3                                   0.131                                        0.151                                                     0.173
volume at compressor
Remarks                                                                             Deduced from the 10 Average value of two                                                                Deduced from the 10
                                                                                    bar pressure level  installations (Tab.                                                                 bar pressure level
                                                                                    assuming a          10.11)                                                                              assuming an
                                                                                    reduction of 7%/bar                                                                                     increase of 7%/bar



10.3.4 LCI Input Data

Tab. 10.13: Unit process raw data of the datasets “air compressor, screw type compressor"”




                                                                                                                                                                                   StandardDeviati
                                                                                                  InfrastructurePr




                                                                                                                                                                  UncertaintyTyp
                                                                                                                             air compressor,    air compressor,
                                                                                       Location




                                                                                                                                                                                       on95%
                                                                                                       ocess




                                                                                                                                screw-type         screw-type
                                                                                                                      Unit




                                               Name                                                                                                                                                   GeneralComment

                                                                                                                                                                        e
                                                                                                                             compressor, 4     compressor, 300
                                                                                                                               kW, at plant       kW, at plant

                                                Location                                                                          RER               RER
                                         InfrastructureProcess                                                                     1                 1
                                                  Unit                                                                            unit              unit
product        air compressor, screw-type compressor, 4 kW, at plant                  RER              1             unit          1
product        air compressor, screw-type compressor, 300 kW, at plant                RER              1             unit                            1
technosphere   chromium steel 18/8, at plant                                          RER              0             kg         1.60E+1           2.50E+2              1            1.24              (1,4,1,3,1,5); manufacturer data
               steel, low-alloyed, at plant                                           RER              0             kg         4.00E+1           2.10E+3              1            1.24              (1,4,1,3,1,5); manufacturer data
               cast iron, at plant                                                    RER              0             kg         3.00E+1           1.70E+3              1            1.24              (1,4,1,3,1,5); manufacturer data
               copper, at regional storage                                            RER              0             kg         2.00E+1           3.00E+2              1            1.24              (1,4,1,3,1,5); manufacturer data
               aluminium, production mix, at plant                                    RER              0             kg         2.00E+1           2.20E+2              1            1.24              (1,4,1,3,1,5); manufacturer data
               polystyrene, high impact, HIPS, at plant                               RER              0             kg         1.00E+1           2.00E+1              1            1.24              (1,4,1,3,1,5); manufacturer data
               printed wiring board, surface mount, at plant                          GLO              0             m2         2.51E-1           2.51E-1              1            1.24              (1,4,1,3,1,5); manufacturer data
               synthetic rubber, at plant                                             RER              0             kg         3.00E+0           9.00E+0              1            1.24              (1,4,1,3,1,5); manufacturer data
               sheet rolling, chromium steel                                          RER              0             kg         1.60E+1           2.50E+2              1            1.24              (1,4,1,3,1,5); manufacturer data
               sheet rolling, steel                                                   RER              0             kg         4.00E+1           2.10E+3              1            1.24              (1,4,1,3,1,5); manufacturer data
               sheet rolling, aluminium                                               RER              0             kg         2.00E+1           2.20E+2              1            1.24              (4,3,2,1,1,4); estimation
               wire drawing, copper                                                   RER              0             kg         2.00E+1           3.00E+2              1            1.24              (4,3,2,1,1,4); estimation
               injection moulding                                                     RER              0             kg         1.00E+1           2.00E+1              1            1.24              (4,3,2,1,1,4); estimation
               disposal, polystyrene, 0.2% water, to municipal incineration           CH               0             kg         1.00E+1           2.00E+1              1            1.24              (4,3,2,1,1,4); assumption
               disposal, rubber, unspecified, 0% water, to municipal incineration     CH               0             kg         3.00E+0           9.00E+0              1            1.24              (4,3,2,1,1,4); assumption
                                                                                                                                                                                                      (4,5,1,1,1,5); Standard distance to
               transport, lorry 32t                                                   RER              0             tkm        1.40E+1           4.60E+2              1            2.14
                                                                                                                                                                                                      for materials to manufacturer
                                                                                                                                                                                                      (4,5,1,1,1,5); Standard distance to
               transport, freight, rail                                               RER              0             tkm        2.80E+1           9.20E+2              1            2.14
                                                                                                                                                                                                      for materials to manufacturer




ecoinvent-report No. 23                                                              - 80 -
                                                                                  10. Compressed Air Supply



Tab. 10.14: Unit process raw data of the datasets “compressed air, average generation, <30kW, at compressor ”




                                                                                                                 InfrastructureProc




                                                                                                                                                                                                                              StandardDeviatio
                                                                                                                                                                                                          UncertaintyType
                                                                                                                                                      compressed air, compressed air, compressed air,
                                                                                                                                                          average         average         average




                                                                                                 Location




                                                                                                                                                                                                                                   n95%
                                                                                                                                                        generation,     generation,     generation,




                                                                                                                                          Unit
                                                                                                                         ess
                                                            Name                                                                                                                                                                                       GeneralComment
                                                                                                                                                       <30kW, 8 bar    <30kW, 10 bar <30kW, 12 bar
                                                                                                                                                         gauge, at       gauge, at       gauge, at
                                                                                                                                                        compressor      compressor      compressor
                                                            Location                                                                                       RER             RER             RER
                                                     InfrastructureProcess                                                                                   0              0               0
                                                              Unit                                                                                          m3             m3              m3
product              compressed air, average generation, <30kW, 8 bar gauge, at compressor      RER                    0               m3                   1
product              compressed air, average generation, <30kW, 10 bar gauge, at compressor     RER                    0               m3                                    1
product              compressed air, average generation, <30kW, 12 bar gauge, at compressor     RER                    0               m3                                                    1
technosphere         air compressor, screw-type compressor, 4 kW, at plant                      RER                    1              unit                8.26E-5         8.26E-5         8.26E-5             1                  3.06                  (2,4,2,1,1,5); manufacturer value
                     lubricating oil, at plant                                                  RER                    0               kg                 1.00E-5         1.00E-5         1.00E-5             1                  1.24                  (1,4,1,1,1,5); manufacturer value
                     disposal, used mineral oil, 10% water, to hazardous waste incineration      CH                    0               kg                 1.00E-5         1.00E-5         1.00E-5             1                  1.24                  (1,4,1,1,1,5); manufacturer value
                     electricity, low voltage, production UCTE, at grid                         UCTE                   0              kWh                 1.57E-1         1.81E-1         2.07E-1             1                  1.13                  (1,3,2,1,1,4); average value
                                                                                                                                                                                                                                                       (4,5,1,1,1,5); assuming 100km lorry,
                     transport, lorry >16t, fleet average                                       RER                    0              tkm                 1.16E-3         1.16E-3         1.16E-3             1                  2.14                  200km train for transport of
                                                                                                                                                                                                                                                       compressor and lubricating oil
                                                                                                                                                                                                                                                       (4,5,1,1,1,5); assuming 100km lorry,
                     transport, freight, rail                                                   RER                    0              tkm                 2.31E-3         2.31E-3         2.31E-3             1                  2.14                  200km train for transport of
                                                                                                                                                                                                                                                       compressor and lubricating oil
emission air, high
                     Heat, waste                                                                   -                    -                 MJ              5.64E-1         6.52E-1         7.46E-1             1                  1.13                  (1,3,2,1,1,4);
population density




Tab. 10.15: Unit process raw data of the datasets “compressed air, optimised generation, <30kW, at compressor ”


                                                                                                                InfrastructureProc




                                                                                                                                                                                                                            StandardDeviatio
                                                                                                                                                                                                        UncertaintyType
                                                                                                                                                     compressed air, compressed air, compressed air,
                                                                                                                                                        optimised       optimised       optimised
                                                                                                 Location




                                                                                                                                                                                                                                 n95%
                                                                                                                                                       generation,     generation,     generation,
                                                                                                                                          Unit
                                                                                                                        ess
                                                            Name                                                                                                                                                                                      GeneralComment
                                                                                                                                                      <30kW, 8 bar    <30kW, 10 bar <30kW, 12 bar
                                                                                                                                                        gauge, at       gauge, at       gauge, at
                                                                                                                                                       compressor      compressor      compressor
                                                            Location                                                                                       RER             RER             RER
                                                     InfrastructureProcess                                                                                  0               0               0
                                                              Unit                                                                                         m3              m3              m3
product              compressed air, optimised generation, <30kW, 8 bar gauge, at compressor    RER                    0               m3                   1
product              compressed air, optimised generation, <30kW, 10 bar gauge, at compressor   RER                    0               m3                                   1
product              compressed air, optimised generation, <30kW, 12 bar gauge, at compressor   RER                    0               m3                                                    1
technosphere         air compressor, screw-type compressor, 4 kW, at plant                      RER                    1              unit                1.57E-4        1.57E-4          1.57E-4           1                  3.06                   (2,4,2,1,1,5); manufacturer value
                     lubricating oil, at plant                                                  RER                    0               kg                 1.00E-5        1.00E-5          1.00E-5           1                  1.24                   (1,4,1,1,1,5); manufacturer value
                     disposal, used mineral oil, 10% water, to hazardous waste incineration      CH                    0               kg                 1.00E-5        1.00E-5          1.00E-5           1                  1.24                   (1,4,1,1,1,5); manufacturer value
                     electricity, low voltage, production UCTE, at grid                         UCTE                   0              kWh                 1.31E-1        1.51E-1          1.73E-1           1                  1.13                   (1,3,2,1,1,4); average value
                                                                                                                                                                                                                                                      (4,5,1,1,1,5); assuming 100km lorry,
                     transport, lorry >16t, fleet average                                       RER                    0              tkm                 2.20E-3        2.20E-3          2.20E-3           1                  2.14                   200km train for transport of
                                                                                                                                                                                                                                                      compressor and lubricating oil
                                                                                                                                                                                                                                                      (4,5,1,1,1,5); assuming 100km lorry,
                     transport, freight, rail                                                   RER                    0              tkm                 4.39E-3        4.39E-3          4.39E-3           1                  2.14                   200km train for transport of
                                                                                                                                                                                                                                                      compressor and lubricating oil
emission air, high
                     Heat, waste                                                                   -                   -              MJ                  4.70E-1        5.44E-1          6.22E-1           1                  1.13                   (1,3,2,1,1,4);
population density




Tab. 10.16: Unit process raw data of the datasets “compressed air, average generation, >30kW, at compressor ”
                                                                                                                             InfrastructureProc




                                                                                                                                                                                                                                                 StandardDeviatio
                                                                                                                                                                                                                            UncertaintyType




                                                                                                                                                          compressed air, compressed air, compressed air,
                                                                                                                                                              average         average         average
                                                                                                            Location




                                                                                                                                                                                                                                                      n95%




                                                                                                                                                            generation,     generation,     generation,
                                                                                                                                                   Unit
                                                                                                                                     ess




                                                             Name                                                                                                                                                                                                   GeneralComment
                                                                                                                                                           >30kW, 6 bar    >30kW, 7 bar    >30kW, 8 bar
                                                                                                                                                             gauge, at       gauge, at       gauge, at
                                                                                                                                                            compressor      compressor      compressor
                                                        Location                                                                                               RER               RER             RER
                                                 InfrastructureProcess                                                                                          0                 0               0
                                                          Unit                                                                                                 m3                m3              m3
product              compressed air, average generation, >30kW, 6 bar gauge, at compressor              RER                           0           m3            1
product              compressed air, average generation, >30kW, 7 bar gauge, at compressor              RER                           0           m3                               1
product              compressed air, average generation, >30kW, 8 bar gauge, at compressor              RER                           0           m3                                                1
                                                                                                                                                                                                                                                                    (1,4,1,1,1,5); manufacturer
technosphere         air compressor, screw-type compressor, 300 kW, at plant                            RER                           1           unit       6.30E-8            6.30E-8       6.30E-8                           1                 3.06
                                                                                                                                                                                                                                                                    value
                                                                                                                                                                                                                                                                    (1,4,1,1,1,5); manufacturer
                     lubricating oil, at plant                                                          RER                           0           kg         2.08E-6            2.08E-6       2.08E-6                           1                 1.24
                                                                                                                                                                                                                                                                    value
                                                                                                                                                                                                                                                                    (1,4,1,1,1,5); manufacturer
                     disposal, used mineral oil, 10% water, to hazardous waste incineration                 CH                        0           kg         2.08E-6            2.08E-6       2.08E-6                           1                 1.24
                                                                                                                                                                                                                                                                    value
                     electricity, low voltage, production UCTE, at grid                              UCTE                             0           kWh        1.39E-1            1.49E-1       1.59E-1                           1                 1.13              (1,3,2,1,1,4); average value

                                                                                                                                                                                                                                                                    (4,5,1,1,1,5); assuming
                                                                                                                                                                                                                                                                    100km lorry, 200km train for
                     transport, lorry >16t, fleet average                                               RER                           0           tkm        2.90E-5            2.90E-5       2.90E-5                           1                 2.14
                                                                                                                                                                                                                                                                    transport of compressor and
                                                                                                                                                                                                                                                                    lubricating oil

                                                                                                                                                                                                                                                                    (4,5,1,1,1,5); assuming
                                                                                                                                                                                                                                                                    100km lorry, 200km train for
                     transport, freight, rail                                                           RER                           0           tkm        5.80E-5            5.80E-5       5.80E-5                           1                 2.14
                                                                                                                                                                                                                                                                    transport of compressor and
                                                                                                                                                                                                                                                                    lubricating oil

emission air, high
                     Heat, waste                                                                             -                        -           MJ         4.99E-1            5.36E-1       5.74E-1                           1                 1.13              (1,3,2,1,1,4); from electricity
population density




ecoinvent-report No. 23                                                                         - 81 -
                                                                                   10. Compressed Air Supply



Tab. 10.17: Unit process raw data of the datasets “compressed air, optimised generation, >30kW, at compressor ”




                                                                                                                                 InfrastructureProc




                                                                                                                                                                                                                                                     StandardDeviatio
                                                                                                                                                                                                                                   UncertaintyType
                                                                                                                                                               compressed air, compressed air, compressed air,
                                                                                                                                                                  optimised       optimised       optimised




                                                                                                              Location




                                                                                                                                                                                                                                                          n95%
                                                                                                                                                                 generation,     generation,     generation,




                                                                                                                                                       Unit
                                                                                                                                         ess
                                                             Name                                                                                                                                                                                                       GeneralComment
                                                                                                                                                                >30kW, 6 bar    >30kW, 7 bar    >30kW, 8 bar
                                                                                                                                                                  gauge, at       gauge, at       gauge, at
                                                                                                                                                                 compressor      compressor      compressor
                                                          Location                                                                                                   RER              RER                RER
                                                   InfrastructureProcess                                                                                              0                0                  0
                                                            Unit                                                                                                     m3               m3                 m3
product               compressed air, optimised generation, >30kW, 6 bar gauge, at compressor              RER                         0              m3              1
product               compressed air, optimised generation, >30kW, 7 bar gauge, at compressor              RER                         0              m3                                1
product               compressed air, optimised generation, >30kW, 8 bar gauge, at compressor              RER                         0              m3                                                  1
                                                                                                                                                                                                                                                                        (1,4,1,1,1,5); manufacturer
technosphere          air compressor, screw-type compressor, 300 kW, at plant                              RER                         1              unit         7.65E-8           7.65E-8          7.65E-8                          1              3.06
                                                                                                                                                                                                                                                                        value
                                                                                                                                                                                                                                                                        (1,4,1,1,1,5); manufacturer
                      lubricating oil, at plant                                                            RER                         0              kg           2.08E-6           2.08E-6          2.08E-6                          1              1.24
                                                                                                                                                                                                                                                                        value
                                                                                                                                                                                                                                                                        (1,4,1,1,1,5); manufacturer
                      disposal, used mineral oil, 10% water, to hazardous waste incineration               CH                          0              kg           2.08E-6           2.08E-6          2.08E-6                          1              1.24
                                                                                                                                                                                                                                                                        value
                      electricity, low voltage, production UCTE, at grid                                   UCTE                        0              kWh          1.19E-1           1.28E-1          1.37E-1                          1              1.13              (1,3,2,1,1,4); average value

                                                                                                                                                                                                                                                                        (4,5,1,1,1,5); assuming
                                                                                                                                                                                                                                                                        100km lorry, 200km train for
                      transport, lorry >16t, fleet average                                                 RER                         0              tkm          3.52E-5           3.52E-5          3.52E-5                          1              2.14
                                                                                                                                                                                                                                                                        transport of compressor and
                                                                                                                                                                                                                                                                        lubricating oil

                                                                                                                                                                                                                                                                        (4,5,1,1,1,5); assuming
                                                                                                                                                                                                                                                                        100km lorry, 200km train for
                      transport, freight, rail                                                             RER                         0              tkm          7.04E-5           7.04E-5          7.04E-5                          1              2.14
                                                                                                                                                                                                                                                                        transport of compressor and
                                                                                                                                                                                                                                                                        lubricating oil

emission air, high
                      Heat, waste                                                                               -                       -             MJ           4.29E-1           4.61E-1          4.93E-1                          1              1.13              (1,3,2,1,1,4); from electricity
population density




Tab. 10.18: Unit process raw data of the datasets “compressed air, best generation, >30kW, at compressor”
                                                                                                                                 InfrastructureProc




                                                                                                                                                                                                                                                     StandardDeviatio
                                                                                                                                                                                                                                   UncertaintyType
                                                                                                                                                               compressed air, compressed air, compressed air,
                                                                                                              Location




                                                                                                                                                               best generation, best generation, best generation,




                                                                                                                                                                                                                                                          n95%
                                                                                                                                                       Unit
                                                                                                                                         ess




                                                             Name                                                                                               >30kW, 6 bar     >30kW, 7 bar     >30kW, 8 bar                                                          GeneralComment
                                                                                                                                                                  gauge, at        gauge, at        gauge, at
                                                                                                                                                                 compressor       compressor       compressor

                                                          Location                                                                                                   RER              RER                RER
                                                   InfrastructureProcess                                                                                              0                0                  0
                                                            Unit                                                                                                     m3               m3                 m3
product               compressed air, best generation, >30kW, 6 bar gauge, at compressor                   RER                         0              m3              1
product               compressed air, best generation, >30kW, 7 bar gauge, at compressor                   RER                         0              m3                                1
product               compressed air, best generation, >30kW, 8 bar gauge, at compressor                   RER                         0              m3                                                  1
                                                                                                                                                                                                                                                                        (1,4,1,1,1,5); manufacturer
technosphere          air compressor, screw-type compressor, 300 kW, at plant                              RER                         1              unit         8.10E-8           8.10E-8          8.10E-8                          1              3.06
                                                                                                                                                                                                                                                                        value
                                                                                                                                                                                                                                                                        (1,4,1,1,1,5); manufacturer
                      lubricating oil, at plant                                                            RER                         0              kg           2.08E-6           2.08E-6          2.08E-6                          1              1.24
                                                                                                                                                                                                                                                                        value
                                                                                                                                                                                                                                                                        (1,4,1,1,1,5); manufacturer
                      disposal, used mineral oil, 10% water, to hazardous waste incineration               CH                          0              kg           2.08E-6           2.08E-6          2.08E-6                          1              1.24
                                                                                                                                                                                                                                                                        value
                      electricity, low voltage, production UCTE, at grid                                   UCTE                        0              kWh          9.10E-2           9.74E-2          1.04E-1                          1              1.13              (1,3,2,1,1,4); average value

                                                                                                                                                                                                                                                                        (4,5,1,1,1,5); assuming
                                                                                                                                                                                                                                                                        100km lorry, 200km train for
                      transport, lorry >16t, fleet average                                                 RER                         0              tkm          3.73E-5           3.73E-5          3.73E-5                          1              2.14
                                                                                                                                                                                                                                                                        transport of compressor and
                                                                                                                                                                                                                                                                        lubricating oil

                                                                                                                                                                                                                                                                        (4,5,1,1,1,5); assuming
                                                                                                                                                                                                                                                                        100km lorry, 200km train for
                      transport, freight, rail                                                             RER                         0              tkm          7.46E-5           7.46E-5          7.46E-5                          1              2.14
                                                                                                                                                                                                                                                                        transport of compressor and
                                                                                                                                                                                                                                                                        lubricating oil

emission air, high
                      Heat, waste                                                                               -                       -             MJ           3.28E-1           3.51E-1          3.75E-1                          1              1.13              (1,3,2,1,1,4); from electricity
population density




Tab. 10.19: Unit process raw data of the datasets “compressed air, average installation, <30kW, at supply network ”
                                                                                                                                                                                                                                 StandardDeviation
                                                                                                            InfrastructureProc




                                                                                                                                                                                                               UncertaintyType




                                                                                                                                                      compressed air, compressed air, compressed air,
                                                                                                                                                          average          average          average
                                                                                                Location




                                                                                                                                                        installation,    installation,    installation,
                                                                                                                                                                                                                                       95%
                                                                                                                                      Unit
                                                                                                                    ess




                                                         Name                                                                                                                                                                                            GeneralComment
                                                                                                                                                       <30kW, 8 bar     <30kW, 10 bar <30kW, 12 bar
                                                                                                                                                      gauge, at supply gauge, at supply gauge, at supply
                                                                                                                                                          network          network          network
                                                       Location                                                                                                RER             RER              RER
                                                InfrastructureProcess                                                                                           0                0               0
                                                         Unit                                                                                                  m3               m3               m3
product          compressed air, average installation, <30kW, 8 bar gauge, at supply network    RER               0                 m3                          1
product          compressed air, average installation, <30kW, 10 bar gauge, at supply network   RER               0                 m3                                           1
product          compressed air, average installation, <30kW, 12 bar gauge, at supply network   RER               0                 m3                                                            1
                                                                                                                                                                                                                                                         (4,3,2,1,1,5); average value of one
technosphere     aluminium, production mix, at plant                                            RER               0                  kg                       3.35E-5         3.35E-5          3.35E-5             1              1.31
                                                                                                                                                                                                                                                         distribution network
                                                                                                                                                                                                                                                         (4,3,2,1,1,5); average value of one
                 section bar extrusion, aluminium                                               RER               0                  kg                       3.35E-5         3.35E-5          3.35E-5             1              1.31
                                                                                                                                                                                                                                                         distribution network
                                                                                                                                                                                                                                                         (4,5,1,1,1,5); assuming 100km lorry,
                 transport, lorry >16t, fleet average                                           RER               0                tkm                        3.35E-6         3.35E-6          3.35E-6             1              2.14                   200km train for transport of pipe
                                                                                                                                                                                                                                                         network
                                                                                                                                                                                                                                                         (4,5,1,1,1,5); assuming 100km lorry,
                 transport, freight, rail                                                       RER               0                tkm                        6.69E-6         6.69E-6          6.69E-6             1              2.14                   200km train for transport of pipe
                                                                                                                                                                                                                                                         network
                                                                                                                                                                                                                                                         (1,3,2,1,1,4); average value for
                 compressed air, average generation, <30kW, 8 bar gauge, at compressor          RER               0                 m3                        1.50E+0                                              1              1.13
                                                                                                                                                                                                                                                         Swiss and German installations
                                                                                                                                                                                                                                                         (1,3,2,1,1,4); average value for
                 compressed air, average generation, <30kW, 10 bar gauge, at compressor         RER               0                 m3                                        1.50E+0                              1              1.13
                                                                                                                                                                                                                                                         Swiss and German installations
                                                                                                                                                                                                                                                         (1,3,2,1,1,4); average value for
                 compressed air, average generation, <30kW, 12 bar gauge, at compressor         RER               0                 m3                                                         1.50E+0             1              1.13
                                                                                                                                                                                                                                                         Swiss and German installations




ecoinvent-report No. 23                                                                         - 82 -
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 m3.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
