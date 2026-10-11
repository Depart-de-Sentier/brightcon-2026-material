You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: steel, electric, un- and low-alloyed, at plant  (input)
  quote: steel, electric, un- and low-alloyed, at plant, RER, [kg]                                 2.23E+0      2.72E+0      3.17E+0      3.66E+0                                                                           4.61E+0                        5.55E+0                  1.22, (2,3,1,1,1,5)
  search: steel electric un- and low-alloyed at plant
  candidates:
    - Steel, electric, un- and low-alloyed, at plant [RER] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [DE] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [FR] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [IT] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [PL] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant [CH] (kilogram, 23 inputs)
    - Steel, electric, low-alloyed, at plant, best plants (min. values) [RER] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant, worst plants (max. values) [RER] (kilogram, 17 inputs)
- item: steel, converter, unalloyed, at plant  (input)
  quote: steel, converter, unalloyed, at plant, RER, [kg]                                          3.80E+0      4.63E+0      5.40E+0      6.24E+0                                                                           7.85E+0                        9.45E+0                  1.22, (2,3,1,1,1,5)
  search: steel converter unalloyed at plant
  candidates:
    - Steel, converter, unalloyed, at plant [RER] (kilogram, 26 inputs)
    - Steel, electric, unalloyed, at plant [CH] (kilogram, 40 inputs)
    - Reinforcing steel, converter, at plant [RER] (kilogram, 2 inputs)
    - Steel, converter, low-alloyed, at plant [RER] (kilogram, 21 inputs)
    - Steel, converter, chromium steel 18/8, at plant [RER] (kilogram, 18 inputs)
