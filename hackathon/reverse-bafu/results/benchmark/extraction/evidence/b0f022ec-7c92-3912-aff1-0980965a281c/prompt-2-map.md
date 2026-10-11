You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (GLO), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Water, cooling, unspecified natural origin  (resource to resources)
  quote:                           4              -        Water, cooling, unspecified natural origin         -            -          m3        2.40E-2            1          1.30 (4,5,na,na,na,na); Estimation
  candidates (flow name [compartment]):
    - (no candidate found)
- item: boric acid, anhydrous, powder, at plant  (input)
  quote:                           5              -        boric acid, anhydrous, powder, at plant        RER              0          kg       1.86E+0             1          1.38 (4,5,1,1,1,5); Stoichiometric calculation
  search: boric acid anhydrous powder at plant
  candidates:
    - Boric acid, anhydrous, powder, at plant [RER] (kilogram, 7 inputs)
- item: heat, natural gas, at industrial furnace >100kW  (input)
  quote:                                                   heat, natural gas, at industrial furnace
  search: heat natural gas industrial furnace >100kW
  candidates:
    - xxx Heat, natural gas, at industrial furnace low-NOx >100kW [RER] (megajoule, 1 inputs)
    - Heat, natural gas, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - District heat, at consumer, natural gas in industrial furnace 1MW [CH] (megajoule, 2 inputs)
- item: electricity, medium voltage, production UCTE, at grid  (input)
  quote:                                                   electricity, medium voltage, production
  search: electricity medium voltage production UCTE at grid
  candidates:
    - Electricity, medium voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from hard coal, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from natural gas, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - xxx Electricity, medium voltage, production UCTE, at grid [UCTE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production GLO, at grid [GLO] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from oil, at grid [CH] (kilowatt hour, 3 inputs)
- item: transport, lorry >16t, fleet average  (input)
  quote:                           5              -        transport, lorry >16t, fleet average           RER              0          tkm       1.86E-1            1          2.09 (4,5,na,na,na,na); Standard distances
  search: transport lorry >16t fleet average
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, fleet average [RER] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
- item: transport, freight, rail  (input)
  quote:                           5              -        transport, freight, rail                       RER              0          tkm      1.12E+0             1          2.09 (4,5,na,na,na,na); Standard distances
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
- item: chemical plant, organics  (input)
  quote:                           5              -        chemical plant, organics                       RER              1          unit     4.00E-10            1          3.09 (4,5,na,na,na,na); Estimation
  search: chemical plant organics
  candidates:
    - Chemical plant, organics [RER] (unit, 4 inputs)
    - Chemicals organic, at plant [GLO] (kilogram, 20 inputs)
    - Chemicals inorganic, at plant [GLO] (kilogram, 20 inputs)
    - Heat, unspecific, in chemical plant [RER] (megajoule, 4 inputs)
    - Steam, for chemical processes, at plant [RER] (kilogram, 3 inputs)
    - Liquid storage tank, chemicals, organics [CH] (unit, 12 inputs)
- item: Heat, waste  (emission to air)
  quote: high population            -            4         Heat, waste                                        -            -          MJ       1.20E+0             1          1.30 (4,5,na,na,na,na); Calculated from the electricity input
  candidates (flow name [compartment]):
    - Waste Heat  [air] (megajoule, ef-3.1-biosphere)
    - Energy, waste heat, air  [resources / in air] (megajoule, bafu-2026-residual)
    - Waste Heat  [soil] (megajoule, ef-3.1-biosphere)
    - Waste Heat  [water] (megajoule, ef-3.1-biosphere)
    - Heat, waste  [emissions to water / groundwater, long-term] (megajoule, bafu-2026-residual)
    - Waste water/m3  [emissions to water / unspecified] (cubic meter, bafu-2026-residual)
    - Waste water  [emissions to water / ocean] (kilogram, bafu-2026-residual)
    - Waste water  [emissions to water / river] (kilogram, bafu-2026-residual)
- item: Boron  (emission to air)
  quote:                            -            4         Boron                                              -            -          kg        6.62E-4            1          5.10 (4,5,na,na,na,na); Estimation
  candidates (flow name [compartment]):
    - Boron  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Boron Carbide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Boron trioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Boron Trifluoride  [air] (kilogram, ef-3.1-biosphere)
    - Diethyl Ether--boron Trifluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Boron  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Boron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Boron  [Resources / Resources from ground] (kilogram, ef-3.1-biosphere)
- item: Boron  (emission to water)
  quote:                            -            4         Boron                                              -            -          kg        1.59E-2            1          5.10 (4,5,na,na,na,na); Stoichiometric calculation
  candidates (flow name [compartment]):
    - Boron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - boron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Boron Carbide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - boron carbide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Boron trioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Diethyl Ether--boron Trifluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - diethyl ether--boron trifluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Boron  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
