You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Grain maize IP, at feed mill` [CH], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~14 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: agricultural / animal production\animal foods
- includedProcesses: The inventory includes the transport of the raw materials to the feed processing centre, processing feedstuff (crushing or milling, heat treatment, dosing, mixing squeezing and pelleting) and the storage of the feed mixes. It also includes water use and wastewater treatment, the transformation and use of land related to the storage buildings. No process emissions were included except heat waste from the use of electricity. Packaging is not included.
- technology: Refers to expanded feedstuff.
- generalComment: The inventory refers to 1 kg processed feedstuff (fresh weight).;
UUID: dd8175b2-cdc5-38ed-83d8-c4bbc93f8b71
- source cited in the metadata: Nemecek T. | 2007 | 2007 - LCI agricultural prod. systems - Nemecek
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p117-120.txt` (SHA-256 06a09ba1811e375bfaae88460b5751fc137a08cb49bc536b823ecfe87a8911f1), pages 117-120 of `2007 - LCI agricultural prod. systems - Nemecek.pdf`.

```
Life cycle inventories of Swiss and European agricultural production systems - Feedstuffs



12 Feedstuffs
12.1 Characteristics
The products used as feedstuffs for animal husbandry are numerous and of various origin (Tab. 12.1).
While some raw materials for feedstuff are produced only for this purpose (main products), many
others are by-products of human food production. Cereal crops might be used directly as feedstuffs,
while other crops, such as oilseeds, usually undergo many processing steps before being used as
feedstuffs. Recommendations on the feeding of ruminants and data on numerous feedstuffs can be
found in RAP (1999). RAP (1995) provides the information for the feeding of pigs.
The most important category of feedstuffs is cereals crops, followed by oilseed cakes and cereal
products (Tab. 12.1). Around 40% of livestock feedstuffs are imported into Switzerland, mainly from
Europe. Cereals are largely produced in Switzerland, while oilseed cakes and cereal products are
mainly imported from Europe.

Tab. 12.1   Production, import and total consumption of feedstuff in Switzerland. Source: SBV (2000a) and Eidg.
            Oberzolldirektion (1999). The figures are expressed in t/year and refer to the year 1999.

                                  Production        Import CH,      Consumption
Feed                                                                                    % Import Main provenance
                                  CH, t/year        t/year          CH, t/year
Wheat and rye                         178,100          13,500              191,600           7        EU
Oats                                   26,900          24,100               29,637          47        Australia (65%), EU
Barley and triticale                  286,400          25,500              311,900           8        EU
Maize                                 191,300          20,000              211,300          10        Eastern Europe
Rice                                        0          10,200               10,200         100        Western Europe, 44%
                                                                                                      USA + Africa
Sorghum                                     0           7,126                7,126         100        FR
Total Cereals                         682,700         100,426              783,126          13

Legumes (not including soy             10,000          19,726               29,726          66        FR
beans)
Soy beans                                   0           3,566                3,566         100        Western Europe
Total Legumes                          10,000          23,292               33,292          70

Rape-seed cake                         31,300           2,910               34,210           9        DE
Soy-bean cake                               0          77,058               77,058         100        Western Europe; 10%
                                                                                                      Brazil
Other cakes and oilseeds                    0          84,492               84,492         100
Total oilseed cakes                    31,300         164,460              195,760          84

Soy beans (beans for oil)                   0          18,636               18,636         100        Brazil, USA
Milling products                       50,900          87,000              137,900          63
Maize gluten                                0          33,250               33,250         100        USA (80%), EU
By-products of beer                                    16,800               16,800         100
production and legume
processing
Sugar-beet molasses                    31,200           3,297               34,497          10        DE
Glucose and fructose                                   15,803               15,803         100        Western Europe
Dried potatoes                          5,900               0                5,900           0
Potato proteins                             0          20,616               20,616         100        DE, EU
Dextrin and other starch                               30,344               30,344         100        DE, EU
Skimmed milk and whey                  11,500               0               11,500           0
powder
Animal fatsa                           20,000           4,961                    -           -        DE, Western Europe
Yeast                                     200           5,946                6,146          97        EU


ecoinvent-report no. 15a                             Printed: 15.12.2007                                               112
                     Life cycle inventories of Swiss and European agricultural production systems - Feedstuffs


                                    Production        Import CH,      Consumption
Feed                                                                                        % Import Main provenance
                                    CH, t/year        t/year          CH, t/year
Animal proteins (fish meal                      0        10,295              10,295           100       Western Europe
and others)
Total                                   823,700         535,126           1,358,826            39
a
    The use of animal fat in animal feed has been prohibited since 2000 (see chapter 18).


Large quantities of these products are processed into compound feed. The proportions of the different
ingredients in feed mixes vary widely from year to year and manufacturer to manufacturer, depending
on price fluctuations and the current market situation. Nevertheless, the nutritive value of the feed
mixes is kept constant. Animal-feed requirements and the properties of different feedstuffs are given in
RAP (1995 & 1999). To calculate the quantities of a specific compound feedstuff the inventory user
must calculate the required quantities of each feedstuff component. The processing of compound feed
is already included in the inventories.


12.1.1 Characteristics of the Production Process
Feed-mix production comprises different processes, the importance of each of which depends on the
proportions of the different feedstuff categories in each feed mix. The main processes are as follows:
1. Production of the feed ingredients: this production takes place on farm fields (agricultural
   production), as a main product, in factories (industrial production) or as a by-product, in food
   processing factories (by-products). Only feedstuffs stemming from agricultural production were
   considered in the ecoinvent database. The modules described in chapters 14, 15 and 17 provide
   information on the production of some of the raw materials of the feed mixes.
2. Transport to the feed-processing centre and storage of the raw materials: transport is by boat for
   overseas imports and mainly by lorry within Europe and Switzerland. The main factor in transport
   distance is the provenance of the raw materials: raw materials produced in Switzerland have the
   shortest transport distances, followed by raw materials from neighbouring countries (see Tab.
   12.1). Transport distances are greatest for inputs imported from overseas.
3. Processing the feedstuffs: the main steps comprise rolling, crushing or milling, heat treatment,
   dosing, mixing, squeezing and pelleting. For some feed categories such as the oilseed cakes, the
   main processing steps are performed outside the feedstuff factory.
4. Storage and packaging of the feed mixes. The packaging materials are not considered in the
   inventories.
5. Transport from the feed processing centre to the regional storehouse or the final user. As all
   inventories included in ecoinvent refer to “at feed mill”, this final step was not included in the
   inventories. It must, however, be borne in mind by the user of these inventories. The relevant
   information is given below.


12.2 Life Cycle Inventories of Feedstuff
12.2.1 Agricultural Production of the Feed Ingredients
The agricultural crop production and drying inventories are documented in chapter 14. For the
integrated production (IP) of wheat, barley and rye, a mix between the integrated intensive production
(denoted by IP) and the integrated extensive production (called “Extenso”) was calculated for
domestic production, since these products are not processed separately (unlike organic feedstuffs,
which follow a different path). As shown in Tab. 14.11, 42% of wheat and rye and 63% of barley were
produced according to the “Extenso”-rules in 2000. These percentages are used to calculate the mix
for the respective cereal (Tab. 12.2).


ecoinvent-report no. 15a                               Printed: 15.12.2007                                               113
                   Life cycle inventories of Swiss and European agricultural production systems - Feedstuffs


No inventories for the production of raw materials outside Switzerland have been defined in ecoinvent
data V1.0. Production abroad is therefore approximated by integrated production (denoted by “IP”) or
organic production with location in Switzerland. As the “Extenso”-production exists only in
Switzerland, it was assumed that imported cereals used in the IP feed stem from integrated intensive
production.
The import statistics do not differentiate between production from conventional, integrated and
organic farming. We therefore assumed the same proportion of imports for integrated and organic
feedstuffs.

Tab. 12.2   Feedstuff-ingredient production processes, based on statistics from the year 1999 (see Tab. 12.1).

                                % import      % CH-         Out of CH-production (%)          values used in ecoinvent
 Feedstuff, at feed mill,
                                            production                                                  data
 CH
                                                              IP      extensive organic          IP      extensive organic
 wheat, IP                              7             93        58          42           0          61         39      0
 wheat, organic                         7             93         0           0         100           0          0    100
 rye, IP                                7             93        58          42           0          61         39      0
 rye, organic                           7             93         0           0         100           0          0    100
 barley, IP                             8             92        37          63           0          42         58      0
 barley, organic                        8             92         0           0         100           0          0    100
 grain maize, IP                       10             90       100           -           0         100          0      0
 grain maize, organic                  10             90         0           -         100           0          0    100
 protein peas, IP                      66             34       100           -           0         100          0      0
 fava beans, IP                        66             34         0           -         100           0          0    100


12.2.2 Transport to the Feed Processing Centre
Transport of raw materials produced in Switzerland to the feed processing centre is by tractor for short
distances and by lorry or rail for longer distances. For simplicity’s sake, transport within Switzerland
is assumed to be 100 km by lorry. Transport of raw materials from Europe is mainly by lorry, and was
estimated to average 1,000 km. Overseas transport is by transoceanic liner, and was assumed to
average 10,000 km by ship and 2,000 km by barge (transport from production location to pier and
from pier to feed processing centre). Using the cereals as an example, the average transport distances
are then calculated as follows: Provenance of the cereals is 87% domestic production, 10% EU import
and 3% overseas import. Transport distance is then calculated as follows: 87%* 100 km = 87 km by
lorry; 10% * 1,000 km = 100 km by lorry; 3% * 10,000 km = 300 km by transoceanic liner and 3% *
2,000 km = 60 km by barge.

Tab. 12.3   Values for cereals, maize and legumes used in the life cycle inventories for the average transport distance
            from the farm to the feed processing centre. The other values are not used in the inventories given in
            ecoinvent data. They are listed here as references for other applications.


                                                      Transport distance in km
                                                                                               Overseas
                   Feed                               lorry, CH      lorry, RER Barge
                                                                                               ship
                   Cereals                                    87           100           60           300
                   Maize                                      90           100            0             0
                   Legumes                                    30           700            0             0

                   Oilseed cakes                              16           800          80           400
                   Cereal products                            30           550         300         1,500
                   Maize gluten                                0           200       1,600         8,000


ecoinvent-report no. 15a                             Printed: 15.12.2007                                                114
                   Life cycle inventories of Swiss and European agricultural production systems - Feedstuffs


                                                      Transport distance in km
                                                                                               Overseas
                   Feed                               lorry, CH     lorry, RER Barge
                                                                                               ship
                   Sugar and molasses                        62           380            0             0
                   Plant fats                                 0             0        2,000        10,000
                   Potato protein                             0         1,000            0             0
                   Dried potatoes                           100             0            0             0
                   Yeast                                      3           970            0             0
                   Fish meal                                  0         1,000            0             0
                   Crude fibre products (straw)              50           500            0             0


12.2.3 Processing the Feedstuffs
Feed ingredients arise either as main products from production processes (e.g. yeast and minerals), or
as by-products (e.g. cereal products, plant fats).
Given the great number of feedstuff production processes, considerable simplification is required to
adequately describe these processes for the ecoinvent database. Only cereals and legumes are included
as feedstuffs in the database, in addition to dried roughage, which is described in chapter 15. The
processes considered are crushing or milling, heat treatment, dosing, mixing, squeezing and pelleting.
The feed-milling and treatment processes were described in detail by Rossel (2001). The actual
processing and treatment may vary widely, as may the environmental impact. The processes can only
be described for an average situation.
Salzgeber & Lörcher (1996) give the total energy and water consumption of a mill processing about
30,000 tonnes of cereals per year. This mill produces flour for human consumption. The total process
energy consumption of this mill was approx. 350 MJ per tonne of cereal grain processed (98% as
electricity and 2% as fuel) or 440 MJ per tonne of flour produced; the CED was calculated by the
authors as 970 MJ/tonne cereals. The mill consumes 1800 m3 water and produces 1200 m3 wastewater
per year.
For production of feed mixes in the feed processing centres, Cederberg (1998) gives an energy
consumption (CED) of 374 MJ per tonne of expander-treated feed for dairy cows. In the process, the
expander and pelleting treatments use about 80% of the total energy consumed (40% as electricity and
60% as gas). The grinding and mixing requires only 47 MJ per tonne of feed. For the production of
non-expander-treated protein mix, Cederberg (1998) gives an energy consumption of 259 MJ per
tonne.
Hilger et al. (1997) calculated that the production of feed mixes from raw materials on an industrial
scale requires about 270 MJ per tonne feedstuff (CED).
InfoMil (1996) gives a total energy consumption for the production of feed mixes of 300 to 500 MJ
(CED) per tonne of final product by units processing from a few thousand to more than 200,000
tonnes per year. The size of the production units corresponds to the conditions in Switzerland, where
the largest feed processing centre produces 275,000 tonnes of feed per year. These data stem from a
survey of the Dutch feed industry. The feed mills use about 25-45 kWh electricity and 2-6 m3 gas per
tonne of feedstuff produced. The production step “dosing, milling and mixing” uses 18-32 MJ per
tonne in production units processing 1 to 6 tons per charge and about 10 charges per hour. The 2-6 m3
of gas is used in the production step “pelleting and expanding”, which also uses 25-30 kWh electricity.
The data from the different sources seem to give a relatively consistent picture, despite the different
conditions in the various countries. The CED reported levels of between 270 and 500 MJ/tonne of
feedstuff. The values for the flour mill (Salzgeber and Lörcher 1996) are higher, but the quality
requirements are stricter for the production of food than for feedstuffs, hence the processes are more
complex. For ecoinvent the values from InfoMil (1996) were used, namely an average of 35 kWh
electricity and 4 m3 natural gas per tonne of feedstuff. The natural gas was converted into final energy

ecoinvent-report no. 15a                             Printed: 15.12.2007                                       115
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
