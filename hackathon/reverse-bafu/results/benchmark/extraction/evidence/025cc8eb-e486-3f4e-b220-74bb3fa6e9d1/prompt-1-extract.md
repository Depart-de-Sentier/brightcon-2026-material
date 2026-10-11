You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Door, inner, room, glass-wood, steel frame, at plant` [CH], reference unit 1 m2, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~6 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: building components / doors
- includedProcesses: Included are the materials used in an inner glass-wood door and steel frame. The door leaf and frame are opaquely painted. Production losses, work materials, packaging materials, energy demand and the transport of the materials are also included.
- technology: Industry data.
- generalComment: The measures of the visible door leaf are 0.9m x 2m. The size of the glass insert for the door leaf is 0.74m2. 1m2 of visible glass-wood door (incl. steel frame) weighs 43.9kg. The door and frame are opaquely painted. The bill of materials is based on data from door manufactures.\nTechnology: Industry data.\nTime period: Time of publications.\nVersion: 1\nEnergy values: Undefined\nLocal category: Bauteile\nLocal subcategory: Türen\nUVEK 2022 source file:634_EcoSpold_Türen_v1.5_UVEK2021_v0.2_R_corr._X-Tür_total.xml\n\n
UUID: 025cc8eb-e486-3f4e-b220-74bb3fa6e9d1
- source cited in the metadata: Ramseier L. | 2020 | 2020 - LCA wooden windows and doors - Ramseier
- time period: 2018-01-2019-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 m2):
- Energy, gross calorific value, in biomass, resource correction: -57.17 megajoule (resources biotic)
- Iron: -7.601 kilogram (Resources Resources from ground Non-renewable element resources from ground)

## Report excerpt

Source file: `report-p31-34.txt` (SHA-256 87b3eb83cb0c0b3262c7df53498d11c0af9a775f4807c20ac09fee8e0ebd40c7), pages 31-34 of `2020 - LCA wooden windows and doors - Ramseier.pdf`.

```
31
                                                                                                                                                                                                    Ökobilanz von Holztüren und Holzfenstern




                Tabelle 16: Sachbilanzdaten für die Herstellung von 1 m2 Türflügel ab Werk in der Schweiz




                                                                                                                                                                                                                           Standard Deviation 95%
                                                                                           Infrastructure Process




                                                                                                                                                                                                       Uncertainty Type
                                                                                                                                             door leaf,     door leaf,                   door leaf,




                                                                                Location
                                                                                                                               door leaf,                                 door leaf,
                                                                                                                                            functional,   room, inner,                  outer, wood-




                                                                                                                     Unit
                                              Name                                                                           room, inner,                                outer, wood,                                                               General Comment
                                                                                                                                           inner, wood,   wood-glass,                     glass, at
                                                                                                                            wood, at plant                                 at plant
                                                                                                                                              at plant       at plant                       plant




                                             Location                                                                            CH            CH             CH             CH             CH

                                     Infrastructure Process                                                                       0             0              0              0              0

                                               Unit                                                                              m2            m2             m2             m2             m2

