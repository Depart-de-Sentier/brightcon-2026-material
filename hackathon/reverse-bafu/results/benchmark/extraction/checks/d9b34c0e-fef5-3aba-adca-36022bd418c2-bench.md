# Check: SOx retained, in hard coal flue gas desulphurisation (d9b34c0e-fef5-3aba-adca-36022bd418c2)

target `bafu-2026` vs explicit model `d9b34c0e-fef5-3aba-adca-36022bd418c2-bench-disagg` and hybrid `d9b34c0e-fef5-3aba-adca-36022bd418c2-bench-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: Tab. 9.33 'REA-Massenbilanz pro kg reduziertes SO2', column 'REA-Nass' (hard coal), plus the 'mit 5 l Abwasser/kg SO2' column of Tab. 9.34 for the water emissions; per 1 kg SO2 retained; allocation: The gypsum is treated as a free co-product of the power plant operation and is not allocated a burden ('wird in Ecoinvent nicht aufgenommen').. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 19/50 within ±10 %, median |Δ| 26.6%
- kilogram mass covered within ±10 %: 58.5% of the target's total kg mass
- of the 1786 flows of the target, 1670 are determined by the solve (116 are round-off and are not scored; see lci.determined_flows)
- 586 of those 1670 within ±10 % (35%), median |Δ| 14.9%, 1 missing from the model, 2 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 600 | 34% |
| 10–20 % | 345 | 19% |
| 20–50 % | 212 | 12% |
| 50–100 % | 277 | 16% |
| > 100 % | 352 | 20% |
| missing (0 in model) | 1 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1470 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Calcite [resources/in ground] (kilogram) | 1.65 | 1.65 | +0.0% | -0.000352 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.776 | 0.227 | -70.8% | +0.55 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.251 | 0.000859 | -99.7% | +0.25 |
| Calcium [Emissions/Emissions to water] (kilogram) | 0.0501 | 0.000101 | -99.8% | +0.05 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0295 | 0.0326 | +10.5% | -0.0031 |
| Gravel [soil] (kilogram) | 0.0282 | 0.0354 | +25.2% | -0.00712 |
| Sodium chloride [resources/in ground] (kilogram) | 0.0169 | 0.017 | +0.5% | -9.15e-05 |
| Sulfate Ion [water] (kilogram) | 0.0102 | 0.0103 | +0.9% | -9.1e-05 |
| Magnesium [Emissions/Emissions to water] (kilogram) | 0.01 | 1.48e-05 | -99.9% | +0.01 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00893 | 0.00091 | -89.8% | +0.00802 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.00843 | 0.56 | +6547.1% | -0.552 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.00622 | 0.00661 | +6.4% | -0.000395 |
| Nitrate [Emissions/Emissions to water] (kilogram) | 0.00518 | 1.47e-05 | -99.7% | +0.00516 |
| COD, Chemical Oxygen Demand [emissions to water/groundwater, long-term] (kilogram) | 0.00474 | 0.000122 | -97.4% | +0.00462 |
| Chemically polluted water [emissions to water/river] (kilogram) | 0.00432 | 0.00449 | +4.1% | -0.000175 |
| TOC, Total Organic Carbon [emissions to water/groundwater, long-term] (kilogram) | 0.0043 | 4.77e-05 | -98.9% | +0.00426 |
| DOC, Dissolved Organic Carbon [emissions to water/groundwater, long-term] (kilogram) | 0.0043 | 4.77e-05 | -98.9% | +0.00426 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.00354 | 0.033 | +830.7% | -0.0294 |
| Sodium [water] (kilogram) | 0.00284 | 0.000386 | -86.4% | +0.00245 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00272 | 0.0363 | +1236.8% | -0.0336 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 28.5 | 30.7 | +7.5% | -2.15 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 9.84 | 10.5 | +6.8% | -0.673 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.396 | 0.423 | +6.8% | -0.0271 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.257 | 0.277 | +7.9% | -0.0202 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.0767 | 0.196 | +155.5% | -0.119 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 0.000122 | 0.00019 | +55.5% | -6.79e-05 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 8.67e-05 | 0.000135 | +55.5% | -4.82e-05 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 5.25e-05 | 0.000149 | +184.0% | -9.66e-05 |
| From Arable, Non-irrigated [Land use/Land transformation] (square meter) | 4.96e-05 | 0.000145 | +192.2% | -9.53e-05 |
| From Pasture/meadow [Land use/Land transformation] (square meter) | 4.28e-05 | 6.52e-05 | +52.4% | -2.24e-05 |

### megajoule (28 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Waste Heat [air] (megajoule) | 2.78 | 3.2 | +14.8% | -0.413 |
| Crude Oil [Resources/Resources from ground] (megajoule) | 1.43 | 1.48 | +3.5% | -0.0506 |
| Waste Heat [water] (megajoule) | 0.795 | 0.856 | +7.7% | -0.0609 |
| Heat, waste [emissions to water/groundwater, long-term] (megajoule) | 0.668 | 0.00165 | -99.8% | +0.666 |
| Waste Heat [air] (megajoule) | 0.58 | 0.573 | -1.2% | +0.00704 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.0034 | 0.0572 | +1584.9% | -0.0538 |
| Forest [Land use/Land occupation] (square meter-year) | 0.00112 | 0.00172 | +53.7% | -0.000602 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.000298 | 0.000325 | +8.9% | -2.64e-05 |
| Inland Water Bodies [land use] (square meter-year) | 0.000213 | 0.000227 | +6.5% | -1.39e-05 |
| Water Bodies [land use] (square meter-year) | 0.000205 | 0.000263 | +28.2% | -5.78e-05 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 2.08 | 2.22 | +7.0% | -0.146 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 2.07 | 2.22 | +7.0% | -0.145 |
| river water [Resources/Resources from water] (cubic meter) | 0.0208 | 0.0209 | +0.1% | -2.98e-05 |
| Water, salt, ocean [resources/in water] (cubic meter) | 0.00868 | 0.0101 | +16.5% | -0.00143 |
| Water [water] (cubic meter) | 0.00865 | 0.0101 | +16.5% | -0.00143 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | 6.81e-20 | 5.42e-20 | -20.4% | +1.39e-20 |
| Uranium alpha [emissions to water/lake] (Becquerel) | 3.19e-20 | 2.54e-20 | -20.4% | +6.51e-21 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | 5.8e-21 | 4.62e-21 | -20.4% | +1.18e-21 |
| Thorium-232 [emissions to water/river] (Becquerel) | 6.89e-23 | 5.48e-23 | -20.4% | +1.41e-23 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | 2.04e-23 | 1.62e-23 | -20.4% | +4.15e-24 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.00568 | 0.00696 | +22.5% | -0.00128 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 1.64e-05 | 1.83e-05 | +11.2% | -1.84e-06 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 0.201 | 0.212 | +5.5% | -0.011 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 3.75e-07 | 5.1e-07 | +36.1% | -1.35e-07 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | -9.85e-18 | -5.4e-20 | -99.5% | -9.8e-18 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | 6.44e-21 | 5.13e-21 | -20.4% | +1.31e-21 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.00303 | 0.00344 | +13.5% | -0.000408 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 2.03e-06 | 2.37e-06 | +17.0% | -3.45e-07 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.00843 | 0.56 | +6547.1% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00272 | 0.0363 | +1236.8% |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.00354 | 0.033 | +830.7% |
| Silicon [Emissions/Emissions to water] (kilogram) | 0.000501 | 0.00281 | +461.3% |
| Boron [Emissions/Emissions to water] (kilogram) | 0.000331 | 4.21e-07 | -99.9% |
| Magnesium [Emissions/Emissions to water] (kilogram) | 0.01 | 1.48e-05 | -99.9% |
| Fluoride Ion [Emissions/Emissions to water] (kilogram) | 0.00015 | 2.37e-07 | -99.8% |
| Calcium [Emissions/Emissions to water] (kilogram) | 0.0501 | 0.000101 | -99.8% |
| Nitrate [Emissions/Emissions to water] (kilogram) | 0.00518 | 1.47e-05 | -99.7% |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.251 | 0.000859 | -99.7% |

## Structural checks

- ✓ 8 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 21.6 kg technosphere + 0 kg resources per 1 kg product (informational)
- ✓ all inputs resolved

residual: 192 flows under-explained, 1596 over-explained (negative residual)

## Evidence

- 2007 - Coal - Dones.pdf — pages 136-138 -> report-p136-138.txt report sha256 bf34696094afe13c…, text sha256 f7043221e7dab118…
