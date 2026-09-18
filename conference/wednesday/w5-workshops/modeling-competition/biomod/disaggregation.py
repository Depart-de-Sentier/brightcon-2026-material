import pandas as pd
import numpy as np
from scipy.optimize import linprog

def filter_data(df, agriculture_filters, fisheries_filters, forestry_filters):
    """
    Filters the DataFrame based on the provided filter criteria for each sector.
    """
    df = df[df['Level_Sankey (Id)'] == 'L3']
    df = df[df['Unit (Id)'] == 'KT_DRY_NET']
    
    df_agriculture = df[df['Sector'] == 'Agriculture']
    df_agriculture = df_agriculture[
        (df_agriculture['Year'] == agriculture_filters['Year']) & 
        (df_agriculture['Geopolitical Entity (Id)'] == agriculture_filters['Geopolitical Entity (Id)'])
    ]

    df_fisheries = df[df['Sector'] == 'Fisheries']
    df_fisheries = df_fisheries[df_fisheries['Year'] == fisheries_filters['Year']]
    df_fisheries_aggregated = df_fisheries.groupby([
        'Sector', 'Year', 'Level_Sankey (Id)', 'Level_Sankey', 'Lifecycle Step',
        'Lifecycle Step (Id)', 'Source', 'Source (Id)', 'Target', 'Target (Id)',
        'Flow', 'Flow (Id)', 'Unit', 'Unit (Id)'
    ], as_index=False).agg({'Value (THOUSAND TONNES)': 'sum'})
    df_fisheries_aggregated['Geopolitical Entity (Id)'] = fisheries_filters['Geopolitical Entity (Id)']
    df_fisheries_aggregated['Geopolitical Entity'] = fisheries_filters['Geopolitical Entity']

    df_forestry = df[df['Sector'] == 'Forestry']
    df_forestry = df_forestry[
        (df_forestry['Year'] == forestry_filters['Year']) & 
        (df_forestry['Geopolitical Entity (Id)'] == forestry_filters['Geopolitical Entity (Id)'])
    ]

    filtered_df = pd.concat([df_agriculture, df_fisheries_aggregated, df_forestry])
    filtered_df = filtered_df[['Sector', 'Source', 'Flow', 'Target', 'Value (THOUSAND TONNES)']]
    filtered_df = filtered_df.rename(columns={'Flow': 'Detail'})

    return filtered_df

