You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `xxx Wood wool boards, cement bonded, at plant` [RER], reference unit 1 m3, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~1302 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: material, obsolete / wood, obsolete\products, obsolete
- includedProcesses: Includes the inputs to the production processes, transports of those inputs. No process emission data are available.
- technology: Medium enterprise technology (2000); data stemming from varous sources
- generalComment: density of wood wool boards differs considerably (360-570 kg/m3);
Synonyms: Fichte, Duropanel, Spruce; 
UUID: 2b7663df-e40b-3aa9-b7ee-2ae098409a40
- source cited in the metadata: Werner F. | 2007 | 2007 - LCI wood as fuel and const. mat. - Werner
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 m3):
- Energy, gross calorific value, in biomass: 2804 megajoule (resources biotic)
- Crude Oil: 689.7 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Water to turbine: 403.2 cubic meter (Resources Resources from water Renewable material resources from water)
- Uranium: 271.3 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Natural Gas: 268.4 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Hard Coal: 254.5 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- carbon dioxide (biogenic): 249.1 kilogram (Resources Resources from air Renewable material resources from air)
- Calcite: 215.7 kilogram (resources in ground)
- Clay: 81.4 kilogram (soil)
- Brown Coal: 56.6 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Energy, Potential (in Hydropower Reservoir), Converted: 52.03 megajoule (natural resource)
- Gravel: 19.64 kilogram (soil)

## Report excerpt

Source file: `report-p97-99.txt` (SHA-256 e4722b9d949de48aeba406b29f06dd143015e2e0775e3491a37a0fe4136eac0e), pages 97-99 of `2007 - LCI wood as fuel and const. mat. - Werner.pdf`.

