You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CN), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Carbon dioxide, in air  (resource to resources)
  quote:     resource, in air            4             - Carbon dioxide, in air                           -             -         kg     2.56E+4        1           1.24
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Energy, gross calorific value, in biomass  (resource to resources)
  quote:     resource, biotic            4             - Energy, gross calorific value, in biomass        -             -         MJ     2.74E+5        1           1.24
  candidates (flow name [compartment]):
    - Energy, gross calorific value, in biomass  [resources / unspecified] (megajoule, bafu-2026-residual)
    - Energy, gross calorific value, in biomass, resource correction  [resources / unspecified] (megajoule, bafu-2026-residual)
    - Energy, gross calorific value, in biomass  [resources / biotic] (megajoule, bafu-2026-residual)
    - Energy, gross calorific value, in biomass  [resources / in air] (megajoule, bafu-2026-residual)
    - Energy, gross calorific value, in biomass, resource correction  [resources / biotic] (megajoule, bafu-2026-residual)
    - Energy, Gross Calorific Value, In Biomass, Primary Forest  [natural resource] (megajoule, ef-3.1-biosphere)
- item: urea, as N, at regional storehouse  (input)
  quote:     technosphere                5             - urea, as N, at regional storehouse             RER            0          kg     4.00E+1        1           1.11       (3,1,1,1,1,1); IFA 2006
  search: urea as N at regional storehouse
  candidates:
    - Urea, as N, at regional storehouse [RER] (kilogram, 6 inputs)
    - [sulfonyl]urea-compounds, at regional storehouse [RER] (kilogram, 43 inputs)
    - xx Urea ammonium nitrate, as N, at regional storehouse [RER] (kilogram, 7 inputs)
    - [sulfonyl]urea-compounds, at regional storehouse [CH] (kilogram, 43 inputs)
    - MCPA, at regional storehouse [RER] (kilogram, 21 inputs)
    - 2,4-D, at regional storehouse [RER] (kilogram, 21 inputs)
    - Diuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Dicamba, at regional storehouse [RER] (kilogram, 32 inputs)
- item: ammonium nitrate, as N, at regional storehouse  (input)
  quote:                                                 ammonium nitrate, as N, at regional
  search: ammonium nitrate as N at regional storehouse
  candidates:
    - Ammonium nitrate, as N, at regional storehouse [RER] (kilogram, 5 inputs)
    - Calcium ammonium nitrate, as N, at regional storehouse [RER] (kilogram, 7 inputs)
    - xx Urea ammonium nitrate, as N, at regional storehouse [RER] (kilogram, 7 inputs)
    - Ammonium nitrate phosphate, as N, at regional storehouse [RER] (kilogram, 7 inputs)
    - Ammonium nitrate phosphate, as P2O5, at regional storehouse [RER] (kilogram, 7 inputs)
    - Calcium nitrate, as N, at regional storehouse [RER] (kilogram, 8 inputs)
    - Ammonium sulphate, as N, at regional storehouse [RER] (kilogram, 8 inputs)
    - Potassium nitrate, as N, at regional storehouse [RER] (kilogram, 4 inputs)
- item: diammonium phosphate, as P2O5, at regional storehouse  (input)
  quote:                                                 diammonium phosphate, as P2O5, at
  search: diammonium phosphate as P2O5 at regional storehouse
  candidates:
    - Diammonium phosphate, as P2O5, at regional storehouse [RER] (kilogram, 7 inputs)
    - Diammonium phosphate, as N, at regional storehouse [RER] (kilogram, 7 inputs)
    - xx Monoammonium phosphate, as P2O5, at regional storehouse [RER] (kilogram, 7 inputs)
    - Ammonium nitrate phosphate, as P2O5, at regional storehouse [RER] (kilogram, 7 inputs)
- item: potassium chloride, as K2O, at regional storehouse  (input)
  quote:                                                 potassium chloride, as K2O, at regional
  search: potassium chloride as K2O at regional storehouse
  candidates:
    - Potassium chloride, as K2O, at regional storehouse [RER] (kilogram, 10 inputs)
    - Potassium nitrate, as K2O, at regional storehouse [RER] (kilogram, 4 inputs)
    - Potassium sulphate, as K2O, at regional storehouse [RER] (kilogram, 7 inputs)
- item: lime, from carbonation, at regional storehouse  (input)
  quote:                                                 lime, from carbonation, at regional
  search: lime from carbonation at regional storehouse
  candidates:
    - Lime, from carbonation, at regional storehouse [CH] (kilogram, 1 inputs)
