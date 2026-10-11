You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Heat, residential, by conversion of hydrogen using fuel cell, SOFC, allocated by exergy, distributed by pipeline, produced by Electrolysis, PEM using electricity from Solar PV + Wind (MA)` [CH], reference unit 1 MJ, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~8 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: heat / synthetic\transformation
- includedProcesses: —
- technology: —
- generalComment: This dataset represents the supply of 1 megajoule of heat in a residence, by hydrogen conversion in a fuel cell, SOFC. The hydrogen is produced by  Electrolysis, PEM, with electricity from Solar PV + Wind (MA) as feedstock. Heat conversion efficiency [% LHV input]: 33%. LHV [MJ/kg]: 120. Market price [Euro/MJ]: 0.03. Synthesis efficiency [% LHV input]: 0%. Total cap. Input-related [kW]: 268.75. CO2 biogenic share [%]: 0%. Power [kW]: 90. Lifetime [years]: 19.51. Annual operation [hours]: 4100. Allocation factor: 0.08. On-site storage loss [%]: 0. Use loss [%]: 0.56. For more information, refer to: Sacchi, R. and Bauer, C. LCA of Power-to-X processes and applications in the residential sector. Paul Scherrer Institut, 2023. Source: Sacchi, R. and Bauer, C. LCA of Power-to-X processes and applications in the residential sector. Paul Scherrer Institut, 2023.

 UUID: 405ca232-c566-37a2-98a7-913d686ea0e3
- source cited in the metadata: Sacchi R. | 2024 | 2024 - LCA power-to-X in residential sector - Sacchi
- time period: 2024-01-2024-01

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 MJ):
- none

## Report excerpt

Source file: `report-p84-86.txt` (SHA-256 102f9702f0c8e923d7cf5447e70660d03ba0c4624fdfe90aabf3bfd761b72738), pages 84-86 of `2024 - LCA power-to-X in residential sector - Sacchi.pdf`.

```
Sacchi, R. and Bauer, C. (2024) LCA of Power-to-X processes and applications in the residential sector.
                                          PSI, Villigen, Switzerland.




             hydrogen supply, …
        1 kWh/33.33 kWh/kg/thermal or
          electric eff.*allocation factor

                                                                                                            electricity, from residential
             hydrogen supply, …
          ((1+storage loss)*(1+use loss)-
                                                                                                                  heating system
                1)*hydrogen input                                                                                       1 kWh
                                                               electricity, residential, by
        fuel cell system assembly, 1                            conversion of hydrogen                              Water (to air)
           kWe, proton exchange                                   using fuel cell PEM,                       1 kWh/33.33 kWh/thermal eff. * 9 kg
              membrane (PEM)
         1/(Power [kW] * Annual op. [hours] *
                                                                  allocated by exergy
     lifetime [years] * 1 [kWh/kWh]) * allocation                                                                 Hydrogen (to air)
                          factor
                                                                                                                           losses
                  If delivery by truck

          high pressure hydrogen
                storage tank
        2.00e-4 unit * (hydrogen input + losses)



                       others

Figure 30 Schematic mass and energy balance for the electricity supply via hydrogen conversion in a PEM fuel cell
system. Red numbers represent material, energy, or infrastructure input amounts. Blue numbers represent
incoming and outgoing biosphere flows. The green number is the amount of the reference flow of the process.

Additionally, forty alternative datasets are modeled:
    •        using different electrolyzer types: AEC, SOEC, and SOEC with steam input,
    •        using other hydrogen production methods: Auto-Thermal Reforming, with and without
             CCS,
    •        using different feedstock inputs: for electrolytic hydrogen, we consider the Swiss
             renewable electricity mix, Swiss solar power, Morocco-based solar power, Morocco-
             based wind power, and Denmark-based wind power. For the SMR and pyrolysis
             options, we consider liquefied natural gas from Algeria.
Referring to Section 7.3 of (Rolf Frischknecht et al. 2007), the pedigree matrix factors
described in Table 54 for uncertainty estimation are considered.
Table 54 Uncertainty factors used for uncertainty estimation. Note that the scores apply to all data points of the
dataset. In addition, a flow-specific basic uncertainty factor is applied (see Table 7.2 of (Frischknecht et al. 2007)).

                        Reliability                 Completeness       Temporal          Geographical        Further                      Sample
                                                                       correlation       correlation         technological                size
                                                                                                             correlation

 H2            in                          1                       5                 1                  2                           3              5
 PEMFC



Additionally, basic uncertainty factors listed in Table 7.2 of (Rolf Frischknecht et al. 2007) are
applied to the relevant technosphere and biosphere flows.

2.8.2 SOFC fuel cell
For this study, we consider the life cycle inventories from the UVEK:2022 database, originally
from (Primas 2007), which describes a 125 kWel solid oxide fuel cell system. However,
biomethane or natural gas are the fuels considered in the original publication. The system has
an electrical efficiency of 47%, a thermal efficiency of 33%, for an overall efficiency of 80%.
Table 55 Specifications for a 125-kWel SOFC fuel cell system.




                                                                             84
     Sacchi, R. and Bauer, C. (2024) LCA of Power-to-X processes and applications in the residential sector.
                                          PSI, Villigen, Switzerland.


                                                                                                               Source/Remark

 Energy carrier                                                               Hydrogen

 End-use technology                                                           Fuel cell, SOFC

 Heat conversion efficiency [% LHV input]                                                         33.0%        (Primas 2007)

 Electricity conversion efficiency [% LHV input]                                                  47.0%

 Lifetime [years]                                                                                      20

 Powerth [kW]                                                                                          90

 Powerel [kW]                                                                                        125

 Total cap. input-related [kW]                                                                       270       Calculated from
                                                                                                               the rows above.
 Total eff. (heat + el.)                                                                            80%

 Annual operation [hours]                                                                          4’100       (Kägi et al. 2021)

                                                                                                369,000        Calculated from
 Annual heating [kWh]
                                                                                                               the rows above.
 Annual heating period [months]                                                                          6     Assumption used
                                                                                                               for sizing of the
                                                                                                               hydrogen storage
 Annual H2 need [kg]                                                                              33’056       Calculated from
                                                                                                               the rows above.



