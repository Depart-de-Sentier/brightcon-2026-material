You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Bisphenol A  (input)
  quote: production by interfacial polycondesation out of phosgene and bisphenol A
  search: bisphenol A powder
  candidates:
    - Bisphenol A, powder, at plant [RER] (kilogram, 7 inputs)
    - Powder coating, steel [RER] (square meter, 14 inputs)
    - Soda, powder, at plant [RER] (kilogram, 8 inputs)
    - Coating powder, at plant [RER] (kilogram, 11 inputs)
    - Zeolite, powder, at plant [RER] (kilogram, 0 inputs, aggregated)
    - Powder coating, aluminium sheet [RER] (square meter, 15 inputs)
    - Sodium chlorate, powder, at plant [RER] (kilogram, 13 inputs)
    - Sodium chloride, powder, at plant [RER] (kilogram, 10 inputs)
- item: Phosgene  (input)
  quote: production by interfacial polycondesation out of phosgene and bisphenol A
  search: phosgene liquid
  candidates:
    - Phosgene, liquid, at plant [RER] (kilogram, 7 inputs)
    - Argon, liquid, at plant [RER] (kilogram, 4 inputs)
    - Ozone, liquid, at plant [RER] (kilogram, 2 inputs)
    - Oxygen, liquid, at plant [RER] (kilogram, 3 inputs)
    - Acetone, liquid, at plant [RER] (kilogram, 8 inputs, aggregated)
    - Toluene, liquid, at plant [RER] (kilogram, 8 inputs, aggregated)
    - Fluorine, liquid, at plant [RER] (kilogram, 5 inputs)
    - Hydrogen, liquid, at plant [RER] (kilogram, 2 inputs)
- item: Sodium hydroxide  (input)
  quote: interfacial polycondesation
  search: sodium hydroxide 50%
  candidates:
    - Sodium hydroxide, 50% in H2O, mercury cell, at plant [RER] (kilogram, 14 inputs)
    - Sodium hydroxide, 50% in H2O, membrane cell, at plant [RER] (kilogram, 13 inputs)
    - Sodium hydroxide, 50% in H2O, diaphragm cell, at plant [RER] (kilogram, 14 inputs)
    - Sodium hydroxide, 50% in H2O, production mix, at plant [RER] (kilogram, 3 inputs)

Return only the JSON object described by the schema.
