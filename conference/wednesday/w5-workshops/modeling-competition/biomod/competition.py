import pandas as pd
import pulp
import logging
import gurobipy as gp

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def _report_and_return(adj, M_csv_path, logger, deficits=None, surpluses=None):
    """
    Helper to report changes and return results.
    M_csv_path can be a file path (str) or a pandas DataFrame.
    """
    if adj is not None:
        print("\n--- Solution Analysis ---")
        try:
            if isinstance(M_csv_path, str):
                original_df = pd.read_csv(
                    M_csv_path,
                    header=0, index_col=0
                ).fillna(0).apply(pd.to_numeric)
            elif isinstance(M_csv_path, pd.DataFrame):
                original_df = M_csv_path.copy()
            else:
                raise TypeError("M_csv_path must be a file path (str) or a pandas DataFrame.")
            original_sums = original_df.sum(axis=1)
            adjusted_sums = adj.sum(axis=1).reindex(original_sums.index, fill_value=0.0)
            
            changes = adjusted_sums - original_sums
            significant_changes = changes[abs(changes) > 0.1]

            print("Row Sum Changes Exceeding 0.1:")
            if not significant_changes.empty:
                for idx, diff in significant_changes.items():
                    orig = original_sums[idx]
                    adj_sum = adjusted_sums[idx]
                    print(f"  Row '{idx}': Δ = {diff:+.2f} (Original: {orig:.2f} → New: {adj_sum:.2f})")
            else:
                print("  No significant row sum changes detected.")

        # Create the detailed DataFrame
            results_df = pd.DataFrame({
                'Row index': original_sums.index.to_series().apply(lambda x: original_df.index.get_loc(x)),
                'Row label': original_sums.index,
                'Original row sum': original_sums,
                'Final row sum': adjusted_sums,
                'Delta': changes
            })

            # Add deficits and surpluses to the results
            results_df['Deficit'] = results_df['Row label'].map(deficits).fillna(0)
            results_df['Surplus'] = results_df['Row label'].map(surpluses).fillna(0)

        except FileNotFoundError:
            logger.error(f"Could not read {M_csv_path} for reporting.")
            results_df = pd.DataFrame()

        except Exception as e:
            logger.error(f"An error occurred during solution analysis: {e}")
            results_df = pd.DataFrame()

    else:
        print("\n--- Solution Analysis ---")
        print("Problem is infeasible or no solution was found.")
        results_df = pd.DataFrame()
    
    return adj, results_df

def solve_adjustable_model(
    M_csv_path, row_class, target_rows, new_demands,
    row_ratios, column_ratios, slack_rows=None, exclude_deficit_rows=None, exclude_surplus_rows=None,
    eps=1e-9,
    deficit_weight_output=0, 
    deficit_weight_primary=1.0,
    deficit_weight_intermediate=1.0,
    surplus_weight_primary=1.0, 
    surplus_weight_intermediate_direct=1.0,
    surplus_weight_intermediate_indirect=1.0,
    surplus_weight_output=1.0,
    slack_weight=1e6,
    tol=1e-8,
    max_deficit_penalty=0,  
    fix_primary_diagonals=True, 
    allow_neg_primary=False,     
    allow_neg_intermediate=False,
    allow_neg_output=False,
    distribution: str = 'row_sum',
    special_rows=None
):
    """
    Solves an adjustable model to find an optimal matrix adjustment.
    M_csv_path can be a file path (str) or a pandas DataFrame.
    """
    if isinstance(M_csv_path, str):
        try:
            M_df = pd.read_csv(
                M_csv_path,
                header=0, index_col=0
            ).fillna(0).apply(pd.to_numeric)
        except Exception as e:
            raise IOError(f"Could not read matrix CSV: {e}")
    elif isinstance(M_csv_path, pd.DataFrame):
        M_df = M_csv_path.copy()
    else:
        raise TypeError("M_csv_path must be a file path (str) or a pandas DataFrame.")

    n = len(M_df)
    slack_rows = slack_rows or []

    if len(row_class) != n:
        raise ValueError(f"row_class length {len(row_class)} != matrix size {n}")

    for tr in target_rows:
        if tr < 0 or tr >= n:
            raise IndexError(f"target row {tr} out of range [0,{n})")

    for i, cls in row_class.items():
        if cls not in ('primary', 'intermediate', 'output'):
            raise ValueError(f"Invalid class '{cls}' for row {i}")

    adj, deficits, surpluses = try_solve_adjustable_model(
        M_df, row_class, target_rows, new_demands, row_ratios,
        column_ratios, slack_rows, exclude_deficit_rows, exclude_surplus_rows, eps,
        deficit_weight_output, 
        deficit_weight_primary,
        deficit_weight_intermediate,
        surplus_weight_primary, 
        surplus_weight_intermediate_direct,
        surplus_weight_intermediate_indirect,
        surplus_weight_output,
        slack_weight, max_deficit_penalty, tol,
        allow_neg_primary,
        allow_neg_intermediate,
        allow_neg_output,
        fix_primary_diagonals,
        distribution,
        special_rows
    )
    return _report_and_return(adj, M_csv_path, logger, deficits=deficits, surpluses=surpluses)

