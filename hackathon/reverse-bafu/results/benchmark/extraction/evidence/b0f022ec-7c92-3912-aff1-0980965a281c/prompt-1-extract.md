You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Boric oxide, at plant` [GLO], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~12 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: chemicals / inorganic
- includedProcesses: Production of boric oxide including materials, energy uses, infrastructure and emissions.
- technology: Fusion of boric oxide
- generalComment: The process "boric oxide, at plant, GLO" is modelled for the production of  boric oxide from boric acid in the world.  Raw materials are modelled with a stoechiometric calculation, Energy consumptions and emissions are estimated. Infrastructure and transports are calculated with standard values.;
CAS number: 001303-86-2; 
Formula: B2O3; 
UUID: b0f022ec-7c92-3912-aff1-0980965a281c
- source cited in the metadata: Sutter J. | 2007 | 2007 - LCI highly pure chemicals - Sutter
- time period: 2000-01-2006-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Water To Cooling: 0.024 cubic meter (Resources Resources from water Renewable material resources from water)

## Report excerpt

Source file: `report-p45-48.txt` (SHA-256 7e50e64e49bc38a54c6b235cf45ca8d4d741b854023013ebcd84be78802c7cd3), pages 45-48 of `2007 - LCI highly pure chemicals - Sutter.pdf`.

```
Error! Style not defined.. Error! Style not defined.


form of boric acid and metal borates as fire retardants in cellulosic insulation and plastics; 4 % as
soluble borates in agriculture as a fertilizer to amend boron-deficient soils and as a herbicide at high
dosages; 10 % from borax decahydrate and sodium perborate for cleaning and bleaching of laundry
products; and 2 % as corrosion inhibitors in aqueous systems, especially automotive antifreeze.
In Western Europe about one-half of the B2O3 is used in the manufacture of glass-related products.
Sodium perborate accounts for about one-third of the total boron consumption as a bleach in high-
temperature laundry products.
In Japan 70 % of B2O3 consumption is used in glass-related products.


3.4        Production Technologies (Ullmanns 2004)
High-purity B2O3 (99 %) is made by fusing refined boric acid.
2 H3BO3 → B2O3 + 3 H2O
A 96 % grade of B2O3 is made commercially by fusing a mixture of sodium tetraborate plus sulfuric
acid at 800 °C. Two molten layers are formed, an upper layer of boric oxide and a lower layer of so-
dium sulfate. The molten B2O3 layer is separated and cooled on chill rollers. The resulting glass is
ground, sized, and packaged in moisture-proof containers. The product B2O3 contains 3 – 4 % sodium
sulfate.
Boric oxide can also be prepared by thermal decomposition of ammonium pentaborate,
NH4B5O8 · 4 H2O, at 500 – 900 °C and through direct reaction of boron with oxygen.


3.5        System Characterisation
In this study the fusing of boric acid is considered. The system includes the process with consumption
of raw materials, energy, infrastructure, and land use, as well as the generation of emissions to air and
water. It also includes transportation of the raw materials. For the study transient or unstable opera-
tions like starting-up or shutting-down, are not included, but the production during stable operation
conditions. Storage and transportation of the final product are also not included. It is assumed that the
manufacturing plants are located in an urban/industrial area and consequently the emissions are cate-
gorised as emanating in a high population density area. The emissions into water are assumed to be
emitted into rivers.


3.6        Raw materials and auxiliaries
As there was no data available for the production of boric oxide, the values for the consumption of the
raw materials are calculated with an assumed yield of 95 % (Frischknecht et al. 2007).
There was no information available on the amount of cooling water used within the plant. In order not
to neglect the process cooling water demand this value was approximated with data from an large
chemical plant site in Germany producing 2.05 Mt a-1 (intermediates included) of different chemicals
(Gendorf 2000). In this plant in total an average 24 kg water per kg of product were used for. This
value was used in this inventory as approximation for the cooling water consumption of the boric ox-
ide production.

Tab. 3.3   Consumption of raw materials and auxilliaries for the boric oxide production


                         Input                     Values       Remarks
                         Boric acid (kg)           1.86         Calculated with a yield of 95 %
                         Cooling water (kg)        24           Estimation




41LCI bioenergy report                                     - 41 -
                                    Error! Style not defined.. Error! Style not defined.


3.7          Energy
There was no information available on the amount of energy used for the production process. In order
not to neglect the process energy demand those values were approximated with data from an large
chemical plant site in Germany producing 2.05 Mt a-1 (intermediates included) of different chemicals
(Gendorf (2000)). The values for the energy consumption per kg of product of this plant (3.2 MJ kg-1)
were used as approximation for the energy consumption of boric oxide production. This total energy
demand contains a split of 50% natural gas, 38% electricity and 12% steam from external energy
sources. For this inventory all energy used for heat or steam was assumed to be natural gas. For this
inventory an amount of 2 MJ natural gas and 0.333 kW electricity per kg product was used. A sum-
mary of the values used is given in Tab. 3.4.

