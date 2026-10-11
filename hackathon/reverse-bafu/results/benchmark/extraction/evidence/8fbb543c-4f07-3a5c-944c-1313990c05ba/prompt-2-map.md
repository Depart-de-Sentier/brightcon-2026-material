You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: polyurethane, rigid foam, at plant  (input)
  quote:            polyurethane,         9.000E-01          1.200E+00        1.500E+00       1.800E+00         2.400E+00
  search: polyurethane rigid foam at plant
  candidates:
    - Polyurethane, rigid foam, at plant [RER] (kilogram, 7 inputs)
    - Polyurethane, rigid foam, market mix, at regional storage [CH] (kilogram, 4 inputs)
    - Polyurethane, flexible foam, at plant [RER] (kilogram, 6 inputs)
- item: polyvinylchloride, at regional storage  (input)
  quote:            polyvinylchloride,    4.273E-01          4.273E-01        4.273E-01       4.273E-01         4.273E-01
  search: polyvinylchloride at regional storage
  candidates:
    - Polyvinylchloride, at regional storage [RER] (kilogram, 4 inputs)
    - Rail, at regional storage [CH] (kilogram, 10 inputs)
    - Diesel, at regional storage [CH] (kilogram, 18 inputs)
    - Petrol, at regional storage [CH] (kilogram, 19 inputs)
    - Naphtha, at regional storage [CH] (kilogram, 14 inputs)
    - Kerosene, at regional storage [CH] (kilogram, 15 inputs)
    - Methanol, at regional storage [CH] (kilogram, 6 inputs)
    - Rape oil, at regional storage [CH] (kilogram, 11 inputs)
- item: extrusion, plastic film  (input)
  quote:            extrusion, plastic    4.273E-01          4.273E-01        4.273E-01       4.273E-01         4.273E-01
  search: extrusion plastic film
  candidates:
    - Extrusion, plastic film [RER] (kilogram, 16 inputs)
    - Extrusion, plastic pipes [RER] (kilogram, 13 inputs)
- item: transport, freight, rail  (input)
  quote:            transport, freight,   2.655E-01          3.255E-01        3.855E-01       4.455E-01         5.655E-01
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
  quote:            transport, lorry      6.636E-02          8.136E-02        9.636E-02       1.114E-01         1.414E-01
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
