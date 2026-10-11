# Check: Panelling, aluminium, window frame cover, m2 visible, at plant (f3f28c27-d1a8-3ac8-b40f-2c66bc92c83a)

target `bafu-2026` vs explicit model `f3f28c27-d1a8-3ac8-b40f-2c66bc92c83a-bench-disagg` and hybrid `f3f28c27-d1a8-3ac8-b40f-2c66bc92c83a-bench-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: Tabelle 10 'Sachbilanzdaten der Herstellung der Aluminiumbeplankung des Holz-Metallfensterrahmens pro m2 Rahmenflaeche im Licht, ab Werk', column 'panelling, aluminium, window casement and frame cover, m2 visible, at plant' [CH], per 1 m2; allocation: none stated. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 0/50 within ±10 %, median |Δ| 81.2%
- kilogram mass covered within ±10 %: 0.0% of the target's total kg mass
- of the 1787 flows of the target, 1669 are determined by the solve (118 are round-off and are not scored; see lci.determined_flows)
- 0 of those 1669 within ±10 % (0%), median |Δ| 81.8%, 0 missing from the model, 0 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 0 | 0% |
| 10–20 % | 1 | 0% |
| 20–50 % | 0 | 0% |
| 50–100 % | 1658 | 93% |
| > 100 % | 128 | 7% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1472 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 67.3 | 122 | +81.2% | -54.7 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 62.4 | 112 | +80.1% | -49.9 |
| Gravel [soil] (kilogram) | 18 | 33.1 | +83.3% | -15 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 17.9 | 32.4 | +81.3% | -14.5 |
| Aluminium [Resources/Resources from ground] (kilogram) | 10.7 | 19.4 | +80.9% | -8.68 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 10.1 | 18.4 | +81.3% | -8.26 |
| calcium [Emissions/Emissions to water] (kilogram) | 9.66 | 17.5 | +81.4% | -7.87 |
| Calcite [resources/in ground] (kilogram) | 3.83 | 6.97 | +81.7% | -3.13 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 3.23 | 5.97 | +84.8% | -2.74 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 2.59 | 4.73 | +82.4% | -2.14 |
| Sodium chloride [resources/in ground] (kilogram) | 2.48 | 4.47 | +79.8% | -1.98 |
| Platinum [air] (kilogram) | 2.43 | 4.49 | +85.2% | -2.07 |
| Chemically polluted water [emissions to water/river] (kilogram) | 2.24 | 4.05 | +80.4% | -1.8 |
| Silicon [Emissions/Emissions to water] (kilogram) | 2.04 | 3.69 | +80.9% | -1.65 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 1.94 | 3.61 | +86.0% | -1.67 |
| Sodium [emissions to water/groundwater, long-term] (kilogram) | 1.22 | 2.2 | +81.3% | -0.989 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.781 | 1.37 | +75.4% | -0.589 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.685 | 1.27 | +85.2% | -0.583 |
| COD, Chemical Oxygen Demand [emissions to water/groundwater, long-term] (kilogram) | 0.613 | 1.11 | +80.7% | -0.495 |
| Iron [Resources/Resources from ground] (kilogram) | 0.511 | 0.932 | +82.4% | -0.421 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 3.71e+04 | 6.77e+04 | +82.2% | -3.05e+04 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 1.36e+04 | 2.47e+04 | +82.2% | -1.12e+04 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 546 | 995 | +82.2% | -449 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 345 | 628 | +82.1% | -283 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 137 | 249 | +81.4% | -112 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 0.065 | 0.121 | +86.4% | -0.0561 |
| To Forest, Intensive [Land use/Land transformation] (square meter) | 0.0542 | 0.0993 | +83.2% | -0.0451 |
| From Forest, Intensive [Land use/Land transformation] (square meter) | 0.0537 | 0.0984 | +83.1% | -0.0447 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 0.046 | 0.0858 | +86.4% | -0.0398 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 0.0368 | 0.0679 | +84.5% | -0.0311 |

### megajoule (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Waste Heat [air] (megajoule) | 1.01e+03 | 1.82e+03 | +80.5% | -812 |
| Waste Heat [air] (megajoule) | 649 | 1.18e+03 | +82.1% | -533 |
| Uranium [Resources/Resources from ground] (megajoule) | 504 | 918 | +82.2% | -414 |
| Natural Gas [Resources/Resources from ground] (megajoule) | 485 | 859 | +77.3% | -374 |
| Waste Heat [air] (megajoule) | 397 | 723 | +82.3% | -327 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 4.64 | 8.5 | +83.1% | -3.86 |
| Water Bodies [land use] (square meter-year) | 0.461 | 0.84 | +82.0% | -0.378 |
| Forest [Land use/Land occupation] (square meter-year) | 0.415 | 0.758 | +82.6% | -0.343 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.345 | 0.628 | +82.2% | -0.283 |
| Dump Site [Land use/Land occupation] (square meter-year) | 0.175 | 0.317 | +81.2% | -0.142 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 340 | 624 | +83.6% | -284 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 337 | 619 | +83.7% | -282 |
| Water, salt, ocean [resources/in water] (cubic meter) | 35.6 | 62.8 | +76.3% | -27.2 |
| Water [water] (cubic meter) | 35.1 | 61.9 | +76.3% | -26.8 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 1.95 | 3.54 | +81.2% | -1.59 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | 8.66e-16 | -1.82e-15 | -310.3% | +2.69e-15 |
| Uranium alpha [emissions to water/lake] (Becquerel) | 4.06e-16 | -8.53e-16 | -310.3% | +1.26e-15 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | 7.38e-17 | -1.55e-16 | -310.3% | +2.29e-16 |
| Thorium-232 [emissions to water/river] (Becquerel) | 8.76e-19 | -1.84e-18 | -310.3% | +2.72e-18 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | 2.59e-19 | -5.44e-19 | -310.3% | +8.03e-19 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 1.83 | 3.33 | +81.8% | -1.5 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 0.0263 | 0.0461 | +75.2% | -0.0198 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 39.6 | 71.8 | +81.4% | -32.2 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 0.000117 | 0.000214 | +82.5% | -9.67e-05 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | 2.25e-14 | -7.83e-14 | -447.2% | +1.01e-13 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | 8.19e-17 | -1.72e-16 | -310.3% | +2.54e-16 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 13.8 | 25.1 | +81.3% | -11.2 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 0.00784 | 0.0139 | +77.0% | -0.00604 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Sodium [water] (kilogram) | 0.0933 | 0.196 | +110.5% |
| Sulfate Ion [water] (kilogram) | 0.32 | 0.653 | +103.9% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 1.94 | 3.61 | +86.0% |
| Platinum [air] (kilogram) | 2.43 | 4.49 | +85.2% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.685 | 1.27 | +85.2% |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 3.23 | 5.97 | +84.8% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.123 | 0.225 | +83.6% |
| Gravel [soil] (kilogram) | 18 | 33.1 | +83.3% |
| chloride [Emissions/Emissions to water] (kilogram) | 0.0756 | 0.138 | +82.6% |
| Potassium [emissions to water/groundwater, long-term] (kilogram) | 0.155 | 0.283 | +82.5% |

## Structural checks

- ✓ 5 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 31.3 kg technosphere + 0 kg resources per 1 m2 product (informational)
- ✓ all inputs resolved

residual: 27 flows under-explained, 1760 over-explained (negative residual)

## Evidence

- 2020 - LCA wooden windows and doors - Ramseier.pdf — pages 25-27 -> report-p25-27.txt report sha256 f1b267004c921d2b…, text sha256 6ab63fb788d71d66…
