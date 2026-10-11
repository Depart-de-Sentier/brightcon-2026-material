You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Sweet sorghum stem, at farm` [CN], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~55 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: agricultural / plant production
- includedProcesses: Cultivation of sweet sorghum in China including use of diesel, machines, fertilizers, and pesticides.
- technology: High yield production.
- generalComment: The multioutput-process "sweet sorghum, CN"  delivers the co-products sorghum grains and sorghum stem. The functional unit is 1 ha cultivated with sweet sorghum. Yield: 1. 3860 kg sorghum grains/ha (fresh mass with a water content of 9.1 %, carbon content: 0.369 kg/kg fresh mass, biomass energy content: 14.27 MJ/kg fresh mass). 2. 48263 kg stems/ha (fresh mass with a water content of 73 %, carbon content: 0.115 kg/kg fresh mass, biomass energy content: 4.54 MJ/kg fresh mass). The emissions of N2O and NH3 to air are calculated with standard factors for mineral fertilizers from Nemecek et al. 2004. The emission of nitrate to water is calculated with a nitrogen loss factor of 32%. The allocation is based on economic criteria (prices: 1.4 yuan/kg sorghum grains, 0.15 yuan/kg sorghum stems).;
UUID: a9df4097-3687-35ca-8550-e42a8624df71
- source cited in the metadata: Jungbluth N. | 2007 | 2007 - LCI bioenergy - Jungbluth
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Energy, gross calorific value, in biomass: 4.536 megajoule (resources biotic)
- carbon dioxide (biogenic): 0.4217 kilogram (Resources Resources from air Renewable material resources from air)

## Report excerpt

Source file: `report-p198-200.txt` (SHA-256 162d005ae458a7359eb7cddc648ab9b921a262c45ea716c6f8aa12b9e39c8136), pages 198-200 of `2007 - LCI bioenergy - Jungbluth.pdf`.

```
11. Sweet Sorghum, production in China



Tab. 11.19 Allocation factors for the co-products from sorghum cultivation


                   Inputs/Outputs                                    Grains         Stems
                   Inputs
                   all fertilizers                                           42.7      57.3
                   all pesticides                                            42.7      57.3
                   all machine usages                                        42.7      57.3
                   all transports                                            42.7      57.3
                   land use                                                  42.7      57.3
                   CO2, biogenic                                             20.4      79.6
                   Energy, biomass                                           20.1      79.9

                   Outputs
                   Emissions to air                                          42.7      57.3
                   Emissions to water                                        42.7      57.3
                   Emissions to agricultural soil                            42.7      57.3


1.8        Life cycle inventory of sorghum cultivation and data quality
           considerations
Tab. 11.20 shows the life cycle inventory and the data quality indicators for the cultivation of sweet
sorghum. The simplified approach with a pedigree matrix has been used for calculating the standard
deviation.




ecoinvent-report No. 17                                 - 170 -
                                                                                    11. Sweet Sorghum, production in China