def redistribute_flows_agriculture(df, target_mappings, import_mappings):
    df = df.copy()
    df['Value (THOUSAND TONNES)'] = pd.to_numeric(df['Value (THOUSAND TONNES)'], errors='coerce')
    
    inflows = df[df['Target'] == 'Biomass supply']
    outflows = df[df['Source'] == 'Biomass supply']
    
    sources = list(inflows['Source'].unique())
    targets = list(outflows['Target'].unique())
    
    non_import_inflows = inflows[inflows['Source'] != 'Imports']
    import_inflows = inflows[inflows['Source'] == 'Imports']
    
    source_values = non_import_inflows.groupby('Source')['Value (THOUSAND TONNES)'].sum()
    
    import_details = {}
    for _, row in import_inflows.iterrows():
        detail = row['Detail']
        value = row['Value (THOUSAND TONNES)']
        if detail not in import_details:
            import_details[detail] = 0
        import_details[detail] += value
    
    target_values = outflows.groupby('Target')['Value (THOUSAND TONNES)'].sum()
    
    n_sources = len(sources)
    n_targets = len(targets)
    
    valid_flows = np.zeros((n_sources, n_targets))
    for i, source in enumerate(sources):
        for j, target in enumerate(targets):
            is_valid = False
            if source != 'Imports':
                for mapping in target_mappings.values():
                    if source in mapping['sources'] and target in mapping['targets']:
                        is_valid = True
                        break
            else:
                for detail in import_details.keys():
                    if detail in import_mappings and target in import_mappings.get(detail, []):
                        is_valid = True
                        break
            valid_flows[i, j] = 1 if is_valid else 0
    
    total_target_value = target_values.sum()
    new_connections = []
    
    for i, source in enumerate(sources):
        if source != 'Imports':
            source_detail = non_import_inflows[non_import_inflows['Source'] == source]['Detail'].iloc[0]
            source_value = source_values.get(source, 0)
            valid_target_indices = np.where(valid_flows[i, :] == 1)[0]
            
            if len(valid_target_indices) == 0:
                continue
            
            target_proportions = np.zeros(len(valid_target_indices))
            for k, j in enumerate(valid_target_indices):
                target = targets[j]
                target_proportions[k] = target_values.get(target, 0) / total_target_value if total_target_value > 0 else 0
            
            if np.sum(target_proportions) > 0:
                target_proportions = target_proportions / np.sum(target_proportions)
            else:
                target_proportions = np.ones(len(valid_target_indices)) / len(valid_target_indices)

            for k, j in enumerate(valid_target_indices):
                target = targets[j]
                flow_value = source_value * target_proportions[k]
                if flow_value < 0.01:
                    flow_value = 0.01
                new_connections.append({
                    'Source': source, 'Target': target, 'Detail': source_detail,
                    'Value (THOUSAND TONNES)': flow_value
                })
        else:
            for detail, detail_value in import_details.items():
                if detail_value <= 0:
                    continue
                
                valid_targets_for_detail = [t for t in import_mappings.get(detail, []) if t in targets]
                if len(valid_targets_for_detail) == 0:
                    continue
                
                total_valid_target_value = sum(target_values.get(t, 0) for t in valid_targets_for_detail)
                
                for target in valid_targets_for_detail:
                    proportion = (target_values.get(target, 0) / total_valid_target_value) if total_valid_target_value > 0 else (1.0 / len(valid_targets_for_detail))
                    flow_value = detail_value * proportion
                    if flow_value < 0.01:
                        flow_value = 0.01
                    new_connections.append({
                        'Source': source, 'Target': target, 'Detail': detail,
                        'Value (THOUSAND TONNES)': flow_value
                    })

    new_df = pd.DataFrame(new_connections)
    target_sums = new_df.groupby('Target')['Value (THOUSAND TONNES)'].sum()

    for target in targets:
        if target in target_sums:
            current_sum = target_sums[target]
            required_sum = target_values.get(target, 0)
            if current_sum > 0:
                scale_factor = required_sum / current_sum
                new_df.loc[new_df['Target'] == target, 'Value (THOUSAND TONNES)'] *= scale_factor

    for source in sources:
        if source != 'Imports':
            current_sum = new_df[new_df['Source'] == source]['Value (THOUSAND TONNES)'].sum()
            required_sum = source_values.get(source, 0)
            if current_sum > 0:
                scale_factor = required_sum / current_sum
                new_df.loc[new_df['Source'] == source, 'Value (THOUSAND TONNES)'] *= scale_factor
        else:
            for detail, required_sum in import_details.items():
                if required_sum <= 0:
                    continue
                current_sum = new_df[(new_df['Source'] == source) & (new_df['Detail'] == detail)]['Value (THOUSAND TONNES)'].sum()
                if current_sum > 0:
                    scale_factor = required_sum / current_sum
                    new_df.loc[(new_df['Source'] == source) & (new_df['Detail'] == detail), 'Value (THOUSAND TONNES)'] *= scale_factor
    
    final_df = pd.concat([
        df[~(df['Source'].isin(['Biomass supply']) | df['Target'].isin(['Biomass supply']))],
        new_df
    ]).drop_duplicates()
    final_df['Sector'] = 'Agriculture'
    
    return final_df

