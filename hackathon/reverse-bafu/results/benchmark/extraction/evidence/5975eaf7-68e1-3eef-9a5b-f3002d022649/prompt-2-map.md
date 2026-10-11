You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Fortluftauslass, Stahl / Alu, 85x365 mm, ab Werk  (input)
  quote: Fortluftauslass, Stahl / Alu, 85x365 mm, ab Werk            CH           - unit                     -            -            -            -      1.20E+1      1.20E+1
  search: exhaust air outlet steel aluminium
  candidates:
    - Exhaust air outlet, steel/aluminum, 85x365 mm, at plant [CH] (unit, 12 inputs)
- item: Zulufteinlass, Stahl / SS, DN 75, ab Werk  (input)
  quote: Zulufteinlass, Stahl / SS, DN 75, ab Werk                   RER          - unit               3.00E+1      3.00E+1      3.00E+1      3.00E+1      3.00E+1      3.00E+1
  search: supply air inlet steel
  candidates:
    - Supply air inlet, steel, SS, DN 75, at plant [RER] (unit, 12 inputs)
- item: Abluftventil, UP-Gehäuse, Kunststoff / Stahl, DN 125, ab Werk  (input)
  quote: Abluftventil, UP-Gehäuse, Kunststoff / Stahl, DN 125, ab Werk CH        -   unit             1.80E+1                1.80E+1                1.80E+1                1.80E+1               1.80E+1                  1.80E+1
  search: exhaust air valve plastic steel
  candidates:
    - Disposal, exhaust air valve, in-wall housing, plastic/steel, DN 125 [CH] (unit, 2 inputs)
    - Exhaust air valve, in-wall housing, plastic/steel, DN 125, at plant [CH] (unit, 14 inputs)
- item: AP-Luftverteilkasten, Stahl, 120 m3/h, ab Werk  (input)
  quote: Fortluftauslass, Stahl / Alu, 85x365 mm, ab Werk            CH           - unit                     -            -            -            -      1.20E+1      1.20E+1
  search: air distribution box steel
  candidates:
    - Air distribution housing, steel, 120 m3/h, at plant [CH] (unit, 12 inputs)
    - Disposal, air distribution housing, steel, 120 m3/h [CH] (unit, 2 inputs)
- item: Überströmelement, Stahl, ca. 40 m3/h, ab Werk  (input)
  quote: Abluftventil, UP-Gehäuse, Kunststoff / Stahl, DN 125, ab Werk CH        -   unit             1.80E+1                1.80E+1                1.80E+1                1.80E+1               1.80E+1                  1.80E+1
  search: overflow element steel
  candidates:
    - Disposal, overflow element, steel, approx. 40 m3/h [CH] (unit, 4 inputs)
    - Overflow element, steel, approx. 40 m3/h [RER] (unit, 14 inputs)
- item: Wickelfalzrohr, Stahl, DN 125, ab Werk  (input)
  quote: Fortluftauslass, Stahl / Alu, 85x365 mm, ab Werk            CH           - unit                     -            -            -            -      1.20E+1      1.20E+1
  search: spiral seam duct steel DN 125
  candidates:
    - Spiral-seam duct, steel, DN 125, at plant [RER] (meter, 11 inputs)
    - Disposal, spiral-seam duct, stainless steel, s= 0.5mm [CH] (square meter, 2 inputs)
    - Disposal, spiral-seam duct, stainless steel, s= 0.6mm [CH] (square meter, 2 inputs)
    - Disposal, spiral-seam duct, stainless steel, s= 0.8mm [CH] (square meter, 2 inputs)
    - Disposal, spiral-seam duct, stainless steel, s= 1.0mm [CH] (square meter, 2 inputs)
    - Spiral-seam duct, stainless steel, s= 0.5mm, at plant [CH] (square meter, 11 inputs)
    - Spiral-seam duct, stainless steel, s= 0.6mm, at plant [CH] (square meter, 11 inputs)
    - Spiral-seam duct, stainless steel, s= 0.8mm, at plant [CH] (square meter, 11 inputs)
- item: Lüftungsrohr, PE Wellrohr, DN 75, ab Werk  (input)
  quote: Lüftungsrohr, PE Wellrohr, DN 75, ab Werk                    RER     - m                       -      4.00E+2               -       4.00E+2                                                   -                  4.00E+2
  search: ventilation pipe PE corrugated DN 75
  candidates:
    - Ventilation duct, PE corrugated tube, DN 75, at plant [RER] (meter, 9 inputs)
