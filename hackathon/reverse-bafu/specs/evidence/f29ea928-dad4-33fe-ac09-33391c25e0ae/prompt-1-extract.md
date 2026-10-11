You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Titanium dioxide at plant, sulphate process, at plant` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~1302 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: chemicals / inorganic
- includedProcesses: Cradle-to-gate, includes all ancillary materials, precursors, transports and infrastructure.
- technology: represents a current cross-section of actual plants in Europe
- generalComment: Titanium dioxide produced by the sulfate process is preferred for paper, ink, rubber and a variety of specialty applications. Inventory data are confidential;
CAS number: 013463-67-7; 
Formula: TiO2; 
Synonyms: rutil; 
UUID: f29ea928-dad4-33fe-ac09-33391c25e0ae
- source cited in the metadata: Althaus H.-J. | 2007 | 2007 - LCI chemicals - Althaus
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Natural Gas: 53.31 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Crude Oil: 10.12 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Water to turbine: 7.392 cubic meter (Resources Resources from water Renewable material resources from water)
- Uranium: 6.47 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Hard Coal: 3.442 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Brown Coal: 2.609 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Energy, Potential (in Hydropower Reservoir), Converted: 0.9404 megajoule (natural resource)
- Gravel: 0.693 kilogram (soil)
- Titanium: 0.6895 kilogram (Resources Resources from ground Non-renewable element resources from ground)
- Calcite: 0.5461 kilogram (resources in ground)
- Energy, gross calorific value, in biomass: 0.4262 megajoule (resources biotic)
- Sodium chloride: 0.2462 kilogram (resources in ground)

## Report excerpt

Source file: `report-p845-847.txt` (SHA-256 e1b3f9c29c3269b844db4e57473f744af43e5b933def1abda959c3777ed79248), pages 845-847 of `2007 - LCI chemicals - Althaus.pdf`.

```
85. Titanium dioxide (rutile, anatase, cosmetic white)




       TiCl4 + O2 Æ TiO2 + 2 Cl2                                                                     (5)


The major share of the chlorine is emitted during combustion and is recycled back to the process Some
chlorine is converted to HCl, but most (upwards of 98%) is recycled. The chlorination temperature is
about 1000 °C. TiCl4 is separated and the residual off-gases are treated. The liquid TiCl4 is combusted
to TiO2. Combustion temperatures range from about 900 – 2000 °C. The hot off-gases are cooled and
the TiO2 is separated by filtering. the off-gases are recycled to the combustion chanber.


Also obtained is a metal chloride solution that contains mostly iron (II). Under certain conditions this
solution can be used as a precipitation agent, otherwise it is treated with lime and the solids are land-
filled. The calcium chloride is an effluent resulting from lime treatment and can be drained to sea
(Chemlink.com).


85.6 Life cycle Inventory for titanium dioxide
This inventory is based on confidential information provided by industry sources. The input informa-
tion may not be divulged. Some data can be compared with minimum and maximum values of all
German production locations (UBA BAT Notes, 2001).


85.6.1 Precursor materials

Tab. 85.3   precursors for TiO2 production


Kg per kg of product         Sulfate process        Chloride process         Source
Sulphuric acid               2.4 – 3.5                                       (UBA BAT Notes, 2001)
Rutile, ilmenite             Ca. 2                  na                       Industry sources
Synthetic rutile             ng                     1.06                     (Chemlink.com)
Chlorine                     na                     0.18                     (UBA BAT Notes, 2001)


This report assumes that the sulfate process titanium dioxide has been manufactured from ilmenite, al-
though in fact titanium slag is also used. The chloride process titanium dioxide is also assumed to stem
from ilmenite, although in fact rutile, synthetic rutile and /or beneficiate are used. The data for mining
of ilmenite are taken from (BUWAL 232). Transports are assumed to be from Capetown and from
Melbourne to Rotterdam with some 200 km trucking in Europe.




ecoinvent report No. 8                                     - 764 -
                                        85. Titanium dioxide (rutile, anatase, cosmetic white)


85.6.2 Energy usage

Tab. 85.4   energy consumption for TiO2 production (sulfate process) (UBA BAT Notes, 2001)


Consumption per kg of                                          Follow-up treat-         Acid concentration and      Total
                                     TiO2 manufacture
