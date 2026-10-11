You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Energy, Geothermal, Converted  (resource to resources)
  quote: - Energy, Geothermal, Converted: 1 megajoule (natural resource)
  candidates (flow name [compartment]):
    - Energy, Geothermal, Converted  [natural resource] (megajoule, ef-3.1-biosphere)
    - Energy, Solar, Converted  [natural resource] (megajoule, ef-3.1-biosphere)
    - Energy, Kinetic (in Wind), Converted  [natural resource] (megajoule, ef-3.1-biosphere)
    - Energy, Potential (in Hydropower Reservoir), Converted  [natural resource] (megajoule, ef-3.1-biosphere)
- item: electricity, low voltage, at grid  (input)
  quote: - generalComment: This dataset represents the supply of 1 megajoule of heat in a residence, by transfer of geothermal heat in a ground source heat pump.  The electricity is from grid. Heat conversion efficiency [% LHV input]: 390%.
  search: electricity low voltage at grid
  candidates:
    - Electricity, low voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import DE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import FR, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import IT, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import ENTSO, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)

Return only the JSON object described by the schema.
