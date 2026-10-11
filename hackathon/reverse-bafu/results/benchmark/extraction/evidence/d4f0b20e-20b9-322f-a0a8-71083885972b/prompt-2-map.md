You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Aluminium, Produktionsmix, ab Werk  (input)
  quote:                   Aluminium, Produktionsmix, ab Werk          126         kg
  search: aluminium production mix at plant
  candidates:
    - Aluminiumtrihydroxide-acrylic glass, production mix, at plant [CH] (kilogram, 6 inputs)
    - Aluminium, production mix for aluminium profiles, SZFF 2014, at plant [CH] (kilogram, 3 inputs)
    - Aluminium, production mix, at plant [RER] (kilogram, 3 inputs)
    - Aluminium, production mix, cast alloy, at plant [RER] (kilogram, 3 inputs)
    - Aluminium, production mix, wrought alloy, at plant [RER] (kilogram, 3 inputs)
    - Synthetic gas, production mix, at plant [CH] (cubic meter, 2 inputs)
    - Electricity, production mix photovoltaic, at plant [CH] (kilowatt hour, 29 inputs)
    - Formaldehyde, production mix, at plant [RER] (kilogram, 6 inputs)
- item: Polystyrol schlagfest  (input)
  quote:                   Polystyrol schlagfest                        66         kg
  search: polystyrene high impact at plant
  candidates:
    - Polystyrene, high impact, HIPS, at plant [RER] (kilogram, 8 inputs)
- item: Polyethylen (LD)  (input)
  quote:                   Polyethylen (LD)                            101         kg
  search: polyethylene LDPE granulate at plant
  candidates:
    - Polyethylene, LDPE, granulate, at plant [RER] (kilogram, 16 inputs, aggregated)
    - Polyethylene, HDPE, granulate, at plant [RER] (kilogram, 17 inputs, aggregated)
    - Polyethylene, LLDPE, granulate, at plant [RER] (kilogram, 17 inputs, aggregated)
    - Polyethylene terephthalate, granulate, amorphous, at plant [RER] (kilogram, 16 inputs)
    - Polyethylene terephthalate, granulate, bottle grade, at plant [RER] (kilogram, 1 inputs, aggregated)
- item: Zement  (input)
  quote:                   Zement                                      900         kg
  search: cement unspecified at plant
  candidates:
    - Cement, unspecified, at plant [CH] (kilogram, 5 inputs)
    - Cement plant [CH] (unit, 4 inputs)
    - CEM I cement, at plant [CH] (kilogram, 10 inputs)
    - Cement ZN, D, at plant [CH] (kilogram, 0 inputs, aggregated)
    - White cement, at plant [CH] (kilogram, 32 inputs)
    - Cement mortar, at plant [CH] (kilogram, 8 inputs)
    - Cement plaster, at plant [CH] (kilogram, 12 inputs)
    - CEM II, A cement, at plant [CH] (kilogram, 12 inputs)
- item: Sand für Bau  (input)
  quote:                   Sand für Bau                              4'650         kg
  search: silica sand at plant
  candidates:
    - Silica sand, at plant [DE] (kilogram, 2 inputs)
    - Hard sandstone, at plant [CH] (cubic meter, 15 inputs)
    - Portland slag sand cement, at plant [CH] (kilogram, 7 inputs)
    - Silicate plaster, dispersion, at plant [CH] (kilogram, 20 inputs)
    - Sand / concrete gravel, in sorting plant [CH] (kilogram, 1 inputs)
    - xx Disposal, building, plaster-cardboard sandwich, to sorting plant [CH] (kilogram, 7 inputs)
    - Disposal, building, plaster-cardboard sandwich, at sorting plant, to recycling [CH] (kilogram, 6 inputs)
    - Sodium silicate, spray powder 80%, at plant [RER] (kilogram, 10 inputs)
- item: Wasser  (resource to resources)
  quote:                   Wasser                                        0.45      m3
  candidates (flow name [compartment]):
    - Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - lake water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - river water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Ground Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water To Cooling  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water to turbine  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water, salt, sole  [resources / in water] (cubic meter, bafu-2026-residual)
    - Water, salt, ocean  [resources / in water] (cubic meter, bafu-2026-residual)
- item: Transport Schiene  (input)
  quote:                   Transport Schiene                           160         tkm
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
- item: Transport LKW 28 t  (input)
  quote:                   Transport LKW 28 t                          128         tkm
  search: transport lorry 28t
  candidates:
    - Disposal, lorry 28t [CH] (unit, 6 inputs)
    - Maintenance, lorry 28t [CH] (unit, 11 inputs)
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - xxx Operation, lorry >28t, fleet average [CH] (kilometer, 1 inputs)
    - xxx Operation, lorry 20-28t, fleet average [CH] (kilometer, 1 inputs)
    - Operation, lorry 28t, rape methyl ester 100% [CH] (kilometer, 1 inputs)
    - Transport, municipal waste collection, lorry 21t [CH] (ton kilometer, 5 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)
- item: Abfall in Inertstoffdeponie  (input)
  quote:                   Abfall in Inertstoffdeponie               5'730         kg
  search: disposal inert material landfill
  candidates:
    - Disposal, inert material, 0% water, to sanitary landfill [CH] (kilogram, 10 inputs)
    - Disposal, concrete, 5% water, to inert material landfill [GLO] (kilogram, 0 inputs)
    - xx Inert material landfill facility [CH] (unit, 10 inputs)
    - Process-specific burdens, inert material landfill [CH] (kilogram, 3 inputs)
    - Disposal, inert waste, 5% water, to construction waste landfill [CH] (kilogram, 18 inputs)
    - Disposal, cement, hydrated, 0% water, to residual material landfill [CH] (kilogram, 2 inputs)
    - Disposal, drilling waste, 71.5% water, to residual material landfill [CH] (kilogram, 2 inputs)
    - Disposal, frit for CRT tube production, to residual material landfill [CH] (kilogram, 6 inputs)
- item: Kunststoff in Verbrennungsanlage  (input)
  quote:                   Kunststoff in Verbrennungsanlage            167         kg
  search: disposal plastics municipal incineration
  candidates:
    - Disposal, plastics, mixture, 15.3% water, to municipal incineration [CH] (kilogram, 20 inputs)
    - Disposal, plastics as construction waste, to municipal waste incineration [CH] (kilogram, 2 inputs)
    - Disposal, plastics conduits as building waste, to municipal waste incineration [CH] (kilogram, 2 inputs)
    - Disposal, polystyrene plastics as building waste, to municipal waste incineration [CH] (kilogram, 2 inputs)
    - Disposal, plastics conduits ABS as building waste, to municipal waste incineration [CH] (kilogram, 2 inputs)
    - Disposal, plastics conduits PVC as building waste, to municipal waste incineration [CH] (kilogram, 2 inputs)
    - Disposal, pure hydrocarbon plastics as building waste, to municipal waste incineration [CH] (kilogram, 2 inputs)
    - Disposal, plastics conduits PE or PP as building waste, to municipal waste incineration [CH] (kilogram, 2 inputs)

Return only the JSON object described by the schema.