- item: Flex Rohr, Alu / PET, DN 125, ab Werk  (input)
  quote: Entsorgung, Gebäude, Mineralwolle, in Sortieranlage        CH       - kg                                                                                                              1.26E+1                        1.60E+1                            1.00E+1                                                -
  search: flexible duct aluminium PET
  candidates:
    - Disposal, flexible duct, aluminum/PET, DN of 125 [CH] (meter, 5 inputs)
    - Flexible duct, aluminum/PET, DN of 125, at plant [RER] (meter, 16 inputs)
- item: Schalldämpfer, Stahl, DN 125, ab Werk  (input)
  quote: Schalldämpfer, Stahl, DN 125, ab Werk                        CH      - unit             2.40E+1       2.40E+1       1.20E+1         1.20E+1                                             2.40E+1                  2.40E+1
  search: silencer steel DN 125
  candidates:
    - Disposal, silencer, steel, DN 125 [CH] (unit, 2 inputs)
    - Silencer, steel, DN 125, at plant [CH] (unit, 12 inputs)
    - Disposal, silencer, steel, DN 315, 50 mm [CH] (unit, 2 inputs)
    - Silencer, steel, DN 315, 50 mm, at plant [CH] (unit, 13 inputs)
    - Disposal, exhaust air valve, in-wall housing, plastic/steel, DN 125 [CH] (unit, 2 inputs)
    - Exhaust air valve, in-wall housing, plastic/steel, DN 125, at plant [CH] (unit, 14 inputs)
    - Spiral-seam duct, steel, DN 125, at plant [RER] (meter, 11 inputs)
- item: Zu- Abluftfilter, dezentral, 180-250 m3/h, ab Werk  (input)
  quote: Fortluftauslass, Stahl / Alu, 85x365 mm, ab Werk            CH           - unit                     -            -            -            -      1.20E+1      1.20E+1
  search: air filter decentral ventilation
  candidates:
    - xx Disposal, air filter, decentralized unit, 250 m3/h [CH] (unit, 3 inputs)
    - Disposal, air filter, decentralized unit, 180-250 m3/h [CH] (unit, 3 inputs)
    - xx Air filter, decentralized unit, 250 m3/h, at plant [RER] (unit, 11 inputs)
    - Air filter, decentralized unit, 180-250 m3/h, at plant [RER] (unit, 11 inputs)
- item: Abluftfilter, in Abluftventil, ab Werk  (input)
  quote: Abluftventil, UP-Gehäuse, Kunststoff / Stahl, DN 125, ab Werk CH        -   unit             1.80E+1                1.80E+1                1.80E+1                1.80E+1               1.80E+1                  1.80E+1
  search: exhaust air filter
  candidates:
    - Disposal, air filter, in exhaust air valve [CH] (unit, 2 inputs)
    - Air filter, in exhaust air valve, at plant [RER] (unit, 9 inputs)
    - Disposal, air filter, central unit, 600 m3/h [CH] (unit, 3 inputs)
    - Disposal, exhaust air roof hood, steel, DN 400 [CH] (unit, 2 inputs)
    - Exhaust air roof hood, steel, DN 400, at plant [CH] (unit, 11 inputs)
    - xx Disposal, air filter, decentralized unit, 250 m3/h [CH] (unit, 3 inputs)
    - Disposal, air filter, decentralized unit, 180-250 m3/h [CH] (unit, 3 inputs)
    - Exhaust air system for kitchen in appartment buildings [CH] (square meter, 9 inputs)
- item: Kaltschrumpfband, Alu/ PE, 50 mm breit, ab Werk  (input)
  quote: Kaltschrumpfband, Alu/ PE, 50 mm breit, ab Werk              RER     - m               7.00E+2        2.00E+2       7.00E+2         2.00E+2                                             7.00E+2                  2.00E+2
  search: cold shrink tape aluminium PE
  candidates:
    - (no candidate found)
- item: Steuerung, Verkablung, dezentral, ab Werk  (input)
  quote:                                             CH          -   kg                  2.50E+0                   2.20E+0                                         -        6.00E+0                 1.90E+0                 1.50E+0                  2.70E-1                    2.00E-1                                 -
  search: control unit cabling decentral ventilation
  candidates:
    - (no candidate found)
- item: Lüftungsgerät, dezentral, 180-250 m3/h, ab Werk  (input)
  quote:                                             CH          -   kg                  2.50E+0                   2.20E+0                                         -        6.00E+0                 1.90E+0                 1.50E+0                  2.70E-1                    2.00E-1                                 -
  search: ventilation device decentral
  candidates:
    - Disposal, ventilation equipment, decentralized, 180-250 m3 [CH] (unit, 8 inputs)
    - Ventilation system, decentralized, 6 x 120 m3/h, PE ducts, with GHE [CH] (unit, 37 inputs)
    - Ventilation system, decentralized, 6 x 120 m3/h, PE ducts, without GHE [CH] (unit, 29 inputs)
    - Ventilation system, decentralized, 6 x 120 m3/h, steel ducts, with GHE [CH] (unit, 39 inputs)
    - Ventilation of dwellings, decentralized, 6 x 120 m3/h, PE ducts, with GHE [CH] (square meter-year, 17 inputs)
    - Ventilation system, decentralized, 6 x 120 m3/h, steel ducts, without GHE [CH] (unit, 30 inputs)
    - Ventilation of dwellings, decentralized, 6 x 120 m3/h, PE ducts, without GHE [CH] (square meter-year, 17 inputs)
    - Ventilation of dwellings, decentralized, 6 x 120 m3/h, steel ducts, with GHE [CH] (square meter-year, 17 inputs)