def try_solve_adjustable_model(
    M_df, row_class, target_rows, new_demands,
    row_ratios, column_ratios, slack_rows, exclude_deficit_rows, exclude_surplus_rows,
    eps,
    deficit_weight_output, 
    deficit_weight_primary,
    deficit_weight_intermediate,
    surplus_weight_primary, 
    surplus_weight_intermediate_direct,
    surplus_weight_intermediate_indirect, 
    surplus_weight_output,
    slack_weight,
    max_deficit_penalty, tol,
    allow_neg_primary,
    allow_neg_intermediate,
    allow_neg_output,
    fix_primary_diagonals,
    distribution,
    special_rows=None
):
    n = len(M_df)
    M = M_df.values.tolist()
    orig_row_sum = [sum(row) for row in M]
    orig_col_sum = [sum(M[i][j] for i in range(n)) for j in range(n)]
    
    special_rows = special_rows or []

    primary_rows_indices = {i for i, cls in row_class.items() if cls == 'primary'}
    intermediate_rows_indices = {i for i, cls in row_class.items() if cls == 'intermediate'}
    output_rows_indices = {i for i, cls in row_class.items() if cls == 'output'}

    # Step 1: Find all rows reachable from target_rows via graph traversal
    logger.info("--- Identifying All Linked Rows via Graph Traversal from Target ---")
    adj_list = {i: [] for i in range(n)}
    rev_adj_list = {i: [] for i in range(n)}
    for r_parent in range(n):
        for r_child in range(n):
            if r_parent != r_child and abs(M[r_parent][r_child]) > 1e-9:
                adj_list[r_parent].append(r_child)
                rev_adj_list[r_child].append(r_parent)

    queue = list(target_rows)
    visited = set(target_rows)
    head = 0
    while head < len(queue):
        current_node = queue[head]
        head += 1
        all_neighbors = adj_list.get(current_node, []) + rev_adj_list.get(current_node, [])
        for neighbor in all_neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    logger.info(f"Traversal identified {len(visited)} linked rows/columns: {sorted(list(visited))}")

    # Step 2: Define variables ONLY for the linked portion of the matrix
    prob = pulp.LpProblem("AdjustableModel", pulp.LpMinimize)
    x_vars = {}
    logger.info("Defining variables for linked cells...")
    for i in range(n):
        for j in range(n):
            if (i in visited or j in visited) and M[i][j] != 0:
                if fix_primary_diagonals and i in primary_rows_indices and i == j:
                    x_vars[(i,j)] = pulp.LpVariable(f"x_{i}_{j}", lowBound=M[i][j], upBound=M[i][j])
                else:
                    allow_neg = (row_class[i] == 'primary' and allow_neg_primary) or \
                                (row_class[i] == 'intermediate' and allow_neg_intermediate) or \
                                (row_class[i] == 'output' and allow_neg_output)
                    if allow_neg:
                        x_vars[(i,j)] = pulp.LpVariable(f"x_{i}_{j}")
                    else:
                        x_vars[(i,j)] = pulp.LpVariable(f"x_{i}_{j}", lowBound=0 if M[i][j] > 0 else None, upBound=None if M[i][j] > 0 else -eps)

    # Step 3: Define deficit/surplus variables
    final_eligible_rows = {i for i in visited if i in output_rows_indices and i not in target_rows and (exclude_deficit_rows is None or i not in exclude_deficit_rows)}
    logger.info(f"Final set of eligible rows for deficit: {sorted(list(final_eligible_rows))}")

    deficit_output_vars = {i: pulp.LpVariable(f"deficit_out_{i}", lowBound=0) for i in final_eligible_rows}
    deficit_primary_vars = {i: pulp.LpVariable(f"deficit_prim_{i}", lowBound=0) for i in primary_rows_indices if i in visited}
    deficit_intermediate_vars = {i: pulp.LpVariable(f"deficit_int_{i}", lowBound=0) for i in intermediate_rows_indices if i in visited}
    surplus_vars = {i: pulp.LpVariable(f"surplus_{i}", lowBound=0) for i in range(n) if i in visited and row_class[i] in ('primary', 'intermediate', 'output') and i not in target_rows and (exclude_surplus_rows is None or i not in exclude_surplus_rows)}
    s_vars = {i: pulp.LpVariable(f"s_{i}", lowBound=0) for i in target_rows}
    max_deficit = pulp.LpVariable("max_deficit", lowBound=0)

    # Step 4: Build model
    prob += (
        deficit_weight_output * pulp.lpSum(deficit_output_vars.values()) +
        deficit_weight_intermediate * pulp.lpSum(deficit_intermediate_vars.values()) +
        deficit_weight_primary * pulp.lpSum(deficit_primary_vars.values()) +
        max_deficit_penalty * max_deficit +
        slack_weight * pulp.lpSum(s_vars.values()) +
        surplus_weight_primary * pulp.lpSum(surplus_vars[i] for i in primary_rows_indices if i in surplus_vars) +
        surplus_weight_intermediate_direct * pulp.lpSum(surplus_vars[i] for i in intermediate_rows_indices if any(M[i][j] != 0 for j in primary_rows_indices) and i in surplus_vars) +
        surplus_weight_intermediate_indirect * pulp.lpSum(surplus_vars[i] for i in intermediate_rows_indices if not any(M[i][j] != 0 for j in primary_rows_indices) and i in surplus_vars) +
        surplus_weight_output * pulp.lpSum(surplus_vars[i] for i in output_rows_indices if i in surplus_vars)
    )

    all_deficit_vars = {**deficit_output_vars, **deficit_intermediate_vars, **deficit_primary_vars}
    for var in all_deficit_vars.values():
        prob += max_deficit >= var

    for i in range(n):
        row_expr = pulp.lpSum(x_vars.get((i, j), M[i][j]) for j in range(n))
        if i in target_rows:
            prob += row_expr == new_demands[target_rows.index(i)] + s_vars.get(i, 0)
        elif i not in visited:
            prob += row_expr == orig_row_sum[i]
        elif row_class[i] in ('primary', 'intermediate', 'output'):
            prob += row_expr == orig_row_sum[i] + surplus_vars.get(i, 0) - all_deficit_vars.get(i, 0)

        if i in visited and not ((row_class[i] == 'primary' and allow_neg_primary) or \
                (row_class[i] == 'intermediate' and allow_neg_intermediate) or \
                (row_class[i] == 'output' and allow_neg_output)):
            prob += row_expr >= 0
    
    for j in range(n):
        col_expr = pulp.lpSum(x_vars.get((i, j), M[i][j]) for i in range(n))
        if j not in visited:
            prob += col_expr == orig_col_sum[j]
        elif row_class[j] == 'primary':
            prob += col_expr == orig_col_sum[j]
        else:
            prob += col_expr == 0

    for i, cols in row_ratios.items():
        if len(cols) < 2 or M[i][cols[0]] == 0: continue
        for j in cols[1:]:
            if M[i][j] != 0:
                prob += x_vars.get((i,j), M[i][j]) * M[i][cols[0]] == x_vars.get((i,cols[0]), M[i][cols[0]]) * M[i][j]

    for j, rows in column_ratios.items():
        if len(rows) < 2 or M[rows[0]][j] == 0: continue
        for k in rows[1:]:
            if M[k][j] != 0:
                prob += x_vars.get((k,j), M[k][j]) == (M[k][j] / M[rows[0]][j]) * x_vars.get((rows[0],j), M[rows[0]][j])

    if distribution == 'row_sum':
        logger.info("Enforcing row_sum distribution (proportional deficits) for eligible output rows...")
        sorted_eligible = sorted(list(final_eligible_rows))
        if len(sorted_eligible) > 1:
            ref_i = sorted_eligible[0]
            ref_sum = orig_row_sum[ref_i]
            # Ensure we don't divide by zero or rely on zero-sum rows
            if abs(ref_sum) > eps:
                for i in sorted_eligible[1:]:
                    if i in special_rows: continue
                    
                    row_sum_i = orig_row_sum[i]
                    if abs(row_sum_i) > eps:
                        # deficit_i / row_sum_i = deficit_ref / ref_sum
                        # => deficit_i * ref_sum = deficit_ref * row_sum_i
                        prob += deficit_output_vars[i] * ref_sum == deficit_output_vars[ref_i] * row_sum_i
    
    for i in range(n):
        if M[i][i] != 0:
            if (i, i) in x_vars:
                # Only force positivity if the original diagonal was positive
                if M[i][i] > 0:
                                prob += x_vars[(i, i)] >= eps
                # If original was negative, force it to be negative (away from zero)
                elif M[i][i] < 0:
                                prob += x_vars[(i, i)] <= -eps

    prob.solve(pulp.PULP_CBC_CMD(msg=False, options=[f'primalTolerance {tol}']))
    prob.writeLP("problem.lp")
    
    if prob.status == pulp.LpStatusOptimal:
        logger.info("--- Solution found. ---")
        adj = M_df.copy()
        for i in range(n):
            for j in range(n):
                adj.iat[i,j] = x_vars[(i,j)].varValue if (i,j) in x_vars else M[i][j]
        
        deficits = {M_df.index[i]: var.varValue for i, var in all_deficit_vars.items() if var.varValue > eps}
        surpluses = {M_df.index[i]: var.varValue for i, var in surplus_vars.items() if var.varValue > eps}
        return adj, deficits, surpluses
    
    logger.error("Model is likely infeasible.")
    try:
        prob.writeLP("infeasible_problem.lp")
        model = gp.read("infeasible_problem.lp")
        model.computeIIS()
        model.write("infeasibility.ilp")
        logger.info("Infeasibility report written to infeasibility.ilp")
    except Exception as e:
        logger.error(f"Could not run Gurobi for IIS analysis: {e}")
    return None, {}, {}