product       door leaf, room, inner, wood, at plant                            CH            0                     m2            1             0              0              0              0
              door leaf, functional, inner, wood, at plant                      CH            0                     m2            0             1              0              0              0
              door leaf, room, inner, wood-glass, at plant                      CH            0                     m2            0             0              1              0              0
              door leaf, outer, wood, at plant                                  CH            0                     m2            0             0              0              1              0
              door leaf, outer, wood-glass, at plant                            CH            0                     m2            0             0              0              0              1
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); particle board light; Average of
technosphere particleboard, average glue mix, uncoated, at plant                RER           0                     m3         2.06E-2          0           2.29E-3           0              0           1                1.16
                                                                                                                                                                                                                               data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); particle board; Average of data
              particleboard, average glue mix, uncoated, at plant               RER           0                     m3            0          2.71E-2        1.32E-2        1.20E-2        9.53E-3        1                1.16
                                                                                                                                                                                                                               from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); fibreboard, hard; Average of data
              fibreboard, hard, at plant                                        RER           0                     m3         6.65E-3       1.04E-2        6.61E-3        1.26E-2        8.06E-3        1                1.16
                                                                                                                                                                                                                               from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); lath CH; Average of data from
              sawnwood, lath, softwood, dried (u=10%), planed, at sawmill       CH            0                     m3         3.76E-3       6.52E-3        3.86E-3        7.28E-3        9.67E-3        1                1.16
                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); lath RER; Average of data from
              sawnwood, lath, softwood, dried (u=10%), planed, at sawmill       RER           0                     m3         1.26E-3       2.18E-3        1.29E-3        2.43E-3        3.23E-3        1                1.16
                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); fibreboard; Average of data from
              medium density fibreboard, uncoated, at plant                     RER           0                     m3            0          3.26E-3           0           3.85E-3        3.76E-3        1                1.16
                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); laminated veneer timber CH;
              glued laminated timber, outdoor use, at plant                     CH            0                     m3            0          1.25E-3           0           1.04E-3           0           1                1.16
                                                                                                                                                                                                                               Average of data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); laminated veneer timber RER;
              glued laminated timber, outdoor use, at plant                     RER           0                     m3            0          4.17E-4           0           3.44E-4           0           1                1.16
                                                                                                                                                                                                                               Average of data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); fibreboard; Average of data from
              medium density fibreboard, uncoated, at plant                     RER           0                     m3            0             0              0           2.18E-3           0           1                1.16
                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); polyurethane foam; Average of
              polyurethane, rigid foam, market mix, at regional storage         CH            0                     kg            0             0              0           3.81E-1        2.97E-1        1                1.16
                                                                                                                                                                                                                               data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); aluminium sheet; Average of data
              aluminium sheet, uncoated                                         CH            0                     kg            0             0              0          2.63E+0        1.74E+0         1                1.16
                                                                                                                                                                                                                               from manufacturers
              glazing, double (2-IV), U=1.1 W/m2K, 4 Float / 16 Ar / VSG 2x4,                                                                                                                                                  (3,3,1,1,1,4,BU:1.05); Glazing; Average of data from
                                                                                 CH           0                     m2            0             0           4.04E-1           0              0           1                1.16
              0.76 PVB, Low E 1.1, at plant                                                                                                                                                                                    manufacturers
              glazing, triple (3-IV), U=0.6 W/m2K, 4 Low E 1.1 Float / 14 Ar / 4                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Glazing; Average of data from
                                                                                 CH           0                     m2            0             0              0              0           3.70E-1        1                1.16
              Float / 14 Ar / VSG 2x4, 0.76 PVB, Low E 1.1 Float, at plant                                                                                                                                                     manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); steel for fittings; Average of data
              steel sheet, zinc-coated, recycling share 2000 (37% Rec.)         CH            0                     kg         5.00E-1       9.00E-1        5.00E-1        9.00E-1        9.00E-1        1                1.16
                                                                                                                                                                                                                               from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); steel screws for fittings; Average of
              steel, low-alloyed, at plant                                      RER           0                     kg         1.85E-2       1.67E-2        1.85E-2        1.67E-2        1.67E-2        1                1.16
                                                                                                                                                                                                                               data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); processing of steel screws;
              steel product manufacturing, average metal working                RER           0                     kg         1.85E-2       1.67E-2        1.85E-2        1.67E-2        1.67E-2        1                1.16
                                                                                                                                                                                                                               Average of data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Chromium steel for fittings;
              chromium steel sheet 18, recycling share 2000 (37% Rec.)          CH            0                     kg         2.43E-1       3.18E-1        2.43E-1        3.18E-1        3.18E-1        1                1.16
                                                                                                                                                                                                                               Average of data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); silicon; Average of data from
              silicone product, at plant                                        RER           0                     kg         7.56E-2       1.36E-1        1.01E-1        1.39E-1        1.85E-1        1                1.16
                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); white glue; Average of data from
              vinyl acetate, at plant                                           RER           0                     kg         1.69E-1       4.29E-1        1.49E-1        4.48E-1        5.17E-1        1                1.16
                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); urea-based glue; Average of data
              urea formaldehyde resin, at plant                                 RER           0                     kg         4.55E-2          0           6.06E-2           0              0           1                1.16
                                                                                                                                                                                                                               from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); disposal production waste particle
              disposal, particle board, outdoor application                     CH            0                     kg            0             0              0           7.25E-1        6.21E-1        1                1.16
                                                                                                                                                                                                                               board; Average of data from manufacturers
              disposal, particle board, indoor application                      CH            0                     kg         8.08E-1       1.31E+0        8.57E-1                                      1                1.16 (3,3,1,1,1,4,BU:1.05); disposal production waste particle
              disposal, fibreboard, hard                                        CH            0                     kg         5.75E-1       9.00E-1        5.77E-1       1.07E+0         7.06E-1        1                1.16 (3,3,1,1,1,4,BU:1.05); disposal production waste
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); disposal production waste
              disposal, fibreboard, medium density (MDF)                        CH            0                     kg            0          2.24E-1           0           3.51E-1        2.57E-1        1                1.16 fibreboard medium density; Average of data from
                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); disposal production waste
              disposal, glue-laminated timber                                   CH            0                     kg            0          5.75E-2           0           4.75E-2           0           1                1.16 laminated veneer timber; Average of data from
                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); disposal production waste
              disposal, building, polyurethane foam, to final disposal          CH            0                     kg            0             0              0           2.56E-2           0           1                1.16 polyurethande foam; Average of data from
                                                                                                                                                                                                                               manufacturers
              disposal, rubber, unspecified, 0% water, to municipal                                                                                                                                                            (3,3,1,1,1,4,BU:1.05); disposal production waste silicon;
                                                                                CH            0                     kg         7.49E-4       1.35E-3        9.98E-4        1.38E-3        1.83E-3        1                1.16
              incineration                                                                                                                                                                                                     Average of data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); disposal production waste withe
              disposal, polyurethane, 0.2% water, to municipal incineration     CH            0                     kg         1.14E-2       3.01E-2        1.20E-2        3.06E-2        3.75E-2        1                1.16
                                                                                                                                                                                                                               glue; Average of data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); disposal production waste urea-
              disposal, polyurethane, 0.2% water, to municipal incineration     CH            0                     kg         4.50E-4          0           6.00E-4           0              0           1                1.16
                                                                                                                                                                                                                               based glue; Average of data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); electricty for production; Average of
              electricity, medium voltage, at grid                              CH            0                     kWh       1.01E+1        1.01E+1       1.01E+1        1.01E+1        1.01E+1         1                1.16
                                                                                                                                                                                                                               data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); production waste from laths;
              wood chips, from industry, softwood, burned in furnace 300kW CH                 0                     MJ        6.47E+1        6.47E+1       6.47E+1        6.47E+1        6.47E+1         1                1.16
                                                                                                                                                                                                                               Average of data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); cleaning agent; Average of data
              chemicals organic, at plant                                       GLO           0                     kg         2.09E-3       2.09E-3        2.09E-3        2.09E-3        2.09E-3        1                1.16
                                                                                                                                                                                                                               from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); water; Average of data from
              tap water, at user                                                CH            0                     kg         1.61E-2       1.61E-2        1.61E-2        1.61E-2        1.61E-2        1                1.16
                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); lubricating oil; Average of data
              lubricating oil, at plant                                         RER           0                     kg         4.51E-3       4.51E-3        4.51E-3        4.51E-3        4.51E-3        1                1.16
                                                                                                                                                                                                                               from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); chemicals; Average of data from
              chemicals organic, at plant                                       GLO           0                     kg         2.67E-4       2.67E-4        2.67E-4        2.67E-4        2.67E-4        1                1.16
                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); packaging cardboard; Average of
              packaging, corrugated board, mixed fibre, single wall, at plant   CH            0                     kg         1.31E-2       1.31E-2        1.31E-2        1.31E-2        1.31E-2        1                1.16
                                                                                                                                                                                                                               data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); packaging plastics; Average of
              packaging film, LDPE, at plant                                    RER           0                     kg         3.75E-2       3.75E-2        3.75E-2        3.75E-2        3.75E-2        1                1.16
                                                                                                                                                                                                                               data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); packaging pallet; Average of data
              EUR-flat pallet                                                   RER           0                     unit       1.04E-3       1.04E-3        1.04E-3        1.04E-3        1.04E-3        1                1.16
                                                                                                                                                                                                                               from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); packaging paper; Average of data
              kraft paper, bleached, at plant                                   RER           0                     kg            0          2.50E-3           0           2.50E-3        2.50E-3        1                1.16
                                                                                                                                                                                                                               from manufacturers
              disposal, plastics, mixture, 15.3% water, to municipal                                                                                                                                                           (3,3,1,1,1,4,BU:1.05); disposal packaging plastics;
                                                                                CH            0                     kg         3.75E-2       3.75E-2        3.75E-2        3.75E-2        3.75E-2        1                1.16
              incineration                                                                                                                                                                                                     Average of data from manufacturers
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:2); Transportation to production site;
              transport, freight, lorry, fleet average                          CH            0                     tkm       1.28E+1        1.52E+1       9.27E+0        1.44E+1        1.14E+1         1                2.03 Average of data from manufacturers or Frischknecht et
                                                                                                                                                                                                                               al. 2007
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:2); Transportation to production site ;
              transport, freight, rail                                          CH            0                     tkm        6.12E-1       1.04E+0       8.39E+0        1.81E+0        1.11E+1         1                2.03 Average of data from manufacturers or Frischknecht et
                                                                                                                                                                                                                               al. 2007
                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Transport of waste to municipal
              transport, municipal waste collection, lorry 21t                  CH            0                     tkm        3.75E-4       3.75E-4        3.75E-4        3.75E-4        3.75E-4        1                1.16 incineration; Average of data from manufacturers or
                                                                                                                                                                                                                               Frischknecht et al. 2007
 32
 Ökobilanz von Holztüren und Holzfenstern




              Für die Herstellung der Türrahmen werden von den Türherstellern verschiedene Kanteltypen
              eingesetzt. Deshalb wurde für die Modellierung der Holztürrahmen die Durchschnittskantel (siehe
              Unterkapitel 4.2) verwendet. Da keine Angaben über die Herkunft der Kanteln verfügbar waren,
              wurde angenommen, dass die Anteile von Kanteln aus der Schweiz und Europa identisch sind wie
              bei den Fensterherstellern.

              Aufgrund geringer Datenverfügbarkeit wurde für die Berechnung des Durchschnitts der
              Stahlmenge in der Stahlzarge ein Literaturwert aus Werner et al. (1997) hinzugezogen.

              Für die Transportdistanzen der Kanteln aus der Schweiz wurden die Angaben der Türhersteller
              verwendet und für die Kanteln aus Europa die Angaben der Fensterhersteller. Für die Transport-
              distanz der Stahlzarge wurden Standarddistanzen gemäss Frischknecht et al. (2007) verwendet.

              Die Sachbilanzdaten für die Herstellung der Türrahmen von Innen- und Aussentüren pro m2
              Flügelansichtsfläche sind in Tabelle 17 dargestellt.

              Tabelle 17: Sachbilanzdaten für die Herstellung von Türrahmen bezogen auf 1 m2 Flügelansichtsfläche ab Werk in der

              Schweiz




                                                                                                                                                                                    Standard Deviation 95%
                                                                                  Infrastructure Process




                                                                                                                                                                Uncertainty Type
                                                                       Location




                                                                                                                   door frame,   door frame,     door frame,
                                                                                                           Unit




                                           Name                                                                   inner, wood,   inner, steel,   outer, wood,                                                General Comment
                                                                                                                     at plant      at plant        at plant




                                         Location                                                                     CH             CH              CH

                                Infrastructure Process                                                                0              0               0
                                           Unit                                                                       m2             m2              m2
