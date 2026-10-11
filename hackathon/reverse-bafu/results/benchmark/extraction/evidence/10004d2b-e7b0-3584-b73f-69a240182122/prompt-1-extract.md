You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Yarn production, bast fibres` [IN], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~7 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: textiles / unspecified
- includedProcesses: The inventories include energy consumption, transport and infrastructure related to the processing of bast fibres to yarn (opening, batching, cardening, spinning).
- technology: Opening, batching, cardening, combing and spinning are the main processes of the yarn production. Mechanical cleaning and no chemical cleaning was assumed for this study. 
- generalComment: Inventory refers to the processing of 1 kg fibres only, without the production of the fibres itself.;
UUID: 10004d2b-e7b0-3584-b73f-69a240182122
- source cited in the metadata: Althaus H.-J. | 2007 | 2007 - LCI renewable materials - Althaus
- time period: 2000-01-2007-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p103-106.txt` (SHA-256 693d7bb3f67ee6caf708eb222acef6b2f1325a2d66083005eb2a837bb4d4683c), pages 103-106 of `2007 - LCI renewable materials - Althaus.pdf`.

```
Part I: Life Cycle Inventories of Renewable Fibres




Fig. 4.1   Structure of the processes for the production of textiles from bast fibres


The inventories of processing include data of processing steps apart from the fibres production itself.
The inventories of output products for different bast fibres ‘yarn, at plant’ and ‘textile, at plant’ in-
clude the required bast fibres input good inclusive material loss of processing. Data about different
process steps are listed in Tab. 3.1. The data is based on expert interviews with persons from Jute mill
in Kolkata India (S.K. Dokania, General Manager, The Hooghly Mills Co. Ltd., 2003) and experts
from “Central Research Institute for Jut & Allied Fibres”, Dr. H.S. Sen.. India is one of the main pro-
ducer of bast fibre products (Jute and Kenaf mainly).
The total amount of energy and auxiliary products applied were split on different process stages ac-
cording to expert judgements. Data for infrastructure was added for consistency with ecoinvent proc-
esses. The infrastructure of the mechanical steps spinning and weaving was considered to be similar as
in the packaging industry. Generally infrastructure was assumed to contribute less than 5% of impacts.
Average transport distances were assumed to be about 250 km from the local trader to the bast fibres
mills. Yarn production and if required weeving were assumed to be carried out on the same site
mainly, as in the example of Hessian production in Jute mill ‘The Hooghly Mills Co. Ltd.’ In Kolkata,
India
No data was available for required water and waste water treatment of processing, and therefore not
included.

Tab. 4.1   Energy and material need split for processing steps in jute mill (Total energy and material need from expert
           interview Jute Mill, S.K. Dokania, General Manager, The Hooghly Mills Co. Ltd., 2003)


 Process                   Fibre       Energy need                  Material need            Assumptions
                           loss
 Hessian for textile       18 %        ∅ 1250 MJ/t                  9.4 kg/t batching oil    Transport 250 km local
 production:                           (electricity mainly)         (petroleum based or      trader to bast fibres mill
 - Opening/Batching                    20%                          vegetable oil as for     (lorry)
 - Carding                             40%                          example rice bran oil)
 - Combing/flyer                       10%                                                   Infrastructure similar size
 - Spinning                            10%                                                   and equipment than
                                       20%                                                   packaging plant
 - Weaving



ecoinvent-report No. 21                                    - 25 -
                                          Part I: Life Cycle Inventories of Renewable Fibres


     4.1.1      Input from techno sphere
     Existing ecoinvent data inventories were applied for the energy and material consumption (water, salt,
     auxiliary products), transports, assumption of infrastructure and waste water treatment in the process-
     ing of bast fibres.


     4.1.2      Emissions, CO2-binding and Solar Energy in Biomass of bast fibres
     Emissions, CO2-binding and solar energy are included in the used data inventories. No direct emis-
     sions were considered in the processing.


     4.1.3      Land occupation
     Land occupation is included in the used data inventories of fibres cultivation and infrastructure of
     processing (infrastructure of mechanical processing of bast fibres assumed similar than packaging in-
     dustry ‘packaing box production unit’).


     4.2        Statistics of yarn and textile production
     Statistics of world production of Jute, Kenaf and allied bast fibres are published in the internet by the
     FAO 32 . The world production 2006 was 2’466’620 t Jute (1’415’700 t from India) and 359’260 t Ke-
     naf and allied fibres (159’300 t from India).
     The processed Jute from India is exported 35% as yarn, 30% as hessian and 35% other products as
     carpet, shopping bags, floor coverings, sacking, geotextile etc (P.K. Banerjee, 2003).


     4.3        Characterisation and Use of bast yarn and textiles 33
     Bast fibres, mainly Jute and Kenaf, are cultivated almost exclusively in developing countries of East
     Asia and in some parts of Latin America. Bangladesh, India and Thailand account for over 90 percent
     of world production. The fibre is processed mainly in the producing countries themselves and is used
     for the manufacturing of traditional products such as hessian cloth, food grade bags, carpet backing
     and other floor covering. Diversified jute products, such as geo-textiles and composites are also manu-
     factured in relatively small quantities. Jute constitutes a low proportion of the value of world trade,
     but its cultivation and processing is labour-intensive and therefore provides a livelihood and an impor-
     tant source of food security for many farmers and their families in Asia.


     4.4        Life Cycle Inventories of bast fibre products and processing
     The inventories of processing refer to the spinning of yarn and weaving of textiles. The inventories of
     processing steps include data about the transport to the factories, the energy and material need apart
     from fibres as well as estimations about the related infrastructure. The reference function refers to the
     processing of 1 kg input good. The inventories of resulting products yarn and textile include the pro-
     duction of fibres itself. The reference function is 1 kg yarn or textile respectively.




32
     FAO statistics about world production and price from ftp://ftp.fao.org/docrep/fao/009/j8117m/j8117m00.pdf (August 2007)
33
     Text about Jute, kenaf and allied fibres from http://www.fao.org/docrep/006/y5143e/y5143e1g.htm (August 2007)

     ecoinvent-report No. 21                                    - 26 -
                                                    Part I: Life Cycle Inventories of Renewable Fibres


Tab. 4.2       Unit process of yarn production from jute




                                                                                                                                                                           Standard Deviation
                                                                                                                                         UncertaintyType
                                                                           Location




                                                                                                                                                                                 95%
                                                                                             Unit
                                        Name                                                         yarn, jute, at plant                                                                       GeneralComment




                                      Location                                                                 IN
                               InfrastructureProcess                                                            0
                                        Unit                                                                   kg

product                yarn, jute, at plant                                IN                kg                1


                                                                                                                                                                                                (2,2,3,1,1,4); Fibres loss Jute mill 18% (expert
                                                                                                                                                                                                interview general manager of Jute mill, 2003).
                                                                                                                                                                                                Assumption Carbotech AG, loss mainly in yarn
technosphere           jute fibres, irrigated system, at farm              IN                kg            6.96E-1                         1                               1.16
                                                                                                                                                                                                production and only 2% in further processing
                                                                                                                                                                                                (weeving). 60% fibres from rainfed and 40% from
                                                                                                                                                                                                irrigated systems (FAO statistics)

                                                                                                                                                                                                (2,2,3,1,1,4); Fibres loss 18% (expert interview
                                                                                                                                                                                                general manager of Jute mill, 2003). Assumption
                                                                                                                                                                                                Carbotech AG, loss mainly in yarn production and
technosphere           jute fibres, rainfed system, at farm                IN                kg            4.64E-1                         1                               1.16
                                                                                                                                                                                                only 2% in further processing (weeving). 60% fibres
                                                                                                                                                                                                from rainfed and 40% from irrigated systems (FAO
                                                                                                                                                                                                statistics)

                                                                                                                                                                                                (2,2,3,3,1,4); Fibres loss jute mill about 18% (expert
                                                                                                                                                                                                interview general manager of Jute mill, 2003).
technosphere           yarn production, bast fibres                        IN                kg            1.16E+0                         1                               1.17                 Assumption Carbotech AG, loss mainly in yarn
                                                                                                                                                                                                production and only 2% in further processing
                                                                                                                                                                                                (weeving).


                       disposal, paper, 11.2% water, to
technosphere                                                          CH                     kg            1.60E-1                         1                               1.17                 (2,2,3,3,1,4); 0
                       sanitary landfill




Tab. 4.3       Unit process of yarn production from kenaf
                                                                                                                                                      Standard Deviation
                                                                                                                       UncertaintyType
                                                                Location




                                                                                                    yarn, kenaf, at
                                                                                                                                                            95%
                                                                                      Unit




                                      Name                                                                                                                                        GeneralComment
                                                                                                         plant



                                     Location                                                             IN
                              InfrastructureProcess                                                        0
                                       Unit                                                               kg




product              yarn, kenaf, at plant                      IN                    kg                  1




                                                                                                                                                                                  (2,2,3,1,1,4); Fibres loss Jute mill 18% (expert interview
                                                                                                                                                                                  general manager of Jute mill, 2003). Assumption Carbotech
technosphere         kenaf fibres, at farm                      IN                    kg               1.16E+0           1                             1.16                       AG, loss mainly in yarn production and only 2% in further
                                                                                                                                                                                  processing (weeving). 60% fibres from rainfed and 40% from
                                                                                                                                                                                  irrigated systems (FAO statistics)




                                                                                                                                                                                  (2,2,3,3,1,4); Fibres loss jute mill about 18% (expert interview
                                                                                                                                                                                  general manager of Jute mill, 2003). Assumption Carbotech
technosphere         yarn production, bast fibres               IN                    kg               1.16E+0           1                             1.17
                                                                                                                                                                                  AG, loss mainly in yarn production and only 2% in further
                                                                                                                                                                                  processing (weeving).




                     disposal, paper, 11.2% water, to
technosphere                                                    CH                    kg               1.60E-1           1                             1.17                       (2,2,3,3,1,4); 0
                     sanitary landfill




ecoinvent-report No. 21                                                                              - 27 -
                                                               Part I: Life Cycle Inventories of Renewable Fibres


Tab. 4.4          Unit process of weaving of bast fibres




                                                                                                                             UncertaintyType




                                                                                                                                                                 Deviation 95%
                                                                                                                                                                   Standard
                                                                     Location
                                                                                                         weeving, bast




                                                                                           Unit
                                              Name                                                                                                                                         GeneralComment
                                                                                                            fibres



                                             Location                                                         IN
                                      InfrastructureProcess                                                    0
                                               Unit                                                           kg

product                     weeving, bast fibres                     IN                    kg                 1

                                                                                                                                                                                           (2,2,3,1,1,4); Expert Interview, S.K. Dokania, General Manager of
technosphere                electricity, production mix UCTE        UCTE               kWh                 7.44E-1             1                                 1.16                      Jute Mill 'The Hooghly Mills co. LTD' (2003). Normally the elecricity is
                                                                                                                                                                                           produced by diesel engines.


emission air, unspecified   Heat, waste                                -                   MJ              2.68E+0             1                                 1.16                      (2,2,3,1,1,4); Heat waste derived from electricity consumption


                                                                                                                                                                                           (2,2,3,3,1,4); Assumption Carbotech AG, weeving and yarn
                                                                                                                                                                                           production generally at same site 80%, 10% inland transport of yarn
technosphere                transport, lorry >16t, fleet average    RER                    tkm             5.00E-2             1                                 2.03
                                                                                                                                                                                           to further processing and 10% inland transport to port and oversea
                                                                                                                                                                                           transport to further processing

                                                                                                                                                                                           (2,2,3,3,1,4); Assumption Carbotech AG, weeving and yarn
                                                                                                                                                                                           production generally at same site 80%, 10% inland transport of yarn
                            transport, transoceanic freight ship    OCE                    tkm             1.20E+0             1                                 2.03
                                                                                                                                                                                           to further processing and 10% inland transport to port and oversea
                                                                                                                                                                                           transport to further processing



                                                                                                                                                                                           (5,1,1,3,4,5); Estimation infrastructure of Jute mill comparable to
                                                                                                                                                                                           packaging plant (buidling, equipment, electronics). 50% accounted for
                            packaging box production unit           RER                    unit            5.00E-10            1                                 3.50
                                                                                                                                                                                           spinning and 50% for weeving. Assumption life time 50 years with an
                                                                                                                                                                                           output of 20' 000 t of textile per year. Totally max. 5% of impacts.




Tab. 4.5          Unit process of textile production from jute yarn
                                                                                                                                               UncertaintyType



                                                                                                                                                                           Deviation 95%
                                                                                                                                                                             Standard
                                                                                Location


                                                                                                  Unit




                                                   Name                                                    textile, jute, at plant                                                         GeneralComment




                                                 Location                                                             IN
                                          InfrastructureProcess                                                        0
                                                   Unit                                                               kg

product                      textile, jute, at plant                            IN                kg                  1


                                                                                                                                                                                           (4,2,2,1,1,5); Fibres loss Jute mill 18% (expert interview general
                                                                                                                                                                                           manager of Jute mill, 2003). Assumption Carbotech AG, loss
technosphere                 yarn, jute, at plant                               IN                kg               1.02E+0                       1                          1.30
                                                                                                                                                                                           mainly in yarn production and only 2% in further processing
                                                                                                                                                                                           (weeving).



                                                                                                                                                                                           (4,2,2,1,1,5); Fibres loss Jute mill 18% (expert interview general
                                                                                                                                                                                           manager of Jute mill, 2003). Assumption Carbotech AG, loss
technosphere                 weeving, bast fibres                               IN                kg               1.02E+0                       1                          1.30
                                                                                                                                                                                           mainly in yarn production and only 2% in further processing
                                                                                                                                                                                           (weeving).




                             disposal, paper, 11.2% water, to sanitary                                                                                                                     (4,2,2,1,1,5); The fibre losses are disposed or given for free to
technosphere                                                                    CH                kg               2.00E-2                       1                          1.30
                             landfill                                                                                                                                                      the workers for different uses.




4.5               Data Quality Considerations
There is a wide range concerning the use of fertilizers and pesticides as well as the yields depending
on the region and the type of agriculture. Especially concerning the use of pesticides there are only
very few data available. Large uncertainties exist for emissions on the field. The inventory is based on
published data, statistics and expert interviews. The data of jute fibre processing are also connected
with high uncertainties, because there is a large amount of jute mills and no statistic data are available
e.g. on energy consumption. Nevertheless the data are acceptable for an average production. To quan-
tify the uncertainties the simplified approach with a pedigree matrix has been used for calculating the
standard deviation.

ecoinvent-report No. 21                                                                                           - 28 -
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
