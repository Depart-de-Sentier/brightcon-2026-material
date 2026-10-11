You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: rock wool, at plant  (input)
  quote:            rock wool, at         1.530E+00          1.913E+00         2.295E+00          3.060E+00         3.825E+00
  search: rock wool at plant
  candidates:
    - Rock wool plant [CH] (unit, 4 inputs)
    - Rock wool, at plant [CH] (kilogram, 31 inputs)
    - Rock wool, packed, at plant [CH] (kilogram, 8 inputs)
    - Rock wool, Flumroc, at plant [CH] (kilogram, 0 inputs, aggregated)
    - Rock wool, Flumroc, packed, at plant [CH] (kilogram, 0 inputs, aggregated)
    - Disposal, rock wool, Flumroc, at plant [CH] (kilogram, 0 inputs, aggregated)
    - Rock wool, Flumroc, import, at plant [RER] (kilogram, 0 inputs, aggregated)
    - Glass wool mat, at plant [CH] (kilogram, 43 inputs)
- item: glass wool mat, at plant  (input)
  quote:            glass wool mat,       1.530E+00          1.913E+00         2.295E+00          3.060E+00         3.825E+00
  search: glass wool mat at plant
  candidates:
    - Glass wool mat, at plant [CH] (kilogram, 43 inputs)
    - Glass wool mat, phenolic binder ISOVER, at plant [CH] (kilogram, 0 inputs, aggregated)
    - Glass wool mat, bio-based binder ISOVER, at plant [CH] (kilogram, 0 inputs, aggregated)
- item: aluminium, production mix, at plant  (input)
  quote:            aluminium,            1.080E-01          1.080E-01         1.080E-01          1.080E-01         1.080E-01
  search: aluminium production mix at plant
  candidates:
    - Aluminiumtrihydroxide-acrylic glass, production mix, at plant [CH] (kilogram, 6 inputs)
    - Aluminium, production mix for aluminium profiles, SZFF 2014, at plant [CH] (kilogram, 3 inputs)
    - Aluminium, production mix, at plant [RER] (kilogram, 3 inputs)
    - Aluminium, production mix, cast alloy, at plant [RER] (kilogram, 3 inputs)
    - Aluminium, production mix, wrought alloy, at plant [RER] (kilogram, 3 inputs)
    - Synthetic gas, production mix, at plant [CH] (cubic meter, 2 inputs)
    - Electricity, production mix photovoltaic, at plant [CH] (kilowatt hour, 29 inputs)
    - Formaldehyde, production mix, at plant [RER] (kilogram, 6 inputs)
- item: sheet rolling, aluminium  (input)
  quote:            sheet rolling,        1.080E-01          1.080E-01         1.080E-01          1.080E-01         1.080E-01
  search: sheet rolling aluminium
  candidates:
    - Sheet rolling, aluminium [RER] (kilogram, 16 inputs)
    - Aluminium sheet, uncoated [CH] (kilogram, 2 inputs)
    - Aluminium sheet, uncoated, with resource correction [CH] (kilogram, 1 inputs)
    - Sealing sheet, aluminium, recycling share 2000 (32% Rec.) [CH] (kilogram, 2 inputs)
    - Sealing sheet, aluminium, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
    - Aluminium sheet, uncoated, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
    - Mineral wool insulation 40mm, cladding with aluminium sheet [CH] (square meter, 6 inputs)
    - Mineral wool insulation 50mm, cladding with aluminium sheet [CH] (square meter, 6 inputs)
- item: polyethylene, LDPE, granulate, at plant  (input)
  quote:            polyethylene,         5.433E-02          5.433E-02         5.433E-02          5.433E-02         5.433E-02
  search: polyethylene LDPE granulate at plant
  candidates:
    - Polyethylene, LDPE, granulate, at plant [RER] (kilogram, 16 inputs, aggregated)
    - Polyethylene, HDPE, granulate, at plant [RER] (kilogram, 17 inputs, aggregated)
    - Polyethylene, LLDPE, granulate, at plant [RER] (kilogram, 17 inputs, aggregated)
    - Polyethylene terephthalate, granulate, amorphous, at plant [RER] (kilogram, 16 inputs)
    - Polyethylene terephthalate, granulate, bottle grade, at plant [RER] (kilogram, 1 inputs, aggregated)
- item: injection moulding  (input)
  quote:            injection moul-       5.433E-02          5.433E-02         5.433E-02          5.433E-02         5.433E-02
  search: injection moulding
  candidates:
    - Injection moulding [RER] (kilogram, 17 inputs)
    - Glass fibre reinforced plastic, polyamide, injection moulding, at plant [RER] (kilogram, 6 inputs)
    - xx Blow moulding [RER] (kilogram, 7 inputs)
    - Stretch blow moulding [RER] (kilogram, 5 inputs)
- item: transport, freight, rail  (input)
  quote:            transport, freight,   3.385E-01          4.150E-01         4.915E-01          6.445E-01         7.975E-01
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
- item: transport, lorry 20-28t, fleet average  (input)
  quote:            transport, lorry      6.932E-02          8.462E-02         9.992E-02          1.305E-01         1.611E-01
  search: transport lorry 20-28t fleet average
  candidates:
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - xxx Operation, lorry >28t, fleet average [CH] (kilometer, 1 inputs)
    - xxx Operation, lorry 20-28t, fleet average [CH] (kilometer, 1 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [CH] (ton kilometer, 20 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [CH] (ton kilometer, 11 inputs)

Return only the JSON object described by the schema.
