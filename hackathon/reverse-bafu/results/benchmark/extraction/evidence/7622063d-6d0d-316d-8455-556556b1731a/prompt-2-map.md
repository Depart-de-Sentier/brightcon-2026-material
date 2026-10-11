You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: diesel, burned in building machine  (input)
  quote: technosphere    diesel, burned in building machine             GLO         MJ         4.52E-3           4.52E-3           1 1.07 documentation ground granulated blast furnace slag
  search: diesel burned building machine
  candidates:
    - Diesel, burned in building machine, average [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, with particle filter [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, without particle filter [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, with particle filter, without building machine [CH] (megajoule, 3 inputs)
    - Diesel, burned in building machine, with particle filter, without building machine and lubricating oil [CH] (megajoule, 1 inputs)
    - Diesel, burned in building machine, with particle filter [GLO] (megajoule, 4 inputs)
    - Diesel, burned in agricultural machine [CH] (kilogram, 4 inputs)
    - Diesel, burned in auxillary machines at concrete crusher [CH] (kilogram, 4 inputs)
- item: electricity, medium voltage, production ENTSO, at grid  (input)
  quote:                                                                ENTSO kWh              9.12E-2           9.12E-2           1 1.07 documentation ground granulated blast furnace slag
  search: electricity medium voltage ENTSO
  candidates:
    - Electricity, medium voltage, import ENTSO, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production ENTSO-E, at grid [ENTSO-E] (kilowatt hour, 3 inputs)
    - xxx Electricity, medium voltage, production ENTSO, at grid [ENTSO-E] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, residual mix [CH] (kilowatt hour, 3 inputs)
- item: light fuel oil, at regional storage  (input)
  quote:                 light fuel oil, at regional storage            RER         kg         1.00E-3           1.00E-3           1 1.07 documentation ground granulated blast furnace slag
  search: light fuel oil regional storage
  candidates:
    - Light fuel oil, at regional storage [RER] (kilogram, 12 inputs)
    - Light fuel oil, at regional storage [CH] (kilogram, 14 inputs)
    - Heavy fuel oil, at regional storage [RER] (kilogram, 12 inputs)
    - Heavy fuel oil, at regional storage [CH] (kilogram, 14 inputs)
- item: lubricating oil, at plant  (input)
  quote:                 lubricating oil, at plant                      RER         kg         4.01E-6           4.01E-6           1 1.07 documentation ground granulated blast furnace slag
  search: lubricating oil plant
  candidates:
    - Lubricating oil, at plant [RER] (kilogram, 4 inputs)
    - Soya oil, at plant [RER] (kilogram, 10 inputs)
    - Oil power plant 500MW [RER] (unit, 19 inputs)
    - Heavy fuel oil, burned in power plant [RER] (megajoule, 12 inputs)
    - Fatty alcohol, from palm oil, at plant [RER] (kilogram, 10 inputs)
    - Fatty alcohol sulfate, palm oil, at plant [RER] (kilogram, 9 inputs)
    - Fatty alcohol, from coconut oil, at plant [RER] (kilogram, 10 inputs)
    - Fatty acids, from vegetarian oil, at plant [RER] (kilogram, 12 inputs)
- item: natural gas, high pressure, at consumer  (input)
  quote:                 natural gas, high pressure, at consumer        RER         MJ         3.23E-1           3.23E-1           1 1.07 documentation ground granulated blast furnace slag
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
- item: air filter, central unit, 600 m3/h, at plant  (input)
  quote:                 air filter, central unit, 600 m3/h, at plant   RER         unit       8.03E-5           8.03E-5           1 1.07 documentation ground granulated blast furnace slag
  search: air filter central unit
  candidates:
    - Air filter, central unit, 600 m3/h, at plant [RER] (unit, 13 inputs)
    - Disposal, air filter, central unit, 600 m3/h [CH] (unit, 3 inputs)
    - xx Air filter, decentralized unit, 250 m3/h, at plant [RER] (unit, 11 inputs)
    - Air filter, decentralized unit, 180-250 m3/h, at plant [RER] (unit, 11 inputs)
    - xx Disposal, air filter, decentralized unit, 250 m3/h [CH] (unit, 3 inputs)
    - Disposal, air filter, decentralized unit, 180-250 m3/h [CH] (unit, 3 inputs)
- item: cement plant  (input)
  quote:                 cement plant                                    CH         unit      5.36E-11          5.36E-11           1 3.00 documentation ground granulated blast furnace slag
  search: cement plant
  candidates:
    - Particle board, cement bonded, at plant [RER] (cubic meter, 0 inputs, aggregated)
    - Wood wool boards, cement bonded, at plant [RER] (cubic meter, 8 inputs)
    - xxx Wood wool boards, cement bonded, at plant [RER] (cubic meter, 0 inputs, aggregated)
    - Wooden board manufacturing plant, cement bonded boards [RER] (unit, 8 inputs)
    - Cement plant [CH] (unit, 4 inputs)
    - CEM I cement, at plant [CH] (kilogram, 10 inputs)
    - Cement ZN, D, at plant [CH] (kilogram, 0 inputs, aggregated)
    - White cement, at plant [CH] (kilogram, 32 inputs)
- item: solvents, organic, unspecified, at plant  (input)
  quote:                 solvents, organic, unspecified, at plant       GLO         kg         8.26E-7           8.26E-7           1 1.07 documentation ground granulated blast furnace slag
  search: solvents organic unspecified
  candidates:
    - Solvents, organic, unspecified, at plant [GLO] (kilogram, 15 inputs)
- item: ethylene glycol, at plant  (input)
  quote:                 ethylene glycol, at plant                      RER         kg         1.26E-6           1.26E-6           1 1.07 documentation ground granulated blast furnace slag
  search: ethylene glycol plant
  candidates:
    - Ethylene glycol, at plant [RER] (kilogram, 8 inputs, aggregated)
    - Ethylene glycol monoethyl ether, at plant [RER] (kilogram, 7 inputs)
    - xx Ethylene glycol diethyl ether, at plant [RER] (kilogram, 8 inputs)
    - xx Ethylene glycol dimethyl ether, at plant [RER] (kilogram, 7 inputs)
    - Ethylene oxide, at plant [RER] (kilogram, 7 inputs)
    - Ethylenediamine, at plant [RER] (kilogram, 8 inputs)
    - Ethylene bromide, at plant [RER] (kilogram, 6 inputs)
    - Diethylene glycol, at plant [RER] (kilogram, 3 inputs)
- item: steel, low-alloyed, at plant  (input)
  quote:                 steel, low-alloyed, at plant                   RER         kg         3.53E-4           3.53E-4           1 1.07 documentation ground granulated blast furnace slag
  search: steel low-alloyed plant
  candidates:
    - Steel, low-alloyed, at plant [RER] (kilogram, 3 inputs)
    - Steel, converter, low-alloyed, at plant [RER] (kilogram, 21 inputs)
    - Steel, electric, un- and low-alloyed, at plant [RER] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant, best plants (min. values) [RER] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant, worst plants (max. values) [RER] (kilogram, 17 inputs)
    - Steel, electric, low-alloyed, at plant [CH] (kilogram, 23 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [DE] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [FR] (kilogram, 16 inputs)
- item: disposal, inert waste, 5% water, to inert material landfill  (input)
  quote: technosphere                                                 CH         kg         1.12E-3           1.12E-3            1 1.07 documentation ground granulated blast furnace slag
  search: disposal inert waste landfill
  candidates:
    - Disposal, inert waste, 5% water, to construction waste landfill [CH] (kilogram, 18 inputs)
    - Disposal, inert material, 0% water, to sanitary landfill [CH] (kilogram, 10 inputs)
    - Disposal, glass, 0% water, to construction waste landfill [CH] (kilogram, 18 inputs)
    - Disposal, steel, 0% water, to construction waste landfill [CH] (kilogram, 18 inputs)
    - Disposal, cement, 5% water, to construction waste landfill [CH] (kilogram, 18 inputs)
    - Disposal, zeolite, 5% water, to construction waste landfill [CH] (kilogram, 18 inputs)
    - Disposal, concrete, 5% water, to construction waste landfill [CH] (kilogram, 18 inputs)
    - Disposal, gravel, 0.2% water, to construction waste landfill [CH] (kilogram, 18 inputs)
- item: treatment, concrete production effluent, to wastewater treatment, class 3  (input)
  quote:                                                              CH         m3         3.52E-4           3.52E-4            1 1.07 documentation ground granulated blast furnace slag
  search: treatment concrete production effluent
  candidates:
    - Treatment, concrete production effluent, to wastewater treatment, class 3 [CH] (cubic meter, 29 inputs)
    - Treatment hard fibreboard production effluent, to wastewater treatment, class 1 [RER] (cubic meter, 24 inputs)
    - Treatment, particle board production effluent, to wastewater treatment, class 1 [RER] (cubic meter, 16 inputs)
    - Treatment, soft fibreboard production effluent, to wastewater treatment, class 1 [RER] (cubic meter, 28 inputs)
    - Treatment, medium density fibreboard production effluent, to wastewater treatment, class 1 [RER] (cubic meter, 24 inputs)
    - Treatment, glass production effluent, to wastewater treatment, class 2 [CH] (cubic meter, 28 inputs)
    - Treatment, lorry production effluent, to wastewater treatment, class 1 [CH] (cubic meter, 24 inputs)
    - Treatment, PV cell production effluent, to wastewater treatment, class 3 [CH] (cubic meter, 29 inputs)
- item: transport, lorry 16-32t, EURO4  (input)
  quote:                transport, lorry 16-32t, EURO4                RER        tkm        3.59E-5           5.01E-2            1 2.05
  search: transport lorry 16-32t EURO4
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2020, EURO-VI, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2002, EURO-III, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, urban delivery [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, urban delivery [RER] (ton kilometer, 11 inputs)
- item: transport, freight, rail  (input)
  quote:                transport, freight, rail                      RER        tkm        7.43E-5           7.43E-5            1 2.05
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
- item: Carbon dioxide, fossil  (emission to air)
  quote:                 Carbon dioxide, fossil                            -        kg         1.97E-2           1.97E-2           1 1.07 documentation ground granulated blast furnace slag
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
  quote:                 Carbon monoxide, fossil                           -        kg         5.45E-5           5.45E-5           1 5.00 documentation ground granulated blast furnace slag
  candidates (flow name [compartment]):
    - Carbon Monoxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - carbon monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - carbon monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Black carbon  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
- item: Hydrogen sulfide  (emission to air)
  quote:                 Hydrogen sulfide                                  -        kg         2.70E-4           2.70E-4           1 1.50 documentation ground granulated blast furnace slag
  candidates (flow name [compartment]):
    - Hydrogen Sulfide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen Sulfide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Hydrogen Sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - hydrogen sulfide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - hydrogen sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Hydrogen  [air] (kilogram, ef-3.1-biosphere)
    - Hydrogen-3  [Emissions / Emissions to air] (kilo Becquerel, ef-3.1-biosphere)
    - Sulfide ion  [air] (kilogram, ef-3.1-biosphere)
- item: Methane, fossil  (emission to air)
  quote:                 Methane, fossil                                   -        kg         1.37E-6           1.37E-6           1 1.50 documentation ground granulated blast furnace slag
  candidates (flow name [compartment]):
    - Methanethiol  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methane (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methane (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methanesulfonic Acid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Fluoro(methoxy)methane  [air] (kilogram, ef-3.1-biosphere)
    - Sodium Methanethiolate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methyl Methanesulfonate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Difluoro(methoxy)methane  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Nitrogen oxides  (emission to air)
  quote:                 Nitrogen oxides                                   -        kg         2.42E-6           2.42E-6           1 1.50 documentation ground granulated blast furnace slag
  candidates (flow name [compartment]):
    - Nitrogen Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Mustard  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Trifluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen oxide (N2O4)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: NMVOC, non-methane volatile organic compounds, unspecified origin  (emission to air)
  quote:                                                                   -        kg         7.95E-7           7.95E-7           1 1.50 documentation ground granulated blast furnace slag
  candidates (flow name [compartment]):
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - non-methane volatile organic compounds  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - non-methane volatile organic compounds  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Particulates, > 2.5 um, and < 10um  (emission to air)
  quote:                 Particulates, > 2.5 um, and < 10um                -        kg         1.53E-6           1.53E-6           1 2.00 documentation ground granulated blast furnace slag
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Sulfur dioxide  (emission to air)
  quote:                 Sulfur dioxide                                    -        kg         2.31E-4           2.31E-4           1 1.07 documentation ground granulated blast furnace slag
  candidates (flow name [compartment]):
    - Sulfur Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [soil] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [water] (kilogram, ef-3.1-biosphere)
    - Sulfur  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
- item: Water (emission to air)  (emission to air)
  quote:                 Water                                             -        kg         1.38E-1           1.38E-1           1 1.50 documentation ground granulated blast furnace slag
  candidates (flow name [compartment]):
    - Water  [air] (cubic meter, ef-3.1-biosphere)
    - sea water  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Green Water  [air] (kilogram, ef-3.1-biosphere)
    - Water Vapour  [air] (kilogram, ef-3.1-biosphere)
    - Water, In Air  [air] (kilogram, ef-3.1-biosphere)
    - Water (evapotranspiration)  [air] (kilogram, ef-3.1-biosphere)
    - Raffinates (petroleum), Catalytic Reformer Ethylene Glycol-water Countercurrent Exts.  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Reaction Mass Of Potassium Didodecylphosphate And Dipotassium Dodecylphosphate And Water  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Water (emission to water)  (emission to water)
  quote:                 Water                                          -        kg         4.29E-1           4.29E-1            1 1.50 documentation ground granulated blast furnace slag
  candidates (flow name [compartment]):
    - Waste water/m3  [emissions to water / unspecified] (cubic meter, bafu-2026-residual)
    - Water  [Emissions / Emissions to water] (cubic meter, ef-3.1-biosphere)
    - Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water  [water] (cubic meter, ef-3.1-biosphere)
    - Sea Water  [water] (kilogram, ef-3.1-biosphere)
    - sea water  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - lake water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Waste water  [emissions to water / ocean] (kilogram, bafu-2026-residual)
- item: Heat, waste  (emission to air)
  quote:                Heat, waste                                     -        MJ         6.93E-1           6.93E-1            1 1.07 documentation ground granulated blast furnace slag
  candidates (flow name [compartment]):
    - Waste Heat  [air] (megajoule, ef-3.1-biosphere)
    - Energy, waste heat, air  [resources / in air] (megajoule, bafu-2026-residual)
    - Waste Heat  [soil] (megajoule, ef-3.1-biosphere)
    - Waste Heat  [water] (megajoule, ef-3.1-biosphere)
    - Heat, waste  [emissions to water / groundwater, long-term] (megajoule, bafu-2026-residual)
    - Waste water/m3  [emissions to water / unspecified] (cubic meter, bafu-2026-residual)
    - Waste water  [emissions to water / ocean] (kilogram, bafu-2026-residual)
    - Waste water  [emissions to water / river] (kilogram, bafu-2026-residual)
- item: Water, unspecified, Europe  (resource to resources)
  quote: resource, in   Water, unspecified, Europe                      -        m3         9.19E-4           9.19E-4            1 1.07 documentation ground granulated blast furnace slag
  candidates (flow name [compartment]):
    - Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - lake water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - river water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Ground Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water To Cooling  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water to turbine  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Clay, unspecified  [resources / in ground] (kilogram, bafu-2026-residual)
    - Water, salt, sole  [resources / in water] (cubic meter, bafu-2026-residual)

Return only the JSON object described by the schema.
