You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: reinforcing steel, secondary production, (100% Rec.)  (input)
  quote:                                                                   CH                          0                    kg          2.90E+1             4.50E+1           2.10E+1             2.10E+1            1                                 1.16                      APT Ingenieure 2014, pers.
  search: reinforcing steel secondary production
  candidates:
    - Reinforcing steel, primary production (0% Rec.) [CH] (kilogram, 2 inputs)
    - Steel, low alloyed, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
    - Chromium steel 18/8, secondary production (100% Rec.) [CH] (kilogram, 5 inputs)
    - Steel sheet, uncoated, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
    - Steel profile, uncoated, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
    - Steel sheet, zinc-coated, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
    - Chromium steel sheet 18/8, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
    - Steel profile, tin-coated, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
- item: concrete, concrete for drilled piles, average cement Switzerland, at plant  (input)
  quote:                                                                   CH                          0                    kg            0                    0                 0                1.82E+3            1                                 1.16                      APT Ingenieure 2014, pers.
  search: concrete for drilled piles average cement Switzerland at plant
  candidates:
    - (no candidate found)
- item: diesel, burned in building machine  (input)
  quote:             diesel, burned in building machine                  GLO                           0                    MJ          2.43E+2             2.13E+2           2.43E+2             2.13E+2            1                                 1.16                      Marti AG, 2014, pers. communication
  search: diesel burned in building machine
  candidates:
    - Diesel, burned in building machine, average [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, with particle filter [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, without particle filter [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, with particle filter, without building machine [CH] (megajoule, 3 inputs)
    - Diesel, burned in building machine, with particle filter, without building machine and lubricating oil [CH] (megajoule, 1 inputs)
    - Diesel, burned in building machine, with particle filter [GLO] (megajoule, 4 inputs)
    - Diesel, burned in agricultural machine [CH] (kilogram, 4 inputs)
    - Diesel, burned in auxillary machines at concrete crusher [CH] (kilogram, 4 inputs)
- item: transport, lorry >28t, fleet average  (input)
  quote:             transport, lorry >28t, fleet average                  CH                          0                   tkm          2.55E+1             3.83E+1           2.51E+1             3.75E+1            1                                 2.03                      concrete, 50 km for steel; standard
  search: transport lorry >28t fleet average
  candidates:
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - xxx Operation, lorry >28t, fleet average [CH] (kilometer, 1 inputs)
    - xxx Operation, lorry 20-28t, fleet average [CH] (kilometer, 1 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [CH] (ton kilometer, 20 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
- item: transport, freight, rail  (input)
  quote:             transport, freight, rail                              CH                          0                   tkm          1.74E+1             2.70E+1           1.26E+1             1.26E+1            1                                 2.03
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

Return only the JSON object described by the schema.
