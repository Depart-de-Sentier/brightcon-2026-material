You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: air compressor, screw-type compressor, 300 kW, at plant  (input)
  quote: technosphere          air compressor, screw-type compressor, 300 kW, at plant                              RER                         1              unit         8.10E-8           8.10E-8          8.10E-8                          1              3.06
  search: air compressor screw-type compressor
  candidates:
    - Air compressor, screw-type compressor, 4 kW, at plant [RER] (unit, 17 inputs)
    - Air compressor, screw-type compressor, 300 kW, at plant [RER] (unit, 17 inputs)
- item: lubricating oil, at plant  (input)
  quote:                       lubricating oil, at plant                                                            RER                         0              kg           2.08E-6           2.08E-6          2.08E-6                          1              1.24
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
- item: disposal, used mineral oil, 10% water, to hazardous waste incineration  (input)
  quote:                       disposal, used mineral oil, 10% water, to hazardous waste incineration               CH                          0              kg           2.08E-6           2.08E-6          2.08E-6                          1              1.24
  search: disposal used mineral oil hazardous
  candidates:
    - Disposal, used mineral oil, 10% water, to hazardous waste incineration [CH] (kilogram, 15 inputs)
- item: electricity, low voltage, production UCTE, at grid  (input)
  quote:                       electricity, low voltage, production UCTE, at grid                                   UCTE                        0              kWh          9.10E-2           9.74E-2          1.04E-1                          1              1.13              (1,3,2,1,1,4); average value
  search: electricity low voltage UCTE
  candidates:
    - Electricity, low voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production from hard coal, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production from natural gas, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - xxx Electricity, low voltage, production UCTE, at grid [UCTE] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
- item: transport, lorry >16t, fleet average  (input)
  quote:                       transport, lorry >16t, fleet average                                                 RER                         0              tkm          3.73E-5           3.73E-5          3.73E-5                          1              2.14
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
- item: transport, freight, rail  (input)
  quote:                       transport, freight, rail                                                             RER                         0              tkm          7.46E-5           7.46E-5          7.46E-5                          1              2.14
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
- item: Heat, waste  (emission to air)
  quote:                       Heat, waste                                                                               -                       -             MJ           3.28E-1           3.51E-1          3.75E-1                          1              1.13              (1,3,2,1,1,4); from electricity
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
