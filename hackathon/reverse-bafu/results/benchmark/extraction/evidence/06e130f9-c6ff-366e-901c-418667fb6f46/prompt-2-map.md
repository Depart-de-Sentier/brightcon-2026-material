You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (GLO), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Ammoniak  (input)
  quote:                              Ammoniak                       kg/kg NOx                 0.3
  search: ammonia liquid at regional storehouse
  candidates:
    - Ammonia, liquid, at regional storehouse [RER] (kilogram, 4 inputs)
    - Ammonia, liquid, at regional storehouse [CH] (kilogram, 4 inputs)
- item: TiO2  (input)
  quote:                              TiO2                           kg/kg NOx                0.025
  search: titanium dioxide production mix at plant
  candidates:
    - Titanium dioxide, production mix, at plant [RER] (kilogram, 2 inputs)
- item: Transport Bahn  (input)
  quote:                              Transport Bahn                tkm/kg NOx                 0.06
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
- item: Sonderabfall in Deponie  (input)
  quote:                              Sonderabfall in Deponie*       kg/kg NOx                0.025
  search: disposal hazardous waste underground deposit
  candidates:
    - Disposal, hazardous waste, 0% water, to underground deposit [DE] (kilogram, 13 inputs)
    - Disposal, waste, silicon wafer production, 0% water, to underground deposit [DE] (kilogram, 12 inputs)
- item: Ammonia  (emission to air)
  quote:                              NH3 p (in Luft)                kg/kg NOx                0.003
  candidates (flow name [compartment]):
    - Ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