- item: Entsorgung, Gebäude, Massiveisen ohne Armierungseisen, in Sortieranlage  (input)
  quote:                                                              CH      - kg               1.32E+3       3.29E+2       1.35E+3         3.59E+2                                             1.11E+3                  1.19E+2
  search: disposal building bulk iron sorting plant
  candidates:
    - Disposal, building, bulk iron (excluding reinforcement), to sorting plant [CH] (kilogram, 4 inputs)
- item: Entsorgung, Gebäude, Polyethylen/Polypropylen-Produkte, in Beseitigung  (input)
  quote:                                                              CH      - kg               3.60E+2       4.92E+2       3.60E+2         4.92E+2                                                            -         1.32E+2
  search: disposal building polyethylene polypropylene products final disposal
  candidates:
    - Disposal, building, polyethylene/polypropylene products, to final disposal [CH] (kilogram, 2 inputs)
- item: Entsorgung, Abluftventil, UP-Gehäuse, Kunststoff / Stahl, DN 125  (input)
  quote: Abluftventil, UP-Gehäuse, Kunststoff / Stahl, DN 125, ab Werk CH        -   unit             1.80E+1                1.80E+1                1.80E+1                1.80E+1               1.80E+1                  1.80E+1
  search: disposal exhaust air valve
  candidates:
    - Disposal, air filter, in exhaust air valve [CH] (unit, 2 inputs)
    - Disposal, exhaust air valve, in-wall housing, plastic/steel, DN 125 [CH] (unit, 2 inputs)
    - Disposal, exhaust air roof hood, steel, DN 400 [CH] (unit, 2 inputs)
    - Disposal, exhaust air system for kitchen in appartment buildings [CH] (square meter, 1 inputs)
    - Exhaust air valve, in-wall housing, plastic/steel, DN 125, at plant [CH] (unit, 14 inputs)
    - Disposal, exhaust air system for kitchen and bathroom in appartment buildings [CH] (square meter, 6 inputs)
    - Air filter, in exhaust air valve, at plant [RER] (unit, 9 inputs)
- item: Entsorgung, AP-Luftverteilkasten, Stahl, 120 m3/h  (input)
  quote: Fortluftauslass, Stahl / Alu, 85x365 mm, ab Werk            CH           - unit                     -            -            -            -      1.20E+1      1.20E+1
  search: disposal air distribution box steel
  candidates:
    - Disposal, air distribution housing, steel, 120 m3/h [CH] (unit, 2 inputs)
- item: Entsorgung, Überströmelement, Stahl, ca. 40 m3/h  (input)
  quote: Abluftventil, UP-Gehäuse, Kunststoff / Stahl, DN 125, ab Werk CH        -   unit             1.80E+1                1.80E+1                1.80E+1                1.80E+1               1.80E+1                  1.80E+1
  search: disposal overflow element steel
  candidates:
    - Disposal, overflow element, steel, approx. 40 m3/h [CH] (unit, 4 inputs)
    - Overflow element, steel, approx. 40 m3/h [RER] (unit, 14 inputs)
- item: Entsorgung, Flex Rohr, Alu / PET, DN 125  (input)
  quote: Entsorgung, Gebäude, Mineralwolle, in Sortieranlage        CH       - kg                                                                                                              1.26E+1                        1.60E+1                            1.00E+1                                                -
  search: disposal flexible duct aluminium PET
  candidates:
    - Disposal, flexible duct, aluminum/PET, DN of 125 [CH] (meter, 5 inputs)
- item: Entsorgung, Schalldämpfer, Stahl, DN 125  (input)
  quote: Schalldämpfer, Stahl, DN 125, ab Werk                        CH      - unit             2.40E+1       2.40E+1       1.20E+1         1.20E+1                                             2.40E+1                  2.40E+1
  search: disposal silencer steel DN 125
  candidates:
    - Disposal, silencer, steel, DN 125 [CH] (unit, 2 inputs)
    - Silencer, steel, DN 125, at plant [CH] (unit, 12 inputs)
    - Disposal, silencer, steel, DN 315, 50 mm [CH] (unit, 2 inputs)
    - Disposal, exhaust air valve, in-wall housing, plastic/steel, DN 125 [CH] (unit, 2 inputs)