- item: steel, low-alloyed, at plant  (input)
  quote: steel, low-alloyed, at plant, RER, [kg]                                                    2.50E-1      2.50E-1      2.50E-1      2.50E-1                                                                           2.50E-1                        2.50E-1                 1.32, (4,4,1,1,1,5)
  search: steel low-alloyed at plant
  candidates:
    - Steel, electric, low-alloyed, at plant [CH] (kilogram, 23 inputs)
    - Steel, low-alloyed, at plant [RER] (kilogram, 3 inputs)
    - Steel, converter, low-alloyed, at plant [RER] (kilogram, 21 inputs)
    - Steel, electric, un- and low-alloyed, at plant [RER] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant, best plants (min. values) [RER] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant, worst plants (max. values) [RER] (kilogram, 17 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [DE] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [FR] (kilogram, 16 inputs)
- item: synthetic rubber, at plant  (input)
  quote: synthetic rubber, at plant, RER, [kg]                                                      5.00E-2      5.00E-2      5.00E-2      5.00E-2                                                                           5.00E-2                        5.00E-2                 1.32, (4,4,1,1,1,5)
  search: synthetic rubber at plant
  candidates:
    - Synthetic rubber, at plant [RER] (kilogram, 13 inputs)
    - Synthetic gas plant [CH] (unit, 12 inputs)
    - Methanol, from synthetic gas, at plant [CH] (kilogram, 12 inputs)
    - Synthetic gas, production mix, at plant [CH] (cubic meter, 2 inputs)
    - Flooring, from rubber granulate, at plant [CH] (square meter, 11 inputs)
    - Methane, 96 vol.-%, from synthetic gas, wood, at plant [CH] (cubic meter, 27 inputs)
    - Disposal, organic floor covering as construction waste, to sanitary landfill, synthetic rubber [CH] (kilogram, 2 inputs)
    - Disposal, organic floor covering as construction waste, to municipal waste incineration, synthetic rubber [CH] (kilogram, 2 inputs)
- item: sheet rolling, steel  (input)
  quote: sheet rolling, steel, RER, [kg]                                                           6.03E+0      7.35E+0      8.58E+0      9.91E+0                                                                           1.25E+1                        1.50E+1                  1.22, (2,3,1,1,1,5)
  search: sheet rolling steel
  candidates:
    - Sheet rolling, steel [RER] (kilogram, 24 inputs)
    - Sheet rolling, chromium steel [RER] (kilogram, 26 inputs)
    - Sheet rolling, electric steel [RER] (kilogram, 24 inputs)
    - Hot rolling, steel [CH] (kilogram, 20 inputs)
    - Hot rolling, electric steel [CH] (kilogram, 20 inputs)
    - Selective coating, stainless steel sheet, black chrome [CH] (square meter, 10 inputs)
    - Steel sheet, uncoated, recycling share 2000 (37% Rec.) [CH] (kilogram, 2 inputs)
    - Steel sheet, uncoated, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
- item: section bar rolling, steel  (input)
  quote: section bar rolling, steel, RER, [kg]                                                      2.50E-1     7.65E+0      8.88E+0      1.02E+1                                                                           1.28E+1                        1.53E+1                  1.32, (4,4,1,1,1,5)
  search: section bar rolling steel
  candidates:
    - Section bar rolling, steel [RER] (kilogram, 1 inputs)
- item: zinc coating, coils  (input)
  quote: zinc coating, coils, RER, [m2]                                                            1.24E+0      1.25E+0      1.26E+0      1.26E+0                                                                           1.27E+0                        1.27E+0                  1.22, (2,3,1,1,1,5)
  search: zinc coating coils
  candidates:
    - Zinc coating, coils [RER] (square meter, 17 inputs)
    - Zinc coating, pieces [RER] (square meter, 18 inputs)
    - Zinc coating for hydrogen pipeline [RER] (kilogram, 19 inputs)
    - Zinc coating, pieces, adjustment per um [RER] (square meter, 2 inputs)
- item: zinc coating, pieces  (input)
  quote: zinc coating, pieces, RER, [m2]                                                            2.13E-2      2.13E-2      2.13E-2      2.13E-2                                                                           2.13E-2                        2.13E-2                 1.32, (4,4,1,1,1,5)
  search: zinc coating pieces
  candidates:
    - Zinc coating, pieces [RER] (square meter, 18 inputs)
    - Zinc coating, pieces, adjustment per um [RER] (square meter, 2 inputs)
    - Zinc coating, coils [RER] (square meter, 17 inputs)
    - Zinc coating for hydrogen pipeline [RER] (kilogram, 19 inputs)
- item: zinc coating, pieces, adjustment per um  (input)
  quote: zinc coating, pieces, adjustment per um, RER, [m2]                                       -1.89E+1     -1.91E+1     -1.92E+1     -1.93E+1                                                                          -1.94E+1                       -1.95E+1                  1.22, (2,3,1,1,1,5)
  search: zinc coating pieces adjustment per um
  candidates:
    - Zinc coating, pieces, adjustment per um [RER] (square meter, 2 inputs)
- item: electricity, medium voltage, production UCTE, at grid  (input)
  quote: electricity, medium voltage, production UCTE, at grid, UCTE, [kWh]                        1.90E+0      2.30E+0      2.66E+0      3.06E+0                                                                           3.83E+0                        4.59E+0                  1.22, (2,3,1,1,1,5)
  search: electricity medium voltage production UCTE at grid
  candidates:
    - Electricity, medium voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from hard coal, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from natural gas, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - xxx Electricity, medium voltage, production UCTE, at grid [UCTE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from oil, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, high voltage, production from oil, UCTE at grid [CH] (kilowatt hour, 2 inputs)
    - Electricity, low voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
- item: metal working factory operation, average heat energy  (input)
  quote: section bar rolling, steel, RER, [kg]                                                      2.50E-1     7.65E+0      8.88E+0      1.02E+1                                                                           1.28E+1                        1.53E+1                  1.32, (4,4,1,1,1,5)
  search: metal working factory operation average heat energy
  candidates:
    - Metal working factory operation, average heat energy [RER] (kilogram, 9 inputs)
    - xx Metal working factory operation, heat energy from hard coal [RER] (kilogram, 7 inputs)
    - xx Metal working factory operation, heat energy from natural gas [RER] (kilogram, 7 inputs)
    - xx Metal working factory operation, heat energy from heavy fuel oil [RER] (kilogram, 7 inputs)
    - xx Metal working factory operation, heat energy from light fuel oil [RER] (kilogram, 7 inputs)
- item: metal working factory  (input)
  quote: metal working factory, RER, [unit]                                                         2.90E-9      3.51E-9      4.07E-9      4.67E-9                                                                           5.84E-9                        7.01E-9                 3.07, (2,4,2,1,3,4)
  search: metal working factory
  candidates:
    - Metal working factory [RER] (unit, 2 inputs)
    - Metal working factory operation, average heat energy [RER] (kilogram, 9 inputs)
    - xx Metal working factory operation, heat energy from hard coal [RER] (kilogram, 7 inputs)
    - xx Metal working factory operation, heat energy from natural gas [RER] (kilogram, 7 inputs)
    - xx Metal working factory operation, heat energy from heavy fuel oil [RER] (kilogram, 7 inputs)
    - xx Metal working factory operation, heat energy from light fuel oil [RER] (kilogram, 7 inputs)
    - Metal working machine, unspecified, at plant [RER] (kilogram, 30 inputs)
    - Metal product manufacturing, average metal working [RER] (kilogram, 8 inputs)
- item: transport, freight, rail  (input)
  quote: electricity, medium voltage, production UCTE, at grid, UCTE, [kWh]                        1.90E+0      2.30E+0      2.66E+0      3.06E+0                                                                           3.83E+0                        4.59E+0                  1.22, (2,3,1,1,1,5)
  search: transport freight rail
  candidates:
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting, Betrieb [CH] (ton kilometer, 2 inputs)
    - Transport, freight, rail, electricity with shunting, Fahrzeug [CH] (ton kilometer, 5 inputs)
    - Transport, freight, rail, electricity with shunting, Infrastruktur [CH] (ton kilometer, 3 inputs)
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
- item: transport, lorry 20-28t, fleet average  (input)
  quote: transport, lorry 20-28t, fleet average, CH, [tkm]                                          3.16E-1      3.83E-1      4.44E-1      5.10E-1                                                                           6.38E-1                        7.65E-1                 2.14, (4,5,1,1,1,5)
  search: transport lorry 20-28t fleet average
  candidates:
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - xxx Operation, lorry >28t, fleet average [CH] (kilometer, 1 inputs)
    - xxx Operation, lorry 20-28t, fleet average [CH] (kilometer, 1 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [CH] (ton kilometer, 20 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [CH] (ton kilometer, 11 inputs)

Return only the JSON object described by the schema.
