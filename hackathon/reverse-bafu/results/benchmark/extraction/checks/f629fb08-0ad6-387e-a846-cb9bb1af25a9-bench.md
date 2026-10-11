# Check: Compressed air, average generation, <30kW, 10 bar gauge, at compressor (f629fb08-0ad6-387e-a846-cb9bb1af25a9)

target `bafu-2026` vs explicit model `f629fb08-0ad6-387e-a846-cb9bb1af25a9-bench-disagg` and hybrid `f629fb08-0ad6-387e-a846-cb9bb1af25a9-bench-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: Tab. 10.14 'Unit process raw data of the datasets "compressed air, average generation, <30kW, at compressor"', 10 bar gauge column [RER], per 1 m3; allocation: none stated. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 22/50 within ±10 %, median |Δ| 13.5%
- kilogram mass covered within ±10 %: 30.8% of the target's total kg mass
- of the 1783 flows of the target, 1667 are determined by the solve (116 are round-off and are not scored; see lci.determined_flows)
- 906 of those 1667 within ±10 % (54%), median |Δ| 7.6%, 0 missing from the model, 1 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 909 | 51% |
| 10–20 % | 195 | 11% |
| 20–50 % | 471 | 26% |
| 50–100 % | 123 | 7% |
| > 100 % | 85 | 5% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1468 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0492 | 0.0712 | +44.8% | -0.022 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0209 | 0.0352 | +68.7% | -0.0143 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0165 | 0.0163 | -1.3% | +0.00022 |
| Gravel [soil] (kilogram) | 0.014 | 0.0149 | +6.3% | -0.000884 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.0123 | 0.0156 | +27.1% | -0.00333 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.0121 | 0.0122 | +1.0% | -0.000122 |
| Platinum [air] (kilogram) | 0.0105 | 0.00662 | -36.7% | +0.00383 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.00839 | 0.00495 | -41.0% | +0.00344 |
| Iron [Resources/Resources from ground] (kilogram) | 0.00739 | 0.00736 | -0.4% | +2.66e-05 |
| calcium [Emissions/Emissions to water] (kilogram) | 0.00515 | 0.00596 | +15.9% | -0.000817 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00467 | 0.0028 | -40.1% | +0.00187 |
| Calcite [resources/in ground] (kilogram) | 0.00384 | 0.00459 | +19.5% | -0.00075 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0029 | 0.00137 | -52.9% | +0.00153 |
| Silicon [Emissions/Emissions to water] (kilogram) | 0.00261 | 0.00322 | +23.4% | -0.00061 |
| magnesium [Emissions/Emissions to water] (kilogram) | 0.00212 | 0.00253 | +19.6% | -0.000414 |
| Chemically polluted water [emissions to water/river] (kilogram) | 0.00141 | 0.00182 | +28.7% | -0.000405 |
| Sulfate Ion [water] (kilogram) | 0.00139 | 0.00156 | +11.7% | -0.000163 |
| Copper [Resources/Resources from ground] (kilogram) | 0.00135 | 0.00134 | -0.2% | +2.95e-06 |
| Potassium [emissions to water/groundwater, long-term] (kilogram) | 0.0012 | 0.00144 | +20.0% | -0.00024 |
| Aluminium [Resources/Resources from ground] (kilogram) | 0.00116 | 0.00115 | -0.8% | +8.9e-06 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 53.1 | 70.4 | +32.5% | -17.2 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 18.8 | 27.7 | +47.2% | -8.88 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.757 | 1.11 | +47.2% | -0.357 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.488 | 0.65 | +33.1% | -0.162 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.164 | 0.195 | +19.2% | -0.0315 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Forest, Intensive [Land use/Land transformation] (square meter) | 0.000108 | 6.43e-05 | -40.4% | +4.36e-05 |
| From Forest, Intensive [Land use/Land transformation] (square meter) | 0.000108 | 6.4e-05 | -40.5% | +4.36e-05 |
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 8.36e-05 | 8.81e-05 | +5.4% | -4.48e-06 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 5.89e-05 | 6.16e-05 | +4.7% | -2.75e-06 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 3.5e-05 | 3.73e-05 | +6.7% | -2.35e-06 |

### megajoule (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Waste Heat [air] (megajoule) | 1.25 | 0.721 | -42.5% | +0.534 |
| Uranium [Resources/Resources from ground] (megajoule) | 0.722 | 0.955 | +32.3% | -0.233 |
| Waste Heat [air] (megajoule) | 0.697 | 1.01 | +44.5% | -0.31 |
| Natural Gas [Resources/Resources from ground] (megajoule) | 0.416 | 0.505 | +21.5% | -0.0892 |
| Hard Coal [Resources/Resources from ground] (megajoule) | 0.239 | 0.382 | +59.9% | -0.143 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.00966 | 0.0057 | -41.0% | +0.00396 |
| Forest [Land use/Land occupation] (square meter-year) | 0.000984 | 0.000684 | -30.5% | +0.0003 |
| Water Bodies [land use] (square meter-year) | 0.000694 | 0.000274 | -60.5% | +0.00042 |
| Dump Site [Land use/Land occupation] (square meter-year) | 0.000398 | 0.000447 | +12.4% | -4.92e-05 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.00038 | 0.000261 | -31.3% | +0.000119 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 1.2 | 1.15 | -4.2% | +0.0504 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 1.2 | 1.15 | -4.3% | +0.0518 |
| Water, salt, ocean [resources/in water] (cubic meter) | 0.0266 | 0.0335 | +25.6% | -0.00683 |
| Water [water] (cubic meter) | 0.0265 | 0.0333 | +25.6% | -0.00679 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 0.00186 | 0.00329 | +77.3% | -0.00143 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | 2.38e-20 | 1.25e-20 | -47.7% | +1.14e-20 |
| Uranium alpha [emissions to water/lake] (Becquerel) | 1.12e-20 | 5.83e-21 | -47.7% | +5.32e-21 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | 2.03e-21 | 1.06e-21 | -47.7% | +9.67e-22 |
| Thorium-232 [emissions to water/river] (Becquerel) | 2.41e-23 | 1.26e-23 | -47.7% | +1.15e-23 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | 7.12e-24 | 3.72e-24 | -47.7% | +3.39e-24 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.00176 | 0.00189 | +7.5% | -0.000133 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 1.45e-05 | 1.33e-05 | -8.2% | +1.19e-06 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 0.0415 | 0.0607 | +46.2% | -0.0192 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 3.55e-07 | 2.39e-07 | -32.9% | +1.17e-07 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | -3.76e-19 | -8.17e-19 | +117.4% | +4.41e-19 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | 2.25e-21 | 1.18e-21 | -47.7% | +1.07e-21 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.00771 | 0.00805 | +4.4% | -0.000339 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 6.05e-06 | 7.4e-06 | +22.4% | -1.36e-06 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| chloride [Emissions/Emissions to water] (kilogram) | 0.000131 | 0.000229 | +74.8% |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0209 | 0.0352 | +68.7% |
| Nitrate [Emissions/Emissions to water] (kilogram) | 7.53e-05 | 0.00012 | +58.9% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0029 | 0.00137 | -52.9% |
| Methane (fossil) [Emissions/Emissions to air] (kilogram) | 0.000134 | 0.000203 | +51.2% |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0492 | 0.0712 | +44.8% |
| Sodium [emissions to water/groundwater, long-term] (kilogram) | 0.000941 | 0.00135 | +43.4% |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.00839 | 0.00495 | -41.0% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00467 | 0.0028 | -40.1% |
| Platinum [air] (kilogram) | 0.0105 | 0.00662 | -36.7% |

## Structural checks

- ✓ 6 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 0.181 kg technosphere + 0 kg resources per 1 m3 product (informational)
- ✓ all inputs resolved

residual: 950 flows under-explained, 834 over-explained (negative residual)

## Evidence

- 2007 - LCI metal proc. and comp. air supply - Steiner.pdf — pages 88-90 -> report-p88-90.txt report sha256 ff1c92da6068a0e3…, text sha256 f63b09c007cb424c…