product       door frame, inner, wood, at plant                        CH            0                     m2          1              0               0
              door frame, inner, steel, at plant                       CH            0                     m2          0              1               0
              door frame, outer, wood, at plant                        CH            0                     m2          0              0               1
                                                                                                                                                                                                             (3,3,1,1,1,4,BU:1.05); Scantling from Switzerland; Average of
technosphere Scantling, softwood, average, at plant                    CH            0                     m3       2.69E-3           0            2.88E-3        1                1.16
                                                                                                                                                                                                             data from manufacturers
                                                                                                                                                                                        (3,3,1,1,1,4,BU:1.05); Scantling from Europe; Average of data
              Scantling, softwood, average, at plant                   RER           0                     m3       1.70E-2           0            1.82E-2        1                1.16
                                                                                                                                                                                        from manufacturers
                                                                                                                                                                                        (3,3,1,1,1,4,BU:1.05); Steel frame; Average of data from
              steel sheet, uncoated, recycling share 2000 (37% Rec.)   CH            0                     kg          0          1.21E+1             0           1                1.16
                                                                                                                                                                                        manufacturers and Werner et al. 1997
                                                                                                                                                                                        (3,3,1,1,1,4,BU:1.05); Processing of steel frame; Average of
              steel product manufacturing, average metal working       RER           0                     kg          0          1.21E+1             0           1                1.16
                                                                                                                                                                                        data from manufacturers and Werner et al. 1997

              disposal, wood untreated, 20% water, to municipal                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Disposal of processing waste scantling
                                                                       CH            0                     kg      1.20E+0            0           1.16E+0         1                1.16
              incineration                                                                                                                                                                                   wood; Average of data from manufacturers

              disposal, polyurethane, 0.2% water, to municipal                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal of processing waste scantling
                                                                       CH            0                     kg       1.62E-2           0            1.57E-2        1                1.16
              incineration                                                                                                                                                                                   glue; Average of data from manufacturers
                                                                                                                                                                                                             (3,3,1,1,1,4,BU:2); Transportation to production site; Average
              transport, freight, lorry, fleet average                 CH            0                     tkm     9.04E+0         6.03E-1        9.66E+0         1                2.03
                                                                                                                                                                                                             of data from manufacturers or Frischknecht et al. 2007
                                                                                                                                                                                                             (3,3,1,1,1,4,BU:2); Transportation to production site; Average
              transport, freight, rail                                 CH            0                     tkm         0          7.24E+0             0           1                2.03
                                                                                                                                                                                                             of data from manufacturers or Frischknecht et al. 2007
                                                                                                                                                                                        (3,3,1,1,1,4,BU:1.05); Transport of production waste to
              transport, municipal waste collection, lorry 21t         CH            0                     tkm      1.21E-2           0            1.18E-2        1                1.16 municipal incineration; Average of data from manufacturers or
                                                                                                                                                                                        Frischknecht et al. 2007




              Die Oberflächen der Innen- und Aussentüren sind naturbehandelt/transparent lackiert oder
              deckend gestrichen. Dafür verwenden die Hersteller unterschiedliche Kombinationen von
              Grundierung, Lasur und Lack. Basierend auf den Herstellerangaben wurden die durchschnittlichen
              Sachbilanzdaten in Tabelle 18 erstellt. Die Produktionsabfälle werden in der KVA verbrannt. Für
              die Transportdistanzen wurden Standarddistanzen gemäss Frischknecht et al. (2007) verwendet.
                                                                                                                                                                                            33
                                                                                                                                                      Ökobilanz von Holztüren und Holzfenstern




             Tabelle 18: Sachbilanzdaten für die Oberflächenbehandlung von 1 m2 Flügelansichtsfläche ab Werk in der Schweiz




                                                                                                                                                                                     Standard Deviation
                                                                                                                                                                  Uncertainty Type
                                                                                                                           surface                    surface
                                                                                                            surface                     surface




                                                                                 Infrastructure
                                                                                                                         treatment,                 treatment,




                                                                      Location


                                                                                    Process
                                                                                                          treatment,                  treatment,




                                                                                                                                                                                           95%
                                                                                                                        inner door,                 outer door,




                                                                                                  Unit
                                        Name                                                             inner door,                  outer door,                                                         General Comment
                                                                                                                          opaquely                   opaquely
                                                                                                          natural, at                 natural, at
                                                                                                                        painted, at                 painted, at
                                                                                                             plant                       plant
                                                                                                                            plant                      plant

                                    Location                                                                 CH            CH            CH            CH
                            Infrastructure Process                                                            0             0             0             0
                                      Unit                                                                   m2            m2            m2            m2