- item: irrigating  (input)
  quote:                                 5             - irrigating                                     CH             0          ha     1.25E+0        1           1.14       (3,3,2,1,1,3); Smith 2000
  search: irrigating
  candidates:
    - Irrigating [CH] (hectare, 13 inputs)
    - xx Irrigating [CH] (cubic meter, 1 inputs)
    - Irrigating [US] (cubic meter, 13 inputs)
- item: 2,4-D, at regional storehouse  (input)
  quote:                                 5             - 2,4-D, at regional storehouse                  RER            0          kg     7.45E-2        1           1.07       (1,1,1,3,1,3); USDA 2004
  search: 2,4-D at regional storehouse
  candidates:
    - MCPA, at regional storehouse [RER] (kilogram, 21 inputs)
    - 2,4-D, at regional storehouse [RER] (kilogram, 21 inputs)
    - Diuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Dicamba, at regional storehouse [RER] (kilogram, 32 inputs)
    - Linuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Alachlor, at regional storehouse [RER] (kilogram, 73 inputs)
    - Atrazine, at regional storehouse [RER] (kilogram, 11 inputs)
    - xx Maneb, at regional storehouse [RER] (kilogram, 15 inputs)
- item: alachlor, at regional storehouse  (input)
  quote:                                 5             - alachlor, at regional storehouse               RER            0          kg     2.76E-1        1           1.07       (1,1,1,3,1,3); USDA 2004
  search: alachlor at regional storehouse
  candidates:
    - Alachlor, at regional storehouse [RER] (kilogram, 73 inputs)
    - xx Alachlor, at regional storehouse [CH] (kilogram, 73 inputs)
    - MCPA, at regional storehouse [RER] (kilogram, 21 inputs)
    - 2,4-D, at regional storehouse [RER] (kilogram, 21 inputs)
    - Diuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Dicamba, at regional storehouse [RER] (kilogram, 32 inputs)
    - Linuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Atrazine, at regional storehouse [RER] (kilogram, 11 inputs)
- item: atrazine, at regional storehouse  (input)
  quote:                                 5             - atrazine, at regional storehouse               RER            0          kg     8.16E-1        1           1.07       (1,1,1,3,1,3); USDA 2004
  search: atrazine at regional storehouse
  candidates:
    - Atrazine, at regional storehouse [RER] (kilogram, 11 inputs)
    - Atrazine, at regional storehouse [CH] (kilogram, 11 inputs)
    - MCPA, at regional storehouse [RER] (kilogram, 21 inputs)
    - 2,4-D, at regional storehouse [RER] (kilogram, 21 inputs)
    - Diuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Dicamba, at regional storehouse [RER] (kilogram, 32 inputs)
    - Linuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Alachlor, at regional storehouse [RER] (kilogram, 73 inputs)
- item: dicamba, at regional storehouse  (input)
  quote:                                 5             - dicamba, at regional storehouse                RER            0          kg     1.26E-2        1           1.07       (1,1,1,3,1,3); USDA 2004
  search: dicamba at regional storehouse
  candidates:
    - Dicamba, at regional storehouse [RER] (kilogram, 32 inputs)
    - Dicamba, at regional storehouse [CH] (kilogram, 32 inputs)
    - MCPA, at regional storehouse [RER] (kilogram, 21 inputs)
    - 2,4-D, at regional storehouse [RER] (kilogram, 21 inputs)
    - Diuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Linuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Alachlor, at regional storehouse [RER] (kilogram, 73 inputs)
    - Atrazine, at regional storehouse [RER] (kilogram, 11 inputs)
- item: acetamide-anillide-compounds, at regional storehouse  (input)
  quote:                                                 acetamide-anillide-compounds, at regional
  search: acetamide-anillide-compounds at regional storehouse
  candidates:
    - Acetamide-anillide-compounds, at regional storehouse [RER] (kilogram, 37 inputs)
    - Acetamide-anillide-compounds, at regional storehouse [CH] (kilogram, 37 inputs)
- item: glyphosate, at regional storehouse  (input)
  quote:                                 5             - glyphosate, at regional storehouse             RER            0          kg     2.45E-1        1           1.07       (1,1,1,3,1,3); USDA 2004
  search: glyphosate at regional storehouse
  candidates:
    - Glyphosate, at regional storehouse [RER] (kilogram, 12 inputs)
    - Glyphosate, at regional storehouse [CH] (kilogram, 12 inputs)
    - MCPA, at regional storehouse [RER] (kilogram, 21 inputs)
    - 2,4-D, at regional storehouse [RER] (kilogram, 21 inputs)
    - Diuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Dicamba, at regional storehouse [RER] (kilogram, 32 inputs)
    - Linuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Alachlor, at regional storehouse [RER] (kilogram, 73 inputs)
