You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process.

The dataset `Cement ZN, D, at plant` [CH], reference unit 1 kg, is shipped in the BAFU-2026 database as a "system terminated" inventory: it has no technosphere inputs, only ~1660 cumulative elementary flows. A public report documents the underlying process. Your job is to read the report excerpt and produce the *unit process* as line items — what the process consumes from other datasets and what it emits directly — each traceable to the excerpt.

## What the database says about the dataset

- BAFU category: construction materials / binder
- includedProcesses: <null>
- technology: Unspecified
- generalComment: na;
UUID: c3490cfc-bcf2-38a2-a8c1-2d50ba65c83e
- source cited in the metadata: Tschuemperlin L. | 2020 | 2020 - LCA selected types of concrete - Tschuemperlin
- time period: 2018-01-2018-12

## Direct resource flows visible in the aggregated vector

These flows appear in the aggregated inventory with amounts that no upstream dataset would plausibly emit on this dataset's behalf; they are candidates for the process's own direct resource flows (per 1 kg):
- Water to turbine: 1.027 cubic meter (Resources Resources from water Renewable material resources from water)
- Calcite: 0.8329 kilogram (resources in ground)
- Uranium: 0.6241 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Hard Coal: 0.5833 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Crude Oil: 0.4984 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Crude Oil: 0.4955 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Energy, Potential (in Hydropower Reservoir), Converted: 0.1792 megajoule (natural resource)
- Brown Coal: 0.1707 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Natural Gas: 0.1616 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Shale: 0.1304 kilogram (soil)
- Uranium: 0.08262 megajoule (Resources Resources from ground Non-renewable energy resources from ground)
- Clay: 0.05474 kilogram (soil)

## Report excerpt

Source file: `report-p25-26.txt` (SHA-256 95d82d20fed0b8de32be942d875bbaf190fecd235312a53b0e24f17642dd4db1), pages 25-26 of `2020 - LCA selected types of concrete - Tschuemperlin.pdf`.

