You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Electronic components, washing machine, at plant` [CH], reference unit 1 p, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~7 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: private consumption / household devices
- includedProcesses: This process describes the passive elements and printed wiring boards and integrated circuits of a washing machine.
- technology: Electronic components for an actual washing machine for a household.
- generalComment: Thie process is based on measurements of the surface of printed wiring boards as well as on the quantity of integrated circuits and on the measurements and amount of passive elements.;
UUID: 01b38117-37b0-311d-8609-6f9286d87759
- source cited in the metadata: Hischier R. | 2007 | 2007 - LCI electric and electronic equipment - Hischier
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 p):
- none

## Report excerpt

Source file: `report-p194-196.txt` (SHA-256 86d4c1633ed4649f0c7b5bbe94086c452e36fa6dc3d37b88680a12c5639fc2d8), pages 194-196 of `2007 - LCI electric and electronic equipment - Hischier.pdf`.

```
11. Unspecified datasets for electronic components


Calculating the average from the three printed wiring boards in Tab. 11.1, results in a distribution for
the active components that is used here in order to establish this unspecified dataset (the used specific
datasets for the respective components are mentioned here as well) – shown in Tab. 11.4.

Tab. 11.4   Composition of the unspecified dataset for active components (data represent average composition of PWB
            from television, desktop computer and laptop computer)


                         Used dataset                                                      [%]
                         transistor, unspecified, at plant                                11.7%
                         integrated circuit, IC, logic type, at plant                     55.0%
                         integrated circuit, IC, memory type, at plant                    30.9%
                         diode, unspecified, at plant                                     2.0%
                         light emitting diode, LED, at plant                              0.4%




11.2.2 Data Uncertainty and Input Data for ecoinvent Database
The uncertainty scores established according to the method used in the ecoinvent project (see
Frischknecht et al. (2007)) include reliability, completeness, temporal correlation, geographical corre-
lation, further technological correlation and sample size. The dataset here represents a weighted aver-
age of various active components shown in this database – weighted on the basis of three different
types of printed wiring board. Nevertheless, the uncertainty values are rather high.
The resulting unit process “electronic component, active, unspecified, at plant” is shown in Tab. 11.6
(on page 184).


11.3        Dataset “electronic component, unspecified, at plant”
This dataset here represents an average composition of active and passive electronic components,
based on the composition of three different types of printed wiring board (see Tab. 11.1) for all those
cases, where these components are not further specified. The dataset has a functional unit of “1 kg of
components”.
The datasets represents an average composition of active and passive components as it can be found
on printed wiring boards in television devices, desktop computers and laptop computers. From the data
in Tab. 11.1 results a mixture of 67% passive and 33% active components – mixture that is used here
together with the two preceding datasets (for unspecific passive resp. active components).


11.3.1 Data Uncertainty and Input Data for ecoinvent Database
The uncertainty scores established according to the method used in the ecoinvent project (see
Frischknecht et al. (2007)) include reliability, completeness, temporal correlation, geographical corre-
lation, further technological correlation and sample size. The dataset here represents a weighted aver-
age of various components shown in this database – weighted on the basis of three different types of
printed wiring board. Nevertheless, the uncertainty values are rather high.
The resulting unit process “electronic component, unspecified, at plant” is shown in Tab. 11.7 (on
page 184).




ecoinvent report No. 18 / part I                           - 182 -
                                                                                                                  11. Unspecified datasets for electronic components



Tab. 11.5            Unit process inventory of the dataset “electronic component, passive, unspecified, at plant (GLO)”

                             General Flow information                                                                                                     Representation in ecoinvent                                                                   Uncertainty information
                                                                                                                                             Infra-
                             Proc ess                                                                                               Sub-               Loc a-       Modul name in                                                                               StDv       General
       Input                                                                                Output      Remarks   Category                   struc -                                                 Mean value          Unit         Sourc e           Ty pe
                              Name                                                                                               c ategory             tion             ec oinvent                                                                              95%       Comment
                                                                                                                                              ture

                                                                                                                                                                                                                                average of PC                          (5,3,2,1,5,5,3);
connector, PCI bus                                                                                                                                                                                                              mot herboard, lapt op                  calculat ed from
                         H                                                                                        elect ronics   component     No        GLO    connector, PCI bus, at plant               1.82E-01 kg                                    1     2.29