product      surface treatment, inner door, natural, at plant         CH             0            m2          1             0             0             0
             surface treatment, inner door, opaquely painted, at      CH             0            m2          0             1             0             0
             surface treatment, outer door, natural, at plant         CH             0            m2          0             0             1             0
             surface treatment, outer door, opaquely painted, at
                                                                      CH             0            m2          0             0             0             1
             plant
technospher                                                                                                                                                                                (3,3,1,1,1,4,BU:1.05); Primer / impregnation;
            alkyd paint, white, 60% in H2O, at plant                  RER            0            kg      4.61E-1        8.13E-1       4.22E-1       8.61E-1        1                 1.16
e                                                                                                                                                                                          Average of data from manufacturers
                                                                                                                                                                                           (3,3,1,1,1,4,BU:1.05); opaquely painted;
             acrylic varnish, 87.5% in H2O, at plant                  RER            0            kg          0          5.84E-1          0          8.93E-1        1                 1.16
                                                                                                                                                                                           Average of data from manufacturers
                                                                                                                                                                                           (3,3,1,1,1,4,BU:1.05); natural glaze; Average of
             acrylic dispersion, 65% in H2O, at plant                 RER            0            kg          0             0          8.29E-1          0           1                 1.16
                                                                                                                                                                                           data from manufacturers
                                                                                                                                                                                                          (3,3,1,1,1,4,BU:1.05); natural oil/varnised;
             alkyd resin, long oil, 70% in white spirit, at plant     RER            0            kg      6.28E-1           0             0             0           1                 1.16
                                                                                                                                                                                                          Average of data from manufacturers
                                                                                                                                                                                           (3,3,1,1,1,4,BU:1.05); Disposal production
             disposal, building, paint on wood, to final disposal     CH             0            kg      2.57E-1        3.22E-1       2.09E-1       4.27E-1        1                 1.16 waste paint; Average of data from
                                                                                                                                                                                           manufacturers
                                                                                                                                                                                           (3,3,1,1,1,4,BU:2); Transportation to production
             transport, freight, lorry, fleet average                 CH             0            tkm     5.45E-2        6.98E-2       6.25E-2       8.77E-2        1                 2.03
                                                                                                                                                                                           site; Frischknecht et al. 2007
                                                                                                                                                                                           (3,3,1,1,1,4,BU:2); Transportation to production
             transport, freight, rail                                 CH             0            tkm     4.02E-1        8.38E-1       7.51E-1       1.05E+0        1                 2.03
                                                                                                                                                                                           site; Frischknecht et al. 2007
                                                                                                                                                                                           (3,3,1,1,1,4,BU:1.05); Transportation
             transport, municipal waste collection, lorry 21t         CH             0            tkm     2.57E-3        3.22E-3       2.09E-3       4.27E-3        1                 1.16 production waste to municipal incineration;
                                                                                                                                                                                           Frischknecht et al. 2007




             Aufgrund geringer Datenverfügbarkeit wurde die Aluminiumbeplankung der Aussentüre für die
             Türansichtsfläche von 2 m2 und einer Rahmenfläche von 1.12 m2 (bei angenommenen
             Rahmenbreite 150 mm und einer Türdicke von 65 mm) berechnet. Basierend auf Herstellerdaten
             wurde angenommen, dass die Blechstärke des Aluminiums 2 mm ist. Bei einer Dichte von
             2690 kg/m3                  wird           für     die   Aluminiumbeplankung                                          16.8 kg          Aluminium                                    benötigt.                  Für        die
             Transportdistanz des Aluminiumblechs wurden Standarddistanzen aus Frischknecht et al. (2007)
             verwendet. Die Sachbilanz der Aluminiumbeplankung ist in Tabelle 19 aufgeführt.
 34
 Ökobilanz von Holztüren und Holzfenstern




                 Tabelle 19: Sachbilanzdaten für die Herstellung der Aluminiumbeplankung für 1 m2 Flügelansichtsfläche einer Aussentüre

                 aus Holz ab Werk in der Schweiz




                                                                                                                                                                                                                                         Standard Deviation 95%
                                                                                                                                               Infrastructure Process




                                                                                                                                                                                                                     Uncertainty Type
                                                                                                                               Location
                                                                                                                                                                                           panelling,




                                                                                                                                                                               Unit
                                                              Name                                                                                                                      aluminium, outer                                                              General Comment
                                                                                                                                                                                          door, at plant




                                                         Location                                                                                                                                 CH
                                              Infrastructure Process                                                                                                                               0

                                                              Unit                                                                                                                                m2

