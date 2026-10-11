You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Packing, clay products` [CH], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~12 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: Others / unspecified
- includedProcesses: Includes the process of packing, transportation within the plant and loading of the bags on paletts. The machines used therefore are included in the infrastructure. The waste treatment after use by the end-user and transports of the packing materials are included.
- technology: Assumption that the same process is used as for packing lime products
- generalComment: The packing and loading process is normalized with an annual production volume of 1'000'000 kg/a and a density of 1'600 m3/kg. The estimated lifespan of the machines is assumed to be 25 years.;
UUID: 80edb9d9-1b57-3472-9388-1f6a3961b4c9
- source cited in the metadata: Kellenberger D. | 2007 | 2007 - LCI building products - Kellenberger
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p178-179.txt` (SHA-256 5ff45668cf7ea68ea1cfbb0aa02103a4d047d609299f9a94e1e18f00ec8a1a74), pages 178-179 of `2007 - LCI building products - Kellenberger.pdf`.

```
Part IV: Clay Products and Processes


7.5         Packing, clay products
The ecoinvent meta information of “packing, clay products” (Tab. 7.10) includes all important and
necessary information to use the data correctly.

Tab. 7.10   Ecoinvent meta information for the product “packing, clay products”


 Name                                 packing, clay products

 Location                             CH
 Infrastructure Process               0
 Unit                                 kg
 Data Set Version                     2.0
 Included Processes                   Includes the process of packing, transportation of packed products to stor-
                                      age and loading of the bags on pallets. The machines used for these proc-
                                      esses are taken into account. The waste treatment of the packaging mate-
                                      rials is included.
 Amount                               1
 Local Name                           Verpacken, Tonprodukte
 Synonyms
 General Comment to refer-            The packing and loading process is normalized with an annual production
 ence function                        volume of 1'000'000 kg/a and a density of 1'600 m3/kg. The estimated life-
                                      span of the machines is assumed to be 25 years.
 Start Date                           2000
 End Date                             2002
 Data Valid For Entire Period         1
 Other Period Text
 Geography text                       Data are from one company (packing, lime products) in Switzerland and
                                      adjusted for clay products.
 Technology text                      Assumption that the same process is used as for packing lime products
 Representativeness [%]
 Production Volume                    Unknown
 Sampling Procedure                   Measured data of one Swiss plant
 Extrapolations                       See geography
 Uncertainty Adjustments              None


Fig. 7.5 shows the module “packing, clay products”. It shows all in- and output flows, the allocation to
the modules in ecoinvent, the sources and the standard deviation for each data. This module is based
on the module “packing, lime products”. The flows are extrapolated using the ratio of the average den-
sities for lime and clay products (about 800 kg/m3 bulk density for average lime product and 1'600
kg/m3 for clay products).




ecoinvent-report No. 7                                   - 31 -
                                                                                                                                               Part IV: Clay Products and Processes



                                                       General Flow information                                                                                                  Representation in ecoinvent                                                                     Uncertainty information
                                                                                                                                                                                    Infra-
                              Process                                                                                                                                 Sub-                 Loca-         Modul name in                Mean                                              StDv         General
         Input                                                                   Output                          Remarks                              Category                      struc-                                                      Unit          Source             Type
                               Name                                                                                                                                 category                tion         ecoinvent 2000               value                                             95%         Comment
                                                                                                                                                                                     ture

                                                                                                 infrastructure weight, copied from module
Infrastructure packing                                                                           "packing, lime product": estimated total     construction                                         industrial machine, heavy,
                         Î                                                                                                                                     machinery             Yes    RER                                       1.50E-03 kg                                 1     3.45   (5,na,na,na,4,na);
and loading                                                                                      weight of machines: 30t, estimated lifespan: processes                                            unspecified, at plant
                                                                                                 20years
energy consumption
                         Î
                               packing and loading of 1 kg clay product                          as no data available, the energy
                                                                                                 consumption is copied from "packing, lime electricity         production mix        No    UCTE
                                                                                                                                                                                                   electricity, medium voltage,
                                                                                                                                                                                                                                      3.09E-03 kWh                                1     1.51   (1,2,1,1,4,1);
packing and loading                                                                                                                                                                                production UCTE, at grid
                                                                                                 product"
                                                                                                 Assumptions: average density (over all lime
                                                                                                 products): 1600kg/m3; loading volume:                                                                                                                 Information Frantschach
pallets, at plant        Î                                                                                                                    wooden materials processing            No     RER    EUR-flat pallet                    6.25E-05 unit                               1     1.68   (4,5,1,1,4,5);
                                                                                                 1m3; pallets used 10 times; weight of                                                                                                                 per Email 05.06.02
                                                                                                 pallet: 22 kg
                                                                                                 circumference of pallet: 4 m; height: 2 m, 2                                                                                                          http://www.dm-
plastic foil extrusion   Î                                                                       layer of plastic with a weight of 0.0123     plastics         processing            No     RER    extrusion, plastic film            6.15E-05 kg      folien.de/hpage.htm,       1     1.56   (4,na,na,na,4,na);
                                                                                                 kg/m2                                                                                                                                                 access Oct. 2003
                                                                                                 circumference of pallet: 4 m; height: 2 m, 2                                                                                                          http://www.dm-
                                                                                                                                                                                                   polyethylene, HDPE, granulate,
plastic foil             Î                                                                       layer of plastic with a weight of 0.0123     plastics         polymers              No     RER                                       6.15E-05 kg      folien.de/hpage.htm,       1     1.56   (4,na,na,na,4,na);
                                                                                                                                                                                                   at plant
                                                                                                 kg/m2                                                                                                                                                 access Oct. 2003
transports of pallets
                                                                                                 standard distance: transport by train with
and plastic foil to plant Î                                                                                                                     transport systems train              No     CH     transport, freight, rail           1.39E-03 tkm                                1     2.46   (5,na,na,na,4,na);
                                                                                                 distance of: 200km,
by train
transports of pallets
                                                                                                 standard distance: transport by lorry 28t                                                         transport, lorry 20-28t, fleet
and plastic foil to plant Î                                                                                                                     transport systems road               No     CH                                        1.39E-03 tkm                                1     2.46   (5,na,na,na,4,na);
                                                                                                 with distance of: 50km,                                                                           average
by lorry
transports of plastic
                                                                                                 assumption: transports all by lorry 16t and                                                       transport, lorry 3.5-16t, fleet
foil to municipal        Î                                                                                                                      transport systems road               No     RER                                       6.15E-07 tkm                                1     1.78   (5,na,na,na,4,na);
                                                                                                 total of transportdistance: 10km                                                                  average
incineration
                                                                          Î   waste heat         Same amount as electricity used                air               unspecified                      Heat, waste                        1.11E-02 MJ                                 1     1.57   (1,3,1,1,4,5);
                                                                              pallets, to                                                       waste             municipal                        disposal, wood untreated, 20%
                                                                          Î                                                                                                          No     CH                                        1.83E-03 kg      EMPA                       1     1.32   (1,4,1,2,3,5);
                                                                              disposal                                                          management        incineration                     water, to municipal incineration

                                                                              plastic foil, in
                                                                                                                                                waste             municipal                        disposal, polyethylene, 0.4%
                                                                          Î   municipal waste                                                                                        No     CH                                        6.15E-05 kg                                 1     1.56   (4,na,na,na,4,na);
                                                                                                                                                management        incineration                     water, to municipal incineration
                                                                              incineration

                                                                              packing of 1 kg
                                                                                                                                                construction
                                                                          Î   of clay product                                                                     others             No     CH     packing, clay products             1.00E+00 kg
                                                                                                                                                materials
                                                                              in general




Fig. 7.5            Flows for “packing, clay products" and their representation in the ecoinvent database




ecoinvent-report No. 7                                                                                                                                                     - 32 -
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
