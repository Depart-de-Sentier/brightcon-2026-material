You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Final repository for nuclear waste SF, HLW, and ILW` [CH], reference unit 1 p, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~19 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: waste / nuclear waste\infrastructure
- includedProcesses: This module includes the material and energy requirements as well as transports for mining and refilling of shafts and tunnels of a repository for spent fuel, vitrified high-level waste and long-lived intermediate radioactive waste in the Swiss context. Also included is disposal of part of the mined rock. Land use of the entrance area and buildings are accounted for. Wastewater is not included.
- technology: Currently available knowledge.
- generalComment: This module is based on the Swiss project "Opalinus Clay" for a conditioned spent fuel (SF), vitrified high level waste (HLW) and intermediate level waste (ILW) repository developed to fullfill the concept of a "monitored long-term geological disposal" in deep geologic stratum. A 5 km long ramp leads to the approximately 650 m deep and 120 m thick host rock. The depository is made of: a pilot facility to be monitored;
Synonyms: Conditioned Spent Fuel, High level radioactive waste, Intermediate level radioactive waste, Geological repository; 
UUID: 0a5b5999-d064-3e3f-b0b6-bf9903a75c35
- source cited in the metadata: Dones R. | 2009 | 2009 - Nuclear energy - Dones
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 p):
- none

## Report excerpt

Source file: `report-p341-343.txt` (SHA-256 bf9bccf1272bc4f766f664c1d1e261499f5f71b277d34df90ff2db404e908d22), pages 341-343 of `2009 - Nuclear energy - Dones.pdf`.

```
Endlagerung der radioaktiven Abfälle


     12.9        Übersicht über die Eingabedaten
     In Tab. 12.13 bis Tab. 12.16 sind die Eingabedaten für die Bilanzierung der Endlager SMA
     und BE/HAA/LMA zusammengefasst. Tab. 12.17 zeigt den Datensatz für die Entsorgung schwach
     radioaktiver Abfälle.

     Tab. 12.13 Zusammenstellung der Eingabedaten für die Infrastruktur des geologischen Endlagers für kurzlebige,
                                                                   98
                 schwach- und mittelaktive Abfälle (SMA).




                                                                                                                     Uncertainty




                                                                                                                                            Comment
                                                                                                                      Deviation
                                                                                                                      Standard
                                                                            Location




                                                                                                                                             General
                                                                                                                        Type
                                                                                              final repository for




                                                                                                                        95%
                                                                                       Unit
                                   Name
                                                                                              nuclear waste LLW


                                                               Location                              CH
                                                                   Unit                              unit
     Transformation, from unknown                                             m2                  3.25E+04            1     2    own assumption
     Transformation, to industrial area, built up                             m2                  2.60E+04            1     2    own assumption
     Transformation, to industrial area, vegetation                           m2                  6.50E+03            1     2    own assumption
     Transformation, from industrial area                                     m2                  3.25E+04            1     2    own assumption
     Transformation, to unknown                                               m2                  3.25E+04            1     2    own assumption
     Occupation, industrial area, built up                                    m2a                 7.28E+05            1     3    own assumption, time factor
     Occupation, industrial area, vegetation                                  m2a                 1.82E+05            1     3    own assumption, time factor
     building, multi-storey                                               RER m3                  1.30E+05            1     2    own assumption
     Industrial machine, heavy, unspecified, at plant                     RER kg                  1.60E+06            1    1.5   own assumption
     electricity, medium voltage, at grid                                 CH kWh                  7.39E+07            1     2    own assumption
     diesel, burned in building machine                                   GLO MJ                  1.50E+07            1     2    own assumption
     reinforcing steel, at plant                                          RER kg                  1.67E+07            1     2    own assumption
     concrete, normal, at plant                                           CH m3                   8.40E+04            1     2    own assumption
     transport, lorry 28t                                                 CH tkm                  1.44E+07            1    2.1   standard
     transport, freight, rail                                             RER tkm                 1.03E+07            1    2.1   standard
     treatment, sewage, unpolluted, to wastewater treatment, class 3      CH m3                   2.55E+05            1     2    own assumption
     disposal, inert waste, 5% water, to inert material landfill          CH kg                   3.00E+08            1     2    own assumption
     Heat, waste                                                               MJ                 2.66E+08            1     2    same as electricity
     Methane, fossil                                                           kg                 1.60E+06            1     4    own assumption
     all emissions to "air, low population density"




