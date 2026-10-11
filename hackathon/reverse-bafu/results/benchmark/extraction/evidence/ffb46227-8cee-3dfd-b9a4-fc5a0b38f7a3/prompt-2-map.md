You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (GLO), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Sheet rolling, aluminium  (input)
  quote:  Sheet rolling, aluminium/RER U                                        kg                                                  6.00e+00
  search: sheet rolling aluminium
  candidates:
    - Sheet rolling, aluminium [RER] (kilogram, 16 inputs)
    - Sheet rolling, steel [RER] (kilogram, 24 inputs)
    - Sheet rolling, copper [RER] (kilogram, 15 inputs)
    - Anodising, aluminium sheet [RER] (square meter, 25 inputs)
    - Sheet rolling, chromium steel [RER] (kilogram, 26 inputs)
    - Sheet rolling, electric steel [RER] (kilogram, 24 inputs)
    - Powder coating, aluminium sheet [RER] (square meter, 15 inputs)
    - Aluminium sheet, uncoated [CH] (kilogram, 2 inputs)
- item: Aluminium alloy, AlMg3, at plant  (input)
  quote:  Aluminium alloy, AlMg3, at plant/RER U                                kg                                                  6.00e+00
  search: aluminium alloy AlMg3 at plant
  candidates:
    - Aluminium alloy, AlMg3, at plant [RER] (kilogram, 11 inputs)
    - Aluminium, production mix, cast alloy, at plant [RER] (kilogram, 3 inputs)
    - Aluminium, production mix, wrought alloy, at plant [RER] (kilogram, 3 inputs)
- item: Sheet rolling, chromium steel  (input)
  quote:  Sheet rolling, chromium steel/RER U                                   kg                                                  9.00e+00
  search: sheet rolling chromium steel
  candidates:
    - Sheet rolling, chromium steel [RER] (kilogram, 26 inputs)
    - Sheet rolling, steel [RER] (kilogram, 24 inputs)
    - Sheet rolling, electric steel [RER] (kilogram, 24 inputs)
    - Tin plated chromium steel sheet, 2 mm, at plant [RER] (square meter, 3 inputs)
    - Chromium steel sheet 18/8, recycling share 2000 (37% Rec.) [CH] (kilogram, 2 inputs)
    - Chromium steel sheet 18/8, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
    - Chromium-nickel steel sheet 18/8, recycling share 2000 (37% Rec.) [CH] (kilogram, 2 inputs)
    - Chromium-nickel steel sheet 18/8, secondary production (100% Rec.) [CH] (kilogram, 2 inputs)
- item: Chromium steel 18/8, at plant  (input)
  quote:  Chromium steel 18/8, at plant/RER U                                  kg                                        9.00e+00
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
- item: carbon fiber production, weaved, at factory  (input)
  quote:  carbon fiber production, weaved, at factory/RER U                    kg                                        7.14e+01
  search: carbon fibre weaved at factory
  candidates:
    - Carbon fiber, weaved, at factory [RER] (kilogram, 2 inputs)
    - Carbon fiber production, weaved, at factory [RER] (kilogram, 3 inputs)
- item: Epoxy resin, liquid, at plant  (input)
  quote:  Epoxy resin, liquid, at plant/RER U                                  kg                                        3.06e+01
  search: epoxy resin liquid at plant
  candidates:
    - Epoxy resin, liquid, at plant [RER] (kilogram, 9 inputs)
    - Epoxy resin, liquid, disaggregated data, at plant [RER] (kilogram, 9 inputs)
    - Epoxy resin insulator (SiO2), at plant [RER] (kilogram, 4 inputs)
    - Epoxy resin insulator (Al2O3), at plant [RER] (kilogram, 4 inputs)
    - Flooring 2K, epoxy resin, industrial use, at plant [CH] (square meter, 16 inputs)
    - Flooring, 2K epoxy resin PU, living and administration, at plant [CH] (square meter, 17 inputs)
- item: Sheet rolling, copper  (input)
  quote:  Sheet rolling, copper/RER U                                          kg                                        9.00e+00
  search: sheet rolling copper
  candidates:
    - Sheet rolling, copper [RER] (kilogram, 15 inputs)
    - Sheet rolling, steel [RER] (kilogram, 24 inputs)
    - Sheet rolling, aluminium [RER] (kilogram, 16 inputs)
    - Sheet rolling, chromium steel [RER] (kilogram, 26 inputs)
    - Sheet rolling, electric steel [RER] (kilogram, 24 inputs)
    - Selective coating, copper sheet, black chrome [RER] (square meter, 15 inputs)
    - Copper sheet, uncoated, primary production (0% Rec.) [CH] (kilogram, 2 inputs)
    - Copper sheet, uncoated, high recycling share (85% Rec.) [CH] (kilogram, 2 inputs)
- item: Steel, low-alloyed, at plant  (input)
  quote:  Steel, low-alloyed, at plant/RER U                                   kg                                        9.00e+00
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
- item: transport, freight, rail  (input)
  quote:  transport, freight, rail/tkm/RER U                                   tkm                                       2.32e+01     Generic transport distances are
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
- item: transport, freight, lorry 16-32 metric ton, fleet average  (input)
  quote:  transport, freight, lorry 16-32 metric ton, fleet average/RER U      tkm                                       4.83e+01     Generic transport distances are
  search: transport freight lorry 16-32t fleet average
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, fleet average, long haul [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, fleet average, urban delivery [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, fleet average, regional delivery [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, fleet average [RER] (ton kilometer, 4 inputs)
- item: transport, barge tanker  (input)
  quote:  transport, barge tanker/tkm/RER U                                    tkm                                       7.14e+00     Generic transport distances are
  search: transport barge tanker
  candidates:
    - Transport, barge tanker [RER] (ton kilometer, 7 inputs)
    - Barge tanker [RER] (unit, 20 inputs)
    - Transport, barge [RER] (ton kilometer, 7 inputs)
    - Transport, barge, Betrieb [RER] (ton kilometer, 1 inputs)
    - Transport, barge, Fahrzeug [RER] (ton kilometer, 2 inputs)
    - Transport, barge, Infrastruktur [RER] (ton kilometer, 4 inputs)
    - Transport, transoceanic tanker [OCE] (ton kilometer, 7 inputs)
    - Transport, transoceanic tanker, Betrieb [OCE] (ton kilometer, 2 inputs)
- item: electricity, low voltage, production ENTSO, at grid  (input)
  quote:  electricity, low voltage, production ENTSO, at grid/kWh/ENTSO U      kWh                                       4.50e+00
  search: electricity low voltage production ENTSO at grid
  candidates:
    - Electricity, low voltage, production ENTSO-E, at grid [ENTSO-E] (kilowatt hour, 3 inputs)
    - xxx Electricity, low voltage, production ENTSO, at grid [ENTSO-E] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production GLO, at grid [GLO] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, import ENTSO, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production from oil, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, low voltage, production from biogas, at grid [CH] (kilowatt hour, 3 inputs)

Return only the JSON object described by the schema.
