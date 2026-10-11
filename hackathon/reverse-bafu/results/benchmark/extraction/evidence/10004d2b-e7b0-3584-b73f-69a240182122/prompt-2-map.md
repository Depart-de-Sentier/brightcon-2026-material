You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (IN), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: electricity, low voltage, at grid  (input)
  quote:  Hessian for textile       18 %        ∅ 1250 MJ/t                  9.4 kg/t batching oil    Transport 250 km local
  search: electricity low voltage at grid
  candidates:
    - Electricity, low voltage, at grid [IN] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production IN, at grid [IN] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import DE, at grid [CH] (kilowatt hour, 3 inputs)
- item: batching oil  (input)
  quote:  Hessian for textile       18 %        ∅ 1250 MJ/t                  9.4 kg/t batching oil    Transport 250 km local
  search: vegetable oil at plant
  candidates:
    - Vegetable oil esterification plant [CH] (unit, 5 inputs)
    - Vegetable oil, from waste cooking oil, at plant [CH] (kilogram, 10 inputs)
    - Vegetable oil methyl ester, at esterification plant [CH] (kilogram, 10 inputs)
    - Vegetable oil, from waste cooking oil, at plant [FR] (kilogram, 10 inputs)
    - Vegetable oil methyl ester, at esterification plant [FR] (kilogram, 10 inputs)
    - Glycerine, from vegetable oil, at esterification plant [FR] (kilogram, 10 inputs)
    - Soya oil, at plant [RER] (kilogram, 10 inputs)
    - Oil power plant 500MW [RER] (unit, 19 inputs)
- item: transport, lorry  (input)
  quote:  Hessian for textile       18 %        ∅ 1250 MJ/t                  9.4 kg/t batching oil    Transport 250 km local
  search: transport lorry
  candidates:
    - Transport, freight, lorry, fleet average [RER] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 3.5t-7.5t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, diesel, fleet average, urban delivery [RER] (ton kilometer, 12 inputs)

Return only the JSON object described by the schema.