```
10 Wood boards based on round wood



Tab. 10.3   Ecoinvent meta information for the wood wool board production processes


Name                                  wood wool production, u=20%            wood wool boards, cement
                                                                             bonded, at plant

Location                              RER                                    RER
Infrastructure Process                0                                      0
Unit                                  kg                                     m3
Data Set Version                      2.0                                    2.0
Included Processes                    Includes all processes of wood wool Includes the inputs to the production
                                      production from industrial softwood processes, transports of those
                                      (debarked), including air drying (from inputs. No process emission data
                                      u=70 - 20%), external and internal     are available.
                                      transports, sucktion, air
                                      compression, sawmill production
Amount                                1                                      1
Local Name                            Holzwolleproduktion, u=20%             Holzwolle-Leichtbauplatte,
                                                                             zementgebunden, ab Werk
Synonyms                              Fichte,                                Fichte, Duropanel//Spruce
                                      Verpackungsmaterial//Spruce,
                                      packaging material
General Comment to reference          Covers high quality wood wool          density of wood wool boards differs
function                              without shives. The multi-output       considerably (360-570 kg/m3)
                                      process "wood wool production,
                                      u=20%" delivers the two coproducts
                                      "wood wool, u=20%, at plant" and
                                      "industrial residue wood, wood wool
                                      production, softwood, u=20%, at
                                      plant". Allocation is based on the
                                      over-all proceeds of the process.
Start Date                            2002                                   1989
End Date                              2002                                   2002
Data Valid For Entire Period          1                                      1
Other Period Text
Geography text                        Data from the only Swiss wood wool Swiss energy data. Production data
                                      production plant used for central  based on composition from
                                      Europe                             literature. Used for central Europe
Technology text                       Medium enterprise technology           Medium enterprise technology
                                      (2000)                                 (2000); data stemming from varous
                                                                             sources
Representativeness [%]
Production Volume                     unknown                                unknown
Sampling Procedure                    personal communication                 Literature, personal communication
Extrapolations                        see Geography and Technology           see Geography and Technology
Uncertainty Adjustments               The assumption that the technology     The assumption that the technology
                                      is representative for central Europe   is representative for central Europe
                                      is considered in the uncertainties.    is considered in the uncertainties.




ecoinvent-report No. 9                                 - 86 -
                                                                                                                                  10 Wood boards based on round wood




                                                                     General Flow information                                                                                                                Representation in ecoinvent                                                      Uncertainty information
                                                                                                                                                                                                  Infra
                                                                                                                                                                                                          Loca                                                          Source mean               StDv         General
         Input             Process Name                               Output              Allocation          source allocation                Remarks                Category    Sub category    struc            Modul name in ecoinvent       Mean value     Unit                     Type
                                                                                                                                                                                                          tion                                                             value                  95%         Comment
                                                                                                                                                                                                  ture

                                                                                                                                                                                                                                                                       Lindner
                                                                                                                                                                                                                                                                       Produktions AG,
                                                                                                                                   Data from the only Swiss wood
Industrial wood                                                                                                                                                                                                  industrial residue wood,                              Wattwil (2002);
                                                                                                                                   wool production plant.           wooden
spruce debarked, at    Î                                                                                                                                                         extraction        No     RER    softwood, forest-debarked,          2.12E-03   m3     Hr. Wildnagel;     1        1.12   (1,4,1,3,1,1,3)
                                                                                                                                   Shrinkage from drying is         materials
forest road (u=70%)                                                                                                                                                                                              u=70%, at plant                                       www.lindner.ch
                                                                                                                                   included.
                                                                                                                                                                                                                                                                       ; Fax 071/987
                                                                                                                                                                                                                                                                       61 59

                                                                                                                                                                                                                                                                       Lindner
                                                                                                                                   contains all processes incl.                                                                                                        Produktions AG,
                                                                                                                                   Internal transports, sucktion,                                                                                                      Wattwil (2002);
                                                                                                                                                                                                                 electricity, medium voltage,
Electricity            Î                                                                                                           air compression, sawmill       electricity    production mix    No     UCTE                                       5.92E-02   kWh    Taschenbuch        1        1.12   (1,4,1,3,1,1,2)
                                                                                                                                                                                                                 production UCTE, at grid
                                                                                                                                   production; average years 2000                                                                                                      der
                                                                                                                                   and 2001                                                                                                                            Holztechnologie
                              wood wool production, u=20%




                                                                                                                                                                                                                                                                       , p. 443
                                                                                                                                                                    transport                                                                                                                             (4,5,nA,nA,nA,nA,
Transport rail         Î                                                                                                           Wood: 100 km                                  train             No     RER    transport, freight, rail            1.62E-01   tkm    estimated          1        2.09
                                                                                                                                                                    systems                                                                                                                               5)
                                                                                                                                                                    transport                                    transport, lorry >16t, fleet                                                             (4,5,nA,nA,nA,nA,
Transport lorry        Î                                                                                                           50 km transport distance                      road              No     RER                                        8.11E-02   tkm    estimated          1        2.09
                                                                                                                                                                    systems                                      average                                                                                  5)
                                                                                                                                                                    wooden
plant                  Î                                                                                                           Sawmill used as proxy                         extraction       Yes     RER    sawmill                             8.48E-10   unit   estimated          1        3.36   (4,5,2,3,4,5,9)
                                                                                                                                                                    materials
                                                                                                                                   adds / subtracts the amount of
Softwood, allocation                                                                                                                                                wooden                                       softwood, allocation                                                                     calculated
                       Î                                                              100% to wood wool                            CO2 uptake, ressouce                          extraction        No     RER                                       -9.26E-05   m3     calculated         1        1.00
correction                                                                                                                                                          materials                                    correction, 1                                                                            correction term
                                                                                                                                   consumption and embodied
                                                                                                                                   energy that is lacking / too
Softwood, allocation                                                                                                                                                wooden                                       softwood, allocation                                                                     calculated
                       Î                                                              100% to saw dust                             much according to economic                    extraction        No     RER                                        9.26E-05   m3     calculated         1        1.00
correction                                                                                                                                                          materials                                    correction, 2                                                                            correction term
                                                                                                                                   allocation
                                                                                      2.2 CHF/kg;
                                                                                      revenue: 2.2 CHF;    Personal                                                                                                                                                    Lindner
                                                                Wood wool, at plant                                                                                 wooden
                                                            Î                         revenue process:     communication, Mr.                                                    extraction        No     RER    wood wool, u=20%, at plant          1.00E+00   kg     Produktions AG,
                                                                (u=20%)                                                                                             materials
                                                                                      2.2012 CHF; alloc.   Wildhaber, Linder AG                                                                                                                                        Wattwil (2002)
                                                                                      factor: 1.0

                                                                                                            estimation after Werner
                                                                                      13 CHF/m3;            2002, based on Gautschi
                                                              Sawdust spruce, at      revenue: 0.0012       2001 (value increased by                                                                             industrial residue wood, wood                         Lindner
                                                                                                                                     around 5% input material; used wooden
                                                            Î woodwool-plant          CHF; revenue          1.61 based on wood with                                              extraction        No     RER    wool production, softwood,          9.26E-05   m3     Produktions AG,
                                                                                                                                     mainly by farmers              materials
                                                              (u=20%)                 process: 2.2012       u=140% due to lower                                                                                  u=20%, at plant                                       Wattwil (2002)
                                                                                      CHF; alloc. factor: 0 water content (after
                                                                                                            Vhe Nr. 407 (2002))

                                                                                                                                                                                                                                                                       Lindner
                                                            Î Waste heat into air                                                                                   air          unspecified                     Heat, waste                         5.92E-02   MJ     Produktions AG,    1        1.12   (1,4,1,3,1,1,2)
                                                                                                                                                                                                                                                                       Wattwil (2002)




Fig. 10.7         Flows for "wood wool production, u=20%" and its representation in the ecoinvent database




ecoinvent-report No. 9                                                                                                                                         - 87 -
                                                                                                                                         10 Wood boards based on round wood



                                                                             General Flow information                                                                                        Representation in ecoinvent                                                        Uncertainty information
                                                                                                                                                                                Infra
                                                                                                                                                                                        Loca                                                             Source mean                StDv         General
         Input                Process Name                                                        Output                     Remarks              Category     Sub category     struc            Modul name in ecoinvent        Mean value       Unit                      Type
                                                                                                                                                                                        tion                                                                value                   95%         Comment
                                                                                                                                                                                ture

Wood wool, at plant                                                                                                                             wooden                                                                                                  Schniewind
                      Î                                                                                         120-180 kg                                    extraction         No     RER    wood wool, u=20%, at plant            1.50E+02    kg                         1        1.24   (1,4,4,3,1,1,4)
(u=20%)                                                                                                                                         materials                                                                                               1989, p. 197 ff.

                                                                                                                                                construction                                                                                            Schniewind
Portland Cement       Î                                                                                         180-250 kg                                   binder              No     CH     cement, unspecified, at plant         2.15E+02    kg                         1        1.24   (1,4,4,3,1,1,4)
                                                                                                                                                materials                                                                                               1989, p. 197 ff.

Process and cooling
water
                      Î          wood wool boards, cement bonded, at plant                                      200-290 kg; evaporates partly
                                                                                                                during drying
                                                                                                                                                resource      in water
                                                                                                                                                                                               Water, cooling, unspecified
                                                                                                                                                                                               natural origin
                                                                                                                                                                                                                                      2.45E-01   m3
                                                                                                                                                                                                                                                        Schniewind
                                                                                                                                                                                                                                                        1989, p. 197 ff.
                                                                                                                                                                                                                                                                            1        1.24   (1,4,4,3,1,1,4)


                                                                                                                Additives: 6-8 kg; sometimes,
                                                                                                                                                                                                                                                        Schniewind
Organic chemicals     Î                                                                                         no organic chemicals but        chemicals     organics           No     GLO    chemicals organic, at plant           7.00E+00    kg                         1        1.24   (1,4,4,3,1,1,4)
                                                                                                                                                                                                                                                        1989, p. 197 ff.
                                                                                                                waterglas is used

                                                                                                                                                                                                                                                        CEWAG
                                                                                                                                                                                               electricity, medium voltage,                             Düdingen, Herr
Electricity           Î                                                                                         confidential                    electricity   production mix     No     UCTE                                   confidential      kWh                        1        1.12   (1,4,1,3,1,1,2)
                                                                                                                                                                                               production UCTE, at grid                                 Kurzo, Tel. 026
                                                                                                                                                                                                                                                        492 94 50

                                                                                                                                                                                                                                                        CEWAG
Thermal heat from oil                                                                                                                                                                          heat, light fuel oil, at                                 Düdingen, Herr
                      Î                                                                                         confidential                    oil           heating systems    No     RER                                    confidential      MJ                         1        1.12   (1,4,1,3,1,1,1)
firing extra light                                                                                                                                                                             industrial furnace 1MW                                   Kurzo, Tel. 026
                                                                                                                                                                                                                                                        492 94 50
                                                                                                                Chemicals: 600 km, cement:      transport                                                                                                                                   (4,5,nA,nA,nA,nA,
Transport rail        Î                                                                                                                                       train              No     RER    transport, freight, rail              2.57E+01    tkm    estimated           1        2.09
                                                                                                                100 km, wood: 0 km              systems                                                                                                                                     5)
                                                                                                                Chemicals & cement: 100 km,     transport                                      transport, lorry >16t, fleet                                                                 (4,5,nA,nA,nA,nA,
Transport lorry       Î                                                                                                                                       road               No     RER                                          2.22E+01    tkm    estimated           1        2.09
                                                                                                                wood: 0 km                      systems                                        average                                                                                      5)
                                                                                                                                                wooden                                         wooden board manufacturing
plant                 Î                                                                                                                                       extraction        Yes     RER                                           4.00E-07   unit   estimated           1        3.36   (4,5,2,3,4,5,9)
                                                                                                                                                materials                                      plant, cement bonded boards
                                                                                          Woodwool boards,
                                                                                                                medium density 450 kg/m3 (360 wooden                                           wood wool boards, cement
                                                                                        Î cement bonded, at                                                   extraction         No     RER                                          1.00E+00    m3
                                                                                                                570 kg/m3)                    materials                                        bonded, at plant
                                                                                          plant
                                                                                        Î Waste heat into air                                   air           unspecified                      Heat, waste                           3.29E+01    MJ     calculated          1        1.12   (1,4,1,3,1,1,13)



Fig. 10.8         Flows for "wood wool boards, cement bonded, at plant" and its representation in the ecoinvent database




ecoinvent-report No. 9                                                                                                                                                - 88 -
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
