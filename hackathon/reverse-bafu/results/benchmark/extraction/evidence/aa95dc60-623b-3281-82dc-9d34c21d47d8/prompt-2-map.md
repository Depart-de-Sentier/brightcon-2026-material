You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: amine-based silica production, for sorbent-based direct air capture system  (input)
  quote: amine-based    silica       kg                                                  3.00e-03               4.00e-03                  4.00e-03    operational
  search: amine-based silica sorbent
  candidates:
    - Amine-based silica production, for sorbent-based direct air capture system [RER] (kilogram, 20 inputs)
- item: Sodium hydroxide, 50% in H2O, production mix, at plant  (input)
  quote: Sodium     hydroxide,       kg                                                                         1.00e-04                  1.00e-04
  search: sodium hydroxide 50% in H2O production mix at plant
  candidates:
    - Sodium hydroxide, 50% in H2O, production mix, at plant [RER] (kilogram, 3 inputs)
- item: tap water, at user  (input)
  quote: tap     water,        at    kg                                                                         9.66e-03                  9.66E-03
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
- item: transport, freight, rail, electricity with shunting  (input)
  quote: transport, freight, rail,   tkm            5.34e+05                             1.80e-03               2.40e-03                  2.52e-03    Generic         transport
  search: transport freight rail electricity with shunting
  candidates:
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting, Betrieb [CH] (ton kilometer, 2 inputs)
    - Transport, freight, rail, electricity with shunting, Fahrzeug [CH] (ton kilometer, 5 inputs)
    - Transport, freight, rail, electricity with shunting, Infrastruktur [CH] (ton kilometer, 3 inputs)
- item: transport, freight, lorry 16-32 metric ton, fleet average  (input)
  quote:  transport,     freight,   tkm           3.16e+05                             1.50e-04              2.00e-04                  2.10e-04    Generic         transport
  search: transport freight lorry 16-32t fleet average
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, fleet average, long haul [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, fleet average, urban delivery [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, fleet average, regional delivery [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
- item: electricity, low voltage, at grid  (input)
  quote:  electricity,       low    kW                                                 5.00e-01              6.90e-03                  1.00e-01    operational
  search: electricity low voltage at grid
  candidates:
    - Electricity, low voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import DE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import FR, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import IT, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import ENTSO, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
- item: Steam, for chemical processes, at plant  (input)
  quote:  Steam, for chemical       kg                                                1.94e+00     1.32e+00 / 9.00e-01       1.40e+00 / 1.44e-01   With / without heat
  search: steam for chemical processes at plant
  candidates:
    - Steam, for chemical processes, at plant [RER] (kilogram, 3 inputs)
- item: Carbon dioxide, fossil  (emission to air)
  quote:  Carbon dioxide, fossil    kg                                                                       1.03e-01                  8.40e-02    CO2 leakage.
  candidates (flow name [compartment]):
    - Carbon Dioxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (biogenic)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic-100yr)  [air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
- item: Carbon dioxide, biogenic  (emission to air)
  quote:  Carbon        dioxide,    kg                                                 2.10e-02              6.46e-03                  9.10e-02    CO2 leakage.
  candidates (flow name [compartment]):
    - Carbon Dioxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (biogenic)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic-100yr)  [air] (kilogram, ef-3.1-biosphere)
    - Correction Flow For Delayed Emission Of Biogenic Carbon Dioxide (within First 100 Years)  [air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [soil] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [water] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
