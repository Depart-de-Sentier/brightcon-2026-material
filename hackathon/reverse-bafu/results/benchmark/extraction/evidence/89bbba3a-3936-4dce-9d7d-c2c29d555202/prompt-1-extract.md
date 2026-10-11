You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Radioactive waste, in interim storage conditioning` [CH], reference unit 1 m3, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~35 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: nuclear waste / unspecified
- includedProcesses: The module requires input of service from the final repository for low active level waste, i.e. the take over of the conditioned waste. The module describes the plasma torch incineration of low radioactive level waste, operating at very high temperature. The radioactive and non radioactive emissions to air and water expected from the design have been included. The electricity use, light oil consumption, material consumption, and related transport requirements are added. The values are normalized by the incinerated waste volume.
- technology: Information regards design in mid 1990s.
- generalComment: The module describes the plasma torch incineration of low radioactive level waste, operating at very high temperature. Five cubic meter of waste per year are assumed to be produced by incineration. The emissions from the design have been included. Therefore the oil consumption has been modeled with oil from regional storage and not with oil burned in furnace, to prevent double counting. Emissions to air expected by the designer are used, and the uncertainty estimated on the basis of the range with the maximum considered in desing. Particles are assumed to be below 2.5 micrometer due to the use of several HEPA filters. In 2003 the torch is not yet operating. Maximum designed emissions to water are given.;
UUID: 89bbba3a-3936-4dce-9d7d-c2c29d555202
- source cited in the metadata: Dones R. | 2009 | 2009 - Nuclear energy - Dones
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 m3):
- none

## Report excerpt

Source file: `report-p308-310.txt` (SHA-256 42387697e1dbc29265cd76489f54209319ddf9d9243141b0a60b3f1d9c4f3e05), pages 308-310 of `2009 - Nuclear energy - Dones.pdf`.

```
Zwischenlagerung der radioaktiven Abfälle


11.6             Zusammenstellung der Eingabedaten
In Tab. 11.7 bis Tab. 11.11 sind die Eingabedaten dieses Kapitels zusammengefasst.

Tab. 11.7        Zusammenstellung der Eingabedaten für die Infrastruktur des Zwischenlagers für schwach- und mittelaktive
                 (SMA) Abfälle.




                                                                                                                                                                                                 Standard Deviation




                                                                                                                                                                                                                                                         General Comment
                                                                                                                                                         Uncertainty Type
                                                                                                                            interim storage,




                                                                                   Location
                                                                                                                            nuclear waste to




                                                                                                                                                                                                       95%
                                                                                                                Unit
                              Name
                                                                                                                            dispose in final
                                                                                                                            repository LLW


                                                             Location                                                              CH
                                                                 Unit                                                              unit
Transformation, from pasture and meadow                                                                          m2             1.60E+04                   1                                       1.3                  own estimation from plan
Transformation, to industrial area                                                                               m2             1.60E+04                   1                                       1.3                  own estimation from plan
Transformation, from industrial area                                                                             m2             1.60E+04                   1                                       1.3                  own estimation from plan
Transformation, to unknown                                                                                       m2             1.60E+04                   1                                       1.3                  own estimation from plan
Occupation, industrial area                                                                                     m2a             9.76E+05                   1                                       1.5                  own estimation from plan
electricity, medium voltage, at grid                                               CH                           kWh             1.68E+05                   1                                        2                   own estimation from an ecoinvent module, lack of direct data
diesel, burned in building machine                                             GLO                              MJ              3.81E+06                   1                                        2                   own estimation from an ecoinvent module, lack of direct data
steel, low-alloyed, at plant                                                  RER                                kg             2.25E+05                   1                                        2                   own estimation, lack of data
reinforcing steel, at plant                                                   RER                                kg             1.00E+06                   1                                       1.5                  own estimation, lack of data
concrete, normal, at plant                                                    CH                                m3              8.30E+03                   1                                       1.5                  own estimation, lack of data
transport, lorry 28t                                                          CH                                tkm             4.23E+04                   1                                       2.1                  standard
transport, freight, rail                                                      RER                               tkm             7.35E+05                   1                                       2.1                  standard
disposal, building, reinforced concrete, to final disposal                         CH                           kg              2.10E+07                   1                                       1.7                  own estimation from total reinforced concrete
Heat, waste                                                                                                     MJ              5.15E+05                   1                                        2                   same as for electricity



