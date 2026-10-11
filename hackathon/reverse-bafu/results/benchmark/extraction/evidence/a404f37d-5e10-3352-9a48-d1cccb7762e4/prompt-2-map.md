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
  quote:                   electricity, medium voltage, production CH, at grid   CH              0 kWh                                                      1.10E+0             1            1.05
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
- item: sulphur hexafluoride, liquid, at plant  (input)
  quote:                   sulphur hexafluoride, liquid, at plant                RER             0             kg                          3.73E-8          2.19E-9             1            1.08           (1,1,2,1,1,3); based on emission data
  search: sulphur hexafluoride liquid at plant
  candidates:
    - Sulphur hexafluoride, liquid, at plant [RER] (kilogram, 5 inputs)
    - Sulphuric acid, liquid, at plant [RER] (kilogram, 7 inputs)
    - Sulphur dioxide, liquid, at plant [RER] (kilogram, 4 inputs)
- item: distribution network, electricity, low voltage  (input)
  quote:                   distribution network, electricity, low voltage        CH              1             km                                           2.94E-7             1            3.15
  search: distribution network electricity low voltage
  candidates:
    - Distribution network, electricity, low voltage [CH] (kilometer, 20 inputs)
- item: Heat, waste  (emission to soil)
  quote: emission soil,                                                                                                                                                                                     (4,1,3,1,1,5); estimations based on
  candidates (flow name [compartment]):
    - Waste Heat  [soil] (megajoule, ef-3.1-biosphere)
    - Waste Heat  [air] (megajoule, ef-3.1-biosphere)
    - Waste Heat  [water] (megajoule, ef-3.1-biosphere)
    - Heat, waste  [emissions to water / groundwater, long-term] (megajoule, bafu-2026-residual)
    - Energy, waste heat, air  [resources / in air] (megajoule, bafu-2026-residual)
    - Waste water/m3  [emissions to water / unspecified] (cubic meter, bafu-2026-residual)
    - Waste water  [emissions to water / ocean] (kilogram, bafu-2026-residual)
    - Waste water  [emissions to water / river] (kilogram, bafu-2026-residual)
- item: Heat, waste  (emission to air)
  quote: emission air,                                                                                                                                                                                      (4,1,3,1,1,5); estimations based on
  candidates (flow name [compartment]):
    - Waste Heat  [air] (megajoule, ef-3.1-biosphere)
    - Energy, waste heat, air  [resources / in air] (megajoule, bafu-2026-residual)
    - Waste Heat  [soil] (megajoule, ef-3.1-biosphere)
    - Waste Heat  [water] (megajoule, ef-3.1-biosphere)
    - Heat, waste  [emissions to water / groundwater, long-term] (megajoule, bafu-2026-residual)
    - Waste water/m3  [emissions to water / unspecified] (cubic meter, bafu-2026-residual)
    - Waste water  [emissions to water / ocean] (kilogram, bafu-2026-residual)
    - Waste water  [emissions to water / river] (kilogram, bafu-2026-residual)
- item: Sulfur hexafluoride  (emission to air)
  quote:                   Sulfur hexafluoride                                       -            -            kg                          3.73E-8          2.19E-9             1            1.51           (1,1,2,1,1,3); national statistics
  candidates (flow name [compartment]):
    - Sulfur Hexafluoride  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur hexafluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur hexafluoride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Sulfur hexafluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sulfur  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
    - Sulfuric acid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
