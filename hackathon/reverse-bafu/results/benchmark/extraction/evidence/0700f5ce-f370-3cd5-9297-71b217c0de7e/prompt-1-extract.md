You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Heat, residential, by transfer of geothermal heat using ground source heat pump using electricity from grid` [CH], reference unit 1 MJ, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~13 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: energy, obsolete / heat, obsolete\heat pumps, obsolete\transformation
- includedProcesses: —
- technology: —
- generalComment: This dataset represents the supply of 1 megajoule of heat in a residence, by transfer of geothermal heat in a ground source heat pump.  The electricity is from grid. Heat conversion efficiency [% LHV input]: 390%. LHV [MJ/kg]: 3.6. Market price [Euro/MJ]: 0.03. Distribution loss [% output]: 0%. Storage loss [% output]: 0%. Synthesis efficiency [% LHV input]: 0%. Hydrogen production efficiency [% LHV input]: 0. Grid loss [%]: 0.06. CO2 biogenic share [%]: 0%. Power [kW]: 10. Lifetime [years]: 20. Annual operation [hours]: 2100. : .  For more information, refer to: Sacchi, R., Bauer, C. LCA of Power-to-X processes and applications in the residential sector. Paul Scherrer Institut, 2023. Source: Sacchi, R., Bauer, C. LCA of Power-to-X processes and applications in the residential sector. Paul Scherrer Institut, 2023.

 UUID: 0700f5ce-f370-3cd5-9297-71b217c0de7e
- source cited in the metadata: Sacchi R. | 2024 | 2024 - LCA power-to-X in residential sector - Sacchi
- time period: 2024-01-2024-01

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 MJ):
- Energy, Geothermal, Converted: 1 megajoule (natural resource)

## Report excerpt

Source file: `report-p131-132.txt` (SHA-256 c1ddf27731b3daeb18941a4a21a8d70842ebd036edd758f855fc37dce9a0f256), pages 131-132 of `2024 - LCA power-to-X in residential sector - Sacchi.pdf`.

```
Sacchi, R. and Bauer, C. (2024) LCA of Power-to-X processes and applications in the residential sector.
                                         PSI, Villigen, Switzerland.




Figure 60 Life-cycle overall environmental impacts per kilogram of methanol produced according to the ecological
scarcity method. “Biomass” = methanol produced from wood chips. “NG” = methanol produced from natural gas.
“PEM” = Proton Exchange Membrane. “biological” = biological methanation. “chemical” = electrochemical
methanation. “grid” = Swiss grid electricity. “DAC” = atmospheric carbon dioxide captured by Direct Air Capture.
“Cement” = carbon dioxide, captured at cement plant. “Cement + HR” = carbon dioxide captured at cement plant
with use of recovered process heat. “MSWI” = carbon dioxide, captured at municipal solid waste incineration plant.
“MSWI + HR” = carbon dioxide captured at municipal solid waste incineration plant with use of recovered process
heat. “100:0” = carbon dioxide emissions allocated to emitter. «50:50 » = carbon dioxide emissions allocated
equally between emitter and fuel producer. «0:100» = carbon dioxide emissions allocated entirely to fuel producer.
“CC” = carbon dioxide capture/sourcing. “CCS” = carbon dioxide capture and storage. “EoL” = End-of-Life. “LNG”
= liquefied natural gas. “NG” = compressed natural gas. “grid” = electricity from the Swiss grid. “Hydro” = Swiss
hydropower. “PV” = Swiss solar photovoltaic power. “RES” = mix of Swiss-based renewable energy sources. “Wind”
= wind power. “Hydro” = Swiss hydropower. “PV” = Swiss solar photovoltaic power. “RES” = mix of Swiss-based
renewable energy sources. “Wind” = wind power. “Wind (MA)” = Morocco-based autonomous wind power-based
hydrogen production. “PV (MA)” = Morocco-based autonomous solar power-based hydrogen production. “PV +
Wind (MA)” = Morocco-based autonomous wind and solar power-based hydrogen production. These results do not
include the combustion of the fuel.


