You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Panelling, aluminium, window frame cover, wall opening, at plant` [CH], reference unit 1 m2, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~6 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: building components / windows
- includedProcesses: Included are the materials for the panelling of the frame of a wood-metal window. Production losses and transport of the materials are included.
- technology: Industry data.
- generalComment: The measures of the window are 1.75m (width) x 1.3m (height). The average visible area is 0.29m2. The bill of materials is based on data from 4 window producers.;
UUID: 28d0e400-dfe2-3209-8f0e-849dbae9d0c6
- source cited in the metadata: Ramseier L. | 2020 | 2020 - LCA wooden windows and doors - Ramseier
- time period: 2018-01-2019-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 m2):
- none

## Report excerpt

Source file: `report-p25-27.txt` (SHA-256 6ab63fb788d71d66f953e434d63e6dd38b34ed869b5dc9b299fed5e57b3d3d72), pages 25-27 of `2020 - LCA wooden windows and doors - Ramseier.pdf`.

```
25
                                                                                                                                                                     Ökobilanz von Holztüren und Holzfenstern




          Tabelle 9: Sachbilanzdaten für die Herstellung von 1 m2 Holz-Metallfensterrahmen, ohne Oberflächenbehandlung, ab
          Werk (Fortsetzung)




                                                                                                                                                                      Standard Deviation 95%
                                                                                              Infrastructure Process




                                                                                                                                                  Uncertainty Type
                                                                                                                              window frame,




                                                                                   Location
                                                                                                                                wood-metal,




                                                                                                                       Unit
                                               Name                                                                              w/o surface                                                   General Comment
                                                                                                                               treatment, m2
                                                                                                                              visible, at plant



                                             Location                                                                               CH
                                       Infrastructure Process                                                                        0
                                                 Unit                                                                               m2
