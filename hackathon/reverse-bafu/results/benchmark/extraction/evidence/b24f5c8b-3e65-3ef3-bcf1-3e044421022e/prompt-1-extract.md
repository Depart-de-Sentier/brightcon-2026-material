You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Nuclear spent fuel conditioning plant` [CN], reference unit 1 p, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~15 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: waste / nuclear waste\infrastructure
- includedProcesses: It includes land use, building, cranes and other mashines, concrete for shielding and its lining, transport of materials and mashines, and disposal of concrete for shielding. The disposal of the building is in the used module.
- technology: Estimation of current technologies
- generalComment: Datasets established on the basis of the modelling for CH. The assumed area and the volume of the building have been estimated from a preliminary aerial view of the CH design. Concrete for shielding and weight of machines are rough estimations. Used CN electricity mix and (coal) freight train transport. This dataset has been developed with the goal to serve a preliminary estimation of the Chinese nuclear chain for the Chinese electricity mix. Hence, it cannot be used for comparisons of conditioning among countries.;
UUID: b24f5c8b-3e65-3ef3-bcf1-3e044421022e
- source cited in the metadata: Dones R. | 2009 | 2009 - Nuclear energy - Dones
- time period: 1999-01-2002-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 p):
- none

## Report excerpt

Source file: `report-p404-406.txt` (SHA-256 e39f4fe4b083d8a997fcb7b230cae145b423f0b5c36d82e3101c67f177c51dfd), pages 404-406 of `2009 - Nuclear energy - Dones.pdf`.

```
16. Anhang, Nuclear Energy in China (ecoinvent v2.0)

Tab. 16.8 shows the dataset.

Tab. 16.8: Dataset “electricity, nuclear, at power plant pressure water reactor (CN)” in ecoinvent data v2.0.




                                                                                                                                          InfrastructureProcess




                                                                                                                                                                                                                  Standard Deviation




                                                                                                                                                                                                                                                                  General Comment
                                                                                                                                                                                           Uncertainty Type
                                                                                                                                                                           electricity,




                                                                                                                            SubCategory
                                                                                                    Category
                                                                              Location
                                                                                                                                                                           nuclear, at




                                                                                                                                                                                                                         95%
                                                                                                                                                                  Unit
                                        Name                                                                                                                              power plant
                                                                                                                                                                         pressure water
                                                                                                                                                                             reactor


                                       Location                                                                                                                               CN
                                InfrastructureProcess                                                                                                                          0
                                         Unit                                                                                                                                kWh
