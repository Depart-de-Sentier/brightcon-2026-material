# Check: Electricity, low voltage, production from hard coal, at grid (02fd8be4-a33b-3cb5-a1ca-40bcbddb251a)

target `bafu-2026` vs explicit model `02fd8be4-a33b-3cb5-a1ca-40bcbddb251a-bench-disagg` and hybrid `02fd8be4-a33b-3cb5-a1ca-40bcbddb251a-bench-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: Tab. 4.25 'Sachbilanzdaten für das Modul "Strom, Hochspannung / Mittelspannung / Niederspannung, ab Netz (CH)"', column 'electricity, low voltage, production CH, at grid', per 1 kWh; allocation: none stated. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 1/50 within ±10 %, median |Δ| 72.3%
- kilogram mass covered within ±10 %: 0.0% of the target's total kg mass
- of the 1785 flows of the target, 1668 are determined by the solve (117 are round-off and are not scored; see lci.determined_flows)
- 66 of those 1668 within ±10 % (4%), median |Δ| 77.8%, 0 missing from the model, 0 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 67 | 4% |
| 10–20 % | 58 | 3% |
| 20–50 % | 342 | 19% |
| 50–100 % | 597 | 33% |
| > 100 % | 721 | 40% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1469 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.984 | 0.0512 | -94.8% | +0.933 |
| Gravel [soil] (kilogram) | 0.108 | 0.061 | -43.7% | +0.0474 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.0435 | 0.0117 | -73.0% | +0.0318 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0246 | 0.0297 | +21.0% | -0.00515 |
| Calcite [resources/in ground] (kilogram) | 0.0195 | 0.00846 | -56.6% | +0.0111 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0176 | 0.0112 | -36.2% | +0.00638 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.0176 | 0.0368 | +109.9% | -0.0193 |
| calcium [Emissions/Emissions to water] (kilogram) | 0.0119 | 0.00684 | -42.7% | +0.00509 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.01 | 0.0261 | +160.6% | -0.0161 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.00668 | 0.000589 | -91.2% | +0.00609 |
| Silicon [Emissions/Emissions to water] (kilogram) | 0.00597 | 0.00173 | -71.0% | +0.00424 |
| Sodium [emissions to water/groundwater, long-term] (kilogram) | 0.00589 | 0.00121 | -79.4% | +0.00467 |
| magnesium [Emissions/Emissions to water] (kilogram) | 0.00566 | 0.00188 | -66.8% | +0.00378 |
| Platinum [air] (kilogram) | 0.00519 | 0.0038 | -26.8% | +0.00139 |
| Potassium [emissions to water/groundwater, long-term] (kilogram) | 0.00397 | 0.00137 | -65.5% | +0.0026 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00345 | 0.0213 | +518.8% | -0.0179 |
| Methane (fossil) [Emissions/Emissions to air] (kilogram) | 0.00328 | 0.000126 | -96.2% | +0.00315 |
| Iron [Resources/Resources from ground] (kilogram) | 0.00218 | 0.0013 | -40.3% | +0.000881 |
| Phosphate [Emissions/Emissions to water] (kilogram) | 0.00165 | 0.000341 | -79.4% | +0.00131 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00154 | 0.00284 | +84.3% | -0.0013 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 29.5 | 467 | +1485.0% | -438 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 10.4 | 159 | +1423.8% | -148 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.419 | 6.39 | +1423.6% | -5.97 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.28 | 4.11 | +1365.5% | -3.83 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.16 | 0.983 | +515.6% | -0.823 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 0.000328 | 8.86e-05 | -73.0% | +0.000239 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 0.000233 | 6.22e-05 | -73.3% | +0.00017 |
| To Forest, Intensive [Land use/Land transformation] (square meter) | 0.000151 | 0.000331 | +119.1% | -0.00018 |
| From Forest, Intensive [Land use/Land transformation] (square meter) | 0.00015 | 0.00033 | +120.3% | -0.00018 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 0.000147 | 3.51e-05 | -76.2% | +0.000112 |

### megajoule (28 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Hard Coal [Resources/Resources from ground] (megajoule) | 9.53 | 0.16 | -98.3% | +9.37 |
| Waste Heat [air] (megajoule) | 6.16 | 0.675 | -89.0% | +5.48 |
| Waste Heat [water] (megajoule) | 1.6 | 0.0732 | -95.4% | +1.53 |
| Waste Heat [air] (megajoule) | 0.612 | 3.92 | +540.4% | -3.31 |
| Waste Heat [air] (megajoule) | 0.526 | 0.281 | -46.5% | +0.245 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.0127 | 0.0298 | +134.5% | -0.0171 |
| Dump Site [Land use/Land occupation] (square meter-year) | 0.00347 | 0.000313 | -91.0% | +0.00316 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.00168 | 0.000411 | -75.6% | +0.00127 |
| Traffic Area, Rail/road Embankment [Land use/Land occupation] (square meter-year) | 0.00143 | 0.000402 | -71.9% | +0.00103 |
| Traffic Area, Rail Network [Land use/Land occupation] (square meter-year) | 0.00139 | 2.42e-05 | -98.3% | +0.00137 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 0.627 | 9.41 | +1400.5% | -8.78 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 0.591 | 9.4 | +1490.1% | -8.81 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 0.0363 | 0.00167 | -95.4% | +0.0346 |
| Water, salt, ocean [resources/in water] (cubic meter) | 0.0128 | 0.0432 | +237.0% | -0.0304 |
| Water [water] (cubic meter) | 0.0128 | 0.0427 | +234.0% | -0.0299 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | -2.2e-21 | -1.14e-20 | +415.4% | +9.15e-21 |
| Uranium alpha [emissions to water/lake] (Becquerel) | -1.03e-21 | -5.32e-21 | +415.4% | +4.29e-21 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | -1.88e-22 | -9.67e-22 | +415.4% | +7.79e-22 |
| Thorium-232 [emissions to water/river] (Becquerel) | -2.23e-24 | -1.15e-23 | +415.4% | +9.25e-24 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | -6.58e-25 | -3.39e-24 | +415.4% | +2.73e-24 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.00731 | 0.0019 | -74.0% | +0.00541 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 9.83e-06 | 3.57e-05 | +263.4% | -2.59e-05 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 1.72 | 0.0301 | -98.2% | +1.69 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 1.76e-07 | 6.83e-07 | +289.4% | -5.08e-07 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | -6.6e-19 | -9.81e-19 | +48.6% | +3.21e-19 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | -2.08e-22 | -1.07e-21 | +415.4% | +8.65e-22 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.00371 | 0.0388 | +948.0% | -0.0351 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 3.02e-06 | 1.16e-05 | +286.2% | -8.63e-06 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00345 | 0.0213 | +518.8% |
| Copper [Resources/Resources from ground] (kilogram) | 0.000359 | 0.00103 | +185.5% |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.01 | 0.0261 | +160.6% |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.0176 | 0.0368 | +109.9% |
| Particles (> PM10) [air] (kilogram) | 0.00135 | 4.2e-05 | -96.9% |
| Methane (fossil) [Emissions/Emissions to air] (kilogram) | 0.00328 | 0.000126 | -96.2% |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.984 | 0.0512 | -94.8% |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.00668 | 0.000589 | -91.2% |
| Sulfur Dioxide [Emissions/Emissions to air] (kilogram) | 0.000395 | 3.84e-05 | -90.3% |
| Nitrogen Oxides [Emissions/Emissions to air] (kilogram) | 0.000585 | 6.35e-05 | -89.1% |

## Structural checks

- ✓ 3 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 1.1 kg technosphere + 0 kg resources per 1 kWh product (informational)
- ✓ all inputs resolved

residual: 786 flows under-explained, 999 over-explained (negative residual)

## Evidence

- 2007 - Electricy mix and grid - Frischknecht.pdf — pages 114-116 -> report-p114-116.txt report sha256 36348918d6707bf8…, text sha256 b55b40673db59d41…
