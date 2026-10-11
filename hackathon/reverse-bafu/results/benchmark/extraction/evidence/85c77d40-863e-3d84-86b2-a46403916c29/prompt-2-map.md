You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: feldspar, at plant  (input)
  quote:       feldspar          Î                                                                           for ceramic mass                                 others                 No   RER    feldspar, at plant             3.79E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
  search: feldspar at plant
  candidates:
    - Feldspar, at plant [RER] (kilogram, 0 inputs, aggregated)
    - Planting [CH] (hectare, 4 inputs)
    - Cement plant [CH] (unit, 4 inputs)
    - Ceramic plant [CH] (unit, 3 inputs)
    - Brass, at plant [CH] (kilogram, 8 inputs)
    - Potato planting [CH] (hectare, 4 inputs)
    - Rock wool plant [CH] (unit, 4 inputs)
    - Bronze, at plant [CH] (kilogram, 8 inputs)
- item: kaolin, at plant  (input)
  quote:       kaolin            Î   sanitary ceramics, at regional storage; inputs                          for ceramic mass                  chemicals      inorganics             No   RER    kaolin, at plant               4.08E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
  search: kaolin at plant
  candidates:
    - Kaolin, at plant [RER] (kilogram, 15 inputs)
    - Planting [CH] (hectare, 4 inputs)
    - Cement plant [CH] (unit, 4 inputs)
    - Ceramic plant [CH] (unit, 3 inputs)
    - Brass, at plant [CH] (kilogram, 8 inputs)
    - Potato planting [CH] (hectare, 4 inputs)
    - Rock wool plant [CH] (unit, 4 inputs)
    - Bronze, at plant [CH] (kilogram, 8 inputs)
- item: clay, at mine  (input)
  quote:       clay              Î                                                                           for ceramic mass                                 additives              No   CH     clay, at mine                  4.25E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
  search: clay at mine
  candidates:
    - Mine, clay [CH] (unit, 3 inputs)
    - Clay, at mine [CH] (kilogram, 2 inputs)
    - Sand, at mine [CH] (kilogram, 17 inputs)
    - Mine, limestone [CH] (unit, 2 inputs)
    - Mine, gravel/sand [CH] (unit, 3 inputs)
    - Limestone, at mine [CH] (kilogram, 5 inputs)
    - Clay plaster, at plant [CH] (kilogram, 7 inputs)
    - Gravel, round, at mine [CH] (kilogram, 17 inputs)
- item: silica sand, at plant  (input)
  quote:       porcelain meal,   Î                                                                           for ceramic mass                                 additives              No    DE    silica sand, at plant          2.20E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
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
- item: chemicals inorganic, at plant  (input)
  quote:                         Î                                                                           for ceramic mass                  chemicals      inorganics             No   GLO                                   2.75E-03   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
  search: chemicals inorganic at plant
  candidates:
    - Chemicals inorganic, at plant [GLO] (kilogram, 20 inputs)
    - Wood preservative, inorganic salt, containing Cr, at plant [RER] (kilogram, 0 inputs, aggregated)
    - Chemicals organic, at plant [GLO] (kilogram, 20 inputs)
- item: silica sand, at plant (glazing)  (input)
  quote:       oxydic minerals   Î                                                                           for glazing                                      additives              No    DE    silica sand, at plant          3.17E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
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
- item: chemicals inorganic, at plant (pigments)  (input)
  quote:       pigments          Î                                                                           for glazing                       chemicals      inorganics             No   GLO                                   2.87E-04   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
  search: chemicals inorganic at plant
  candidates:
    - Chemicals inorganic, at plant [GLO] (kilogram, 20 inputs)
    - Wood preservative, inorganic salt, containing Cr, at plant [RER] (kilogram, 0 inputs, aggregated)
    - Chemicals organic, at plant [GLO] (kilogram, 20 inputs)
- item: kaolin, at plant (glazing)  (input)
  quote:       refractories,     Î                                                                           for glazing                       chemicals      inorganics             No   RER    kaolin, at plant               3.63E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,3)
  search: kaolin at plant
  candidates:
    - Kaolin, at plant [RER] (kilogram, 15 inputs)
    - Planting [CH] (hectare, 4 inputs)
    - Cement plant [CH] (unit, 4 inputs)
    - Ceramic plant [CH] (unit, 3 inputs)
    - Brass, at plant [CH] (kilogram, 8 inputs)
    - Potato planting [CH] (hectare, 4 inputs)
    - Rock wool plant [CH] (unit, 4 inputs)
    - Bronze, at plant [CH] (kilogram, 8 inputs)
