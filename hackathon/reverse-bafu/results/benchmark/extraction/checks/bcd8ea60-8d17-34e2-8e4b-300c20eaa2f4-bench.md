# Check: Canning of legumes (bcd8ea60-8d17-34e2-8e4b-300c20eaa2f4)

target `bafu-2026` vs explicit model `bcd8ea60-8d17-34e2-8e4b-300c20eaa2f4-bench-disagg` and hybrid `bcd8ea60-8d17-34e2-8e4b-300c20eaa2f4-bench-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: Figure 20 'Unit process raw data of canning of food', column 'Canning of legumes' [CH], per 1 kg; allocation: none stated. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 50/50 within ±10 %, median |Δ| 0.0%
- kilogram mass covered within ±10 %: 100.0% of the target's total kg mass
- of the 1785 flows of the target, 1669 are determined by the solve (116 are round-off and are not scored; see lci.determined_flows)
- 1669 of those 1669 within ±10 % (100%), median |Δ| 0.0%, 0 missing from the model, 0 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 1680 | 94% |
| 10–20 % | 4 | 0% |
| 20–50 % | 23 | 1% |
| 50–100 % | 12 | 1% |
| > 100 % | 66 | 4% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1469 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0377 | 0.0377 | -0.0% | +1.56e-05 |
| Gravel [soil] (kilogram) | 0.0311 | 0.0311 | -0.0% | +1.08e-05 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.0254 | 0.0254 | -0.0% | +6.81e-06 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0212 | 0.0212 | -0.0% | +9.26e-06 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.0189 | 0.0189 | -0.0% | +8.14e-06 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0155 | 0.0155 | -0.0% | +6.69e-06 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.00924 | 0.00924 | -0.0% | +2.78e-06 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.0067 | 0.00669 | -0.0% | +2.48e-06 |
| Calcite [resources/in ground] (kilogram) | 0.00525 | 0.00524 | -0.0% | +1.66e-06 |
| calcium [Emissions/Emissions to water] (kilogram) | 0.00487 | 0.00487 | -0.0% | +1.44e-06 |
| Clay [soil] (kilogram) | 0.00452 | 0.00452 | -0.0% | +1.66e-07 |
| Platinum [air] (kilogram) | 0.00303 | 0.00303 | -0.0% | +1.18e-06 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00207 | 0.00207 | -0.0% | +8.91e-07 |
| Iron [Resources/Resources from ground] (kilogram) | 0.00163 | 0.00163 | -0.0% | +3.67e-07 |
| Silicon [Emissions/Emissions to water] (kilogram) | 0.00138 | 0.00138 | -0.0% | +4.5e-07 |
| Chemically polluted water [emissions to water/river] (kilogram) | 0.00137 | 0.00137 | -0.0% | +5.59e-07 |
| magnesium [Emissions/Emissions to water] (kilogram) | 0.00103 | 0.00103 | -0.0% | +3.57e-07 |
| Sodium [emissions to water/groundwater, long-term] (kilogram) | 0.000774 | 0.000774 | -0.0% | +2.88e-07 |
| Potassium [emissions to water/groundwater, long-term] (kilogram) | 0.000642 | 0.000642 | -0.0% | +2.39e-07 |
| Sulfate Ion [water] (kilogram) | 0.000576 | 0.000575 | -0.0% | +1.93e-07 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 320 | 320 | -0.0% | +0.148 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 109 | 109 | -0.0% | +0.0502 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 4.38 | 4.38 | -0.0% | +0.00202 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 2.82 | 2.82 | -0.0% | +0.0013 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.588 | 0.588 | -0.0% | +0.000254 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Forest, Intensive [Land use/Land transformation] (square meter) | 0.000229 | 0.000229 | -0.0% | +1.03e-07 |
| From Forest, Intensive [Land use/Land transformation] (square meter) | 0.000229 | 0.000229 | -0.0% | +1.03e-07 |
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 7.29e-05 | 7.29e-05 | -0.0% | +2.49e-08 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 5.13e-05 | 5.13e-05 | -0.0% | +1.74e-08 |
| From Forest [Land use/Land transformation] (square meter) | 3.62e-05 | 3.62e-05 | -0.0% | +7.12e-09 |

### megajoule (28 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium [Resources/Resources from ground] (megajoule) | 4.32 | 4.31 | -0.0% | +0.00199 |
| Waste Heat [air] (megajoule) | 2.7 | 2.7 | -0.0% | +0.00124 |
| Energy, Potential (in Hydropower Reservoir), Converted [natural resource] (megajoule) | 1.11 | 1.11 | -0.0% | +0.000511 |
| Waste Heat [air] (megajoule) | 0.541 | 0.54 | -0.0% | +0.000199 |
| Natural Gas [Resources/Resources from ground] (megajoule) | 0.466 | 0.465 | -0.0% | +0.0002 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.0207 | 0.0207 | -0.0% | +9.34e-06 |
| Forest [Land use/Land occupation] (square meter-year) | 0.00432 | 0.00432 | -0.0% | +7.69e-07 |
| Water Bodies [land use] (square meter-year) | 0.000655 | 0.000655 | -0.0% | +2.88e-07 |
| Inland Water Bodies [land use] (square meter-year) | 0.000653 | 0.000652 | -0.0% | +2.99e-07 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.000571 | 0.000571 | -0.0% | +1.13e-07 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 6.46 | 6.46 | -0.0% | +0.00296 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 6.46 | 6.46 | -0.0% | +0.00296 |
| Water, salt, ocean [resources/in water] (cubic meter) | 0.0314 | 0.0314 | -0.0% | +1.35e-05 |
| Water [water] (cubic meter) | 0.031 | 0.031 | -0.0% | +1.33e-05 |
| river water [Resources/Resources from water] (cubic meter) | 0.0031 | 0.00309 | -0.0% | +1.12e-06 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | -1.13e-19 | 8.95e-20 | -179.3% | -2.02e-19 |
| Uranium alpha [emissions to water/lake] (Becquerel) | -5.29e-20 | 4.19e-20 | -179.3% | -9.48e-20 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | -9.61e-21 | 7.62e-21 | -179.3% | -1.72e-20 |
| Thorium-232 [emissions to water/river] (Becquerel) | -1.14e-22 | 9.05e-23 | -179.3% | -2.05e-22 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | -3.37e-23 | 2.67e-23 | -179.3% | -6.05e-23 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.00171 | 0.00171 | -0.0% | +4.8e-07 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 5.48e-05 | 5.48e-05 | -0.0% | +1.03e-08 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 0.0217 | 0.0217 | -0.0% | +8.34e-06 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 1.37e-06 | 1.37e-06 | -0.0% | +1.97e-10 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | -4.75e-18 | 2.4e-18 | -150.5% | -7.16e-18 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | -1.07e-20 | 8.46e-21 | -179.3% | -1.91e-20 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.0268 | 0.0268 | -0.0% | +1.23e-05 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 8.37e-06 | 8.37e-06 | -0.0% | +3.64e-09 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Carbon Dioxide (land Use Change) [Emissions/Emissions to air] (kilogram) | 0.000226 | 0.000226 | -0.0% |
| Solids, Inorganic [water] (kilogram) | 6.68e-05 | 6.67e-05 | -0.0% |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0212 | 0.0212 | -0.0% |
| Nitrate [Emissions/Emissions to water] (kilogram) | 8.79e-05 | 8.79e-05 | -0.0% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00207 | 0.00207 | -0.0% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0155 | 0.0155 | -0.0% |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.0189 | 0.0189 | -0.0% |
| Sodium [water] (kilogram) | 0.000183 | 0.000183 | -0.0% |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.000272 | 0.000272 | -0.0% |
| Barite [resources/in ground] (kilogram) | 7.98e-05 | 7.98e-05 | -0.0% |

## Structural checks

- ✓ 3 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 1.91 kg technosphere + 0 kg resources per 1 kg product (informational)
- ✓ all inputs resolved

residual: 1698 flows under-explained, 86 over-explained (negative residual)

## Evidence

- 2021 - LCA tomatoes and green beans production - Kaegi.pdf — pages 49-50 -> report-p49-50.txt report sha256 f3715d5d00e21335…, text sha256 d93302ef1b62ab86…