product                panelling, aluminium, outer door, at plant                                                             CH                  0                            m2                  1
             aluminium profile, uncoated, SZFF 2014, recycling                                                                                                                                                                                                        (4,5,1,1,1,5,BU:1.05); Aluminium for door panelling;
technosphere                                                                                                                  CH                  0                            kg                8.39E+0               1                1.38
             share 52%, at plant                                                                                                                                                                                                                                      Calculated based on door measures
                                                                                                                                                                                                                                                                      (4,5,1,1,1,5,BU:1.05); Powder coating of aluminium;
                       powder coating, aluminium sheet                                                                        RER                 0                            m2                1.56E+0               1                1.38
                                                                                                                                                                                                                                                                      Calculated based on door measures
                                                                                                                                                                                                                                                                      (4,5,1,1,1,5,BU:2); Transportation to production site;
                       transport, freight, lorry, fleet average                                                               CH                  0                            tkm               4.20E-1               1                2.14
                                                                                                                                                                                                                                                                      Frischknecht 2007 et al.
                                                                                                                                                                                                                                                                      (4,5,1,1,1,5,BU:2); Transportation to production site;
                       transport, freight, rail                                                                               CH                  0                            tkm               1.68E+0               1                2.14
                                                                                                                                                                                                                                                                      Frischknecht 2007 et al.




                 Die Sachbilanzen der Innen- und Aussentüren mit Oberflächenbehandlung und Ressourcen-
                 korrektur (siehe Unterkapitel 2.6) sind in Tabelle 20 dargestellt.

                 Tabelle 20: Sachbilanzdaten für die Herstellung von 1 m2 Holz-Innentüre oder Aussentüre ab Werk in der Schweiz



                                                                                                                                                                                                                                                                                                                    Standard Deviation 95%
                                                                                  Infrastructure Process




                                                                                                                                                                                                                 door, outer,
                                                                                                                                 door, inner, door, inner,                                          door, outer,              door, outer,                                                      Uncertainty Type
                                                                                                                   door, inner,                                           door, inner, door, inner,              glass-wood,
                                                                                                                                room, glass- functional, door, inner,                               wood, U=1.0                  wood-
                                                                       Location




                                                                                                                  room, wood,                                            room, glass- functional,                    U=0.7
                                                                                                                                    wood,        wood,     room, wood,                                W/m2K,                  aluminium,
                                                                                                           Unit




                                         Name                                                                        wooden                                               wood, steel wood, steel                   W/m2K,                                                                                                                   General Comment
                                                                                                                                   wooden       wooden     steel frame ,                              wooden                    wooden
                                                                                                                    frame, at                                              frame, at    frame, at                   wooden
                                                                                                                                  frame, at    frame, at      at plant                               frame, at                 frame, at
                                                                                                                       plant                                                  plant       plant                    frame, at
                                                                                                                                     plant        plant                                                plant                      plant
                                                                                                                                                                                                                      plant


                                       Location                                                                       CH                  CH                              CH            CH             CH       CH                                     CH                   CH         CH

                               Infrastructure Process                                                                 0                   0                               0             0              0        0                                      0                    0          0
                                         Unit                                                                         m2                  m2                              m2            m2             m2       m2                                     m2                   m2         m2