98
     Die Tabelle zeigt die in Version v1.01 der ecoinvent Datenbank enthaltenen Eingabedaten. Die Bilanzierung von „concrete,
     normal, at plant“, „transport, lorry 28t“ und „treatment, sewage, unpolluted, to wastewater treatment, class 3“ ist nicht
     korrekt, die richtigen Wert betragen 87000 m3/unit, 1.86E+7 tkm/unit bzw. 1.1E5 m3/unit. Die korrekten Eingabedaten sind
     im Text beschrieben. Die Fehler werden in v.1.1 korrigiert.




     ecoinvent-Bericht No. 6 - Teil VII                                   - 315 -
                                                         Endlagerung der radioaktiven Abfälle


     Tab. 12.14 Zusammenstellung der Eingabedaten für die Infrastruktur des geologischen Endlagers für hoch und
                                                                    99
                    mittelaktive Abfälle (BE/HAA/LMA).




                                                                                                                         Uncertainty




                                                                                                                                                                      Comment
                                                                                                                          Deviation
                                                                                                                          Standard
                                                                          Location




                                                                                                                                                                       General
                                                                                              final repository for




                                                                                                                            Type


                                                                                                                            95%
                                                                                     Unit
                                    Name                                                      nuclear waste SF,
                                                                                                 HLW, and ILW

                                                            Location                                 CH
                                                                Unit                                 unit
      Transformation, from unknown                                           m2                   3.25E+04                  1   1.5 own assumption on preliminary project data
      Transformation, to industrial area, built up                           m2                   2.60E+04                  1   1.5 own assumption on preliminary project data
      Transformation, to industrial area, vegetation                         m2                   6.50E+03                  1   1.5 own assumption on preliminary project data
      Transformation, from industrial area                                   m2                   3.25E+04                  1   1.5 own assumption on preliminary project data
      Transformation, to unknown                                             m2                   3.25E+04                  1   1.5 own assumption on preliminary project data
      Occupation, industrial area, built up                                  m2a                  5.34E+05                  1     3 own assumption, time factor
      Occupation, industrial area, vegetation                                m2a                  1.34E+05                  1     3 own assumption, time factor
      building, multi-storey                                             RER m3                   1.30E+05                  1     2 own assumption
      Industrial machine, heavy, unspecified, at plant                   RER kg                   4.20E+06                  1   1.5 own assumption
      electricity, medium voltage, at grid                               CH kWh                   6.47E+07                  1   1.3 own assumption
      diesel, burned in building machine                                 GLO MJ                   5.20E+06                  1     2 own assumption
      reinforcing steel, at plant                                        RER kg                   2.94E+07                  1   1.5 own assumption
      concrete, normal, at plant                                         CH m3                    1.53E+05                  1   1.3 estimation
      transport, lorry 28t                                               CH tkm                   1.47E+07                  1   2.1 standard
      transport, freight, rail                                           RER tkm                  1.85E+07                  1   2.1 standard
      disposal, inert waste, 5% water, to inert material landfill        CH kg                    1.13E+09                  1   1.5 own assumption
      Heat, waste                                                             MJ                  2.33E+08                  1   1.3 same as electricity



     Tab. 12.15 Zusammenstellung der Eingabedaten für die Endlagerung kurzlebiger, schwach- und mittelaktiver Abfälle
                              100
                    (SMA).




                                                                                                                                                           Deviation 95%
                                                                                                                           radioactive



                                                                                                                                             Uncertainty




                                                                                                                                                                                   Comment
                                                                                                                                                             Standard
                                                                                                       Location




                                                                                                                                                                                    General
                                                                                                                          waste, in final



                                                                                                                                               Type
                                                                                                                  Unit




                                              Name                                                                        repository for
                                                                                                                          nuclear waste
                                                                                                                              LLW
                                                                     Location                                                   CH
                                                                         Unit                                                   m3
      Volume occupied, final repository for low-active radioactive waste                                          m3         1.00E+00           1            1             certainty, definition
      electricity, medium voltage, at grid                                                            CH kWh                 3.77E+02           1            2             own assumption
      concrete, normal, at plant                                                                      CH m3                  8.00E-01           1            2             own assumption
      transport, lorry 28t                                                                            CH tkm                 5.00E+02           1           2.1            standard
      final repository for nuclear waste LLW                                                          CH unit                1.00E-05           1            1             certainty
      treatment, sewage, unpolluted, to wastewater treatment, class 3                                 CH m3                  2.80E-03           1            2             own assumption
      Heat, waste                                                                                         MJ                 1.36E+03           1            2             same as electricity




