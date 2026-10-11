You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: gravel, crushed, at mine  (input)
  quote:             technosphere gravel, crushed, at mine                            CH            0                    kg         1.00E+0                                                1 1.05 (1,1,1,1,1,1,BU:1.05); 1 kg Kies;
  search: gravel crushed at mine
  candidates:
    - Gravel, crushed, at mine [CH] (kilogram, 17 inputs)
    - Mine, gravel/sand [CH] (unit, 3 inputs)
    - Gravel, round, at mine [CH] (kilogram, 17 inputs)
    - Gravel, unspecified, at mine [CH] (kilogram, 2 inputs)
    - Gravel, crushed, market mix, at regional storage [CH] (kilogram, 4 inputs)
    - Gravel, crushed, market mix, at regional storage, with resource correction [CH] (kilogram, 4 inputs)
- item: transport, lorry >16t, fleet average  (input)
  quote:                           transport, lorry >16t, fleet average               RER           0                    tkm        3.02E-3          3.02E-3           3.02E-3             1 2.09
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
- item: transport, freight, rail  (input)
  quote:                           transport, freight, rail                           RER           0                    tkm        5.05E-4          5.05E-4           5.05E-4             1 2.09
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
- item: transport, barge  (input)
  quote:                           transport, barge                                   RER           0                    tkm        3.23E-4          3.23E-4           3.23E-4             1 2.09
  search: transport barge
  candidates:
    - Transport, barge [RER] (ton kilometer, 7 inputs)
    - Transport, barge tanker [RER] (ton kilometer, 7 inputs)
    - Transport, barge, Betrieb [RER] (ton kilometer, 1 inputs)
    - Transport, barge, Fahrzeug [RER] (ton kilometer, 2 inputs)
    - Transport, barge, Infrastruktur [RER] (ton kilometer, 4 inputs)
    - Transport, passenger ship [CH] (person kilometer, 3 inputs)
    - Transport, passenger cable car [CH] (person kilometer, 4 inputs)
    - Transport, Tram, electric, 2020 [CH] (person kilometer, 5 inputs)

Return only the JSON object described by the schema.
