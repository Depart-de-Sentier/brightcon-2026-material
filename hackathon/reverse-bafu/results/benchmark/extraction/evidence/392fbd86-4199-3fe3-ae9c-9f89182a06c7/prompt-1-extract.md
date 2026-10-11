You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Green manure IP, until march` [CH], reference unit 1 ha, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~31 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: agricultural / plant production
- includedProcesses: The inventory includes the processes of soil cultivation, sowing and mulching. Machine infrastructure and a shed for machine sheltering is included. Inputs of fertilisers, pesticides and seed as well as their transports to the farm are considered. The direct emissions on the field are also included. 
- technology: Integrated production
- generalComment: Inventory refers to the production of 1 kg green manure IP, until march.;
Synonyms: catch crop; 
UUID: 392fbd86-4199-3fe3-ae9c-9f89182a06c7
- source cited in the metadata: Nemecek T. | 2007 | 2007 - LCI agricultural prod. systems - Nemecek
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 ha):
- none

## Report excerpt

Source file: `report-p142-144.txt` (SHA-256 fc414d5403b07f6670be36f5e63838c2a01f5284da51ee777b0552d0324b87db), pages 142-144 of `2007 - LCI agricultural prod. systems - Nemecek.pdf`.

```
Life cycle inventories of Swiss and European agricultural production systems - Arable Crop Production in Switzerland


    multiplying the masses of the inputs by the corresponding transport distances for each transport
    carrier.
    Pesticides and fertilisers were converted into the product weight in order to calculate the requirements
    for transport in tkm. For pesticides, a mean active-ingredient content of 50% was used. This mean
    value represents the average active-ingredient content of the pesticides authorised in 2000 (FAW &
    BLW 2000). For phosphate rock, the product weight was calculated based on a P2O5 content of 32%.
    For N-, P- and K fertilisers, the average nutrient contents from Tab. 8.2 were used.
    The transport distances for N-, P-, and K fertilisers were provided by Landor GmbH 76 (see Tab. 8.6).
    For the transport distances of phosphate rock, see chapter 8.2.1 (“Transport” section). For the transport
    of pesticides and seeds, distance from the regional storehouse to the farm was estimated at 15 km.
    Most of the auxiliaries are sold by the agricultural cooperatives (http://www.landi.ch). As there are
    450 sale points distributed throughout Switzerland (http://www.landischweiz.ch/), the distance from
    regional storehouse to farm is unlikely to be very great.

    Tab. 14.8   Supplementary transport considered for crop production.


                               Transport          transport,                         transport,
                               carrier            transoceanic transport, transport, freight,   transport, transport,
                                                  freight ship  barge     lorry      rail       lorry      van <3.5t
                          Location                OCE          RER        RER        CH         CH         CH
Inventories used as input
for crop production       Transport
                          distance added
Seed, at regional         to user CH
storehouse CH
                                                                                                                                  15
N-fertilisers, at regional     to user CH
storehouse RER
                                                                          900                         100          100
P-fertilisers, at regional     to user CH
storehouse RER
                                                                          400                         100          100
K-fertilisers, at regional     to user CH
storehouse RER
                                                                          100                         100          100
Phosphate                      to regional
rock/phosphoric acid, at       storehouse
plant MA                            RER
                                                       2500                             400
Pesticides, at regional        to user CH
storehouse CH
                                                                                                                                  15


    14.2.9 Green Manure
    With integrated and organic production, a soil cover during winter is generally required to reduce the
    risk of soil erosion and nitrate leaching. For autumn-sown crops this soil cover is to a certain extent
    provided by the crop itself. For spring-sown crops (all arable crops in ecoinvent except the cereals and
    rape seed), a green manure was included in the inventories to take account of the winter period,
    thereby ensuring that the period considered is approximately the same for all crops. This means that
    machine usage, any nitrogen applications (for integrated production) and field emissions during the
    winter are included in the inventories for the spring-sown crops. The end date for green manure was
    chosen on the basis of the date of soil cultivation of the spring-sown crop in question. As these dates
    differ between the various spring-sown crops, several inventories for green manure with different end
    dates were included in ecoinvent. Tab. 14.9 shows which green manure inventory was used for the



 76 Personal communication from C. Kopp, Landor GmbH, 6 February 2001.


    ecoinvent-report no. 15a                             Printed: 15.12.2007                                                    137
      Life cycle inventories of Swiss and European agricultural production systems - Arable Crop Production in Switzerland


different spring sown-crops. As the green manure has no harvested product, its reference function is 1
ha cultivated land. Each module for a spring-sown crop uses the fraction of 1 ha of green manure
corresponding to the area required to produce 1 kg of product.

Tab. 14.9   Green manure inventories used for spring-sown crops.


                                                              Spring sown crops for which green manure
Name                                      Location Unit
                                                              inventory was used
                                                              protein peas, IP, at farm
green manure IP, until January            CH          ha
                                                              fava beans IP, at farm
                                                              protein peas, organic, at farm
green manure organic, until January       CH          ha
                                                              fava beans organic, at farm
                                                              sugar beets IP, at farm
green manure IP, until February           CH          ha
                                                              fodder beets IP, at farm
                                                              potatoes IP, at farm
green manure IP, until March              CH          ha
                                                              soy beans IP, at farm
                                                              potatoes organic, at farm
green manure organic, until March         CH          ha
                                                              soy beans organic, at farm
                                                              grain maize IP, at farm
green manure IP, until April              CH          ha      silage maize IP, at farm
                                                              sunflower IP, at farm
                                                              grain maize organic, at farm
green manure organic, until April         CH          ha
                                                              silage maize organic, at farm


The inventories in ecoinvent are for overwintering green manure established by mid-August, with no
biological nitrogen fixation capability (e.g. Cruciferae). Inventories for green manure were compiled
following the same approach as for crop production. The only difference between integrated and
organic production is the application of 30 kg N/ha in the form of mineral fertiliser in the integrated
variant (according to Walther et al., 2001, Tab. 2), which is not done in the case of the organic variant
(LBL et al. 2000, p. 37).


14.2.10 Land Use
Land occupation was calculated from the duration of land use (taking account of the time from soil
cultivation until harvest) and the yield per area unit (see chapter 4.2.1). Land occupation by green
manure was derived using the period from the time of seeding until the end of the month specified in
each green manure inventory. The land occupied was always considered as “Occupation, arable, non-
irrigated”, since the land was assumed not to be irrigated (see chapter 4.3).
Land transformation was calculated on the basis of the area required to produce 1 kg of product. The
type of use before establishment of the crop was assumed to be 71% arable land and 29% meadow
(sown on arable land) for all winter crops. These percentages correspond to the proportions of arable
crops and leys out of the total arable surface in Switzerland (293,000 ha arable crops (71%), 118,000
ha leys (29%), 411,000 ha total (100%) arable surface in 2000), taken from BLW (2001, p. A4). Green
manure is not established after meadow or pasture (as this would cause the meadow to assume the
function of a green manure), but is always established between two arable crops. Land transformation
to green manure was therefore calculated 100% as “Transformation, from arable, non-irrigated”. The
spring-sown crops were assumed to follow a green manure. In these cases too, land transformation was
calculated 100% as “Transformation, from arable, non-irrigated”.
The categories of land resources included are presented in Tab. 14.10.



ecoinvent-report no. 15a                              Printed: 15.12.2007                                                    138
     Life cycle inventories of Swiss and European agricultural production systems - Arable Crop Production in Switzerland


Tab. 14.10 Consideration of land requirements affiliated with crop production.


     Name                                             Category          Unit    Method of Compilation

     Occupation, arable, non-irrigated                resource          m2 a    Time period from soil cultivation for
                                                                                the crop until harvesting and for the
                                                                                area required to produce 1 kg of
                                                                                product
     Transformation, from meadow and pasture, resource                  m2      Derived from the area required to
     intensive                                                                  produce 1 kg of product
     Transformation, from arable, non-irrigated       resource          m2

     Transformation, to arable, non-irrigated         resource          m2



14.2.11 Direct Field Emissions
Direct field emissions were calculated using emission models (described in the chapter 4.4), the results
of which were included in the inventories.
In addition, all pesticides applied for crop production were assumed to end up as emissions to the soil.
The amounts of pesticides used as inputs were thus simultaneously calculated as outputs (emissions to
agricultural soil). The substances specified in the inventories were used as references to correlate the
corresponding emissions. Only for the inputs “pesticides, unspecified”, “fungicides, unspecified” and
“insecticides, unspecified”, could no corresponding flow be assigned. Field emissions resulting from
these admittedly small quantities of substances were thus not considered.


14.2.12 Straw Inventories
ecoinvent data include detailed straw inventories for the different production methods of wheat, rye
and barley (see Tab. 14.1). The inventories “straw IP, at farm” and “straw organic, at farm” calculate a
production mix for straw in Swiss agriculture. They are intended for those wishing to use average
inventories for straw in their studies, without having detailed information about the exact production
method of the cereals, which is the normal situation. Integrated and organic straw are differentiated,
since they are marketed through separate channels.
General straw inventories were compiled by combining the straw inventories for wheat, barley and rye
based on their relative importance over the total agricultural surface area designated for these crops in
Switzerland in the year 2000 (BLW 2001, p. A4 & A40).
Since not all cereal crops were included in ecoinvent, the following assignments were applied:
•   wheat/rye mix for bread production was calculated as wheat,
•   spelt and triticale were calculated as rye,
•   oats and mixes for fodder production were calculated as barley.




ecoinvent-report no. 15a                             Printed: 15.12.2007                                                    139
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 ha.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
