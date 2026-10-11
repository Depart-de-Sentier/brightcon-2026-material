You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Transformation, from unknown  (resource to resources)
  quote:      Transformation, from unknown                                             m2                  3.25E+04            1     2    own assumption
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Transformation, to industrial area, built up  (resource to resources)
  quote:      Transformation, to industrial area, built up                             m2                  2.60E+04            1     2    own assumption
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Transformation, to industrial area, vegetation  (resource to resources)
  quote:      Transformation, to industrial area, vegetation                           m2                  6.50E+03            1     2    own assumption
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Transformation, from industrial area  (resource to resources)
  quote:      Transformation, from industrial area                                     m2                  3.25E+04            1     2    own assumption
  candidates (flow name [compartment]):
    - From Industrial Area  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
- item: Transformation, to unknown  (resource to resources)
  quote:      Transformation, to unknown                                               m2                  3.25E+04            1     2    own assumption
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Occupation, industrial area, built up  (resource to resources)
  quote:       Occupation, industrial area, built up                                  m2a                  5.34E+05                  1     3 own assumption, time factor
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Occupation, industrial area, vegetation  (resource to resources)
  quote:       Occupation, industrial area, vegetation                                m2a                  1.34E+05                  1     3 own assumption, time factor
  candidates (flow name [compartment]):
    - (no candidate found)
- item: building, multi-storey  (input)
  quote:      building, multi-storey                                               RER m3                  1.30E+05            1     2    own assumption
  search: building multi-storey
  candidates:
    - Building, multi-storey [RER] (cubic meter, 24 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [CH] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, laminated, integrated, at building [CH] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [RER] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, laminated, integrated, at building [RER] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [APAC] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [CN] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [US] (unit, 7 inputs)
- item: Industrial machine, heavy, unspecified, at plant  (input)
  quote:       Industrial machine, heavy, unspecified, at plant                   RER kg                   4.20E+06                  1   1.5 own assumption
  search: industrial machine heavy unspecified at plant
  candidates:
    - Industrial machine, heavy, unspecified, at plant [RER] (kilogram, 8 inputs)
- item: electricity, medium voltage, at grid  (input)
  quote:       electricity, medium voltage, at grid                               CH kWh                   6.47E+07                  1   1.3 own assumption
  search: electricity medium voltage at grid
  candidates:
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import DE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import FR, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import IT, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import ENTSO, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
- item: diesel, burned in building machine  (input)
  quote:       diesel, burned in building machine                                 GLO MJ                   5.20E+06                  1     2 own assumption
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
- item: reinforcing steel, at plant  (input)
  quote:       reinforcing steel, at plant                                        RER kg                   2.94E+07                  1   1.5 own assumption
  search: reinforcing steel at plant
  candidates:
    - Reinforcing steel, at plant [CH] (kilogram, 2 inputs)
    - Reinforcing steel, at plant [RER] (kilogram, 2 inputs)
    - Reinforcing steel, electric, at plant [RER] (kilogram, 2 inputs)
    - Reinforcing steel, converter, at plant [RER] (kilogram, 2 inputs)
    - Reinforcing steel, electric, import CH, at plant [DE] (kilogram, 2 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [DE] (kilogram, 16 inputs)
    - Reinforcing steel, electric, import CH, at plant [FR] (kilogram, 2 inputs)
    - Reinforcing steel, electric, import CH, at plant [IT] (kilogram, 2 inputs)
- item: concrete, normal, at plant  (input)
  quote:       concrete, normal, at plant                                         CH m3                    1.53E+05                  1   1.3 estimation
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
- item: transport, lorry 28t  (input)
  quote:       transport, lorry 28t                                               CH tkm                   1.47E+07                  1   2.1 standard
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
- item: transport, freight, rail  (input)
  quote:       transport, freight, rail                                           RER tkm                  1.85E+07                  1   2.1 standard
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
- item: disposal, inert waste, 5% water, to inert material landfill  (input)
  quote:       disposal, inert waste, 5% water, to inert material landfill        CH kg                    1.13E+09                  1   1.5 own assumption
  search: disposal inert waste inert material landfill
  candidates:
    - Disposal, inert material, 0% water, to sanitary landfill [CH] (kilogram, 10 inputs)
    - Disposal, inert waste, 5% water, to construction waste landfill [CH] (kilogram, 18 inputs)
    - Disposal, concrete, 5% water, to inert material landfill [GLO] (kilogram, 0 inputs)
- item: Heat, waste  (emission to air)
  quote:       Heat, waste                                                             MJ                  2.33E+08                  1   1.3 same as electricity
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