def redistribute_flows_fisheries(df, validity_rules, initial_flexibility=1e-4, min_flexibility=1e-8, reduction_factor=0.5):
    df = df.copy()
    value_col = 'Value (THOUSAND TONNES)'
    
    inflows = df[df['Target'] == 'Biomass supply']
    outflows = df[df['Source'] == 'Biomass supply']
    independent_flows = df[
        (df['Source'] != 'Biomass supply') & 
        (df['Target'] != 'Biomass supply')
    ]
    
    sources = list(inflows['Source'].unique())
    targets = list(outflows['Target'].unique())

    valid_flows_matrix = np.ones((len(sources), len(targets)))
    for i, source in enumerate(sources):
        for j, target in enumerate(targets):
            if source in validity_rules:
                if isinstance(validity_rules[source], dict):
                    detail = inflows[inflows['Source'] == source]['Detail'].iloc[0]
                    if detail in validity_rules[source] and target not in validity_rules[source][detail]:
                        valid_flows_matrix[i, j] = 0
                elif target not in validity_rules[source]:
                    valid_flows_matrix[i, j] = 0

    n_vars = len(sources) * len(targets)
    current_flexibility = initial_flexibility
    
    while current_flexibility >= min_flexibility:
        A_ub, b_ub = [], []
        upper_flexibility, lower_flexibility = 1 + current_flexibility * 2, 1 - current_flexibility * 2
        
        for i, source in enumerate(sources):
            row = np.zeros(n_vars)
            row[i*len(targets):(i+1)*len(targets)] = 1
            A_ub.append(row)
            b_ub.append(float(inflows[inflows['Source'] == source][value_col].sum()) * upper_flexibility)
            A_ub.append(-row)
            b_ub.append(-float(inflows[inflows['Source'] == source][value_col].sum()) * lower_flexibility)
        
        for j, target in enumerate(targets):
            row = np.zeros(n_vars)
            row[j::len(targets)] = 1
            A_ub.append(row)
            b_ub.append(float(outflows[outflows['Target'] == target][value_col].sum()) * upper_flexibility)
            A_ub.append(-row)
            b_ub.append(-float(outflows[outflows['Target'] == target][value_col].sum()) * lower_flexibility)
        
        for i in range(len(sources)):
            for j in range(len(targets)):
                if valid_flows_matrix[i, j] == 0:
                    row = np.zeros(n_vars)
                    row[i*len(targets) + j] = 1
                    A_ub.append(row)
                    b_ub.append(0.0)
        
        c = np.ones(n_vars)
        penalty_factor = 1e6
        for i in range(len(sources)):
            for j in range(len(targets)):
                if valid_flows_matrix[i, j] == 1:
                    c[i * len(targets) + j] += penalty_factor * 1 / len(targets)
        
        result = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=[(0, None)] * n_vars, method='highs')
        
        if result.success:
            print(f"Solution found with flexibility: {current_flexibility}")
            break
        current_flexibility *= reduction_factor
    
    if not result.success:
        raise ValueError(f"No feasible solution found even with minimum flexibility of {min_flexibility}")
    
    flows = result.x.reshape((len(sources), len(targets)))
    new_flows = []
    for i, source in enumerate(sources):
        detail = inflows[inflows['Source'] == source]['Detail'].iloc[0]
        for j, target in enumerate(targets):
            if flows[i, j] > 1e-6:
                new_flows.append({
                    'Source': source, 'Detail': detail, 'Target': target,
                    'Value (THOUSAND TONNES)': flows[i, j]
                })
    
    result_df = pd.concat([pd.DataFrame(new_flows), independent_flows])
    result_df['Sector'] = 'Fisheries'
    
    return result_df.groupby(['Sector', 'Source', 'Detail', 'Target'])[value_col].sum().reset_index()

def redistribute_roundwood_flows(data):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")

    incoming_roundwood = data[data['Target'] == 'Roundwood']
    outgoing_roundwood = data[data['Source'] == 'Roundwood']
    original_target_details = list(outgoing_roundwood.groupby(['Target', 'Detail']).size().index)
    total_input = incoming_roundwood['Value (THOUSAND TONNES)'].sum()

    energy_bark = outgoing_roundwood[(outgoing_roundwood['Detail'] == 'Bark') & (outgoing_roundwood['Target'] == 'Energy (prev. node)')]['Value (THOUSAND TONNES)'].sum()
    energy_primary = outgoing_roundwood[(outgoing_roundwood['Detail'] == 'Primary wood') & (outgoing_roundwood['Target'] == 'Energy (prev. node)')]['Value (THOUSAND TONNES)'].sum()
    total_energy = energy_bark + energy_primary
    prop_bark = energy_bark / total_energy if total_energy > 0 else 0.0
    prop_primary = energy_primary / total_energy if total_energy > 0 else 0.0

    new_flows = []
    for _, source_row in incoming_roundwood.iterrows():
        source, value = source_row['Source'], source_row['Value (THOUSAND TONNES)']
        energy_allocation = (value / total_input) * total_energy if total_input > 0 else 0
        material_val = value - energy_allocation

        for target, detail in original_target_details:
            val = 0
            if target == 'Energy (prev. node)':
                if detail == 'Bark': val = energy_allocation * prop_bark
                elif detail == 'Primary wood': val = energy_allocation * prop_primary
            elif target == 'Material industry' and detail == 'Primary wood':
                val = material_val
            new_flows.append({
                'Source': source, 'Detail': detail, 'Target': target,
                'Value (THOUSAND TONNES)': round(val, 1), 'Sector': 'Forestry'
            })

    df_cleaned = data[~((data['Target'] == 'Roundwood') | (data['Source'] == 'Roundwood'))]
    df_final = pd.concat([df_cleaned, pd.DataFrame(new_flows)], ignore_index=True)
    return df_final

