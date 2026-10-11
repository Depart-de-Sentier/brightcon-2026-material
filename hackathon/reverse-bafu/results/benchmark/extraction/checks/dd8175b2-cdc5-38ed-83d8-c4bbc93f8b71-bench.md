# Check: Grain maize IP, at feed mill (dd8175b2-cdc5-38ed-83d8-c4bbc93f8b71)

target `bafu-2026` vs explicit model `dd8175b2-cdc5-38ed-83d8-c4bbc93f8b71-bench-disagg` and hybrid `dd8175b2-cdc5-38ed-83d8-c4bbc93f8b71-bench-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: Chapter 12 'Feedstuffs': Tab. 12.2 for the production-process shares, Tab. 12.3 (Maize row) for the transport distances and section 12.2.3 for the processing energy (35 kWh electricity and 4 m3 natural gas per tonne of feedstuff). Per 1 kg of feedstuff at the feed mill.; allocation: none stated. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 36/50 within ±10 %, median |Δ| 2.6%
- kilogram mass covered within ±10 %: 97.6% of the target's total kg mass
- of the 1786 flows of the target, 1668 are determined by the solve (118 are round-off and are not scored; see lci.determined_flows)
- 1292 of those 1668 within ±10 % (77%), median |Δ| 1.9%, 0 missing from the model, 0 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 1295 | 73% |
| 10–20 % | 180 | 10% |
| 20–50 % | 153 | 9% |
| 50–100 % | 56 | 3% |
| > 100 % | 102 | 6% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1471 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 1.39 | 1.39 | -0.1% | +0.0012 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.157 | 0.157 | -0.1% | +0.000126 |
| Gravel [soil] (kilogram) | 0.0696 | 0.0651 | -6.4% | +0.00448 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0614 | 0.0613 | -0.3% | +0.000164 |
| Nitrate [Emissions/Emissions to water] (kilogram) | 0.0469 | 0.0469 | -0.0% | +1.04e-05 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0417 | 0.0393 | -5.9% | +0.00246 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.0234 | 0.0188 | -19.6% | +0.00458 |
| Chemically polluted water [emissions to water/river] (kilogram) | 0.0101 | 0.01 | -1.4% | +0.000138 |
| Calcite [resources/in ground] (kilogram) | 0.00935 | 0.00875 | -6.4% | +0.000599 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00744 | 0.00638 | -14.3% | +0.00106 |
| Iron [Resources/Resources from ground] (kilogram) | 0.00667 | 0.00668 | +0.1% | -8.92e-06 |
| Sulfate Ion [water] (kilogram) | 0.00435 | 0.00434 | -0.2% | +9.75e-06 |
| Clay [soil] (kilogram) | 0.00411 | 0.00202 | -50.8% | +0.00208 |
| calcium [Emissions/Emissions to water] (kilogram) | 0.0037 | 0.003 | -19.0% | +0.000702 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.00258 | 0.00223 | -13.9% | +0.000358 |
| Calcium [Emissions/Emissions to water] (kilogram) | 0.00238 | 0.00238 | -0.3% | +6.98e-06 |
| Ammonia [Emissions/Emissions to air] (kilogram) | 0.002 | 0.002 | -0.0% | +5.66e-07 |
| Platinum [air] (kilogram) | 0.00172 | 0.0017 | -1.2% | +2.06e-05 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00165 | 0.00153 | -7.4% | +0.000122 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.00163 | 0.0016 | -1.9% | +3.07e-05 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 41.5 | 41.2 | -0.8% | +0.323 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 14.1 | 14 | -0.8% | +0.115 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.569 | 0.564 | -0.8% | +0.00461 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.379 | 0.376 | -0.8% | +0.00298 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.246 | 0.242 | -1.6% | +0.00382 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 2.18 | 2.18 | -0.0% | +0.000195 |
| From Arable, Non-irrigated [Land use/Land transformation] (square meter) | 2.18 | 2.18 | -0.0% | +0.000186 |
| From Pasture/meadow [Land use/Land transformation] (square meter) | 0.00289 | 0.00274 | -5.1% | +0.000148 |
| From Pasture/meadow, Intensive [Land use/Land transformation] (square meter) | 0.00181 | 0.0018 | -0.1% | +1.87e-06 |
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 0.000831 | 0.000321 | -61.4% | +0.00051 |

### megajoule (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Energy, gross calorific value, in biomass [resources/biotic] (megajoule) | 16 | 16 | -0.1% | +0.0145 |
| Waste Heat [air] (megajoule) | 6.29 | 6.14 | -2.3% | +0.145 |
| Crude Oil [Resources/Resources from ground] (megajoule) | 2.74 | 2.72 | -0.9% | +0.0236 |
| Waste Heat [water] (megajoule) | 1.25 | 1.25 | -0.4% | +0.00442 |
| Waste Heat [air] (megajoule) | 1.18 | 1.18 | -0.4% | +0.00456 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Arable, Non-irrigated [Land use/Land occupation] (square meter-year) | 1.32 | 1.32 | -0.0% | +9.92e-05 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.0193 | 0.0193 | -0.3% | +6.7e-05 |
| Forest [Land use/Land occupation] (square meter-year) | 0.00685 | 0.00547 | -20.2% | +0.00138 |
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.00394 | 0.00385 | -2.3% | +8.96e-05 |
| Construction Site [Land use/Land occupation] (square meter-year) | 0.00118 | 0.00117 | -0.3% | +3.41e-06 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 0.887 | 0.879 | -0.9% | +0.00823 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 0.885 | 0.876 | -0.9% | +0.00813 |
| Water, salt, ocean [resources/in water] (cubic meter) | 0.0601 | 0.0596 | -0.9% | +0.000526 |
| Water [water] (cubic meter) | 0.0601 | 0.0595 | -0.9% | +0.000524 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 0.00112 | 0.00111 | -1.4% | +1.6e-05 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | -1.5e-17 | -2.58e-16 | +1620.2% | +2.43e-16 |
| Uranium alpha [emissions to water/lake] (Becquerel) | -7.03e-18 | -1.21e-16 | +1620.2% | +1.14e-16 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | -1.28e-18 | -2.2e-17 | +1620.2% | +2.07e-17 |
| Thorium-232 [emissions to water/river] (Becquerel) | -1.52e-20 | -2.61e-19 | +1620.2% | +2.46e-19 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | -4.49e-21 | -7.72e-20 | +1620.2% | +7.27e-20 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.0379 | 0.0357 | -5.7% | +0.00215 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 8.2e-05 | 6.34e-05 | -22.7% | +1.86e-05 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 0.0675 | 0.0676 | +0.2% | -0.000145 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 1.78e-06 | 1.46e-06 | -18.3% | +3.26e-07 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | -5.28e-16 | -9.07e-15 | +1616.1% | +8.54e-15 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | -1.42e-18 | -2.44e-17 | +1620.2% | +2.3e-17 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.00405 | 0.00398 | -1.7% | +6.83e-05 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 1.42e-05 | 1.41e-05 | -0.9% | +1.22e-07 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Clay [soil] (kilogram) | 0.00411 | 0.00202 | -50.8% |
| Copper [Resources/Resources from ground] (kilogram) | 0.000175 | 0.000126 | -28.0% |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.0234 | 0.0188 | -19.6% |
| Potassium chloride [resources/in ground] (kilogram) | 0.000165 | 0.000133 | -19.4% |
| calcium [Emissions/Emissions to water] (kilogram) | 0.0037 | 0.003 | -19.0% |
| Sulfate Ion [water] (kilogram) | 0.000224 | 0.000183 | -18.5% |
| Aluminium [Resources/Resources from ground] (kilogram) | 0.000245 | 0.000204 | -16.6% |
| magnesium [Emissions/Emissions to water] (kilogram) | 0.00045 | 0.000377 | -16.4% |
| chloride [Emissions/Emissions to water] (kilogram) | 0.0002 | 0.00017 | -15.3% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00744 | 0.00638 | -14.3% |

## Structural checks

- ✓ 5 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 1.03 kg technosphere + 0 kg resources per 1 kg product (informational)
- ✓ all inputs resolved

residual: 1475 flows under-explained, 311 over-explained (negative residual)

## Evidence

- 2007 - LCI agricultural prod. systems - Nemecek.pdf — pages 117-120 -> report-p117-120.txt report sha256 d01758706ebea797…, text sha256 06a09ba1811e375b…
