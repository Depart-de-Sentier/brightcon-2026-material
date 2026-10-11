# Check: Burnt shale, at plant (d8ec4be3-c410-3806-98f5-a2ec5a284fee)

target `bafu-2026` vs explicit model `d8ec4be3-c410-3806-98f5-a2ec5a284fee-draft-disagg` and hybrid `d8ec4be3-c410-3806-98f5-a2ec5a284fee-draft-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: per tonne of burnt shale (GÖS), 71.30 % economic-allocation column of Tab. 3.9; transport from Tab. 3.10; allocation: economic allocation between the co-products electricity (28.7 %) and burnt shale (71.3 %) per Werner (2018); the 71.30 % column is used; 22 of 22 inputs carry a printed amount, 0 a printed range, 0 no number in the report. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 3/50 within ±10 %, median |Δ| 79.2%
- kilogram mass covered within ±10 %: 30.4% of the target's total kg mass
- of the 1326 flows of the target, 1326 are determined by the solve (0 are round-off and are not scored; see lci.determined_flows)
- 81 of those 1326 within ±10 % (6%), median |Δ| 144.5%, 0 missing from the model, 445 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 81 | 6% |
| 10–20 % | 57 | 4% |
| 20–50 % | 198 | 15% |
| 50–100 % | 277 | 21% |
| > 100 % | 713 | 54% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1084 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Shale [soil] (kilogram) | 0.963 | 7.14e-10 | -100.0% | +0.963 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.424 | 0.428 | +1.0% | -0.00402 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.00204 | 0.0116 | +469.3% | -0.00957 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.00169 | 0.012 | +612.9% | -0.0103 |
| Gravel [soil] (kilogram) | 0.00084 | 0.00195 | +132.3% | -0.00111 |
| Nitrogen Oxides [Emissions/Emissions to air] (kilogram) | 0.000525 | 2.98e-05 | -94.3% | +0.000495 |
| Sulfur Dioxide [Emissions/Emissions to air] (kilogram) | 0.000454 | 0.000454 | +0.0% | -3.57e-08 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.000445 | 0.000564 | +26.7% | -0.000119 |
| Carbon Monoxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.000415 | 0.000423 | +1.9% | -7.91e-06 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.000353 | 0.000136 | -61.5% | +0.000217 |
| Calcite [resources/in ground] (kilogram) | 0.000177 | 0.000657 | +272.0% | -0.00048 |
| Sodium [water] (kilogram) | 0.000169 | 1.86e-05 | -89.0% | +0.000151 |
| Sodium chloride [resources/in ground] (kilogram) | 0.000158 | 0.000197 | +24.6% | -3.89e-05 |
| Clay [soil] (kilogram) | 0.000146 | 3.42e-05 | -76.7% | +0.000112 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.000119 | 0.00275 | +2207.2% | -0.00263 |
| Iron [Resources/Resources from ground] (kilogram) | 0.000119 | 0.00016 | +34.0% | -4.06e-05 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.000117 | 8.37e-05 | -28.4% | +3.32e-05 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.000104 | 0.00128 | +1124.3% | -0.00117 |
| calcium [Emissions/Emissions to water] (kilogram) | 9.31e-05 | 0.000731 | +684.5% | -0.000638 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 8.32e-05 | 0.00233 | +2696.6% | -0.00224 |

### kilo Becquerel (138 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.413 | 3.46 | +737.4% | -3.04 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 0.217 | 1.08 | +398.9% | -0.864 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.00965 | 0.0319 | +230.9% | -0.0223 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.00871 | 0.0435 | +399.3% | -0.0348 |
| Radium-226 [Emissions/Emissions to water] (kilo Becquerel) | 0.00198 | 0.000617 | -68.8% | +0.00136 |

### square meter (37 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 1.31e-05 | 1.13e-05 | -14.2% | +1.86e-06 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 9.31e-06 | 7.67e-06 | -17.6% | +1.64e-06 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 6.53e-06 | 5.62e-06 | -13.9% | +9.08e-07 |
| From Arable, Non-irrigated [Land use/Land transformation] (square meter) | 6.31e-06 | 5.39e-06 | -14.5% | +9.14e-07 |
| From Pasture/meadow [Land use/Land transformation] (square meter) | 3.86e-06 | 5.2e-06 | +34.7% | -1.34e-06 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 0.0108 | 0.176 | +1522.6% | -0.165 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 0.0103 | 0.175 | +1602.1% | -0.164 |
| river water [Resources/Resources from water] (cubic meter) | 0.000263 | 0.000316 | +20.1% | -5.29e-05 |
| Ground Water [Resources/Resources from water] (cubic meter) | 0.000211 | 0.000254 | +20.1% | -4.26e-05 |
| lake water [Resources/Resources from water] (cubic meter) | 0.000103 | 0.000103 | +0.6% | -6.62e-07 |

### megajoule (21 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Crude Oil [Resources/Resources from ground] (megajoule) | 3.92 | 0.0374 | -99.0% | +3.88 |
| Waste Heat [air] (megajoule) | 0.354 | 0.129 | -63.5% | +0.225 |
| Waste Heat [water] (megajoule) | 0.113 | 0.0231 | -79.6% | +0.09 |
| Natural Gas [Resources/Resources from ground] (megajoule) | 0.0293 | 0.101 | +244.5% | -0.0717 |
| Waste Heat [air] (megajoule) | 0.0267 | 0.178 | +567.1% | -0.151 |

### square meter-year (17 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest [Land use/Land occupation] (square meter-year) | 8.56e-05 | 0.000207 | +141.4% | -0.000121 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 6.31e-05 | 8.68e-05 | +37.5% | -2.37e-05 |
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 5.7e-05 | 0.00264 | +4531.2% | -0.00258 |
| Traffic Area, Road Network [Land use/Land occupation] (square meter-year) | 1.98e-05 | 5.98e-06 | -69.7% | +1.38e-05 |
| Arable, Non-irrigated, Intensive [Land use/Land occupation] (square meter-year) | 1.2e-05 | 9.9e-06 | -17.6% | +2.12e-06 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.00152 | 0.00152 | +0.3% | -5.27e-06 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 1.67e-06 | 2.8e-06 | +67.2% | -1.13e-06 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 0.00104 | 0.0121 | +1059.2% | -0.011 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 2.09e-08 | 7.85e-08 | +276.6% | -5.77e-08 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 9.42e-05 | 0.00158 | +1582.9% | -0.00149 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 1.26e-07 | 1.23e-06 | +873.9% | -1.1e-06 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 1.53e-05 | 0.00275 | +17840.4% |
| Platinum [air] (kilogram) | 3.85e-05 | 0.00168 | +4263.3% |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 8.32e-05 | 0.00233 | +2696.6% |
| Potassium [emissions to water/groundwater, long-term] (kilogram) | 6.66e-06 | 0.00017 | +2452.9% |
| magnesium [Emissions/Emissions to water] (kilogram) | 1.28e-05 | 0.0003 | +2244.2% |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.000119 | 0.00275 | +2207.2% |
| Sodium [emissions to water/groundwater, long-term] (kilogram) | 1.24e-05 | 0.000287 | +2203.8% |
| Sulfate Ion [water] (kilogram) | 5.68e-06 | 0.000116 | +1932.8% |
| Silicon [Emissions/Emissions to water] (kilogram) | 2.5e-05 | 0.000445 | +1680.5% |
| aluminium [Emissions/Emissions to water] (kilogram) | 3.4e-06 | 4.54e-05 | +1236.8% |

## Structural checks

- ✓ 22 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 0.568 kg technosphere + 0 kg resources per 1 kg product (informational)
- ✓ all inputs resolved

residual: 438 flows under-explained, 1333 over-explained (negative residual)

## Evidence

- 2020 - LCA selected types of concrete - Tschuemperlin.pdf — pages 19-21 -> report-p19-21.txt report sha256 83e2e7ea46d35899…, text sha256 8f862e61970465b0…
