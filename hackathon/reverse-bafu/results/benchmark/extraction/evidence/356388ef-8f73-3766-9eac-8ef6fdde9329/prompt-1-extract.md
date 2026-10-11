You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Ceramic plant` [CH], reference unit 1 p, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~11 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: ceramics / infrastructure
- includedProcesses: Includes land use and materials used in buildings and machinery as well as their disposal
- technology: large scale production plant in Europe.
- generalComment: Life time of 50 years for buildings and of 25 years for machines is assumed. Dataset refers to a factory with yearly output of 5'000 t of ceramic products.;
UUID: 356388ef-8f73-3766-9eac-8ef6fdde9329
- source cited in the metadata: Kellenberger D. | 2007 | 2007 - LCI building products - Kellenberger
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 p):
- none

## Report excerpt

Source file: `report-p213-214.txt` (SHA-256 0d31bb2f67a79b1072dfedd255f42471bd37b6b55d6406320a722f3eb3318b16), pages 213-214 of `2007 - LCI building products - Kellenberger.pdf`.

```
Part VI: Ceramics


                                                                       General Flow information                                                                          Representation in ecoinvent                                                Uncertainty information
                                                                                                                                                                 Infra
                         Process                                                                                                                                         Loca                                                     Source mean             StDv      General
           Input                                                                   Output                 Remarks                 Cate gory     Sub category     struc           Modul name in ecoinvent Mean value      Unit                      Type
                          Name                                                                                                                                           tion                                                        value                95%      Comment
                                                                                                                                                                 ture

                                                                            waste water to
                                                                                                                                                                                                                                Nicoletti et al.
                                                                          Î internal           recycled to wet grinding                                                                                       6.67E-04   m3                         1     1.13   (1,3,1,3,1,4,6)
                                                                                                                                                                                                                                (2002)




                         ceramic tiles, at regional storage; outputs
                                                                            recyclilng
                                                                                                                                                                                treatment, ceramic
                                                                            waste water
                                                                                                                                waste      wastewater                           production effluent, to                         Nicoletti et al.
                                                                          Î after internal     to external treatment                                              No     CH                                   2.00E-05   m3                         1     1.13   (1,3,1,3,1,4,6)
                                                                                                                                management treatment                            wastewater treatment, class                     (2002)
                                                                            pre-treatment
                                                                                                                                                                                3
                                                                              sludge from
                                                                              waste water
                                                                                                                                                                                                                                Nicoletti et al.
                                                                          Î   treatment to     not inventoried                                                                                                2.22E-03   kg                         1     1.13   (1,3,1,3,1,4,6)
                                                                                                                                                                                                                                (2002)
                                                                              external
                                                                              recycling
                                                                              sludge from
                                                                                                                                                                                disposal, hazardous waste,
                                                                              waste water      assumed to be hazardous waste waste       underground                                                                            Nicoletti et al.
                                                                          Î                                                                                       No     DE     0% water, to underground      1.11E-03   kg                         1     1.13   (1,3,1,3,1,4,6)
                                                                              treatment to     because it can not be recycled management deposit                                                                                (2002)
                                                                                                                                                                                deposit
                                                                              landfill
                                                                              wastes to
                                                                                                                                                                                                                                Nicoletti et al.
                                                                          Î   internal         not inventoried                                                                                                3.47E-02   kg                         1     1.13   (1,3,1,3,1,4,6)
                                                                                                                                                                                                                                (2002)
                                                                              recycling
                                                                              wastes to
                                                                                                                                                                                                                                Nicoletti et al.
                                                                          Î   external         not inventoried                                                                                                3.29E-02   kg                         1     1.13   (1,3,1,3,1,4,6)
                                                                                                                                                                                                                                (2002)
                                                                              recycling
                                                                                               assumed to be hazardous                                                          disposal, hazardous waste,
                                                                              wastes to                                       waste      underground                                                                            Nicoletti et al.
                                                                          Î                    wastes because they can not be                                     No     DE     0% water, to underground      8.50E-03   kg                         1     1.13   (1,3,1,3,1,4,6)
                                                                              disposal                                        management deposit                                                                                (2002)
                                                                                               recycled                                                                         deposit
                                                                              dust emissions   Value for comminution and                                                                                                        EPA (1998), size                 (1,3,1,5,1,5,28
                                                                          Î                                                     air            unspecified                      Particulates, < 2.5 um        8.71E-03   kg                         1     1.32
                                                                              to air           glace spray booth (controlled)                                                                                                   assumed                          )
                                                                                                                                                                                                                                                                 (1,3,1,3,1,4,13
                                                                          Î waste heat                                          air            unspecified                      Heat, waste                   1.13E+00   MJ     calculated          1     1.13
                                                                                                                                                                                                                                                                 )
                                                                                                                                construction                                    ceramic tiles, at regional
                                                                          Î tiles (product)                                                    coverings          No     CH                                   1.00E+00   kg
                                                                                                                                materials                                       storage