- item: metolachlor, at regional storehouse  (input)
  quote:                                 5             - metolachlor, at regional storehouse            RER            0          kg     3.64E-1        1           1.07       (1,1,1,3,1,3); USDA 2004
  search: metolachlor at regional storehouse
  candidates:
    - Metolachlor, at regional storehouse [RER] (kilogram, 16 inputs)
    - Metolachlor, at regional storehouse [CH] (kilogram, 16 inputs)
    - MCPA, at regional storehouse [RER] (kilogram, 21 inputs)
    - 2,4-D, at regional storehouse [RER] (kilogram, 21 inputs)
    - Diuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Dicamba, at regional storehouse [RER] (kilogram, 32 inputs)
    - Linuron, at regional storehouse [RER] (kilogram, 43 inputs)
    - Alachlor, at regional storehouse [RER] (kilogram, 73 inputs)
- item: [sulfonyl]urea-compounds, at regional storehouse  (input)
  quote:                                                 [sulfonyl]urea-compounds, at regional
  search: sulfonylurea-compounds at regional storehouse
  candidates:
    - Nitro-compounds, at regional storehouse [RER] (kilogram, 73 inputs)
    - Nitrile-compounds, at regional storehouse [RER] (kilogram, 19 inputs)
    - Phenoxy-compounds, at regional storehouse [RER] (kilogram, 21 inputs)
    - Cyclic N-compounds, at regional storehouse [RER] (kilogram, 42 inputs)
    - Triazine-compounds, at regional storehouse [RER] (kilogram, 14 inputs)
    - Pyretroid-compounds, at regional storehouse [RER] (kilogram, 19 inputs)
    - Phtalamide-compounds, at regional storehouse [RER] (kilogram, 67 inputs)
    - Pyridazine-compounds, at regional storehouse [RER] (kilogram, 73 inputs)
- item: organophosphorus-compounds, at regional storehouse  (input)
  quote:                                                 organophosphorus-compounds, at regional
  search: organophosphorus-compounds at regional storehouse
  candidates:
    - Organophosphorus-compounds, at regional storehouse [RER] (kilogram, 27 inputs)
    - Organophosphorus-compounds, at regional storehouse [CH] (kilogram, 27 inputs)
    - Nitro-compounds, at regional storehouse [RER] (kilogram, 73 inputs)
    - Nitrile-compounds, at regional storehouse [RER] (kilogram, 19 inputs)
    - Phenoxy-compounds, at regional storehouse [RER] (kilogram, 21 inputs)
    - Cyclic N-compounds, at regional storehouse [RER] (kilogram, 42 inputs)
    - Triazine-compounds, at regional storehouse [RER] (kilogram, 14 inputs)
    - Pyretroid-compounds, at regional storehouse [RER] (kilogram, 19 inputs)
- item: fertilising, by broadcaster  (input)
  quote:                                 5             - fertilising, by broadcaster                    CH             0          ha     3.33E-1        1           1.22       (1,1,4,1,1,3); FAO 2002
  search: fertilising by broadcaster
  candidates:
    - Fertilising, by broadcaster [CH] (hectare, 4 inputs)
- item: tillage, ploughing  (input)
  quote:                                 5             - tillage, ploughing                             CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002
  search: tillage ploughing
  candidates:
    - Tillage, ploughing [CH] (hectare, 4 inputs)
    - Tillage, rolling [CH] (hectare, 4 inputs)
    - Tillage, currying, by weeder [CH] (hectare, 4 inputs)
    - xx Tillage, rotary cultivator [CH] (hectare, 4 inputs)
    - Tillage, cultivating, chiselling [CH] (hectare, 4 inputs)
    - Tillage, harrowing, by rotary harrow [CH] (hectare, 4 inputs)
    - Tillage, harrowing, by spring tine harrow [CH] (hectare, 4 inputs)
    - Tillage, hoeing and earthing-up, potatoes [CH] (hectare, 4 inputs)
- item: tillage, harrowing, by spring tine harrow  (input)
  quote:                                 5             - tillage, harrowing, by spring tine harrow      CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002
  search: tillage harrowing spring tine harrow
  candidates:
    - Tillage, harrowing, by spring tine harrow [CH] (hectare, 4 inputs)