product        door, inner, room, wood, wooden frame, at plant         CH            0                     m2          1                   0                               0             0              0        0                                      0                    0          0

               door, inner, room, glass-wood, wooden frame, at plant   CH            0                     m2          0                  1                                0             0             0         0                                                0          0          0

               door, inner, functional, wood, wooden frame, at plant   CH            0                     m2          0                  0                                1             0             0         0                                                0          0          0
               door, inner, room, wood, steel frame , at plant         CH            0                     m2          0                  0                                0             1             0         0                                                0          0          0
               door, inner, room, glass-wood, steel frame, at plant    CH            0                     m2          0                  0                                0             0             1         0                                                0          0          0
               door, inner, functional, wood, steel frame, at plant    CH            0                     m2          0                  0                                0             0             0         1                                                0          0          0
               door, outer, wood, U=1.0 W/m2K, wooden frame, at        CH            0                     m2          0                  0                                0             0             0         0                                                1          0          0
               door, outer, glass-wood, U=0.7 W/m2K, wooden
                                                                       CH            0                     m2          0                  0                                0             0             0         0                                                0          1          0
               frame, at plant
               door, outer, wood-aluminium, wooden frame, at plant     CH            0                     m2          0                  0                                0             0             0         0                                                0          0          1
                                                                                                                                                                                                                                                                                                                                             (3,3,1,1,1,4,BU:1.05); ; Average of data
