# Check: High pressure hydrogen Type IV storage tank production (ffb46227-8cee-3dfd-b9a4-fc5a0b38f7a3)

target `bafu-2026` vs explicit model `ffb46227-8cee-3dfd-b9a4-fc5a0b38f7a3-bench-disagg` and hybrid `ffb46227-8cee-3dfd-b9a4-fc5a0b38f7a3-bench-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: Table 36 'Life cycle inventories to produce a high-pressure Type IV hydrogen tank. Storage capacity of 10 kg', column 'high pressure hydrogen storage tank/GLO U', per 1 p; allocation: none stated. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 50/50 within ±10 %, median |Δ| 0.0%
- kilogram mass covered within ±10 %: 100.0% of the target's total kg mass
- of the 1787 flows of the target, 1667 are determined by the solve (120 are round-off and are not scored; see lci.determined_flows)
- 1654 of those 1667 within ±10 % (99%), median |Δ| 0.0%, 0 missing from the model, 0 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 1668 | 93% |
| 10–20 % | 16 | 1% |
| 20–50 % | 6 | 0% |
| 50–100 % | 23 | 1% |
| > 100 % | 74 | 4% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1472 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 2.79e+03 | 2.79e+03 | +0.0% | -1.34 |
| Nitrogen [air] (kilogram) | 2.63e+03 | 2.63e+03 | -0.0% | +5.47e-05 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 731 | 730 | -0.2% | +1.45 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 627 | 628 | +0.0% | -0.177 |
| Gravel [soil] (kilogram) | 370 | 370 | +0.0% | -0.138 |
| Platinum [air] (kilogram) | 217 | 217 | -0.1% | +0.123 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 180 | 180 | -0.0% | +0.0562 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 137 | 137 | +0.1% | -0.0828 |
| Chemically polluted water [emissions to water/river] (kilogram) | 113 | 113 | +0.0% | -0.0263 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 102 | 102 | +0.1% | -0.13 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 95.2 | 96.6 | +1.5% | -1.46 |
| Calcite [resources/in ground] (kilogram) | 82.2 | 82.1 | -0.1% | +0.0931 |
| Sodium chloride [resources/in ground] (kilogram) | 75 | 75 | -0.0% | +0.00064 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 61.8 | 61.8 | -0.1% | +0.0385 |
| Chloride [Emissions/Emissions to water] (kilogram) | 57.3 | 57.3 | +0.0% | -0.00357 |
| calcium [Emissions/Emissions to water] (kilogram) | 41.3 | 41.7 | +1.1% | -0.456 |
| Iron [Resources/Resources from ground] (kilogram) | 37.1 | 36.2 | -2.6% | +0.96 |
| Argon [air] (kilogram) | 32.6 | 32.6 | -0.0% | +6.79e-07 |
| Silicon [Emissions/Emissions to water] (kilogram) | 28.2 | 28.3 | +0.3% | -0.0706 |
| Chloride [Emissions/Emissions to water] (kilogram) | 22.5 | 22.5 | +0.0% | -0.00442 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 1.11e+06 | 1.11e+06 | +0.0% | -252 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 3.94e+05 | 3.94e+05 | +0.0% | -134 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 1.59e+04 | 1.59e+04 | +0.0% | -5.38 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 1.04e+04 | 1.04e+04 | +0.0% | -2.47 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 3.3e+03 | 3.31e+03 | +0.3% | -9.09 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 2.8 | 2.8 | -0.0% | +0.00136 |
| To Forest, Intensive [Land use/Land transformation] (square meter) | 2.26 | 2.26 | -0.0% | +0.000806 |
| From Forest, Intensive [Land use/Land transformation] (square meter) | 2.24 | 2.24 | -0.0% | +0.000804 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 1.98 | 1.98 | -0.0% | +0.000974 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 1.15 | 1.15 | +0.0% | -0.000484 |

### megajoule (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Waste Heat [air] (megajoule) | 5.14e+04 | 5.14e+04 | +0.0% | -21.7 |
| Natural Gas [Resources/Resources from ground] (megajoule) | 4.47e+04 | 4.47e+04 | +0.0% | -1.21 |
| Crude Oil [Resources/Resources from ground] (megajoule) | 2e+04 | 2.01e+04 | +0.0% | -8.63 |
| Waste Heat [air] (megajoule) | 1.75e+04 | 1.75e+04 | +0.0% | -6.27 |
| Uranium [Resources/Resources from ground] (megajoule) | 1.58e+04 | 1.58e+04 | +0.0% | -3.46 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 202 | 202 | -0.0% | +0.0716 |
| Forest [Land use/Land occupation] (square meter-year) | 23.4 | 23.4 | +0.1% | -0.0136 |
| Water Bodies [land use] (square meter-year) | 16.2 | 16.2 | -0.1% | +0.00967 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 8.31 | 8.32 | +0.0% | -0.00384 |
| Traffic Area, Rail/road Embankment [Land use/Land occupation] (square meter-year) | 3.58 | 3.58 | -0.0% | +0.000924 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 2.16e+04 | 2.16e+04 | +0.1% | -15 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 2.15e+04 | 2.16e+04 | +0.1% | -15.1 |
| Water, salt, ocean [resources/in water] (cubic meter) | 3.11e+03 | 3.11e+03 | -0.0% | +0.04 |
| Water [water] (cubic meter) | 3.1e+03 | 3.1e+03 | -0.0% | +0.0406 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 60.1 | 59.9 | -0.3% | +0.178 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | -3.72e-16 | -1.68e-16 | -54.9% | -2.04e-16 |
| Uranium alpha [emissions to water/lake] (Becquerel) | -1.74e-16 | -7.87e-17 | -54.9% | -9.56e-17 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | -3.17e-17 | -1.43e-17 | -54.9% | -1.74e-17 |
| Thorium-232 [emissions to water/river] (Becquerel) | -3.76e-19 | -1.7e-19 | -54.9% | -2.06e-19 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | -1.11e-19 | -5.02e-20 | -54.9% | -6.1e-20 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 58.1 | 58.1 | -0.0% | +0.0112 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 1.43 | 1.43 | -0.0% | +1.15e-05 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 1.15e+03 | 1.15e+03 | -0.0% | +0.309 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 0.00689 | 0.00689 | +0.0% | -1.86e-06 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | -1.96e-13 | -1.88e-13 | -4.2% | -8.3e-15 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | -3.52e-17 | -1.59e-17 | -54.9% | -1.93e-17 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 144 | 144 | +0.0% | -0.053 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 0.66 | 0.66 | -0.0% | +1.39e-05 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Sulfate Ion [water] (kilogram) | 5.8 | 6.01 | +3.6% |
| Dolomite [soil] (kilogram) | 5.41 | 5.26 | -2.8% |
| Iron [Resources/Resources from ground] (kilogram) | 37.1 | 36.2 | -2.6% |
| iron [Emissions/Emissions to water] (kilogram) | 3.41 | 3.49 | +2.3% |
| magnesium [Emissions/Emissions to water] (kilogram) | 12.9 | 13.2 | +2.2% |
| Potassium [emissions to water/groundwater, long-term] (kilogram) | 7.93 | 8.09 | +2.0% |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 95.2 | 96.6 | +1.5% |
| calcium [Emissions/Emissions to water] (kilogram) | 41.3 | 41.7 | +1.1% |
| Phosphate [Emissions/Emissions to water] (kilogram) | 3.34 | 3.37 | +1.1% |
| Sodium [emissions to water/groundwater, long-term] (kilogram) | 13.2 | 13.2 | +0.4% |

## Structural checks

- ✓ 12 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✗ depends on system processes (rebuild those first): ['Epoxy resin, liquid, at plant']
- ✓ mass in: 154 kg technosphere + 0 kg resources per 1 p product (informational)
- ✓ all inputs resolved

residual: 626 flows under-explained, 1161 over-explained (negative residual)

## Evidence

- 2024 - LCA power-to-X in residential sector - Sacchi.pdf — pages 63-64 -> report-p63-64.txt report sha256 165eb1e3cb0728f7…, text sha256 121187c43fba8d55…
