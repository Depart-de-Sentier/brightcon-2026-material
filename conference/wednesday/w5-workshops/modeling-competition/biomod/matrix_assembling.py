import pandas as pd
import numpy as np

# Helper functions
def preprocess_feed_food(df):
    flow_fb_original = df.loc[(df['Source1'] == 'Feed & food products supply') & 
                              (df['Target1'] == 'Feed & bedding'), 'Value1'].values[0]
    flow_pb_original = df.loc[(df['Source1'] == 'Feed & food products supply') & 
                              (df['Target1'] == 'Plant-based food supply'), 'Value1'].values[0]    
    
    original_diag_ffps = df.loc[(df['Source1'] == 'Feed & food products supply') & 
                            (df['Target1'] == 'Feed & food products supply'), 'Value1'].values[0]
    
    diag_ffp = df.loc[(df['Source1'] == 'Feed & food products') & 
                      (df['Target1'] == 'Feed & food products'), 'Value1'].values[0]
    
    df.loc[(df['Source1'] == 'Feed & food products') & 
           (df['Target1'] == 'Feed & food products supply'), 'Value1'] = -diag_ffp
    
    updated_flow = df.loc[(df['Source1'] == 'Feed & food products') & 
                          (df['Target1'] == 'Feed & food products supply'), 'Value1'].values[0]
    df.loc[(df['Source1'] == 'Feed & food products supply') & 
           (df['Target1'] == 'Feed & food products supply'), 'Value1'] = -updated_flow
    
    ratio_fb = flow_fb_original / original_diag_ffps if original_diag_ffps != 0 else 0
    ratio_pb = flow_pb_original / original_diag_ffps if original_diag_ffps != 0 else 0
    
    new_diag_ffps = df.loc[(df['Source1'] == 'Feed & food products supply') & 
                           (df['Target1'] == 'Feed & food products supply'), 'Value1'].values[0]
    df.loc[(df['Source1'] == 'Feed & food products supply') & 
           (df['Target1'] == 'Feed & bedding'), 'Value1'] = ratio_fb * new_diag_ffps
    df.loc[(df['Source1'] == 'Feed & food products supply') & 
           (df['Target1'] == 'Plant-based food supply'), 'Value1'] = ratio_pb * new_diag_ffps
    
    updated_flow_fb = df.loc[(df['Source1'] == 'Feed & food products supply') & 
                             (df['Target1'] == 'Feed & bedding'), 'Value1'].values[0]
    updated_flow_pb = df.loc[(df['Source1'] == 'Feed & food products supply') & 
                             (df['Target1'] == 'Plant-based food supply'), 'Value1'].values[0]
    df.loc[(df['Source1'] == 'Feed & bedding') & 
           (df['Target1'] == 'Feed & bedding'), 'Value1'] = -updated_flow_fb
    df.loc[(df['Source1'] == 'Plant-based food supply') & 
           (df['Target1'] == 'Plant-based food supply'), 'Value1'] = -updated_flow_pb

    waste_mask = (df['Source1'] == 'Feed & food products') & (df['Target1'].str.startswith('Waste'))
    waste_flows = df[waste_mask].copy()
    df.loc[waste_mask, 'Value1'] = 0
    
    total_waste_out = -waste_flows['Value1'].sum()
    
    new_waste_rows = []
    for _, row in waste_flows.iterrows():
        original_value = row['Value1']
        target = row['Target1']
        fb_value = original_value * -ratio_fb
        pb_value = original_value * -ratio_pb
        new_waste_rows.append({'Source1': 'Feed & bedding', 'Target1': target, 'Value1': fb_value})
        new_waste_rows.append({'Source1': 'Plant-based food supply', 'Target1': target, 'Value1': pb_value})

    df = pd.concat([df, pd.DataFrame(new_waste_rows)], ignore_index=True)
    
    return df