Tab. 3.4     Energy consumption for the boric oxide production


              Input                                                            per kg boric oxide
           Heat, natural gas burned in industrial furnace > 100 kW                       2
           Electricity (kWh)                                                             0.333


3.8          Transportation
No information is available in the sources consulted concerning transportation of raw materials or aux-
iliaries. Therefore, the following standard distances as defined in Frischknecht et al. (2007) are used:
100 km by lorry 32t and 600 km by train. Tab. 3.5 summarises the total transport amounts for the bo-
ric oxide production.

Tab. 3.5     Total transport amounts for the boric oxide production

                                            -1
                                   tkm kg boric oxide              lorry             train
                                  Total transports             1.86E-01       1.12


3.9          Infrastructure and land use
No information was readily available about infrastructure and land-use of boric oxide production
plants. Therefore, in this study, the infrastructure is estimated based on the module "chemical plant,
organics". This module assumes a built area of about 4.2 ha, an average output of 50'000 t/a, and plant
life of fifty years. For this study, the estimated value is 4.00 E-10 units per kg of produced chemical.


3.10         Emissions to air
It is assumed that 100% of the electricity consumed is converted to waste heat and that 100% of the
waste heat is released to the air.
There was no data available on process emissions to air for the boric oxide production. As approxima-
tion the air emissions occurring from the purge vent, the distillation vent and fugitive emission sources
were estimated to 0.2% of the input of boric acid. The boric acid is calculated as boron emission.

Tab. 3.6     Process emissions to air from the boric oxide production


                         Output                        Value        Remarks
                       Waste heat (MJ)             1.2              calculated from electricity input
                       Boron, to air (MJ)          6.62E-04         calculated as 0.2 % of the input




42LCI bioenergy report                                     - 42 -
                                  Error! Style not defined.. Error! Style not defined.




3.11       Emissions to water
The remaining amount of unreacted boric acid (4.8 % of the input) is assumed to leave the production
process with the waste water. The boric acid is calculated as boron emission.

Tab. 3.7   Process emissions to water from the boric oxide production


                         Output             Value           Remarks
                         Boron (kg)         1.59E-02        calculated from mass balance


3.12       Life cycle inventory of boric oxide production and data
           quality considerations
Tab. 3.8 shows the life cycle inventory and the data quality indicators for the boric oxide production.
The simplified approach with a pedigree matrix has been used for calculating the standard deviation.




43LCI bioenergy report                                   - 43 -
                                                                                      Error! Style not defined.. Error! Style not defined.



Tab. 3.8   Unit process raw data for the boric oxide production




                                                                                                             Infrastructur




                                                                                                                                                                    StandardDe
                                     OutputGrou




                                                                                                                                                      Uncertainty
                        InputGroup




                                                                                                                                                                    viation95%
                                                                                                               eProcess
                                                                                                  Location
                                                                                                                                    boric oxide, at




                                                                                                                                                        Type
                                                                                                                             Unit
                  401                                                Name                                                                                                        GeneralComment

                                         p
                                                                                                                                         plant

                  662                                                Location                                                           GLO
                  493                                         InfrastructureProcess                                                      0
                  403                                                   Unit                                                             kg
                           -             0        boric oxide, at plant                          GLO              0          kg       1.00E+0
resource, in
                          4              -        Water, cooling, unspecified natural origin         -            -          m3        2.40E-2            1          1.30 (4,5,na,na,na,na); Estimation
water
                          5              -        boric acid, anhydrous, powder, at plant        RER              0          kg       1.86E+0             1          1.38 (4,5,1,1,1,5); Stoichiometric calculation
                                                  heat, natural gas, at industrial furnace
                          5              -                                                       RER              0          MJ       2.00E+0             1          1.30 (4,5,na,na,na,na); Estimation
                                                  >100kW
                                                  electricity, medium voltage, production
                          5              -                                                      UCTE              0          kWh       3.33E-1            1          1.30 (4,5,na,na,na,na); Estimation
                                                  UCTE, at grid
                          5              -        transport, lorry >16t, fleet average           RER              0          tkm       1.86E-1            1          2.09 (4,5,na,na,na,na); Standard distances
                          5              -        transport, freight, rail                       RER              0          tkm      1.12E+0             1          2.09 (4,5,na,na,na,na); Standard distances
                          5              -        chemical plant, organics                       RER              1          unit     4.00E-10            1          3.09 (4,5,na,na,na,na); Estimation
emission air,
high population            -            4         Heat, waste                                        -            -          MJ       1.20E+0             1          1.30 (4,5,na,na,na,na); Calculated from the electricity input
density
                           -            4         Boron                                              -            -          kg        6.62E-4            1          5.10 (4,5,na,na,na,na); Estimation
emission water,
                           -            4         Boron                                              -            -          kg        1.59E-2            1          5.10 (4,5,na,na,na,na); Stoichiometric calculation
river




LCI bioenergy report                                                       - 44 -
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
