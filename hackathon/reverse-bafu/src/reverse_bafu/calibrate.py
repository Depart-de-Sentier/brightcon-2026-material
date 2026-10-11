"""Step 2 - amounts for the inputs marked ``free``, by bounded least squares against the target's
cumulative inventory, flow by flow, with every other input held at its spec amount. The input
*list* is never changed here: with a free structure the fit reproduces the inventory and invents
the process (see the method explainer in artifacts/, §2 and §7); with the right list it recovers
the input amounts (benchmark: 772 of 786 within ±20 %).

No impact assessment: every flow present in the target or the model is one equation, weighted by
its relative error, with each (unit, compartment) group of flows counting equally and round-off
flows left out (``lci.System.fit_weights``). There is no per-category emphasis to choose."""

from __future__ import annotations

import numpy as np
import bw2data as bd

from . import db
from .lci import System, determined_flows, solve_weighted
from .spec import Spec


def run(spec: Spec, apply: bool = False) -> None:
    target = bd.get_node(database=db.INVENTORY_DB, code=spec.target_code)
    node = spec.node
    inputs = [i for i in node.inputs if i.code]
    if any(i.node for i in node.inputs):
        print("note: nested nodes are not calibrated; only the top node's free inputs are")
    free = [i for i in inputs if i.free]
    fixed = [i for i in inputs if not i.free]
    if not free:
        print("no inputs marked \"free\": nothing to calibrate")
        return
    # the matrices must contain the sandbox when inputs link to rebuilt nodes
    demand = target
    if any(i.sandbox for i in inputs):
        demand = bd.get_node(database=db.SANDBOX_DB, code=next(i.sandbox for i in inputs if i.sandbox))
    sys_ = System(demand)
    ids = {i.code: bd.get_node(database=db.SANDBOX_DB if i.sandbox else db.INVENTORY_DB, code=i.code).id for i in inputs}
    b = sys_.cumulative([target.id])[:, 0]
    det = determined_flows(sys_, target.id)
    M_fixed = sys_.cumulative([ids[i.code] for i in fixed]) if fixed else np.zeros((sys_.n_flows, 0))
    M_free = sys_.cumulative([ids[i.code] for i in free])
    # direct flows of the node itself are part of the fixed contribution too
    direct = np.zeros(sys_.n_flows)
    for f in node.emissions + node.resources:
        if f.code:
            row = sys_.flow_row(f.database, f.code)
            if row is not None:
                direct[row] += f.amount
    fixed_part = M_fixed @ np.array([i.amount for i in fixed]) + direct
    residual_target = b - fixed_part
    lo = np.array([i.bounds[0] if i.bounds else 0.0 for i in free])
    hi = np.array([i.bounds[1] if i.bounds else np.inf for i in free])
    kg = np.array([1.0 if i.unit.startswith("kilo") else 0.0 for i in free])

    def fit(model: np.ndarray) -> tuple[np.ndarray, float, int]:
        """One weighted solve. The weights are relative to ``model``, so a flow the model brings in
        that the target does not have counts by its own size rather than being divided by zero."""
        w = sys_.fit_weights(b, model, det)
        rows = np.where(w > 0)[0]
        A = w[rows, None] * M_free[rows]
        y = w[rows] * residual_target[rows]
        if node.mass_sum is not None:
            # one heavily weighted row: the free kilogram inputs add up to mass_sum
            wt = 1e3 * np.linalg.norm(y)
            A = np.vstack([A, wt * kg])
            y = np.append(y, wt * node.mass_sum)
        x = solve_weighted(A, y, lo, hi)
        return x, float(np.linalg.norm(A @ x - y)), len(rows)

    # two passes: the first weights against the spec's own amounts, the second against the fit, so
    # the result does not depend on the amounts a draft happened to start from
    x, rnorm, n_rows = fit(fixed_part + M_free @ np.array([i.amount for i in free]))
    x, rnorm, n_rows = fit(fixed_part + M_free @ x)
    print(f"fit over {n_rows} flows; {len(free)} free input(s)"
          f"{'; bounds from the report' if any(i.bounds for i in free) else ''}"
          f"{f'; mass sum = {node.mass_sum}' if node.mass_sum is not None else ''}; residual norm {rnorm:.3g}; two passes\n")
    print(f"{'spec amount':>12s} {'fitted':>12s} {'ratio':>7s}  input")
    for i, v in zip(free, x):
        ratio = v / i.amount if i.amount else float("inf")
        print(f"{i.amount:12.4g} {v:12.4g} {ratio:7.2f}  {i.name} [{i.location}]")
        if apply:
            i.amount = float(v)
    if apply:
        from .spec import save
        save(spec)
        print("\namounts written back to", spec.path)
