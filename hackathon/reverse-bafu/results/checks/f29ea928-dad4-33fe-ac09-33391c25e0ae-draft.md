# Check: Titanium dioxide at plant, sulphate process, at plant (f29ea928-dad4-33fe-ac09-33391c25e0ae)

target `bafu-2026` vs explicit model `f29ea928-dad4-33fe-ac09-33391c25e0ae-draft-disagg` and hybrid `f29ea928-dad4-33fe-ac09-33391c25e0ae-draft-hybrid`

**Strategy:** S3 — top-down model drafted from the report excerpt by the LLM pipeline (reverse-bafu draft); the report's tables are published comparison data, not this dataset's inventory. basis: per 1 kg of TiO2; Tab. 85.3 'Kg per kg of product', Tab. 85.4 'Consumption per kg of product (MJ/kg)', Tab. 85.6 and Tab. 85.8 'Gram per kg of product'. The SULFATE-process column is used.; allocation: none stated; the report notes filter salts 'that are produced can be sold' but gives no allocation; 2 of 7 inputs carry a printed amount, 5 a printed range, 0 no number in the report. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** Sulphuric acid, liquid, at plant [2.4–3.5], xxx Electricity, medium voltage, production UCTE, at grid [0.619–1.41], Heat, natural gas, at industrial furnace 1MW [10.4–24.2], Natural gas, burned in industrial furnace 1MW [9.67–16.2], Hard coal, burned in industrial furnace 1-10MW [5.8–8.5]
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 11/50 within ±10 %, median |Δ| 41.6%
- kilogram mass covered within ±10 %: 13.3% of the target's total kg mass
- of the 1148 flows of the target, 1148 are determined by the solve (0 are round-off and are not scored; see lci.determined_flows)
- 117 of those 1148 within ±10 % (10%), median |Δ| 75.2%, 0 missing from the model, 635 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 117 | 10% |
| 10–20 % | 107 | 9% |
| 20–50 % | 239 | 21% |
| 50–100 % | 265 | 23% |
| > 100 % | 420 | 37% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (924 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 3.22 | 2.32 | -28.0% | +0.901 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.876 | 0.366 | -58.2% | +0.51 |
| Gravel [soil] (kilogram) | 0.693 | 0.488 | -29.6% | +0.205 |
| Titanium [Resources/Resources from ground] (kilogram) | 0.689 | 0.682 | -1.1% | +0.00748 |
| Calcite [resources/in ground] (kilogram) | 0.546 | 0.274 | -49.8% | +0.272 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.337 | 0.291 | -13.6% | +0.046 |
| Sodium chloride [resources/in ground] (kilogram) | 0.246 | 0.00794 | -96.8% | +0.238 |
| Sulfate Ion [water] (kilogram) | 0.15 | 0.00022 | -99.9% | +0.15 |
| Clay [soil] (kilogram) | 0.128 | 0.0437 | -65.9% | +0.0843 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.111 | 0.107 | -3.0% | +0.00332 |
| Silicon [Emissions/Emissions to water] (kilogram) | 0.0991 | 0.0947 | -4.4% | +0.00438 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.0428 | 0.0577 | +34.8% | -0.0149 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0361 | 0.0356 | -1.5% | +0.000556 |
| Iron [Resources/Resources from ground] (kilogram) | 0.0331 | 0.0183 | -44.8% | +0.0148 |
| Sulfur Dioxide [Emissions/Emissions to air] (kilogram) | 0.0291 | 0.0184 | -36.9% | +0.0107 |
| calcium [Emissions/Emissions to water] (kilogram) | 0.0275 | 0.0377 | +36.8% | -0.0101 |
| titanium [Emissions/Emissions to water] (kilogram) | 0.02 | 0.02 | +0.0% | -7.17e-06 |
| Methane (fossil) [Emissions/Emissions to air] (kilogram) | 0.0151 | 0.00564 | -62.7% | +0.00949 |
| magnesium [Emissions/Emissions to water] (kilogram) | 0.011 | 0.0105 | -4.5% | +0.000499 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.0103 | 0.0234 | +127.4% | -0.0131 |

### kilo Becquerel (135 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 366 | 400 | +9.3% | -34.2 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 198 | 150 | -24.5% | +48.6 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 8.75 | 3.71 | -57.6% | +5.05 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 7.98 | 6.03 | -24.5% | +1.95 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.856 | 1.5 | +75.3% | -0.645 |

### square meter (34 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| From Forest [Land use/Land transformation] (square meter) | 0.000626 | 0.0016 | +155.1% | -0.00097 |
| To Mineral Extraction Site [Land use/Land transformation] (square meter) | 0.000565 | 0.0031 | +449.2% | -0.00254 |
| To Dump Site [Land use/Land transformation] (square meter) | 0.000517 | 0.000247 | -52.2% | +0.00027 |
| From Forest, Extensive [Land use/Land transformation] (square meter) | 0.000462 | 1.84e-06 | -99.6% | +0.00046 |
| To Forest, Intensive [Land use/Land transformation] (square meter) | 0.000458 | 0.000628 | +37.1% | -0.00017 |

### cubic meter (20 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 7.55 | 6.72 | -11.1% | +0.835 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 7.39 | 6.56 | -11.3% | +0.832 |
| Water [Resources/Resources from water] (cubic meter) | 0.111 | 0.124 | +11.4% | -0.0126 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 0.0478 | 0.0186 | -61.1% | +0.0292 |
| river water [Resources/Resources from water] (cubic meter) | 0.0058 | 0.0039 | -32.7% | +0.0019 |

### megajoule (20 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Natural Gas [Resources/Resources from ground] (megajoule) | 53.4 | 27.9 | -47.7% | +25.4 |
| Waste Heat [air] (megajoule) | 47.8 | 67.3 | +40.7% | -19.5 |
| Crude Oil [Resources/Resources from ground] (megajoule) | 10.1 | 14.4 | +41.9% | -4.24 |
| Waste Heat [air] (megajoule) | 8.98 | 7.73 | -14.0% | +1.25 |
| Waste Heat [air] (megajoule) | 7.13 | 0.635 | -91.1% | +6.5 |

### square meter-year (14 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.0591 | 0.0544 | -7.8% | +0.00463 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.00578 | 0.00669 | +15.8% | -0.000912 |
| Traffic Area, Road Network [Land use/Land occupation] (square meter-year) | 0.00487 | 0.004 | -18.0% | +0.000877 |
| Dump Site [Land use/Land occupation] (square meter-year) | 0.00392 | 0.00493 | +25.8% | -0.00101 |
| Water Bodies [land use] (square meter-year) | 0.00291 | 0.00494 | +69.9% | -0.00203 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.0168 | 0.0458 | +172.5% | -0.029 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Sulfate Ion [water] (kilogram) | 0.00802 | 0.207 | +2477.5% |
| Sodium [water] (kilogram) | 0.00138 | 0.0136 | +887.6% |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.00218 | 0.0195 | +793.5% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00376 | 0.0143 | +280.3% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0039 | 0.012 | +208.9% |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.0103 | 0.0234 | +127.4% |
| Sulfate Ion [water] (kilogram) | 0.15 | 0.00022 | -99.9% |
| Particles (PM10) [Emissions/Emissions to air] (kilogram) | 0.00702 | 0.000159 | -97.7% |
| Sodium chloride [resources/in ground] (kilogram) | 0.246 | 0.00794 | -96.8% |
| Barite [resources/in ground] (kilogram) | 0.00326 | 0.00637 | +95.6% |

## Structural checks

- ✓ 7 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 5.5 kg technosphere + 0 kg resources per 1 kg product (informational)
- ✓ all inputs resolved

residual: 546 flows under-explained, 1237 over-explained (negative residual)

## Evidence

- 2007 - LCI chemicals - Althaus.pdf — pages 845-847 -> report-p845-847.txt report sha256 68e0839ffea919f9…, text sha256 e1b3f9c29c3269b8…
