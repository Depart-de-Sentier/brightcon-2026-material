You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: door leaf, room, inner, wood-glass, at plant  (input)
  quote:               door leaf, room, inner, wood-glass, at plant                      CH            0                     m2            0             0              1              0              0
  search: door leaf room inner wood-glass at plant
  candidates:
    - Door leaf, room, inner, wood-glass, at plant [CH] (square meter, 31 inputs)
    - Door leaf, room, inner, wood, at plant [CH] (square meter, 29 inputs)
    - Door, inner, room, glass-wood, steel frame, at plant [CH] (square meter, 3 inputs)
    - Door, inner, room, glass-wood, wooden frame, at plant [CH] (square meter, 3 inputs)
    - Disposal, door leaf, room, inner, wood-glass, to final disposal [CH] (square meter, 8 inputs)
- item: door frame, inner, steel, at plant  (input)
  quote:               door frame, inner, steel, at plant                       CH            0                     m2          0              1               0
  search: door frame inner steel at plant
  candidates:
    - Door frame, inner, steel, at plant [CH] (square meter, 4 inputs)
    - Door, inner, room, wood, steel frame , at plant [CH] (square meter, 3 inputs)
    - Door, inner, functional, wood, steel frame, at plant [CH] (square meter, 3 inputs)
    - Door, inner, room, glass-wood, steel frame, at plant [CH] (square meter, 3 inputs)
    - Door frame, inner, wood, at plant [CH] (square meter, 6 inputs)
    - Door, inner, room, wood, wooden frame, at plant [CH] (square meter, 3 inputs)
    - Door, inner, functional, wood, wooden frame, at plant [CH] (square meter, 3 inputs)
    - Door, inner, room, glass-wood, wooden frame, at plant [CH] (square meter, 3 inputs)
- item: surface treatment, inner door, opaquely painted, at plant  (input)
  quote:                                                                        CH            0                     m2      1.00E+0          5.96E-1                             1.00E+0       1.00E+0       5.96E-1   1.00E+0                                             0          0          0         1                1.16
  search: surface treatment inner door opaquely painted at plant
  candidates:
    - Surface treatment, inner door, opaquely painted, at plant [CH] (square meter, 6 inputs)
    - Surface treatment, outer door, opaquely painted, at plant [CH] (square meter, 6 inputs)
    - Disposal, surface treatment, inner door, opaquely painted, to final disposal [CH] (square meter, 2 inputs)
- item: Energy, gross calorific value, in biomass, resource correction  (resource to resources)
  quote:                                                                          -               -                 MJ      -1.50E+2       -1.50E+2                              -2.26E+2      -8.07E+1     -8.08E+1   -1.57E+2                  -2.71E+2                          -2.25E+2   -2.71E+2     1                1.16
  candidates (flow name [compartment]):
    - Energy, gross calorific value, in biomass  [resources / unspecified] (megajoule, bafu-2026-residual)
    - Energy, gross calorific value, in biomass, resource correction  [resources / unspecified] (megajoule, bafu-2026-residual)
    - Energy, gross calorific value, in biomass  [resources / biotic] (megajoule, bafu-2026-residual)
    - Energy, gross calorific value, in biomass  [resources / in air] (megajoule, bafu-2026-residual)
    - Energy, gross calorific value, in biomass, resource correction  [resources / biotic] (megajoule, bafu-2026-residual)
    - Energy, Gross Calorific Value, In Biomass, Primary Forest  [natural resource] (megajoule, ef-3.1-biosphere)

Return only the JSON object described by the schema.
