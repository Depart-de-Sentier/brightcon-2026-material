You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: electricity, medium voltage, at grid  (input)
  quote:      electricity, medium voltage, at grid                                 CH kWh                                                                                             2.40E-03                1    2 own assumption
  search: electricity medium voltage at grid
  candidates:
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import DE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import FR, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import IT, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import ENTSO, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
- item: welding, arc, steel  (input)
  quote:      welding, arc, steel                                                  RER m                                                                                              8.00E-03                1    3 own assumption
  search: welding arc steel
  candidates:
    - Welding, arc, steel [RER] (meter, 8 inputs)
    - Welding, gas, steel [RER] (meter, 5 inputs)
    - Welding, arc, aluminium [RER] (meter, 6 inputs)
- item: chromium steel 18/8, at plant  (input)
  quote:      chromium steel 18/8, at plant                                        RER kg             5.00E+03              1                             3 own assumption            1.57E+01                1 1.15 variation in lenght of canister
  search: chromium steel 18/8 at plant
  candidates:
    - Sink, chromium steel, at plant [CH] (unit, 21 inputs)
    - Kitchen worktop, chromium steel, high-end, at plant [CH] (square meter, 8 inputs)
    - Kitchen worktop, chromium steel, standard, at plant [CH] (square meter, 11 inputs)
    - Chromium steel sheet 18/8, recycling share 70 %, with resource correction, at plant [CH] (square meter, 3 inputs)
    - Chromium steel 18/8, at plant [RER] (kilogram, 3 inputs)
    - Steel, electric, chromium steel 18/8, at plant [RER] (kilogram, 16 inputs)
    - Steel, converter, chromium steel 18/8, at plant [RER] (kilogram, 18 inputs)
    - Tin plated chromium steel sheet, 2 mm, at plant [RER] (square meter, 3 inputs)
- item: transport, lorry 28t  (input)
  quote:      transport, lorry 28t                                                 CH tkm             2.68E+04              1                             3 own assumption            7.80E-01                1              2.1 standard for transports
  search: transport lorry 28t
  candidates:
    - Disposal, lorry 28t [CH] (unit, 6 inputs)
    - Maintenance, lorry 28t [CH] (unit, 11 inputs)
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - xxx Operation, lorry >28t, fleet average [CH] (kilometer, 1 inputs)
    - xxx Operation, lorry 20-28t, fleet average [CH] (kilometer, 1 inputs)
    - Operation, lorry 28t, rape methyl ester 100% [CH] (kilometer, 1 inputs)
    - Transport, municipal waste collection, lorry 21t [CH] (ton kilometer, 5 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)
- item: transport, lorry 32t  (input)
  quote:      transport, lorry 32t                                                 RER tkm                                                                                            1.23E+00                1              2.1 standard for transports
  search: transport lorry 32t
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, long haul [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, long haul [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2020, EURO-VI, long haul [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, fleet average, long haul [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2002, EURO-III, long haul [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, urban delivery [CH] (ton kilometer, 11 inputs)
- item: transport, freight, rail  (input)
  quote:      transport, freight, rail                                             RER tkm            3.30E+04              1                             3 own assumption            9.40E+00                1              2.1 standard for transports
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
- item: nuclear spent fuel conditioning plant  (input)
  quote:      nuclear spent fuel conditioning plant                                CH unit                                                                                             5.56E-07               1    2 uncertainty in the scenario
  search: nuclear spent fuel conditioning plant
  candidates:
    - Nuclear spent fuel conditioning plant [CH] (unit, 7 inputs)
    - Nuclear spent fuel, in conditioning, at plant [CH] (kilogram, 8 inputs)
    - Nuclear spent fuel conditioning plant [CN] (unit, 7 inputs)
    - Nuclear spent fuel, in conditioning, at plant [CN] (kilogram, 7 inputs)
    - Nuclear spent fuel reprocessing plant [RER] (unit, 16 inputs)
    - Nuclear spent fuel, in reprocessing, at plant [RER] (kilogram, 23 inputs)
- item: radioactive waste, in final repository for nuclear waste SF, HLW, and ILW  (input)
  quote:      and ILW                                                           CH            m3                                                                                       2.30E-03               1 1.15 metal
  search: radioactive waste in final repository for nuclear waste SF HLW ILW
  candidates:
    - Radioactive waste, in final repository for nuclear waste SF, HLW, and ILW [CH] (cubic meter, 9 inputs)
    - Final repository for nuclear waste SF, HLW, and ILW [CH] (unit, 10 inputs)
    - Radioactive waste, in interim storage, for final repository SF, HLW, and ILW [CH] (cubic meter, 3 inputs)

Return only the JSON object described by the schema.