Fig. 4.2    Flows for "ceramic tiles, at regional storage" and its representation in the ecoinvent database (cont.)




ecoinvent report No. 7                                                                                                                                       - 13 -
                                                                                                                    Part VI: Ceramics


                                            General Flow information                                                                    Representation in ecoinvent                                                   Uncertainty information
                                                                                                                                Infra
                            Process                                                                                                     Loca                                                       Source mean              StDv      General
            Input                                       Output                Remarks             Cate gory      Sub category   struc           Modul name in ecoinvent Mean value        Unit                       Type
                             Name                                                                                                       tion                                                          value                 95%      Comment
                                                                                                                                ture

      total area                                                                                                                               Transformation, from
                        Î                                                                        resource       land                                                           7.69E+04   m2     ÖSPAG (2002)         1     2.02   (1,3,1,3,1,4,8)
      transformed                                                                                                                              unknown
      transformed to                                                                                                                           Transformation, to industrial
                        Î                                                                        resource       land                                                           3.59E+04   m2     ÖSPAG (2002)         1     2.02   (1,3,1,3,1,4,8)
      vegetation area                                                                                                                          area, vegetation

      transformed to                                                                                                                           Transformation, to industrial
                        Î                                                                        resource       land                                                           3.28E+04   m2     ÖSPAG (2002)         1     2.03   (3,3,1,3,1,4,8)
      built up area                                                                                                                            area, built up
      transformed to
                                                                                                                                               Transformation, to traffic
      paved parking     Î                                                                        resource       land                                                           8.20E+03   m2     ÖSPAG (2002)         1     2.03   (3,3,1,3,1,4,8)
                                                                                                                                               area, road network
      lot
      occupation as                                                                                                                            Occupation, industrial area,
                            ceramic plant


                        Î                                                                        resource       land                                                           1.80E+06   m2a    ÖSPAG (2002)         1     1.54   (3,3,1,3,1,4,7)
      vegetation area                                                                                                                          vegetation
      occupation as                                                                                                                            Occupation, industrial area,
                        Î                                                                        resource       land                                                           1.64E+06   m2a    ÖSPAG (2002)         1     1.54   (3,3,1,3,1,4,7)
      built up area                                                                                                                            built up
      occupation as
                                                                                                                                               Occupation, traffic area,
      paved parking     Î                                                                        resource       land                                                           4.10E+05   m2a    ÖSPAG (2002)         1     1.54   (3,3,1,3,1,4,7)
                                                                                                                                               road network
      lot
                                                                                                 construction                                                                                    assumption, based
      building hall     Î                                                                                       buildings        Yes    CH     building, hall                  2.95E+04   m2                          1     3.03   (3,3,1,3,1,4,9)
                                                                                                 processes                                                                                       on ÖSPAG (2002)

      building multy-                                                                            construction                                                                                    assumption, based
                        Î                                                                                       buildings        Yes    RER    building, multi-storey          2.63E+04   m3                          1     3.03   (3,3,1,3,1,4,9)
      storey                                                                                     processes                                                                                       on ÖSPAG (2002)

                                                                                                 construction                                  industrial machine, heavy,                                                          (5,n.A.,n.A.,n.
      machines          Î                                                                                       machinery        Yes    RER                                    1.68E+05   kg     assumption           1     3.23
                                                                                                 processes                                     unspecified, at plant                                                               A.,n.A.,n.A.,9)

                                                   machines to                                                                                                                                                                     (5,n.A.,n.A.,n.
                                               Î                                                                                                                               1.68E+05   kg     assumption           1     3.23
                                                   recycling                                                                                                                                                                       A.,n.A.,n.A.,9)
                                                                   Life time: 50 a; production   construction
                                               Î ceramic plant                                                  others           Yes    CH     ceramic plant                   1.00E+00   unit
                                                                   volume: 5000000 kg/a          materials


Fig. 4.3      Flows for "ceramic plant" and its representation in the ecoinvent database




ecoinvent report No. 7                                                                                                      - 14 -
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 p.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
