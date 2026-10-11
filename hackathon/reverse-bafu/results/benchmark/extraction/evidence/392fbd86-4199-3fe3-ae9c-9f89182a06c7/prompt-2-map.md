You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: mineral nitrogen fertiliser, 30 kg N per ha (integrated production only)  (input)
  quote: organic production is the application of 30 kg N/ha in the form of mineral fertiliser in the integrated
  search: nitrogen fertiliser regional storehouse
  candidates:
    - Average mineral fertiliser, as N, at regional storehouse [RER] (kilogram, 5 inputs)
    - Average mineral fertiliser, as K2O, at regional storehouse [RER] (kilogram, 2 inputs)
    - Average mineral fertiliser, as P2O5, at regional storehouse [RER] (kilogram, 6 inputs)
- item: Occupation, arable, non-irrigated  (resource to resources)
  quote: manure was derived using the period from the time of seeding until the end of the month specified in
  candidates (flow name [compartment]):
    - Arable, Non-irrigated  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Arable, Non-irrigated  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Arable, Non-irrigated  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - Arable, Non-irrigated, Extensive  [Land use / Land occupation] (kilogram, ef-3.1-biosphere)
    - Arable, Non-irrigated, Intensive  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Arable, Non-irrigated, Extensive  [Land use / Land transformation] (kilogram, ef-3.1-biosphere)
    - To Arable, Non-irrigated, Intensive  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Arable, Non-irrigated, Extensive  [Land use / Land transformation] (kilogram, ef-3.1-biosphere)
- item: Transformation, from arable, non-irrigated  (resource to resources)
  quote: to green manure was therefore calculated 100% as “Transformation, from arable, non-irrigated”. The
  candidates (flow name [compartment]):
    - From Arable, Non-irrigated  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Arable, Non-irrigated, Extensive  [Land use / Land transformation] (kilogram, ef-3.1-biosphere)
    - From Arable, Non-irrigated, Intensive  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
- item: Transformation, to arable, non-irrigated  (resource to resources)
  quote:      Transformation, to arable, non-irrigated         resource          m2
  candidates (flow name [compartment]):
    - Arable, Non-irrigated  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Arable, Non-irrigated  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Arable, Non-irrigated  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - Arable, Non-irrigated, Extensive  [Land use / Land occupation] (kilogram, ef-3.1-biosphere)
    - Arable, Non-irrigated, Intensive  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Arable, Non-irrigated, Extensive  [Land use / Land transformation] (kilogram, ef-3.1-biosphere)
    - To Arable, Non-irrigated, Intensive  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Arable, Non-irrigated, Extensive  [Land use / Land transformation] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