- item: stucco, at plant  (input)
  quote:       gypsum            Î                                                                           for mould                                        binder                 No   CH     stucco, at plant               1.25E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,4)
  search: stucco at plant
  candidates:
    - Stucco, at plant [CH] (kilogram, 5 inputs)
    - Planting [CH] (hectare, 4 inputs)
    - Cement plant [CH] (unit, 4 inputs)
    - Ceramic plant [CH] (unit, 3 inputs)
    - Brass, at plant [CH] (kilogram, 8 inputs)
    - Potato planting [CH] (hectare, 4 inputs)
    - Rock wool plant [CH] (unit, 4 inputs)
    - Bronze, at plant [CH] (kilogram, 8 inputs)
- item: polyethylene, HDPE, granulate, at plant  (input)
  quote:       plastic forms     Î                                                                           for mould                         plastics       polymers               No   RER                                   1.51E-03   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,4)
  search: polyethylene HDPE granulate at plant
  candidates:
    - Polyethylene, HDPE, granulate, at plant [RER] (kilogram, 17 inputs, aggregated)
    - Polyethylene, LDPE, granulate, at plant [RER] (kilogram, 16 inputs, aggregated)
    - Polyethylene, LLDPE, granulate, at plant [RER] (kilogram, 17 inputs, aggregated)
    - Polyethylene terephthalate, granulate, amorphous, at plant [RER] (kilogram, 16 inputs)
    - Polyethylene terephthalate, granulate, bottle grade, at plant [RER] (kilogram, 1 inputs, aggregated)
- item: natural gas, burned in industrial furnace >100kW  (input)
  quote:       natural gas       Î                                                                           for heating                       natural gas    heating systems        No   RER                                   2.41E+01   MJ     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,1)
  search: natural gas burned in industrial furnace >100kW
  candidates:
    - Natural gas, burned in industrial furnace 1MW [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace 1MWth [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace, for asphalt production, 1MWth [CH] (megajoule, 4 inputs)
    - xxx Heat, natural gas, at industrial furnace low-NOx >100kW [RER] (megajoule, 1 inputs)
- item: electricity, medium voltage, production UCTE, at grid  (input)
  quote:       electricity       Î                                                                           total consumption                 electricity    production mix         No   UCTE                                  8.78E-01   kWh    ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,2)
  search: electricity medium voltage production UCTE at grid
  candidates:
    - Electricity, medium voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from hard coal, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from natural gas, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - xxx Electricity, medium voltage, production UCTE, at grid [UCTE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from oil, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, high voltage, production from oil, UCTE at grid [CH] (kilowatt hour, 2 inputs)
    - Electricity, low voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
- item: Water, well, in ground  (resource to resources)
  quote:       well water        Î                                                                           total consumption                 resource       in water                           Water, well, in ground         1.06E-02   m3     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,4)
  candidates (flow name [compartment]):
    - (no candidate found)
- item: tap water, at user  (input)
  quote:       tap water         Î                                                                           total consumption                 water supply production               No   RER    tap water, at user             5.41E-01   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,4)
  search: tap water at user
  candidates:
    - Tap water, at user [CH] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin CH, at user [CH] (kilogram, 14 inputs)
    - Tap water, water balance according to MoeK 2013, at user [CH] (kilogram, 14 inputs)
    - Tap water, at user [RER] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin RER, at user [RER] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin OECD, at user [RER] (kilogram, 14 inputs)
    - Tap water, water balance according to MoeK 2013, at user [RER] (kilogram, 14 inputs)
    - Tap water, water balance according to MoeK 2013, at user [DE] (kilogram, 14 inputs)