product    window frame, wood-metal, w/o surface treatment, m2 visible, at plant   CH            0                     m2            1

                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal production waste scantling;
           disposal, wood untreated, 20% water, to municipal incineration          CH            0                     kg        3.16E+1            1                1.16
                                                                                                                                                                                               Average of data from manufacturers

                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal production waste adhesive in
           disposal, polyurethane, 0.2% water, to municipal incineration           CH            0                     kg        4.27E-1            1                1.16
                                                                                                                                                                                               scantling; Average of data from manufacturers

                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal production waste steel sheet,
           disposal, steel, 0% water, to municipal incineration                    CH            0                     kg        4.46E-1            1                1.16
                                                                                                                                                                                               low-alloyed; Average of data from manufacturers

                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal production waste steel screws,
           disposal, steel, 0% water, to municipal incineration                    CH            0                     kg        1.00E-2            1                1.16
                                                                                                                                                                                               low-alloyed; Average of data from manufacturers

                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal production waste polyamide;
           glass reinforced plastic sheet (GFK), in MSWI                           CH            0                     kg        6.25E-2            1                1.16
                                                                                                                                                                                               Average of data from manufacturers

                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal production waste other plastics;
           disposal, plastics, mixture, 15.3% water, to municipal incineration     CH            0                     kg            0              1                1.16
                                                                                                                                                                                               Average of data from manufacturers


                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal production waste EPDM;
           disposal, rubber, unspecified, 0% water, to municipal incineration      CH            0                     kg        2.00E-1            1                1.16
                                                                                                                                                                                               Average of data from manufacturers

                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal production waste TPE; Average
           disposal, rubber, unspecified, 0% water, to municipal incineration      CH            0                     kg        2.96E-2            1                1.16
                                                                                                                                                                                               of data from manufacturers
                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal production waste silicon;
           disposal, rubber, unspecified, 0% water, to municipal incineration      CH            0                     kg        5.95E-2            1                1.16
                                                                                                                                                                                               Average of data from manufacturers
                                                                                                                                                                          (3,3,1,1,1,4,BU:1.05); Disposal production waste PVCa-
           disposal, polyurethane, 0.2% water, to municipal incineration           CH            0                     kg        1.28E-3            1                1.16
                                                                                                                                                                          adhesive; Average of data from manufacturers
                                                                                                                                                                          (3,3,1,1,1,4,BU:1.05); Disposal production waste acrylic
           disposal, polyurethane, 0.2% water, to municipal incineration           CH            0                     kg        2.05E-4            1                1.16
                                                                                                                                                                          adhesive; Average of data from manufacturers
                                                                                                                                                                          (3,3,1,1,1,4,BU:1.05); Disposal production waste metal
           disposal, polyurethane, 0.2% water, to municipal incineration           CH            0                     kg        2.17E-3            1                1.16
                                                                                                                                                                          adhesive; Average of data from manufacturers
           disposal, building, polystyrene isolation, flame-retardant, to final                                                                                                                (3,3,1,1,1,4,BU:1.05); Disposal production waste insulation;
                                                                                   CH            0                     kg        1.82E-3            1                1.16
           disposal                                                                                                                                                                            Average of data from manufacturers

                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal production waste other
           disposal, polyurethane, 0.2% water, to municipal incineration           CH            0                     kg            0              1                1.16
                                                                                                                                                                                               adhesive; Average of data from manufacturers

                                                                                                                                                                          (3,3,1,1,1,4,BU:1.05); Electricity; Average of data from
           electricity, medium voltage, at grid                                    CH            0                     kWh       1.04E+2            1                1.16
                                                                                                                                                                          manufacturers
                                                                                                                                                                          (3,3,1,1,1,4,BU:1.05); Heat from heating oil ; Average of data
           heat, light fuel oil, at boiler 100kW condensing, non-modulating        CH            0                     MJ        3.92E+0            1                1.16
                                                                                                                                                                          from manufacturers

                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Wood chips; Average of data from
           wood chips, from industry, softwood, burned in furnace 300kW            CH            0                     MJ        1.70E+2            1                1.16
                                                                                                                                                                                               manufacturers

                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Cleaning agent; Average of data from
           chemicals organic, at plant                                             GLO           0                     kg        1.99E-2            1                1.16
                                                                                                                                                                                               manufacturers
                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Water; Average of data from
           tap water, at user                                                      CH            0                     kg        8.97E-2            1                1.16
                                                                                                                                                                                               manufacturers
                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Lubricating oil; Average of data from
           lubricating oil, at plant                                               RER           0                     kg        3.26E-2            1                1.16
                                                                                                                                                                                               manufacturers
                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Other chemicals; Average of data from
           chemicals organic, at plant                                             GLO           0                     kg        9.34E-3            1                1.16
                                                                                                                                                                                               manufacturers
                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Packaging cardboard; Average of data
           packaging, corrugated board, mixed fibre, single wall, at plant         CH            0                     kg        1.20E-2            1                1.16
                                                                                                                                                                                               from manufacturers
                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Packaging PE foil; Average of data from
           packaging film, LDPE, at plant                                          RER           0                     kg        2.91E-1            1                1.16
                                                                                                                                                                                               manufacturers
                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Packaging pallet; Average of data from
           EUR-flat pallet                                                         RER           0                     unit      2.57E-4            1                1.16
                                                                                                                                                                                               manufacturers
                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Disposal of packaging PE foil; Average of
           disposal, plastics, mixture, 15.3% water, to municipal incineration     CH            0                     kg        2.91E-1            1                1.16
                                                                                                                                                                                               data from manufacturers
                                                                                                                                                                                               (3,3,1,1,1,4,BU:2); Transport of materials to production site;
           transport, freight, lorry, fleet average                                CH            0                     tkm       1.20E+2            1                2.03
                                                                                                                                                                                               Average of data from manufacturers and standard distances
                                                                                                                                                                          (3,3,1,1,1,4,BU:2); Transport of materials to production site;
           transport, freight, rail                                                CH            0                     tkm       7.96E+0            1                2.03
                                                                                                                                                                          Average of data from manufacturers and standard distances
                                                                                                                                                                          (3,3,1,1,1,4,BU:1.05); Transport production waste to municipal
           transport, municipal waste collection, lorry 21t                        CH            0                     tkm       3.32E-1            1                1.16
                                                                                                                                                                          incineration; Standard distances
 26
 Ökobilanz von Holztüren und Holzfenstern




            Die Rahmen und die Flügel des Holz-Metallfensterrahmen sind aluminiumbeplankt. Die
            Herstellung der Aluminiumbeplankung wurde mit dem spezifischen Sachbilanzdatensatz für
            Aluminiumprofile für den Schweizer Markt abgebildet (Stolz & Frischknecht 2016). Die
            Transportdistanzen sind gemäss den durchschnittlichen Herstellerangaben modelliert. Die
            Sachbilanzdaten der Aluminiumbeplankung des Holz-Metallfensterrahmens sind in Tabelle 10
            dargestellt.

            Tabelle 10: Sachbilanzdaten der Herstellung der Aluminiumbeplankung des Holz-Metallfensterrahmens pro m2

            Rahmenfläche im Licht, ab Werk




                                                                                                                                                                   Standard Deviation 95%
                                                                                        Infrastructure Process




                                                                                                                                               Uncertainty Type
                                                                                                                            panelling,
                                                                             Location
                                                                                                                           aluminium,




                                                                                                                 Unit
                                              Name                                                                      window casement                                                     General Comment
                                                                                                                         and frame cover,
                                                                                                                        m2 visible, at plant



                                             Location                                                                           CH
                                     Infrastructure Process                                                                      0


                                               Unit                                                                             m2


             panelling, aluminium, window casement and frame cover, m2
                                                                             CH            0                     m2              1
             visible, at plant
             aluminium profile, uncoated, SZFF 2014, recycling share 52%,                                                                                              (3,3,1,1,1,4,BU:1.05); Aluminium profil (anodised); Average of
