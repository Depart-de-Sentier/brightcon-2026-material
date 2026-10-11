You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Wood wool, at plant (u=20%)  (input)
  quote: Wood wool, at plant (u=20%)  Î  120-180 kg  wooden materials extraction No RER  wood wool, u=20%, at plant  1.50E+02 kg  Schniewind 1989, p. 197 ff.
  search: wood wool u=20%
  candidates:
    - xxx Wood wool, u=20%, at plant [RER] (kilogram, 6 inputs)
    - xxx Industrial residue wood, wood wool production, softwood, u=20%, at plant [RER] (cubic meter, 1 inputs)
    - Wood wool, at plant [RER] (kilogram, 5 inputs)
    - Wood wool boards, cement bonded, at plant [RER] (cubic meter, 8 inputs)
    - xxx Wood wool boards, cement bonded, at plant [RER] (cubic meter, 0 inputs, aggregated)
    - xxx Industrial residue wood, LTE production, hardwood, u=20%, at plant [RER] (cubic meter, 1 inputs)
    - xxx Industrial residue wood, LTE production, softwood, u=20%, at plant [RER] (cubic meter, 6 inputs)
    - xxx Residual wood, hardwood, under bark, air dried, u=20%, at forest road [RER] (cubic meter, 2 inputs)
- item: Portland Cement  (input)
  quote: Portland Cement  Î  180-250 kg  construction materials binder No CH  cement, unspecified, at plant  2.15E+02 kg  Schniewind 1989, p. 197 ff.
  search: cement unspecified plant
  candidates:
    - Cement, unspecified, at plant [CH] (kilogram, 5 inputs)
    - Particle board, cement bonded, at plant [RER] (cubic meter, 0 inputs, aggregated)
    - Wood wool boards, cement bonded, at plant [RER] (cubic meter, 8 inputs)
    - Ethoxylated alcohols, unspecified, at plant [RER] (kilogram, 6 inputs)
    - Metal working machine, unspecified, at plant [RER] (kilogram, 30 inputs)
    - xxx Wood wool boards, cement bonded, at plant [RER] (cubic meter, 0 inputs, aggregated)
    - Industrial machine, heavy, unspecified, at plant [RER] (kilogram, 8 inputs)
    - Pigments, paper production, unspecified, at plant [RER] (kilogram, 3 inputs)
- item: Process and cooling water  (resource to resources)
  quote: Process and cooling water  Î  200-290 kg; evaporates partly during drying  resource in water  Water, cooling, unspecified natural origin  2.45E-01 m3  Schniewind 1989, p. 197 ff.
  candidates (flow name [compartment]):
    - Water To Cooling  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water Cooling Sea  [water] (kilogram, ef-3.1-biosphere)
    - Water from cooling  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - lake water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - river water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Ground Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water to turbine  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
- item: Organic chemicals  (input)
  quote: Organic chemicals  Î  Additives: 6-8 kg; sometimes, no organic chemicals but waterglas is used  chemicals organics No GLO  chemicals organic, at plant  7.00E+00 kg
  search: chemicals organic plant
  candidates:
    - Chemicals organic, at plant [GLO] (kilogram, 20 inputs)
    - Chemical plant, organics [RER] (unit, 4 inputs)
    - Wood preservative, organic salt, Cr-free, at plant [RER] (kilogram, 0 inputs, aggregated)
    - Wooden board manufacturing plant, organic bonded boards [RER] (unit, 8 inputs)
    - Strawberry seedling, organic, for planting, in unheated greenhouse [RER] (unit, 3 inputs)
    - Adhesive, organic, at plant [CH] (kilogram, 17 inputs)
    - xx Cover coat, organic, at plant [CH] (kilogram, 8 inputs)
    - Liquid storage tank, chemicals, organics [CH] (unit, 12 inputs)
- item: Electricity medium voltage UCTE  (input)
  quote: Electricity  Î  confidential  electricity production mix No UCTE  electricity, medium voltage, production UCTE, at grid  confidential kWh  CEWAG Düdingen, Herr Kurzo
  search: electricity medium voltage UCTE
  candidates:
    - Electricity, medium voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from hard coal, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from natural gas, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - xxx Electricity, medium voltage, production UCTE, at grid [UCTE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
- item: Thermal heat from oil firing extra light  (input)
  quote: Thermal heat from oil firing extra light  Î  confidential  oil heating systems No RER  heat, light fuel oil, at industrial furnace 1MW  confidential MJ  CEWAG Düdingen, Herr Kurzo
  search: heat light fuel oil industrial furnace 1MW
  candidates:
    - Heat, light fuel oil, at industrial furnace 1MW [RER] (megajoule, 1 inputs)
    - Heat, light fuel oil, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - District heat, at consumer, light fuel oil in industrial furnace 1MW [CH] (megajoule, 2 inputs)
    - Heat, heavy fuel oil, at industrial furnace 1MW [RER] (megajoule, 1 inputs)
    - Light fuel oil, burned in industrial furnace 1MW, non-modulating [RER] (megajoule, 5 inputs)
    - Heat, heavy fuel oil, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - Light fuel oil, burned in industrial furnace 1MW, non-modulating [CH] (megajoule, 5 inputs)
    - Light fuel oil, burned in industrial furnace, for asphalt production, 1MW, non-modulating [CH] (megajoule, 5 inputs)
- item: Transport rail  (input)
  quote: Transport rail  Î  Chemicals: 600 km, cement: 100 km, wood: 0 km  transport systems train No RER  transport, freight, rail  2.57E+01 tkm  estimated
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
- item: Transport lorry  (input)
  quote: Transport lorry  Î  Chemicals & cement: 100 km, wood: 0 km  transport systems road No RER  transport, lorry >16t, fleet average  2.22E+01 tkm  estimated
  search: transport lorry 16t fleet average
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, fleet average [RER] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
- item: plant (wooden board manufacturing plant, cement bonded boards)  (input)
  quote: plant  Î  wooden materials extraction Yes RER  wooden board manufacturing plant, cement bonded boards  4.00E-07 unit  estimated
  search: wooden board manufacturing plant cement bonded
  candidates:
    - Wooden board manufacturing plant, cement bonded boards [RER] (unit, 8 inputs)
    - Wooden board manufacturing plant, organic bonded boards [RER] (unit, 8 inputs)
- item: Waste heat into air  (emission to air)
  quote: Î  Waste heat into air  air unspecified  Heat, waste  3.29E+01 MJ  calculated
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
