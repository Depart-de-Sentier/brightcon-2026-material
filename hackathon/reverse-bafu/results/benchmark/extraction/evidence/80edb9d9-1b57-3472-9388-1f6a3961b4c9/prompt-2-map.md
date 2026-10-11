You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: industrial machine, heavy, unspecified, at plant  (input)
  quote:                          Î                                                                                                                                                     machinery             Yes    RER                                       1.50E-03 kg                                 1     3.45   (5,na,na,na,4,na);
  search: industrial machine heavy unspecified
  candidates:
    - Industrial machine, heavy, unspecified, at plant [RER] (kilogram, 8 inputs)
- item: electricity, medium voltage, production UCTE, at grid  (input)
  quote:                                                                                                                                                                                                    electricity, medium voltage,                                                                                                                      3.09E-03 kWh                                1     1.51   (1,2,1,1,4,1);
  search: electricity medium voltage UCTE
  candidates:
    - Electricity, medium voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from hard coal, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from natural gas, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - xxx Electricity, medium voltage, production UCTE, at grid [UCTE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, residual mix [CH] (kilowatt hour, 3 inputs)
    - xxx Electricity, medium voltage, GO supply mix [CH] (kilowatt hour, 3 inputs)
- item: EUR-flat pallet  (input)
  quote: pallets, at plant        Î                                                                                                                    wooden materials processing            No     RER    EUR-flat pallet                    6.25E-05 unit                               1     1.68   (4,5,1,1,4,5);
  search: EUR-flat pallet
  candidates:
    - EUR-flat pallet [RER] (unit, 3 inputs)
- item: extrusion, plastic film  (input)
  quote: plastic foil extrusion   Î                                                                       layer of plastic with a weight of 0.0123     plastics         processing            No     RER    extrusion, plastic film            6.15E-05 kg      folien.de/hpage.htm,       1     1.56   (4,na,na,na,4,na);
  search: extrusion plastic film
  candidates:
    - Extrusion, plastic film [RER] (kilogram, 16 inputs)
    - Extrusion, plastic pipes [RER] (kilogram, 13 inputs)
- item: polyethylene, HDPE, granulate, at plant  (input)
  quote: plastic foil             Î                                                                       layer of plastic with a weight of 0.0123     plastics         polymers              No     RER                                       6.15E-05 kg      folien.de/hpage.htm,       1     1.56   (4,na,na,na,4,na);
  search: polyethylene HDPE granulate
  candidates:
    - Polyethylene, HDPE, granulate, at plant [RER] (kilogram, 17 inputs, aggregated)
    - Polyethylene, LDPE, granulate, at plant [RER] (kilogram, 16 inputs, aggregated)
    - Polyethylene, LLDPE, granulate, at plant [RER] (kilogram, 17 inputs, aggregated)
    - Polyethylene terephthalate, granulate, amorphous, at plant [RER] (kilogram, 16 inputs)
    - Polyethylene terephthalate, granulate, bottle grade, at plant [RER] (kilogram, 1 inputs, aggregated)
- item: transport, freight, rail  (input)
  quote: and plastic foil to plant Î                                                                                                                     transport systems train              No     CH     transport, freight, rail           1.39E-03 tkm                                1     2.46   (5,na,na,na,4,na);
  search: transport freight rail
  candidates:
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting, Betrieb [CH] (ton kilometer, 2 inputs)
    - Transport, freight, rail, electricity with shunting, Fahrzeug [CH] (ton kilometer, 5 inputs)
    - Transport, freight, rail, electricity with shunting, Infrastruktur [CH] (ton kilometer, 3 inputs)
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
- item: transport, lorry 20-28t, fleet average  (input)
  quote: and plastic foil to plant Î                                                                                                                     transport systems road               No     CH                                        1.39E-03 tkm                                1     2.46   (5,na,na,na,4,na);
  search: transport lorry 20-28t fleet average
  candidates:
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - xxx Operation, lorry >28t, fleet average [CH] (kilometer, 1 inputs)
    - xxx Operation, lorry 20-28t, fleet average [CH] (kilometer, 1 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [CH] (ton kilometer, 20 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
- item: transport, lorry 3.5-16t, fleet average  (input)
  quote: foil to municipal        Î                                                                                                                      transport systems road               No     RER                                       6.15E-07 tkm                                1     1.78   (5,na,na,na,4,na);
  search: transport lorry 3.5-16t fleet average
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [CH] (ton kilometer, 20 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
- item: disposal, wood untreated, 20% water, to municipal incineration  (input)
  quote:                                                                           Î                                                                                                        No     CH                                        1.83E-03 kg      EMPA                       1     1.32   (1,4,1,2,3,5);
  search: disposal wood untreated municipal incineration
  candidates:
    - Disposal, wood untreated, 20% water, to municipal incineration [CH] (kilogram, 20 inputs)
    - Disposal, ash horse dung and wood chips, to municipal incineration [CH] (kilogram, 18 inputs)
    - Disposal, wood ash mixture, pure, 0% water, to municipal incineration [CH] (kilogram, 5 inputs)
    - Disposal, wood pole, chrome preserved, 20% water, to municipal incineration [CH] (kilogram, 20 inputs)
    - Disposal, building wood, chrome preserved, 20% water, to municipal incineration [CH] (kilogram, 20 inputs)
    - Disposal, 3-layered laminated wood board, 4% binder, to municipal waste incineration [CH] (kilogram, 3 inputs)
    - Disposal, wood fibre board 1.25% binder as building waste, to municipal waste incineration [CH] (kilogram, 3 inputs)
    - Disposal, wood particle board 10% binder as building waste, to municipal waste incineration [CH] (kilogram, 3 inputs)
- item: disposal, polyethylene, 0.4% water, to municipal incineration  (input)
  quote:                                                                           Î   municipal waste                                                                        No     CH                                        6.15E-05 kg                                 1     1.56   (4,na,na,na,4,na);
  search: disposal polyethylene municipal incineration
  candidates:
    - Disposal, polyethylene, 0.4% water, to municipal incineration [CH] (kilogram, 20 inputs)
    - Disposal, polyethylene terephtalate, 0.2% water, to municipal incineration [CH] (kilogram, 20 inputs)
    - Disposal, polyethylene/polypropylene products, to municipal waste incineration [CH] (kilogram, 2 inputs)
    - Disposal, digester sludge, to municipal incineration [CH] (kilogram, 20 inputs)
    - Disposal, glass, 0% water, to municipal incineration [CH] (kilogram, 5 inputs)
    - Disposal, paint, 0% water, to municipal incineration [CH] (kilogram, 20 inputs)
    - Disposal, steel, 0% water, to municipal incineration [CH] (kilogram, 5 inputs)
    - Disposal, ash olive pomace, to municipal incineration [CH] (kilogram, 16 inputs)
- item: Heat, waste  (emission to air)
  quote:                                                                           Î   waste heat         Same amount as electricity used                air               unspecified                      Heat, waste                        1.11E-02 MJ                                 1     1.57   (1,3,1,1,4,5);
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
