You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Copper oxide, at plant` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~16 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: chemicals / inorganic
- includedProcesses: Raw materials and chemicals used for production, transport of materials to manufacturing plant, estimated emissions to air and water from production (incomplete), estimation of energy demand and infrastructure of the plant (approximation). Solid wastes omitted.
- technology: Production from copper(II)oxide by hyrdometallurgy. Metallic copper is leached by a solution of ammonia and ammonium carbonate. The overall process yield is of 98%. Inventory bases on stoechiometric calculations. The emissions to air (0.2 wt.% of raw material input) and water were estimated using mass balance. Treatment of the waste water in a internal waste water treatment plant assumed (elimination efficiency of 90% for C).
- generalComment: The functional unit represent 1 kg of solid copper(II)oxide. Large uncertainty of the process data due to weak data on the production process and missing data on process emissions.;
CAS number: 001317-38-0; 
Formula: CuO; 
UUID: 87f791bb-fc12-31eb-ae1e-387398762a32
- source cited in the metadata: Althaus H.-J. | 2007 | 2007 - LCI chemicals - Althaus
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Water To Cooling: 0.024 cubic meter (Resources Resources from water Renewable material resources from water)
- Water: 0.006 cubic meter (Resources Resources from water Renewable material resources from water)

## Report excerpt

Source file: `report-p326-328.txt` (SHA-256 4feacafcef271a7ff3b026626c0a76bd40aae693b048d4b8a87defc2d28bd314), pages 326-328 of `2007 - LCI chemicals - Althaus.pdf`.

```
27. Copper compounds


Raw materials and Chemicals
According to the above shown reaction equations - the following stoechiometric inputs are needed
(yield 100%) for the production of 1.0 kg of copper oxide:

-   copper, Cu: 798.24 g (12.571 mol)

-   ammonium, NH3: 213.702 g (12.571 mol)

-   oxygen, O2: 201.131 g (6.286 mol)

-   ammonium carbonate, (NH4)2CO3: 603.394 g (6.286 mol)


For the production a yield of 98% for the overall reaction out of copper is used. For ammonium and
ammonium carbonate, as these substances are recovered and go back to the process, only an amount
equal to the emissions to air is reported as input in this study here. Therefore 814.531 g copper, 0.427
g ammonium and 1.207 g ammonium carbonate are considered as raw materials in this inventory.
Oxygen is used in the form of air and therefore not further taken into account within this inventory. A
summary of the values used is given in Tab. 27.4.


Cooling water
There was no information available on the amount of cooling water used within the plant. In order not
to neglect the process cooling water demand this value was approximated with data from an large
chemical plant site in Germany producing 2.05 Mt a-1 (intermediates included) of different chemicals
(Gendorf (2000)). In this plant in total an average of 24 kg water per kg of product were used for. This
value is used in this inventory as approximation for the cooling water consumption of the copper(II)-
oxide production.
Concerning the process water, no information is given in the examined sources. Therefore, as a first
approximation, 25% of the cooling water amount are assumed for the process water, i.e. 6 kg per kg of
product.


Transport and Infrastructure
As there is no information about the transport amounts, standard distances and means according to
Frischknecht et al. (2007) are used for the different raw materials.
For the infrastructure of the production plant no information was available. It was assumed that the
importance of the infrastructure is low and therefore the module “chemical plant, organics” was used
as approximation. For this module with a production capacity of 50'000 t per year and a plant life time
of 50 years, an amount of 4 * 10-10 units per kg copper carbonate was included.


27.6.3 Emissions
By-products
According to Richardson (2000a) are the produced ammonium as well as the produced carbon dioxide
recovered and goes back to the start of the process – therefore, these two products are not further taken
into account within this process here.




ecoinvent report No. 8                           - 245 -
                                               27. Copper compounds


Waste heat
It was assumed, that 100% of the electricity consumed, i.e. 1.2 MJ per kg copper oxide is converted to
waste heat. It was assumed that 100% of the waste heat is released to the air.


Emissions to air
There was no data available on process emissions to air for the production of copper oxide. As ap-
proximation the air emissions occurring in the different stages of the production were estimated to
0.2% of the stoechiometric amount (without copper).
This assumption leads to air emissions of 0.427 g ammonium and 1.207 g ammonium carbonates.


Emissions to water
The remaining amount of ammonia compounds is assumed to be recovered together with the produced
amounts of ammonium and carbon dioxide. As these amounts are reused, for this study here, no water
emissions occurs from the copper(II)oxide production.


Solid wastes
Solid wastes occurring during the production of copper(II)oxide were neglected in this inventory.

Tab. 27.4   Energy demand, Resource demand and emissions for the production of copper(II)oxide.


[per kg copper(II)oxide]                                                    Remark

