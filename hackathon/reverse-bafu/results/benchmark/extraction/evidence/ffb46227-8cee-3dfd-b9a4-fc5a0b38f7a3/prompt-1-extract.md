You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `High pressure hydrogen Type IV storage tank production` [GLO], reference unit 1 p, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~13 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: pipeline / infrastructure
- includedProcesses: —
- technology: —
- generalComment: Inventory for a high pressure storage Type IV tank, with a capacity of 10 kg of hydrogen at 700 bar (Boureima et al., 2011; Das, 2011). Assumed lifetime of 20 years. Source: C. Wulf et al. / Journal of Cleaner Production 199 (2018) 431-443

 UUID: ffb46227-8cee-3dfd-b9a4-fc5a0b38f7a3
- source cited in the metadata: Sacchi R. | 2024 | 2024 - LCA power-to-X in residential sector - Sacchi
- time period: 2024-01-2024-01

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 p):
- none

## Report excerpt

Source file: `report-p63-64.txt` (SHA-256 121187c43fba8d55fc8ba58ced038f8b7fd6159fe0e3ec727c0cd1e21d3b0451), pages 63-64 of `2024 - LCA power-to-X in residential sector - Sacchi.pdf`.

```
Sacchi, R. and Bauer, C. (2024) LCA of Power-to-X processes and applications in the residential sector.
                                           PSI, Villigen, Switzerland.


                                  polyacrylon     carbon        carbon        carbon        carbon        carbon fiber     carbon      fiber   carbon        carbon
                                  itrile          fiber         fiber         fiber         fiber         production,      production,         fiber         fiber
                                  production      productio     producti      production,   productio     exhaust gas      fiber               productio     productio
                                  (PAN),   by     n,    fiber   on, fiber     fiber         n, exhaust    treatment        stabilization,      n,    fiber   n,
                                  polymerisat     coagulati     relaxatio     winding       gas           2/RER U          carbonization,      drying and    weaved,
                                  ion/RER U       on,           n/RER U       and           treatment                      electrolysis        sizing/RE     at
                                                  stretchin                   unwinding/    1/RER U                        and                 RU            factory/R
                                                  g,                          RER U                                        washing/RER                       ER U
                                                  washing,                                                                 U
                                                  sizing
                                                  and
                                                  drying/R
                                                  ER U

 polymerisation/R
 ER U

 Potassium             kg                          4.06e-02
 permanganate,
 at plant/RER U

 Silicone product,     kg                                       5.00e-03
 at plant/RER U

 tap water, at         kg                                                                                                           6.11E-01
 user/kg/RER U

 transport, freight,   tkm             1.18E-01    1.01E-02     5.03e-02                                       9.54e-03             4.16e-01     1.02e-03     5.85e-02
 lorry 16-32 metric
 ton,          fleet
 average/RER U

 transport, freight,   tkm             2.60E-01    5.72E-02     1.03e-01                                       1.91e-02             8.43e-01     6.09e-03    1.00e+00
 rail/tkm/RER U

 Water,                kg              7.65E-01    2.38E-01                      1.02E-01                                           8.11E-05     2.51E-04
 deionised,       at
 plant/CH U

 Energy inputs


 electricity, low      kWh             2.50e+00   1.03E+00      1.52E-01         1.59E-01      2.29e-02        2.62e-02          2.83E+01        6.25E-01     5.20e-01
 voltage,
 production
 ENTSO,         at
 grid/kWh/ENTSO
 U

 Steam,      for       kg              1.94e+01   3.22E+00      3.56E-01                                                         1.81E+00        1.31E-01
 chemical
 processes,   at
 plant/RER U

 Resources


 Emissions to air

 Argon                 kg                                                                      1.26e-02


 Carbon dioxide,       kg                                                                      1.63e-03        7.02e-01
 fossil

 Nitrogen              kg                                                                      7.43e-03        3.44e+00


 Nitrogen oxides       kg                                                                                      9.99e-03

 Water                 m3                          6.23e-07                                    2.07e-07        4.74e-07


 Emissions        to
 water

 Waste
 treatment

 Treatment,            m3                          1.14e-03
 sewage,       to
 wastewater
 treatment, class
 1/CH U




Table 36 Life cycle inventories to produce a high-pressure Type IV hydrogen tank. Storage capacity of 10 kg.
                                                                                        high pressure hydrogen storage tank/GLO U         Remark(s)

                                                                       Unit                                                       1p      Represents 10kg of storage
                                                                                                                                          capacity

 Material and infrastructure inputs


 Sheet rolling, aluminium/RER U                                        kg                                                  6.00e+00

 Aluminium alloy, AlMg3, at plant/RER U                                kg                                                  6.00e+00


 Sheet rolling, chromium steel/RER U                                   kg                                                  9.00e+00




                                                                                   63
      Sacchi, R. and Bauer, C. (2024) LCA of Power-to-X processes and applications in the residential sector.
                                           PSI, Villigen, Switzerland.


 Chromium steel 18/8, at plant/RER U                                  kg                                        9.00e+00

 carbon fiber production, weaved, at factory/RER U                    kg                                        7.14e+01

 Epoxy resin, liquid, at plant/RER U                                  kg                                        3.06e+01

 Sheet rolling, copper/RER U                                          kg                                        9.00e+00

 Steel, low-alloyed, at plant/RER U                                   kg                                        9.00e+00

 transport, freight, rail/tkm/RER U                                   tkm                                       2.32e+01     Generic transport distances are
                                                                                                                             calculated based on Table 4.2 of
                                                                                                                             the ecoinvent v.2 Methodology
                                                                                                                             report. Distribution: 19.3 kg over
                                                                                                                             1200.0 km.

 transport, freight, lorry 16-32 metric ton, fleet average/RER U      tkm                                       4.83e+01     Generic transport distances are
                                                                                                                             calculated based on Table 4.2 of
                                                                                                                             the ecoinvent v.2 Methodology
                                                                                                                             report. Distribution: 48.3 kg over
                                                                                                                             1000.0 km.

 transport, barge tanker/tkm/RER U                                    tkm                                       7.14e+00     Generic transport distances are
                                                                                                                             calculated based on Table 4.2 of
                                                                                                                             the ecoinvent v.2 Methodology
                                                                                                                             report. Distribution: 71.4 kg over
                                                                                                                             100.0 km.

 Energy inputs

 electricity, low voltage, production ENTSO, at grid/kWh/ENTSO U      kWh                                       4.50e+00




To determine the fraction of a storage tank to attribute per unit mass of hydrogen used, we
need to estimate the need for hydrogen considering a heating period assumed to be six
months per year and monthly deliveries, as described in


Table 37. We can infer the number of high-pressure hydrogen tanks needed on site.




Table 37 Hydrogen storage specifications, for Type I and IV storage tanks.

                                                                                                       Fuel     cell,
 End-use technology                                                Boiler            CHP                                   Fuel cell, SOFC
                                                                                                       PEM

 Power [kWth + kWel]                                                           15      125 + 160              1.6 + 1                            90 + 125

 Total eff. (heat + el.)                                                    111%               81%              95%                                     80%

 Total cap. input-related [kW]                                                 15               444              2.7                                     270

 Annual operation [hours]                                                    2,100            4,100            4,100                                  4,100

 Annual heating [kWh]                                                       34,860         820,000             6,560                              369,000

 Heating period [months/year]                                                   6                 6                6                                         6

 Annual H2 need [kg]                                                          942            54,599              337                                33,056

 Monthly H2 need [kg]                                                         157              9100               56                                   5509

                                                                                             Type I tank requirements

 35-kg H2 storage tanks [unit]                                                  5               260                2                                     158

 H2 storage tank lifetime [years]                                                                                                                          20
 H2 storage tank fraction per kg H2
                                                                       2.65*10-4           2.38*10-4      2.97*10-4                              2.38*10-4
 consumed [unit]

                                                                                             Type IV tank requirements

 10-kg H2 storage tanks [unit]                                                 16               910                6                                     551

 H2 storage tank lifetime [years]                                                                                                                          20




                                                                                64
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