- item: tillage, currying, by weeder  (input)
  quote:                                 5             - tillage, currying, by weeder                   CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002
  search: tillage currying by weeder
  candidates:
    - Tillage, currying, by weeder [CH] (hectare, 4 inputs)
- item: sowing  (input)
  quote:                                 5             - sowing                                         CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002
  search: sowing
  candidates:
    - Sowing [CH] (hectare, 4 inputs)
- item: application of plant protection products, by field sprayer  (input)
  quote:                                                 application of plant protection products, by
  search: application of plant protection products by field sprayer
  candidates:
    - Application of plant protection products, by field sprayer [CH] (hectare, 4 inputs)
- item: combine harvesting  (input)
  quote:                                 5             - combine harvesting                             CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002
  search: combine harvesting
  candidates:
    - Combine harvesting [CH] (hectare, 3 inputs)
    - Harvesting, forestry harvester [RER] (hour, 6 inputs)
    - Gas combined cycle power plant, 400MWe [RER] (unit, 14 inputs)
    - Harvesting, bundling, energy wood harvester [RER] (hour, 7 inputs)
    - Natural gas, burned in combined cycle plant, best technology [RER] (megajoule, 6 inputs)
    - Electricity, natural gas, at combined cycle plant, best technology [RER] (kilowatt hour, 1 inputs)
    - Harvesting, by complete harvester, beets [CH] (hectare, 4 inputs)
    - Harvesting, by complete harvester, potatoes [CH] (hectare, 4 inputs)
- item: tillage, cultivating, chiselling  (input)
  quote:                                 5             - tillage, cultivating, chiselling               CH             0          ha     1.00E+0        1           1.22       (1,1,4,1,1,3); FAO 2002
  search: tillage cultivating chiselling
  candidates:
    - Tillage, cultivating, chiselling [CH] (hectare, 4 inputs)
- item: transport, tractor and trailer  (input)
  quote:                                 5             - transport, tractor and trailer                 CH             0          tkm    4.30E+1        1           2.09       (4,5,na,na,na,na); Standard Distances
  search: transport tractor and trailer
  candidates:
    - (no candidate found)
- item: transport, lorry 28t  (input)
  quote:                                 5             - transport, lorry 28t                           CH             0          tkm    3.00E+1        1           2.09       (4,5,na,na,na,na); Standard Distances
  search: transport lorry 28t
  candidates:
    - Lorry 28t [RER] (unit, 38 inputs)
    - Transport, freight, lorry, fleet average [RER] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 3.5t-7.5t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
