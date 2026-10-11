# Check: Door, inner, room, glass-wood, steel frame, at plant (025cc8eb-e486-3f4e-b220-74bb3fa6e9d1)

target `bafu-2026` vs explicit model `025cc8eb-e486-3f4e-b220-74bb3fa6e9d1-bench-disagg` and hybrid `025cc8eb-e486-3f4e-b220-74bb3fa6e9d1-bench-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: Tabelle 20 'Sachbilanzdaten fuer die Herstellung von 1 m2 Holz-Innentuere oder Aussentuere ab Werk in der Schweiz', 5th product column 'door, inner, room, glass-wood, steel frame, at plant' [CH], per 1 m2; allocation: none stated. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 49/50 within ±10 %, median |Δ| 0.0%
- kilogram mass covered within ±10 %: 96.3% of the target's total kg mass
- of the 1783 flows of the target, 1669 are determined by the solve (114 are round-off and are not scored; see lci.determined_flows)
- 1667 of those 1669 within ±10 % (100%), median |Δ| 0.0%, 0 missing from the model, 1 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 1681 | 94% |
| 10–20 % | 1 | 0% |
| 20–50 % | 42 | 2% |
| 50–100 % | 9 | 1% |
| > 100 % | 50 | 3% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1468 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 43.9 | 43.9 | -0.0% | +0.000106 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 42.6 | 42.6 | -0.0% | +7.08e-05 |
| Gravel [soil] (kilogram) | 35.7 | 35.7 | -0.0% | +0.000164 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 32.8 | 32.8 | -0.0% | +0.000749 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 15.9 | 15.9 | -0.0% | +1.52e-05 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 10.5 | 10.5 | -0.0% | +3.93e-05 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 10.5 | 10.5 | -0.0% | +0.000215 |
| Iron [Resources/Resources from ground] (kilogram) | 8.73 | 16.3 | +87.1% | -7.6 |
| Calcite [resources/in ground] (kilogram) | 7.19 | 7.19 | -0.0% | +5.73e-05 |
| Dolomite [soil] (kilogram) | 5.83 | 5.83 | -0.0% | +7.54e-07 |
| Sodium chloride [resources/in ground] (kilogram) | 2.7 | 2.7 | -0.0% | +5.93e-05 |
| Platinum [air] (kilogram) | 2.62 | 2.62 | -0.0% | +1.15e-05 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 1.99 | 1.99 | -0.0% | +2.42e-05 |
| Chemically polluted water [emissions to water/river] (kilogram) | 1.73 | 1.73 | -0.0% | +1.36e-05 |
| calcium [Emissions/Emissions to water] (kilogram) | 1.71 | 1.71 | -0.0% | +1.16e-05 |
| Silicon [Emissions/Emissions to water] (kilogram) | 1.5 | 1.5 | -0.0% | +1.04e-05 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.894 | 0.894 | -0.0% | +6.59e-06 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.878 | 0.878 | -0.0% | +4.05e-06 |
| Clay [soil] (kilogram) | 0.775 | 0.775 | -0.0% | +2.02e-05 |
| Carbon Monoxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.592 | 0.592 | -0.0% | +4.99e-07 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 2.11e+04 | 2.11e+04 | -0.0% | +0.146 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 7.38e+03 | 7.38e+03 | -0.0% | +0.0665 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 396 | 396 | -0.0% | +0.00931 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 297 | 297 | -0.0% | +0.00268 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 195 | 195 | -0.0% | +0.00259 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 0.55 | 0.55 | -0.0% | +0.000236 |
| From Arable, Non-irrigated [Land use/Land transformation] (square meter) | 0.544 | 0.544 | -0.0% | +0.000236 |
| To Forest, Intensive [Land use/Land transformation] (square meter) | 0.507 | 0.507 | -0.0% | +1.83e-07 |
| From Forest, Intensive [Land use/Land transformation] (square meter) | 0.506 | 0.506 | -0.0% | +1.31e-07 |
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 0.374 | 0.374 | -0.0% | +7.7e-07 |

### megajoule (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Waste Heat [air] (megajoule) | 858 | 858 | -0.0% | +0.0117 |
| Energy, gross calorific value, in biomass [resources/biotic] (megajoule) | 468 | 468 | -0.0% | +0.000906 |
| Natural Gas [Resources/Resources from ground] (megajoule) | 466 | 466 | -0.0% | +0.00793 |
| Crude Oil [Resources/Resources from ground] (megajoule) | 325 | 325 | -0.0% | +0.00679 |
| Waste Heat [air] (megajoule) | 303 | 302 | -0.0% | +0.00323 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 44.3 | 44.3 | -0.0% | +1.78e-05 |
| Forest [Land use/Land occupation] (square meter-year) | 15 | 15 | -0.0% | +8.85e-06 |
| Traffic Area, Rail/road Embankment [Land use/Land occupation] (square meter-year) | 0.676 | 0.676 | -0.0% | +9.27e-07 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.485 | 0.485 | -0.0% | +3.49e-06 |
| Arable, Non-irrigated, Intensive [Land use/Land occupation] (square meter-year) | 0.343 | 0.343 | -0.0% | +7.05e-07 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 620 | 620 | -0.0% | +0.0031 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 590 | 590 | -0.0% | +0.00304 |
| Water, salt, ocean [resources/in water] (cubic meter) | 30.3 | 30.3 | -0.0% | +0.00022 |
| Water [water] (cubic meter) | 30.3 | 30.3 | -0.0% | +0.00022 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 30.2 | 30.2 | -0.0% | +1.79e-05 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | 4.22e-15 | -2.89e-15 | -168.4% | +7.11e-15 |
| Uranium alpha [emissions to water/lake] (Becquerel) | 1.98e-15 | -1.35e-15 | -168.4% | +3.33e-15 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | 3.59e-16 | -2.46e-16 | -168.4% | +6.05e-16 |
| Thorium-232 [emissions to water/river] (Becquerel) | 4.27e-18 | -2.92e-18 | -168.4% | +7.19e-18 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | 1.26e-18 | -8.63e-19 | -168.4% | +2.12e-18 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 6.14 | 6.14 | -0.0% | +2.24e-05 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 0.0206 | 0.0206 | -0.0% | +2.59e-07 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 58.7 | 58.7 | -0.0% | +0.00061 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 0.00522 | 0.00522 | -0.0% | +3.03e-09 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | 0.014 | 0.014 | -0.0% | +2.5e-13 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | 3.99e-16 | -2.73e-16 | -168.4% | +6.72e-16 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 2.49 | 2.49 | -0.0% | +1.25e-05 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 0.00745 | 0.00745 | -0.0% | +5.24e-08 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Iron [Resources/Resources from ground] (kilogram) | 8.73 | 16.3 | +87.1% |
| Titanium [Resources/Resources from ground] (kilogram) | 0.153 | 0.153 | -0.0% |
| TOC, Total Organic Carbon [emissions to water/groundwater, long-term] (kilogram) | 0.09 | 0.09 | -0.0% |
| COD, Chemical Oxygen Demand [emissions to water/groundwater, long-term] (kilogram) | 0.238 | 0.238 | -0.0% |
| Clay [soil] (kilogram) | 0.775 | 0.775 | -0.0% |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 32.8 | 32.8 | -0.0% |
| Sodium chloride [resources/in ground] (kilogram) | 2.7 | 2.7 | -0.0% |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 10.5 | 10.5 | -0.0% |
| Methane (fossil) [Emissions/Emissions to air] (kilogram) | 0.107 | 0.107 | -0.0% |
| Barite [resources/in ground] (kilogram) | 0.0932 | 0.0932 | -0.0% |

## Structural checks

- ✓ 3 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 0 kg technosphere + 0 kg resources per 1 m2 product (informational)
- ✓ all inputs resolved

residual: 1742 flows under-explained, 42 over-explained (negative residual)

## Evidence

- 2020 - LCA wooden windows and doors - Ramseier.pdf — pages 31-34 -> report-p31-34.txt report sha256 f1b267004c921d2b…, text sha256 87b3eb83cb0c0b32…
