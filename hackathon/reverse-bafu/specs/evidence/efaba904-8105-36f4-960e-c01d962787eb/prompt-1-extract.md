You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Particle board, cement bonded, at plant` [RER], reference unit 1 m3, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~1302 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: wood / products
- includedProcesses: Includes the inputs to the production processes and transports of those inputs. No process emission data are available. ; Geography: Data for Switzerland used for central Europe
- technology: Medium enterprise technology (2000)
- generalComment: na;
UUID: efaba904-8105-36f4-960e-c01d962787eb
- source cited in the metadata: Werner F. | 2007 | 2007 - LCI wood as fuel and const. mat. - Werner
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 m3):
- Energy, gross calorific value, in biomass: 3532 megajoule (resources biotic)
- Crude Oil: 2907 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Natural Gas: 1358 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Water to turbine: 1320 cubic meter (Resources Resources from water Renewable material resources from water)
- Uranium: 862.7 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Hard Coal: 855.2 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Calcite: 801 kilogram (resources in ground)
- carbon dioxide (biogenic): 317 kilogram (Resources Resources from air Renewable material resources from air)
- Clay: 301.8 kilogram (soil)
- Energy, Potential (in Hydropower Reservoir), Converted: 173.7 megajoule (natural resource)
- Brown Coal: 137.6 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Gravel: 52.41 kilogram (soil)

## Report excerpt

Source file: `report-p118-119.txt` (SHA-256 8878f744111ef929728b45473b11712460e3499721b8f050980a042900c3cee8), pages 118-119 of `2007 - LCI wood as fuel and const. mat. - Werner.pdf`.

```
12 Boards based on industrial residual wood



Tab. 12.3   Ecoinvent meta information for the cement bonded particle board production processes


Name                                                       particle board, cement bonded, at plant

Location                                                   RER
Infrastructure Process                                     0
Unit                                                       m3
Data Set Version                                           2.0
Included Processes                                         Includes the inputs to the production processes and
                                                           transports of those inputs. No process emission data
                                                           are available.
Amount                                                     1
Local Name                                                 Holzspan-Leichtbauplatte, zementgebunden, ab Werk
Synonyms
General Comment to reference function
Start Date                                                 1989
End Date                                                   2002
Data Valid For Entire Period                               1
Other Period Text
Geograhy text                                              Data for Switzerland used for central Europe
Technology text                                            Medium enterprise technology (2000)
Representativeness [%]
Production Volume                                          unknown
Sampling Procedure                                         Literature
Extrapolations                                             see Geography and Technology
Uncertainty Adjustments                                    The assumption that the technology is representative
                                                           for central Europe is considered in the uncertainties.




ecoinvent-report No. 9                                  - 107 -
                                                                                                                                               12 Boards based on industrial residual wood




                                                                          General Flow information                                                                                                   Representation in ecoinvent                                                                             Uncertainty information

                                                                                                                                                                                      Infra
        Input                Process Name                                          Output                           Remarks                          Cate gory     Sub category               Loca tion      Modul name in ecoinvent             Mean value         Unit     Source mean value        Type       StDv 95% General Comment
                                                                                                                                                                                   struc ture

Industrial residual
                                                                                                                                                                                                          industrial residue wood, mix,
wood softwood            Î                                                                                                                     wooden materials extraction         No        RER                                                       2.33E-01 m3                                           1        1.40 (3,3,4,3,3,5,3)
                                                                                                                                                                                                          softwood, u=40%, at plant
(u=40%), at plant
Industrial residual                                                                             Wood mix: 25% hardwood (beech), 75% softwood
                                                                                                                                                                                                          industrial residue wood, mix,                                    Schniewind 1989, p. 197
wood hardwood            Î                                                                      (pine and spruce); sources: 70% industrial    wooden materials extraction          No        RER                                                       2.31E-02 m3                                           1        1.40 (3,3,4,3,3,5,3)
                                                                                                                                                                                                          hardwood, u=40%, at plant                                        ff.; Wegener et al.
(u=40%), at plant                                                                               residual wood, 30 % industrial wood; hardwood
Industrial wood                                                                                 under bark and softwood under bark reduced by                                                                                                                              (1994: 68ff); Ressel
                                                                                                                                                                                                          industrial wood, hardwood,
beech, at forest road    Î                                                                      12% and 10% respectively because bark is not  wooden materials extraction          No        RER                                                       3.74E-02 m3         (1986)                            1        1.40 (3,3,4,3,3,5,3)
                                                                                                                                                                                                          under bark, u=80%, at forest road
(u=80%)                                                                                         included.
Industrial wood
                                                                                                                                                                                                          industrial wood, softwood, under
