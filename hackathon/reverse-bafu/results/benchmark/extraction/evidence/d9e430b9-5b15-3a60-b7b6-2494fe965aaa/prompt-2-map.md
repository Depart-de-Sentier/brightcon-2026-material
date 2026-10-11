You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (BE), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Natural Gas  (resource to resources)
  quote: - Natural Gas: 35.98 megajoule (Resources Resources from ground)
  candidates (flow name [compartment]):
    - Natural Gas  [Resources / Resources from ground] (megajoule, ef-3.1-biosphere)
    - Gasoline, Natural  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Gasoline, Natural  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Gasoline, Natural  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - gasoline, natural  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - gasoline, natural  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Natural Gas Condensates (petroleum)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Natural Gas Condensates (petroleum)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Ground Water  (resource to resources)
  quote: - Ground Water: 0.0002558 cubic meter (Resources Resources from water)
  candidates (flow name [compartment]):
    - Ground Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - lake water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - river water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water To Cooling  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water to turbine  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water, salt, sole  [resources / in water] (cubic meter, bafu-2026-residual)
    - Water, salt, ocean  [resources / in water] (cubic meter, bafu-2026-residual)
- item: Water  (resource to resources)
  quote: - Water: 3.023e-05 cubic meter (Resources Resources from water)
  candidates (flow name [compartment]):
    - Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - lake water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - river water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Ground Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water To Cooling  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water to turbine  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water, salt, sole  [resources / in water] (cubic meter, bafu-2026-residual)
    - Water, salt, ocean  [resources / in water] (cubic meter, bafu-2026-residual)

Return only the JSON object described by the schema.
