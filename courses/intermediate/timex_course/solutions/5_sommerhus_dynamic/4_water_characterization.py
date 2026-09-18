from dynamic_characterization import characterize
from dynamic_characterization.classes import CharacterizedRow

# straight from the dynamic-characterization notebook, unchanged
water_stress_index_by_month = [0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.0, 1.0, 0.8, 0.6, 0.4, 0.3]


def characterize_water_scarcity(series, period: int = 1) -> CharacterizedRow:
    """A toy seasonal water scarcity characterization function"""
    month = series.date.month
    weight = water_stress_index_by_month[month - 1]
    impact = series.amount * weight

    return CharacterizedRow(
        date=np.array([series.date.to_datetime64()], dtype="datetime64[s]"),
        amount=np.array([impact], dtype="float64"),
        flow=series.flow,
        activity=series.activity,
    )


# ... and now pointed at a real supply chain instead of three dummy rows
water_rows = tlca.dynamic_inventory_df.query("flow == @water_flow.id")
water_scarcity = characterize(
    tlca.dynamic_inventory_df,
    characterization_functions={water_flow.id: characterize_water_scarcity},
)

print(f"withdrawn:  {water_rows['amount'].sum():,.0f} m3 over {len(water_rows)} withdrawals")
print(f"weighted:   {water_scarcity['amount'].sum():,.0f} stress-m3")