Water, salt, ocean                                                                       resource              in water                                           m3           5.75E-03                       1             1.3 own estimation
water, decarbonised, at plant                                                 RER        water supply          production                    0                    kg           2.68E+00                       1             1.2 own estimation
diesel, burned in diesel-electric generating set                              GLO        oil                   fuels                         0                    MJ           4.10E-04                       1             1.3 own estimation
lubricating oil, at plant                                                     RER        chemicals             organics                      0                    kg           1.80E-06                       1             1.3 own estimation
acetylene, at regional storehouse                                             CH         chemicals             organics                      0                    kg           3.99E-08                       1         1.25 own estimation
anionic resin, at plant                                                       CH         chemicals             organics                      0                    kg           7.13E-08                       1         1.15 own estimation
argon, liquid, at plant                                                       RER        chemicals             inorganics                    0                    kg           2.89E-05                       1             1.3 own estimation
boric acid, anhydrous, powder, at plant                                       RER        chemicals             inorganics                    0                    kg           7.13E-08                       1         1.15 own estimation on data from utility
bitumen, at refinery                                                          CH         oil                   fuels                         0                    kg           8.55E-07                       1             1.3 own estimation
carbon dioxide liquid, at plant                                               RER        chemicals             inorganics                    0                    kg           1.85E-07                       1             1.3 own estimation
cationic resin, at plant                                                      CH         chemicals             organics                      0                    kg           7.13E-08                       1         1.15 own estimation
cement, unspecified, at plant                                                 CH         construction materialsbinder                        0                    kg           1.02E-06                       1             1.3 own estimation
chemicals inorganic, at plant                                                 GLO        chemicals             inorganics                    0                    kg           2.59E-06                       1         1.25 own estimation
chemicals organic, at plant                                                   GLO        chemicals             organics                      0                    kg           1.53E-06                       1             1.2 own estimation
flat glass, coated, at plant                                                  RER        glass                 construction                  0                    kg           4.85E-06                       1             1.3 own estimation
hydrogen, liquid, at plant                                                    RER        chemicals             inorganics                    0                    kg           1.14E-05                       1             1.3 own estimation
nitrogen, liquid, at plant                                                    RER        chemicals             inorganics                    0                    kg           6.84E-05                       1             1.3 own estimation
oxygen, liquid, at plant                                                      RER        chemicals             inorganics                    0                    kg           1.85E-05                       1             1.3 own estimation
paper, woodfree, coated, at integrated mill                                   RER        paper & cardboard     graphic paper                 0                    kg           7.13E-07                       1             1.3 own estimation
sodium hypochlorite, 15% in H2O, at plant                                     RER        chemicals             inorganics                    0                    kg           1.91E-05                       1             1.3 own estimation
cast iron, at plant                                                           RER        metals                extraction                    0                    kg           1.43E-07                       1             1.2 extrapolation from another plant type
steel, low-alloyed, at plant                                                  RER        metals                extraction                    0                    kg           1.77E-06                       1             1.6 own assumption
reinforcing steel, at plant                                                   RER        metals                extraction                    0                    kg           5.21E-07                       1             1.3 own assumption
concrete, normal, at plant                                                    CH         construction materialsconcrete                      0                    m3           1.08E-08                       1             1.3 own estimation
transport, lorry >16t, fleet average                                          RER        transport systems     road                          0                    tkm          1.68E-05                       1               3 approx.)
transport, coal freight, rail                                                 CN         transport systems     train                         0                    tkm          7.94E-05                       1                    3                                  "
nuclear power plant, pressure water reactor 1000MW                            CN         nuclear power         power plants                  1                    unit         3.57E-12                       1          1.1 own estimation (1.05 for European datasets)
U enriched 3.8%, in fuel element for LWR, at nuclear fuel fabrication plant   CN         nuclear power         production                    0                     kg          2.95E-06                       1         1.15 estimated variation over lifetime
nuclear spent fuel, in conditioning, at plant                                 CN         nuclear power         waste treatment               0                    kg           2.95E-06                       1                    1
radioactive waste, in interim storage, for final repository LLW               CH         nuclear power         waste treatment               0                    m3           1.76E-09                       1             1.2 own estimation
radioactive waste, in interim storage conditioning                            CH         nuclear power         waste treatment               0                    m3           4.32E-11                       1             1.2 own estimation
radioactive waste, in final repository for nuclear waste LLW                  CH         nuclear power         waste treatment           0                        m3           3.15E-08                       1                    2 own estimation (1.4 assumed for European plants)
disposal, hazardous waste, 25% water, to hazardous waste incineration         CH         waste management      hazardous waste incineration
                                                                                                                                         0                        kg           1.08E-06                       1             1.3 own estimation
disposal, separator sludge, 90% water, to hazardous waste incineration        CH         waste management      hazardous waste incineration
                                                                                                                                         0                        kg           2.42E-06                       1             1.3 own estimation
disposal, used mineral oil, 10% water, to hazardous waste incineration        CH         waste management      hazardous waste incineration
                                                                                                                                         0                        kg           1.80E-06                       1             1.3 own estimation
Heat, waste                                                                              air                   low population density        0                    MJ           7.65E+00                       1         1.03 uncertainty on efficiency
                                                                                                                                                                                                                             own ass. after UNSCEAR (2000) data (1.4 for European plants,
Hydrogen-3, Tritium                                                                      air                   low population density
                                                                                                                                             0                    kBq           3.85E-01                      1            2 after uncertainty in reports for rad.releases)
Noble gases, radioactive, unspecified                                                    air                   low population density        0                    kBq          1.45E+00                       1                    2                                  "
Iodine-131                                                                               air                   low population density        0                    kBq          1.18E-05                       1                    2                                  "
Aerosols, radioactive, unspecified                                                       air                   low population density        0                    kBq          4.36E-07                       1                    2                                  "
Hydrogen-3, Tritium                                                                      water                 ocean                         0                    kBq          1.67E+00                       1                    2                                  "
Radioactive species, Nuclides, unspecified                                               water                 ocean                         0                    kBq          1.23E-03                       1                    2                                  "
electricity, nuclear, at power plant pressure water reactor                   CN         nuclear power         power plants                  0                    kWh                 1




16.7                        Conditioning
The differences from the original infrastructure and operation datasets with same names but CH
location are:
- “electricity, medium voltage, at grid (CN)” used instead of CH;
- Transport of “radioactive waste, in final repository for nuclear waste SF, HLW, and ILW” modelled
with 1000 km by train and 50 km by lorry; transport of steel as for other CN datasets described above.
Tab. 16.9 and Tab. 16.10 show the infrastructure and operation datasets.




