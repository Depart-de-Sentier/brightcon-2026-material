def characterize_water_scarcity_prospective(series, period: int = 1) -> CharacterizedRow:
    """Seasonal weight, times a scarcity trend read off the year of the withdrawal."""
    month = series.date.month
    weight = water_stress_index_by_month[month - 1]
    trend = np.interp(series.date.year, [2025, 2075], [1.0, 1.6])  # flat outside the range

    return CharacterizedRow(
        date=np.array([series.date.to_datetime64()], dtype="datetime64[s]"),
        amount=np.array([series.amount * weight * trend], dtype="float64"),
        flow=series.flow,
        activity=series.activity,
    )


water_scarcity_prospective = characterize(
    tlca.dynamic_inventory_df,
    characterization_functions={water_flow.id: characterize_water_scarcity_prospective},
)

print(f"today's index:     {water_scarcity['amount'].sum():,.0f} stress-m3")
print(f"rising index:      {water_scarcity_prospective['amount'].sum():,.0f} stress-m3")
