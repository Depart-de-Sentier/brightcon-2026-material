You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: aluminium, production mix, wrought alloy, at plant  (input)
  quote:  technos phere                                                       RER         0               kg       2.64E+0                3.27E+0              2.52E+0           2.84E+0                2.25E+0              3.98E+0                  2.30E+0             1 2.05 (1,2,1,1,1,na); Literature and own es timations
  search: aluminium production mix wrought alloy at plant
  candidates:
    - Aluminium, production mix, wrought alloy, at plant [RER] (kilogram, 3 inputs)
    - Aluminium, production mix, cast alloy, at plant [RER] (kilogram, 3 inputs)
- item: corrugated board, mixed fibre, single wall, at plant  (input)
  quote:                                                                      RER         0               kg       4.03E-2                    -                1.83E-2           1.33E-1                1.14E-1               8.64E-2                 1.33E-1             1 2.18 (3,4,3,1,3,5); Schwarz et al. 1992
  search: corrugated board mixed fibre single wall at plant
  candidates:
    - Corrugated board, mixed fibre, single wall, at plant [RER] (kilogram, 17 inputs)
    - Packaging, corrugated board, mixed fibre, single wall, at plant [RER] (kilogram, 19 inputs)
    - Corrugated board, mixed fibre, single wall, at plant [CH] (kilogram, 21 inputs)
    - Packaging, corrugated board, mixed fibre, single wall, at plant [CH] (kilogram, 14 inputs)
    - xx Corrugated board, fresh fibre, single wall, at plant [RER] (kilogram, 16 inputs)
    - xx Corrugated board, recycling fibre, single wall, at plant [RER] (kilogram, 16 inputs)
    - xx Corrugated board, fresh fibre, single wall, at plant [CH] (kilogram, 20 inputs)
    - xx Corrugated board, recycling fibre, single wall, at plant [CH] (kilogram, 20 inputs)
- item: polyethylene, HDPE, granulate, at plant  (input)
  quote:                 polyethylene, HDPE, granulate, at plant              RER         0               kg       7.32E-4                    -                1.92E+0           1.40E-3                2.82E-2               9.09E-4                 1.40E-3             1 2.05
  search: polyethylene HDPE granulate at plant
  candidates:
    - Polyethylene, HDPE, granulate, at plant [RER] (kilogram, 17 inputs, aggregated)
    - Polyethylene, LDPE, granulate, at plant [RER] (kilogram, 16 inputs, aggregated)
    - Polyethylene, LLDPE, granulate, at plant [RER] (kilogram, 17 inputs, aggregated)
    - Polyethylene terephthalate, granulate, amorphous, at plant [RER] (kilogram, 16 inputs)
    - Polyethylene terephthalate, granulate, bottle grade, at plant [RER] (kilogram, 1 inputs, aggregated)
- item: polystyrene, high impact, HIPS, at plant  (input)
  quote:                 polys tyrene, high impact, HIPS, at plant            RER         0               kg       3.66E-3                    -                8.30E-3           7.02E-3                6.02E-3               4.55E-3                 7.02E-3             1 2.18 (3,4,3,1,3,5); Schwarz et al. 1992
  search: polystyrene high impact HIPS at plant
  candidates:
    - Polystyrene, high impact, HIPS, at plant [RER] (kilogram, 8 inputs)
