You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Erdgas, in Industriefeuerung >100kW  (input)
  quote: Erdgas, in Industriefeuerung >100kW                         RER          - MJ                 9.06E+1      8.40E+1      7.35E+1      6.86E+1      1.37E+2      3.16E+0
  search: natural gas burned in industrial furnace >100kW
  candidates:
    - xxx Heat, natural gas, at industrial furnace low-NOx >100kW [RER] (megajoule, 1 inputs)
    - Natural gas, burned in industrial furnace 1MW [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace 1MWth [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace, for asphalt production, 1MWth [CH] (megajoule, 4 inputs)
- item: Heizöl EL, in Industriefeuerung 1MW, nicht-modulierend  (input)
  quote: Heizöl EL, in Industriefeuerung 1MW, nicht-modulierend      RER          - MJ                 9.06E+1      8.40E+1      7.35E+1      6.86E+1      1.37E+2      3.16E+0
  search: light fuel oil burned in industrial furnace 1MW non-modulating
  candidates:
    - Light fuel oil, burned in industrial furnace 1MW, non-modulating [RER] (megajoule, 5 inputs)
    - Light fuel oil, burned in industrial furnace 1MW, non-modulating [CH] (megajoule, 5 inputs)
    - Light fuel oil, burned in industrial furnace, for asphalt production, 1MW, non-modulating [CH] (megajoule, 5 inputs)
    - Heavy fuel oil, burned in industrial furnace 1MW, non-modulating [RER] (megajoule, 5 inputs)
    - Heavy fuel oil, burned in industrial furnace 1MW, non-modulating [CH] (megajoule, 5 inputs)
- item: Strom, Mittelspannung, Produktion UCTE, ab Netz  (input)
  quote: Strom, Mittelspannung, Produktion UCTE, ab Netz             UCTE         - kWh                2.18E+1      2.24E+1      2.92E+1      1.20E+1            -      2.40E-1
  search: electricity medium voltage production UCTE at grid
  candidates:
    - Electricity, medium voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from hard coal, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from natural gas, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - xxx Electricity, medium voltage, production UCTE, at grid [UCTE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from oil, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, high voltage, production from oil, UCTE at grid [CH] (kilowatt hour, 2 inputs)
- item: Elektrostahl, un- und niedriglegiert, ab Werk  (input)
  quote: Blasstahl, unlegiert, ab Werk                             RER            - kg                 1.18E+1      4.64E+0            -            -            -      2.43E-1
  search: steel electric un- and low-alloyed at plant
  candidates:
    - Steel, electric, un- and low-alloyed, at plant [RER] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [DE] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [FR] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [IT] (kilogram, 16 inputs)
    - Steel, electric, un- and low-alloyed, for reinforcing steel, import to CH, at plant [PL] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant, best plants (min. values) [RER] (kilogram, 16 inputs)
    - Steel, electric, low-alloyed, at plant, worst plants (max. values) [RER] (kilogram, 17 inputs)
    - Steel, electric, low-alloyed, at plant [CH] (kilogram, 23 inputs)
- item: Blasstahl, unlegiert, ab Werk  (input)
  quote: Blasstahl, unlegiert, ab Werk                               RER          - kg                 1.64E+1      2.17E+1      8.78E+0      1.54E+1      2.46E+1            -
  search: steel converter unalloyed at plant
  candidates:
    - Steel, converter, unalloyed, at plant [RER] (kilogram, 26 inputs)
    - Reinforcing steel, converter, at plant [RER] (kilogram, 2 inputs)
    - Steel, converter, low-alloyed, at plant [RER] (kilogram, 21 inputs)
    - Steel, converter, chromium steel 18/8, at plant [RER] (kilogram, 18 inputs)
    - Steel, electric, unalloyed, at plant [CH] (kilogram, 40 inputs)
- item: Aluminium, Produktionsmix, Knetlegierung, ab Werk  (input)
  quote: Aluminium, Produktionsmix, Knetlegierung, ab Werk           RER          - kg                 7.69E+0      7.59E+0      2.29E+1      8.80E-1      2.29E+1            -
  search: aluminium production mix wrought alloy at plant
  candidates:
    - Aluminium, production mix, wrought alloy, at plant [RER] (kilogram, 3 inputs)
    - Aluminium, production mix, cast alloy, at plant [RER] (kilogram, 3 inputs)
- item: Kupfer, ab Regionallager  (input)
  quote: Kupfer, ab Regionallager                                    RER          - kg                 6.21E-1      6.60E-1      4.40E-1      7.15E-1      7.15E-1      6.60E-1
  search: copper at regional storage
  candidates:
    - Copper, at regional storage [RER] (kilogram, 13 inputs)
    - Tin, at regional storage [RER] (kilogram, 13 inputs)
    - Gold, at regional storage [RER] (kilogram, 4 inputs)
    - Lead, at regional storage [RER] (kilogram, 5 inputs)
    - Diesel, at regional storage [RER] (kilogram, 15 inputs)
    - Indium, at regional storage [RER] (kilogram, 7 inputs)
    - Petrol, at regional storage [RER] (kilogram, 16 inputs)
    - Silver, at regional storage [RER] (kilogram, 6 inputs)
- item: Steinwolle, verpackt, ab Werk  (input)
  quote: Entsorgung, Gebäude, Mineralwolle, in Sortieranlage       CH         - kg             3.00E+0       1.60E+0              -              -                                                                                  -                              -
  search: rock wool packed at plant
  candidates:
    - Rock wool, packed, at plant [CH] (kilogram, 8 inputs)
    - Rock wool, Flumroc, packed, at plant [CH] (kilogram, 0 inputs, aggregated)
    - Rock wool, Flumroc, import, at plant [RER] (kilogram, 0 inputs, aggregated)
    - Rock wool plant [CH] (unit, 4 inputs)
    - Rock wool, at plant [CH] (kilogram, 31 inputs)
    - Rock wool, Flumroc, at plant [CH] (kilogram, 0 inputs, aggregated)
    - Disposal, rock wool, Flumroc, at plant [CH] (kilogram, 0 inputs, aggregated)
- item: Elektronik für technische Anlagen  (input)
  quote: Elektronik für technische Anlagen                           RER          - kg                 2.29E-1      1.50E-1      1.50E-1      3.50E-1      3.50E-1      6.00E-1
  search: electronics for control units
  candidates:
    - Electronics for control units [RER] (kilogram, 11 inputs)
    - Disposal, electronics for control units [RER] (kilogram, 5 inputs)
- item: Pulverbeschichten, Stahl  (input)
  quote: Bandverzinkung                                            RER            - m2                 1.46E+0      1.40E+0            -            -            -      1.00E-1
  search: powder coating steel
  candidates:
    - Powder coating, steel [RER] (square meter, 14 inputs)
    - Coating powder, at plant [RER] (kilogram, 11 inputs)
    - Powder coating, aluminium sheet [RER] (square meter, 15 inputs)
    - Selective coating, stainless steel sheet, black chrome [CH] (square meter, 10 inputs)
    - Disposal, steel board, 10 mm, powder coated, cardboard filled [CH] (square meter, 1 inputs)
    - Disposal, steel board, 20 mm, powder coated, cardboard filled [CH] (square meter, 1 inputs)
    - Steel board, 10 mm, powder coated, cardboard filled, at plant [CH] (square meter, 10 inputs)
    - Steel board, 20 mm, powder coated, cardboard filled, at plant [CH] (square meter, 10 inputs)
- item: Blech walzen, Aluminium  (input)
  quote: Blech walzen, Aluminium                                     RER          - kg                 7.69E+0      7.59E+0      2.29E+1      8.80E-1      2.29E+1            -
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
- item: Blech walzen, Stahl  (input)
  quote: Blech walzen, Stahl                                         RER          - kg                 2.53E+1      3.37E+1      1.34E+1      2.37E+1      3.82E+1            -
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
- item: Draht ziehen, Kupfer  (input)
  quote: Draht ziehen, Kupfer                                        RER          - kg                 6.21E-1      6.60E-1      4.40E-1      7.15E-1      7.15E-1      6.60E-1
  search: wire drawing copper
  candidates:
    - Wire drawing, copper [RER] (kilogram, 15 inputs)
    - Wire drawing, steel [RER] (kilogram, 23 inputs)
- item: Bandverzinkung  (input)
  quote: Entsorgung, Gebäude, Mineralwolle, in Sortieranlage       CH         - kg             3.00E+0       1.60E+0              -              -                                                                                  -                              -
  search: zinc coating coils
  candidates:
    - Zinc coating, coils [RER] (square meter, 17 inputs)
    - Zinc coating, pieces [RER] (square meter, 18 inputs)
    - Zinc coating for hydrogen pipeline [RER] (kilogram, 19 inputs)
    - Zinc coating, pieces, adjustment per um [RER] (square meter, 2 inputs)
- item: Entsorgung, Inertstoff, 5% Wasser, in Inertstoffdeponie  (input)
  quote: Entsorgung, Inertstoff, 5% Wasser, in Inertstoffdeponie   CH         - kg              2.20E-1      1.60E-1       1.45E-1               -                                                      4.60E-1                           -
  search: disposal inert material inert material landfill
  candidates:
    - Disposal, inert material, 0% water, to sanitary landfill [CH] (kilogram, 10 inputs)
    - Disposal, concrete, 5% water, to inert material landfill [GLO] (kilogram, 0 inputs)
    - xx Inert material landfill facility [CH] (unit, 10 inputs)
    - Process-specific burdens, inert material landfill [CH] (kilogram, 3 inputs)
- item: Transport, Fracht, Schiene  (input)
  quote: Transport, Fracht, Schiene                                RER        - tkm            9.49E+0       8.80E+0       7.70E+0      7.18E+0                                                         3.15E+1                     4.58E-1
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
- item: Transport, Lkw 32t  (input)
  quote: Transport, Lkw 32t                                        RER        - tkm            4.76E+0       4.40E+0       3.85E+0      3.60E+0                                                               -                     2.29E-1
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
- item: Lüftungskomponentenfabrik  (input)
  quote: Lüftungskomponentenfabrik                                 RER        1 unit            1.73E-7      1.60E-7       1.40E-7      1.31E-7                                                         2.60E-7                           -
  search: ventilation component factory
  candidates:
    - Ventilation components factory [RER] (unit, 4 inputs)
    - Ventilation system, various components [CH] (cubic meter, 27 inputs)
    - Ventilation system, various components, m2 [CH] (square meter, 27 inputs)
    - Disposal, ventilation system, various components, m2 [CH] (square meter, 8 inputs)
    - Disposal, ventilation system, various components, m3/h [CH] (cubic meter, 8 inputs)
    - Ventilation system, Bürohaus Fribourg, special components [CH] (unit, 6 inputs)
    - Ventilation system, Bürohaus Fribourg, various components [CH] (unit, 24 inputs)
    - Ventilation system, Schulhaus Heslibach, various components [CH] (unit, 26 inputs)

Return only the JSON object described by the schema.