def disag_feedfood(df):
    df['Value1'] = pd.to_numeric(df['Value1'], errors='coerce')
    
    waste_mask = (df['Source1'] == 'Feed & food products') & (df['Target1'].str.startswith('Waste'))
    waste_flows = df[waste_mask].copy()
    total_waste = waste_flows['Value1'].sum()
    absolute_total_waste = abs(total_waste)
    waste_flows['Proportion'] = waste_flows['Value1'].abs() / absolute_total_waste if absolute_total_waste != 0 else 0

    outflow_feed_bedding = abs(df.loc[(df['Source1'] == 'Feed & food products supply') & (df['Target1'] == 'Feed & bedding'), 'Value1'].values[0])
    outflow_plant = abs(df.loc[(df['Source1'] == 'Feed & food products supply') & (df['Target1'] == 'Plant-based food supply'), 'Value1'].values[0])
    total_outflow = outflow_feed_bedding + outflow_plant
    share_feed_bedding = outflow_feed_bedding / total_outflow if total_outflow else 0.5
    share_plant = outflow_plant / total_outflow if total_outflow else 0.5

    new_rows = []
    for _, row in waste_flows.iterrows():
        original_value = row['Value1']
        prop = row['Proportion']
        sign = np.sign(original_value)
        abs_val = abs(original_value)
        fb_value = abs_val * share_feed_bedding * prop * sign
        pb_value = abs_val * share_plant * prop * sign
        new_rows.append({'Source1': 'Feed & bedding', 'Target1': row['Target1'], 'Value1': fb_value})
        new_rows.append({'Source1': 'Plant-based food supply', 'Target1': row['Target1'], 'Value1': pb_value})

    new_df = pd.DataFrame(new_rows)
    df = pd.concat([df, new_df], ignore_index=True)

    fb_inflows = df[(df['Target1'] == 'Feed & bedding') & (df['Source1'] != 'Feed & bedding')]['Value1'].sum()
    fb_outflows = df[(df['Source1'] == 'Feed & bedding') & (df['Target1'] != 'Feed & bedding')]['Value1'].sum()
    pb_inflows = df[(df['Target1'] == 'Plant-based food supply') & (df['Source1'] != 'Plant-based food supply')]['Value1'].sum()
    pb_outflows = df[(df['Source1'] == 'Plant-based food supply') & (df['Target1'] != 'Plant-based food supply')]['Value1'].sum()

    fb_adjustment = -fb_inflows
    pb_adjustment = -pb_inflows

    fb_self_mask = (df['Source1'] == 'Feed & bedding') & (df['Target1'] == 'Feed & bedding')
    if not df[fb_self_mask].empty:
        df.loc[fb_self_mask, 'Value1'] = fb_adjustment
    else:
        df = pd.concat([df, pd.DataFrame([{'Source1': 'Feed & bedding', 'Target1': 'Feed & bedding', 'Value1': fb_adjustment}])], ignore_index=True)

    pb_self_mask = (df['Source1'] == 'Plant-based food supply') & (df['Target1'] == 'Plant-based food supply')
    if not df[pb_self_mask].empty:
        df.loc[pb_self_mask, 'Value1'] = pb_adjustment
    else:
        df = pd.concat([df, pd.DataFrame([{'Source1': 'Plant-based food supply', 'Target1': 'Plant-based food supply', 'Value1': pb_adjustment}])], ignore_index=True)

    return df