- item: steel, low-alloyed, at plant  (input)
  quote:                 steel, low-alloyed, at plant                         RER         0               kg       1.80E+0                    -                2.67E-1           1.50E+0                2.00E-1                  -                        -               1 2.05 (1,2,1,1,1,na); Literature and own es timations
  search: steel low-alloyed at plant
  candidates:
    - Steel, low-alloyed, at plant [RER] (kilogram, 3 inputs)
    - Steel, converter, low-alloyed, at plant [RER] (kilogram, 21 inputs)
    - Steel, electric, un- and low-alloyed, at plant [RER] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant, best plants (min. values) [RER] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant, worst plants (max. values) [RER] (kilogram, 17 inputs)
    - Steel, electric, low-alloyed, at plant [CH] (kilogram, 23 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [DE] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [FR] (kilogram, 16 inputs)
- item: section bar extrusion, aluminium  (input)
  quote:  technos phere                                                       RER         0               kg       2.64E+0                3.27E+0              2.52E+0           2.84E+0                2.25E+0              3.98E+0                  2.30E+0             1 2.05 (1,2,1,1,1,na); Literature and own es timations
  search: section bar extrusion aluminium
  candidates:
    - Section bar extrusion, aluminium [RER] (kilogram, 17 inputs)
- item: sheet rolling, steel  (input)
  quote:                 steel, low-alloyed, at plant                         RER         0               kg       1.80E+0                    -                2.67E-1           1.50E+0                2.00E-1                  -                        -               1 2.05 (1,2,1,1,1,na); Literature and own es timations
  search: sheet rolling steel
  candidates:
    - Sheet rolling, steel [RER] (kilogram, 24 inputs)
    - Sheet rolling, chromium steel [RER] (kilogram, 26 inputs)
    - Sheet rolling, electric steel [RER] (kilogram, 24 inputs)
    - Hot rolling, steel [RER] (kilogram, 20 inputs)
    - Sheet rolling, copper [RER] (kilogram, 15 inputs)
    - Sheet rolling, aluminium [RER] (kilogram, 16 inputs)
    - Section bar rolling, steel [RER] (kilogram, 1 inputs)
    - Hot rolling, electric steel [RER] (kilogram, 20 inputs)
- item: transport, lorry >16t, fleet average  (input)
  quote:  trans port     transport, lorry >16t, fleet average                 RER         0               tkm      2.24E-1                1.64E-1              2.56E-1           2.25E-1                2.07E-1               2.17E-1                 1.27E-1             1 2.14 (4,5,na,na,na,na); Standard dis tance 50km
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
- item: transport, freight, rail  (input)
  quote:                 steel, low-alloyed, at plant                         RER         0               kg       1.80E+0                    -                2.67E-1           1.50E+0                2.00E-1                  -                        -               1 2.05 (1,2,1,1,1,na); Literature and own es timations
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
- item: transport, van <3.5t  (input)
  quote:                 transport, van <3.5t                                 RER         0               tkm      4.44E-1                3.27E-1              4.72E-1           4.34E-1                3.75E-1              1.14E+0                  2.37E-1             1 2.18 (3,4,3,1,3,5); 100km to construction place
  search: transport van <3.5t
  candidates:
    - Van <3.5t [RER] (unit, 26 inputs)
    - Transport, barge [RER] (ton kilometer, 7 inputs)
    - Maintenance, van < 3.5t [RER] (unit, 12 inputs)
    - Transport, barge tanker [RER] (ton kilometer, 7 inputs)
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
    - Transport, barge, Betrieb [RER] (ton kilometer, 1 inputs)
    - Transport, barge, Fahrzeug [RER] (ton kilometer, 2 inputs)
    - Transport, aircraft, freight [RER] (ton kilometer, 5 inputs)
- item: disposal, packaging cardboard, 19.6% water, to municipal incineration  (input)
  quote:                                                                      RER         0               kg       4.03E-2                    -                1.83E-2           1.33E-1                1.14E-1               8.64E-2                 1.33E-1             1 2.18 (3,4,3,1,3,5); Schwarz et al. 1992
  search: disposal packaging cardboard municipal incineration
  candidates:
    - Disposal, packaging cardboard, 19.6% water, to municipal incineration [CH] (kilogram, 20 inputs)
    - Disposal, packaging paper, 13.7% water, to municipal incineration [CH] (kilogram, 20 inputs)
- item: disposal, building, polyethylene/polypropylene products, to final disposal  (input)
  quote:                 polyethylene, HDPE, granulate, at plant              RER         0               kg       7.32E-4                    -                1.92E+0           1.40E-3                2.82E-2               9.09E-4                 1.40E-3             1 2.05
  search: disposal building polyethylene polypropylene products final disposal
  candidates:
    - Disposal, building, polyethylene/polypropylene products, to final disposal [CH] (kilogram, 2 inputs)
- item: disposal, building, polystyrene isolation, flame-retardant, to final disposal  (input)
  quote:                 polys tyrene, high impact, HIPS, at plant            RER         0               kg       3.66E-3                    -                8.30E-3           7.02E-3                6.02E-3               4.55E-3                 7.02E-3             1 2.18 (3,4,3,1,3,5); Schwarz et al. 1992
  search: disposal building polystyrene isolation flame-retardant final disposal
  candidates:
    - Disposal, building, polystyrene isolation, flame-retardant, to final disposal [CH] (kilogram, 2 inputs)

Return only the JSON object described by the schema.