- item: transport, lorry 32t  (input)
  quote:                                 5             - transport, lorry 32t                           RER            0          tkm    2.23E+2        1           2.09       (4,5,na,na,na,na); Standard Distances
  search: transport lorry 32t
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2020, EURO-VI, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2002, EURO-III, long haul [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, urban delivery [RER] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, urban delivery [RER] (ton kilometer, 11 inputs)
- item: transport, freight, rail  (input)
  quote:                                 5             - transport, freight, rail                       RER            0          tkm    2.68E+2        1           2.09       (4,5,na,na,na,na); Standard Distances
  search: transport freight rail
  candidates:
    - Transport, coal freight, rail [CN] (ton kilometer, 11 inputs)
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [RER] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting, Betrieb [CH] (ton kilometer, 2 inputs)
- item: transport, barge  (input)
  quote:                                 5             - transport, barge                               RER            0          tkm    7.86E+2        1           2.09       (4,5,na,na,na,na); Standard Distances
  search: transport barge
  candidates:
    - Transport, barge [RER] (ton kilometer, 7 inputs)
    - Transport, barge tanker [RER] (ton kilometer, 7 inputs)
    - Transport, barge, Betrieb [RER] (ton kilometer, 1 inputs)
    - Transport, barge, Fahrzeug [RER] (ton kilometer, 2 inputs)
    - Transport, barge, Infrastruktur [RER] (ton kilometer, 4 inputs)
    - Transport, coal freight, rail [CN] (ton kilometer, 11 inputs)
    - Crude oil, market mix, at long distance transport [CN] (kilogram, 37 inputs)
    - Transport, natural gas, onshore pipeline, long distance [CN] (ton kilometer, 5 inputs)
- item: Transformation, from arable  (resource to resources)
  quote:     resources                   4             - Transformation, from arable                      -             -         m2     1.00E+4        1           2.05       (1,3,4,3,1,1); FAOSTAT 2006, FAO 1994
  candidates (flow name [compartment]):
    - From Arable  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Arable, Fallow  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Arable, Irrigated  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Arable, Greenhouse  [Land use / Land transformation] (kilogram, ef-3.1-biosphere)
    - From Arable, Flooded Crops  [Land use / Land transformation] (kilogram, ef-3.1-biosphere)
    - From Arable, Non-irrigated  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Arable, Irrigated, Extensive  [Land use / Land transformation] (kilogram, ef-3.1-biosphere)
    - From Arable, Irrigated, Intensive  [Land use / Land transformation] (kilogram, ef-3.1-biosphere)
- item: Transformation, to arable  (resource to resources)
  quote:                                 4             - Transformation, to arable                        -             -         m2     1.00E+4        1           2.05       (1,3,4,3,1,1); FAOSTAT 2006, FAO 1994
  candidates (flow name [compartment]):
    - Arable  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Arable  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Arable  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - Arable, Fallow  [Land use / Land occupation] (kilogram, ef-3.1-biosphere)
    - Arable, Irrigated  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Arable, Fallow  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - Arable, Greenhouse  [Land use / Land occupation] (kilogram, ef-3.1-biosphere)
    - From Arable, Fallow  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
- item: Occupation, arable  (resource to resources)
  quote:                                 4             - Occupation, arable                               -             -         m2a    5.83E+3        1           1.56       (1,3,4,3,1,1); FAOSTAT 2006, FAO 1994
  candidates (flow name [compartment]):
    - Arable  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Arable  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Arable  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - Arable, Fallow  [Land use / Land occupation] (kilogram, ef-3.1-biosphere)
    - Arable, Irrigated  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Arable, Fallow  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - Arable, Greenhouse  [Land use / Land occupation] (kilogram, ef-3.1-biosphere)
    - From Arable, Fallow  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
- item: Ammonia  (emission to air)
  quote:     low population               -           4 Ammonia                                            -            -         kg     6.80E+0        1           1.32
  candidates (flow name [compartment]):
    - Ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Dinitrogen monoxide  (emission to air)
  quote:                                  -           4 Dinitrogen monoxide                                -            -         kg     3.83E+0        1           1.58
  candidates (flow name [compartment]):
    - Carbon Monoxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - lead monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - lead monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - carbon monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Nitrogen oxides  (emission to air)
  quote:                                  -           4 Nitrogen oxides                                    -            -         kg     8.05E-1        1           1.58
  candidates (flow name [compartment]):
    - Nitrogen Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Mustard  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Trifluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen oxide (N2O4)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Phosphorus  (emission to water)
  quote:                                  -           4 Phosphorus                                         -            -         kg     9.07E-1        1           1.58
  candidates (flow name [compartment]):
    - Phosphorus  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Phosphorus, Total  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - phosphorus, total  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Phosphorus Trichloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Phosphorus oxychloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - phosphorus trichloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Phosphorus Pentachloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - phosphorus pentachloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Phosphorus  (emission to water)
  quote:                                  -           4 Phosphorus                                         -            -         kg     7.00E-2        1           1.58
  candidates (flow name [compartment]):
    - Phosphorus  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Phosphorus, Total  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - phosphorus, total  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Phosphorus Trichloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Phosphorus oxychloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - phosphorus trichloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Phosphorus Pentachloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - phosphorus pentachloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Nitrate  (emission to water)
  quote:                                  -           4 Nitrate                                            -            -         kg     1.13E+2        1           1.58       (4,3,1,1,1,4); Estimation
  candidates (flow name [compartment]):
    - Nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Zinc nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Barium nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cupric nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Silver Nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium Nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Cadmium  (emission to soil)
  quote:                                  -           4 Cadmium                                            -            -         kg     -1.83E-3       1           1.58
  candidates (flow name [compartment]):
    - Cadmium  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - cadmium  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Cadmium(2+)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - cadmium (ii)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Cadmium oxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Cadmium Sulfate  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Cadmium nitrate  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Cadmium sulfide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Copper  (emission to soil)
  quote:                                  -           4 Copper                                             -            -         kg     -8.29E-2       1           1.58
  candidates (flow name [compartment]):
    - Copper  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - copper  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Copper(2+)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - copper (ii)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Oxine-copper  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - oxine-copper  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Copper hydroxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - copper (i) oxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Lead  (emission to soil)
  quote:                                  -           4 Lead                                               -            -         kg     -4.00E-2       1           1.58
  candidates (flow name [compartment]):
    - Lead  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - lead  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Lead(2+)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Lead-210  [soil] (kilogram, ef-3.1-biosphere)
    - lead (ii)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Lead oxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Lead nitrate  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Zinc  (emission to soil)
  quote:                                  -           4 Zinc                                               -            -         kg     -9.60E-2       1           1.58
  candidates (flow name [compartment]):
    - Zinc  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - zinc  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Zinc-65  [soil] (kilogram, ef-3.1-biosphere)
    - Zinc(2+)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - zinc (ii)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - zinc oxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Zinc Sulfate  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Zinc nitrate  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: 2,4-D  (emission to soil)
  quote:                                  -           4 2,4-D                                              -            -         kg     7.45E-2        1           1.32
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Alachlor  (emission to soil)
  quote:                                  -           4 Alachlor                                           -            -         kg     2.76E-1        1           1.32
  candidates (flow name [compartment]):
    - Alachlor  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Alachlor  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Alachlor  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Atrazine  (emission to soil)
  quote:                                  -           4 Atrazine                                           -            -         kg     8.16E-1        1           1.32
  candidates (flow name [compartment]):
    - Atrazine  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - atrazine  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Atrazine  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Atrazine  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - atrazine  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Dicamba  (emission to soil)
  quote:                                  -           4 Dicamba                                            -            -         kg     1.26E-2        1           1.32
  candidates (flow name [compartment]):
    - Dicamba  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - dicamba  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Dicamba-sodium  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Dicamba  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Dicamba  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - dicamba  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Dicamba-sodium  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Dicamba-sodium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Dimethenamid  (emission to soil)
  quote:                                  -           4 Dimethenamid                                       -            -         kg     7.61E-2        1           1.32
  candidates (flow name [compartment]):
    - Dimethenamid  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - dimethenamid  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Dimethenamid-P  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Dimethenamid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Dimethenamid  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - dimethenamid  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Dimethenamid-P  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Dimethenamid-P  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Glyphosate  (emission to soil)
  quote:                                  -           4 Glyphosate                                         -            -         kg     2.45E-1        1           1.32
  candidates (flow name [compartment]):
    - Glyphosate  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - glyphosate  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Glyphosate-trimesium  [soil] (kilogram, ef-3.1-biosphere)
    - Glyphosate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Glyphosate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - glyphosate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Glyphosate-trimesium  [air] (kilogram, ef-3.1-biosphere)
    - Glyphosate-trimesium  [water] (kilogram, ef-3.1-biosphere)
- item: Metolachlor  (emission to soil)
  quote:                                  -           4 Metolachlor                                        -            -         kg     3.64E-1        1           1.32
  candidates (flow name [compartment]):
    - Metolachlor  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - metolachlor  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - S-Metolachlor  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - metolachlor (s-isomer)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Metolachlor  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Metolachlor  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - metolachlor  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - S-Metolachlor  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Metsulfuron-methyl  (emission to soil)
  quote:                                  -           4 Metsulfuron-methyl                                 -            -         kg     1.68E-4        1           1.32
  candidates (flow name [compartment]):
    - Metsulfuron-methyl  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - metsulfuron-methyl  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Metsulfuron-methyl  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Metsulfuron-methyl  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - metsulfuron-methyl  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Methylamine  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - methylamine  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - 1-methylurea  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Prosulfuron  (emission to soil)
  quote:                                  -           4 Prosulfuron                                        -            -         kg     1.35E-3        1           1.32
  candidates (flow name [compartment]):
    - Prosulfuron  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - prosulfuron  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Prosulfuron  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Prosulfuron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - prosulfuron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Chlorpyrifos  (emission to soil)
  quote:                                  -           4 Chlorpyrifos                                       -            -         kg     8.07E-3        1           1.32
  candidates (flow name [compartment]):
    - Chlorpyrifos  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - chlorpyrifos  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Chlorpyrifos-methyl  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - chlorpyrifos-methyl  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Chlorpyrifos  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chlorpyrifos  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chlorpyrifos  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chlorpyrifos-methyl  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Terbufos  (emission to soil)
  quote:                                  -           4 Terbufos                                           -            -         kg     2.11E-2        1           1.32
  candidates (flow name [compartment]):
    - Terbufos  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - terbufos  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Terbufos  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Terbufos  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - terbufos  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
