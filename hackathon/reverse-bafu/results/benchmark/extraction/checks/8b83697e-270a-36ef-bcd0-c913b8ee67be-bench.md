# Check: Electricity, hydropower, net, at reservoir power plant (8b83697e-270a-36ef-bcd0-c913b8ee67be)

target `bafu-2026` vs explicit model `8b83697e-270a-36ef-bcd0-c913b8ee67be-bench-disagg` and hybrid `8b83697e-270a-36ef-bcd0-c913b8ee67be-bench-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: Tab. 4.1 'Unit process raw data of electricity, hydropower, at reservoir power plant/CH and electricity, hydropower, net, at reservoir power plant/CH', SECOND column ('net, at reservoir power plant'), per 1 kWh; allocation: none stated. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 49/50 within ±10 %, median |Δ| 0.1%
- kilogram mass covered within ±10 %: 98.3% of the target's total kg mass
- of the 1787 flows of the target, 1668 are determined by the solve (119 are round-off and are not scored; see lci.determined_flows)
- 1648 of those 1668 within ±10 % (99%), median |Δ| 0.1%, 0 missing from the model, 1 extra
- hybrid vs target: 2 flows differ

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 1658 | 93% |
| 10–20 % | 0 | 0% |
| 20–50 % | 65 | 4% |
| 50–100 % | 33 | 2% |
| > 100 % | 31 | 2% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1471 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Gravel [soil] (kilogram) | 0.0333 | 0.0333 | +0.1% | -2.97e-05 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.0315 | 0.0315 | +0.1% | -2.81e-05 |
| Calcite [resources/in ground] (kilogram) | 0.00438 | 0.00438 | +0.1% | -3.91e-06 |
| calcium [Emissions/Emissions to water] (kilogram) | 0.00428 | 0.00428 | +0.1% | -3.82e-06 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.00287 | 0.00287 | +0.1% | -2.56e-06 |
| Carbon Dioxide (land Use Change) [Emissions/Emissions to air] (kilogram) | 0.00136 | 7.7e-07 | -99.9% | +0.00136 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.000455 | 0.000456 | +0.1% | -4.07e-07 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.000427 | 0.000427 | +0.1% | -3.81e-07 |
| Clay [soil] (kilogram) | 0.000261 | 0.000261 | +0.1% | -2.33e-07 |
| Sodium [emissions to water/groundwater, long-term] (kilogram) | 0.000258 | 0.000259 | +0.1% | -2.31e-07 |
| Silicon [Emissions/Emissions to water] (kilogram) | 0.00023 | 0.00023 | +0.1% | -2.06e-07 |
| Iron [Resources/Resources from ground] (kilogram) | 0.000208 | 0.000208 | +0.1% | -1.86e-07 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.000183 | 0.000183 | +0.1% | -1.63e-07 |
| COD, Chemical Oxygen Demand [emissions to water/groundwater, long-term] (kilogram) | 0.000175 | 0.000175 | +0.1% | -1.56e-07 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.000173 | 0.000173 | +0.1% | -1.55e-07 |
| magnesium [Emissions/Emissions to water] (kilogram) | 0.000136 | 0.000137 | +0.1% | -1.22e-07 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 7.55e-05 | 7.56e-05 | +0.1% | -6.74e-08 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 5.59e-05 | 5.6e-05 | +0.1% | -4.99e-08 |
| TOC, Total Organic Carbon [emissions to water/groundwater, long-term] (kilogram) | 3.98e-05 | 3.98e-05 | +0.1% | -3.55e-08 |
| DOC, Dissolved Organic Carbon [emissions to water/groundwater, long-term] (kilogram) | 3.98e-05 | 3.98e-05 | +0.1% | -3.55e-08 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.682 | 0.683 | +0.1% | -0.000609 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 0.233 | 0.233 | +0.1% | -0.000208 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.00938 | 0.00939 | +0.1% | -8.38e-06 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.00606 | 0.00606 | +0.1% | -5.41e-06 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.00205 | 0.00205 | +0.1% | -1.83e-06 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| From Unspecified [Land use/Land transformation] (square meter) | 2.58e-05 | 1.39e-06 | -94.6% | +2.44e-05 |
| To Water Bodies [land use] (square meter) | 2.44e-05 | 2.21e-07 | -99.1% | +2.41e-05 |
| From Pasture/meadow [Land use/Land transformation] (square meter) | 2.11e-06 | 2.11e-06 | +0.1% | -1.88e-09 |
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 2.07e-06 | 2.07e-06 | +0.1% | -1.84e-09 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 1.54e-06 | 1.54e-06 | +0.1% | -1.37e-09 |

### megajoule (28 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Energy, Potential (in Hydropower Reservoir), Converted [natural resource] (megajoule) | 3.79 | 3.79 | +0.0% | -2.87e-06 |
| Waste Heat [air] (megajoule) | 0.17 | 0.0117 | -93.1% | +0.158 |
| Waste Heat [air] (megajoule) | 0.017 | 0.017 | +0.1% | -1.52e-05 |
| Uranium [Resources/Resources from ground] (megajoule) | 0.0092 | 0.00921 | +0.1% | -8.22e-06 |
| Crude Oil [Resources/Resources from ground] (megajoule) | 0.0088 | 0.00881 | +0.1% | -7.85e-06 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water Bodies [land use] (square meter-year) | 0.00362 | 4.88e-06 | -99.9% | +0.00362 |
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 6.19e-05 | 6.19e-05 | +0.1% | -5.53e-08 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 4.51e-05 | 8.93e-06 | -80.2% | +3.62e-05 |
| Dump Site [Land use/Land occupation] (square meter-year) | 2.55e-05 | 2.56e-05 | +0.1% | -2.28e-08 |
| Forest [Land use/Land occupation] (square meter-year) | 1.4e-05 | 1.41e-05 | +0.1% | -1.25e-08 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 1.43 | 0.0229 | -98.4% | +1.4 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 1.43 | 0.0229 | -98.4% | +1.4 |
| Water [air] (cubic meter) | 0.00175 | 1.75 | +99735.2% | -1.75 |
| Water, salt, ocean [resources/in water] (cubic meter) | 0.000309 | 0.000309 | +0.1% | -2.76e-07 |
| Water [water] (cubic meter) | 0.000308 | 0.000308 | +0.1% | -2.75e-07 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | 3.66e-21 | -1.42e-21 | -138.7% | +5.08e-21 |
| Uranium alpha [emissions to water/lake] (Becquerel) | 1.72e-21 | -6.65e-22 | -138.7% | +2.38e-21 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | 3.12e-22 | -1.21e-22 | -138.7% | +4.33e-22 |
| Thorium-232 [emissions to water/river] (Becquerel) | 3.71e-24 | -1.44e-24 | -138.7% | +5.14e-24 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | 1.1e-24 | -4.24e-25 | -138.7% | +1.52e-24 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.000585 | 0.000586 | +0.1% | -5.23e-07 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 4.61e-07 | 4.62e-07 | +0.1% | -4.12e-10 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 0.00168 | 0.00169 | +0.1% | -1.5e-06 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 3.7e-09 | 3.71e-09 | +0.1% | -3.31e-12 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | 7.69e-20 | -1.02e-19 | -232.2% | +1.79e-19 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | 3.47e-22 | -1.34e-22 | -138.7% | +4.81e-22 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.164 | 0.164 | -0.1% | +0.000183 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 6.86e-08 | 6.87e-08 | +0.1% | -6.13e-11 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Carbon Dioxide (land Use Change) [Emissions/Emissions to air] (kilogram) | 0.00136 | 7.7e-07 | -99.9% |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.0315 | 0.0315 | +0.1% |
| Organic carbon, placed in landfill [resources/in ground] (kilogram) | 3.89e-05 | 3.89e-05 | +0.1% |
| calcium [Emissions/Emissions to water] (kilogram) | 0.00428 | 0.00428 | +0.1% |
| Gravel [soil] (kilogram) | 0.0333 | 0.0333 | +0.1% |
| COD, Chemical Oxygen Demand [emissions to water/groundwater, long-term] (kilogram) | 0.000175 | 0.000175 | +0.1% |
| Calcite [resources/in ground] (kilogram) | 0.00438 | 0.00438 | +0.1% |
| BOD5, Biological Oxygen Demand [emissions to water/groundwater, long-term] (kilogram) | 2.46e-05 | 2.46e-05 | +0.1% |
| DOC, Dissolved Organic Carbon [emissions to water/groundwater, long-term] (kilogram) | 3.98e-05 | 3.98e-05 | +0.1% |
| TOC, Total Organic Carbon [emissions to water/groundwater, long-term] (kilogram) | 3.98e-05 | 3.98e-05 | +0.1% |

## Structural checks

- ✓ 3 explicit input(s) over 1 node(s)
- ✗ inputs are individual power plants: ['Reservoir hydropower plant']
- ✓ no dependency on another system process
- ✓ mass in: 3.27e-08 kg technosphere + 0 kg resources per 1 kWh product (informational)
- ✓ all inputs resolved

residual: 116 flows under-explained, 1672 over-explained (negative residual)

## Evidence

- 2012 - LCI hydroelectric power generation - Flury.pdf — pages 37-38 -> report-p37-38.txt report sha256 0f624a5445034749…, text sha256 9cef332a3a1e6258…
