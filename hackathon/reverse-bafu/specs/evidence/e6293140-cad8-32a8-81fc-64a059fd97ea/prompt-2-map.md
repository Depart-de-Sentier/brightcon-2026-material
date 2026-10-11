You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: water  (input)
  quote: water   kg   9000   [Tab. 44.3 Input and output data for the production of anthraquinone, chromic acid column]
  search: water decarbonised plant
  candidates:
    - Water, decarbonised, at plant [RER] (kilogram, 7 inputs)
    - Water, completely softened, at plant [RER] (kilogram, 6 inputs)
    - Small hydropower plant, in waterworks infrastructure [RER] (unit, 30 inputs)
    - Water, deionised, water balance according to MoeK 2013, at plant [RER] (kilogram, 7 inputs)
    - Electricity, hydropower, at small hydropower plant, in waterworks infrastructure [RER] (kilowatt hour, 1 inputs)
    - Water, deionised, at plant [CH] (kilogram, 7 inputs)
    - Hot water tank 600l, at plant [CH] (unit, 19 inputs)
    - Water treatment plant, deionisation [CH] (unit, 10 inputs)
- item: anthracene  (input)
  quote: anthracene   kg   2600   [Tab. 44.3, chromic acid column]
  search: chemicals organic plant
  candidates:
    - Chemicals organic, at plant [GLO] (kilogram, 20 inputs)
    - Chemical plant, organics [RER] (unit, 4 inputs)
    - Wood preservative, organic salt, Cr-free, at plant [RER] (kilogram, 0 inputs, aggregated)
    - Wooden board manufacturing plant, organic bonded boards [RER] (unit, 8 inputs)
    - Strawberry seedling, organic, for planting, in unheated greenhouse [RER] (unit, 3 inputs)
    - Adhesive, organic, at plant [CH] (kilogram, 17 inputs)
    - xx Cover coat, organic, at plant [CH] (kilogram, 8 inputs)
    - Liquid storage tank, chemicals, organics [CH] (unit, 12 inputs)
- item: sulphuric acid, 48%  (input)
  quote: sulphuric acid, 48%   kg   10200   [Tab. 44.3, chromic acid column]
  search: sulphuric acid liquid plant
  candidates:
    - Sulphuric acid, liquid, at plant [RER] (kilogram, 7 inputs)
    - Sulphuric acid from viscose production, at plant [GLO] (kilogram, 24 inputs)
- item: sodium dichromate, 20%  (input)
  quote: sodium dichromate, 20%   kg   23500   [Tab. 44.3, chromic acid column]
  search: sodium dichromate plant
  candidates:
    - Sodium dichromate, at plant [RER] (kilogram, 12 inputs)
    - Sodium cyanide, at plant [RER] (kilogram, 7 inputs)
    - Sodium phosphate, at plant [RER] (kilogram, 8 inputs)
    - Sodium chlorate, powder, at plant [RER] (kilogram, 13 inputs)
    - Sodium chloride, powder, at plant [RER] (kilogram, 10 inputs)
    - Sodium tripolyphosphate, at plant [RER] (kilogram, 4 inputs)
    - Sodium percarbonate, powder, at plant [RER] (kilogram, 0 inputs, aggregated)
    - Sodium dithionite, anhydrous, at plant [RER] (kilogram, 9 inputs)
- item: Electricity, UCTE medium voltage  (input)
  quote: For the electricity consumed, an average European medium voltage mix (UCTE-mix) is used.
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
- item: Steam, for chemical processes  (input)
  quote: The used steam is shown as "steam, for chemical processes, at plant (RER)" according to the description in Zah & Hischier (2007).
  search: steam chemical processes plant
  candidates:
    - Steam, for chemical processes, at plant [RER] (kilogram, 3 inputs)
- item: chemical plant, organics  (input)
  quote: Concerning the infrastructure, due to a lack of more specific information, the module "chemical plant, organics (RER)" is used here.
  search: chemical plant organics
  candidates:
    - Chemical plant, organics [RER] (unit, 4 inputs)
    - Heat, unspecific, in chemical plant [RER] (megajoule, 4 inputs)
    - Steam, for chemical processes, at plant [RER] (kilogram, 3 inputs)
    - Liquid storage tank, chemicals, organics [CH] (unit, 12 inputs)
    - Chemicals organic, at plant [GLO] (kilogram, 20 inputs)
    - Chemicals inorganic, at plant [GLO] (kilogram, 20 inputs)
- item: Transport, freight, rail  (input)
  quote: Infrastructure and Transport: In the examined sources, no information about average transport distances for the raw materials used are indicated. Therefore, standard distances according to Frischknecht et al. (2007) are used within this dataset.
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
- item: Transport, lorry >16t  (input)
  quote: Infrastructure and Transport: ... standard distances according to Frischknecht et al. (2007) are used within this dataset.
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
- item: Sulphuric acid to water  (emission to water)
  quote: No removal efficiency for sulphuric acid was assumed, leading to emissions of 220 g sulphuric acid per kg product in the treated water.
  candidates (flow name [compartment]):
    - Sulfate  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Sulfate Ion  [water] (kilogram, ef-3.1-biosphere)
    - Zinc Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Barium sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cobalt Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Sodium to water  (emission to water)
  quote: The remaining amount of sodium dichromate is approximated by an emission of about 1 mol of sodium, e.g. 23 g/kg
  candidates (flow name [compartment]):
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Sodium  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Sodium  [water] (kilogram, ef-3.1-biosphere)
    - sodium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium-24  [water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Bromide ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Chromium ions to water  (emission to water)
  quote: and of 0.5 mol (due to a removal efficiency of 50%) of chromium ions, e.g. of 26 g/kg.
  candidates (flow name [compartment]):
    - Chromium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chromium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Bromide ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chromium VI  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Chromium-51  [water] (kilogram, ef-3.1-biosphere)
- item: Sulphuric acid to air  (emission to air)
  quote: Emissions to air: 1% of the sulphuric acid input into the chromic acid process (as this is emitted easily into air)
  candidates (flow name [compartment]):
    - Sulfur Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [soil] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [water] (kilogram, ef-3.1-biosphere)
    - Sulfur  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
- item: Sodium dichromate to air  (emission to air)
  quote: and 0.2% of the sodium dichromate input (assumption);
  candidates (flow name [compartment]):
    - Chromium VI  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - chromium (vi)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - chromium (vi)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chromium  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium-51  [air] (kilogram, ef-3.1-biosphere)
    - Vinclozolin  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium(3+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium(6+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
