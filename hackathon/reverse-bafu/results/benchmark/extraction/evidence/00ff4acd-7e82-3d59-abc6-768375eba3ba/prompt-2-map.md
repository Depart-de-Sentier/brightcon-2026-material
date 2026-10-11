You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: ferromanganese, high-coal, 74.5% Mn, at regional storage  (input)
  quote: f erromanganes                                                                                                                                                                                                                                    (5,5,1,1,1,5,4);
  search: ferromanganese high-coal 74.5% Mn at regional storage
  candidates:
    - Ferromanganese, high-coal, 74.5% Mn, at regional storage [RER] (kilogram, 13 inputs)
- item: manganese, concentrate, at beneficiation  (input)
  quote: concentrate f or                                                                                      metals               extraction        No         GLO         concentrate, at        9.83E-01   kg     Calculation       1     1.62
  search: manganese concentrate at beneficiation
  candidates:
    - Manganese concentrate, at beneficiation [GLO] (kilogram, 11 inputs)
    - Copper concentrate, at beneficiation [RER] (kilogram, 14 inputs)
    - Lead concentrate, at beneficiation [GLO] (kilogram, 14 inputs)
    - Zinc concentrate, at beneficiation [GLO] (kilogram, 14 inputs)
    - Copper concentrate, at beneficiation [GLO] (kilogram, 14 inputs)
    - Chromite, ore concentrate, at beneficiation [GLO] (kilogram, 11 inputs)
    - Copper concentrate, at beneficiation [ID] (kilogram, 14 inputs)
    - Copper concentrate, at beneficiation [RAS] (kilogram, 14 inputs)
- item: electricity, medium voltage, production UCTE, at grid  (input)
  quote: Energy f or
  search: electricity medium voltage production UCTE at grid
  candidates:
    - Electricity, medium voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from hard coal, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from natural gas, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - xxx Electricity, medium voltage, production UCTE, at grid [UCTE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from oil, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, high voltage, production from oil, UCTE at grid [CH] (kilowatt hour, 2 inputs)
- item: non-ferrous metal, smelter  (input)
  quote: Inf rastructure,                                                                                                                                                     non-f errous metal,
  search: non-ferrous metal smelter
  candidates:
    - Non-ferrous metal smelter [GLO] (unit, 5 inputs)
    - Disposal, non-ferrous metals, as building waste [CH] (kilogram, 3 inputs)
    - Non-ferrous metal mine, surface [GLO] (unit, 4 inputs)
    - Non-ferrous metal mine, underground [GLO] (unit, 4 inputs)
- item: Heat, waste  (emission to air)
  quote:                                                w aste heat                                            air                                                           Heat, w aste           9.47E+00   MJ                       1     1.16 (3,2,3,1,1,2,13)
  candidates (flow name [compartment]):
    - Waste Heat  [air] (megajoule, ef-3.1-biosphere)
    - Energy, waste heat, air  [resources / in air] (megajoule, bafu-2026-residual)
    - Waste Heat  [soil] (megajoule, ef-3.1-biosphere)
    - Waste Heat  [water] (megajoule, ef-3.1-biosphere)
    - Heat, waste  [emissions to water / groundwater, long-term] (megajoule, bafu-2026-residual)
    - Waste water/m3  [emissions to water / unspecified] (cubic meter, bafu-2026-residual)
    - Waste water  [emissions to water / ocean] (kilogram, bafu-2026-residual)
    - Waste water  [emissions to water / river] (kilogram, bafu-2026-residual)

Return only the JSON object described by the schema.