ecoinvent-Bericht No. 6 - Teil VII                                                                                        - 378 -
                                                 16. Anhang, Nuclear Energy in China (ecoinvent v2.0)

Tab. 16.9: Dataset “nuclear spent fuel conditioning plant (CN)” in ecoinvent data v2.0.




                                                                                                                                                       InfrastructureProcess




                                                                                                                                                                                                                                                               Standard Deviation




                                                                                                                                                                                                                                                                                                       General Comment
                                                                                                                                                                                                                                        Uncertainty Type
                                                                                                                                 SubCategory
                                                                                                      Category
                                                                             Location
                                                                                                                                                                                               nuclear spent fuel




                                                                                                                                                                                                                                                                      95%
                                                                                                                                                                                        Unit
                                       Name
                                                                                                                                                                                               conditioning plant




                                      Location                                                                                                                                                                           CN
                               InfrastructureProcess                                                                                                                                                                      1
                                        Unit                                                                                                                                                                             unit
Transformation, from unknown                                                    resource              land                                                                             m2                                     22500                        1            2 own estimation
Transformation, to industrial area, built up                                    resource              land                                                                             m2                                  1.80E+04                        1            2 own estimation
Transformation, to industrial area, vegetation                                  resource              land                                                                             m2                                      4500                        1            2 own estimation
Transformation, from industrial area                                            resource              land                                                                             m2                                     22500                        1            2 own estimation
Transformation, to unknown                                                      resource              land                                                                             m2                                     22500                        1            2 own estimation
Occupation, industrial area, built up                                           resource              land                                                                             m2a                                 3.60E+05                        1          2.5 own estimation
Occupation, industrial area, vegetation                                         resource              land                                                                             m2a                                 9.00E+04                        1          2.5 own estimation
building, multi-storey                                                      RER construction processesbuildings                                          1                             m3                                  1.30E+05                        1            2 own assumption
industrial machine, heavy, unspecified, at plant                            RER construction processesmachinery                                           1                            kg                                  5.00E+04                        1            3 own assumption
chromium steel 18/8, at plant                                               RER metals                extraction                                         0                              kg                                     5000                        1            3 own assumption
concrete, normal, at plant                                                  CH construction materialsconcrete                                            0                             m3                                       250                        1            3 own assumption
transport, lorry >16t, fleet average                                        RER transport systems                                                        0                             tkm                                 3.93E+04                        1            3 own assumption
transport, coal freight, rail                                               CN transport systems      train                                              0                             tkm                                 5.57E+03                        1            3 own assumption
disposal, building, concrete, not reinforced, to final disposal             CH                                                                           0                             kg                                  6.00E+05                        1            3 own assumption
nuclear spent fuel conditioning plant                                       CN          nuclear power                   waste treatment                  1                             unit                                       1




Tab. 16.10:                     Dataset “nuclear spent fuel, in conditioning, at plant (CN)” in ecoinvent data v2.0.




                                                                                                                                                                                                 InfrastructureProcess




                                                                                                                                                                                                                                                                                                                         Standard Deviation
                                                                                                                                                                                                                                                                                    Uncertainty Type
                                                                                                                                                                         SubCategory
                                                                                                                      Category
                                                                                           Location




                                                                                                                                                                                                                                  nuclear spent fuel,




                                                                                                                                                                                                                                                                                                                                95%
                                                                                                                                                                                                                           Unit
                                           Name                                                                                                                                                                                   in conditioning, at
                                                                                                                                                                                                                                        plant




                                      Location                                                                                                                                                                                                  CN
                               InfrastructureProcess                                                                                                                                                                                             0
                                         Unit                                                                                                                                                                                                   kg
electricity, medium voltage, at grid                                                      CN            electricity                            supply mix                                          0                     kWh                      2.40E-03                                                1                   2
welding, arc, steel                                                                       RER                                                                                                      0                      m                       8.00E-03                                                1                   3
chromium steel 18/8, at plant                                                             RER           metals                                 extraction                                          0                      kg                          15.7                                                1                1.15
transport, lorry >16t, fleet average                                                      RER           transport systems                                                                          0                     tkm                     1.56E+00                                                 1                   3
transport, coal freight, rail                                                             CN            transport systems                      train                                               0                     tkm                     3.29E+01                                                 1                   3
nuclear spent fuel conditioning plant                                                     CN                                                                                                       1                     unit                     5.56E-07                                                1                   2
radioactive waste, in final repository for nuclear waste SF, HLW, and ILW                 CH            nuclear power                          waste treatment                                     0                      m3                      2.30E-03                                                1                1.15
nuclear spent fuel, in conditioning, at plant                                             CN            nuclear power                          waste treatment                                     0                      kg                             1




