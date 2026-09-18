water_inventory_df = pd.DataFrame(
    data={
        "date": pd.Series(["15-01-2026", "15-05-2026", "15-07-2026"], dtype="datetime64[s]"),
        "amount": pd.Series([100.0, 100.0, 100.0], dtype="float64"),  # m3 withdrawn
        "flow": pd.Series([10, 10, 10], dtype="int"), 
        "activity": pd.Series([1, 1, 1], dtype="int"),
    }
)

characterization_functions_water = {
    10: characterize_water_scarcity,
}

df_water_characterized = characterize(
    water_inventory_df,
    characterization_functions=characterization_functions_water,
)
df_water_characterized


import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3))  # own figure: the month labels are not dates
ax.bar(df_water_characterized["date"].dt.strftime("%b %Y"), df_water_characterized["amount"])
ax.set_ylabel("water scarcity impact [dummy units]")
ax.set_title("Same 100 m³ withdrawn, different season")
plt.show()