- item: Entsorgung, Zu- Abluftfilter, dezentral, 180-250 m3/h  (input)
  quote: Fortluftauslass, Stahl / Alu, 85x365 mm, ab Werk            CH           - unit                     -            -            -            -      1.20E+1      1.20E+1
  search: disposal air filter decentral
  candidates:
    - xx Disposal, air filter, decentralized unit, 250 m3/h [CH] (unit, 3 inputs)
    - Disposal, air filter, decentralized unit, 180-250 m3/h [CH] (unit, 3 inputs)
    - Disposal, air filter, in exhaust air valve [CH] (unit, 2 inputs)
    - Disposal, air filter, central unit, 600 m3/h [CH] (unit, 3 inputs)
    - xx Air filter, decentralized unit, 250 m3/h, at plant [RER] (unit, 11 inputs)
    - Air filter, decentralized unit, 180-250 m3/h, at plant [RER] (unit, 11 inputs)
- item: Entsorgung, Abluftfilter, in Abluftventil  (input)
  quote: Abluftventil, UP-Gehäuse, Kunststoff / Stahl, DN 125, ab Werk CH        -   unit             1.80E+1                1.80E+1                1.80E+1                1.80E+1               1.80E+1                  1.80E+1
  search: disposal exhaust air filter
  candidates:
    - Disposal, air filter, in exhaust air valve [CH] (unit, 2 inputs)
    - Disposal, air filter, central unit, 600 m3/h [CH] (unit, 3 inputs)
    - Disposal, exhaust air roof hood, steel, DN 400 [CH] (unit, 2 inputs)
    - xx Disposal, air filter, decentralized unit, 250 m3/h [CH] (unit, 3 inputs)
    - Disposal, air filter, decentralized unit, 180-250 m3/h [CH] (unit, 3 inputs)
    - Disposal, exhaust air system for kitchen in appartment buildings [CH] (square meter, 1 inputs)
    - Disposal, exhaust air valve, in-wall housing, plastic/steel, DN 125 [CH] (unit, 2 inputs)
    - Disposal, exhaust air system for kitchen and bathroom in appartment buildings [CH] (square meter, 6 inputs)
- item: Entsorgung, Kaltschrumpfband, Alu/ PE, 50 mm breit  (input)
  quote: Kaltschrumpfband, Alu/ PE, 50 mm breit, ab Werk              RER     - m               7.00E+2        2.00E+2       7.00E+2         2.00E+2                                             7.00E+2                  2.00E+2
  search: disposal cold shrink tape
  candidates:
    - (no candidate found)
- item: Entsorgung, Steuerung, Verkablung, dezentral  (input)
  quote:                                             CH          -   kg                  2.50E+0                   2.20E+0                                         -        6.00E+0                 1.90E+0                 1.50E+0                  2.70E-1                    2.00E-1                                 -
  search: disposal control unit cabling decentral
  candidates:
    - Disposal, control and wiring, decentralized unit [CH] (unit, 3 inputs)
- item: Entsorgung, Lüftungsgerät, dezentral, 180-250 m3/h  (input)
  quote:                                             CH          -   kg                  2.50E+0                   2.20E+0                                         -        6.00E+0                 1.90E+0                 1.50E+0                  2.70E-1                    2.00E-1                                 -
  search: disposal ventilation device decentral
  candidates:
    - Disposal, ventilation equipment, decentralized, 180-250 m3 [CH] (unit, 8 inputs)
- item: Transport, Lkw 32t  (input)
  quote: Transport, Lkw 32t                                           RER     - tkm              5.72E+2       3.33E+2       5.32E+2         2.92E+2                                             3.31E+2                  9.21E+1
  search: transport lorry 32t
  candidates:
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [CH] (ton kilometer, 33 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, long haul [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2006, EURO-IV, long haul [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2020, EURO-VI, long haul [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, fleet average, long haul [CH] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2002, EURO-III, long haul [CH] (ton kilometer, 11 inputs)
    - Transport, freight, lorry, diesel, 32t gross weight, 2010, EURO-V, urban delivery [CH] (ton kilometer, 11 inputs)
- item: Transport, Lkw 28t  (input)
  quote: Transport, Lkw 28t                                           CH      - tkm              8.76E+0       8.76E+0       8.84E+0         8.84E+0                                             9.43E+0                  9.43E+0
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
- item: Transport, Lieferwagen <3.5t  (input)
  quote: Transport, Lieferwagen <3.5t                                 CH      - tkm              1.26E+2       8.16E+1       1.15E+2         7.05E+1                                             8.86E+1                  4.41E+1
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

Return only the JSON object described by the schema.