```
Sachbilanzdaten und Modellierungsannahmen                                                                                                                                                                                     21




Tab. 3.13: Sachbilanzen von 1 kg CEM II/B CH-Mix, CEM II/B-LL und CEM II/A Zement, ab Werk




                                                                                                                                                                              StandardDeviation95%
                                                                               InfrastructureProcess




                                                                                                                                                           UncertaintyType
                                                                    Location
                                                                                                               CEM II/B CH-     CEM II/B-LL    CEM II/A




                                                                                                        Unit
                                           Name                                                                Mix cement, at   cement, at    cement, at                                             GeneralComment
                                                                                                                    plant         plant         plant



                                        Location                                                                    CH             CH            CH
                                InfrastructureProcess                                                                0              0             0
                                          Unit                                                                      kg             kg            kg
product         CEM II/B CH-Mix cement, at plant                    CH            0                     kg           1               0             0
product         CEM II/B-LL cement, at plant                        CH            0                     kg           0               1             0
product         CEM II/A cement, at plant                           CH            0                     kg           0               0             1
                                                                                                                                                                                  (1,1,1,1,1,1,BU:3); ; basiert auf
technosphere    cement plant                                        CH            1                    unit      2.73E-11        2.73E-11     2.73E-11       1               3.00
                                                                                                                                                                                  ecoinvent 3.2 Datensatz
                                                                                                                                                                                  (2,1,1,1,3,5,BU:1.05); ; basiert auf
                clinker (data from ecoinvent v3.2), at plant        CH            0                     kg        6.88E-1        7.10E-1       7.88E-1       1               1.31
                                                                                                                                                                                  ecoinvent 3.2 Datensatz
                                                                                                                                                                                  (1,3,3,3,1,1,BU:1.05); ; basiert auf
                burnt shale, at plant                               DE            0                     kg        1.36E-1                                    1               1.31
                                                                                                                                                                                  ecoinvent 3.2 Datensatz
                ground granulated blast furnace slag, no                                                                                                                          (1,3,3,3,1,1,BU:1.05); ; basiert auf
                                                                    RER           0                     kg                                     1.80E-3       1               1.31
                burdens, at plant                                                                                                                                                 ecoinvent 3.2 Datensatz
                                                                                                                                                                                  (2,1,1,1,3,5,BU:1.05); ; basiert auf
                electricity, medium voltage, at grid                CH            0                    kWh        3.42E-2        3.42E-2       3.13E-2       1               1.31
                                                                                                                                                                                  ecoinvent 3.2 Datensatz
                                                                                                                                                                                  (1,3,3,3,1,1,BU:1.05); ; basiert auf
                ethylene glycol, at plant                           RER           0                     kg        2.10E-4        2.10E-4       2.12E-4       1               1.13
                                                                                                                                                                                  ecoinvent 3.2 Datensatz
                                                                                                                                                                                  (4,5,na,na,na,na,BU:1.05); ; basiert
                gypsum, mineral, at mine                            CH            0                     kg        2.11E-2        2.11E-2       4.64E-2       1               1.30
                                                                                                                                                                                  auf ecoinvent 3.2 Datensatz
                                                                                                                                                                                  (2,1,1,1,1,5,BU:1.05); ; basiert auf
air, unspecified Heat, waste                                         -               -                  MJ        1.23E-1        1.23E-1       1.13E-1       1               1.22
                                                                                                                                                                                  ecoinvent 3.2 Datensatz
                                                                                                                                                                                  (2,1,1,1,1,5,BU:1.05); ; basiert auf
technosphere    steel, low-alloyed, at plant                        RER           0                     kg        4.00E-5        4.00E-5       4.04E-5       1               1.22
                                                                                                                                                                                  ecoinvent 3.2 Datensatz
                heavy fuel oil, burned in industrial furnace 1MW,                                                                                                                 (2,1,1,1,1,5,BU:1.05); ; basiert auf
                                                                    RER           0                     MJ                                     1.21E-3       1               1.22
                non-modulating                                                                                                                                                    ecoinvent 3.2 Datensatz
                                                                                                                                                                                  (2,1,1,1,1,5,BU:1.05); ; basiert auf
                limestone, crushed, for mill                        CH            0                     kg        1.51E-1        2.69E-1       1.61E-1       1               1.22
                                                                                                                                                                                  ecoinvent 3.2 Datensatz
                                                                                                                                                                                  (2,1,1,1,1,5,BU:2); hinzugefügt, da in
                transport, lorry 20-28t, fleet average              CH            0                    tkm        4.44E-2        2.00E-2       2.00E-2       1               2.05
                                                                                                                                                                                  ecoinvent v3.2 nicht berücksichtigt;
                                                                                                                                                                                  (2,1,1,1,1,5,BU:2); hinzugefügt, da in
                transport, freight, rail                            RER           0                    tkm        1.50E-4        1.50E-4       1.23E-3       1               2.05
                                                                                                                                                                                  ecoinvent v3.2 nicht berücksichtigt;



3.10 Herstellung von Zement ZN/D
Zement ZN/D setzt sich hauptsächlich aus Klinker, Mischgranulat und gebranntem Öl-
schiefer zusammen (Werner 2018). Die Tab. 3.14 dargestellte Sachbilanz stammt aus
Werner (2018) und addiert sich zu 1.00 kg Zement.
Tab. 3.14: Sachbilanz von 1kg Zement ZN/D, ab Werk

Inputs                                                                                                 Einheit                           Menge
Klinker                                                                                                %                                 40%-70%
Gips, mineralisch                                                                                      %                                  < 10%
Mischgranulat (MG)                                                                                     %                                 15%-30%
Schiefer, gebrannt                                                                                     %                                 15%-30%
Eisen-II Sulfat                                                                                        %                                    < 1%
Filterstaub / Kalkstein                                                                                %                                  < 10%
Ethylenglykol als Mahlhilfe                                                                            kg/kg                             5.50E-04
Strom, Mittelspannung                                                                                  kWh/kg                            4.97E-02
Schweröl zur Wärmeerzeugung                                                                            MJ/kg                             1.62E-01
Zementfabrik, Infrastruktur                                                                            p/kg                              5.36E-11
Stahl für Mahlwerk, niedrig legiert                                                                    kg/kg                             1.10E-04
Transport LKW                                                                                          tkm/kg                            8.37E-03
Transport Bahn                                                                                         tkm/kg                            4.28E-02


Ökobilanz ausgewählter Betonsorten                                                                                                                                                                                    treeze Ltd.
Sachbilanzdaten und Modellierungsannahmen                                                                            22




Die Umweltkennwerte des Zements ZN/D stammen aus Werner (2018) und wurden mit
den Sachbilanzdaten von gebranntem Ölschiefer gemäss den beiden Allokationsansät-
zen ermittelt (siehe Beschreibung Unterkapitel 3.6 und Anhang A). Im Betonrechner ist
die Variante „ökonomische Allokation“ implementiert.


3.11 Herstellung unspezifischer Betonsorten
Die vier unspezifischen Betone unterscheiden sich in ihrer Rohdichte, Druckfestigkeit,
Verarbeitung, ihrem Anwendungsbereich sowie weiteren besonderen Eigenschaften8.
Sie haben zudem unterschiedliche Zementgehalte.
Die Daten der Fachstelle Ingenieurwesen des Amts für Hochbauten der Stadt Zürich
geben Auskunft über die Zusammensetzung der Betone bezüglich deren Gehalt an na-
türlicher und Recycling-Gesteinskörnung, Zement (Anteile CEM I, CEM II/A und CEM
II/B), deren Fliessmittelbedarf sowie deren Rohdichte. Dabei handelt es sich um Durch-
schnittswerte der NPK Betonsorten dieser Anwendungsbereiche. Tab. 3.15 zeigt die
Zusammensetzung der vier unspezifischen Betonsorten auf. Die Rohdichten der Betone
berechnen sich durch das Aufaddieren der durchschnittlichen Mengen an Zement, natür-
licher und Recycling-Gesteinskörnung, Wasser und Fliessmittel. Der Wassergehalt
wurde für alle vier unspezifischen Betone über den w/z-Wert von 0.5 bestimmt9.
Tab. 3.15: Zusammensetzung und Rohdichten der unspezifischen Betonsorten

                                                          Natürliche GK
                                CEM I CEM II/A CEM II/B                    M       C    Wasser Fliessmittel Rohdichte
        Betonsorte                                         (Kies/S and)
                               [kg/m3] [kg/m3] [kg/m3]                  [kg/m3] [kg/m3]   [l]    [kg/m3]     [kg/m3]
                                                             [kg/m3]
Hochbaubeton, unspezifisch       30      130     130           1678        93      93    145         1         2300
Tiefbaubeton, unspezifisch       30      145     145          1865         0       0      160        5        2350
Bohrpfahlbeton, unspezifisch     35      160     160          1611         0      179     178        2        2325
M agerbeton, unspezifisch        0       75       75           963        963      0      75         0        2150

In den Sachbilanzdaten der vier unspezifischen Betonsorten (siehe Tab. 3.16) wird das
Fliessmittel nicht mehr mit dem Datensatz „plasticiser, for concrete, based on sul-
fonated melamine formaldehyde“, welches die Produktion von Betonverflüssiger aus
Melaminharz abbildet, sondern mit dem Datensatz „polycarboxylates, 40% active sub-
stance, at plant“ bilanziert. Heute werden Betonverflüssiger mehrheitlich auf Polycar-
boxylatbasis hergestellt, da diese effizienter wirken und dadurch geringer dosiert wer-
den können. Zudem sind Fliessmittel auf Polycarboxylatbasis weniger problematisch für
die Umwelt, da sie keine Formaldehyde beinhalten (Müller & Hampel 2010).
Die Transportaufwände der Hilfsmittel und Rohstoffe zum Betonwerk werden berück-
sichtigt. Die Distanzen per Bahn und per LKW werden über Standardtransportdistanzen


8
    http://www.baunetzwissen.de/standardartikel/Beton_Klassifizierung-der-Betonarten_150972.html,
    abgerufen am 03.02.2016
9
    Persönliche Mitteilung, Michael Pöll, Amt für Hochbauten Stadt Zürich, 27.06.2016




Ökobilanz ausgewählter Betonsorten                                                                          treeze Ltd.
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
