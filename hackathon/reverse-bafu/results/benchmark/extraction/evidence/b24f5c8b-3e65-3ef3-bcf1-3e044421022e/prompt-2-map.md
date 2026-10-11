You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CN), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Transformation, from unknown  (resource to resources)
  quote: Transformation, from unknown                                                    resource              land                                                                             m2                                     22500                        1            2 own estimation
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Transformation, to industrial area, built up  (resource to resources)
  quote: Transformation, to industrial area, built up                                    resource              land                                                                             m2                                  1.80E+04                        1            2 own estimation
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Transformation, to industrial area, vegetation  (resource to resources)
  quote: Transformation, to industrial area, vegetation                                  resource              land                                                                             m2                                      4500                        1            2 own estimation
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Transformation, from industrial area  (resource to resources)
  quote: Transformation, from unknown                                                    resource              land                                                                             m2                                     22500                        1            2 own estimation
  candidates (flow name [compartment]):
    - From Industrial Area  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
- item: Transformation, to unknown  (resource to resources)
  quote: Transformation, from unknown                                                    resource              land                                                                             m2                                     22500                        1            2 own estimation
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Occupation, industrial area, built up  (resource to resources)
  quote: Occupation, industrial area, built up                                           resource              land                                                                             m2a                                 3.60E+05                        1          2.5 own estimation
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Occupation, industrial area, vegetation  (resource to resources)
  quote: Occupation, industrial area, vegetation                                         resource              land                                                                             m2a                                 9.00E+04                        1          2.5 own estimation
  candidates (flow name [compartment]):
    - (no candidate found)
- item: building, multi-storey  (input)
  quote: building, multi-storey                                                      RER construction processesbuildings                                          1                             m3                                  1.30E+05                        1            2 own assumption
  search: building multi-storey
  candidates:
    - Building, multi-storey [RER] (cubic meter, 24 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [CN] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, laminated, integrated, at building [CN] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [RER] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, laminated, integrated, at building [RER] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [CH] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, laminated, integrated, at building [CH] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [APAC] (unit, 7 inputs)
- item: industrial machine, heavy, unspecified, at plant  (input)
  quote: industrial machine, heavy, unspecified, at plant                            RER construction processesmachinery                                           1                            kg                                  5.00E+04                        1            3 own assumption
  search: industrial machine heavy unspecified at plant
  candidates:
    - Industrial machine, heavy, unspecified, at plant [RER] (kilogram, 8 inputs)
- item: chromium steel 18/8, at plant  (input)
  quote: chromium steel 18/8, at plant                                               RER metals                extraction                                         0                              kg                                     5000                        1            3 own assumption
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
- item: concrete, normal, at plant  (input)
  quote: concrete, normal, at plant                                                  CH construction materialsconcrete                                            0                             m3                                       250                        1            3 own assumption
  search: concrete normal at plant
  candidates:
    - Concrete, normal, at plant [CH] (cubic meter, 19 inputs)
    - Concrete, normal, at plant, with resource correction [CH] (cubic meter, 1 inputs)
    - Normal concrete, C20/25, with resource correction, at plant [CH] (cubic meter, 13 inputs)
    - Concrete mixing plant [CH] (unit, 4 inputs)
    - Poor concrete, at plant [CH] (cubic meter, 19 inputs)
    - Concrete, exacting, at plant [CH] (cubic meter, 24 inputs)
    - xx Concrete roof tile, at plant [CH] (kilogram, 9 inputs)
    - Precast polymer concrete, at plant [CH] (cubic meter, 27 inputs)
- item: transport, lorry >16t, fleet average  (input)
  quote: transport, lorry >16t, fleet average                                        RER transport systems                                                        0                             tkm                                 3.93E+04                        1            3 own assumption
  search: transport lorry >16t fleet average
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, fleet average [RER] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
- item: transport, coal freight, rail  (input)
  quote: transport, coal freight, rail                                               CN transport systems      train                                              0                             tkm                                 5.57E+03                        1            3 own assumption
  search: transport coal freight rail
  candidates:
    - Transport, coal freight, rail [CN] (ton kilometer, 11 inputs)
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [RER] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting, Betrieb [CH] (ton kilometer, 2 inputs)
- item: disposal, building, concrete, not reinforced, to final disposal  (input)
  quote: disposal, building, concrete, not reinforced, to final disposal             CH                                                                           0                             kg                                  6.00E+05                        1            3 own assumption
  search: disposal building concrete not reinforced final disposal
  candidates:
    - Disposal, building, concrete, not reinforced, to final disposal [CH] (kilogram, 3 inputs)
    - Disposal, building, reinforced concrete, to final disposal [CH] (kilogram, 4 inputs)
    - xx Disposal, building, concrete, not reinforced, to recycling [CH] (kilogram, 1 inputs)
    - Disposal, building, concrete, not reinforced, to sorting plant [CH] (kilogram, 6 inputs)
    - Disposal, building, concrete, not reinforced, at sorting plant, to recycling [CH] (kilogram, 5 inputs)

Return only the JSON object described by the schema.
