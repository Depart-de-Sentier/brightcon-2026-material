You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: reservoir hydropower plant  (input)
  quote: technosphere         reservoir hydropower plant           CH         unit    3.35E-11         3.35E-11           1             3.05
  search: reservoir hydropower plant
  candidates:
    - Reservoir hydropower plant [CH] (unit, 15 inputs)
    - Electricity, hydropower, at reservoir power plant [CH] (kilowatt hour, 4 inputs)
    - Electricity, hydropower, net, at reservoir power plant [CH] (kilowatt hour, 3 inputs)
    - Electricity, hydropower, at run-of-river power plant with reservoir [CH] (kilowatt hour, 2 inputs)
    - Electricity, hydropower, at run-of-river power plant without reservoir [CH] (kilowatt hour, 2 inputs)
    - Reservoir hydropower plant, alpine region [RER] (unit, 15 inputs)
    - Reservoir hydropower plant, non alpine regions [RER] (unit, 15 inputs)
    - Electricity, hydropower, at reservoir power plant, alpine region [RER] (kilowatt hour, 3 inputs)
- item: sulphur hexafluoride, liquid, at plant  (input)
  quote:                      sulphur hexafluoride, liquid, at                                                                                                 (4,5,1,5,1,5,BU:1.05); In electric insulation (e.g.
  search: sulphur hexafluoride liquid at plant
  candidates:
    - Sulphur hexafluoride, liquid, at plant [RER] (kilogram, 5 inputs)
    - Sulphuric acid, liquid, at plant [RER] (kilogram, 7 inputs)
    - Sulphur dioxide, liquid, at plant [RER] (kilogram, 4 inputs)
- item: lubricating oil, at plant  (input)
  quote:                      lubricating oil, at plant            RER        kg       3.24E-8          3.24E-8           1             1.40
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
- item: Transformation, from unknown  (resource to resources)
  quote: resource, land       Transformation, from unknown           -        m2       2.44E-5          2.44E-5           1             2.01
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Transformation, to water bodies, artificial  (resource to resources)
  quote:                      Transformation, to water bodies,
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Transformation, to industrial area, built up  (resource to resources)
  quote:                      Transformation, to industrial                                                                                                    than held-back river; recalculated based on
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Occupation, water bodies, artificial  (resource to resources)
  quote:                      Occupation, water bodies,
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Occupation, industrial area, built up  (resource to resources)
  quote:                      Occupation, industrial area, built                                                                                               infrastructure; recalculated based on Frischknecht et
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Volume occupied, reservoir  (resource to resources)
  quote: resource, in water   Volume occupied, reservoir             -        m3a      1.64E-1          1.64E-1           1             1.11 reservoir; based on Schweizerisches
  candidates (flow name [compartment]):
    - Volume Occupied, Reservoir  [land use] (cubic meter-year, ef-3.1-biosphere)
    - Volume Occupied, Underground Deposit  [land use] (cubic meter, ef-3.1-biosphere)
    - Volume Occupied, Final Repository For Radioactive Waste  [land use] (cubic meter, ef-3.1-biosphere)
    - Volume Occupied, Final Repository For Low-active Radioactive Waste  [land use] (cubic meter, ef-3.1-biosphere)
- item: Water, turbine use, unspecified natural origin  (resource to resources)
  quote:                      Water, turbine use, unspecified                                                                                                  (3,1,1,1,1,1,BU:1.05); Amount of water turbined for the
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Energy, potential (in hydropower reservoir), converted  (resource to resources)
  quote:                      Energy, potential (in hydropower
  candidates (flow name [compartment]):
    - Energy, Potential (in Hydropower Reservoir), Converted  [natural resource] (megajoule, ef-3.1-biosphere)
- item: Dinitrogen monoxide  (emission to air)
  quote:                    Dinitrogen monoxide                      -        kg       2.56E-8          2.56E-8           1             1.58 the biomass in the reservoirs; calculated based on
  candidates (flow name [compartment]):
    - Carbon Monoxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - lead monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - lead monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - carbon monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Methane, biogenic  (emission to air)
  quote:                      Methane, biogenic                      -        kg       2.64E-7          2.64E-7           1             1.57 biomass in the reservoirs; calculated based on Diem
  candidates (flow name [compartment]):
    - Methane (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Correction Flow For Delayed Emission Of Biogenic Methane (within First 100 Years)  [air] (kilogram, ef-3.1-biosphere)
    - Methanethiol  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methane (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methanesulfonic Acid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Fluoro(methoxy)methane  [air] (kilogram, ef-3.1-biosphere)
    - Sodium Methanethiolate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Methyl Methanesulfonate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Carbon dioxide, land transformation  (emission to air)
  quote:                      Carbon dioxide, land
  candidates (flow name [compartment]):
    - Carbon Dioxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
- item: Sulfur hexafluoride  (emission to air)
  quote:                      Sulfur hexafluoride                    -        kg      3.40E-10         3.40E-10           1             1.69
  candidates (flow name [compartment]):
    - Sulfur Hexafluoride  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur hexafluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur hexafluoride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Sulfur hexafluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sulfur  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
    - Sulfuric acid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Heat, waste  (emission to air)
  quote:                      Heat, waste                            -        MJ       1.58E-1          1.58E-1           1             1.12 (3,1,1,1,1,2,BU:1.05); Waste heat
  candidates (flow name [compartment]):
    - Waste Heat  [air] (megajoule, ef-3.1-biosphere)
    - Energy, waste heat, air  [resources / in air] (megajoule, bafu-2026-residual)
    - Waste Heat  [soil] (megajoule, ef-3.1-biosphere)
    - Waste Heat  [water] (megajoule, ef-3.1-biosphere)
    - Heat, waste  [emissions to water / groundwater, long-term] (megajoule, bafu-2026-residual)
    - Waste water/m3  [emissions to water / unspecified] (cubic meter, bafu-2026-residual)
    - Waste water  [emissions to water / ocean] (kilogram, bafu-2026-residual)
    - Waste water  [emissions to water / river] (kilogram, bafu-2026-residual)
- item: Water, CH  (emission to air)
  quote:                      Water, CH                              -        kg       1.75E+0          1.75E+0           1             1.89
  candidates (flow name [compartment]):
    - Water  [air] (cubic meter, ef-3.1-biosphere)
    - sea water  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Green Water  [air] (kilogram, ef-3.1-biosphere)
    - Water Vapour  [air] (kilogram, ef-3.1-biosphere)
    - Water, In Air  [air] (kilogram, ef-3.1-biosphere)
    - Water (evapotranspiration)  [air] (kilogram, ef-3.1-biosphere)
    - Raffinates (petroleum), Catalytic Reformer Ethylene Glycol-water Countercurrent Exts.  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Reaction Mass Of Potassium Didodecylphosphate And Dipotassium Dodecylphosphate And Water  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Oils, unspecified  (emission to water)
  quote:                      Oils, unspecified                      -        kg       2.27E-8          2.27E-8           1             1.69
  candidates (flow name [compartment]):
    - Oils, Unspecified  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Oils, unspecified  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Oils, Unspecified  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Oils, Unspecified  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Oils, Unspecified  [soil] (kilogram, ef-3.1-biosphere)
    - Oils, unspecified  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Acidity, unspecified  [emissions to water / unspecified] (kilogram, bafu-2026-residual)
    - Lubricating Oils  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Oils, unspecified  (emission to soil)
  quote:                      Oils, unspecified                      -        kg       9.76E-9          9.76E-9           1             1.69
  candidates (flow name [compartment]):
    - Oils, Unspecified  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Oils, Unspecified  [soil] (kilogram, ef-3.1-biosphere)
    - Oils, unspecified  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Oils, Unspecified  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Oils, Unspecified  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Oils, unspecified  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Oils, biogenic  [emissions to soil / unspecified] (kilogram, bafu-2026-residual)
    - Oils, biogenic  [emissions to soil / agricultural] (kilogram, bafu-2026-residual)

Return only the JSON object described by the schema.