technosphere                                                                 CH            0                     kg          1.75E+1             1                1.16
             at plant                                                                                                                                                  data from manufacturers
                                                                                                                                                                       (3,3,1,1,1,4,BU:1.05); Anodising of aluminium profil; Average of
              anodising, aluminium sheet                                     RER           0                     m2          4.34E+0             1                1.16
                                                                                                                                                                       data from manufacturers
              aluminium profile, uncoated, SZFF 2014, recycling share 52%,                                                                                             (3,3,1,1,1,4,BU:1.05); Aluminium profil (powder coated); Average
                                                                             CH            0                     kg          1.38E+1             1                1.16
              at plant                                                                                                                                                 of data from manufacturers
                                                                                                                                                                       (3,3,1,1,1,4,BU:1.05); Powder coating of aluminium profil;
              powder coating, aluminium sheet                                RER           0                     m2          3.41E+0             1                1.16
                                                                                                                                                                       Average of data from manufacturers
                                                                                                                                                                       (3,3,1,1,1,4,BU:2); Transport of materials to production site;
              transport, freight, lorry, fleet average                       CH            0                     tkm         3.75E+0             1                2.03
                                                                                                                                                                       Average of data from manufacturers




            Die Oberflächen der Holz- und Holz-Metallfensterrahmen sind geölt/lasiert oder deckend
            gestrichen. Dafür verwenden die Hersteller unterschiedliche Kombinationen von Holzschutzmittel,
            Grundierung, Lasur, Lack und Naturöl. Basierend auf den Herstellerangaben wurden die
            durchschnittlichen Sachbilanzdaten in Tabelle 11 (Holzfensterrahmen) und in Tabelle 12 (Holz-
            Metallfensterrahmen) erstellt. Es wurde angenommen, dass die Produktionsabfälle in der KVA
            verbrannt werden. Für die Transportdistanzen wurden Standarddistanzen gemäss Frischknecht et
            al. (2007) verwendet.
                                                                                                                                                                                                                                                                                          27
                                                                                                                                                                                                                                                    Ökobilanz von Holztüren und Holzfenstern




               Tabelle 11: Sachbilanzdaten der Oberflächenbehandlung (geölt/lasiert oder deckend gestrichen) für Holz-Fensterrahmen
               pro m2 Rahmenfläche im Licht, ab Werk




                                                                                                                                                                                                                                                     Standard Deviation 95%
                                                                                                        Infrastructure Process




                                                                                                                                                                                                                    Uncertainty Type
                                                                                                                                                                        surface treatment, surface treatment,




                                                                                  Location
                                                                                                                                                                         wood window,         wood window,




                                                                                                                                                          Unit
                                                  Name                                                                                                                                                                                                                                        General Comment
                                                                                                                                                                        natural/varnished, opaquely painted,
                                                                                                                                                                        m2 visible, at plant m2 visible, at plant




                                                Location                                                                                                                        CH                   CH

                                          Infrastructure Process                                                                                                                 0                    0



                                                   Unit                                                                                                                         m2                   m2



               surface treatment, wood window, natural/varnished, m2 visible,