Fifty datasets are modeled using different hydrogen production technologies and feedstocks,
following the modelling principle schematically represented in Figure 31 and Figure 32.
However, none of those datasets are further discussed in this report. Their associated
environmental impacts are considered as part of a sensitivity analysis.


           hydrogen supply, …
    1 MJ/120 MJ/kg/thermal or electric
          eff.*allocation factor


           hydrogen supply, …
         ((1+storage loss)*(1+use loss)-
               1)*hydrogen input


      fuel cell production, stack
    solid oxide, 125kW electrical,                                                              electricity, from residential
                 future                                                                               heating system
        1/(Power [kW] * Annual op. [hours] *
                                                                                                             1 MJ
    lifetime [years] * 3.6 [MJ/kWh]) * allocation     heat, residential, by
                         factor
                                                    conversion of hydrogen
                                                                                                        Water (to air)
    maintenance, solid oxide fuel
                                                      using fuel cell SOFC,                        1 MJ/120 MJ/thermal eff. * 9 kg

    cell 125kW electrical, future                     allocated by exergy
        1/(Power [kW] * Annual op. [hours] *
    lifetime [years] * 3.6 [MJ/kWh]) * allocation
                                                                                                     Hydrogen (to air)
                         factor                                                                                losses

                If delivery by truck

        high pressure hydrogen
              storage tank
      2.08e-4 unit * (hydrogen input + losses)



                     others

Figure 31 Schematic mass and energy balance for the heat supply via hydrogen conversion in a PEM fuel cell
system. Red numbers represent material, energy, or infrastructure input amounts. Blue numbers represent
incoming and outgoing biosphere flows. The green number is the amount of the reference flow of the process.




                                                                85
     Sacchi, R. and Bauer, C. (2024) LCA of Power-to-X processes and applications in the residential sector.
                                          PSI, Villigen, Switzerland.



          hydrogen supply, …
    1 kWh/33.33 kWh/kg/thermal or
      electric eff.*allocation factor


          hydrogen supply, …
       ((1+storage loss)*(1+use loss)-
             1)*hydrogen input


     fuel cell production, stack
   solid oxide, 125kW electrical,                                                                             electricity, from residential
                future                                                                                              heating system
       1/(Power [kW] * Annual op. [hours] *
   lifetime [years] * 1 [kWh/kWh]) * allocation                                                                           1 kWh
                        factor
                                                              electricity, residential, by
                                                               conversion of hydrogen                                 Water (to air)
   maintenance, solid oxide fuel                                 using fuel cell SOFC,                         1 kWh/33.33 kWh/thermal eff. * 9 kg

   cell 125kW electrical, future                                 allocated by exergy
       1/(Power [kW] * Annual op. [hours] *
   lifetime [years] * 1 [kWh/kWh]) * allocation
                                                                                                                    Hydrogen (to air)
                        factor                                                                                               losses


               If delivery by truck

       high pressure hydrogen
             storage tank
     2.08e-4 unit * (hydrogen input + losses)



                    others

Figure 32 Schematic mass and energy balance for the electricity supply via hydrogen conversion in a SOFC fuel
cell system. Red numbers represent material, energy, or infrastructure input amounts. Blue numbers represent
incoming and outgoing biosphere flows. The green number is the amount of the reference flow of the process.

Referring to Section 7.3 of (Rolf Frischknecht et al. 2007), the pedigree matrix factors
described in Table 54 for uncertainty estimation are considered.


Table 56 Uncertainty factors used for uncertainty estimation. Note that the scores apply to all data points of the
dataset. In addition, a flow-specific basic uncertainty factor is applied (see Table 7.2 of (Frischknecht et al. 2007)).

                            Reliability               Completeness       Temporal          Geographical        Further                    Sample size
                                                                         correlation       correlation         technological
                                                                                                               correlation

 H2 in SOFC                                       1                  5                 1                  2                           3              5



Additionally, basic uncertainty factors listed in Table 7.2 of (Rolf Frischknecht et al. 2007) are
applied to the relevant technosphere and biosphere flows.


3 Synthetic natural gas (SNG)
Synthetic natural gas (SNG), or substitute natural gas, can be produced from fossil fuels such
as coal and oil or renewable sources such as biomass. The production of SNG involves a
process called gasification followed by methanation.
Here is a simplified description of the process:
Gasification: The feedstock (e.g., biomass) is heated in a low-oxygen environment, which
causes it to break down into a mixture of gases, primarily carbon monoxide (CO) and hydrogen
(H2). This mixture is often referred to as “syngas” or synthetic gas.
Cleaning and Purification: The syngas is then purified to remove contaminants and
unwanted gases. The goal is to get a pure mixture of CO and H2.


                                                                             86
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 MJ.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
