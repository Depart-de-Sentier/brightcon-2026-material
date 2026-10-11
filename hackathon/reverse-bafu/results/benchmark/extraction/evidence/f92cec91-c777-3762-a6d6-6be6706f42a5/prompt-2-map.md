You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (GLO), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: cotton fibres, ginned, at farm  (input)
  quote: technosphere                  cotton fibres, ginned, at farm                                CN               kg            6.60E-1                            1                           1.16                 Datendokumentation (Wiegmann K., 2002),
  search: cotton fibres ginned at farm
  candidates:
    - Cotton fibres, ginned, at farm [CN] (kilogram, 24 inputs)
    - Cotton fibres, at farm [US] (kilogram, 36 inputs)
- item: cotton fibres, at farm  (input)
  quote: technosphere                  cotton fibres, at farm                                         US              kg            4.40E-1                            1                           1.16                 Datendokumentation (Wiegmann K., 2002),
  search: cotton fibres at farm
  candidates:
    - Cotton fibres, at farm [US] (kilogram, 36 inputs)
    - Cotton fibres, ginned, at farm [CN] (kilogram, 24 inputs)
    - Yarn production, cotton fibres [GLO] (kilogram, 4 inputs)
    - Cotton seed, at farm [US] (kilogram, 36 inputs)
    - Kenaf fibres, at farm [IN] (kilogram, 8 inputs)
    - xx Cotton seed, at farm [CN] (kilogram, 24 inputs)
    - Jute fibres, rainfed system, at farm [IN] (kilogram, 8 inputs)
    - Jute fibres, irrigated system, at farm [IN] (kilogram, 5 inputs)
- item: yarn production, cotton fibres  (input)
  quote: technosphere                  yarn production, cotton fibres                               GLO               kg            1.00E+0                            1                           1.17                 Datendokumentation (Wiegmann K., 2002),
  search: yarn production cotton fibres
  candidates:
    - Yarn production, cotton fibres [GLO] (kilogram, 4 inputs)
    - Yarn production, bast fibres [IN] (kilogram, 5 inputs)
- item: disposal, paper, 11.2% water, to sanitary landfill  (input)
  quote:                               disposal, paper, 11.2% water, to sanitary
  search: disposal paper sanitary landfill
  candidates:
    - Disposal, paper, 11.2% water, to sanitary landfill [CH] (kilogram, 33 inputs)
    - xx Disposal, packaging paper, 13.7% water, to sanitary landfill [CH] (kilogram, 33 inputs)
    - Disposal, sludge from pulp and paper production, 25% water, to sanitary landfill [CH] (kilogram, 33 inputs)
    - Disposal, paint, 0% water, to sanitary landfill [CH] (kilogram, 25 inputs)
    - Disposal, ash olive pomace, to sanitary landfill [CH] (kilogram, 28 inputs)
    - Disposal, aluminium, 0% water, to sanitary landfill [CH] (kilogram, 25 inputs)
    - Disposal, asphalt, 0.1% water, to sanitary landfill [CH] (kilogram, 33 inputs)
    - Disposal, bitumen, 1.4% water, to sanitary landfill [CH] (kilogram, 33 inputs)

Return only the JSON object described by the schema.