def redirect_flows(df, allowed_links):
    allowed_links_clean = {
        key.strip(): [t.strip() for t in targets]
        for key, targets in allowed_links.items()
    }

    df['Value1'] = pd.to_numeric(df['Value1'], errors='coerce')

    mask_fb = (df['Source1'] == 'Feed & food products supply') & (df['Target1'] == 'Feed & bedding')
    mask_pb = (df['Source1'] == 'Feed & food products supply') & (df['Target1'] == 'Plant-based food supply')
    
    outflow_fb = abs(df.loc[mask_fb, 'Value1'].values[0]) if not df[mask_fb].empty else 0
    outflow_pb = abs(df.loc[mask_pb, 'Value1'].values[0]) if not df[mask_pb].empty else 0
    total_outflow = outflow_fb + outflow_pb

    share_fb = outflow_fb / total_outflow if total_outflow else 0.5
    share_pb = outflow_pb / total_outflow if total_outflow else 0.5

    mask_original = df['Target1'] == 'Feed & food products'
    original_rows = df[mask_original].copy()
    df = df[~mask_original]

    fixed_rows = []
    flexible_rows = []

    for _, row in original_rows.iterrows():
        source = row['Source1'].strip()
        value = row['Value1']
        targets = allowed_links_clean.get(source, [])

        if len(targets) == 1:
            fixed_rows.append({'Source1': source, 'Target1': targets[0], 'Value1': value})
        elif len(targets) == 2:
            flexible_rows.append((source, value, targets))

    df_fixed = pd.DataFrame(fixed_rows)

    fixed_fb = df_fixed[df_fixed['Target1'] == 'Feed & bedding']['Value1'].sum()
    fixed_pb = df_fixed[df_fixed['Target1'] == 'Plant-based food supply']['Value1'].sum()

    total_flexible_value = sum(val for _, val, _ in flexible_rows)
    remaining_fb = (fixed_fb + fixed_pb + total_flexible_value) * share_fb - fixed_fb
    remaining_pb = (fixed_fb + fixed_pb + total_flexible_value) * share_pb - fixed_pb

    flexible_distribution = []
    for source, value, targets in flexible_rows:
        sign = np.sign(value)
        abs_val = abs(value)
    
        if remaining_fb + remaining_pb == 0:
            fb_ratio = 0.5
        else:
            fb_ratio = abs(remaining_fb) / (abs(remaining_fb) + abs(remaining_pb))
    
        value_fb = abs_val * fb_ratio * sign
        value_pb = abs_val * (1 - fb_ratio) * sign
    
        flexible_distribution.append({
            'Source1': source,
            'Target1': 'Feed & bedding',
            'Value1': value_fb
        })
        flexible_distribution.append({
            'Source1': source,
            'Target1': 'Plant-based food supply',
            'Value1': value_pb
        })

    df_flexible = pd.DataFrame(flexible_distribution)
    df_new = pd.concat([df, df_fixed, df_flexible], ignore_index=True)

    return df_new

def sort_matrix(df):
    col_sums = df.sum(axis=0)
    
    high_sum_cols = col_sums[col_sums > 1].index
    low_sum_cols = col_sums[col_sums <= 1].index
    
    high_sum_cols = sorted(high_sum_cols)
    low_sum_cols = sorted(low_sum_cols)
    
    sorted_cols = high_sum_cols + low_sum_cols
    
    df_sorted = df.loc[sorted_cols, sorted_cols]
    
    return df_sorted

#Disaggregate exports to ensure non-substitutability among them.
#They are placed at the edges of the matrix to avoid messing with indexes

