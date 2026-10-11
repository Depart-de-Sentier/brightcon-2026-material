You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Calcite, in ground  (resource to resources)
  quote: Calcite, in ground                                                 -      -           kg             7.10E-1
  candidates (flow name [compartment]):
    - Calcite  [resources / in ground] (kilogram, bafu-2026-residual)
- item: Gas, natural, in ground  (resource to resources)
  quote: Gas, natural, in ground                                            -      -          Nm3             6.78E-1
  candidates (flow name [compartment]):
    - Natural Gas  [Resources / Resources from ground] (megajoule, ef-3.1-biosphere)
    - Gasoline, Natural  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Gasoline, Natural  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Gasoline, Natural  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - gasoline, natural  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - gasoline, natural  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Natural Gas Condensates (petroleum)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Natural Gas Condensates (petroleum)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Oil, crude, in ground  (resource to resources)
  quote: Oil, crude, in ground                                              -      -           kg             3.55E-1
  candidates (flow name [compartment]):
    - Crude Oil  [Resources / Resources from ground] (megajoule, ef-3.1-biosphere)
    - crude tall oil soap (tos)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - crude tall oil soap (tos)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Fuel Gases, Crude Oil Distillates  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Fuel Gases, Crude Oil Distillates  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Fuel Gases, Crude Oil Distillates  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - fuel gases, crude oil distillates  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - fuel gases, crude oil distillates  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Sand, unspecified, in ground  (resource to resources)
  quote: Sand, unspecified, in ground                                       -      -           kg             1.20E+3
  candidates (flow name [compartment]):
    - Sand, resource correction  [resources / in ground] (kilogram, bafu-2026-residual)
    - Sand  [soil] (kilogram, ef-3.1-biosphere)
    - Oil Sand (10% Bitumen)  [natural resource] (kilogram, ef-3.1-biosphere)
    - Oil Sand (100% Bitumen)  [natural resource] (kilogram, ef-3.1-biosphere)
- item: Sodium chloride, in ground  (resource to resources)
  quote: Sodium chloride, in ground                                         -      -           kg             1.80E+0
  candidates (flow name [compartment]):
    - Sodium chloride  [resources / in ground] (kilogram, bafu-2026-residual)
    - Sodium chloride  [resources / in water] (kilogram, bafu-2026-residual)
    - sodium chloride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - sodium chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium Chloride - 1-benzylpyridinium-3-carboxylate (1:1)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sodium Chloride - 1-benzylpyridinium-3-carboxylate (1:1)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Sodium Chloride - 1-benzylpyridinium-3-carboxylate (1:1)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - sodium chloride - 1-benzylpyridinium-3-carboxylate (1:1)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: sylvite, 25 % in sylvinite, in ground  (resource to resources)
  quote: sylvite, 25 % in sylvinite, in ground                              -      -           kg             2.90E-2
  candidates (flow name [compartment]):
    - Potassium chloride  [resources / in ground] (kilogram, bafu-2026-residual)
    - Potassium Chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Potassium Chloride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Potassium Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - potassium chloride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - potassium chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Potassium  [Resources / Resources from ground] (kilogram, ef-3.1-biosphere)
    - Sodium chloride  [resources / in ground] (kilogram, bafu-2026-residual)
- item: Water, well, in ground  (resource to resources)
  quote: Water, well, in ground                                             -      -           m3             1.40E-5
  candidates (flow name [compartment]):
    - Ground Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - lake water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - river water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water To Cooling  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water to turbine  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water, salt, sole  [resources / in water] (cubic meter, bafu-2026-residual)
    - Water, salt, ocean  [resources / in water] (cubic meter, bafu-2026-residual)
- item: Water, river  (resource to resources)
  quote: Water, river                                                       -      -           m3             9.20E-5
  candidates (flow name [compartment]):
    - river water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - lake water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Ground Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water To Cooling  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water to turbine  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water, salt, sole  [resources / in water] (cubic meter, bafu-2026-residual)
    - Water, salt, ocean  [resources / in water] (cubic meter, bafu-2026-residual)
- item: Water, salt, ocean  (resource to resources)
  quote: Water, salt, ocean                                                 -      -           m3             9.50E-4
  candidates (flow name [compartment]):
    - Water, salt, ocean  [resources / in water] (cubic meter, bafu-2026-residual)
    - Water, salt, sole  [resources / in water] (cubic meter, bafu-2026-residual)