technosphere door leaf, room, inner, wood, at plant                    CH            0                     m2      1.00E+0                0                                0          1.00E+0          0         0                                                0          0          0         1                1.16
                                                                                                                                                                                                                                                                                                                                             from manufacturers
                                                                                                                                                                                                                                                                                                                                             (3,3,1,1,1,4,BU:1.05); ; Average of data
               door leaf, functional, inner, wood, at plant            CH            0                     m2          0                  0                             1.00E+0          0             0      1.00E+0                                             0          0          0         1                1.16
                                                                                                                                                                                                                                                                                                                                             from manufacturers
                                                                                                                                                                                                                                                                                                                                             (3,3,1,1,1,4,BU:1.05); ; Average of data
               door leaf, room, inner, wood-glass, at plant            CH            0                     m2          0           1.00E+0                                 0             0         1.00E+0       0                                                0          0          0         1                1.16
                                                                                                                                                                                                                                                                                                                                             from manufacturers
                                                                                                                                                                                                                                                                                                                                             (3,3,1,1,1,4,BU:1.05); ; Average of data
               door leaf, outer, wood, at plant                        CH            0                     m2          0                  0                                0             0             0         0                      1.00E+0                              0       1.00E+0      1                1.16
                                                                                                                                                                                                                                                                                                                                             from manufacturers
                                                                                                                                                                                                                                                                                                                                             (3,3,1,1,1,4,BU:1.05); ; Average of data
               door leaf, outer, wood-glass, at plant                  CH            0                     m2          0                  0                                0             0             0         0                                                0       1.00E+0       0         1                1.16
                                                                                                                                                                                                                                                                                                                                             from manufacturers
                                                                                                                                                                                                                                                                                                                                             (3,3,1,1,1,4,BU:1.05); ; Average of data
               door frame, inner, wood, at plant                       CH            0                     m2      1.00E+0         1.00E+0                              1.00E+0          0             0         0                                                0          0          0         1                1.16
                                                                                                                                                                                                                                                                                                                                             from manufacturers
                                                                                                                                                                                                                                                                                                                                             (3,3,1,1,1,4,BU:1.05); ; Average of data
               door frame, inner, steel, at plant                      CH            0                     m2          0                  0                                0          1.00E+0      1.00E+0    1.00E+0                                             0          0          0         1                1.16
                                                                                                                                                                                                                                                                                                                                             from manufacturers
                                                                                                                                                                                                                                                                                                                                             (3,3,1,1,1,4,BU:1.05); ; Average of data
               door frame, outer, wood, at plant                       CH            0                     m2          0                  0                                0             0             0         0                      1.00E+0                           1.00E+0    1.00E+0      1                1.16
                                                                                                                                                                                                                                                                                                                                             from manufacturers
               surface treatment, inner door, opaquely painted, at                                                                                                                                                                                                                                                                           (3,3,1,1,1,4,BU:1.05); ; Average of data
                                                                       CH            0                     m2      1.00E+0          5.96E-1                             1.00E+0       1.00E+0       5.96E-1   1.00E+0                                             0          0          0         1                1.16
               plant                                                                                                                                                                                                                                                                                                                         from manufacturers
               surface treatment, outer door, opaquely painted, at                                                                                                                                                                                                                                                                           (3,3,1,1,1,4,BU:1.05); ; Average of data
                                                                       CH            0                     m2          0                  0                                0             0             0         0                      1.00E+0                           6.30E-1    1.00E+0      1                1.16
               plant                                                                                                                                                                                                                                                                                                                         from manufacturers
               panelling, aluminium, outer door, at plant              CH            0                     m2          0                  0                                0             0             0         0                                                0          0       1.00E+0      1                1.16                      (3,3,1,1,1,4,BU:1.05); ; Average of data
