You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: electricity, low voltage, at grid  (input)
  quote: technosphere         electricity, low voltage, at grid      CH                        0                    kWh         7.08E-01        1.00E+00 1.25E+00 (2,3,3,2,1,5,BU:1.05); ;
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
- item: chemical plant, organics  (input)
  quote:                      chemical plant, organics              RER                        1                    unit        1.00E-10        1.00E+00 3.06E+00 (2,3,3,2,1,5,BU:3); ;
  search: chemical plant organics
  candidates:
    - Chemical plant, organics [RER] (unit, 4 inputs)
    - Liquid storage tank, chemicals, organics [CH] (unit, 12 inputs)
    - Heat, unspecific, in chemical plant [RER] (megajoule, 4 inputs)
    - Steam, for chemical processes, at plant [RER] (kilogram, 3 inputs)
    - Chemicals organic, at plant [GLO] (kilogram, 20 inputs)
    - Chemicals inorganic, at plant [GLO] (kilogram, 20 inputs)
- item: tap water, at user  (input)
  quote:                      tap water, at user                     CH                        0                    kg         1.20E+00         1.00E+00 1.25E+00 (2,3,3,2,1,5,BU:1.05); ;
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

Return only the JSON object described by the schema.