type                                                                                                                                                                                                                            mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                board                                  and TV mainboards
                                                                                                                                                                                                                                average of PC                          (5,3,2,1,5,5,3);
connector,                                                                                                                                                      connector, comput er,                                           mot herboard, lapt op                  calculat ed from
                         H                                                                                        elect ronics   component     No        GLO                                               1.03E-01 kg                                    1     2.29
peripherical t ype                                                                                                                                              peripherical t ype, at plant                                    mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                board                                  and TV mainboards
                                                                                                                                                                                                                                average of PC                          (5,3,2,1,5,5,3);
                                                                                                                                                                capacit or, Tantalum-, t hrough-                                mot herboard, lapt op                  calculat ed from
tant alum capacitor      H                                                                                        elect ronics   component     No        GLO                                              3.48E-02 kg                                     1     2.29
                                                                                                                                                                hole mount ing, at plant                                        mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                board                                  and TV mainboards
                                                                                                                                                                                                                                average of PC                          (5,3,2,1,5,5,3);
                                                                                                                                                                capacit or, elect rolyt e t ype, <                              mot herboard, lapt op                  calculat ed from
elect rolyt capacit or   H                                                                                        elect ronics   component     No        GLO                                               1.39E-01 kg                                    1     2.29
                                                                                                                                                                2cm height , at plant                                           mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                board                                  and TV mainboards
                                                                                                                                                                                                                                average of PC                          (5,3,2,1,5,5,3);
                                                                                                                                                                capacit or, SM D type, surface-                                 mot herboard, lapt op                  calculat ed from
SM D t ype capacitor     H                                                                                        elect ronics   component     No        GLO                                              4.38E-02 kg                                     1     2.29
                                                                                                                                                                mounting, at plant                                              mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                board                                  and TV mainboards
                                                                                                                                                                                                                                average of PC                          (5,3,2,1,5,5,3);
unspecif ied                                                                                                                                                    capacit or, unspecified, at                                     mot herboard, lapt op                  calculat ed from
                         H                                                                                        elect ronics   component     No        GLO                                               1.05E-01 kg                                    1     2.29
capacitor                                                                                                                                                       plant                                                           mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                board                                  and TV mainboards
                                                                                                                                                                                                                                average of PC                          (5,3,2,1,5,5,3);
                                                                                                                                                                inductor, ring core choke                                       mot herboard, lapt op                  calculat ed from
coils & induct ors       H                                                                                        elect ronics   component     No        GLO                                               3.36E-01 kg                                    1     2.29
                                                                                                                                                                t ype, at plant                                                 mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                board                                  and TV mainboards
                                                                                                                                                                                                                                average of PC                          (5,3,2,1,5,5,3);




                               electronic component, passive, unspecified, at plant
                                                                                                                                                                                                                                mot herboard, lapt op                  calculat ed from
resistor mix             H                                                                                        elect ronics   component     No        GLO    resistor, unspecified, at plant            5.67E-02 kg                                    1     2.29
                                                                                                                                                                                                                                mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                board                                  and TV mainboards
                                                                                          passive
                                                                                                                                                                elect ronic component,
                                                                                      H   component ,             elect ronics   component     No        GLO                                               1.00E+00 kg                                    1
                                                                                                                                                                passive, unspecified, at plant
                                                                                          unspecified




ecoinvent report No. 18 / part I                                                                                                               - 183 -
                                                                                                                                       11. Unspecified datasets for electronic components


Tab. 11.6          Unit process inventory of the dataset “electronic component, active, unspecified, at plant (GLO)”

                             General Flow information                                                                                                                          Representation in ecoinvent                                                                 Uncertainty information
                                                                                                                                                                  Infra-
                             Proc ess                                                                                                                    Sub-               Loc a-       Modul name in                                                                             StDv       General
       Input                                                                                                     Output      Remarks   Category                   struc -                                              Mean value           Unit         Sourc e           Ty pe
                                            Name                                                                                                      c ategory             tion             ec oinvent                                                                            95%       Comme nt
                                                                                                                                                                   ture

                                                                                                                                                                                                                                                   average of PC                          (5,3,2,1,5,5,3);
                                                                                                                                                                                     t ransist or, unspecified, at                                 mot herboard, lapt op                  calculat ed from
