You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (DE), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Explosives  (input)
  quote: Sprengstoff                          kg        9.45E-02     6.74E-02
  search: blasting explosives
  candidates:
    - Blasting [RER] (kilogram, 1 inputs)
    - Explosives, tovex, at plant [CH] (kilogram, 21 inputs)
- item: Diesel, excavation machinery  (input)
  quote: Diesel Abbaugerät                    l         5.40E-01     3.85E-01
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
- item: Electricity, crusher  (input)
  quote: Stromverbrauch Brecher               kWh       1.62E+00    1.16E+00
  search: electricity medium voltage grid
  candidates:
    - Electricity, medium voltage, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, DB, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production DE, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
- item: Electricity, conveyor belts  (input)
  quote: Stromverbrauch Förderbänder          kWh       7.02E-01     5.01E-01
  search: electricity medium voltage grid
  candidates:
    - Electricity, medium voltage, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, DB, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production DE, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
- item: Electricity, comminution  (input)
  quote: Stromverbrauch Zerkleinern           kWh       4.86E+00    3.47E+00
  search: electricity medium voltage grid
  candidates:
    - Electricity, medium voltage, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, DB, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production DE, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
- item: Heating oil EL, mill  (input)
  quote: Heizöl EL, Mühle                     l         2.00E-01     1.43E-01
  search: light fuel oil burned industrial furnace
  candidates:
    - Light fuel oil, burned in industrial furnace 1MW, non-modulating [RER] (megajoule, 5 inputs)
    - Light fuel oil, burned in industrial furnace 1MW, non-modulating [CH] (megajoule, 5 inputs)
    - Light fuel oil, burned in industrial furnace, for asphalt production, 1MW, non-modulating [CH] (megajoule, 5 inputs)
    - Heat, light fuel oil, at industrial furnace 1MW [RER] (megajoule, 1 inputs)
    - Heavy fuel oil, burned in industrial furnace 1MW, non-modulating [RER] (megajoule, 5 inputs)
    - Heat, light fuel oil, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - Heavy fuel oil, burned in industrial furnace 1MW, non-modulating [CH] (megajoule, 5 inputs)
    - District heat, at consumer, light fuel oil in industrial furnace 1MW [CH] (megajoule, 2 inputs)
- item: Electricity, burnt shale production  (input)
  quote: Stromverbrauch GÖS-Produktion        kWh       4.30E+01    3.07E+01
  search: electricity medium voltage grid
  candidates:
    - Electricity, medium voltage, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, DB, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production DE, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
- item: Electricity, power generation own use  (input)
  quote: Stromverbrauch Stromerzeugung        kWh       1.60E+01    1.14E+01
  search: electricity medium voltage grid
  candidates:
    - Electricity, medium voltage, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, DB, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production DE, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
- item: Water  (input)
  quote: Wasserverbrauch                      m3        7.00E-01     4.99E-01
  search: tap water user
  candidates:
    - Tap water, water balance according to MoeK 2013, at user [DE] (kilogram, 14 inputs)
    - Tap water, at user [RER] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin RER, at user [RER] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin OECD, at user [RER] (kilogram, 14 inputs)
    - Tap water, water balance according to MoeK 2013, at user [RER] (kilogram, 14 inputs)
    - Tap water, at user [CH] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin CH, at user [CH] (kilogram, 14 inputs)
    - Tap water, water balance according to MoeK 2013, at user [CH] (kilogram, 14 inputs)
- item: Hydrochloric acid  (input)
  quote: Salzsäure                            kg        1.00E-01     7.13E-02
  search: hydrochloric acid plant
  candidates:
    - Hydrochloric acid, 30% in H2O, at plant [RER] (kilogram, 2 inputs)
    - Hydrochloric acid, from Mannheim process, at plant [RER] (kilogram, 8 inputs)
    - xx Hydrochloric acid from benzene chlorination, at plant [RER] (kilogram, 9 inputs)
    - Hydrochloric acid, from the reaction of hydrogen with chlorine, at plant [RER] (kilogram, 6 inputs)
    - xx Hydrochloric acid, 36% in H2O, from reacting propylene and chlorine, at plant [RER] (kilogram, 10 inputs)
    - Anhydrite from hydrofluoric acid synthesis, at plant [DE] (kilogram, 8 inputs)
    - Adipic acid, at plant [RER] (kilogram, 7 inputs)
    - Formic acid, at plant [RER] (kilogram, 2 inputs)
- item: Sodium hydroxide  (input)
  quote: Natronlauge                          kg        1.00E-01     7.13E-02
  search: sodium hydroxide production mix
  candidates:
    - Sodium hydroxide, 50% in H2O, production mix, at plant [RER] (kilogram, 3 inputs)
    - Sodium sulphate, powder, production mix, at plant [RER] (kilogram, 4 inputs)
- item: Sodium hypochlorite (chlorine bleach)  (input)
  quote: Chlorbleichlauge                     kg        1.00E-01     7.13E-02
  search: sodium hypochlorite
  candidates:
    - Sodium hypochlorite, 15% in H2O, at plant [RER] (kilogram, 6 inputs)
    - Sodium cyanide, at plant [RER] (kilogram, 7 inputs)
    - Sodium phosphate, at plant [RER] (kilogram, 8 inputs)
    - Sodium dichromate, at plant [RER] (kilogram, 12 inputs)
    - Sodium chlorate, powder, at plant [RER] (kilogram, 13 inputs)
    - Sodium chloride, powder, at plant [RER] (kilogram, 10 inputs)
    - Sodium tripolyphosphate, at plant [RER] (kilogram, 4 inputs)
    - Sodium percarbonate, powder, at plant [RER] (kilogram, 0 inputs, aggregated)
