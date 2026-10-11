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
  quote: technosphere electricity, low voltage, at grid               CH             0                    kWh                                        0.575          1.16E-1                        0.186                                1            1.23                     (2,3,2,3,1,5,BU:1.05); ;
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
- item: charcoal, at plant  (input)
  quote:                 charcoal, at plant                           GLO            0                    kg                                      0.00214           6.97E-4                    0.000208                                 1            1.32                     (1,4,1,3,3,5,BU:1.05); ;
  search: charcoal at plant
  candidates:
    - Charcoal, at plant [GLO] (kilogram, 4 inputs)
    - Planting [CH] (hectare, 4 inputs)
    - Cement plant [CH] (unit, 4 inputs)
    - Ceramic plant [CH] (unit, 3 inputs)
    - Brass, at plant [CH] (kilogram, 8 inputs)
    - Potato planting [CH] (hectare, 4 inputs)
    - Rock wool plant [CH] (unit, 4 inputs)
    - Bronze, at plant [CH] (kilogram, 8 inputs)
- item: lubricating oil, at plant  (input)
  quote:                 lubricating oil, at plant                    RER            0                    kg                                     0.000114                                       0.00015                                 1            1.32                     (1,4,1,3,3,5,BU:1.05); ;
  search: lubricating oil at plant
  candidates:
    - Lubricating oil, at plant [RER] (kilogram, 4 inputs)
    - Vegetable oil esterification plant [CH] (unit, 5 inputs)
    - Vegetable oil, from waste cooking oil, at plant [CH] (kilogram, 10 inputs)
    - Glycerine, from rape oil, at esterification plant [CH] (kilogram, 11 inputs)
    - Vegetable oil methyl ester, at esterification plant [CH] (kilogram, 10 inputs)
    - Diesel, burned in building machine, with particle filter, without building machine and lubricating oil [CH] (megajoule, 1 inputs)
    - Soya oil, at plant [RER] (kilogram, 10 inputs)
    - Oil power plant 500MW [RER] (unit, 19 inputs)
- item: chemical plant, organics  (input)
  quote:                 chemical plant, organics                     RER            1                    unit                                     5.4E-11                 5.53E-11             5.40E-11                                1            3.31                     (3,4,3,3,4,5,BU:3); ;
  search: chemical plant organics
  candidates:
    - Chemical plant, organics [RER] (unit, 4 inputs)
    - Liquid storage tank, chemicals, organics [CH] (unit, 12 inputs)
    - Heat, unspecific, in chemical plant [RER] (megajoule, 4 inputs)
    - Steam, for chemical processes, at plant [RER] (kilogram, 3 inputs)
    - Chemicals organic, at plant [GLO] (kilogram, 20 inputs)
    - Chemicals inorganic, at plant [GLO] (kilogram, 20 inputs)
- item: transport, freight, lorry 16-32 metric ton, fleet average  (input)
  quote:                 ton, fleet average                                                                                                      0.000023                                  0.000018099
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
- item: chromium steel 18/8, at plant  (input)
  quote:                 chromium steel 18/8, at plant                RER            0                    kg                      1.04E-4                                                                                               1            1.23                     (2,3,2,1,1,5,BU:1.05); ;
  search: chromium steel 18/8 at plant
  candidates:
    - Sink, chromium steel, at plant [CH] (unit, 21 inputs)
    - Kitchen worktop, chromium steel, high-end, at plant [CH] (square meter, 8 inputs)
    - Kitchen worktop, chromium steel, standard, at plant [CH] (square meter, 11 inputs)
    - Chromium steel sheet 18/8, recycling share 70 %, with resource correction, at plant [CH] (square meter, 3 inputs)
    - Chromium steel 18/8, at plant [RER] (kilogram, 3 inputs)
    - Steel, electric, chromium steel 18/8, at plant [RER] (kilogram, 16 inputs)
    - Steel, converter, chromium steel 18/8, at plant [RER] (kilogram, 18 inputs)
    - Tin plated chromium steel sheet, 2 mm, at plant [RER] (square meter, 3 inputs)
- item: Heat, waste  (emission to air)
  quote: population                                                                                                                                 1.2775                    4.15                  1.2775
  candidates (flow name [compartment]):
    - Waste Heat  [air] (megajoule, ef-3.1-biosphere)
    - Energy, waste heat, air  [resources / in air] (megajoule, bafu-2026-residual)
    - Waste Heat  [soil] (megajoule, ef-3.1-biosphere)
    - Waste Heat  [water] (megajoule, ef-3.1-biosphere)
    - Heat, waste  [emissions to water / groundwater, long-term] (megajoule, bafu-2026-residual)
    - Waste water/m3  [emissions to water / unspecified] (cubic meter, bafu-2026-residual)
    - Waste water  [emissions to water / ocean] (kilogram, bafu-2026-residual)
    - Waste water  [emissions to water / river] (kilogram, bafu-2026-residual)
- item: Carbon dioxide, biogenic  (emission to air)
  quote:                                                                                                                                          0.46896                  0.49866                 0.46896
  candidates (flow name [compartment]):
    - Carbon Dioxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (biogenic)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic-100yr)  [air] (kilogram, ef-3.1-biosphere)
    - Correction Flow For Delayed Emission Of Biogenic Carbon Dioxide (within First 100 Years)  [air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [soil] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [water] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
- item: Methane, biogenic  (emission to air)
  quote:                                                                                                                                          0.00461              0.000432                     0.0101
  candidates (flow name [compartment]):
    - Methane (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Correction Flow For Delayed Emission Of Biogenic Methane (within First 100 Years)  [air] (kilogram, ef-3.1-biosphere)
    - Methanethiol  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methane (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methanesulfonic Acid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Fluoro(methoxy)methane  [air] (kilogram, ef-3.1-biosphere)
    - Sodium Methanethiolate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methyl Methanesulfonate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Hydrogen sulfide  (emission to air)
  quote:                                                                                                                                      0.00000231                   3.49E-06          2.3107E-06
  candidates (flow name [compartment]):
    - Hydrogen Sulfide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen Sulfide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Hydrogen Sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - hydrogen sulfide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - hydrogen sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Hydrogen  [air] (kilogram, ef-3.1-biosphere)
    - Hydrogen-3  [Emissions / Emissions to air] (kilo Becquerel, ef-3.1-biosphere)
    - Sulfide ion  [air] (kilogram, ef-3.1-biosphere)
- item: Sulfur dioxide  (emission to air)
  quote:                                                                                                                                    0.000006599                    5.52E-04          6.5993E-06
  candidates (flow name [compartment]):
    - Sulfur Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [soil] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [water] (kilogram, ef-3.1-biosphere)
    - Sulfur  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