resource,      Energy, gross calorific value, in biomass, resource                                                                                                                                                                                                                                                                           (3,3,1,1,1,4,BU:1.05); Resource
                                                                         -               -                 MJ      -1.50E+2       -1.50E+2                              -2.26E+2      -8.07E+1     -8.08E+1   -1.57E+2                  -2.71E+2                          -2.25E+2   -2.71E+2     1                1.16
biotic         correction                                                                                                                                                                                                                                                                                                                    correction wood;
resource, in                                                                                                                                                                                                                                                                                                                                 (3,3,1,1,1,4,BU:1.05); Resource
               Aluminium, resource correction                            -               -                 kg          0                  0                                0             0             0         0                      -1.35E+0                          -8.93E-1   -5.38E+0     1                1.16
ground                                                                                                                                                                                                                                                                                                                                       correction aluminium;
                                                                                                                                                                                                                                                                                                                                             (3,3,1,1,1,4,BU:1.05); Resource
               Iron, resource correction                                 -               -                 kg          0                  0                                0          -7.60E+0     -7.60E+0   -7.60E+0                                            0          0          0         1                1.16
                                                                                                                                                                                                                                                                                                                                             correction steel;
```

## Rules

1. Every line item must quote the exact line of the excerpt it comes from (`quote`), with the raw value and raw unit as printed. Never invent a value. If the excerpt gives a range, report the range as `raw_min`/`raw_max` and put your point estimate in `raw_value`.
2. Report values per the excerpt's own basis (`per`, e.g. "per t burnt shale", "per m2 board"); do not convert. State the reference basis you found in `basis` so the code can scale to 1 m2.
3. If a value needs a physical conversion (litres of diesel to MJ, m3 of water to kg), give `factor`, `factor_unit` and `factor_source` (a standard value with its source, e.g. "diesel 0.84 kg/l × 42.8 MJ/kg = 36 MJ/l, ecoinvent convention"). Leave `factor` at 1 otherwise.
4. Classify each line: `kind` = "input" (a product or service from another dataset), "emission" (a direct release to air/water/soil), "resource" (a direct extraction from nature), "product" (the reference product), "co-product" or "ignore" (with a reason).
5. Propose a `search` phrase (2–4 words) that a name search in a life-cycle database would use: for inputs the supplying dataset in ecoinvent-2 naming style ("diesel burned building machine", "sodium hydroxide production mix"); for emissions and resources the substance in EF 3.1 / ecoinvent nomenclature ("particles PM10" for dust, "nitrogen oxides", "carbon dioxide fossil", "crude oil", "water"). Do not guess the exact name; the search is resolved by code afterwards.
6. If the excerpt describes allocation (e.g. an economic allocation between co-products), record it in `allocation` and use the allocated column when the table has one. If it states that the composition items add up to a mass ("adds up to 1.00 kg"), put that mass per basis in `mass_sum`, else null.
7. Mark anything you are unsure about with `confidence` = "low" and say why in `note`. Do not omit uncertain items; the reviewer decides.
8. Do not add inputs the excerpt does not mention, even if you know the process needs them. Missing items are reported in `gaps` instead.

Return only the JSON object described by the schema.
