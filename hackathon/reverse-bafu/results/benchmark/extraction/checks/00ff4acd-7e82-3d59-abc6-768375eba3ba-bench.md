# Check: Manganese, at regional storage (00ff4acd-7e82-3d59-abc6-768375eba3ba)

target `bafu-2026` vs explicit model `00ff4acd-7e82-3d59-abc6-768375eba3ba-bench-disagg` and hybrid `00ff4acd-7e82-3d59-abc6-768375eba3ba-bench-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: Fig. 5.6 'Flows for Manganese, pure metal, at regional storage'. The text says the functional unit of the process is one tonne of manganese consumed in Europe, but the figure caption states explicitly 'Values correspond to the functional unit of 1 kg manganese metal', so the basis is 1 kg.; allocation: none stated; an electrothermal/electrolysis production split of 75/25 is assumed, and 75 % of the Mn in the electrothermal raw material is taken from ore, the rest from burden-free slag.. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 22/50 within ±10 %, median |Δ| 13.7%
- kilogram mass covered within ±10 %: 67.5% of the target's total kg mass
- of the 1786 flows of the target, 1666 are determined by the solve (120 are round-off and are not scored; see lci.determined_flows)
- 823 of those 1666 within ±10 % (49%), median |Δ| 10.4%, 0 missing from the model, 0 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 830 | 46% |
| 10–20 % | 267 | 15% |
| 20–50 % | 499 | 28% |
| 50–100 % | 104 | 6% |
| > 100 % | 86 | 5% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1471 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Manganese [Resources/Resources from ground] (kilogram) | 2.33 | 2.33 | -0.0% | +4.43e-06 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.641 | 0.944 | +47.2% | -0.303 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.585 | 0.782 | +33.6% | -0.197 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.498 | 0.5 | +0.3% | -0.00163 |
| Suspended Solids, Unspecified [water] (kilogram) | 0.454 | 0.454 | +0.0% | -3.17e-05 |
| Gravel [soil] (kilogram) | 0.353 | 0.365 | +3.4% | -0.0119 |
| Calcite [resources/in ground] (kilogram) | 0.318 | 0.328 | +3.2% | -0.0103 |
| Platinum [air] (kilogram) | 0.197 | 0.145 | -26.7% | +0.0527 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.169 | 0.166 | -2.0% | +0.00331 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.167 | 0.12 | -28.4% | +0.0473 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0971 | 0.0714 | -26.5% | +0.0257 |
| calcium [Emissions/Emissions to water] (kilogram) | 0.0875 | 0.0987 | +12.8% | -0.0112 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.0804 | 0.126 | +56.9% | -0.0457 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0555 | 0.0344 | -38.0% | +0.0211 |
| Chemically polluted water [emissions to water/river] (kilogram) | 0.0261 | 0.0317 | +21.3% | -0.00556 |
| Dolomite [soil] (kilogram) | 0.0201 | 0.02 | -0.3% | +6.11e-05 |
| Silicon [Emissions/Emissions to water] (kilogram) | 0.0194 | 0.0278 | +43.3% | -0.00839 |
| Iron [Resources/Resources from ground] (kilogram) | 0.014 | 0.0136 | -2.8% | +0.00039 |
| Sodium [emissions to water/groundwater, long-term] (kilogram) | 0.0129 | 0.0185 | +43.4% | -0.00561 |
| Clay [soil] (kilogram) | 0.0123 | 0.0123 | +0.2% | -1.95e-05 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 970 | 1.21e+03 | +24.4% | -237 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 345 | 467 | +35.4% | -122 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 13.9 | 18.8 | +35.4% | -4.91 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 8.9 | 11.1 | +25.0% | -2.22 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 1.96 | 2.39 | +22.0% | -0.431 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 0.00242 | 0.00247 | +2.1% | -5.09e-05 |
| To Forest, Intensive [Land use/Land transformation] (square meter) | 0.00212 | 0.00152 | -28.3% | +0.0006 |
| From Forest, Intensive [Land use/Land transformation] (square meter) | 0.00211 | 0.00151 | -28.4% | +0.0006 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 0.00171 | 0.00174 | +1.8% | -3.02e-05 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 0.00104 | 0.00107 | +2.7% | -2.77e-05 |

### megajoule (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Waste Heat [air] (megajoule) | 24.6 | 28.9 | +17.3% | -4.26 |
| Waste Heat [air] (megajoule) | 18.5 | 10.7 | -42.4% | +7.85 |
| Uranium [Resources/Resources from ground] (megajoule) | 13.1 | 16.3 | +24.5% | -3.21 |
| Energy, Potential (in Hydropower Reservoir), Converted [natural resource] (megajoule) | 10.1 | 9.49 | -6.3% | +0.643 |
| Natural Gas [Resources/Resources from ground] (megajoule) | 5.82 | 7.05 | +21.0% | -1.23 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.19 | 0.136 | -28.7% | +0.0545 |
| Dump Site [Land use/Land occupation] (square meter-year) | 0.0855 | 0.0862 | +0.8% | -0.000676 |
| Forest [Land use/Land occupation] (square meter-year) | 0.0205 | 0.0164 | -20.1% | +0.00413 |
| Water Bodies [land use] (square meter-year) | 0.0129 | 0.00708 | -44.9% | +0.00578 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.0119 | 0.0102 | -13.8% | +0.00164 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 103 | 102 | -0.7% | +0.694 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 103 | 102 | -0.7% | +0.714 |
| Water, salt, ocean [resources/in water] (cubic meter) | 0.37 | 0.464 | +25.3% | -0.0939 |
| Water [water] (cubic meter) | 0.369 | 0.463 | +25.3% | -0.0933 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 0.0332 | 0.0529 | +59.4% | -0.0197 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | 3.52e-20 | -4.34e-19 | -1330.8% | +4.69e-19 |
| Uranium alpha [emissions to water/lake] (Becquerel) | 1.65e-20 | -2.03e-19 | -1330.8% | +2.2e-19 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | 3e-21 | -3.69e-20 | -1330.8% | +3.99e-20 |
| Thorium-232 [emissions to water/river] (Becquerel) | 3.56e-23 | -4.39e-22 | -1330.8% | +4.74e-22 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | 1.05e-23 | -1.3e-22 | -1330.8% | +1.4e-22 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.0873 | 0.0887 | +1.7% | -0.00147 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 0.00021 | 0.000193 | -8.0% | +1.68e-05 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 2.87 | 3.13 | +9.2% | -0.263 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 5.4e-06 | 3.79e-06 | -29.8% | +1.61e-06 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | -1.49e-18 | -1.73e-17 | +1057.0% | +1.58e-17 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | 3.33e-21 | -4.1e-20 | -1330.8% | +4.44e-20 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.127 | 0.131 | +3.7% | -0.00465 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 8.67e-05 | 0.000105 | +21.5% | -1.86e-05 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Solids, Inorganic [water] (kilogram) | 0.00127 | 0.00207 | +62.4% |
| Phosphate [Emissions/Emissions to water] (kilogram) | 0.00279 | 0.00453 | +62.2% |
| Potassium [emissions to water/groundwater, long-term] (kilogram) | 0.0057 | 0.009 | +58.0% |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.0804 | 0.126 | +56.9% |
| chloride [Emissions/Emissions to water] (kilogram) | 0.00243 | 0.00378 | +55.5% |
| Sulfate Ion [water] (kilogram) | 0.00408 | 0.00632 | +55.0% |
| iron [Emissions/Emissions to water] (kilogram) | 0.00243 | 0.00364 | +49.7% |
| magnesium [Emissions/Emissions to water] (kilogram) | 0.0115 | 0.0172 | +49.4% |
| Methane (fossil) [Emissions/Emissions to air] (kilogram) | 0.00196 | 0.00291 | +48.2% |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.641 | 0.944 | +47.2% |

## Structural checks

- ✓ 4 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 4.82 kg technosphere + 0 kg resources per 1 kg product (informational)
- ✓ all inputs resolved

residual: 926 flows under-explained, 860 over-explained (negative residual)

## Evidence

- 2009 - LCI metals - Classen.pdf — pages 405-407 -> report-p405-407.txt report sha256 21b5b36302a484f1…, text sha256 a65356fb60402ea8…
