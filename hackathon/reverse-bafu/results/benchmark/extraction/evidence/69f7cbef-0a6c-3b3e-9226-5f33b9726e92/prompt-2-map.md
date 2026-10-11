You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: copper, at regional storage  (input)
  quote: technosphere copper, at regional storage                         RER        kg         1.80E+4             1                3.05 (na,5,na,1,na,BU:1.05); Estimation
  search: copper at regional storage
  candidates:
    - Copper, at regional storage [RER] (kilogram, 13 inputs)
    - Tin, at regional storage [RER] (kilogram, 13 inputs)
    - Gold, at regional storage [RER] (kilogram, 4 inputs)
    - Lead, at regional storage [RER] (kilogram, 5 inputs)
    - Diesel, at regional storage [RER] (kilogram, 15 inputs)
    - Indium, at regional storage [RER] (kilogram, 7 inputs)
    - Petrol, at regional storage [RER] (kilogram, 16 inputs)
    - Silver, at regional storage [RER] (kilogram, 6 inputs)
- item: chromium steel 18/8, at plant  (input)
  quote:              chromium steel 18/8, at plant                       RER        kg         9.00E+3             1                3.05 (na,5,na,1,na,BU:1.05); Estimation
  search: chromium steel 18/8 at plant
  candidates:
    - Chromium steel 18/8, at plant [RER] (kilogram, 3 inputs)
    - Steel, electric, chromium steel 18/8, at plant [RER] (kilogram, 16 inputs)
    - Steel, converter, chromium steel 18/8, at plant [RER] (kilogram, 18 inputs)
    - Tin plated chromium steel sheet, 2 mm, at plant [RER] (square meter, 3 inputs)
    - Sink, chromium steel, at plant [CH] (unit, 21 inputs)
    - Kitchen worktop, chromium steel, high-end, at plant [CH] (square meter, 8 inputs)
    - Kitchen worktop, chromium steel, standard, at plant [CH] (square meter, 11 inputs)
    - Chromium steel sheet 18/8, recycling share 70 %, with resource correction, at plant [CH] (square meter, 3 inputs)
- item: steel, low-alloyed, at plant  (input)
  quote:              steel, low-alloyed, at plant                        RER        kg         1.80E+5             1                3.05 (na,5,na,1,na,BU:1.05); Estimation
  search: steel low-alloyed at plant
  candidates:
    - Steel, low-alloyed, at plant [RER] (kilogram, 3 inputs)
    - Steel, converter, low-alloyed, at plant [RER] (kilogram, 21 inputs)
    - Steel, electric, un- and low-alloyed, at plant [RER] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant, best plants (min. values) [RER] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant, worst plants (max. values) [RER] (kilogram, 17 inputs)
    - Steel, electric, low-alloyed, at plant [CH] (kilogram, 23 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [DE] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [FR] (kilogram, 16 inputs)
- item: transport, freight, lorry 16-32 metric ton, fleet average  (input)
  quote:              transport, freight, lorry 16-32 metric ton, fleet                                                                   (5,5,na,na,na,BU:2); Standard distance
  search: transport freight lorry 16-32t fleet average
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, fleet average, long haul [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, fleet average, urban delivery [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, fleet average, regional delivery [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, fleet average [RER] (ton kilometer, 4 inputs)
- item: transport, freight, rail  (input)
  quote:                transport, freight, rail                          RER        tkm        1.24E+5             1                3.95
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

Return only the JSON object described by the schema.
