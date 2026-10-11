You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Boric acid (H3BO3)  (input)
  quote: Boric acid (H3BO3)   Î   chemicals inorganics No RER   boric acid, anhydrous, powder, at plant   confidential kg   Künniger et al. 2000
  search: boric acid anhydrous powder
  candidates:
    - Boric acid, anhydrous, powder, at plant [RER] (kilogram, 7 inputs)
- item: Chromium acid  (input)
  quote: Chromium acid        Î   chemicals inorganics No RER   chromium oxide, flakes, at plant   confidential kg   Künniger et al. 2000
  search: chromium oxide flakes
  candidates:
    - Chromium oxide, flakes, at plant [RER] (kilogram, 7 inputs)
- item: Copper(II)oxide (CuO)  (input)
  quote: Copper(II)oxide (CuO) Î  chemicals inorganics No RER   copper oxide, at plant   confidential kg   Künniger et al. 2000
  search: copper oxide plant
  candidates:
    - Copper oxide, at plant [RER] (kilogram, 8 inputs)
    - Zinc oxide, at plant [RER] (kilogram, 6 inputs)
    - Aluminium oxide, plant [RER] (unit, 6 inputs)
    - Ethylene oxide, at plant [RER] (kilogram, 7 inputs)
    - Aluminium oxide, at plant [RER] (kilogram, 17 inputs)
    - Magnesium oxide, at plant [RER] (kilogram, 10 inputs)
    - Copper carbonate, at plant [RER] (kilogram, 8 inputs)
    - Chromium oxide, flakes, at plant [RER] (kilogram, 7 inputs)
- item: Electricity medium voltage - at grid UCTE  (input)
  quote: Electricity medium voltage - at grid UCTE   Î  electricity production mix No UCTE   electricity, medium voltage, production UCTE, at grid   confidential kWh
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
- item: Tap water  (input)
  quote: Tap water            Î   water supply production No RER   tap water, at user   confidential kg   Künniger et al. 2000
  search: tap water user
  candidates:
    - Tap water, at user [RER] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin RER, at user [RER] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin OECD, at user [RER] (kilogram, 14 inputs)
    - Tap water, water balance according to MoeK 2013, at user [RER] (kilogram, 14 inputs)
    - Tap water, at user [CH] (kilogram, 14 inputs)
    - Tap water, unspecified natural origin CH, at user [CH] (kilogram, 14 inputs)
    - Tap water, water balance according to MoeK 2013, at user [CH] (kilogram, 14 inputs)
    - Tap water, water balance according to MoeK 2013, at user [DE] (kilogram, 14 inputs)
- item: Transport rail  (input)
  quote: Transport rail       Î   Chemicals: 600 km   transport systems train No RER   transport, freight, rail   2.94E-01 tkm   estimated
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
- item: Transport lorry  (input)
  quote: Transport lorry   Chemicals: 100 km   transport systems road No RER   transport, lorry >16t, fleet average   4.90E-02 tkm   estimated
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
- item: plant (chemical plant, organics)  (input)
  quote: plant                Î   organic plant as proxy   chemicals organics Yes RER   chemical plant, organics   4.00E-10 unit   estimated
  search: chemical plant organics
  candidates:
    - Chemical plant, organics [RER] (unit, 4 inputs)
    - Heat, unspecific, in chemical plant [RER] (megajoule, 4 inputs)
    - Steam, for chemical processes, at plant [RER] (kilogram, 3 inputs)
    - Liquid storage tank, chemicals, organics [CH] (unit, 12 inputs)
    - Chemicals organic, at plant [GLO] (kilogram, 20 inputs)
    - Chemicals inorganic, at plant [GLO] (kilogram, 20 inputs)
- item: Waste heat into air  (emission to air)
  quote: Waste heat into air   Î   air unspecified   Heat, waste   1.30E-01 MJ   calculated
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