- item: Water, cooling, unspecified natural origin  (resource to resources)
  quote: Water, cooling, unspecified natural origin                         -      -           m3             3.84E-1
  candidates (flow name [compartment]):
    - Water To Cooling  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water Cooling Sea  [water] (kilogram, ef-3.1-biosphere)
    - Water from cooling  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - lake water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - river water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Ground Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water to turbine  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
- item: Water, unspecified natural origin  (resource to resources)
  quote: Water, unspecified natural origin                                  -      -           m3             6.10E-3
  candidates (flow name [compartment]):
    - (no candidate found)
- item: electricity, medium voltage, production UCTE, at grid  (input)
  quote: electricity, medium voltage, production UCTE, at grid                  UCTE     0          kWh             2.19E+0
  search: electricity medium voltage production grid
  candidates:
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from oil, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from biogas, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from CHP wood, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from hard coal, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from CHP diesel, at grid [CH] (kilowatt hour, 3 inputs)
- item: heavy fuel oil, burned in power plant  (input)
  quote: heavy fuel oil, burned in power plant                                  RER     0           MJ             1.10E+1
  search: heavy fuel oil burned power plant
  candidates:
    - Heavy fuel oil, burned in power plant [RER] (megajoule, 12 inputs)
    - Heavy fuel oil, burned in power plant [DE] (megajoule, 8 inputs)
    - Heavy fuel oil, burned in power plant [AT] (megajoule, 12 inputs)
    - Heavy fuel oil, burned in power plant [BE] (megajoule, 12 inputs)
    - Heavy fuel oil, burned in power plant [CS] (megajoule, 12 inputs)
    - Heavy fuel oil, burned in power plant [CZ] (megajoule, 12 inputs)
    - Heavy fuel oil, burned in power plant [DK] (megajoule, 12 inputs)
    - Heavy fuel oil, burned in power plant [ES] (megajoule, 9 inputs)