INPUTS
copper                                                  kg         0.815    stoechiometric calc., 98% yield
ammonium                                                kg       4.27E-04   equal to emitted amount
ammonium carbonate                                      kg       1.21E-03   equal to emitted amount
Electricity, medium voltage                            kWh         0.333    estimation
Natural gas, burned in industrial furnace >100kW        MJ           2      estimation
Water, cooling, unspecified                             m3       2.40E-02   estimation
Water, process, unspecified                             m3       6.00E-03   estimation
transport by train                                     tkm       4.90E-01   calculated with standard distances
transport by lorry                                     tkm       8.16E-02   calculated with standard distances
chemical plant, organics                               unit      4.00E-10   approximation for infrastructure
OUTPUTS
waste heat, to air                                      MJ       1.20E+00 calculated from electricity input
ammonium, to air                                        kg       4.27E-04 estimated as 0.2% of stoech. amount
ammonium carbonate, to air                              kg       1.21E-03 estimated as 0.2% of stoech. amount




27.6.4 Data quality considerations
The following table shows the data quality indicators for the inventory of copper(II)oxide production
(Location RER). The uncertainty scores include reliability, completeness, temporal correlation, geo-
graphical correlation, further technological correlation and sample size.
The data in the inventory of the copper carbonate production has a high uncertainty, because only few
data of the production processes were available. Therefore the data for the used materials was assessed
with stoechiometric calculations and the energy demand was estimated by using an average chemical
process as approximation. The highest uncertainties exist for the process energy demand and the emis-
sions. Due to missing data these values are based mainly on assumptions and approximations. Espe-

ecoinvent report No. 8                                 - 246 -
                                                                           27. Copper compounds


cially the uncertainty in the emission data is of importance for the quality of the dataset. Further uncer-
tainty occurs from possibly missing auxiliary materials and further emissions or wastes. Smaller un-
certainties are given for the raw material demand because it is only dependant on the yield-factor used
for the stoecheometric calculations. Also for the infrastructure only an approximation was used be-
cause of missing data. Additionally, the most important fields of the ecospold meta information from
this dataset are listed in chapter 27.9.

Tab. 27.5         Input / Output and uncertainty for the process “copper oxide, at plant (RER)”




                                                                            Location




                                                                                                                                  standardDeviation95%
                                                                                               copper oxide,




                                                                                        Unit
Explanation                                 Name                                                                                                                                GeneralComment
                                                                                                 at plant




                                                                                                               uncertaintyType
                                             Location                                              RER
                                      InfrastructureProcess                                          0
                                                Unit                                                kg
Res ource         Water, cooling, uns pecified natural origin                          m3        2.40E-02         1              1.88                       (5,5,1,1,4,5); es tim ated with data from a large chem . plant
                  Water, uns pecified natural origin                                   m3        6.00E-03         1              1.88                       (5,5,1,1,4,5); es tim ated with data from a large chem . plant
Input from        am m onia, liquid, at regional s torehous e              RER          kg       4.27E-04         1              1.21                        (4,na,na,na,na,na); es tim ation - equal to em itted am ount
Technos phere     copper, at regional s torage                             RER          kg       8.15E-01         1              1.21                    (4,na,na,na,na,na); es tim ation bas ed on proces s yield 90-99.8%
                  am m onium carbonate, at plant                           RER          kg       1.21E-03         1              1.21                        (4,na,na,na,na,na); es tim ation - equal to em itted am ount
                  electricity, m edium voltage, production UCTE, at grid   UCTE        kWh       3.33E-01         1              1.88                       (5,5,1,1,4,5); es tim ated with data from a large chem . plant
                  heat, natural gas , at indus trial furnace >100kW        RER          MJ       2.00E+00         1              1.88                       (5,5,1,1,4,5); es tim ated with data from a large chem . plant
                  chem ical plant, organics                                RER         unit      4.00E-10         1              3.77                                           (4,5,1,3,5,4); es tim ation
                  trans port, freight, rail                                RER         tkm       4.90E-01         1              2.09                                  (4,5,na,na,na,na); s tandard dis tances
                  trans port, lorry 32t                                    RER         tkm       8.16E-02         1              2.09                                  (4,5,na,na,na,na); s tandard dis tances
Output            copper oxide, at plant                                   RER          kg           1
Air em is s ion   Heat, was te                                                          MJ       1.20E+00         1              1.88                              (5,5,1,1,4,5); calculated from electricity input
                  Am m onia                                                             kg       4.27E-04         1              2.32                                       (5,5,na,na,na,5); es tim ation
                  Am m onium carbonate                                                  kg       1.21E-03         1              2.32                                       (5,5,na,na,na,5); es tim ation




27.7 Cumulative results and interpretation
Results of the cumulative inventory for both substances can be downloaded from the database.


27.8 Conclusions
The inventory for both copper compounds is based on the a general literature source (Ullmann), esti-
mations and assumptions. The unit process raw data are meant to be used as background information if
one of these copper compounds is used for a product in small amounts. Therefore these data can only
give an approximation. They are not reliable enough for direct comparison of these materials with
other, alternative products.




ecoinvent report No. 8                                                                   - 247 -
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