99
     Die Tabelle zeigt die in Version v1.01 der ecoinvent Datenbank enthaltenen Eingabedaten. Der Bilanzierung von „transport,
     lorry 28 t“ ist nicht korrekt, der richtige Wert beträgt 2.24E7 tkm/unit. Zusätzlich muss in der Kategorie „transport,
     lorry 32 t“ ein Wert von 2.64E7 tkm/unit bilanziert werden. Die korrekten Eingabedaten sind im Text beschrieben. Die
     Fehler werden in v.1.1 korrigiert.
100
               Die Tabelle zeigt die in Version v1.01 der ecoinvent Datenbank enthaltenen Eingabedaten. Die Bilanzierung von
     „transport, lorry 28 t“ und „treatment, sewage, unpolluted, to wastewater treatment, class 3“ ist nicht korrekt, die richtigen
     Werte betragen 5.38E2 tkm/m3 bzw. 2.3E-3 m3/m3. Die korrekten Eingabedaten sind im Text beschrieben. Die Fehler
     werden in v.1.1 korrigiert.




     ecoinvent-Bericht No. 6 - Teil VII                                                     - 316 -
                                                  Endlagerung der radioaktiven Abfälle


                                                                                                                                                                                                                      101
  Tab. 12.16 Zusammenstellung der Eingabedaten für die Endlagerung hoch und mittelaktiver Abfälle (BE/HAA/LMA).




                                                                                                           Uncertainty Type
                                                                                          radioactive




                                                                                                                              Deviation 95%
                                                                                         waste, in final




                                                                                                                                                                                         Comment
                                                                                                                                Standard
                                                                   Location




                                                                                                                                                                                          General
                                                                                         repository for




                                                                               Unit
                               Name
                                                                                         nuclear waste
                                                                                         SF, HLW, and
                                                                                              ILW
                                                          Location                            CH
                                                              Unit                            m3
      Volume occupied, final repository for radioactive waste           m3                 1.00E+00         1                   1                 certainty, definition
      electricity, medium voltage, at grid                         CH kWh                  6.65E+03         1                  1.3                own assumption on preliminary project data
      bentonite, at processing                                     CH kg                   1.45E+04         1                  1.3                own assumption on preliminary project data
      reinforcing steel, at plant                                  RER kg                  8.48E+01         1                  1.3                own assumption on preliminary project data
      concrete, normal, at plant                                   CH m3                   1.80E-01         1                  1.3                own assumption on preliminary project data
      cement mortar, at plant                                      CH kg                   4.73E+03         1                  1.3                own assumption on preliminary project data
      transport, lorry 28t                                         CH tkm                  9.88E+01         1                  2.1                standard
      transport, lorry 32t                                         RER tkm                 6.70E+03         1                  2.1                standard
      transport, freight, rail                                     RER tkm                 8.75E+03         1                  2.1                standard
      final repository for nuclear waste SF, HLW, and ILW          CH unit                 6.25E-05         1                   1                 certainty
      Heat, waste                                                       MJ                 2.39E+04         1                  1.3                same as electricity



  Tab. 12.17 Zusammenstellung der Eingabedaten für die Entsorgung des schwach radioaktiver Abfalls.




                                                                                                                                                             Standard Deviation




                                                                                                                                                                                                    General Comment
                                                                                                                                          Uncertainty Type
                                                              Location




                                                                                             low active




                                                                                                                                                                   95%
                                                                              Unit




                             Name
                                                                                         radioactive waste



                                           Location                                               CH
                                               Unit                                               m3
      Transformation, from pasture and meadow           m2                                         2                                       1                       2              own preliminary estimation
      Transformation, to industrial area                m2                                         2                                       1                       2              own preliminary estimation
      Transformation, from industrial area              m2                                         2                                       1                       2              own preliminary estimation
      Transformation, to unknown                        m2                                         2                                       1                       2              own preliminary estimation
      Occupation, industrial area                       m2a                                       140                                      1                       3              own preliminary estimation
      excavation, hydraulic digger                  RER m3                                         3                                       1                       2              own preliminary estimation
      excavation, skid-steer loader                 RER m3                                         3                                       1                       2              own preliminary estimation




101
            Die Tabelle zeigt die in Version v1.01 der ecoinvent Datenbank enthaltenen Eingabedaten. Die Bilanzierung von
  „bentonite, at processing“, „transport, lorry 28 t“, „transport, lorry 32 t“ und „transport, freight, rail“ ist nicht korrekt, die
  richtigen Werte betragen 8300 kg/m3, 1.07E2 tkm/m3, 4.22E3 tkm/m3 und 5.09E1 tkm/m3. Die korrekten Eingabedaten sind
  im Text beschrieben. Die Fehler werden in v.1.1 korrigiert.

  ecoinvent-Bericht No. 6 - Teil VII                                                 - 317 -
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 p.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