- item: natural gas, burned in industrial furnace >100kW  (input)
  quote: natural gas, burned in industrial furnace >100kW                       RER     0           MJ             5.77E+1
  search: natural gas burned industrial furnace
  candidates:
    - Natural gas, burned in industrial furnace 1MW [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace 1MWth [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace, for asphalt production, 1MWth [CH] (megajoule, 4 inputs)
    - Industrial furnace, 1MW, natural gas [RER] (unit, 18 inputs)
    - xxx Heat, natural gas, at industrial furnace low-NOx >100kW [RER] (megajoule, 1 inputs)
    - Heat, natural gas, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - District heat, at consumer, natural gas in industrial furnace 1MW [CH] (megajoule, 2 inputs)
- item: tap water, at user  (input)
  quote: tap water, at user                                                     RER     0           kg             1.30E+1
  search: tap water at user
  candidates:
    - Tap water, at user [RER] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin RER, at user [RER] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin OECD, at user [RER] (kilogram, 14 inputs)
    - Tap water, water balance according to MoeK 2013, at user [RER] (kilogram, 14 inputs)
    - Tap water, at user [CH] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin CH, at user [CH] (kilogram, 14 inputs)
    - Tap water, water balance according to MoeK 2013, at user [CH] (kilogram, 14 inputs)
    - Tap water, water balance according to MoeK 2013, at user [DE] (kilogram, 14 inputs)
- item: disposal, municipal solid waste, 22.9% water, to sanitary landfill  (input)
  quote: disposal, municipal solid waste, 22.9% water, to sanitary landfill     CH      0           kg             2.98E-1
  search: disposal municipal solid waste sanitary landfill
  candidates:
    - Disposal, municipal solid waste, 22.9% water, to sanitary landfill [CH] (kilogram, 33 inputs)
- item: disposal, municipal solid waste, 22.9% water, to municipal incineration  (input)
  quote: disposal, municipal solid waste, 22.9% water, to municipal incineration CH      0           kg             5.80E-3
  search: disposal municipal solid waste municipal incineration
  candidates:
    - Disposal, municipal solid waste, 22.9% water, to municipal incineration [CH] (kilogram, 20 inputs)
    - Disposal, wood and wood materials as construction waste, to municipal waste incineration, solid wood [CH] (kilogram, 2 inputs)
    - Disposal, LCD module,  to municipal waste incineration [CH] (kilogram, 20 inputs)
    - Disposal, bitumen sheet, to municipal waste incineration [CH] (kilogram, 2 inputs)
    - Disposal, aerogel blanket, to municipal waste incineration [CH] (kilogram, 3 inputs)
    - Disposal, EPDM seal sheeting, to municipal waste incineration [CH] (kilogram, 2 inputs)
    - Disposal, PE 50% flame retarded, to municipal waste incineration [CH] (kilogram, 3 inputs)
    - Disposal, municipal solid waste, 22.9% water, to sanitary landfill [CH] (kilogram, 33 inputs)
- item: chemical plant, organics  (input)
  quote: chemical plant, organics                                               RER     1          unit            4.00E-10
  search: chemical plant organics
  candidates:
    - Chemical plant, organics [RER] (unit, 4 inputs)
    - Heat, unspecific, in chemical plant [RER] (megajoule, 4 inputs)
    - Steam, for chemical processes, at plant [RER] (kilogram, 3 inputs)
    - Liquid storage tank, chemicals, organics [CH] (unit, 12 inputs)
    - Chemicals organic, at plant [GLO] (kilogram, 20 inputs)
    - Chemicals inorganic, at plant [GLO] (kilogram, 20 inputs)
- item: transport, freight, rail  (input)
  quote: transport, freight, rail                                               RER     0          tkm             1.74E+0
  search: transport freight rail
  candidates:
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [RER] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting, Betrieb [CH] (ton kilometer, 2 inputs)
    - Transport, freight, rail, electricity with shunting, Fahrzeug [CH] (ton kilometer, 5 inputs)
- item: transport, lorry 32t  (input)
  quote: transport, lorry 32t                                                   RER     0          tkm             6.06E+1
  search: transport lorry fleet average
  candidates:
    - Transport, freight, lorry, fleet average [RER] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 3.5t-7.5t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, diesel, fleet average, urban delivery [RER] (ton kilometer, 12 inputs)
- item: Acetaldehyde  (emission to air)
  quote: Acetaldehyde   -   -   kg   4.70E-5
  candidates (flow name [compartment]):
    - Acetaldehyde  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde oxime, (1E)-  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - acetaldehyde  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - acetaldehyde  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - acetaldehyde oxime  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Ammonia  (emission to air)
  quote: Ammonia   -   -   kg   4.00E-6
  candidates (flow name [compartment]):
    - Ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Carbon dioxide, fossil  (emission to air)
  quote: Carbon dioxide, fossil   -   -   kg   6.50E-1
  candidates (flow name [compartment]):
    - Carbon Dioxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (biogenic)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic-100yr)  [air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
- item: Carbon monoxide, fossil  (emission to air)
  quote: Carbon monoxide, fossil   -   -   kg   2.60E-4
  candidates (flow name [compartment]):
    - Carbon Monoxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - carbon monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - carbon monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Black carbon  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
- item: Halogenated hydrocarbons, chlorinated  (emission to air)
  quote: Halogenated hydrocarbons, chlorinated   -   -   kg   1.10E-5
  candidates (flow name [compartment]):
    - Hydrocarbons, Chlorinated  [air] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, C3  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, C4  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, C3-4  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, C5-rich  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, Aromatic  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons (unspecified)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, C2-4, C3-rich  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Hydrocarbons, aromatic  (emission to air)
  quote: Hydrocarbons, aromatic   -   -   kg   2.80E-5
  candidates (flow name [compartment]):
    - Hydrocarbons, Aromatic  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Polycyclic Aromatic Hydrocarbons  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Aromatic Hydrocarbons, C6-8, Naphtha-raffinate Pyrolyzate Derived  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, Aromatic  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, Aromatic  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, aromatic  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, aromatic  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Polycyclic Aromatic Hydrocarbons  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Hydrogen chloride  (emission to air)
  quote: Hydrogen chloride   -   -   kg   2.30E-4
  candidates (flow name [compartment]):
    - Hydrogen Chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen Chloride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Hydrogen Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - hydrogen chloride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - hydrogen chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen  [air] (kilogram, ef-3.1-biosphere)
    - Hydrogen-3  [Emissions / Emissions to air] (kilo Becquerel, ef-3.1-biosphere)
- item: Hydrogen fluoride  (emission to air)
  quote: Hydrogen fluoride   -   -   kg   5.00E-7
  candidates (flow name [compartment]):
    - hydrogen fluoride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - hydrogen fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Hydrogen  [air] (kilogram, ef-3.1-biosphere)
    - Hydrogen-3  [Emissions / Emissions to air] (kilo Becquerel, ef-3.1-biosphere)
    - Fluoride Ion  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Vinyl Fluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Fentin Fluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen Iodide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Hydrogen sulfide  (emission to air)
  quote: Hydrogen sulfide   -   -   kg   3.00E-6
  candidates (flow name [compartment]):
    - Hydrogen Sulfide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen Sulfide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Hydrogen Sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - hydrogen sulfide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - hydrogen sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Hydrogen  [air] (kilogram, ef-3.1-biosphere)
    - Hydrogen-3  [Emissions / Emissions to air] (kilo Becquerel, ef-3.1-biosphere)
    - Sulfide ion  [air] (kilogram, ef-3.1-biosphere)
- item: Lead  (emission to air)
  quote: Lead   -   -   kg   5.00E-7
  candidates (flow name [compartment]):
    - Lead  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead-210  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead oxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead nitrate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Sulfochromate Yellow  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Mercury  (emission to air)
  quote: Mercury   -   -   kg   5.00E-7
  candidates (flow name [compartment]):
    - Mercury  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Mercury  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Mercury  [Resources / Resources from ground] (kilogram, ef-3.1-biosphere)
    - mercury  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Methane, fossil  (emission to air)
  quote: Methane, fossil   -   -   kg   2.00E-4
  candidates (flow name [compartment]):
    - Methanethiol  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methane (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methane (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methanesulfonic Acid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Fluoro(methoxy)methane  [air] (kilogram, ef-3.1-biosphere)
    - Sodium Methanethiolate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methyl Methanesulfonate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Difluoro(methoxy)methane  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Methane, chlorotrifluoro-, CFC-13  (emission to air)
  quote: Methane, chlorotrifluoro-, CFC-13   -   -   kg   8.00E-6
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Nitrogen oxides  (emission to air)
  quote: Nitrogen oxides   -   -   kg   2.70E-3
  candidates (flow name [compartment]):
    - Nitrogen Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Mustard  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Trifluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen oxide (N2O4)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Particulates, > 2.5 um, and < 10um  (emission to air)
  quote: Particulates, > 2.5 um, and < 10um   -   -   kg   7.10E-3
  candidates (flow name [compartment]):
    - Particles (PM10)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - particles (PM10)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Particles (> PM10)  [air] (kilogram, ef-3.1-biosphere)
    - Particles (PM2.5 - PM10)  [air] (kilogram, ef-3.1-biosphere)
    - Particles (PM10)  [soil] (kilogram, ef-3.1-biosphere)
    - Particles (PM10)  [water] (kilogram, ef-3.1-biosphere)
    - Particles (> PM10)  [soil] (kilogram, ef-3.1-biosphere)
    - Particles (> PM10)  [water] (kilogram, ef-3.1-biosphere)
- item: Sulfur dioxide  (emission to air)
  quote: Sulfur dioxide   -   -   kg   1.70E-3
  candidates (flow name [compartment]):
    - Sulfur Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [soil] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [water] (kilogram, ef-3.1-biosphere)
    - Sulfur  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
- item: NMVOC, non-methane volatile organic compounds, unspecified origin  (emission to air)
  quote: NMVOC, non-methane volatile organic compounds, unspecified origin   -   -   kg   4.94E-4
  candidates (flow name [compartment]):
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - non-methane volatile organic compounds  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - non-methane volatile organic compounds  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Heat, waste  (emission to air)
  quote: Heat, waste                                                        -      -           MJ             7.87E+0
  candidates (flow name [compartment]):
    - Waste Heat  [air] (megajoule, ef-3.1-biosphere)
    - Energy, waste heat, air  [resources / in air] (megajoule, bafu-2026-residual)
    - Waste Heat  [soil] (megajoule, ef-3.1-biosphere)
    - Waste Heat  [water] (megajoule, ef-3.1-biosphere)
    - Heat, waste  [emissions to water / groundwater, long-term] (megajoule, bafu-2026-residual)
    - Waste water/m3  [emissions to water / unspecified] (cubic meter, bafu-2026-residual)
    - Waste water  [emissions to water / ocean] (kilogram, bafu-2026-residual)
    - Waste water  [emissions to water / river] (kilogram, bafu-2026-residual)
- item: Ammonium, ion (to water)  (emission to water)
  quote: Ammonium, ion   -   -   kg   3.00E-6
  candidates (flow name [compartment]):
    - Ammonium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - ammonium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Bromide ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lithium ion  [water] (kilogram, ef-3.1-biosphere)
    - Sulfate Ion  [water] (kilogram, ef-3.1-biosphere)
- item: Arsenic, ion (to water)  (emission to water)
  quote: Arsenic, ion   -   -   kg   5.00E-7
  candidates (flow name [compartment]):
    - Arsenic  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - arsenic  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Arsenic (v)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - arsenic (v)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Arsenic Acid  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Arsenic (iii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - arsenic (iii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - arsenic trioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: BOD5, Biological Oxygen Demand (to water)  (emission to water)
  quote: BOD5, Biological Oxygen Demand   -   -   kg   1.10E-3
  candidates (flow name [compartment]):
    - Biological Oxygen Demand  [water] (kilogram, ef-3.1-biosphere)
    - BOD5, Biological Oxygen Demand  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Chemical Oxygen Demand  [water] (kilogram, ef-3.1-biosphere)
    - COD, Chemical Oxygen Demand  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
- item: Calcium, ion (to water)  (emission to water)
  quote: Calcium, ion   -   -   kg   5.40E-2
  candidates (flow name [compartment]):
    - Calcium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - calcium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Calcium oxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Calcium Bromide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Calcium Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Calcium acetate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Calcium formate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Calcium nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Carboxylic acids, unspecified (to water)  (emission to water)
  quote: Carboxylic acids, unspecified   -   -   kg   5.90E-5
  candidates (flow name [compartment]):
    - carboxylic acids, di-, c4-6  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Carboxylic Acids, Unspecified  [water] (kilogram, ef-3.1-biosphere)
    - carboxylic acids, di-, c4-6  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - fatty acids, c8-10  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Fatty Acids, C12-18  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Fatty Acids, C14-22  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Fatty Acids, C16-22  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - fatty acids, c12-18  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Chloride (to water)  (emission to water)
  quote: Chloride   -   -   kg   9.80E-1
  candidates (flow name [compartment]):
    - Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Allyl Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Vinyl Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - allyl chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - vinyl chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Acetyl Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Chlorinated solvents, unspecified (to water)  (emission to water)
  quote: Chlorinated solvents, unspecified   -   -   kg   1.13E-4
  candidates (flow name [compartment]):
    - Chlorinated Solvents, Unspecified  [water] (kilogram, ef-3.1-biosphere)
    - Chlorinated Solvents, Unspecified  [air] (kilogram, ef-3.1-biosphere)
    - [29h,31h-phthalocyaninato(2-)-.kappa.n29,.kappa.n30,.kappa.n31,.kappa.n32]copper, Chlorinated  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - [29h,31h-phthalocyaninato(2-)-.kappa.n29,.kappa.n30,.kappa.n31,.kappa.n32]copper, chlorinated  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, Chlorinated  [air] (kilogram, ef-3.1-biosphere)
    - [29h,31h-phthalocyaninato(2-)-.kappa.n29,.kappa.n30,.kappa.n31,.kappa.n32]copper, Chlorinated  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - [29h,31h-phthalocyaninato(2-)-.kappa.n29,.kappa.n30,.kappa.n31,.kappa.n32]copper, Chlorinated  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - [29h,31h-phthalocyaninato(2-)-.kappa.n29,.kappa.n30,.kappa.n31,.kappa.n32]copper, chlorinated  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Chromium VI (to water)  (emission to water)
  quote: Chromium VI   -   -   kg   5.00E-7
  candidates (flow name [compartment]):
    - Chromium VI  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - chromium (vi)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chromium (vi)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Chromium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chromium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - vitamin D2  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chromium-51  [water] (kilogram, ef-3.1-biosphere)
    - Vinclozolin  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: COD, Chemical Oxygen Demand (to water)  (emission to water)
  quote: COD, Chemical Oxygen Demand   -   -   kg   5.10E-2
  candidates (flow name [compartment]):
    - Chemical Oxygen Demand  [water] (kilogram, ef-3.1-biosphere)
    - COD, Chemical Oxygen Demand  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Biological Oxygen Demand  [water] (kilogram, ef-3.1-biosphere)
    - BOD5, Biological Oxygen Demand  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
- item: Copper, ion (to water)  (emission to water)
  quote: Copper, ion   -   -   kg   5.00E-7
  candidates (flow name [compartment]):
    - Copper  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - copper  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Copper(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - copper (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Oxine-copper  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - oxine-copper  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Copper hydroxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - copper (i) oxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Cyanide (to water)  (emission to water)
  quote: Cyanide   -   -   kg   5.00E-7
  candidates (flow name [compartment]):
    - Cyanide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - cyanide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium Cyanide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - sodium cyanide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Hydrogen cyanide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Potassium Cyanide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - potassium cyanide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Carbonyl cyanide (m-chlorophenyl)hydrazone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: DOC, Dissolved Organic Carbon (to water)  (emission to water)
  quote: DOC, Dissolved Organic Carbon   -   -   kg   1.70E-2
  candidates (flow name [compartment]):
    - DOC, Dissolved Organic Carbon  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - DOC, Dissolved Organic Carbon  [water] (kilogram, ef-3.1-biosphere)
    - Total Organic Carbon  [water] (kilogram, ef-3.1-biosphere)
    - TOC, Total Organic Carbon  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Total Organic Carbon  [air] (kilogram, ef-3.1-biosphere)
    - Total Organic Carbon  [soil] (kilogram, ef-3.1-biosphere)
    - Organic carbon, placed in landfill  [resources / in ground] (kilogram, bafu-2026-residual)
    - Carbon, organic, in soil or biomass stock  [resources / in ground] (kilogram, bafu-2026-residual)
- item: Fluoride (to water)  (emission to water)
  quote: Fluoride   -   -   kg   1.00E-6
  candidates (flow name [compartment]):
    - fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Fluoride Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Vinyl Fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Fentin Fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium Fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - fentin fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - sodium fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Calcium Fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Oils, unspecified (to water)  (emission to water)
  quote: Oils, unspecified   -   -   kg   6.90E-5
  candidates (flow name [compartment]):
    - Oils, Unspecified  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Oils, unspecified  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Oils, Unspecified  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Oils, Unspecified  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Oils, Unspecified  [soil] (kilogram, ef-3.1-biosphere)
    - Oils, unspecified  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Acidity, unspecified  [emissions to water / unspecified] (kilogram, bafu-2026-residual)
    - Lubricating Oils  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Hydrocarbons, unspecified (to water)  (emission to water)
  quote: Hydrocarbons, unspecified   -   -   kg   6.40E-5
  candidates (flow name [compartment]):
    - Hydrocarbons (unspecified)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - hydrocarbons (unspecified)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, Aliphatic, Alkanes, Unspecified  [water] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons (unspecified)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons (unspecified)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - hydrocarbons (unspecified)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, Aliphatic, Alkanes, Unspecified  [air] (kilogram, ef-3.1-biosphere)
    - Acidity, unspecified  [emissions to water / unspecified] (kilogram, bafu-2026-residual)
- item: Iron, ion (to water)  (emission to water)
  quote: Iron, ion   -   -   kg   1.00E-6
  candidates (flow name [compartment]):
    - Iron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - iron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iron-59  [water] (kilo Becquerel, ef-3.1-biosphere)
    - Iron(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iron(3+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - iron (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iron Oxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - iron (iii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Magnesium (to water)  (emission to water)
  quote: Magnesium   -   -   kg   1.70E-5
  candidates (flow name [compartment]):
    - Magnesium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - magnesium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Magnesium nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Magnesium Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - magnesium chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - magnesium sulphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Magnesium Carbonate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Magnesium Hydroxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Mercury (to water)  (emission to water)
  quote: Mercury   -   -   kg   1.00E-6
  candidates (flow name [compartment]):
    - Mercury  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - mercury (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Mercury  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Mercury  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury  [Resources / Resources from ground] (kilogram, ef-3.1-biosphere)
    - mercury  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Nickel, ion (to water)  (emission to water)
  quote: Nickel, ion   -   -   kg   5.00E-7
  candidates (flow name [compartment]):
    - Nickel  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - nickel  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel-63  [water] (kilogram, ef-3.1-biosphere)
    - Nickel(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - nickel (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel Sulphide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - nickel sulphide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Nitrate (to water)  (emission to water)
  quote: Nitrate   -   -   kg   1.00E-6
  candidates (flow name [compartment]):
    - Nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Zinc nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Barium nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cupric nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Silver Nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium Nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Nitrogen (to water)  (emission to water)
  quote: Nitrogen   -   -   kg   1.00E-5
  candidates (flow name [compartment]):
    - Nitrogen  [water] (kilogram, ef-3.1-biosphere)
    - Nitrogen Dioxide  [water] (kilogram, ef-3.1-biosphere)
    - Nitrogen Mustard  [water] (kilogram, ef-3.1-biosphere)
    - Nitrogen Trifluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - nitrogen trifluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nitrogen oxide (N2O4)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nitrogen, organic bound  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Nitrogen, Total (excluding N2)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Phenol (to water)  (emission to water)
  quote: Phenol   -   -   kg   6.00E-6
  candidates (flow name [compartment]):
    - Phenol  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - phenol  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Phenolphthalein  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - phenolphthalein  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Phenol, Styrenated  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - phenol, styrenated  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - P-(2-methoxyethyl)phenol  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - p-(2-methoxyethyl)phenol  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Phosphate (to water)  (emission to water)
  quote: Phosphate   -   -   kg   2.20E-4
  candidates (flow name [compartment]):
    - Phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - urea phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Butyl Phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - butyl phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Dibutyl phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Diethyl phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Dimethyl phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Potassium, ion (to water)  (emission to water)
  quote: Potassium, ion   -   -   kg   8.20E-4
  candidates (flow name [compartment]):
    - Potassium  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Potassium  [water] (kilogram, ef-3.1-biosphere)
    - Potassium-40  [water] (kilo Becquerel, ef-3.1-biosphere)
    - Potassium(1+)  [water] (kilogram, ef-3.1-biosphere)
    - Potassium Iodate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Potassium Iodide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - potassium iodate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - potassium iodide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Sodium, ion (to water)  (emission to water)
  quote: Sodium, ion   -   -   kg   3.80E-1
  candidates (flow name [compartment]):
    - Sodium  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Sodium  [water] (kilogram, ef-3.1-biosphere)
    - sodium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium-24  [water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Metam-sodium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium Azide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - metam-sodium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Sulfate (to water)  (emission to water)
  quote: Sulfate   -   -   kg   8.10E-3
  candidates (flow name [compartment]):
    - Sulfate Ion  [water] (kilogram, ef-3.1-biosphere)
    - Sulfate Ion  [air] (kilogram, ef-3.1-biosphere)
    - Sulfate Ion  [soil] (kilogram, ef-3.1-biosphere)
    - Sulfate  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Bromide ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Sulfide (to water)  (emission to water)
  quote: Sulfide   -   -   kg   1.00E-6
  candidates (flow name [compartment]):
    - Sulfide ion  [water] (kilogram, ef-3.1-biosphere)
    - Ethyl sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Barium Sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Propyl sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium Sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - barium sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cadmium sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - diethyl sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Suspended solids, unspecified (to water)  (emission to water)
  quote: Suspended solids, unspecified   -   -   kg   8.30E-2
  candidates (flow name [compartment]):
    - Suspended Solids, Unspecified  [water] (kilogram, ef-3.1-biosphere)
- item: VOC, volatile organic compounds, unspecified origin (to water)  (emission to water)
  quote: VOC, volatile organic compounds, unspecified origin   -   -   kg   5.20E-3
  candidates (flow name [compartment]):
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - non-methane volatile organic compounds  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - non-methane volatile organic compounds  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Volatile Organic Compound  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - volatile organic compound  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Adsorbable Organic Halogen Compounds  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Zinc, ion (to water)  (emission to water)
  quote: Zinc, ion   -   -   kg   5.00E-7
  candidates (flow name [compartment]):
    - Zinc  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Zinc-65  [water] (kilogram, ef-3.1-biosphere)
    - Zinc(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc oxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Zinc Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Zinc nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