spruce, at forest road   Î                                                                                                                     wooden materials extraction         No        RER                                                       5.30E-02 m3                                           1        1.40 (3,3,4,3,3,5,3)
                                                                                                                                                                                                          bark, u=140%, at forest road
(u=140%)
                                                                                                                                               construction                                                                                                                Schniewind 1989, p. 197
Portland Cement          Î                                                                                                                                       binder            No        CH           cement, unspecified, at plant               8.00E+02 kg                                            1        1.24 (1,4,4,3,1,1,4)
                                particle board, cement bonded, at plant




                                                                                                                                               materials                                                                                                                   ff.
Process and cooling                                                                                                                                                                                       Water, cooling, unspecified                                      Schniewind 1989, p. 197
                         Î                                                                      evaporates partly during pressing and drying   resource          in water                                                                              3.00E-01 m3                                           1        1.24 (1,4,4,3,1,1,4)
water                                                                                                                                                                                                     natural origin                                                   ff.
                                                                                                                                                                                                                                                                           Schniewind 1989, p. 197
Organic chemicals        Î                                                                      Additives                                      chemicals         organics          No        GLO          chemicals organic, at plant                 4.50E+01 kg                                            1        1.24 (1,4,4,3,1,1,4)
                                                                                                                                                                                                                                                                           ff.
                                                                                                                                                                                                                                                                           Wegener et al. 1994 for
                                                                                                                                                                                                                                                                           total wood mass into
                                                                                                                                                                                                                                                                           particleboard (586
                                                                                                                                                                                                                                                                           kg/m3 normal
                                                                                                                                                                                                                                                                           particleboard);
                                                                                                Total consumption estimated: chipping                                                                                                                                      Frühwald et al. 2000 for
Electricity medium                                                                              according to Wegner and Frühwald; board                                                                   electricity, medium voltage,                                     part of chip production
                       Î                                                                                                                      electricity        production mix    No        UCTE                                               confidential    kWh                                          1        1.25 (3,3,2,3,1,5,2)
voltage - at grid UCTE                                                                          production according to data on cement-bonded                                                             production UCTE, at grid                                         compared to total
                                                                                                woodwool board production                                                                                                                                                  energy consumption
                                                                                                                                                                                                                                                                           (437 MJ of 1383 MJ
                                                                                                                                                                                                                                                                           Primary energy); CEWAG
                                                                                                                                                                                                                                                                           Düdingen, Herr Kurzo,
                                                                                                                                                                                                                                                                           for mixing, molding,
                                                                                                                                                                                                                                                                           pressing

Thermal heat from oil                                                                           Total consumption estimated based on data on                                                              heat, light fuel oil, at industrial                              CEWAG Düdingen, Herr
                      Î                                                                                                                        oil               heating systems   No        RER                                                confidential    MJ                                           1        1.22 (1,3,2,3,1,5,1)
firing extra light                                                                              cement-bonded wood wool board production                                                                  furnace 1MW                                                      Kurzo
                                                                                                                                                                                                                                                                                                                           (4,5,nA,nA,nA,nA,5
Transport rail           Î                                                                      Chemicals: 600 km, wood & cement: 100 km       transport systems train             No        RER          transport, freight, rail                    1.34E+02 tkm         estimated                         1        2.09
                                                                                                                                                                                                                                                                                                                           )
                                                                                                                                                                                                          transport, lorry >16t, fleet                                                                                     (4,5,nA,nA,nA,nA,5
Transport lorry          Î                                                                      Chemicals & cement: 100 km, wood: 50 km        transport systems road              No        RER                                                      9.80E+01 tkm         estimated                         1        2.09
                                                                                                                                                                                                          average                                                                                                          )
                                                                                                                                                                                                          wooden board manufacturing
plant                    Î                                                                                                                     wooden materials extraction         Yes       RER                                                       4.00E-07 unit       estimated                         1        3.36 (4,5,2,3,4,5,9)
                                                                                                                                                                                                          plant, cement bonded boards
                                                                              Particle board,
                                                                                              Duripanel, medium-high density 1'200 kg/m3                                                                  particle board, cement bonded,
                                                                          Î   cement bonded,                                                   wooden materials extraction         No        RER                                                      1.00E+00 m3
                                                                                              (1000-1350 kg/m3)                                                                                           at plant
                                                                              at plant
                                                                              Waste heat into
                                                                          Î                                                                    air               unspecified                              Heat, waste                                 8.77E+01 MJ          calculated                        1        1.25 (3,3,2,3,1,5,13)
                                                                              air



Fig. 12.4           Flows for "particle board, cement bonded, at plant" and its representation in the ecoinvent database




ecoinvent-report No. 9                                                                                                                                                         - 108 -
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
