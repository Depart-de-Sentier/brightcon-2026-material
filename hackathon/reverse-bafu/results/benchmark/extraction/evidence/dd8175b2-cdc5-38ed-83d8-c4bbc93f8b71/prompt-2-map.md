You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: grain maize IP, at farm  (input)
  quote:  grain maize, IP                       10             90       100           -           0         100          0      0
  search: grain maize IP at farm
  candidates:
    - Grain maize IP, at farm [CH] (kilogram, 33 inputs)
    - Grain maize organic, at farm [CH] (kilogram, 14 inputs)
    - Maize seed IP, at farm [CH] (kilogram, 22 inputs)
    - Rye grains IP, at farm [CH] (kilogram, 36 inputs)
    - Silage maize IP, at farm [CH] (kilogram, 33 inputs)
    - Wheat grains IP, at farm [CH] (kilogram, 35 inputs)
    - Barley grains IP, at farm [CH] (kilogram, 37 inputs)
    - Maize seed organic, at farm [CH] (kilogram, 13 inputs)
- item: electricity, low voltage, at grid  (input)
  quote: electricity and 4 m3 natural gas per tonne of feedstuff. The natural gas was converted into final energy
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
- item: natural gas, burned in industrial furnace  (input)
  quote: electricity and 4 m3 natural gas per tonne of feedstuff. The natural gas was converted into final energy
  search: natural gas burned in industrial furnace
  candidates:
    - Natural gas, burned in industrial furnace 1MW [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace 1MWth [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace, for asphalt production, 1MWth [CH] (megajoule, 4 inputs)
    - Heat, natural gas, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - District heat, at consumer, natural gas in industrial furnace 1MW [CH] (megajoule, 2 inputs)
    - Industrial furnace, 1MW, natural gas [RER] (unit, 18 inputs)
    - xxx Heat, natural gas, at industrial furnace low-NOx >100kW [RER] (megajoule, 1 inputs)
- item: transport, lorry 28t  (input)
  quote:                    Maize                                      90           100            0             0
  search: transport lorry 28t
  candidates:
    - Disposal, lorry 28t [CH] (unit, 6 inputs)
    - Maintenance, lorry 28t [CH] (unit, 11 inputs)
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - xxx Operation, lorry >28t, fleet average [CH] (kilometer, 1 inputs)
    - xxx Operation, lorry 20-28t, fleet average [CH] (kilometer, 1 inputs)
    - Operation, lorry 28t, rape methyl ester 100% [CH] (kilometer, 1 inputs)
    - Transport, municipal waste collection, lorry 21t [CH] (ton kilometer, 5 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)
- item: transport, lorry 28t, RER  (input)
  quote:                    Maize                                      90           100            0             0
  search: transport lorry 28t
  candidates:
    - Disposal, lorry 28t [CH] (unit, 6 inputs)
    - Maintenance, lorry 28t [CH] (unit, 11 inputs)
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - xxx Operation, lorry >28t, fleet average [CH] (kilometer, 1 inputs)
    - xxx Operation, lorry 20-28t, fleet average [CH] (kilometer, 1 inputs)
    - Operation, lorry 28t, rape methyl ester 100% [CH] (kilometer, 1 inputs)
    - Transport, municipal waste collection, lorry 21t [CH] (ton kilometer, 5 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)

Return only the JSON object described by the schema.
