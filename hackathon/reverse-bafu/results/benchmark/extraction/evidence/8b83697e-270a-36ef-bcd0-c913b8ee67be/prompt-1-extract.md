You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Electricity, hydropower, net, at reservoir power plant` [CH], reference unit 1 kWh, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~21 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: electricity by fuel / hydro\reservoir
- includedProcesses: Operation of an average, certified storage hydropower station in Switzerland. It includes the area transformed and occupied, the volume of the reservoir, greenhouse gas emissions, the consumption of lubricant oil and the amount of turbined water. Not considered is the electricity used for the pumps.
- technology: Average installed technology. Efficiency 0.78. Annual production volume: 190GWh/a
- generalComment: A representative sample of Swiss storage hydropower stations with a dam higher than 30 meters is taken into account for calculating the input. Data are the same for reservoir and pumped storage power plants, the impacts of the area used, the amount of turbined water and the greenhouse gas emissions are shared. The lifetime is assumed to be 150 years for the dams and 80 years for the other material. The data describe a mix and can therefore not be used  for an individual storage hydropower station. This dataset is recalculated based on Frischknecht et al. (1996) and Bauer (2007), complemented with data from Vattenfall (2008) and Diem et al. (2008).;
UUID: 8b83697e-270a-36ef-bcd0-c913b8ee67be
- source cited in the metadata: Flury K. | 2012 | 2012 - LCI hydroelectric power generation - Flury
- time period: 1945-01-2008-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kWh):
- Energy, Potential (in Hydropower Reservoir), Converted: 3.79 megajoule (natural resource)
- Water to turbine: 1.404 cubic meter (Resources Resources from water Renewable material resources from water)

## Report excerpt

Source file: `report-p37-38.txt` (SHA-256 9cef332a3a1e62584bae99280cdade13b1fb181426b6c54bc1b3d879066f1a24), pages 37-38 of `2012 - LCI hydroelectric power generation - Flury.pdf`.

```
4. Operation of the hydroelectric power stations


4.5      Data quality
The operation of the storage hydropower stations is described well. Data describing the oil
spill and the SF6 emissions are derived from power stations not included in the sample under
study. It is assumed though that the technology is the same and that the geographic differ-
ences are not significant. The greenhouse gas emissions are based on a study done on a signif-
icant share of the sample investigated. The geographic and technological correlation is good.
The quantification of the land use and the volume of the reservoirs are based on current data.
They do not only cover the same geography, the same technology and the same temporal as-
pects but the information is also available for the whole set of storage power stations under
study. In general, the operation of the storage hydropower stations is described well and with
low uncertainties.
The data of the operation of the run-of-river hydropower station on the other hand have more
uncertainties. The factors for the land use of the stations without reservoir were adopted from
earlier studies (Frischknecht et al. 1996) as no other data are available. This is also the case
for the amount of turbined water and the volume of the water bodies. The methane emissions
are based on one recent study conducted on one large run-of-river power station. This power
station is part of the sample of this study but the emission factor might differ from the emis-
sions of other run-of-river power stations. This leads to a relatively high uncertainty. In gen-
eral, the operation of the run-of-river hydropower stations is described well. Further meas-
urements of greenhouse gas emissions from reservoirs of run-of-river hydropower stations are
needed (and currently on-going).
No information is available about the operation of small hydropower stations. This part of the
life cycle is not well described.




Life Cycle Inventories of Hydroelectric Power Generation   - 31 -                 ESU-services Ltd.
                                                 4. Operation of the hydroelectric power stations


4.6          Life Cycle inventories of the operation of hydropower plants
Tab. 4.1:                    Unit process raw data of electricity, hydropower, at reservoir power plant/CH and
                             electricity, hydropower, net, at reservoir power plant/CH.




                                                                                                                               StandardDeviation95%
                                                                                                             UncertaintyType
                                                                                              electricity,
                                                                             electricity,




                                                          Location
                                                                                             hydropower,
                                                                            hydropower,




                                                                     Unit
                                    Name                                                        net, at                                               GeneralComment
                                                                            at reservoir
                                                                                               reservoir
                                                                            power plant
                                                                                             power plant



                                   Location                                     CH               CH
                           InfrastructureProcess                                 0                0
                                      Unit                                      kWh              kWh
                     electricity, hydropower, at
product                                                   CH         kWh         1
                     reservoir power plant
                     electricity, hydropower, net, at
                                                          CH         kWh                          1
                     reservoir power plant
                                                                                                                                                      (4,1,1,1,1,2,BU:3); Infrastructure of the storage power
technosphere         reservoir hydropower plant           CH         unit    3.35E-11         3.35E-11           1             3.05
                                                                                                                                                      station producing the electricity

                     sulphur hexafluoride, liquid, at                                                                                                 (4,5,1,5,1,5,BU:1.05); In electric insulation (e.g.
                                                          RER        kg      3.40E-10         3.40E-10           1             1.40
                     plant                                                                                                                            switches); based on Vattenfall (2008)

                                                                                                                                                      (4,5,1,5,1,5,BU:1.05); Turbines; based on Vattenfall
                     lubricating oil, at plant            RER        kg       3.24E-8          3.24E-8           1             1.40
                                                                                                                                                      (2008)

                                                                                                                                                      (3,1,1,1,1,2,BU:1.05); Electricity consumption for the
                     electricity, high voltage, at grid   CH         kWh      4.40E-2                            1             1.12
                                                                                                                                                      pumps (excl. pumped storage)

                                                                                                                                                      (3,1,1,1,1,1,BU:2); Original area before the construction
                                                                                                                                                      of the power station; recalculated based on