- item: Organic chemicals  (input)
  quote: Chemikalien, org.                    kg        8.00E-02     5.70E-02
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
- item: Electricity, milling  (input)
  quote: Stromverbrauch Mahlen                kWh       3.00E+01    2.14E+01
  search: electricity medium voltage grid
  candidates:
    - Electricity, medium voltage, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, DB, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production DE, at grid [DE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
- item: Dust  (emission to air)
  quote: Staub                                kg        1.33E-03     9.48E-04
  candidates (flow name [compartment]):
    - Particles (PM10)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - particles (PM10)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Particles (> PM10)  [air] (kilogram, ef-3.1-biosphere)
    - Particles (PM2.5 - PM10)  [air] (kilogram, ef-3.1-biosphere)
    - Particles (PM10)  [soil] (kilogram, ef-3.1-biosphere)
    - Particles (PM10)  [water] (kilogram, ef-3.1-biosphere)
    - Particles (> PM10)  [soil] (kilogram, ef-3.1-biosphere)
    - Particles (> PM10)  [water] (kilogram, ef-3.1-biosphere)
- item: Nitrogen oxides  (emission to air)
  quote: Nox                                  kg        7.28E-01     5.19E-01
  candidates (flow name [compartment]):
    - Nitrogen Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Mustard  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Trifluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen oxide (N2O4)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Sulfur dioxide  (emission to air)
  quote: SO2                                  kg        6.37E-01     4.54E-01
  candidates (flow name [compartment]):
    - Sulfur Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [soil] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [water] (kilogram, ef-3.1-biosphere)
    - Sulfur  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
- item: Carbon dioxide, fossil  (emission to air)
  quote: davon fossil                         kg        3.59E+02     2.56E+02
  candidates (flow name [compartment]):
    - Carbon Dioxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (biogenic)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic-100yr)  [air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
- item: Carbon dioxide, geogenic (carbonate)  (emission to air)
  quote: davon geogen                         kg        2.33E+02     1.66E+02
  candidates (flow name [compartment]):
    - Carbon Dioxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (biogenic)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic-100yr)  [air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
- item: Carbon monoxide  (emission to air)
  quote: CO                                   kg        5.73E-01     4.09E-01
  candidates (flow name [compartment]):
    - Carbon Monoxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - carbon monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - carbon monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Black carbon  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
- item: Wastewater, unpolluted  (input)
  quote: Abwasser, unbelastet                 m3        1.50E-01     1.07E-01
  search: treatment sewage unpolluted
  candidates:
    - Treatment, sewage, unpolluted, to wastewater treatment, class 3 [CH] (cubic meter, 8 inputs)
    - Treatment, sewage, unpolluted, from residence, to wastewater treatment, class 2 [CH] (cubic meter, 9 inputs)
    - Treatment, sewage, to wastewater treatment, class 1 [CH] (cubic meter, 30 inputs)
    - Treatment, sewage, to wastewater treatment, class 2 [CH] (cubic meter, 30 inputs)
    - Treatment, sewage, to wastewater treatment, class 3 [CH] (cubic meter, 30 inputs)
    - Treatment, sewage, to wastewater treatment, class 4 [CH] (cubic meter, 30 inputs)
    - Treatment, sewage, to wastewater treatment, class 5 [CH] (cubic meter, 30 inputs)
    - Treatment, sewage grass refinery, to wastewater treatment, class 3 [CH] (cubic meter, 20 inputs)
- item: Transport, heating oil by rail  (input)
  quote: Heizöl                                       km                 600               0
  search: transport freight rail
  candidates:
    - Transport, freight, rail [DE] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [DE] (ton kilometer, 9 inputs)
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [RER] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
- item: Transport, hydrochloric acid by rail  (input)
  quote: Salzsäure                                    km                 200              100
  search: transport freight rail
  candidates:
    - Transport, freight, rail [DE] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [DE] (ton kilometer, 9 inputs)
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [RER] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
- item: Transport, hydrochloric acid by lorry  (input)
  quote: Salzsäure                                    km                 200              100
  search: transport freight lorry 16t-32t
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2020, EURO-VI, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2002, EURO-III, long haul [RER] (ton kilometer, 11 inputs)
- item: Transport, sodium hydroxide by rail  (input)
  quote: Natronlauge                                  km                 600              100
  search: transport freight rail
  candidates:
    - Transport, freight, rail [DE] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [DE] (ton kilometer, 9 inputs)
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [RER] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
- item: Transport, sodium hydroxide by lorry  (input)
  quote: Natronlauge                                  km                 600              100
  search: transport freight lorry 16t-32t
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2020, EURO-VI, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2002, EURO-III, long haul [RER] (ton kilometer, 11 inputs)
- item: Transport, hypochlorite by rail  (input)
  quote: Chlorbleichlauge                             km                 600              100
  search: transport freight rail
  candidates:
    - Transport, freight, rail [DE] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [DE] (ton kilometer, 9 inputs)
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [RER] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
- item: Transport, hypochlorite by lorry  (input)
  quote: Chlorbleichlauge                             km                 600              100
  search: transport freight lorry 16t-32t
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2020, EURO-VI, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2002, EURO-III, long haul [RER] (ton kilometer, 11 inputs)

Return only the JSON object described by the schema.
