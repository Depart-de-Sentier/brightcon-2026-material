import pandas as pd

def aggregate_and_pivot(df, x_col="year", flow_col="flow", value_col="value", rename_map=None):
    """Aggregates tidy flow data (max 1 value per x-value per flow) and pivots it into a wide DataFrame indexed by x-values.
    """
    aggregated = (
        df.groupby([x_col, flow_col], as_index=False)[value_col]
        .sum()
        .sort_values(x_col)
    )

    # pivot into wide format: rows = years, columns = flows
    wide_df = aggregated.pivot(
        index=x_col, columns=flow_col, values=value_col
    )

    # optionally, rename:
    if rename_map: wide_df.rename(columns=rename_map, inplace=True)

    return wide_df