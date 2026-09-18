#this is a namedtuple("CharacterizedRow", ["date", "amount", "flow", "activity"]) and we want this to be the return type
from dynamic_characterization.classes import CharacterizedRow 

# illustrative monthly water stress index [Jan, Feb, Mar, .., Dec] 
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