Tab. 11.8        Zusammenstellung der Eingabedaten für die Infrastruktur des Zwischenlagers für hoch- und mittelaktive
                 (BE/HAA/LMA) Abfälle.
                                                                                                                                                                                               Standard Deviation




                                                                                                                                                                                                                                                       General Comment
                                                                                                                                                       Uncertainty Type




                                                                                                                       interim storage, nuclear
                                                                        Location




                                                                                                                       waste to dispose in final
                                                                                                                                                                                                     95%
                                                                                                         Unit




                             Name
                                                                                                                       repository SF, HLW, and
                                                                                                                                 ILW


                                                       Location                                                                  CH
                                                           Unit                                                                  unit
Transformation, from pasture and meadow                                                          m2                           1.60E+04                                    1                          1.3 own estimation from plan
Transformation, to industrial area                                                               m2                           1.60E+04                                    1                          1.3 own estimation from plan
Transformation, from industrial area                                                             m2                           1.60E+04                                    1                          1.3 own estimation from plan
Transformation, to unknown                                                                       m2                           1.60E+04                                    1                          1.3 own estimation from plan
Occupation, industrial area                                                                     m2a                           9.76E+05                                    1                          1.5 own estimation from plan
electricity, medium voltage, at grid                                    CH                      kWh                           1.68E+05                                    1                            2 own estimation from an ecoinvent module, lack of direct data
diesel, burned in building machine                                      GLO                         MJ                        3.81E+06                                    1                            2 own estimation from an ecoinvent module, lack of direct data
steel, low-alloyed, at plant                                            RER                        kg                         2.25E+05                                    1                            2 own estimation, lack of data
reinforcing steel, at plant                                             RER                        kg                         1.00E+06                                    1                          1.5 own estimation, lack of data
concrete, normal, at plant                                              CH                        m3                          8.30E+03                                    1                          1.5 own estimation, lack of data
transport, lorry 28t                                                    CH                        tkm                         4.23E+04                                    1                          2.1 standard
transport, freight, rail                                                RER                       tkm                         7.35E+05                                    1                          2.1 standard
disposal, building, reinforced concrete, to final disposal              CH                           kg                       2.10E+07                                    1                          1.7 own estimation from total reinforced concrete
Heat, waste                                                                                         MJ                        5.15E+05                                    1                            2 same as for electricity



Tab. 11.9        Zusammenstellung der Eingabedaten für den Betrieb des Zwischenlagers für schwach- und mittelaktive
                 (SMA) Abfälle.
                                                                                                                                                                                                        Standard Deviation




                                                                                                                                                                                                                                                                General Comment
                                                                                                                                                                            Uncertainty Type
                                                                                              Location




                                                                                                                            radioactive waste, in
                                                                                                                                                                                                              95%
                                                                                                                 Unit




                                 Name                                                                                     interim storage, for final
                                                                                                                               repository LLW


                                                                  Location                                                           CH
                                                                      Unit                                                           m3
electricity, medium voltage, at grid                                                     CH kWh                                   8.89E+03                                   1                            1.5                own calculation
transport, lorry 28t                                                                     CH tkm                                   3.80E+01                                   1                            2.1                standard
transport, freight, rail                                                                 RER tkm                                  3.40E+03                                   1                            2.1                standard
interim storage, nuclear waste to dispose in final repository LLW                        CH unit                                  3.53E-05                                   1                            1.5                estimation based on somewhat outdated waste flow amount
radioactive waste, in final repository for nuclear waste LLW                             CH m3                                    1.00E+00                                   1                             1                 all waste in will move out to final repository
Heat, waste                                                                                   MJ                                  3.20E+04                                   1                            1.5                same as for electricity




