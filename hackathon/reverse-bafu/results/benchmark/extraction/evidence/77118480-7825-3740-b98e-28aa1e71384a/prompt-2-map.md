You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Energy, solar, converted  (resource to resources)
  quote: resource, in air   Energy, solar, converted                    -             -                  MJ       1.28E+0           1.57E+0           1.12E+0          1.13E+0          1.14E+0          1.13E+0           1.08E+0          1.51E+0          1.51E+0           1 1.07
  candidates (flow name [compartment]):
    - Energy, Solar, Converted  [natural resource] (megajoule, ef-3.1-biosphere)
    - Energy, Geothermal, Converted  [natural resource] (megajoule, ef-3.1-biosphere)
    - Primary Energy From Solar Energy  [natural resource] (kilogram, ef-3.1-biosphere)
    - Energy, Kinetic (in Wind), Converted  [natural resource] (megajoule, ef-3.1-biosphere)
    - Energy, Potential (in Hydropower Reservoir), Converted  [natural resource] (megajoule, ef-3.1-biosphere)
- item: electricity, low voltage, at grid  (input)
  quote: technosphere       electricity, low voltage, at grid         CH 0 kWh                                    1.50E-2            9.46E-3          4.05E-3          3.15E-3          3.25E-3           3.15E-3          6.08E-3          7.58E-3          7.58E-3           1 1.07
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
- item: solar system, 30 m2 Cu flat plate collector, on flat roof, hot water  (input)
  quote:                                                              CH 1 unit                                       -                 -                 -                -            8.22E-7              -                -                 -                -             1 3.00
  search: solar system 30 m2 Cu flat plate collector flat roof
  candidates:
    - Solar system, 30 m2 Cu flat plate collector, on flat roof, hot water [CH] (unit, 18 inputs)
    - Solar system, 20 m2 Cu flat plate collector, on slanted roof, hot water [CH] (unit, 18 inputs)
    - Solar system, 30 m2 Cu flat plate collector, on slanted roof, hot water [CH] (unit, 18 inputs)
    - Solar system, 30 m2  Al-Cu flat plate collector, on slanted roof, hot water [CH] (unit, 18 inputs)
    - Solar system for PVT ONLY, 100m2 Al-Cu flat plate collector, on slanted roof, hot water heat storage [CH] (unit, 18 inputs)
    - Solar system for PVT ONLY, 100m2 Al-Cu flat plate collector, on slanted roof, with borehole regeneration [CH] (unit, 17 inputs)
    - xxx Solar system, flat plate collector, one-family house, hot water [CH] (unit, 13 inputs)
    - xxx Solar system, flat plate collector, multiple dwelling, hot water [CH] (unit, 14 inputs)
- item: transport, van <3.5t  (input)
  quote:                    transport, van <3.5t                      CH 0 tkm                                    4.22E-4            2.45E-4          7.52E-5          5.52E-5          5.55E-5           5.52E-5          1.75E-5          1.86E-4          1.86E-4           1 3.00 per plant for
  search: transport van <3.5t
  candidates:
    - xx Disposal, van < 3.5t [CH] (unit, 5 inputs)
    - Transport, passenger ship [CH] (person kilometer, 3 inputs)
    - xxx Operation, van < 3,5t [CH] (kilometer, 2 inputs)
    - Transport, passenger cable car [CH] (person kilometer, 4 inputs)
    - Transport, Tram, electric, 2020 [CH] (person kilometer, 5 inputs)
    - Transport, average train, SBB mix [CH] (person kilometer, 12 inputs)
    - Transport, district heat, average [CH] (megajoule, 13 inputs)
    - Transport, scooter, fleet average [CH] (kilometer, 8 inputs)
- item: Heat, waste  (emission to air)
  quote:                    Heat, waste                                 -             -                  MJ       1.34E+0           1.61E+0           1.14E+0          1.14E+0          1.16E+0          1.14E+0           1.10E+0          1.54E+0          1.54E+0           1 1.07 Simulation and solar
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