- item: transport, freight, rail  (input)
  quote:       transport         Î                                                                                                                            train                  No   CH     transport, freight, rail       6.00E-01   tkm    estimated        1     2.09
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
- item: transport, lorry >16t, fleet average  (input)
  quote:       transport         Î                                                                                                                            road                   No   RER                                   8.14E-02   tkm    estimated        1     2.09
  search: transport lorry >16t fleet average
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [CH] (ton kilometer, 20 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
- item: ceramic plant  (input)
  quote:       infrastructure    Î                                                                                                                            others             Yes      CH     ceramic plant                  4.00E-09   unit   ÖSPAG (2002)     1     3.02   (1,3,1,3,1,4,9)
  search: ceramic plant
  candidates:
    - Ceramic plant [CH] (unit, 3 inputs)
    - Planting [CH] (hectare, 4 inputs)
    - Cement plant [CH] (unit, 4 inputs)
    - Brass, at plant [CH] (kilogram, 8 inputs)
    - Potato planting [CH] (hectare, 4 inputs)
    - Rock wool plant [CH] (unit, 4 inputs)
    - Bronze, at plant [CH] (kilogram, 8 inputs)
    - Stucco, at plant [CH] (kilogram, 5 inputs)
- item: disposal, inert material, 0% water, to sanitary landfill (sanded ceramic)  (input)
  quote:                                                                                       Î                                                                    sanitary landfill         No   CH                                    9.40E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
  search: disposal inert material sanitary landfill
  candidates:
    - Disposal, inert material, 0% water, to sanitary landfill [CH] (kilogram, 10 inputs)
    - Disposal, organic-anorganic compound materials as building waste, to sanitary landfill [CH] (kilogram, 3 inputs)
    - Disposal, concrete, 5% water, to inert material landfill [GLO] (kilogram, 0 inputs)
- item: disposal, inert material, 0% water, to sanitary landfill (rumble)  (input)
  quote:                                                                                       Î rumble                                                             sanitary landfill         No   CH                                    3.19E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
  search: disposal inert material sanitary landfill
  candidates:
    - Disposal, inert material, 0% water, to sanitary landfill [CH] (kilogram, 10 inputs)
    - Disposal, organic-anorganic compound materials as building waste, to sanitary landfill [CH] (kilogram, 3 inputs)
    - Disposal, concrete, 5% water, to inert material landfill [GLO] (kilogram, 0 inputs)
- item: disposal, inert waste, 5% water, to inert material landfill  (input)
  quote:                                                                                       Î                                                                                              No   CH     water, to inert material       1.64E-03   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
  search: disposal inert waste inert material landfill
  candidates:
    - Disposal, inert material, 0% water, to sanitary landfill [CH] (kilogram, 10 inputs)
    - Disposal, inert waste, 5% water, to construction waste landfill [CH] (kilogram, 18 inputs)
    - Disposal, concrete, 5% water, to inert material landfill [GLO] (kilogram, 0 inputs)
- item: disposal, municipal solid waste, 22.9% water, to municipal incineration  (input)
  quote:                                                                                       Î municipal waste                                                                              No   CH     waste, 22.9% water, to         3.86E-02   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
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
- item: disposal, hazardous waste, 0% water, to underground deposit  (input)
  quote:                                                                                       Î                                                                                              No   DE     0% water, to underground       6.85E-05   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
  search: disposal hazardous waste underground deposit
  candidates:
    - Disposal, hazardous waste, 0% water, to underground deposit [DE] (kilogram, 13 inputs)
    - Disposal, waste, silicon wafer production, 0% water, to underground deposit [DE] (kilogram, 12 inputs)
- item: disposal, solvents mixture, 16.5% water, to hazardous waste incineration  (input)
  quote:                                                                                       Î                                                                                              No   CH     16.5% water, to hazardous      2.39E-06   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
  search: disposal solvents mixture hazardous waste incineration
  candidates:
    - Disposal, solvents mixture, 16.5% water, to hazardous waste incineration [CH] (kilogram, 20 inputs)
- item: disposal, used mineral oil, 10% water, to hazardous waste incineration (used oil)  (input)
  quote:                                                                                       Î used oil                                                                                     No   CH     10% water, to hazardous        1.88E-04   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
  search: disposal used mineral oil hazardous waste incineration
  candidates:
    - Disposal, used mineral oil, 10% water, to hazardous waste incineration [CH] (kilogram, 15 inputs)
- item: disposal, used mineral oil, 10% water, to hazardous waste incineration (fat)  (input)
  quote:                                                                                       Î fat                                                                                          No   CH     10% water, to hazardous        1.58E-06   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
  search: disposal used mineral oil hazardous waste incineration
  candidates:
    - Disposal, used mineral oil, 10% water, to hazardous waste incineration [CH] (kilogram, 15 inputs)
- item: disposal, bilge oil, 90% water, to hazardous waste incineration  (input)
  quote:                                                                                       Î                                                                                              No   CH     water, to hazardous waste      6.61E-05   kg     ÖSPAG (2002)     1     1.13   (1,3,1,3,1,4,6)
  search: disposal bilge oil hazardous waste incineration
  candidates:
    - Disposal, bilge oil, 90% water, to hazardous waste incineration [CH] (kilogram, 20 inputs)
    - Disposal, used mineral oil, 10% water, to hazardous waste incineration [CH] (kilogram, 15 inputs)

Return only the JSON object described by the schema.