ecoinvent-Bericht No. 6 - Teil VII                                                                                           - 282 -
                                                 Zwischenlagerung der radioaktiven Abfälle


Tab. 11.10 Zusammenstellung der Eingabedaten für für den Betrieb des Zwischenlagers für hoch- und mittelaktive
               (BE/HAA/LMA) Abfälle.




                                                                                                                                                                           Standard Deviation




                                                                                                                                                                                                                        General Comment
                                                                                                                                                     Uncertainty Type
                                                                                                         radioactive waste, in




                                                                     Location
                                                                                                          interim storage, for




                                                                                                                                                                                 95%
                                                                                           Unit
                             Name
                                                                                                          final repository SF,
                                                                                                             HLW, and ILW


                                                        Location                                                 CH
                                                            Unit                                                 m3
transport, freight, rail                                            RER tkm                                   3.20E+04                                1                      2.1 standard
interim storage, nuclear waste to dispose in final                                                                                                                               estimation based on somewhat outdated
repository SF, HLW, and ILW                                         CH             unit                        1.75E-04                               1                      1.5 waste flow amount
radioactive waste, in final repository for nuclear waste SF,                                                                                                                     all waste in will move out to final
HLW, and ILW                                                        CH              m3                        1.00E+00                                1                       1 repository



Tab. 11.11 Zusammenstellung der Eingabedaten für die Konditionierung radioaktiver Abfälle im Zwischenlager.




                                                                                                                                                      Standard Deviation




                                                                                                                                                                                                      General Comment
                                                                                                                                  Uncertainty Type
                                                                                Location




                                                                                                          radioactive waste, in




                                                                                                                                                            95%
                                                                                                  Unit



                                 Name                                                                        interim storage
                                                                                                               conditioning


                                                                Location                                          CH
                                                                    Unit                                          m3