product                                                                           CH                       0                                              m2                     1                    0
               at plant
               surface treatment, wood window, opaquely painted, m2 visible,
                                                                                  CH                       0                                              m2                     0                    1
               at plant
                                                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Wood preservative; Average of data from
technosphere alkyd paint, white, 60% in H2O, at plant                             RER                      0                                              kg                 1.75E-2                  0               1                             1.16
                                                                                                                                                                                                                                                                                              manufacturers

                                                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Acrylic filler; Average of data from
               acrylic filler, at plant                                           RER                      0                                              kg                     0                 1.34E-2            1                             1.16
                                                                                                                                                                                                                                                                                              manufacturers

                                                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Primer / impregnation; Average of data
               alkyd paint, white, 60% in H2O, at plant                           RER                      0                                              kg                 2.27E+0               8.56E-1            1                             1.16
                                                                                                                                                                                                                                                                                              from manufacturers

                                                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Wood preservative glaze; Average of data
               acrylic dispersion, 65% in H2O, at plant                           RER                      0                                              kg                 3.50E-2                  0               1                             1.16
                                                                                                                                                                                                                                                                                              from manufacturers

                                                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Wood glaze; Average of data from
               acrylic dispersion, 65% in H2O, at plant                           RER                      0                                              kg                 2.62E+0                  0               1                             1.16
                                                                                                                                                                                                                                                                                              manufacturers

                                                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Top and intermediate varnish; Average of
               acrylic varnish, 87.5% in H2O, at plant                            RER                      0                                              kg                     0                5.50E+0             1                             1.16
                                                                                                                                                                                                                                                                                              data from manufacturers

                                                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Natural oil; Average of data from
               alkyd resin, long oil, 70% in white spirit, at plant               RER                      0                                              kg                 1.05E+0                  0               1                             1.16
                                                                                                                                                                                                                                                                                              manufacturers

                                                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Oil paint; Average of data from
               alkyd resin, long oil, 70% in white spirit, at plant               RER                      0                                              kg                     0                2.57E+0             1                             1.16
                                                                                                                                                                                                                                                                                              manufacturers

                                                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Disposal production waste paint; Average
               disposal, building, paint on wood, to final disposal               CH                       0                                              kg                 3.73E-1               3.74E-1            1                             1.16
                                                                                                                                                                                                                                                                                              of data from manufacturers
                                                                                                                                                                                                                                                         (3,3,1,1,1,4,BU:2); Transport of materials to production site;
               transport, freight, lorry, fleet average                           CH                       0                                              tkm                3.00E-1               4.47E-1            1                             2.03
                                                                                                                                                                                                                                                         Standard distances
                                                                                                                                                                                                                                                         (3,3,1,1,1,4,BU:2); Transport of materials to production site;
               transport, freight, rail                                           CH                       0                                              tkm                3.18E+0              4.34E+0             1                             2.03
                                                                                                                                                                                                                                                         Standard distances



               Tabelle 12: Sachbilanzdaten der Oberflächenbehandlung für Holz-Metallfensterrahmen pro m2 Rahmenfläche im Licht, ab
               Werk
                                                                                                                                                                                                                                                                     Standard Deviation 95%
                                                                                                                                 Infrastructure Process




                                                                                                                                                                                                                                 Uncertainty Type




                                                                                                                                                                          surface treatment, surface treatment,
                                                                                             Location




                                                                                                                                                                             wood-metal           wood-metal
                                                                                                                                                                 Unit




                                                     Name                                                                                                                      window,         window, opaquely                                                                                General Comment
                                                                                                                                                                          natural/varnished,      painted, m2
                                                                                                                                                                          m2 visible, at plant  visible, at plant



                                                    Location                                                                                                                         CH                CH
                                        Infrastructure Process                                                                                                                        0                 0
                                                  Unit                                                                                                                               m2                m2
                    surface treatment, wood-metal window, natural/varnished, m2