def disaggregate_export(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy().astype(float)
    
    if 'Exports' not in df.index or 'Exports' not in df.columns:
        raise ValueError("'Exports' must be both in the index and the columns of the dataframe.")

    # Identify rows with negative values in the 'Export' column
    negative_exports = df.loc[df['Exports'] < 0, 'Exports']

    # Store the value on the Export diagonal
    export_diag_value = df.loc['Exports', 'Exports']

    # Drop the original 'Export' row and column
    #df = df.drop(index='Exports', columns='Exports')

    for idx, val in negative_exports.items():
        name = f"Export of {idx}"
        df.loc[name] = pd.Series(0.0, index=df.columns, dtype='float64')
        df[name] = pd.Series(0.0, index=df.index, dtype='float64')

        # Assign the values as specified
        df.loc[idx, name] = val           # original negative value in the new column
        df.loc[name, name] = -val         # opposite sign on diagonal
        #df.loc[name, idx] = val           # symmetric position (optional if keeping symmetry)

    df.loc['Exports'] = pd.Series(0.0, index=df.columns, dtype='float64')
    df['Exports'] = pd.Series(0.0, index=df.index, dtype='float64')
    
    return df

def build_matrix(
    input_csv_path,
    allowed_links,
    waste_subcategories,
    nutrient_aggregations
):
    """
    This function reads disaggregated data, processes it, and builds the final matrix.
    Key modeling choices are passed as parameters.

    Args:
        input_csv_path (str or pd.DataFrame): The file path to the input CSV data or a pandas DataFrame.
        allowed_links (dict): A dictionary defining valid pathways for redirecting flows,
                              e.g., {'Cereals': ['Feed & bedding', 'Plant-based food supply']}.
        waste_subcategories (list): A list of strings identifying the waste categories to be aggregated.
        nutrient_aggregations (list): A list of tuples defining how to aggregate nutrient categories.
                                      Each tuple should be (new_name, list_of_subcategories).
    
    Returns:
        pd.DataFrame: The final, processed matrix.
    """
    if isinstance(input_csv_path, str):
        inputdf = pd.read_csv(input_csv_path)
    elif isinstance(input_csv_path, pd.DataFrame):
        inputdf = input_csv_path.copy()
    else:
        raise TypeError("Input must be a file path (str) or a pandas DataFrame.")

    # Temporary solution. Discrepancies in the source database
    # fix discrepanchy on biofuels
    # Step 1: Calculate the sum for "Biofuels"
    biofuels_sum = inputdf.loc[inputdf['Target'] == 'Biofuels', 'Value (THOUSAND TONNES)'].sum()

    # Step 2: Update the value for "Bioenergy"
    inputdf.loc[inputdf['Target'] == 'Bioenergy', 'Value (THOUSAND TONNES)'] = biofuels_sum

    # FIX imports
    inputdf.loc[(inputdf['Source'] == 'Imports') & (inputdf['Detail'] == 'Plant-based food'), 
        'Detail'] = 'Imported Plant-based food'
    inputdf.loc[(inputdf['Source'] == 'Imports') & (inputdf['Detail'] == 'Processed products (biomass eq.)'),
        'Detail'] = 'Imported Processed products (biomass eq.)'
    inputdf.loc[(inputdf['Source'] == 'Imports') & (inputdf['Detail'] == 'Fish & seafood'),
        'Detail'] = 'Imported Fish & seafood'

    # Add detail for Grazing process output: Grazing products
    inputdf.loc[(inputdf['Source'] == 'Grazing') & (inputdf['Detail'] == 'Agriculture biomass'), 'Detail'] = 'Grazing products'

    # Rename nutrients to ensure separate flows for animal- and plant-based food
    inputdf.loc[(inputdf['Source'] == 'Plant-based food supply') & (inputdf['Detail'] == 'Carbohydrates'), 'Detail'] = 'Plant-based Carbohydrates'
    inputdf.loc[(inputdf['Source'] == 'Plant-based food supply') & (inputdf['Detail'] == 'Fats'), 'Detail'] = 'Plant-based Fats'
    inputdf.loc[(inputdf['Source'] == 'Plant-based food supply') & (inputdf['Detail'] == 'Others'), 'Detail'] = 'Plant-based Other nutrients'
    inputdf.loc[(inputdf['Source'] == 'Plant-based food supply') & (inputdf['Detail'] == 'Proteins'), 'Detail'] = 'Plant-based Proteins'

    inputdf.loc[(inputdf['Source'] == 'Feed & bedding') & (inputdf['Detail'] == 'Carbohydrates'), 'Detail'] = 'Animal-based Carbohydrates'
    inputdf.loc[(inputdf['Source'] == 'Feed & bedding') & (inputdf['Detail'] == 'Fats'), 'Detail'] = 'Animal-based Fats'
    inputdf.loc[(inputdf['Source'] == 'Feed & bedding') & (inputdf['Detail'] == 'Others'), 'Detail'] = 'Animal-based Other nutrients'
    inputdf.loc[(inputdf['Source'] == 'Feed & bedding') & (inputdf['Detail'] == 'Proteins'), 'Detail'] = 'Animal-based Proteins'

    # Rename detail for "Products" in Forestry
    inputdf.loc[(inputdf['Source'] == 'Material industry') & (inputdf['Detail'] == 'Products'), 'Detail'] = 'Material industry products'
    inputdf.loc[(inputdf['Source'] == 'Solid wood products') & (inputdf['Detail'] == 'Products'), 'Detail'] = 'Solid wood-based products'
    inputdf.loc[(inputdf['Source'] == 'Wood pulp') & (inputdf['Detail'] == 'Products'), 'Detail'] = 'Wood pulp products'
    inputdf.loc[(inputdf['Source'] == 'Solid wood products imports') & (inputdf['Detail'] == 'Products'), 'Detail'] = 'Imported solid wood products'
    inputdf.loc[(inputdf['Source'] == 'Wood pulp imports') & (inputdf['Detail'] == 'Products'), 'Detail'] = 'Imported wood pulp'

    inputdf["Source1"] = inputdf["Detail"] 
    inputdf["Target1"] = inputdf["Target"] 
    inputdf["Target"] = inputdf["Detail"] 
    inputdf["Value1"] = inputdf["Value (THOUSAND TONNES)"] * -1 
    inputdf = inputdf.drop(columns = ["Sector", "Target"])
    inputdf = inputdf.rename(columns={'Detail': 'Target'})

    # Fix double fishmeal for feed: keep the one from fisheries (possible discrepancy?)
    # Unique linkage between Agriculture and Fisheries
    inputdf = inputdf[~((inputdf['Source'] == 'Fishmeal & oil for feed') & (inputdf['Target'] == 'Fishmeal & oil for feed'))]
    inputdf.loc[(inputdf['Source'] == 'Fishmeal & oil') & (inputdf['Target'] == 'Fishmeal & oil') &
        (inputdf['Target1'] == 'Fishmeal & oil for animal husbandry'), 'Target1'] = 'Feed & food products'

    # Rename agriculture biomass to avoid merging
    inputdf.loc[(inputdf['Source'] == 'Biofuels') & (inputdf['Target'] == 'Agriculture biomass'), 'Target'] = 'Biofuels for bioenergy'
    inputdf.loc[(inputdf['Source1'] == 'Agriculture biomass') & (inputdf['Target1'] == 'Bioenergy'), 'Source1'] = 'Biofuels for bioenergy'
    inputdf.loc[(inputdf['Source'] == 'Feed & food products') & (inputdf['Target'] == 'Agriculture biomass'), 'Target'] = 'Feed & food products supply'
    inputdf.loc[(inputdf['Source1'] == 'Agriculture biomass') & (inputdf['Target1'] == 'Feed & bedding'), 'Source1'] = 'Feed & food products supply'
    inputdf.loc[(inputdf['Source1'] == 'Agriculture biomass') & (inputdf['Target1'] == 'Plant-based food supply'), 'Source1'] = 'Feed & food products supply'

    # Rename aquaculture to avoid merging
    inputdf.loc[(inputdf['Source'] == 'Aquaculture') & (inputdf['Target'] == 'Aquaculture'), 'Target'] = 'Aquaculture products'
    inputdf.loc[(inputdf['Source1'] == 'Aquaculture') & (inputdf['Target1'] == 'Aquatic-based food'), 'Source1'] = 'Aquaculture products'

    # Rename Fishmeal & oil to avoid merging
    inputdf.loc[(inputdf['Source'] == 'Fishmeal & oil') & (inputdf['Target'] == 'Fishmeal & oil'), 'Target'] = 'Fishmeal & oil products'
    inputdf.loc[(inputdf['Source1'] == 'Fishmeal & oil') & (inputdf['Target1'] == 'Aquaculture'), 'Source1'] = 'Fishmeal & oil products'
    inputdf.loc[(inputdf['Source1'] == 'Fishmeal & oil') & (inputdf['Target1'] == 'Exports'), 'Source1'] = 'Fishmeal & oil products'
    inputdf.loc[(inputdf['Source1'] == 'Fishmeal & oil') & (inputdf['Target1'] == 'Feed & food products'), 'Source1'] = 'Fishmeal & oil products'

    # Rename residues to ensure origin from crop production
    inputdf.loc[(inputdf['Source'] == 'Cereals residues') & (inputdf['Target'] == 'Cereals residues'), 'Source'] = 'Cereals Production'
    inputdf.loc[(inputdf['Source'] == 'Fibre Crops residues') & (inputdf['Target'] == 'Fibre Crops residues'), 'Source'] = 'Fibre Crops Production'
    inputdf.loc[(inputdf['Source'] == 'Fodder crops residues') & (inputdf['Target'] == 'Fodder crops residues'), 'Source'] = 'Fodder crops Production'
    inputdf.loc[(inputdf['Source'] == 'Fruits residues') & (inputdf['Target'] == 'Fruits residues'), 'Source'] = 'Fruits Production'
    inputdf.loc[(inputdf['Source'] == 'Oil crops residues') & (inputdf['Target'] == 'Oil crops residues'), 'Source'] = 'Oil crops Production'
    inputdf.loc[(inputdf['Source'] == 'Olive trees residues') & (inputdf['Target'] == 'Olive trees residues'), 'Source'] = 'Olive trees Production'
    inputdf.loc[(inputdf['Source'] == 'Other industrial crops residues') & (inputdf['Target'] == 'Other industrial crops residues'), 'Source'] = 'Other industrial crops Production'
    inputdf.loc[(inputdf['Source'] == 'Pulses & protein crops residues') & (inputdf['Target'] == 'Pulses & protein crops residues'), 'Source'] = 'Pulses & protein crops Production'
    inputdf.loc[(inputdf['Source'] == 'Root crops residues') & (inputdf['Target'] == 'Root crops residues'), 'Source'] = 'Root crops Production'
    inputdf.loc[(inputdf['Source'] == 'Vegetables residues') & (inputdf['Target'] == 'Vegetables residues'), 'Source'] = 'Vegetables Production'

    # Create a pivot table with the sum of 'Value1' grouped by 'Target1'
    pivot_dft = inputdf.pivot_table(values='Value1', index='Target1', aggfunc='sum')
    pivot_dft = pivot_dft.reset_index()
    pivot_dft["Source1"] = pivot_dft["Target1"] 
    pivot_dft["Value1"] = pivot_dft["Value1"] *-1

    # Apply correction for circular input in Aquaculture
    pivot_dft.loc[(pivot_dft['Source1'] == 'Aquaculture') & (pivot_dft['Target1'] == 'Aquaculture'), 'Value1'] = 0

    # Create a pivot table with the sum of 'Value1' grouped by 'Source1'
    pivot_dfs = inputdf.pivot_table(values='Value1', index='Source1', aggfunc='sum')
    pivot_dfs = pivot_dfs.reset_index()
    pivot_dfs["Target1"] = pivot_dfs["Source1"] 
    pivot_dfs["Value1"] = pivot_dfs["Value1"] *-1

    # Create a pivot table with the sum of 'Value (THOUSAND TONNES)' grouped by 'Source' and 'Target' 
    pivot_df2 = inputdf.pivot_table(
        values='Value (THOUSAND TONNES)', 
        index=['Source', 'Target'], 
        aggfunc='sum'
    )
    pivot_df2 = pivot_df2.reset_index()
    pivot_df2 = pivot_df2.rename(columns={'Source': 'Source1', 'Target': 'Target1', 'Value (THOUSAND TONNES)': 'Value1'})
    pivot_df2["Value1"] = pivot_df2["Value1"] *-1

    # Create a pivot table with the sum of 'Value (THOUSAND TONNES)' grouped by 'Source'
    pivot_df3 = inputdf.pivot_table(
        values='Value (THOUSAND TONNES)', 
        index=['Source'], 
        aggfunc='sum'
    )
    pivot_df3 = pivot_df3.reset_index()
    pivot_df3 = pivot_df3.rename(columns={'Source': 'Source1', 'Value (THOUSAND TONNES)': 'Value1'})
    pivot_df3["Target1"] = pivot_df3["Source1"]

    inputdf = pd.concat([inputdf, pivot_dfs, pivot_dft, pivot_df2], ignore_index=True)

    exception_mask = (pivot_df3['Source1'] == 'Aquaculture') & (pivot_df3['Target1'] == 'Aquaculture')
    pivot_df3_filtered = pivot_df3[exception_mask | ~pivot_df3.set_index(['Source1', 'Target1']).index.isin(pivot_dft.set_index(['Source1', 'Target1']).index)]
    inputdf = pd.concat([inputdf, pivot_df3_filtered], ignore_index=True)

    inputtodisag = pd.DataFrame()
    inputtodisag["Value1"] = inputdf["Value1"] 
    inputtodisag["Source1"] = inputdf["Source1"] 
    inputtodisag["Target1"] = inputdf["Target1"]

    preprocessed_df = preprocess_feed_food(inputtodisag)

    processed_df = disag_feedfood(preprocessed_df)
    pro_df = redirect_flows(processed_df, allowed_links)
    pro_df = pro_df[~pro_df['Source1'].isin(['Feed & food products', 'Feed & food products supply'])]
    matrix = pro_df.pivot_table(values='Value1', index='Source1', columns='Target1', aggfunc='sum').fillna(0)

    sorted_df = sort_matrix(matrix)

    df = sorted_df
    df = df.astype(float)

    # Using the parameter for waste subcategories
    diagonal_sum = df.loc[waste_subcategories, waste_subcategories].sum().sum()

    sum_rows = df.loc[waste_subcategories].sum(axis=0)
    for sub in waste_subcategories:
        sum_rows[sub] -= df.loc[sub, sub]
    df.loc["Waste"] += sum_rows
    df.loc["Waste", "Waste"] += diagonal_sum

    sum_cols = df[waste_subcategories].sum(axis=1)
    for sub in waste_subcategories:
        sum_cols[sub] -= df.loc[sub, sub]
    df["Waste"] += sum_cols

    df = df.drop(index=waste_subcategories).drop(columns=waste_subcategories)

    food_waste_to_waste = df.loc["Food waste", "Waste"]

    if food_waste_to_waste < 0:
        df.loc["Waste", "Waste"] += abs(food_waste_to_waste)

    df.loc["Waste","Food waste"] = 0.0
    df.loc["Food waste"] = 0.0

    # Using the parameter for nutrient aggregations
    original_index = df.index.tolist()
    new_index = original_index.copy()

    for new_name, sub_list in nutrient_aggregations:
        first_sub = sub_list[0]
        pos = new_index.index(first_sub)
        new_index[pos] = new_name
        for sub in sub_list[1:]:
            if sub in new_index:
                new_index.remove(sub)

    new_columns = new_index.copy()

    for new_name, sub_list in nutrient_aggregations:
        df.loc[new_name] = 0.0
        df[new_name] = 0.0
        diagonal_sum = df.loc[sub_list, sub_list].sum().sum()
        sum_rows = df.loc[sub_list].sum(axis=0)
        for sub in sub_list:
            sum_rows[sub] -= df.loc[sub, sub]
        df.loc[new_name] += sum_rows
        df.loc[new_name, new_name] += diagonal_sum
        sum_cols = df[sub_list].sum(axis=1)
        for sub in sub_list:
            sum_cols[sub] -= df.loc[sub, sub]
        df[new_name] += sum_cols

    subcategories_to_remove = [sub for _, subs in nutrient_aggregations for sub in subs]
    df = df.drop(index=subcategories_to_remove).drop(columns=subcategories_to_remove)
    df = df.reindex(index=new_index, columns=new_columns)

    df = disaggregate_export(df) # Call disaggregate_export here

    return df