16.8               Outlook
Approximated specific CN datasets should be expanded in next versions of the database using Chinese
specific data beyond the application of electricity mix as in the current version.
Chinese data on emissions from all nuclear facilities based in China should be pursued (the current
modelling includes only radioactive emissions from power plants).
Specific conditions for uranium mining (mostly ISL), waste repositories, and eventually reprocessing
should be re-evaluated in future studies.




ecoinvent-Bericht No. 6 - Teil VII                                                           - 379 -
                               17. Anhang, Nuclear Energy in the USA (ecoinvent v2.0)


  17 Anhang, Nuclear Energy Chain in the USA
     (ecoinvent v2.0)
  17.1        Introduction
  The model of the US nuclear energy chain has been developed on the basis of the knowledge acquired
  by the model of the chain associated with the current (year 2000) Swiss and European nuclear power
  plants as in (Dones et al. 2004). Information gathered from US operators (USEC) or Regulators
  (Nuclear Regulatory Commission, NRC indirectly through (Harris and Miller 2007)) or official
  Organizations (Energy Information Administration, EIA, of the US Department of Energy, DOE) or
  leading journals (NEI 2007) have been used for the key inputs of important (in terms of contributions
  to cumulative results) stages. Stages of the nuclear chain that are relatively minor contributors on the
  basis of the results for the chain associated to European nuclear power plant as described in ecoinvent,
  or parts that can be assumed to be adequately modeled for US using the existing ecoinvent datasets are
  based entirely or on extrapolations of the modeling in (Dones et al. 2004).
  This chapter reports on the structure of the model developed, provides full information on the US
  specific datasets newly developed for ecoinvent data v2.0, but gives only key pieces of information for
  the other or the adapted datasets.
  Although the model used is believed to be sufficiently closely reflecting US conditions for nuclear
  energy in the first half of the 2000s, some features of a few stages of the chain have been
  approximated, thus not directly representing US-specific characteristics. This applies in particular to
  the final radioactive waste repository of Yucca Mountain that could not be modeled due to limited
  resources. Nevertheless, the very low contribution that final repository brings to cumulative results of
  the Swiss-specific chain is such that even a factor of two to ten difference in the energy and material
  specific uses (per kWh generated or kgHM of spent fuel stored) would not significantly change the
  cumulative results.116 Furthermore, the current, relatively high quota of In-Situ Leaching (ISL) mining
  world-wide is also not explicitly modelled (this applies to all currently developed nuclear modeling
  within ecoinvent). However, the energy uses for ISL are usually smaller than conventional mining
  (roughly one order of magnitude lower), the wastes to dispose on surface are much lower, and the
  emissions to groundwater presumably comparable to conventional mining/milling when very long-
  term emissions from mill tailings would be considered (not included in ecoinvent data v2.0). Anyhow,
  the results for some important indicators (e.g. greenhouse gas emissions) may be influenced more by
  uncertainties in key relevant factors or change in the market for specific services (e.g. enrichment, for
  the above mentioned indicator) rather than from changes in the adopted approximations. Finally,
  although the model presented hereinafter is believed to be sufficient to describe the main features of
  the US nuclear chain, further more region or site-specific assessment may add accuracy and reduce
  uncertainty to the cumulative results.


  17.2        US Uranium Products Market Data
  According to the Energy Information Administration of the U.S. Department of Energy (EIA of
  DOE),117 owners and operators of US civilian nuclear power reactors purchased a total of 66.539
  million pounds (30180 tonne) U3O8eq (uranium oxide equivalent) of deliveries from U.S. and foreign
  suppliers during 2006. The total includes deliveries of U3O8, natural UF6, and enriched uranium.118
  Approximately 16% of all uranium purchased was U.S.-origin. Foreign-origin uranium accounted for



116
            Additionally, see Section 12.5.4 in (Dones 2004) for the discussion on the reasons why the long-term emission of
  long-lived radionuclides to the geosphere and then biosphere have not been considered in the LCA accounting.
117
            http://www.eia.doe.gov/fuelnuclear.html
118
            http://www.eia.doe.gov/cneaf/nuclear/umar/table4.html

  ecoinvent-Bericht No. 6 - Teil VII                       - 380 -
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
