# Check: xx Packaging glass, brown, at plant (ddefdbda-3a45-39fc-84ad-17c4c7bdc3f9)

target `bafu-2026` vs explicit model `ddefdbda-3a45-39fc-84ad-17c4c7bdc3f9-disagg` and hybrid `ddefdbda-3a45-39fc-84ad-17c4c7bdc3f9-hybrid`

**Strategy:** S2 — template transfer from a BAFU unit process of the same product; main amounts calibrated within 0.5-2x. BAFU ships the Swiss brown packaging glass as an aggregated xx dataset, but keeps the same product as a RER unit process (21 inputs). That structure is reused with the grid switched to CH (the datasets describe Vetropack's Swiss sites); ten amounts free within 0.5-2x.
**Calibrated inputs:** Dolomite, at plant [0.0294–0.118], Natural gas, high pressure, at consumer [1.78–7.14], Silica sand, at plant [0.143–0.574], Heavy fuel oil, at regional storage [0.0216–0.0866], Limestone, milled, loose, at plant [0.0209–0.0838], Light fuel oil, at regional storage [0.0209–0.0838], Soda, powder, at plant [0.043–0.172], Glass, from public collection, unsorted [0.278–1.11], Electricity, medium voltage, at grid [0.122–0.488]
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 3/50 within ±10 %, median |Δ| 61.3%
- kilogram mass covered within ±10 %: 0.1% of the target's total kg mass
- of the 1146 flows of the target, 1146 are determined by the solve (0 are round-off and are not scored; see lci.determined_flows)
- 54 of those 1146 within ±10 % (5%), median |Δ| 130.7%, 0 missing from the model, 636 extra
- hybrid vs target: 1 flows differ

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 54 | 5% |
| 10–20 % | 49 | 4% |
| 20–50 % | 145 | 13% |
| 50–100 % | 281 | 25% |
| > 100 % | 617 | 54% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (922 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Gravel [soil] (kilogram) | 0.622 | 0.292 | -53.1% | +0.33 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.505 | 0.0918 | -81.8% | +0.414 |
| Calcite [resources/in ground] (kilogram) | 0.129 | 0.0601 | -53.5% | +0.0693 |
| Dolomite [soil] (kilogram) | 0.103 | 0.03 | -70.9% | +0.073 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.099 | 0.0372 | -62.4% | +0.0618 |
| Sodium chloride [resources/in ground] (kilogram) | 0.0717 | 0.0305 | -57.4% | +0.0412 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.068 | 0.123 | +81.5% | -0.0554 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0384 | 0.543 | +1311.8% | -0.504 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0241 | 0.0532 | +121.1% | -0.0291 |
| Clay [soil] (kilogram) | 0.02 | 0.0353 | +76.2% | -0.0153 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.0125 | 0.00651 | -47.9% | +0.00598 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.00973 | 0.00543 | -44.2% | +0.0043 |
| Iron [Resources/Resources from ground] (kilogram) | 0.00599 | 0.00418 | -30.2% | +0.00181 |
| Calcium [Emissions/Emissions to water] (kilogram) | 0.00479 | 0.0019 | -60.4% | +0.0029 |
| Solids, Inorganic [water] (kilogram) | 0.0047 | 0.00167 | -64.4% | +0.00303 |
| calcium [Emissions/Emissions to water] (kilogram) | 0.0029 | 0.00829 | +185.6% | -0.00538 |
| Nitrogen Oxides [Emissions/Emissions to air] (kilogram) | 0.00253 | 0.000215 | -91.5% | +0.00232 |
| Silicon [Emissions/Emissions to water] (kilogram) | 0.00231 | 0.0015 | -34.9% | +0.000806 |
| Methane (fossil) [Emissions/Emissions to air] (kilogram) | 0.00158 | 0.000331 | -79.0% | +0.00125 |
| magnesium [Emissions/Emissions to water] (kilogram) | 0.00137 | 0.000909 | -33.7% | +0.000462 |

### kilo Becquerel (135 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 28.6 | 76.8 | +168.6% | -48.2 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 13.2 | 26.2 | +98.7% | -13 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.684 | 0.734 | +7.3% | -0.0499 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.53 | 1.05 | +98.8% | -0.524 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.0633 | 6.04 | +9449.5% | -5.98 |

### square meter (34 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| From Forest, Extensive [Land use/Land transformation] (square meter) | 0.00102 | 1.01e-06 | -99.9% | +0.00102 |
| To Forest, Intensive [Land use/Land transformation] (square meter) | 0.00101 | 0.00224 | +122.6% | -0.00123 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 0.000289 | 0.00119 | +309.8% | -0.000896 |
| From Arable, Non-irrigated [Land use/Land transformation] (square meter) | 0.000289 | 0.00115 | +296.6% | -0.000857 |
| To Mineral Extraction Site [Land use/Land transformation] (square meter) | 8.3e-05 | 3.1e-05 | -62.7% | +5.2e-05 |

### cubic meter (20 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 5.18 | 1.64 | -68.3% | +3.54 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 5.17 | 1.63 | -68.4% | +3.54 |
| Water [Resources/Resources from water] (cubic meter) | 0.00571 | 0.00627 | +9.8% | -0.000559 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 0.00487 | 0.00393 | -19.4% | +0.000945 |
| river water [Resources/Resources from water] (cubic meter) | 0.000633 | 0.000868 | +37.1% | -0.000235 |

### megajoule (20 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Waste Heat [air] (megajoule) | 10.2 | 5.13 | -49.7% | +5.08 |
| Natural Gas [Resources/Resources from ground] (megajoule) | 8.11 | 3.16 | -61.0% | +4.95 |
| Crude Oil [Resources/Resources from ground] (megajoule) | 1.11 | 3.57 | +220.4% | -2.45 |
| Waste Heat [air] (megajoule) | 1.04 | 0.927 | -10.7% | +0.111 |
| Hard Coal [Resources/Resources from ground] (megajoule) | 0.95 | 0.249 | -73.8% | +0.701 |

### square meter-year (14 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.132 | 0.215 | +62.9% | -0.083 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.00195 | 0.00218 | +11.5% | -0.000224 |
| Traffic Area, Rail/road Embankment [Land use/Land occupation] (square meter-year) | 0.00174 | 0.00278 | +60.2% | -0.00105 |
| Inland Water Bodies [land use] (square meter-year) | 0.000546 | 0.000163 | -70.2% | +0.000383 |
| Dump Site [Land use/Land occupation] (square meter-year) | 0.000448 | 0.000235 | -47.6% | +0.000213 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.00756 | 0.00821 | +8.6% | -0.000647 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0384 | 0.543 | +1311.8% |
| Fluorspar [soil] (kilogram) | 0.00021 | 0.00243 | +1055.9% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.000307 | 0.00262 | +753.5% |
| Kaolinite [soil] (kilogram) | 0.000441 | 0.00145 | +228.5% |
| Sodium [water] (kilogram) | 0.000311 | 0.000945 | +203.3% |
| calcium [Emissions/Emissions to water] (kilogram) | 0.0029 | 0.00829 | +185.6% |
| Barite [resources/in ground] (kilogram) | 0.000319 | 0.000748 | +134.3% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0241 | 0.0532 | +121.1% |
| Metamorphous rock, graphite containing [resources/in ground] (kilogram) | 0.00104 | 2.42e-07 | -100.0% |
| Nitrogen Oxides [Emissions/Emissions to air] (kilogram) | 0.00253 | 0.000215 | -91.5% |

## Structural checks

- ✓ 21 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✗ depends on system processes (rebuild those first): ['Polyethylene, HDPE, granulate, at plant', 'Feldspar, at plant']
- ✓ mass in: 0.783 kg technosphere + 0 kg resources per 1 kilogram product (informational)
- ✓ all inputs resolved

residual: 395 flows under-explained, 1387 over-explained (negative residual)

## Evidence

- bafu-2026: xx Packaging glass, brown, at plant [RER] (unit process, 21 inputs) — template transfer (S2) Same product and reference unit; grid electricity switched to CH.
- 2007 - LCI packagings and graphical papers - Hischier.pdf — packaging glass The bundled report is a 17-page overview and prints no inventory table, so the sibling unit process is the only evidence.