product                                                                                      CH                                     0                        m2                      1                    0
                    visible, at plant
                    surface treatment, wood-metal window, opaquely painted, m2
                                                                                             CH                                     0                        m2                      0                    1
                    visible, at plant
                                                                                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Wood preservative; Average of data from
technosphere        alkyd paint, white, 60% in H2O, at plant                           RER                                          0                            kg             4.11E-1                   0                        1                     1.16
                                                                                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Acrylic filler; Average of data from
                    acrylic filler, at plant                                           RER                                          0                            kg                  0               1.00E-2                       1                     1.16
                                                                                                                                                                                                                                                                                               manufacturers

                                                                                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Primer / impregnation; Average of data
                    alkyd paint, white, 60% in H2O, at plant                           RER                                          0                            kg             1.53E+0              4.83E-1                       1                     1.16
                                                                                                                                                                                                                                                                                               from manufacturers

                                                                                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Wood preservative glaze; Average of data
                    acrylic dispersion, 65% in H2O, at plant                           RER                                          0                            kg             2.34E-2                   0                        1                     1.16
                                                                                                                                                                                                                                                                                               from manufacturers
                                                                                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Wood glaze; Average of data from
                    acrylic dispersion, 65% in H2O, at plant                           RER                                          0                            kg             1.30E+0                   0                        1                     1.16
                                                                                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Top and intermediate varnish; Average of
                    acrylic varnish, 87.5% in H2O, at plant                            RER                                          0                            kg                  0               4.73E+0                       1                     1.16
                                                                                                                                                                                                                                                                                               data from manufacturers

                                                                                                                                                                                                                                                                                               (3,3,1,1,1,4,BU:1.05); Natural oil; Average of data from
                    alkyd resin, long oil, 70% in white spirit, at plant               RER                                          0                            kg             7.01E-1                   0                        1                     1.16
                                                                                                                                                                                                                                                                                               manufacturers
                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Oil paint; Average of data from
                    alkyd resin, long oil, 70% in white spirit, at plant               RER                                          0                            kg                  0               1.93E+0                       1                     1.16
                                                                                                                                                                                                                                                              manufacturers
                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:1.05); Disposal production waste paint; Average
                    disposal, building, paint on wood, to final disposal                     CH                                     0                            kg             2.14E-1              2.79E-1                       1                     1.16
                                                                                                                                                                                                                                                              of data from manufacturers
                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:2); Transport of materials to production site;
                    transport, freight, lorry, fleet average                                 CH                                     0                        tkm                1.99E-1              3.58E-1                       1                     2.03
                                                                                                                                                                                                                                                              Standard distances
                                                                                                                                                                                                                                                              (3,3,1,1,1,4,BU:2); Transport of materials to production site;
                    transport, freight, rail                                                 CH                                     0                        tkm                2.10E+0              3.52E+0                       1                     2.03
                                                                                                                                                                                                                                                              Standard distances
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
