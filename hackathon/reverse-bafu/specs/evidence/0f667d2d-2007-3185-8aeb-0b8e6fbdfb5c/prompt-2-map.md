You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Ammonia  (input)
  quote: Ammonia                                                        0.76
  search: ammonia liquid
  candidates:
    - Ammonia, liquid, at regional storehouse [RER] (kilogram, 4 inputs)
    - Ammonia, steam reforming, liquid, at plant [RER] (kilogram, 9 inputs)
    - Ammonia, partial oxidation, liquid, at plant [RER] (kilogram, 7 inputs)
    - Ammonia, liquid, at regional storehouse [CH] (kilogram, 4 inputs)
    - Argon, liquid, at plant [RER] (kilogram, 4 inputs)
    - Ozone, liquid, at plant [RER] (kilogram, 2 inputs)
    - Oxygen, liquid, at plant [RER] (kilogram, 3 inputs)
    - Acetone, liquid, at plant [RER] (kilogram, 8 inputs)
- item: Natural gas, feedstock  (input)
  quote: Natural gas                                                    0.68
  search: natural gas high pressure consumer
  candidates:
    - Natural gas, high pressure, at consumer [RER] (megajoule, 25 inputs)
    - Natural gas, high pressure, at consumer [CH] (megajoule, 7 inputs)
    - Natural gas, high pressure, at consumer [DE] (megajoule, 13 inputs)
    - Natural gas, high pressure, at consumer [GLO] (megajoule, 45 inputs)
    - Natural gas, high pressure, at consumer [AE] (megajoule, 4 inputs)
    - Natural gas, high pressure, at consumer [AR] (megajoule, 10 inputs)
    - Natural gas, high pressure, at consumer [AT] (megajoule, 6 inputs)
    - Natural gas, high pressure, at consumer [AU] (megajoule, 3 inputs)
- item: Sulfuric acid (conc.)  (input)
  quote: Sulfuric acid (conc.)                                          0.26
  search: sulphuric acid liquid
  candidates:
    - Sulphuric acid, liquid, at plant [RER] (kilogram, 7 inputs)
    - Sulphuric acid from viscose production, at plant [GLO] (kilogram, 24 inputs)
- item: Natural gas, process fuel  (input)
  quote: Natural gas                       0.78                0.51
  search: heat natural gas industrial furnace
  candidates:
    - xxx Heat, natural gas, at industrial furnace low-NOx >100kW [RER] (megajoule, 1 inputs)
    - Heat, natural gas, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - District heat, at consumer, natural gas in industrial furnace 1MW [CH] (megajoule, 2 inputs)
    - Industrial furnace, 1MW, natural gas [RER] (unit, 18 inputs)
    - Natural gas, burned in industrial furnace 1MW [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace 1MWth [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace, for asphalt production, 1MWth [CH] (megajoule, 4 inputs)
- item: Dust (SPM)  (emission to air)
  quote: Dust (SPM)                                    1.01
  candidates (flow name [compartment]):
    - Metals, unspecified  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
    - Acidity, unspecified  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
    - Particulates, unspecified  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
    - Radioactive species, unspecified  [emissions to air / unspecified] (kilo Becquerel, bafu-2026-residual)
    - Particles (PM10)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - particles (PM10)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Oils, Unspecified  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Particles (PM0.2)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: SOx  (emission to air)
  quote: SOx                                           18.82
  candidates (flow name [compartment]):
    - Sulfur Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [soil] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [water] (kilogram, ef-3.1-biosphere)
    - Sulfur  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
- item: CH4  (emission to air)
  quote: CH4                                           0.98
  candidates (flow name [compartment]):
    - Methanethiol  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methane (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methane (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methanesulfonic Acid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Fluoro(methoxy)methane  [air] (kilogram, ef-3.1-biosphere)
    - Sodium Methanethiolate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methyl Methanesulfonate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Difluoro(methoxy)methane  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: NOx  (emission to air)
  quote: NOx                                           9.30
  candidates (flow name [compartment]):
    - Nitrogen Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Mustard  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Trifluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen oxide (N2O4)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: CO2  (emission to air)
  quote: CO2                                           2473.52
  candidates (flow name [compartment]):
    - Carbon Dioxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (biogenic)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic-100yr)  [air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