product (MJ/kg)                                                ment                     filter salt decomposition
Electric energy                      1.5 – 2.31                0.6 – 1.46               0.13-1.3
Steam                                3.7 – 7.7                 6.7 – 10.47              0 – 6.07
Gas                                  7.3 – 11.85               2.37 – 4.22              0 – 0.1
Coal                                 na                        na                       5.8 – 8.5
Total                                12.6 – 20.5               9.9 – 14.3               5.9 – 15.2                  32.7 – 40.9


Note: values can vary, depending on whether or not acid is reconcentrated or neutralized. Both steam
and electricity can be generated from combined heat and power plants (CHP’s). Steam can stem from
sulphuric acid plants (steam burning). Electricity can stem from the grid. The model facility portrayed
in this report uses power and steam from a CHP plant as well as electricity from the UCTE grid. It is
furthermore assumed that acid is reconcentrated and reused. The filter salts that are produced can be
sold.

Tab. 85.5   energy consumption for TiO2 production (chloride process) (UBA BAT Notes, 2001)


Consumption per kg of                                          Follow-up treat-         Total
                                     TiO2 manufacture
product (MJ/kg)                                                ment
Electric energy                      1.51                      0.83
Steam                                1.7                       7.7
Gas                                  2.9                       4.2
Total                                6.1                       12.7                     18.8


The model facility portrayed here uses natural gas in a boiler to produce steam and imports UCTE grid
electricity.


85.6.3 Air emissions

Tab. 85.6   direct air emissions for TiO2 production (sulfate process) (UBA BAT Notes, 2001)


                                 Storage / grind-      Decomposition         Calcination         Follow-up
Gram per kg of product
                                 ing/drying                                                      treatment
Particles                        0.001 – 0.04          ng                    0.13-1.3 *          0.002 – 0.12
NOx                              0.001 – 0.043         ng                    0 – 6.07
SO2                              ng                    0 – 0.119             1*                  ng
H2S                              ng                    0 – 0.005             ng                  ng
            * 0.7 g / kg is used in this report


** This value is used for the model sulfate plant.




ecoinvent report No. 8                                         - 765 -
                                      85. Titanium dioxide (rutile, anatase, cosmetic white)


Tab. 85.7   direct air emissions for TiO2 production (chloride process) (UBA BAT Notes, 2001)


                                                       Solids treatment    Off-gas treat-      Follow-up
Gram per kg of product          Storage
                                                                           ment                treatment
Particles                       0.005                  ng                  ng                  0.186
HCl                             ng                     0.007               0.024 *             ng
SO2                             ng                     ng                  1.68                ng


* This value is used for the model chloride plant.


85.6.4 Wastewater emissions

Tab. 85.8   wastewater emissions for TiO2 production (sulfate process) (UBA BAT Notes, 2001)


Gram per kg of product          Filtration / washing      Follow-up treatment
Sulfate                         30 – 300 *                80 - 110
Iron                            0.25 – 5 **               ng
Cadmium                         0.000001                  ng
Mercury                         0.00000032                ng
            * This report uses a value of 150 g sulfate per kg produced TiO2
            ** This report uses a value of 2 g iron per kg produced TiO2




Tab. 85.9   wastewater emissions for TiO2 production (chloride process) (UBA BAT Notes, 2001)


                                Preparation of the        Follow-up treatment
Gram per kg of product
                                separated solids
Iron                            0.011 *                   ng
Cadmium                         0.00000022                ng
Mercury                         0.00000022                ng
Filter residues                 0.11                      2.25


This report uses a value of 0.5 g iron per kg produced TiO2


85.6.5 Liquid wastes
According to (UBA BAT Notes, 2001) Figure 2.1.3.1, sulphuric acid that enters the wastewater from
the sulfate process contains 30 – 300 g sulfate per kg spent acid (see Tab. 85.9). An average of
roughly 50 g sulfate / kg product.is assumed in this report.


85.6.6 Solid wastes (UBA BAT Notes, 2001)
Sulfate process: According to (UBA BAT Notes, 2001), residues generated from ore digestion total
340 – 670 g / kg product. These wastes are disposal of as hazardous wastes.. If the acid is neutralized
with lime or calcium carbonate, gypsum (calcium sulfate) can be generated in large quantities. Gyp-
sum can be sold for use in the plasterboard, cement and paper industry, demand is growing. This re-
port assumes that 480 g / kg product are produced, solidified in cement and landfilled.
Chloride process. According to (UBA BAT Notes, 2001), chloride process sludges total 184 g / kg
product. Industry sources however suggest somewhat higher values, ranging up to 1 kg / kg product


ecoinvent report No. 8                                         - 766 -
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
