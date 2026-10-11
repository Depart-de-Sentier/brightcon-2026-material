You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: hydrogen supply, by pipeline  (input)
  quote:     1 MJ/120 MJ/kg/thermal or electric
  search: hydrogen gaseous at consumer
  candidates:
    - Hydrogen, gaseous, 25 bar, from electrolysis [CH] (kilogram, 7 inputs)
    - Hydrogen production, gaseous, 100 bar, from methane pyrolysis [CH] (kilogram, 12 inputs)
    - Hydrogen, gaseous, 700 bar, from SMR of NG, at fuelling station [CH] (kilogram, 4 inputs)
    - Hydrogen, gaseous, 700 bar, from electrolysis, at fuelling station [CH] (kilogram, 4 inputs)
    - Hydrogen production, gaseous, 100 bar, from pyrolysis of liquefied natural gas [CH] (kilogram, 12 inputs)
    - Hydrogen, gaseous, 25 bar, from electrolysis, from label-certified electricity [CH] (kilogram, 7 inputs)
    - Hydrogen production, gaseous, 1 bar, from SOEC electrolysis, from grid electricity [CH] (kilogram, 6 inputs)
    - Hydrogen production, gaseous, 20 bar, from AEC electrolysis, from grid electricity [CH] (kilogram, 9 inputs)
- item: fuel cell production, stack solid oxide, 125kW electrical, future  (input)
  quote:       fuel cell production, stack
  search: fuel cell stack solid oxide 125kW
  candidates:
    - (no candidate found)
- item: maintenance, solid oxide fuel cell 125kW electrical, future  (input)
  quote:     maintenance, solid oxide fuel
  search: maintenance solid oxide fuel cell 125kW
  candidates:
    - (no candidate found)
- item: Water  (emission to air)
  quote:                                                       using fuel cell SOFC,                        1 MJ/120 MJ/thermal eff. * 9 kg
  candidates (flow name [compartment]):
    - Water  [air] (cubic meter, ef-3.1-biosphere)
    - sea water  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Green Water  [air] (kilogram, ef-3.1-biosphere)
    - Water Vapour  [air] (kilogram, ef-3.1-biosphere)
    - Water, In Air  [air] (kilogram, ef-3.1-biosphere)
    - Water (evapotranspiration)  [air] (kilogram, ef-3.1-biosphere)
    - Raffinates (petroleum), Catalytic Reformer Ethylene Glycol-water Countercurrent Exts.  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Reaction Mass Of Potassium Didodecylphosphate And Dipotassium Dodecylphosphate And Water  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
