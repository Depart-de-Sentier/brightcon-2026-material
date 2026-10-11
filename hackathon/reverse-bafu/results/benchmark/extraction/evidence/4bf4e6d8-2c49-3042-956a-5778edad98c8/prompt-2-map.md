You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: natural gas, burned in industrial furnace low-NOx >100kW  (input)
  quote: technosphere natural gas, burned in industrial furnace low-NOx >100kW RER        0             MJ        1.33E+0        1   1.50     (5,na,1,1,1,na); Estimation 20% of melting energy
  search: natural gas burned industrial furnace low-NOx
  candidates:
    - xxx Heat, natural gas, at industrial furnace low-NOx >100kW [RER] (megajoule, 1 inputs)
- item: flat glass, uncoated, at plant  (input)
  quote:              flat glass, uncoated, at plant                           RER        0             kg        1.20E-1        1   1.12     (3,3,1,1,1,na); Estimation 12% glass losses
  search: flat glass uncoated at plant
  candidates:
    - Flat glass, uncoated, at plant [RER] (kilogram, 15 inputs)
    - Flat glass plant [RER] (unit, 4 inputs)
    - Flat glass, coated, at plant [RER] (kilogram, 28 inputs)
    - Photovoltaic panel for PVT, single-Si, without flat glass, at plant [RER] (square meter, 32 inputs)
    - Photovoltaic panel for PVT, single-Si, without flat glass, at plant [APAC] (square meter, 32 inputs)
    - Photovoltaic panel for PVT, single-Si, without flat glass, at plant [CN] (square meter, 32 inputs)
- item: transport, lorry 32t  (input)
  quote:              transport, lorry 32t                                   RER           0            tkm       1.12E-1        1   2.09
  search: transport lorry 32t
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2020, EURO-VI, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2002, EURO-III, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, urban delivery [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, urban delivery [RER] (ton kilometer, 11 inputs)
- item: transport, freight, rail  (input)
  quote:              transport, freight, rail                               RER          0             tkm       2.24E-1        1   2.09
  search: transport freight rail
  candidates:
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [RER] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting, Betrieb [CH] (ton kilometer, 2 inputs)
    - Transport, freight, rail, electricity with shunting, Fahrzeug [CH] (ton kilometer, 5 inputs)

Return only the JSON object described by the schema.