def _perform_binary_search_for_target(target_index_to_search, solver_params, search_precision, max_iterations):
    """
    Private helper to run a binary search for a single target within a set of targets.
    """
    initial_demand = solver_params['new_demands'][target_index_to_search]
    target_row = solver_params['target_rows'][target_index_to_search]

    # Create a dictionary of other targets to display in the log
    other_demands = {
        tr: dm for tr, dm in zip(solver_params['target_rows'], solver_params['new_demands']) 
        if tr != target_row
    }
    if other_demands:
        print(f"  Holding other demands constant: {other_demands}")

    print(f"  Checking feasibility of initial demand {initial_demand} for target {target_row}...")
    
    adj, _ = solve_adjustable_model(**solver_params)
    if adj is None:
        print(f"  Initial state with demand {initial_demand} is infeasible. Cannot start search for this target.")
        return None

    low_bound = initial_demand
    high_bound = initial_demand

    # Find an infeasible upper bound
    print(f"  Finding an infeasible upper bound for target {target_row}...")
    temp_params = solver_params.copy()
    temp_params['new_demands'] = solver_params['new_demands'][:]

    while adj is not None:
        low_bound = high_bound
        if high_bound == 0: # Handle case where initial demand is 0
            high_bound = 1000 
        else:
            high_bound *= 2
        
        temp_params['new_demands'][target_index_to_search] = high_bound
        print(f"    ...testing upper bound: {high_bound:.2f}")
        adj, _ = solve_adjustable_model(**temp_params)
    
    print(f"  Established search range for target {target_row}: [{low_bound:.2f}, {high_bound:.2f}]")

    # Perform binary search
    for i in range(max_iterations):
        mid_demand = low_bound + (high_bound - low_bound) / 2
        if (high_bound - low_bound) < search_precision:
            break
        
        temp_params['new_demands'][target_index_to_search] = mid_demand
        adj, _ = solve_adjustable_model(**temp_params)

        if adj is not None:
            low_bound = mid_demand
        else:
            high_bound = mid_demand
            
    return low_bound