def disaggregate_feed_food_flows(df_final, allowed_links):
    ffp_in = df_final[df_final['Target'] == 'Feed & food products']
    detail_totals = ffp_in.groupby('Source')['Value (THOUSAND TONNES)'].sum()
    total_ffp = detail_totals.sum()

    ffp_src = df_final[df_final['Source'] == 'Feed & food products']
    waste_streams = ['Waste Anaerobic Digestion', 'Waste Composting', 'Waste Disposal', 'Waste Other']
    waste_totals = {w: ffp_src.loc[ffp_src['Target'] == w, 'Value (THOUSAND TONNES)'].sum() for w in waste_streams}
    feed_bed_tot = ffp_src.loc[ffp_src['Target'] == 'Feed & bedding', 'Value (THOUSAND TONNES)'].sum()
    plant_food_tot = ffp_src.loc[ffp_src['Target'] == 'Plant-based food supply', 'Value (THOUSAND TONNES)'].sum()

    disagg = []
    for det, val_det in detail_totals.items():
        share = (val_det / total_ffp) if total_ffp > 0 else 0
        for tgt in allowed_links.get(det, []):
            grp_tot = feed_bed_tot if tgt == 'Feed & bedding' else plant_food_tot
            v = max(share * grp_tot, 0.01)
            disagg.append({'Source': det, 'Detail': det, 'Target': tgt, 'Value (THOUSAND TONNES)': v})
        for w in waste_streams:
            v = max(share * waste_totals.get(w, 0), 0.01)
            disagg.append({'Source': det, 'Detail': det, 'Target': w, 'Value (THOUSAND TONNES)': v})

    df_final = df_final[df_final['Source'] != 'Feed & food products']
    df_final = pd.concat([df_final, pd.DataFrame(disagg)], ignore_index=True)
    return df_final

def disaggregate(df, agriculture_filters, fisheries_filters, forestry_filters,
                 target_mappings, import_mappings,
                 initial_flexibility, min_flexibility, reduction_factor,
                 fisheries_validity_rules, feed_food_allowed_links):
    """
    This function takes a DataFrame and a set of parameters to perform disaggregation.
    """
    filtered_df = filter_data(df, agriculture_filters, fisheries_filters, forestry_filters)

    for index, row in filtered_df[(filtered_df['Source'] == 'Residues') & (filtered_df['Target'] == 'Biomass supply')].iterrows():
        match = filtered_df[
            (filtered_df['Source'] == 'Biomass supply') &
            (filtered_df['Target'] == 'Residues - unknown use') &
            (filtered_df['Detail'] == row['Detail'])
        ]
        if not match.empty:
            filtered_df.at[index, 'Value (THOUSAND TONNES)'] -= match.iloc[0]['Value (THOUSAND TONNES)']
    
    condition = filtered_df['Target'] == 'Residues - unknown use'
    filtered_df.loc[condition, 'Source'] = filtered_df['Detail'] + ' Production'
    filtered_df.loc[condition, 'Detail'] += ' residues'
    
    filtered_df.loc[filtered_df['Source'] == 'Crop production', 'Source'] = filtered_df['Detail'] + ' Production'
    
    condition_residues = filtered_df['Source'] == 'Residues'
    filtered_df.loc[condition_residues, 'Source'] = filtered_df['Detail'] + ' residues'
    filtered_df.loc[condition_residues, 'Detail'] = filtered_df['Source']

    agriculture_rows = filtered_df[filtered_df['Sector'] == 'Agriculture']
    agriculture_transformed = redistribute_flows_agriculture(agriculture_rows, target_mappings, import_mappings)

    fisheries_rows = filtered_df[filtered_df['Sector'] == 'Fisheries']
    fisheries_transformed = redistribute_flows_fisheries(
        fisheries_rows, fisheries_validity_rules, initial_flexibility, min_flexibility, reduction_factor
    )

    forestry_rows = filtered_df[filtered_df['Sector'] == 'Forestry']
    forestry_transformed = redistribute_roundwood_flows(forestry_rows)
    forestry_transformed = disaggregate_feed_food_flows(forestry_transformed, feed_food_allowed_links)

    unaffected_rows = filtered_df[~filtered_df['Sector'].isin(['Agriculture', 'Fisheries', 'Forestry'])]
    
    final_df = pd.concat([agriculture_transformed, fisheries_transformed, forestry_transformed, unaffected_rows])

    return final_df