5.1.5 Heat supply
This section shows the life-cycle impacts of heat supply options. These options are compared
to reference technologies, which specifications are described in Table 83.
Table 83 Main specifications for the reference technologies for heating

 Name         (in   Dataset name               Description                Energy carrier       Power   Efficiency   Source
 figures)                                                                                      [kW]    [%, LHV]
 HP - grid          heat, at heat pump, air-   Air-water heat pump,       Electricity from        15       440%     (Kägi et al.
                    water,       15kW,  CH     installed in a new         the Swiss grid.                   (CoP    2021)
                    electricity,    in new     building in Switzerland.                                    ~4.4)
                    building/MJ/CH
 HP -        RES    heat, at heat pump, air-   Air-water heat pump,       Electricity from a      15       440%
 (CH)               water, 15kW, certified     installed in a new         mix of renewable                  (CoP
                    electricity,  in   new     building in Switzerland.   energy sources.                  ~4.4)
                    building/MJ/CH
 Boiler        –    heat, softwood chips       Wood chips furnace, in     Wood chips, from     50 kW          84%
 Wood               from forest, at furnace    Switzerland                soft wood.
                    50kW/MJ/CH
 Boiler     -       heat, biomethane, at       Home boiler fed with       Biomethane.          15 kW       109%
 Biomethane         boiler cond. modulating    biomethane,       in
                    15kW/MJ/CH                 Switzerland.
 Boiler - NG        heat, natural gas, at      Home boiler fed with       Natural gas.         15 kW   109%
                    boiler      condensing     natural      gas, in
                    modulating 15kW/CH         Switzerland.




                                                              131
    Sacchi, R. and Bauer, C. (2024) LCA of Power-to-X processes and applications in the residential sector.
                                         PSI, Villigen, Switzerland.



Figure 61 shows the life-cycle Global Warming Potential impacts of heat supply options using
hydrogen, SNG, and methanol, in kilogram of CO2-eq. per “megajoule heat output”
(representing the functional unit).
Results are shown alongside those of heat from a 15 kW air-water heat pump operated with
either average electricity or renewable power from the Swiss grid in a new building (“HP”,
represented by the dataset heat pump, air-water, 15 kW, in new building from the UVEK:2022
database), heat from a boiler fed with wood chips (“Wood”, represented by the dataset heat,
softwood chips from forest, at furnace 50kW in the UVEK:2022 database), heat from a 15 kW
biomethane boiler (“biomethane”, represented by the dataset heat, biomethane, at boiler
condensing modulating 15kW from the UVEK:2022 database) as well as heat from a 15 kW
natural gas-fed boiler (“boiler – NG”, represented by the dataset heat, natural gas, at boiler
condensing modulating 15 kW from the UVEK:2022 database).
Among all heat supply options compared, the heat pump using Swiss renewable power causes
the lowest climate impacts as well as the lowest overall environmental impacts, as it uses
renewable power in the most efficient way. Among the non-conventional heat supply pathways
modeled in this work and in case environmental burdens of joint heat and electricity generation
are allocated according to exergy content of these products (as per default in this work),
hydrogen-based CHP and fuel cell options score consistently better (i.e., cause lower GHG
emissions and overall environmental burdens) than those using a boiler due to the exergy
allocation, which assigns a relatively high share of burdens to the co-produced electricity.
Methanol and synthetic gas options score consistently worse. Compared to using natural gas
in a 15-kW condensing boiler, most hydrogen-based options perform better, except for SMR-
based heat supply from a boiler. Finally, the heat options using electrolytic hydrogen from the
Moroccan-based autonomous plant (representing a “best case” in terms of renewable yields
and thus environmental burdens) or those using SMR-based hydrogen with CCS also show
higher impacts than the associated reference technology (heat pump operated with
renewables).
It is important to note the penalty when supplying the hydrogen by truck (Figure 61):
accentuated gas losses and the requirements in on-site storage lead to a 20-25% increase in
greenhouse gas emissions compared to pipeline hydrogen transport.
Applying a global warming characterization factor for hydrogen emissions due to leakage of
11.6 kg CO2-eq./kg H2 for a 100-year time horizon (GWP100), as suggested by (Sand et al.
2023), would increase results related to impacts on climate change by 2-4%. This is insufficient
to change the ordinal rank of the options presented above.




                                                     132
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