electricity, medium voltage, at grid                                            CH kWh                         5.20E+05            1                       2               own calculation after key data on power.
light fuel oil, at regional storage                                             CH kg                          3.60E+03            1                       2               own calculation.
ammonia, liquid, at regional storehouse                                         RER kg                         1.80E+02            1                      1.3              based on flowsheet design estimation
sulphuric acid, liquid, at plant                                                RER kg                         1.80E+01            1                      1.3              based on flowsheet design estimation
transport, lorry 28t                                                            CH tkm                         1.53E+03            1                      2.1              standard
transport, freight, rail                                                        RER tkm                        1.19E+02            1                      2.1              standard
radioactive waste, in final repository for nuclear waste LLW                    CH m3                          1.00E+00            1                       1               all waste in will move out to final repository.
Heat, waste                                                                          MJ                        2.50E+06            1                       2               same as for electricity
Ammonia                                                                              kg                        1.44E+00            1                      1.2              expected emissions used, range with guaranteed value
Cadmium                                                                              kg                        5.40E-06            1                      20               expected emissions used, range with guaranteed value
Carbon dioxide, fossil                                                               kg                        1.14E+04            1                      1.2              own estimation of uncertainty
Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin                             kg                        3.60E-11            1                       5               own estimation of uncertainty
Hydrogen chloride                                                                    kg                        8.10E-01            1                       4               expected emissions used, range with guaranteed value
Lead                                                                                 kg                        2.20E-04            1                      20               expected emissions used, range with guaranteed value
Nitrogen oxides                                                                      kg                        2.16E+01            1                      1.3              expected emissions used, range with guaranteed value
NMVOC, non-methane volatile organic compounds, unspecified origin                    kg                        3.60E-03            1                       5               own estimation of uncertainty
Particulates, < 2.5 um                                                               kg                        1.80E-03            1                       5               own estimation of uncertainty
Sulfur dioxide                                                                       kg                        5.04E+00            1                       2               expected emissions used, range with guaranteed value
Carbon-14                                                                           kBq                        1.66E+06            1                       2               own estimation of uncertainty
Hydrogen-3, Tritium                                                                 kBq                        3.04E+06            1                       2               own estimation of uncertainty
Aluminum                                                                             kg                        2.40E-01            1                       5               own estimation of uncertainty, guaranted releases given
Cadmium, ion                                                                         kg                        2.40E-03            1                       5               own estimation of uncertainty, guaranted releases given
Chlorinated solvents, unspecified                                                    kg                        2.40E-03            1                       5               own estimation of uncertainty, guaranted releases given
Chromium VI                                                                          kg                        2.40E-03            1                       5               own estimation of uncertainty, guaranted releases given
Chromium, ion                                                                        kg                        4.80E-02            1                       5               own estimation of uncertainty, guaranted releases given
Cobalt                                                                               kg                        1.20E-02            1                       5               own estimation of uncertainty, guaranted releases given
Copper, ion                                                                          kg                        1.20E-02            1                       5               own estimation of uncertainty, guaranted releases given
Hydrocarbons, unspecified                                                            kg                        2.40E-01            1                       5               own estimation of uncertainty, guaranted releases given
Iron, ion                                                                            kg                        4.80E-02            1                       5               own estimation of uncertainty, guaranted releases given
Lead                                                                                 kg                        1.20E-02            1                       5               own estimation of uncertainty, guaranted releases given
Mercury                                                                              kg                        2.40E-04            1                       5               own estimation of uncertainty, guaranted releases given
Nickel, ion                                                                          kg                        4.80E-02            1                       5               own estimation of uncertainty, guaranted releases given
Radioactive species, Nuclides, unspecified                                          kBq                        6.00E+02            1                       5               own estimation of uncertainty, guaranted releases given
Zinc, ion                                                                            kg                        4.80E-02            1                       5               own estimation of uncertainty, guaranted releases given
emissions to "air, low population density"
emissions to "water, river"




ecoinvent-Bericht No. 6 - Teil VII                                                                 - 283 -
                                     Zwischenlagerung der radioaktiven Abfälle


11.7        Datenqualität
Die im vorliegenden Bericht dargestellten Daten basieren auf nicht detaillierten Vorprojektsangaben.
Insbesondere Materialbedarfswerte könnten mit Projektunterlagen quantifiziert werden. Einige
Energiebedarfs- und Emissionsdaten während des Betriebs wurden auch aus der Planung extrahiert,
wobei sie als genügend zuverlässig angesehen werden sollten.
Obwohl mit Ausnahme des Plasmaverbrennungsofens die Anlage in Betrieb ist, wurde dieses Kapitel
der vorliegenden Studie nicht aktualisiert. Eine Überarbeitung stand angesichts der relativ geringen
Bedeutung der Zwischenlagerung bezüglich der gesamten Umwelteinwirkungen der nuklearen
Energiekette nicht im Vordergrund. Die Abschätzung der Unsicherheitsfaktoren berücksichtigen diese
Tatsache. Eine Aktualisierung des Inventars zur Erfassung der momentanen Verhältnisse könnte
durchgeführt werden, falls Ressourcen bereitgestellt würden. Es sind jedoch keine bedeutenden
Veränderungen der Grössenordnungen der Umwelteinwirkungen des Zwischenlagers zu erwarten.
In erster Näherung können die Daten für das schweizerische Zwischenlager-Projekt als repräsentativ
für europäischen Verhältnisse betrachtet werden. Ein Vergleich mit ähnlichen Projekten in anderen
Ländern könnten zur Berücksichtigung anderer Datensätze mit der Einführung entsprechender
mittlerer Werte führen.




ecoinvent-Bericht No. 6 - Teil VII                     - 284 -
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 m3.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