transistor mix        H                                                                                                                elect ronics   component     No        GLO                                             1.17E-01 kg                                    1     2.29
                                                                                                                                                                                     plant                                                         mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                                   board                                  and TV mainbo ards
                                                                                                                                                                                                                                                   average of PC                          (5,3,2,1,5,5,3);
                                                                                                                                                                                     int egrated circuit, IC, logic                                mot herboard, lapt op                  calculat ed from
IC, logic type        H                                                                                                                elect ronics   component     No        GLO                                            5.50E-01 kg                                     1     2.29
                                                                                                                                                                                     t ype, at plant                                               mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                                   board                                  and TV mainbo ards
                                                                                                                                                                                                                                                   average of PC                          (5,3,2,1,5,5,3);
                                                                                                                                                                                     int egrated circuit, IC, memory                               mot herboard, lapt op                  calculat ed from
IC, memory t ype      H                                                                                                                elect ronics   component     No        GLO                                            3.09E-01 kg                                     1     2.29
                                                                                                                                                                                     t ype, at plant                                               mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                                   board                                  and TV mainbo ards




                                                                                plant
                                                                                                                                                                                                                                                   average of PC                          (5,3,2,1,5,5,3);
                                                                                                                                                                                                                                                   mot herboard, lapt op                  calculat ed from
Diodes mix            H                                                                                                                elect ronics   component     No        GLO    diode, unspecif ied, at plant           1.96E-02 kg                                     1     2.29
                                                                                                                                                                                                                                                   mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                                   board                                  and TV mainbo ards
                                                                                                                                                                                                                                                   average of PC                          (5,3,2,1,5,5,3);
                                                                                                                                                                                     light emit ting diode, LED, at                                mot herboard, lapt op                  calculat ed from
LEDs                  H                                                                                                                elect ronics   component     No        GLO                                            3.75E-03 kg                                     1     2.29
                                                                                                                                                                                     plant                                                         mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                                   board                                  and TV mainbo ards
                                                                                                               act ive
                                                                                                                                                                                     elect ronic component, active,
                                                                                                               component ,             elect ronics   component     No        GLO                                            1.00E+00 kg                                     1




                                electronic component, active, unspecified, at
                                                                                                           H                                                                         unspecified, at plant
                                                                                                               unspecified




Tab. 11.7          Unit process inventory of the dataset “electronic component, unspecified, at plant (GLO)”

                             General Flow information                                                                                                                          Representation in ecoinvent                                                                 Uncertainty information
                                                                                                                                                                  Infra-
                             Proc ess                                                                                                                    Sub-               Loc a-       Modul name in                                                                             StDv       General
       Input                                                                                                     Output      Remarks   Category                   struc -                                              Mean value           Unit         Sourc e           Ty pe
                                            Name                                                                                                      c ategory             tion             ec oinvent                                                                            95%       Comment
                                                                                                                                                                   ture

                                                                                                                                                                                                                                                   average of PC                          (5,3,2,1,5,5,3);
                                                                                                                                                                                     elect ronic component,                                        mot herboard, lapt op                  calculat ed from
passive component     H                                                                                                                elect ronics   component     No        GLO                                            6.70E-01 kg                                     1     2.29
                                                                                                                                                                                     passive, unspecified, at plant                                mainboard and a TV                     Deskt op PC, Laptop
                                                                                                                                                                                                                                                   board                                  and TV mainboards
                                                                                                                                                                                                                                                   average of PC                          (5,3,2,1,5,5,3);
                                                                                                                                                                                     elect ronic component, active,                                mot herboard, lapt op                  calculat ed from
active component      H                                                                                                                elect ronics   component     No        GLO                                            3.30E-01 kg                                     1     2.29
                                                                                                                                                                                     unspecified, at plant                                         mainboard and a TV                     Deskt op PC, Laptop




                          electronic
                                                                   component,
                                                                                                                                                                                                                                                   board                                  and TV mainboards
                                                                                                               unspecified                                                           elect ronic component,
                                                                                                                                       elect ronics   component     No        GLO                                            1.00E+00 kg                                     1




                                                                                   unspecified, at plant
                                                                                                           H   component                                                             unspecified, at plant




ecoinvent report No. 18 / part I                                                                                                                                    - 184 -
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
