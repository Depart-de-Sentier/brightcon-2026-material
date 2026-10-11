You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Manganese, at regional storage` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~6 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: metals / non ferro
- includedProcesses: The module production by electrolysis from ore and by electrothermic process from ferromanganese and slag. Transportation to Europe is only partially considered.
- technology: The metal is won by electrolysis (assumption: 25%) and electrothermic processes (assumption: 75%). No detailed information available, mainly based on rough estimates.
- generalComment: The module describes the consumption of manganese metal in Europe in 1994. It is designed solely for the use of the metal in special applications like sputtering or as alloying element. This module is explicitly not to be used as alloying element in bulk iron or steel industry. It does not consider secondary sources of manganese. Process data is based on rough estimations, the overall data quality is very poor.;
UUID: 00ff4acd-7e82-3d59-abc6-768375eba3ba
- source cited in the metadata: Classen M. | 2009 | 2009 - LCI metals - Classen
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p405-407.txt` (SHA-256 a65356fb60402ea80618ffd9f4e2251f736f2b2f225dab7e35294d1147b6d859), pages 405-407 of `2009 - LCI metals - Classen.pdf`.

```
5. System Characterisation


Wastes: Dust, fume and sludge; Slag.


5.3.2      “manganese, pure metal, at regional storage” in ecoinvent
The module describes the manganese metal consumed in Europe in 1994. It is designed solely for the
use of the metal in special applications like sputtering or alloying element. This module is explicitly
not to be used as alloying element in bulk iron or steel industry. The overall quality of this module is
poor due to a lack of data.
The layout of the module with general flow information, remarks, sources, values and uncertainty in-
formation is shown in Fig. 5.6. Ecoinvent meta information for this process are summarised in Tab.
5.1 on page 11. The following paragraphs describe calculations, sources and assumptions chosen in
this study. The functional unit of this process is one tonne of manganese consumed in Europe. No in-
formation is available on the share of the two major production processes, a ratio electrother-
mal/electrolysis of 75/25 is assumed.
Electrolytic process
No information on material input and output were available. The energy demand is stated in
Wellbeloved et al. (1997) to be 9 - 12 kWh per kg manganese. Considerable amounts of chemicals
ought to be used for reduction and leaching, but no detailed information is available. Hence none of
these emissions are taken in account. For grinding prior to electrolysis, a value of 20 kWh electrical
energy per tonne processed ore is assumed, reported in IPPC (2002) for base metal sites. A yield of
60 % is roughly estimated.
Electrothermal process
The production of bulk manganese by this method is a well protected secret and little information ap-
pears in the literature. The process is a refinement of the silicothermic reduction of manganese. It re-
sembles that of low-carbon ferromanganese in electric arc furnaces of 1 – 3 MW power consumption.
The raw material used is either low-iron manganese ore or a manganese slag concentrate. The silicon
is in the form of a special silicomanganese which is made from a manganese slag concentrate or from
pure ores. Reduction as complete as possible is ensured by the addition of lime, which forms a basic
slag (Wellbeloved et al. (1997)).
In this study it is assumed, that 75 % of the Mn contained in the raw material originates from ore with
a special grade, which is processed in a way similar to high-coal ferromanganese, the rest being slag,
which is burden free. No information on the further refining process of manganese is available and no
estimations are made in this study. Adelhardt & Saiger (1999) reports efficiencies between 60 % and
65 %, for this study the average of 62.5% was chosen.
Import to Europe: Since some transport intensity is already included in the 1.2 kg ferromanganese
used for the electrothermic process, no further transportation is inventoried within this module. This
approach is obviously not correct, but it will not influence the data quality of the inventoried process,
which is already poor.
Data quality
This process is mainly based on rough estimates. The process specific emissions could be considerable
but due to lack of data none are considered. This module only is to be used, where it plays a minor
role, like in sputtering. If the impact of the modules use is considered to be high, more specific inves-
tigations have to be conduced.




ecoinvent v2.1 report No. 10                       - 29 -
                                                                                                   5. System Characterisation



                      Ge neral Flow Informa tion                                                             Representation in ecoinvent                                                                        Uncertainty Informations




                                                                                                                                                                                                                  Source for
                                                                                                                                                                           ecoinvent




                                                                                                                                                                                                                                      Deviation



                                                                                                                                                                                                                                                       Comment
                                                                                                                                                                                                                                      Standard
                                                                                                              Category




                                                                                                                                                          Location
                                                                                                                                  category



                                                                                                                                             structure
                                                                                         Remarks
                                                              Output




                                                                                                                                                                            name in




                                                                                                                                                                                                                                                        General
                                Process




                                                                                                                                                                             Modul
                                 Name




                                                                                                                                                                                                                    value
           Input




                                                                                                                                                Infra-




                                                                                                                                                                                                                    mean
                                                                                                                                                                                               value
                                                                                                                                    Sub-




                                                                                                                                                                                                                               Type
                                                                                                                                                                                               Mean


                                                                                                                                                                                                       Unit
                                                                                                                                                                     f erromanganese,
f erromanganes                                                                                                                                                                                                                                    (5,5,1,1,1,5,4);
                                                                                                      metals               extraction        No         RER         high-coal, 74.5% Mn,   1.21E+00   kg     Calculation       1     1.62
e                                                                                                                                                                                                                                                 rough estimate
                         regional storage                                                                                                                            at regional storage
                          manganese, at
                                                                                                                                                                                                                                                  (5,5,1,1,1,5,4);
high silica slag                                                      not inventoried                                                                                                      9.68E-01   kg     Calculation       1     1.62
                                                                                                                                                                                                                                                  rough estimate
manganese                                                                                                                                                            manganese,
                                                                                                                                                                                                                                                  (5,5,1,1,1,5,4);
concentrate f or                                                                                      metals               extraction        No         GLO         concentrate, at        9.83E-01   kg     Calculation       1     1.62
                                                                                                                                                                                                                                                  rough estimate
electrolysis                                                                                                                                                         benef iciation
                                                                                                                                                                     electricity, medium                                                   based on
Energy f or
                                                                                                      electricity          production mix    No         UCTE        voltage, production    2.63E+00 k Wh (Wellbeloved 197) 1         1.14 theoretical
electrolysis
                                                                                                                                                                     UCTE, at grid                                                         values
Inf rastructure,                                                                                                                                                     non-f errous metal,
                                                                                                      metals               extraction        Y es GLO                                      1.06E-14 unit rogh estimate         1     3.32 (5,5,1,1,1,5,9)
unspecif ied                                                                                                                                                         smelter
                                                                                                                            low population
                                               w aste heat                                            air                                                           Heat, w aste           9.47E+00   MJ                       1     1.16 (3,2,3,1,1,2,13)
                                                                                                                            density
                                                                                                                                                                     manganese, at
                                               manganese metal        global average                  metals               extraction        No         RER                                1.00E+00   kg
                                                                                                                                                                     regional storage


Fig. 5.6           Flows for “Manganese, pure metal, at regional storage” and its representation in the ecoinvent database. Values correspond to the functional unit of 1 kg manganese metal.




ecoinvent v2.1 report No. 10                                                                                             - 30 -
                                                 6. Literature



6           Literature
Adelhardt & Saiger (1999)      Adelhardt W. and Saiger H. (1999) Stoffmengenflüsse und Energiebedarf bei
                               der Gewinnung ausgewählter mineralischer Rohstoffe; Teilstudie Mangan. In:
                               Geologisches Jahrbuch, Vol. Sonderhefte SH 8. Bundesanstalt für Geowissen-
                               schaften und Rohstoffe, Hannover. ISBN 3-510-95830-6.
Althaus et al. (2004)          Althaus H.-J., Blaser S., Classen M. and Jungbluth N. (2004) Life Cycle Inven-
                               tories of Metals. Final report ecoinvent 2000 No. 10. EMPA Dübendorf, Swiss
                               Centre for Life Cycle Inventories, Dübendorf, CH, Online-Version under:
                               www.ecoinvent.ch.
Anonymous (1998a)              Anonymous (1998a) Dust Control. In: Best Practice Environmental Manage-
                               ment in Mining. Environment Australia, Online-Version under: http://
                               www.ea.gov.au/industry/sustainable/mining/booklets/dust/.
Anonymous (1998b)              Anonymous (1998b) Pollution Prevention and Abatement Handbook. The World
                               Bank Group, Online-Version under: http://lnweb18.worldbank.org/essd/ ess-
                               dext.nsf/51ByDocName/PollutionPreventionandAbatementHandbook.
EC (2002)                      EC (2002) European Dioxin Inventory. European Commission. Retrieved from
                               http://europa.eu.int/comm/environment/dioxin/download.htm. Date of last revi-
                               sion: 22.08.2002.
EPA (1998)                     EPA (1998) Stationary Point and Area Sources. In: Compilation of Air Pollutant
                               Emission Factors, AP-42, Vol. 1. Fifth Edition, Online-Version under:
                               http://www.epa.gov/ttn/chief/ap42/index.html.
Frischknecht et al. (2006)     Frischknecht R., Althaus H.-J., Bauer C., Capello C., Doka G., Dones R.,
                               Faist Emmenegger M., Hischier R., Jungbluth N., Kellenberger D., Margni M.,
                               Nemecek T. and Spielmann M. (2006) Documentation of changes implemented
                               in ecoinvent Data v1.2 and v1.3. ecoinvent report No. 16. EMPA Dübendorf,
                               Swiss Centre for Life Cycle Inventories, Dübendorf, CH.
Frischknecht et al. (2003)     Frischknecht R., Jungbluth N., Althaus H.-J., Doka G., Dones R., Hellweg S.,
                               Hischier R., Nemecek T., Rebitzer G. and Spielmann M. (2003) Overview and
                               Methodology. Final report ecoinvent 2000 No. 1. Swiss Centre for Life Cycle
                               Inventories, Dübendorf, CH, Online-Version under: www.ecoinvent.ch.
Hilbrans & Hinrichs (1999)     Hilbrans H. and Hinrichs W. (1999) Stoffmengenflüsse und Energiebedarf bei
                               der Gewinnung ausgewählter mineralischer Rohstoffe; Teilstudie Nickel. In:
                               Geologisches Jahrbuch, Vol. Sonderhefte SH 7. Bundesanstalt für Geowissen-
                               schaften und Rohstoffe, Hannover. ISBN 3-510-95829-2.
IPCC (1996)                    IPCC (1996) Reference Manual. In: Revised 1996 IPCC Guidelines, Vol. 3,
                               Online-Version under: http://www.ipcc-nggip.iges.or.jp/public/gl/invs1.htm.
IPPC (2001)                    IPPC (2001) Integrated Pollution Prevention and Control (IPPC); Reference
                               Document on Best Available Techniques in the Non Ferrous Metals Industries.
                               European Commission. Retrieved from http://www.jrc.es/pub/english.cgi/
                               0/733169
IPPC (2002)                    IPPC (2002) Integrated Pollution Prevention and Control (IPPC); Draft Refer-
                               ence Document on Best Available Techniques for Management of Tailings and
                               Waste-Rock in Mining Activities. European Commission. Retrieved at
                               01.03.2003 from http://www.jrc.es/pub/english.cgi/0/733169
Jones (1994)                   Jones T. S. (1994) Manganese Material Flow Pattern. IC-9399. U.S. Department
                               of the Interior, Bureau of mines, Online-Version under: http://pubs.usgs.gov/
                               of/of01-304/.



ecoinvent v2.1 report No. 10                        - 31 -
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
