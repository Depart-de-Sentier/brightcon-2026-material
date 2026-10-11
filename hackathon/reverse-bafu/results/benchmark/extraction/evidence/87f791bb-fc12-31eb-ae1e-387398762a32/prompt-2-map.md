You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Water, cooling, unspecified natural origin  (resource to resources)
  quote: Res ource         Water, cooling, uns pecified natural origin                          m3        2.40E-02         1              1.88                       (5,5,1,1,4,5); es tim ated with data from a large chem . plant
  candidates (flow name [compartment]):
    - Water To Cooling  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water Cooling Sea  [water] (kilogram, ef-3.1-biosphere)
    - Water from cooling  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Water, unspecified natural origin  (resource to resources)
  quote:                   Water, uns pecified natural origin                                   m3        6.00E-03         1              1.88                       (5,5,1,1,4,5); es tim ated with data from a large chem . plant
  candidates (flow name [compartment]):
    - Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - lake water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - river water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Ground Water  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water To Cooling  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Water to turbine  [Resources / Resources from water] (cubic meter, ef-3.1-biosphere)
    - Clay, unspecified  [resources / in ground] (kilogram, bafu-2026-residual)
    - Water, salt, sole  [resources / in water] (cubic meter, bafu-2026-residual)
- item: ammonia, liquid, at regional storehouse  (input)
  quote: Input from        am m onia, liquid, at regional s torehous e              RER          kg       4.27E-04         1              1.21                        (4,na,na,na,na,na); es tim ation - equal to em itted am ount
  search: ammonia liquid regional storehouse
  candidates:
    - Ammonia, liquid, at regional storehouse [RER] (kilogram, 4 inputs)
    - Ammonia, liquid, at regional storehouse [CH] (kilogram, 4 inputs)
- item: copper, at regional storage  (input)
  quote: Technos phere     copper, at regional s torage                             RER          kg       8.15E-01         1              1.21                    (4,na,na,na,na,na); es tim ation bas ed on proces s yield 90-99.8%
  search: copper regional storage
  candidates:
    - Copper, at regional storage [RER] (kilogram, 13 inputs)
    - Tin, at regional storage [RER] (kilogram, 13 inputs)
    - Gold, at regional storage [RER] (kilogram, 4 inputs)
    - Lead, at regional storage [RER] (kilogram, 5 inputs)
    - Diesel, at regional storage [RER] (kilogram, 15 inputs)
    - Indium, at regional storage [RER] (kilogram, 7 inputs)
    - Petrol, at regional storage [RER] (kilogram, 16 inputs)
    - Silver, at regional storage [RER] (kilogram, 6 inputs)
- item: ammonium carbonate, at plant  (input)
  quote:                   am m onium carbonate, at plant                           RER          kg       1.21E-03         1              1.21                        (4,na,na,na,na,na); es tim ation - equal to em itted am ount
  search: ammonium carbonate plant
  candidates:
    - Ammonium carbonate, at plant [RER] (kilogram, 7 inputs)
    - Sodium carbonate from ammonium chloride production, at plant [GLO] (kilogram, 9 inputs)
    - Copper carbonate, at plant [RER] (kilogram, 8 inputs)
    - Ammonium bicarbonate, at plant [RER] (kilogram, 4 inputs)
    - Potassium carbonate from manganese dioxide oxidation, at plant [RER] (kilogram, 6 inputs)
    - Ammonium chloride, at plant [GLO] (kilogram, 9 inputs)
    - Lithium carbonate, at plant [GLO] (kilogram, 19 inputs)
    - Potassium carbonate, at plant [GLO] (kilogram, 7 inputs)
- item: electricity, medium voltage, production UCTE, at grid  (input)
  quote:                   electricity, m edium voltage, production UCTE, at grid   UCTE        kWh       3.33E-01         1              1.88                       (5,5,1,1,4,5); es tim ated with data from a large chem . plant
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
- item: heat, natural gas, at industrial furnace >100kW  (input)
  quote:                   heat, natural gas , at indus trial furnace >100kW        RER          MJ       2.00E+00         1              1.88                       (5,5,1,1,4,5); es tim ated with data from a large chem . plant
  search: heat natural gas industrial furnace
  candidates:
    - xxx Heat, natural gas, at industrial furnace low-NOx >100kW [RER] (megajoule, 1 inputs)
    - Heat, natural gas, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - District heat, at consumer, natural gas in industrial furnace 1MW [CH] (megajoule, 2 inputs)
    - Industrial furnace, 1MW, natural gas [RER] (unit, 18 inputs)
    - Natural gas, burned in industrial furnace 1MW [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace 1MWth [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace, for asphalt production, 1MWth [CH] (megajoule, 4 inputs)
- item: chemical plant, organics  (input)
  quote:                   chem ical plant, organics                                RER         unit      4.00E-10         1              3.77                                           (4,5,1,3,5,4); es tim ation
  search: chemical plant organics
  candidates:
    - Chemical plant, organics [RER] (unit, 4 inputs)
    - Heat, unspecific, in chemical plant [RER] (megajoule, 4 inputs)
    - Steam, for chemical processes, at plant [RER] (kilogram, 3 inputs)
    - Liquid storage tank, chemicals, organics [CH] (unit, 12 inputs)
    - Chemicals organic, at plant [GLO] (kilogram, 20 inputs)
    - Chemicals inorganic, at plant [GLO] (kilogram, 20 inputs)
- item: transport, freight, rail  (input)
  quote:                   trans port, freight, rail                                RER         tkm       4.90E-01         1              2.09                                  (4,5,na,na,na,na); s tandard dis tances
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
  quote:                   trans port, lorry 32t                                    RER         tkm       8.16E-02         1              2.09                                  (4,5,na,na,na,na); s tandard dis tances
  search: transport lorry 32t
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2020, EURO-VI, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2002, EURO-III, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, urban delivery [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, urban delivery [RER] (ton kilometer, 11 inputs)
- item: Heat, waste  (emission to air)
  quote: Air em is s ion   Heat, was te                                                          MJ       1.20E+00         1              1.88                              (5,5,1,1,4,5); calculated from electricity input
  candidates (flow name [compartment]):
    - Waste Heat  [air] (megajoule, ef-3.1-biosphere)
    - Energy, waste heat, air  [resources / in air] (megajoule, bafu-2026-residual)
    - Waste Heat  [soil] (megajoule, ef-3.1-biosphere)
    - Waste Heat  [water] (megajoule, ef-3.1-biosphere)
    - Heat, waste  [emissions to water / groundwater, long-term] (megajoule, bafu-2026-residual)
    - Waste water/m3  [emissions to water / unspecified] (cubic meter, bafu-2026-residual)
    - Waste water  [emissions to water / ocean] (kilogram, bafu-2026-residual)
    - Waste water  [emissions to water / river] (kilogram, bafu-2026-residual)
- item: Ammonia  (emission to air)
  quote:                   Am m onia                                                             kg       4.27E-04         1              2.32                                       (5,5,na,na,na,5); es tim ation
  candidates (flow name [compartment]):
    - Ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Ammonium carbonate  (emission to air)
  quote:                   Am m onium carbonate                                                  kg       1.21E-03         1              2.32                                       (5,5,na,na,na,5); es tim ation
  candidates (flow name [compartment]):
    - Ammonium  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonium Acetate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonium Bromide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonium Nitrate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonium oxalate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonium sulfate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonium Chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonium Fluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