Tab. 11.20 Unit process raw data of the cultivation of sweet sorghum




                                                                                                                                           Uncertainty
                                                                                                          Infrastructu
                              InputGroup




                                                                                                                                                         StandardD
                                           OutputGro




                                                                                                                                                         eviation95
                                                                                                           reProcess
                                                                                               Location
                                                                                                                                 sweet




                                                                                                                                             Type
                                                                                                                         Unit
                        401                                            Name                                                                                           GeneralComment




                                                                                                                                                             %
                                                                                                                                sorghum

                        662                                     Location                                                           CN
                        493                              InfrastructureProcess                                                      0
                        403                                       Unit                                                             ha
    allocated                    -           2 sweet sorghum grains, at farm                   CN             0          kg     3.87E+3
    products                     -           2 sweet sorghum stem, at farm                     CN             0          kg     4.83E+4
                                                                                                                                                                      (4,3,1,1,1,4); calculated from the carbon
    resource, in air            4             - Carbon dioxide, in air                           -             -         kg     2.56E+4        1           1.24
                                                                                                                                                                      balance
                                                                                                                                                                      (4,3,1,1,1,4); calculated from the energy
    resource, biotic            4             - Energy, gross calorific value, in biomass        -             -         MJ     2.74E+5        1           1.24
                                                                                                                                                                      balance
    technosphere                5             - urea, as N, at regional storehouse             RER            0          kg     4.00E+1        1           1.11       (3,1,1,1,1,1); IFA 2006
                                                ammonium nitrate, as N, at regional
                                5             -                                                RER            0          kg     4.00E+1        1           1.11       (3,1,1,1,1,1); IFA 2006
                                                storehouse
                                                diammonium phosphate, as P2O5, at
                                5             -                                                RER            0          kg     5.00E+1        1           1.11       (3,1,1,1,1,1); IFA 2006
                                                regional storehouse
                                                potassium chloride, as K2O, at regional
                                5             -                                                RER            0          kg     5.00E+1        1           1.11       (3,1,1,1,1,1); IFA 2006
                                                storehouse
                                                lime, from carbonation, at regional
                                5             -                                                CH             0          kg     3.00E+2        1           1.11       (3,1,1,1,1,1); IFA 2006
                                                storehouse
                                5             - irrigating                                     CH             0          ha     1.25E+0        1           1.14       (3,3,2,1,1,3); Smith 2000
                                5             - 2,4-D, at regional storehouse                  RER            0          kg     7.45E-2        1           1.07       (1,1,1,3,1,3); USDA 2004
                                5             - alachlor, at regional storehouse               RER            0          kg     2.76E-1        1           1.07       (1,1,1,3,1,3); USDA 2004
                                5             - atrazine, at regional storehouse               RER            0          kg     8.16E-1        1           1.07       (1,1,1,3,1,3); USDA 2004
                                5             - dicamba, at regional storehouse                RER            0          kg     1.26E-2        1           1.07       (1,1,1,3,1,3); USDA 2004
                                                acetamide-anillide-compounds, at regional
                                5             -                                                RER            0          kg     7.61E-2        1           1.07       (1,1,1,3,1,3); USDA 2004
                                                storehouse
                                5             - glyphosate, at regional storehouse             RER            0          kg     2.45E-1        1           1.07       (1,1,1,3,1,3); USDA 2004
                                5             - metolachlor, at regional storehouse            RER            0          kg     3.64E-1        1           1.07       (1,1,1,3,1,3); USDA 2004
                                                [sulfonyl]urea-compounds, at regional
                                5             -                                                RER            0          kg     1.51E-3        1           1.07       (1,1,1,3,1,3); USDA 2004
                                                storehouse
                                                organophosphorus-compounds, at regional
                                5             -                                                RER            0          kg     2.91E-2        1           1.07       (1,1,1,3,1,3); USDA 2004
                                                storehouse
                                5             - fertilising, by broadcaster                    CH             0          ha     3.33E-1        1           1.22       (1,1,4,1,1,3); FAO 2002
                                5             - tillage, ploughing                             CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002
                                5             - tillage, harrowing, by spring tine harrow      CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002
                                5             - tillage, currying, by weeder                   CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002
                                5             - sowing                                         CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002
                                                application of plant protection products, by
                                5             -                                                CH             0          ha     3.33E-1        1           1.22       (1,1,4,1,1,3); FAO 2002
                                                field sprayer
                                5             - combine harvesting                             CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002
                                5             - tillage, cultivating, chiselling               CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002

                                5             - transport, tractor and trailer                 CH             0          tkm    4.30E+1        1           2.09       (4,5,na,na,na,na); Standard Distances


                                5             - transport, lorry 28t                           CH             0          tkm    3.00E+1        1           2.09       (4,5,na,na,na,na); Standard Distances


                                5             - transport, lorry 32t                           RER            0          tkm    2.23E+2        1           2.09       (4,5,na,na,na,na); Standard Distances


                                5             - transport, freight, rail                       RER            0          tkm    2.68E+2        1           2.09       (4,5,na,na,na,na); Standard Distances


                                5             - transport, barge                               RER            0          tkm    7.86E+2        1           2.09       (4,5,na,na,na,na); Standard Distances

    resources                   4             - Transformation, from arable                      -             -         m2     1.00E+4        1           2.05       (1,3,4,3,1,1); FAOSTAT 2006, FAO 1994
                                4             - Transformation, to arable                        -             -         m2     1.00E+4        1           2.05       (1,3,4,3,1,1); FAOSTAT 2006, FAO 1994
                                4             - Occupation, arable                               -             -         m2a    5.83E+3        1           1.56       (1,3,4,3,1,1); FAOSTAT 2006, FAO 1994
    emission air,
                                                                                                                                                                      (4,3,1,3,1,4); Calculated with standard
    low population               -           4 Ammonia                                            -            -         kg     6.80E+0        1           1.32
                                                                                                                                                                      method
    density
                                                                                                                                                                      (4,3,1,3,1,4); Calculated with standard
                                 -           4 Dinitrogen monoxide                                -            -         kg     3.83E+0        1           1.58
                                                                                                                                                                      method
                                                                                                                                                                      (4,3,1,3,1,4); Calculated with standard
                                 -           4 Nitrogen oxides                                    -            -         kg     8.05E-1        1           1.58
                                                                                                                                                                      method
    emission water,                                                                                                                                                   (4,3,1,3,1,4); Calculated with standard
                                 -           4 Phosphorus                                         -            -         kg     9.07E-1        1           1.58
    river                                                                                                                                                             method
    emission water,                                                                                                                                                   (4,3,1,3,1,4); Calculated with standard
                                 -           4 Phosphorus                                         -            -         kg     7.00E-2        1           1.58
    ground                                                                                                                                                            method
                                 -           4 Nitrate                                            -            -         kg     1.13E+2        1           1.58       (4,3,1,1,1,4); Estimation
    emission                                                                                                                                                          (4,3,1,1,1,4); Calculated from the fertilizer
                                 -           4 Cadmium                                            -            -         kg     -1.83E-3       1           1.58
    agricultural soil                                                                                                                                                 input
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the fertilizer
                                 -           4 Copper                                             -            -         kg     -8.29E-2       1           1.58
                                                                                                                                                                      input
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the fertilizer
                                 -           4 Lead                                               -            -         kg     -4.00E-2       1           1.58
                                                                                                                                                                      input
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the fertilizer
                                 -           4 Zinc                                               -            -         kg     -9.60E-2       1           1.58
                                                                                                                                                                      input
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the pesticide
                                 -           4 2,4-D                                              -            -         kg     7.45E-2        1           1.32
                                                                                                                                                                      application
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the pesticide
                                 -           4 Alachlor                                           -            -         kg     2.76E-1        1           1.32
                                                                                                                                                                      application
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the pesticide
                                 -           4 Atrazine                                           -            -         kg     8.16E-1        1           1.32
                                                                                                                                                                      application
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the pesticide
                                 -           4 Dicamba                                            -            -         kg     1.26E-2        1           1.32
                                                                                                                                                                      application
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the pesticide
                                 -           4 Dimethenamid                                       -            -         kg     7.61E-2        1           1.32
                                                                                                                                                                      application
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the pesticide
                                 -           4 Glyphosate                                         -            -         kg     2.45E-1        1           1.32
                                                                                                                                                                      application
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the pesticide
                                 -           4 Metolachlor                                        -            -         kg     3.64E-1        1           1.32
                                                                                                                                                                      application
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the pesticide
                                 -           4 Metsulfuron-methyl                                 -            -         kg     1.68E-4        1           1.32
                                                                                                                                                                      application
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the pesticide
                                 -           4 Prosulfuron                                        -            -         kg     1.35E-3        1           1.32
                                                                                                                                                                      application
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the pesticide
                                 -           4 Chlorpyrifos                                       -            -         kg     8.07E-3        1           1.32
                                                                                                                                                                      application
                                                                                                                                                                      (4,3,1,1,1,4); Calculated from the pesticide
                                 -           4 Terbufos                                           -            -         kg     2.11E-2        1           1.32
                                                                                                                                                                      application