resource, land       Transformation, from unknown           -        m2       2.44E-5          2.44E-5           1             2.01
                                                                                                                                                      Frischknecht et al. (1996) and Schweizerisches
                                                                                                                                                      Talsperrenkomitee (2011)

                                                                                                                                    (3,1,1,1,1,1,BU:2); Area covered by the reservoir;
                     Transformation, to water bodies,
                                                            -        m2       2.41E-5          2.41E-5           1             2.01 recalculated based on Frischknecht et al. (1996) and
                     artificial
                                                                                                                                    Schweizerisches Talsperrenkomitee (2011)

                                                                                                                                                      (4,1,1,1,1,1,BU:2); Area covered by infrastructures other
                     Transformation, to industrial                                                                                                    than held-back river; recalculated based on
                                                            -        m2       2.41E-7          2.41E-7           1             2.05
                     area, built up                                                                                                                   Frischknecht et al. (1996) and Schweizerisches
                                                                                                                                                      Talsperrenkomitee (2011)

                                                                                                                                    (3,1,1,1,1,1,BU:1.5); Area occupied by the reservoir;
                     Occupation, water bodies,
                                                            -        m2a      3.62E-3          3.62E-3           1             1.52 recalculated based on Frischknecht et al. (1996) and
                     artificial
                                                                                                                                    Schweizerisches Talsperrenkomitee (2011)

                                                                                                                                                      (4,1,1,1,1,1,BU:1.5); Area occupied by the
                     Occupation, industrial area, built                                                                                               infrastructure; recalculated based on Frischknecht et
                                                            -        m2a      3.62E-5          3.62E-5           1             1.56
                     up                                                                                                                               al. (1996) and Schweizerisches Talsperrenkomitee
                                                                                                                                                      (2011)

                                                                                                                                    (3,1,1,1,1,1,BU:1.05); Volume occupied by the
resource, in water   Volume occupied, reservoir             -        m3a      1.64E-1          1.64E-1           1             1.11 reservoir; based on Schweizerisches
                                                                                                                                    Talsperrenkomitee (2011)

                     Water, turbine use, unspecified                                                                                                  (3,1,1,1,1,1,BU:1.05); Amount of water turbined for the
                                                            -        m3       1.40E+0          1.40E+0           1             1.11
                     natural origin                                                                                                                   generation of electricity; based on BWW (1973)

                     Energy, potential (in hydropower
                                                            -        MJ       3.79E+0          3.79E+0           1             1.11 (3,1,1,1,1,1,BU:1.05); Potential energy of the water
                     reservoir), converted

                                                                                                                                    (4,3,2,3,1,4,BU:1.5); Nitrous oxide emissions due to
emission air, low
                   Dinitrogen monoxide                      -        kg       2.56E-8          2.56E-8           1             1.58 the biomass in the reservoirs; calculated based on
population density
                                                                                                                                    Diem et al. (2008)

                                                                                                                                    (4,3,2,3,1,3,BU:1.5); Methane emissions due to the
                     Methane, biogenic                      -        kg       2.64E-7          2.64E-7           1             1.57 biomass in the reservoirs; calculated based on Diem
                                                                                                                                    et al. (2008)

                                                                                                                                    (4,3,2,3,1,3,BU:1.4); Carbon dioxide emissions due to
                     Carbon dioxide, land
                                                            -        kg       1.36E-3          1.36E-3           1             1.48 the biomass in the reservoirs; calculated based on
                     transformation
                                                                                                                                    Diem et al. (2008)

                                                                                                                                                      (4,5,1,5,1,5,BU:1.5); From electric insulations (e.g.
                     Sulfur hexafluoride                    -        kg      3.40E-10         3.40E-10           1             1.69
                                                                                                                                                      switches); based on Vattenfall (2008)

                     Heat, waste                            -        MJ       1.58E-1          1.58E-1           1             1.12 (3,1,1,1,1,2,BU:1.05); Waste heat

emission air,                                                                                                                                         (4,3,3,2,4,5,BU:1.5); Water evaporated from reservoir;
                     Water, CH                              -        kg       1.75E+0          1.75E+0           1             1.89
unspecified                                                                                                                                           calculated based on Spreafico & Weingartner (2005)

emission water,                                                                                                                                       (4,5,1,5,1,5,BU:1.5); From turbines; based on Vattenfall
                     Oils, unspecified                      -        kg       2.27E-8          2.27E-8           1             1.69
river                                                                                                                                                 (2008)

emission soil,                                                                                                                                        (4,5,1,5,1,5,BU:1.5); From turbines; based on Vattenfall
                     Oils, unspecified                      -        kg       9.76E-9          9.76E-9           1             1.69
industrial                                                                                                                                            (2008)




Life Cycle Inventories of Hydroelectric Power Generation                                    - 32 -                                                                                                ESU-services Ltd.
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 kWh.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
