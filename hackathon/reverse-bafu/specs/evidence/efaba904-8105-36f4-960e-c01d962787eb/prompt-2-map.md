You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Industrial residual wood softwood (u=40%), at plant  (input)
  quote: Industrial residual wood softwood (u=40%), at plant  Î  wooden materials extraction No RER  industrial residue wood, mix, softwood, u=40%, at plant  2.33E-01 m3
  search: industrial residue wood softwood
  candidates:
    - xxx Industrial residue wood, mix, softwood, u=40%, at plant [RER] (cubic meter, 3 inputs)
    - xxx Industrial residue wood, LTE production, softwood, u=20%, at plant [RER] (cubic meter, 6 inputs)
    - xxx Industrial residue wood, softwood, plant-debarked, u=70%, at plant [RER] (cubic meter, 5 inputs)
    - xxx Industrial residue wood, softwood, forest-debarked, u=70%, at plant [RER] (cubic meter, 5 inputs)
    - xxx Industrial residue wood, wood wool production, softwood, u=20%, at plant [RER] (cubic meter, 1 inputs)
    - xxx Industrial residue wood, 3-layered LB production, softwood, u=20%, at plant [RER] (cubic meter, 11 inputs)
    - xxx Industrial residue wood, from planing, softwood, air dried, u=20%, at plant [RER] (cubic meter, 4 inputs)
    - xxx Industrial residue wood, from planing, softwood, kiln dried, u=10%, at plant [RER] (cubic meter, 4 inputs)
- item: Industrial residual wood hardwood (u=40%), at plant  (input)
  quote: Industrial residual wood hardwood (u=40%), at plant  Î  Wood mix: 25% hardwood (beech), 75% softwood (pine and spruce)  wooden materials extraction No RER  industrial residue wood, mix, hardwood, u=40%, at plant  2.31E-02 m3
  search: industrial residue wood hardwood
  candidates:
    - xxx Industrial residue wood, mix, hardwood, u=40%, at plant [RER] (cubic meter, 5 inputs)
    - xxx Industrial residue wood, LTE production, hardwood, u=20%, at plant [RER] (cubic meter, 1 inputs)
    - xxx Industrial residue wood, hardwood, including bark, u=70%, at plant [RER] (cubic meter, 5 inputs)
    - xxx Industrial residue wood, from planing, hardwood, kiln dried, u=10%, at plant [RER] (cubic meter, 4 inputs)
    - xxx Industrial residue wood, hardwood, including bark, air dried, u=20%, at plant [RER] (cubic meter, 2 inputs)
    - xxx Industrial residue wood, plywood prod., indoor use, hardwood, u=20%, at plant [RER] (cubic meter, 1 inputs)
    - xxx Industrial residue wood, plywood prod., outdoor use, hardwood, u=20%, at plant [RER] (cubic meter, 1 inputs)
    - xxx Industrial residue wood, mix, softwood, u=40%, at plant [RER] (cubic meter, 3 inputs)
- item: Industrial wood beech, at forest road (u=80%)  (input)
  quote: Industrial wood beech, at forest road (u=80%)  Î  sources: 70% industrial residual wood, 30 % industrial wood  wooden materials extraction No RER  industrial wood, hardwood, under bark, u=80%, at forest road  3.74E-02 m3
  search: industrial wood hardwood under bark forest
  candidates:
    - xxx Industrial wood, hardwood, under bark, u=80%, at forest road [RER] (cubic meter, 6 inputs)
    - xxx Industrial wood, Scandinavian hardwood, under bark, u=80%, at forest road [NORDEL] (cubic meter, 7 inputs)
    - xxx Round wood, hardwood, under bark, u=70%, at forest road [RER] (cubic meter, 5 inputs)
    - xxx Residual wood, hardwood, under bark, u=80%, at forest road [RER] (cubic meter, 6 inputs)
    - xxx Industrial wood, softwood, under bark, u=140%, at forest road [RER] (cubic meter, 6 inputs)
    - xxx Residual wood, hardwood, under bark, air dried, u=20%, at forest road [RER] (cubic meter, 2 inputs)
    - Pulpwood, hardwood, sustainable forest management, measured as solid wood under bark, at forest road [RER] (cubic meter, 4 inputs)
    - Sawlog and veneer log, hardwood, sustainable forest management, measured as solid wood under bark, at forest road [RER] (cubic meter, 4 inputs)
- item: Industrial wood spruce, at forest road (u=140%)  (input)
  quote: Industrial wood spruce, at forest road (u=140%)  Î  wooden materials extraction No RER  industrial wood, softwood, under bark, u=140%, at forest road  5.30E-02 m3
  search: industrial wood softwood under bark forest
  candidates:
    - xxx Industrial wood, softwood, under bark, u=140%, at forest road [RER] (cubic meter, 6 inputs)
    - Industrial wood, softwood, under bark, u=140%, holzpur, at forest road [CH] (cubic meter, 5 inputs)
    - xxx Industrial wood, Scandinavian softwood, under bark, u=140%, at forest road [NORDEL] (cubic meter, 7 inputs)
    - xxx Round wood, softwood, under bark, u=70% at forest road [RER] (cubic meter, 5 inputs)
    - xxx Residual wood, softwood, under bark, u=140%, at forest road [RER] (cubic meter, 6 inputs)
    - xxx Industrial wood, hardwood, under bark, u=80%, at forest road [RER] (cubic meter, 6 inputs)
    - xxx Residual wood, softwood, under bark, air dried, u=20%, at forest road [RER] (cubic meter, 2 inputs)
    - Pulpwood, softwood, sustainable forest management, measured as solid wood under bark, at forest road [RER] (cubic meter, 5 inputs)
- item: Portland Cement  (input)
  quote: Portland Cement  Î  construction materials binder No CH  cement, unspecified, at plant  8.00E+02 kg  Schniewind 1989, p. 197 ff.
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
  quote: Process and cooling water  Î  evaporates partly during pressing and drying  resource in water  Water, cooling, unspecified natural origin  3.00E-01 m3  Schniewind 1989, p. 197 ff.
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
  quote: Organic chemicals  Î  Additives  chemicals organics No GLO  chemicals organic, at plant  4.50E+01 kg  Schniewind 1989, p. 197 ff.
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
- item: Electricity medium voltage - at grid UCTE  (input)
  quote: Electricity medium voltage - at grid UCTE  Î  Total consumption estimated: chipping according to Wegner and Frühwald; board production according to data on cement-bonded woodwool board production  electricity production mix No UCTE  confidential kWh
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
  quote: Thermal heat from oil firing extra light  Î  Total consumption estimated based on data on cement-bonded wood wool board production  oil heating systems No RER  heat, light fuel oil, at industrial furnace 1MW  confidential MJ  CEWAG Düdingen, Herr Kurzo
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
  quote: Transport rail  Î  Chemicals: 600 km, wood & cement: 100 km  transport systems train No RER  transport, freight, rail  1.34E+02 tkm  estimated
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
  quote: Transport lorry  Î  Chemicals & cement: 100 km, wood: 50 km  transport systems road No RER  transport, lorry >16t, fleet average  9.80E+01 tkm  estimated
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
  quote: Î  Waste heat into air  air unspecified  Heat, waste  8.77E+01 MJ  calculated
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
