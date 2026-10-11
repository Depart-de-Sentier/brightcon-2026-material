You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: aluminium profile, uncoated, SZFF 2014, recycling share 52%, at plant  (input)
  quote: technosphere                                                                 CH            0                     kg          1.75E+1             1                1.16
  search: aluminium profile uncoated SZFF 2014 recycling share 52% at plant
  candidates:
    - Aluminium profile, uncoated, SZFF 2014, recycling share 52%, at plant [CH] (kilogram, 2 inputs)
    - Aluminium profile, uncoated, SZFF 2014, recycling share 52%, with resource correction [CH] (kilogram, 2 inputs)
- item: anodising, aluminium sheet  (input)
  quote:               anodising, aluminium sheet                                     RER           0                     m2          4.34E+0             1                1.16
  search: anodising aluminium sheet
  candidates:
    - Anodising, aluminium sheet [RER] (square meter, 25 inputs)
    - Aluminium sheet, uncoated [CH] (kilogram, 2 inputs)
    - Aluminium sheet, uncoated, with resource correction [CH] (kilogram, 1 inputs)
    - Sealing sheet, aluminium, recycling share 2000 (32% Rec.) [CH] (kilogram, 2 inputs)
    - Sealing sheet, aluminium, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
    - Aluminium sheet, uncoated, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
    - Mineral wool insulation 40mm, cladding with aluminium sheet [CH] (square meter, 6 inputs)
    - Mineral wool insulation 50mm, cladding with aluminium sheet [CH] (square meter, 6 inputs)
- item: aluminium profile, uncoated, SZFF 2014, recycling share 52%, at plant (powder coated)  (input)
  quote:                                                                              CH            0                     kg          1.38E+1             1                1.16
  search: aluminium profile uncoated SZFF 2014 recycling share 52% at plant
  candidates:
    - Aluminium profile, uncoated, SZFF 2014, recycling share 52%, at plant [CH] (kilogram, 2 inputs)
    - Aluminium profile, uncoated, SZFF 2014, recycling share 52%, with resource correction [CH] (kilogram, 2 inputs)
- item: powder coating, aluminium sheet  (input)
  quote:               powder coating, aluminium sheet                                RER           0                     m2          3.41E+0             1                1.16
  search: powder coating aluminium sheet
  candidates:
    - Powder coating, aluminium sheet [RER] (square meter, 15 inputs)
    - Selective coating, aluminium sheet, nickel pigmented aluminium oxide [SK] (square meter, 11 inputs)
- item: transport, freight, lorry, fleet average  (input)
  quote:               transport, freight, lorry, fleet average                       CH            0                     tkm         3.75E+0             1                2.03
  search: transport freight lorry fleet average
  candidates:
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [CH] (ton kilometer, 20 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, 3.5t-7.5t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, fleet average, urban delivery [CH] (ton kilometer, 20 inputs)

Return only the JSON object described by the schema.