ecoinvent-report No. 17                                                                                                    - 171 -
                                                   11. Sweet Sorghum, production in China



11.12 Cumulative Results and Interpretation
1.8.1      Introduction
Selected LCI results and values for the cumulative energy demand are presented and discussed in this
chapter. Please note that only a small part of the about 1'000 elementary flows is presented here. The
selection of the elementary flows shown in the tables is not based on their environmental relevance. It
rather allows to show by examples the contributions of the different life cycle phases, or specific in-
puts from the technosphere to the selected elementary flows. Please refer to the ecoinvent database for
the complete LCIs.
The shown selection is not suited for a life cycle assessment of the analysed processes and products.
Please use the data downloaded from the database for your own calculations, also because of possible
minor deviations between the presented results and the database due to corrections and changes in
background data used as inputs in the dataset of interest.
The ecoinvent database also contains life cycle impact assessment results. Assumptions and interpre-
tations were necessary to match current LCIA methods with the ecoinvent inventory results. They are
described in Frischknecht et al .(2004). It is strongly advised to read the respective chapters of the im-
plementation report before applying LCIA results.


1.8.2      Cultivation of sweet sorghum
Tab. 11.21 shows selected LCI results and the cumulative energy demand for the cultivation of sweet
sorghum.

Tab. 11.21 Selected LCI results and the cumulative energy demand of the cultivation of sweet sorghum




                                                                                                                sweet
                                                                                                                                sweet
                                                                                                              sorghum
                                                                  Name                                                         sorghum
                                                                                                              grains, at
                                                                                                                             stem, at farm
                                                                                                                farm


                                                                  Location                                       CN              CN
                                                                  Unit                                 Unit      kg              kg
                                                                  Infrastructure                                  0               0
               LCIA results
                                                                  non-renewable energy resources,
                              cumulative energy demand                                                MJ-Eq            2.2            0.2
                                                                  fossil
                                                                  non-renewable energy resources,
                              cumulative energy demand                                                MJ-Eq            1.0            0.1
                                                                  nuclear
                              cumulative energy demand            renewable energy resources, water   MJ-Eq            0.3            0.0
                                                                  renewable energy resources, wind,
                              cumulative energy demand                                                MJ-Eq            0.0            0.0
                                                                  solar, geothermal
                                                                  renewable energy resources,
                              cumulative energy demand                                                MJ-Eq           14.3            4.5
                                                                  biomass
               LCI results
               resource     Land occupation                       total                               m2a      6.6E-1          7.1E-2
               air          Carbon dioxide, fossil                total                               kg       1.3E-1          1.4E-2
               air          NMVOC                                 total                               kg       1.8E-4          1.9E-5
               air          Nitrogen oxides                       total                               kg       9.1E-4          9.7E-5
               air          Sulphur dioxide                       total                               kg       4.5E-4          4.8E-5
               air          Particulates, < 2.5 um                total                               kg       9.4E-5          1.0E-5
               air          Dinitrogen monoxide                   total                               kg       5.1E-4          5.5E-5
               air          Methane, fossil                       total                               kg       2.4E-4          2.6E-5
               water        BOD                                   total                               kg       3.6E-4          3.8E-5
               soil         Cadmium                               total                               kg       -2.0E-7         -2.2E-8
               water        Phosphorus                            total                               kg       7.7E-6          8.3E-7
               water        Nitrate                               total                               kg       1.3E-2          1.3E-3
               Further LCI results
               air          Carbon dioxide, biogenic              total                                kg     -1.4E+0          -4.2E-1
               air          Carbon dioxide, land transformation   low population density               kg      1.4E-5          1.5E-6
               air          Methane, biogenic                     total                                kg      1.1E-6          1.2E-7
               air          Carbon monoxide, biogenic             total                                kg      8.5E-6          9.1E-7




Tab. 11.22 shows values for CED, non-renewable, for the two datasets and values, which have been
found in literature. The differences are due to the lower machine usage and the lower fertilizer use,
which has been considered in dos Santos 1997.

ecoinvent-report No. 17                                                   - 172 -
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
