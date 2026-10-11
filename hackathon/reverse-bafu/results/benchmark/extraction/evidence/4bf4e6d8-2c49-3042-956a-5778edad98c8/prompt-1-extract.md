You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Tempering, flat glass` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~5 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: glass / unspecified
- includedProcesses: Gate to gate inventory for the process not including infrastructure and emissions.
- technology: The glass sheet is heated to a temperature just below its softening point (about 640°C) and then immediately cooled by special jets of cold-air. These harden the surface of the glass, giving the inside more time to cool. This allows the external layer to crystallize into a wider lattice while the inside solidifies with greater compression than in the crystal lattice.
- generalComment: Basic assumption of unit process raw data for the tempering of glass. Tempering or toughening is a special process of solidification of a glass sheet in order to make it particularly resistant to breakages. The process may be physical (thermal) or chemical. Here a thermal tempering is assumed. The result is a sheet of glass which is two or three times stronger than untempered glass.;
Synonyms: toughening; 
UUID: 4bf4e6d8-2c49-3042-956a-5778edad98c8
- source cited in the metadata: Kellenberger D. | 2007 | 2007 - LCI building products - Kellenberger
- time period: 2000-01-2000-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- none

## Report excerpt

Source file: `report-p371-372.txt` (SHA-256 4660b6139f9ef36cfea15f93fbc94d548b572600d6b0c9b9a9ef071ed386bc20), pages 371-372 of `2007 - LCI building products - Kellenberger.pdf`.

```
borosilicate glasses. The production of borosilicate glass tubes form this type of glass is investigated in
    chapter 4.6 on page 15.


    4.3        Production of Structured Glass
    Structured glass can be produced in the same way as casting (or rolled) glass. The structuring is not a
    separate process, but a modification in the casting glass process. Casting glass is formed by a
    continuous double-roll process. Molten glass mass at about 1000°C is squeezed between water cooled
    steel rollers to produce a ribbon with controlled thickness and surface pattern (IPPC 2000). Instead of
    using a flat roller after the casting a structured roller is used. The further processing of structured glass
    is the same as for casting glass. The glass is cooled and than cut to its final format. A schematic
    representation of the rolled glass process is shown in Fig. 4.1.




    Fig. 4.1   The process for the production of casting glass (IPPC 2000) which is also used for structured glass


    Unit process data were not available. The composition of raw materials is very similar to normal flat
    glass. Environmental impacts can be considered to be a little bit lower than these for flat (floated)
    glass because the expenditures for the floating process are higher (e.g. use of a zinc bath, gas
    atmosphere). 3 The energy use for casting glass is lower than for float glass (Starzner & Wurmer-Weiß
    2000), but most of the energy use is due to the melting process which is about the same for both
    products (IPPC 2000). It is recommended to use the unit process raw data for “flat glass, uncoated, at
    plant” to approximate the environmental impacts due to the use of structured glasses.


    4.4        Tempering or Toughening
    Tempering or toughening is a special process of solidification of a glass sheet in order to make it more
    resistant to breakages. This is especially important for solar collectors which face high thermal
    tensions. The process may be physical (thermal) or chemical. In the physical process, the glass sheet is



3
    Personal communication with Mr. Braun, Saint-Gobain Glas, FR, 6.2002.

    ecoinvent-report No. 7                                  - 10 -
heated to a temperature just below its softening point (about 640°C) and then immediately cooled by
special jets of cold-air. This hardens the surface of the glass immediately and gives the inside more
time to cool. Thus a tension is build up in the glass. The result is a sheet of glass which is two or three
times stronger than un-tempered glass and which, upon breakage, shatters into tiny pieces with blunt
edges (the most common application is automotive glass).
The chemical process is based on the so-called ion-stuffing technique. Different chemical elements in
the glass structure possess different ionic radii and therefore different densities. If glass containing
sodium is cooled slowly in a salt bath of molten potassium, the sodium ions will migrate from the
glass to the salt, while the potassium ions will move to the surface of the glass. There they create also
a tension in the glass, due to their wider radius, and therefore stronger surface layer (of more than 0.1
mm). Glass sheets which have been chemically tempered are stronger than those which have not
undergone any tempering process (glassOnline 2002).
The inventory for tempering describes the thermal process. It includes the transport to the tempering
plant, the energy use for heating and cooling and losses, but not the throughput of raw glass. The
process is energy intensive using gas or electricity mainly for the heating, but also for cooling. Unit
process data especially for the energy use were not available. The estimation of unit process raw data
and data quality indicators for tempering of glass in Tab. 4.3 is based on the assumption that the
hardening uses about 20% of the energy used for the initial melting (5.5 to 8.0 MJ/kg according to
(IPPC 2000)). About 10-15% of the incoming glass is normally not used due to the wastes from
cutting to the final size. The production loss before the tempering is estimated to be 12%. This loss is
accounted here with the glass production and its transport to the factory for tempering. Furthermore a
recycling of these wastes in the glass production process can be assumed. Thus they are not regarded
as wastes. Data for the infrastructure were not available. It has to be noted that the demand of flat glass
has to be considered in inventory additionally to the process of tempering. The inventory is based
solely on assumptions and thus the data quality is poor.

Tab. 4.3      Unit process raw data and data quality indicators for the tempering of glass
                                                                                Infrastructu




                                                                                                                        Uncertaint

                                                                                                                        Deviation
                                                                                                                        Standard
                                                                     Location




                                                                                                      tempering, flat
                                                                                                                          95%




                                        Name                                                   Unit                                  GeneralComment
                                                                                                          glass

                                        Location                                                           RER
                                InfrastructureProcess                                                        0
                                          Unit                                                              kg
product      tempering, flat glass                                    RER        0             kg        1.00E+0
technosphere natural gas, burned in industrial furnace low-NOx >100kW RER        0             MJ        1.33E+0        1   1.50     (5,na,1,1,1,na); Estimation 20% of melting energy
             flat glass, uncoated, at plant                           RER        0             kg        1.20E-1        1   1.12     (3,3,1,1,1,na); Estimation 12% glass losses
                                                                                                                                     (4,5,na,na,na,na); Standard distance 100km for
             transport, lorry 32t                                   RER           0            tkm       1.12E-1        1   2.09
                                                                                                                                     glass throughput including losses (1.2kg)
                                                                                                                                     (4,5,na,na,na,na); Standard distance 200km for
             transport, freight, rail                               RER          0             tkm       2.24E-1        1   2.09
                                                                                                                                     glass throughput including losses (1.2kg)




4.5           Anti-reflection for Solar Glass
4.5.1         Etching with hydrogen fluoride (HF)
Etching with hydrogen fluoride is used in order to produce milk glass used i.e. bathrooms. One
problem of glass anti-reflected by etching is the ecological impact caused by the etching agent
hydrofluoric acid (Glässer 2000). Detailed and reliable quantitative information for this process were
not available.


4.5.2         Etching with fluosilicic acid (H2(SiF6))
The manufacturer Sunarc, DK uses an acid-process for its AR-solar glass. This glass is for example
used by Wagner-Solartechnik, DE. The antireflection microstructure is impressed on the solar glass by
an automatic etching procedure. Cleaning, etching and clarification are the necessary process stages. A


ecoinvent-report No. 7                                                          - 11 -
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 kg.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
