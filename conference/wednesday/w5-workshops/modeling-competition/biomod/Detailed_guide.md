## Investigating the effects of competition among biobased products within the bioeconomy matrix - `solve_adjustable_model` function documentation

The `solve_adjustable_model` function is a designed to analyze how the bioeconomy's interconnected production system adjusts to changing demand.

### Core concept

The function takes an LCI-like matrix representing the bioeconomy, a set of new demand targets for specific biobased products, and a collection of physical rules and modeling penalties. It then calculates a new, adjusted matrix that meets these demands while maintaining the structural integrity of the bioeconomy.

This is particularly useful for answering "What if?" scenarios:
> *"If the demand for bioenergy increases by 20%, which products competing for the same biomass as feedstock will be unable to meet their current demand, and how much demand will not be met?"*

The model works by defining a complex optimization problem. It tries to satisfy the requested new demand values for the targeted biobased product while penalizing different types of changes (e.g., creating a deficit of another product). The final result is the lowest-penalty solution. Surpluses may also be generated when the demand results in excess output in other activities.

The optimized matrix allows to identify and quantify the deficit linked with the requested new demand. This is the main output of the model.

#### How it works
1.  **Network mapping:** the model starts from the `target_rows` (the products whose demand is changing) and performs a graph traversal to identify all upstream and downstream sectors that are physically linked to these products.
2.  **Optimization:** it defines a linear programming problem over this identified sub-network.
3.  **Resolution:** it calculates the optimal adjustment that satisfies the `new_demands` while minimizing "penalties" for undesirable changes, such as creating a supply **deficit** or generating an unmanageable **surplus**.

---

## 1. Environment setup
Ensure your Jupyter environment has access to `competition.py` and the required solver libraries.

```python
import pandas as pd
from competition import solve_adjustable_model

# Input can be a file path or a pandas DataFrame
matrix_input = "data/matrix.csv" 
```

---

## 2. Parameter reference & default values

The function signature contains several parameters that control the optimization behavior.

### Core required parameters
| Parameter | Description |
| :--- | :--- |
| `M_csv_path` | Path to CSV or a `pd.DataFrame`. Must have headers and index labels. |
| `row_class` | Dictionary `{index: 'type'}`. Types: `'primary'`, `'intermediate'`, or `'output'`. |
| `target_rows` | List of row indices where you want to impose `new_demands`. |
| `new_demands` | List of target row-sum values corresponding to `target_rows`. |
| `row_ratios` | Dictionary `{row_idx: [col_indices]}` to keep elements proportional in a row. |
| `column_ratios` | Dictionary `{col_idx: [row_indices]}` to keep elements proportional in a column. |

### Optional weights & penalties
| Parameter | Default | Description |
| :--- | :--- | :--- |
| `deficit_weight_output` | `0` | Penalty for row-sum falling below original for 'output' rows. |
| `deficit_weight_primary` | `1.0` | Penalty for row-sum falling below original for 'primary' rows. |
| `deficit_weight_intermediate` | `1.0` | Penalty for row-sum falling below original for 'intermediate' rows. |
| `surplus_weight_output` | `1.0` | Penalty for row-sum exceeding original for 'output' rows. |
| `surplus_weight_primary` | `1.0` | Penalty for row-sum exceeding original for 'primary' rows. |
| `surplus_weight_intermediate_direct` | `1.0` | Penalty for surplus in intermediate rows linked to primary inputs. |
| `surplus_weight_intermediate_indirect`| `1.0` | Penalty for surplus in other intermediate rows. |
| `slack_weight` | `1e6` | Penalty for failing to meet the exact `new_demands`. |
| `max_deficit_penalty` | `0` | Penalty applied to the *maximum* single deficit across all rows (minimax). |

### Flags and optimization logic
| Parameter | Default | Description |
| :--- | :--- | :--- |
| `fix_primary_diagonals` | `True` | If True, diagonal elements `(i,i)` for primary rows are locked to original values. |
| `allow_neg_primary` | `False` | Allows primary row elements to become negative. |
| `allow_neg_intermediate` | `False` | Allows intermediate row elements to become negative. |
| `allow_neg_output` | `False` | Allows output row elements to become negative. |
| `distribution` | `'row_sum'` | Options: `'row_sum'` (proportional deficits) or `'default'`. |
| `eps` | `1e-9` | Small constant to handle zero-thresholds and strict positivity. |
| `tol` | `1e-8` | Primal tolerance for the underlying CBC solver. |

### Exclusions and special handling
| Parameter | Default | Description |
| :--- | :--- | :--- |
| `slack_rows` | `None` | List of indices that can act as "slack" (flexible row sums). |
| `exclude_deficit_rows` | `None` | List of indices that are exempt from deficit penalties. |
| `exclude_surplus_rows` | `None` | List of indices that are exempt from surplus penalties. |
| `special_rows` | `None` | List of indices excluded from the proportional `row_sum` distribution logic. |

---

## 3. Step-by-step implementation

### Step 3.1: Define classification
Categorize every row in your matrix.
```python
# Assuming a 4x4 matrix
row_class = {0: 'primary', 1: 'intermediate', 2: 'output', 3: 'output'}
```

### Step 3.2: Set targets and ratios
```python
# Goal: Increase demand of row 2 to 5000 units
target_rows = [2]
new_demands = [5000.0]

# Logic: Ensure columns 1 and 2 in row 0 always scale together
row_ratios = {0: [1, 2]}
```

### Step 3.3: Execution
```python
adjusted_df, summary_results = solve_adjustable_model(
    M_csv_path="my_matrix.csv",
    row_class=row_class,
    target_rows=target_rows,
    new_demands=new_demands,
    row_ratios=row_ratios,
    column_ratios={},
    slack_weight=1e7,           # High priority on meeting targets
    allow_neg_output=False,     # Physical constraint: no negative outputs
)
```

---

## 4. Understanding outputs

The function returns a tuple: `(adjusted_matrix, results_dataframe)`.

1.  **`adjusted_matrix`**: A pandas DataFrame of the same shape as the input, containing the optimized values.
2.  **`results_dataframe`**: A diagnostic table containing:
    *   `Original row sum`: Sums before adjustment.
    *   `Final row sum`: Sums after adjustment.
    *   `Delta`: The net change.
    *   `Deficit / Surplus`: Specific slack values identified by the solver.

---

## 5. Troubleshooting infeasibility

If the solver logs `Model is likely infeasible`:
1.  **Check ratios**: High-constraint ratios (e.g., forcing a row to be 0 while a linked column must be >0) often cause failures.
2.  **Gurobi analysis**: If Gurobi is available, the script generates `infeasibility.ilp`. Open this file in a text editor to see the "Irreducible Inconsistent Subsystem" (IIS)—it will explicitly list which constraints conflict.
3.  **Relax flags**: Try setting `fix_primary_diagonals=False` or `allow_neg_intermediate=True` to see if the model becomes feasible.