def find_max_demands_for_targets(
    M_csv_path, row_class, target_rows, new_demands,
    row_ratios, column_ratios, slack_rows=None, exclude_deficit_rows=None, exclude_surplus_rows=None, eps=1e-9,
    deficit_weight_output=0, 
    deficit_weight_primary=1.0,
    deficit_weight_intermediate=1.0,
    surplus_weight_primary=1.0, 
    surplus_weight_intermediate_direct=1.0,
    surplus_weight_intermediate_indirect=1.0,
    surplus_weight_output=1.0,
    slack_weight=1e6, tol=1e-3,
    max_deficit_penalty=0,
    allow_neg_primary: bool = False,
    allow_neg_intermediate: bool = False,
    allow_neg_output: bool = False,
    fix_primary_diagonals: bool = False,
    search_precision=1000,
    max_iterations=50,
    distribution: str = 'default',
    special_rows=None
):
    """
    Performs an independent binary search for each target row to find its maximum feasible demand.
    """
    if len(target_rows) != len(new_demands):
        raise ValueError("The number of target_rows must equal the number of new_demands.")

    # Store all parameters in a dictionary for easier handling
    all_params = locals().copy()
    search_precision = all_params.pop('search_precision')
    max_iterations = all_params.pop('max_iterations')
    
    original_targets = all_params.pop('target_rows')
    original_demands = all_params.pop('new_demands')

    results = {}
    print(f"--- Starting Maximum Feasible Demand Search for {len(original_targets)} Targets ---")

    for i, current_target_row in enumerate(original_targets):
        print(f"\n>>> Searching for Target Row: {current_target_row} <<<")
        
        # Set up the parameters for this specific search.
        # The demands for all other targets are held constant.
        search_params = all_params.copy()
        search_params['target_rows'] = original_targets[:]
        search_params['new_demands'] = original_demands[:]

        # The helper function will modify the demand for the single row being searched
        max_demand = _perform_binary_search_for_target(
            target_index_to_search=i,
            solver_params=search_params,
            search_precision=search_precision,
            max_iterations=max_iterations
        )

        if max_demand is not None:
            print(f"  >>> Max feasible demand for target {current_target_row}: {max_demand:.2f}")
            results[current_target_row] = max_demand
        else:
            results[current_target_row] = None

    print("\n--- Search Complete ---")
    return results
