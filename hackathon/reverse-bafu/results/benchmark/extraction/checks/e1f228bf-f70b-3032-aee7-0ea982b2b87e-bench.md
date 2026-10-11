# Check: Ventilation duct, steel, zinc coated, s= 0.75mm, at plant (e1f228bf-f70b-3032-aee7-0ea982b2b87e)

target `bafu-2026` vs explicit model `e1f228bf-f70b-3032-aee7-0ea982b2b87e-bench-disagg` and hybrid `e1f228bf-f70b-3032-aee7-0ea982b2b87e-bench-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: Tabelle 42 'Lueftungskanaele aus verzinktem Stahlblech', column 'Lueftungskanal, Stahl verzinkt, s= 0.75mm, ab Werk' [CH], per 1 m2; allocation: none stated. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** Section bar rolling, steel [0.25–7.65]
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 49/50 within ±10 %, median |Δ| 0.7%
- kilogram mass covered within ±10 %: 99.6% of the target's total kg mass
- of the 1786 flows of the target, 1668 are determined by the solve (118 are round-off and are not scored; see lci.determined_flows)
- 1585 of those 1668 within ±10 % (95%), median |Δ| 0.8%, 0 missing from the model, 0 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 1600 | 90% |
| 10–20 % | 84 | 5% |
| 20–50 % | 27 | 2% |
| 50–100 % | 45 | 3% |
| > 100 % | 30 | 2% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1471 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 12.5 | 12.5 | -0.1% | +0.00915 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 8.05 | 8.3 | +3.2% | -0.256 |
| Iron [Resources/Resources from ground] (kilogram) | 7.44 | 7.44 | -0.0% | +0.000654 |
| Gravel [soil] (kilogram) | 7.25 | 7.28 | +0.4% | -0.0321 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 2.63 | 2.79 | +6.1% | -0.16 |
| Calcite [resources/in ground] (kilogram) | 2 | 2.01 | +0.5% | -0.0101 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 1.56 | 1.57 | +0.5% | -0.00787 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 1.29 | 1.26 | -2.0% | +0.026 |
| Dolomite [soil] (kilogram) | 1.16 | 1.16 | -0.0% | +0.000141 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.755 | 0.708 | -6.2% | +0.0467 |
| Zinc [Resources/Resources from ground] (kilogram) | 0.691 | 0.692 | +0.2% | -0.00105 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.667 | 0.705 | +5.7% | -0.038 |
| Platinum [air] (kilogram) | 0.663 | 0.61 | -8.0% | +0.0532 |
| Sodium chloride [resources/in ground] (kilogram) | 0.572 | 0.572 | +0.1% | -0.00045 |
| calcium [Emissions/Emissions to water] (kilogram) | 0.422 | 0.432 | +2.4% | -0.0101 |
| Chemically polluted water [emissions to water/river] (kilogram) | 0.339 | 0.344 | +1.3% | -0.00454 |
| Carbon Monoxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.317 | 0.317 | -0.0% | +7.2e-05 |
| Clay [soil] (kilogram) | 0.23 | 0.23 | +0.1% | -0.000293 |
| Magnesite [soil] (kilogram) | 0.202 | 0.202 | +0.0% | -8.59e-05 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.195 | 0.174 | -10.5% | +0.0204 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 3.73e+03 | 3.92e+03 | +4.9% | -183 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 1.33e+03 | 1.42e+03 | +7.3% | -96.4 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 53.4 | 57.3 | +7.3% | -3.88 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 34.4 | 36.1 | +5.0% | -1.71 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 17.8 | 18.1 | +1.9% | -0.34 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 0.0423 | 0.0418 | -1.0% | +0.000434 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 0.03 | 0.0297 | -1.0% | +0.000313 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 0.0175 | 0.0174 | -0.7% | +0.000121 |
| From Arable, Non-irrigated [Land use/Land transformation] (square meter) | 0.0166 | 0.0165 | -0.7% | +0.000115 |
| From Pasture/meadow [Land use/Land transformation] (square meter) | 0.013 | 0.0128 | -1.5% | +0.000189 |

### megajoule (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Waste Heat [air] (megajoule) | 169 | 162 | -4.0% | +6.8 |
| Natural Gas [Resources/Resources from ground] (megajoule) | 87.8 | 88.8 | +1.1% | -0.937 |
| Waste Heat [air] (megajoule) | 67 | 70.4 | +5.1% | -3.42 |
| Hard Coal [Resources/Resources from ground] (megajoule) | 54.2 | 55.9 | +3.0% | -1.64 |
| Uranium [Resources/Resources from ground] (megajoule) | 50.6 | 53.1 | +4.9% | -2.47 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.761 | 0.708 | -6.9% | +0.0528 |
| Forest [Land use/Land occupation] (square meter-year) | 0.182 | 0.178 | -2.1% | +0.00387 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.176 | 0.175 | -0.8% | +0.0014 |
| Traffic Area, Road Network [Land use/Land occupation] (square meter-year) | 0.071 | 0.0712 | +0.2% | -0.000124 |
| Water Bodies [land use] (square meter-year) | 0.0524 | 0.0473 | -9.9% | +0.00517 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 69 | 71.6 | +3.7% | -2.54 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 68.2 | 70.7 | +3.7% | -2.52 |
| Water, salt, ocean [resources/in water] (cubic meter) | 6.8 | 6.87 | +1.1% | -0.0743 |
| Water [water] (cubic meter) | 6.79 | 6.87 | +1.1% | -0.0739 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 0.65 | 0.667 | +2.5% | -0.0163 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | 6.38e-18 | 3.38e-18 | -46.9% | +2.99e-18 |
| Uranium alpha [emissions to water/lake] (Becquerel) | 2.99e-18 | 1.58e-18 | -46.9% | +1.4e-18 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | 5.43e-19 | 2.88e-19 | -46.9% | +2.55e-19 |
| Thorium-232 [emissions to water/river] (Becquerel) | 6.45e-21 | 3.42e-21 | -46.9% | +3.03e-21 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | 1.91e-21 | 1.01e-21 | -46.9% | +8.95e-22 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.793 | 0.795 | +0.2% | -0.00187 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 0.00642 | 0.0064 | -0.2% | +1.13e-05 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 18.8 | 19 | +1.2% | -0.222 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 4.72e-05 | 4.57e-05 | -3.1% | +1.48e-06 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | 1.07e-16 | 2.58e-18 | -97.6% | +1.05e-16 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | 6.03e-19 | 3.2e-19 | -46.9% | +2.83e-19 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.61 | 0.625 | +2.4% | -0.0146 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 0.00148 | 0.00149 | +1.0% | -1.43e-05 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.195 | 0.174 | -10.5% |
| Platinum [air] (kilogram) | 0.663 | 0.61 | -8.0% |
| Phosphate [Emissions/Emissions to water] (kilogram) | 0.0217 | 0.0232 | +6.6% |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.755 | 0.708 | -6.2% |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 2.63 | 2.79 | +6.1% |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.667 | 0.705 | +5.7% |
| Sodium [emissions to water/groundwater, long-term] (kilogram) | 0.0819 | 0.0866 | +5.7% |
| chloride [Emissions/Emissions to water] (kilogram) | 0.0232 | 0.0243 | +4.7% |
| Potassium [emissions to water/groundwater, long-term] (kilogram) | 0.0606 | 0.0634 | +4.5% |
| magnesium [Emissions/Emissions to water] (kilogram) | 0.107 | 0.112 | +4.5% |

## Structural checks

- ✓ 14 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 32.6 kg technosphere + 0 kg resources per 1 m2 product (informational)
- ✓ all inputs resolved

residual: 780 flows under-explained, 1006 over-explained (negative residual)

## Evidence

- 2014 - LCA data ventilation and heating systems - Klingler.pdf — pages 117-119 -> report-p117-119.txt report sha256 f4692d86e964f922…, text sha256 fbda9f888ca9fd8e…
