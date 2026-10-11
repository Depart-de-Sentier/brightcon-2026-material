You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (GLO), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Diesel, burned in diesel-electric generating set  (input)
  quote:                                           electric generating set“ (Wirkungsgrad: 36 %) bilanziert, der Verbrauch an fossilen Energieträgern für ther-
  search: diesel burned in diesel-electric generating set
  candidates:
    - Diesel, burned in diesel-electric generating set [GLO] (megajoule, 4 inputs)
    - Diesel, burned in diesel-electric generating set, at extraction site [GLO] (megajoule, 4 inputs)
    - Diesel-electric generating set production 10MW [RER] (unit, 5 inputs)
- item: Heavy fuel oil, burned in industrial furnace 1MW, non-modulating  (input)
  quote:                                           electric generating set“ (Wirkungsgrad: 36 %) bilanziert, der Verbrauch an fossilen Energieträgern für ther-
  search: heavy fuel oil burned in industrial furnace 1MW non-modulating
  candidates:
    - Heavy fuel oil, burned in industrial furnace 1MW, non-modulating [RER] (megajoule, 5 inputs)
    - Heavy fuel oil, burned in industrial furnace 1MW, non-modulating [CH] (megajoule, 5 inputs)
    - Light fuel oil, burned in industrial furnace 1MW, non-modulating [RER] (megajoule, 5 inputs)
    - Light fuel oil, burned in industrial furnace 1MW, non-modulating [CH] (megajoule, 5 inputs)
    - Light fuel oil, burned in industrial furnace, for asphalt production, 1MW, non-modulating [CH] (megajoule, 5 inputs)
- item: diesel, burned in building machine  (input)
  quote:                                           electric generating set“ (Wirkungsgrad: 36 %) bilanziert, der Verbrauch an fossilen Energieträgern für ther-
  search: diesel burned in building machine
  candidates:
    - Diesel, burned in building machine, with particle filter [GLO] (megajoule, 4 inputs)
    - Diesel, burned in building machine, average [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, with particle filter [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, without particle filter [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, with particle filter, without building machine [CH] (megajoule, 3 inputs)
    - Diesel, burned in building machine, with particle filter, without building machine and lubricating oil [CH] (megajoule, 1 inputs)
    - Diesel, burned in agricultural machine [CH] (kilogram, 4 inputs)
    - Diesel, burned in auxillary machines at concrete crusher [CH] (kilogram, 4 inputs)

Return only the JSON object described by the schema.
