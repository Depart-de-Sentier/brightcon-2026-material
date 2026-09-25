# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:50:29 2026

"""


"""

Can be executed within the brightcon2026 conda environment (yml file in the folder)

If as a community we want to move towards better metadata lineage, we can prioritize our sourcing efforts to where it matters. 
The code below allows performing a two-step Global Sensitivity Analysis on all coefficients (exchange amounts) in the technosphere and biosphere matrices, foreground and background included, 
and flag the most sensitive parameters which are poorly documented. 
Thus, one can know if their LCA results heavily depend on data that is not linked to any reference, report etc.

The script needs to be adapted to whatever database is used, and its associated metadata structure.


Two complementary options are proposed.
1) a two-step GSA, starting with a correlation screening so that only the dimensionality of the GSA is reduced. 
Delta (moment-independent) GSA is then performed, and the undocumented sensitive exchanges are flagged out.
This option tells you how the uncertainty in your results depends on poorly documented values.

2) Recursive contribution analysis + metadata/documentation audit
In the deterministic impact value for your FU, which exchange amounts belong to the product system branch which carries most of the impact ?
The algorithm goes deeper in the branch until a cut-off threshold, and returns all exchanges on the way, together with whether they are poorly documented or not.
"""
from datetime import datetime

import numpy as np
import bw2data as bd





list(bd.projects)


# SET UP YOUR PROJECT WITH YOUR DATABASES
bd.projects.set_current("310_feedback_CC_copy")

list(bd.databases)


ecoinvent = bd.Database("ecoinvent-3.10-consequential")
biosphere = bd.Database("ecoinvent-3.10-biosphere")


def collect_activity_metadata(activity):
    """Return every available metadata field for `activity` itself, plus for
    each of its individual exchanges, as plain dicts."""
    activity_metadata = dict(activity)
    exchanges_metadata = [dict(exc) for exc in activity.exchanges()]
    return {"activity": activity_metadata, "exchanges": exchanges_metadata}


example_activity = next(iter(ecoinvent))
metadata_example_activity = collect_activity_metadata(example_activity)
metadata_example_activity


# =====================================================================
# 1) Global sensitivity analysis (moment-independent / Delta) on every
# uncertain exchange amount in the technosphere and biosphere matrices
# =====================================================================
#
# Uses the per-exchange uncertainty distributions already embedded in the
# bw2.5 (bw_processing / matrix_utils) matrices -- nothing needs to be
# redefined by hand. For a given functional unit + LCIA method:
#
#   1. `collect_uncertain_matrix_parameters` enumerates every technosphere
#      and biosphere matrix cell that carries a real, sampleable
#      `stats_arrays` uncertainty distribution.
#   2. `sample_uncertain_parameters` draws Monte Carlo samples for each of
#      them, using the exact same `stats_arrays.MCRandomNumberGenerator`
#      brightway's own `use_distributions=True` Monte Carlo relies on.
#   3. `evaluate_lca_for_samples` writes each sample directly into the LCA
#      object's matrices and re-solves, collecting one LCIA score per
#      sample.
#   4. `global_sensitivity_analysis_matrix_exchanges` feeds the resulting
#      (X, Y) into `SALib.analyze.delta` (Borgonovo's moment-independent
#      "delta" measure) and returns the `top_n` most sensitive exchanges.
#
# Requires SALib (`pip install SALib`), in addition to bw2calc/stats_arrays
# (already part of a bw2.5 environment).

import time

import bw2calc as bc
import matplotlib.pyplot as plt
from scipy.stats import rankdata
from stats_arrays import MCRandomNumberGenerator

try:
    from SALib.analyze import delta as salib_delta
    _salib_import_error = None
except ImportError as exc:  # pragma: no cover - depends on environment
    salib_delta = None
    _salib_import_error = exc


# stats_arrays uncertainty_type codes that correspond to an actual,
# sampleable probability distribution -- excludes 0 (undefined) and 1 (no
# uncertainty), which are both effectively constants, and matrix_utils' own
# synthetic 98/99 codes (estimated-from-array / interface data, not real
# stats_arrays distributions). See stats_arrays.uncertainty_choices and
# matrix_utils.MappedMatrix.input_uncertainties.
_SAMPLEABLE_UNCERTAINTY_TYPES = frozenset({2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13})


def _biosphere_flow_weights(lca):
    """Per-biosphere-row total characterization weight for `lca`'s
    already-built `characterization_matrix`: how much one unit of
    inventory at that row contributes to the total score under the
    chosen method, entirely independent of any Monte Carlo sampling.

    Column-sums, not row-sums: correct even when `characterization_matrix`
    isn't purely diagonal (e.g. regionalized/matrix-based methods), since
    score = sum_r (C @ e_r).sum() * inventory[r] for any C, and
    (C @ e_r).sum() is exactly C's r-th column summed. Requires
    `lca.lcia()` to already have been called. Shared by
    `collect_uncertain_matrix_parameters` (to exclude biosphere exchanges
    the chosen method can't see at all) and `_UnitScoreSolver` further
    down.
    """
    return np.asarray(lca.characterization_matrix.sum(axis=0)).ravel()


def build_lca_for_gsa(activity, method, amount=1, verbose=False):
    """Build and solve a `bw2calc.LCA` for `activity`, with per-exchange
    uncertainty distributions loaded (`use_distributions=True`) so its
    `technosphere_mm` / `biosphere_mm` expose every exchange's stats_arrays
    uncertainty parameters.

    This is the one-time cost of constructing the matrices and running the
    baseline `lci()`/`lcia()` solve -- separate from, and not included in,
    the per-sample re-solve cost the GSA loop prints later. `verbose=True`
    prints how long it took.
    """
    t0 = time.perf_counter()
    lca = bc.LCA({activity: amount}, method, use_distributions=True)
    lca.lci()
    lca.lcia()
    if verbose:
        print(f"[GSA] build + solve baseline LCA: {time.perf_counter() - t0:.1f}s")
    return lca


def collect_uncertain_matrix_parameters(
    lca, restrict_to_active_supply_chain=True, supply_tolerance=1e-13,
    exclude_biosphere_without_characterization=False, characterization_tolerance=0.0,
):
    """Enumerate every technosphere and biosphere matrix entry that carries a
    real (sampleable) uncertainty distribution.

    Pulls three arrays out of each of `lca.technosphere_mm` and
    `lca.biosphere_mm` (`matrix_utils.MappedMatrix`), aligned element-wise:
    `input_uncertainties()` (the stats_arrays distribution parameters),
    `input_row_col_indices()` (the matrix row/col each entry is written to),
    and `input_flip_vector()` / `input_rescale_vector()` (the sign flip and
    rescale applied on top of a raw sampled value to get the actual matrix
    entry -- see `matrix_utils.ResourceGroup.calculate`).

    If `restrict_to_active_supply_chain` (default), only exchanges whose
    technosphere/biosphere *column* (the activity producing or consuming the
    flow) has a nonzero entry in `lca.supply_array` are kept: an exchange
    belonging to an activity that this functional unit never actually calls
    upon cannot affect the score no matter how it varies, so keeping it would
    only add noise and (on a full ecoinvent-scale database, with millions of
    uncertain exchanges) make the analysis intractable. Pass
    `restrict_to_active_supply_chain=False` to sweep every uncertain cell in
    both matrices instead.

    If `exclude_biosphere_without_characterization` (default), a biosphere
    exchange whose flow has zero total weight (`abs(...) <=
    characterization_tolerance`, see `_biosphere_flow_weights`) under the
    chosen LCIA method is dropped too: such a flow's amount provably cannot
    move the score, by the same "no unit conversion, ever, moves a
    zero-weighted term" logic as the supply-chain filter above, just
    checked directly against the characterization matrix instead of
    inferred from a Monte Carlo run. This is what keeps an
    uncharacterized flow from ever showing up as "sensitive" in the first
    place, rather than relying on enough samples to statistically wash out
    its (necessarily spurious) apparent delta index.

    Returns a dict of parallel arrays/lists (one entry per uncertain
    exchange): "matrix" ("technosphere"/"biosphere"), "row", "col",
    "uncertainty" (the stacked stats_arrays UNCERTAINTY_DTYPE array),
    "flip", "rescale", "current_amount", "input_key", "output_key" (the
    (database, code) keys on either side of the exchange, or None where not
    resolvable).
    """
    supply = getattr(lca, "supply_array", None)
    if restrict_to_active_supply_chain and supply is None:
        raise ValueError("lca.supply_array not found -- run lca.lci() first.")
    if exclude_biosphere_without_characterization and not hasattr(lca, "characterization_matrix"):
        raise ValueError("lca.characterization_matrix not found -- run lca.lcia() first.")

    activity_reversed = lca.dicts.activity.reversed
    product_reversed = lca.dicts.product.reversed
    biosphere_reversed = lca.dicts.biosphere.reversed
    flow_weights = (
        _biosphere_flow_weights(lca) if exclude_biosphere_without_characterization else None
    )

    matrix_chunks, row_chunks, col_chunks = [], [], []
    uncertainty_chunks, flip_chunks, rescale_chunks, amount_chunks = [], [], [], []
    input_keys, output_keys = [], []

    for matrix_name, mm in (
        ("technosphere", lca.technosphere_mm),
        ("biosphere", lca.biosphere_mm),
    ):
        uncertainties = mm.input_uncertainties()
        indices = mm.input_row_col_indices()
        flips = mm.input_flip_vector()
        rescales = mm.input_rescale_vector()
        values = mm.input_data_vector()

        keep = np.isin(uncertainties["uncertainty_type"], list(_SAMPLEABLE_UNCERTAINTY_TYPES))
        if restrict_to_active_supply_chain:
            keep &= np.abs(supply[indices["col"]]) > supply_tolerance
        if matrix_name == "biosphere" and exclude_biosphere_without_characterization:
            keep &= np.abs(flow_weights[indices["row"]]) > characterization_tolerance

        rows = indices["row"][keep]
        cols = indices["col"][keep]

        matrix_chunks.append(np.full(rows.shape, matrix_name, dtype=object))
        row_chunks.append(rows)
        col_chunks.append(cols)
        uncertainty_chunks.append(uncertainties[keep])
        flip_chunks.append(flips[keep])
        rescale_chunks.append(rescales[keep])
        amount_chunks.append(values[keep])

        for row, col in zip(rows, cols):
            output_keys.append(activity_reversed.get(int(col)))
            if matrix_name == "technosphere":
                input_keys.append(product_reversed.get(int(row)))
            else:
                input_keys.append(biosphere_reversed.get(int(row)))

    if not row_chunks:
        row_chunks = [np.array([], dtype=np.int64)]

    return {
        "matrix": np.concatenate(matrix_chunks),
        "row": np.concatenate(row_chunks),
        "col": np.concatenate(col_chunks),
        "uncertainty": np.concatenate(uncertainty_chunks),
        "flip": np.concatenate(flip_chunks),
        "rescale": np.concatenate(rescale_chunks),
        "current_amount": np.concatenate(amount_chunks),
        "input_key": input_keys,
        "output_key": output_keys,
    }


def sample_uncertain_parameters(parameters, n_samples, seed=None):
    """Draw `n_samples` independent Monte Carlo samples for each entry of
    `parameters` (as built by `collect_uncertain_matrix_parameters`), using
    the same `stats_arrays.MCRandomNumberGenerator` brightway itself uses
    for `use_distributions=True` Monte Carlo.

    Returns an `(n_samples, len(parameters["row"]))` array of values, ready
    to be written directly into the technosphere/biosphere matrices (sign
    flip and rescale already applied, matching
    `matrix_utils.ResourceGroup.calculate`).
    """
    n_params = len(parameters["row"])
    if n_params == 0:
        raise ValueError("No uncertain parameters to sample -- nothing to analyze.")

    rng = MCRandomNumberGenerator(parameters["uncertainty"], seed=seed)
    raw = np.array([next(rng) for _ in range(n_samples)])  # (n_samples, D), pre flip/rescale

    X = raw
    X[:, parameters["flip"]] *= -1
    X *= parameters["rescale"][np.newaxis, :]
    return X


def _csr_data_positions(matrix, rows, cols):
    """Return, for each (row, col) pair, the index into `matrix.data`
    holding that cell's current value. Assumes every (row, col) pair is
    already an explicit stored entry in `matrix` (true here, since these
    come from exchanges that were used to build the matrix in the first
    place)."""
    matrix.sort_indices()
    positions = np.empty(len(rows), dtype=np.int64)
    for k in range(len(rows)):
        row, col = int(rows[k]), int(cols[k])
        start, end = matrix.indptr[row], matrix.indptr[row + 1]
        row_cols = matrix.indices[start:end]
        j = np.searchsorted(row_cols, col)
        if j >= len(row_cols) or row_cols[j] != col:
            raise ValueError(
                f"Cell (row={row}, col={col}) is not an explicit entry in the matrix; "
                "cannot inject a sampled value there."
            )
        positions[k] = start + j
    return positions


def evaluate_lca_for_samples(lca, parameters, X):
    """Run one LCA score calculation per row of `X` (as produced by
    `sample_uncertain_parameters`), writing each sample's values directly
    into `lca.technosphere_matrix` / `lca.biosphere_matrix` before
    re-solving (`lci_calculation` + `lcia_calculation`; no factorized solver
    must be in use, since the technosphere matrix changes every iteration).

    Two or more parameters that land on the exact same matrix cell (an
    unusual but possible case if a database recorded more than one exchange
    between the same two nodes) have their sampled values summed for that
    cell, matching how `matrix_utils` aggregates duplicate entries when the
    matrix is normally built.

    Restores the matrices' original values before returning. Returns a
    1-D array of scores `Y`, aligned with the rows of `X`.
    """
    is_tech = parameters["matrix"] == "technosphere"

    tech_pos = _csr_data_positions(
        lca.technosphere_matrix, parameters["row"][is_tech], parameters["col"][is_tech]
    )
    bio_pos = _csr_data_positions(
        lca.biosphere_matrix, parameters["row"][~is_tech], parameters["col"][~is_tech]
    )

    tech_unique, tech_inverse = np.unique(tech_pos, return_inverse=True)
    bio_unique, bio_inverse = np.unique(bio_pos, return_inverse=True)

    baseline_tech = lca.technosphere_matrix.data[tech_unique].copy()
    baseline_bio = lca.biosphere_matrix.data[bio_unique].copy()

    Y = np.empty(X.shape[0])
    try:
        for i in range(X.shape[0]):
            if tech_unique.size:
                summed = np.zeros(tech_unique.shape)
                np.add.at(summed, tech_inverse, X[i, is_tech])
                lca.technosphere_matrix.data[tech_unique] = summed
            if bio_unique.size:
                summed = np.zeros(bio_unique.shape)
                np.add.at(summed, bio_inverse, X[i, ~is_tech])
                lca.biosphere_matrix.data[bio_unique] = summed

            lca.lci_calculation()
            lca.lcia_calculation()
            Y[i] = lca.score
    finally:
        lca.technosphere_matrix.data[tech_unique] = baseline_tech
        lca.biosphere_matrix.data[bio_unique] = baseline_bio
        lca.lci_calculation()
        lca.lcia_calculation()

    return Y


def screen_parameters_by_correlation(X, Y, top_k=None, min_abs_correlation=None, method="spearman"):
    """Cheap, vectorized screening pass over the D parameters in `X`.

    `SALib.analyze.delta` loops over every parameter one at a time, fitting a
    kernel density estimate and bootstrapping it (~100 resamples by default)
    for each -- a cost that scales with D and, on an ecoinvent-scale
    database with thousands of active uncertain exchanges, is typically what
    actually makes a run "take forever" (see the `technosphere[row,col]`
    "Bin Merge"/"Potential Bias" notices SALib prints from inside that
    loop) -- *not* the sampling or the LCA re-solves, which cost O(N) and
    are independent of D.

    This screens all D parameters using rank correlation (Spearman, the
    default -- robust to the LCIA score's often-skewed distribution; pass
    "pearson" for the linear coefficient instead) between each column of
    `X` and `Y`, computed as one vectorized operation with no per-parameter
    KDE/bootstrap. It reuses the *same* (X, Y) already produced for the full
    analysis, so it costs no extra LCA solves.

    Give at most one of `top_k` (keep the K parameters with the largest
    |correlation|) or `min_abs_correlation` (keep any parameter whose
    |correlation| clears a threshold); with neither, everything is kept.

    Returns `(keep, correlation)`: a boolean mask over X's columns (True =
    passed screening, worth the expensive delta/Sobol' step), and the
    signed correlation for every column (not just the kept ones), aligned
    with X's columns.
    """
    if method == "spearman":
        Xr = np.apply_along_axis(rankdata, 0, X)
        Yr = rankdata(Y)
    elif method == "pearson":
        Xr, Yr = X, Y
    else:
        raise ValueError("method must be 'spearman' or 'pearson'")

    Xc = Xr - Xr.mean(axis=0)
    Yc = Yr - Yr.mean()
    numerator = Xc.T @ Yc
    denominator = np.sqrt((Xc**2).sum(axis=0) * (Yc**2).sum())
    with np.errstate(divide="ignore", invalid="ignore"):
        correlation = np.where(denominator > 0, numerator / denominator, 0.0)

    if top_k is not None and min_abs_correlation is not None:
        raise ValueError("Give at most one of `top_k`, `min_abs_correlation`.")
    elif top_k is not None:
        top_k = min(top_k, len(correlation))
        order = np.argsort(np.abs(correlation))[::-1]
        keep = np.zeros(len(correlation), dtype=bool)
        keep[order[:top_k]] = True
    elif min_abs_correlation is not None:
        keep = np.abs(correlation) >= min_abs_correlation
    else:
        keep = np.ones(len(correlation), dtype=bool)

    return keep, correlation


def _normalize_delta_result(result):
    """Normalize the dict `SALib.analyze.delta.analyze` returns across SALib
    versions.

    Older releases return "delta"/"delta_conf". Newer ones (the ones that
    print the "[balanced] Bin Merge Notice" / "Potential Bias Notice" lines)
    replaced that with three variants instead -- "delta_raw"/"delta_raw_conf"
    (the classic bootstrap, equivalent to the old "delta"), "delta_balanced"
    (a bias-corrected version that stratifies the bootstrap across bins, the
    smaller-of the two when they diverge), and "delta_step" (for step-like,
    ~binary inputs) -- plus a "notes" field with any per-parameter warning
    (e.g. exactly the bin-merge/bias notices).

    Returns `(primary, primary_conf, raw, notes)`, using "delta_balanced" as
    the primary ranking metric when available (it's the one SALib itself
    recommends leaning on when it flags a raw/balanced mismatch), falling
    back to "delta_raw", then the old "delta" key, so this keeps working
    whichever SALib version is installed.
    """
    for primary_key, conf_key in (
        ("delta_balanced", "delta_balanced_conf"),
        ("delta_raw", "delta_raw_conf"),
        ("delta", "delta_conf"),
    ):
        if primary_key in result:
            primary = np.asarray(result[primary_key])
            primary_conf = np.asarray(result[conf_key])
            break
    else:
        raise KeyError(
            "Could not find a delta index in SALib's result (available keys: "
            f"{sorted(result.keys())}); SALib's return schema may have changed "
            "again -- update this helper to match."
        )
    raw = np.asarray(result["delta_raw"]) if "delta_raw" in result else primary
    notes = result.get("notes")
    return primary, primary_conf, raw, notes


DEFAULT_SOURCE_FIELDS = (
    "source", "sources", "reference", "references", "literature_source",
    "literatureReferences", "citation", "authors",
)


def exchange_documentation_status(
    exchange_metadata, node_metadata=None, source_fields=DEFAULT_SOURCE_FIELDS,
    comment_min_length=45,
):
    """Heuristic "is this coefficient's provenance documented" check.
    
    SHOULD BE ADAPATED TO THE STRUCTURE OF THE METADATA AND THE DESIRED LEVEL OF DOCUMENTATION

    Looks for any of `source_fields` populated on the exchange itself or
    on the node at the other end of it (whichever side this project
    happens to record it on), plus a fallback: a `comment` field (on
    either) at least `comment_min_length` characters long, on the theory
    that a real justification is rarely one word.

    This is a generic, schema-agnostic fallback -- it almost certainly
    needs tailoring to match this project's actual metadata convention
    for recording a coefficient's source paper (e.g. a specific custom
    key used elsewhere in this "Metadata_Phylogeny" workflow). Every
    function that runs this check takes `documentation_check` as a
    parameter, so pass a project-specific replacement with the same
    signature -- `(exchange_metadata, node_metadata) -> dict` with at
    least an "is_documented" bool key -- instead of editing this one.

    Returns a dict: "is_documented" (bool), "matched_fields" (dict of
    whichever `source_fields` were found and their value), "has_comment"
    (bool), "comment" (str, possibly empty).
    """
    node_metadata = node_metadata or {}
    matched = {}
    for field in source_fields:
        for meta in (exchange_metadata, node_metadata):
            value = meta.get(field)
            if value:
                matched.setdefault(field, value)
    comment = exchange_metadata.get("comment") or node_metadata.get("comment") or ""
    has_substantive_comment = len(comment.strip()) >= comment_min_length
    return {
        "is_documented": bool(matched) or has_substantive_comment,
        "matched_fields": matched,
        "has_comment": has_substantive_comment,
        "comment": comment,
    }


def _find_exchange(output_activity, input_node_id, matrix_kind):
    """Find the real `bw2data.Exchange` on `output_activity` whose input
    is the node with id `input_node_id` -- a technosphere link if
    `matrix_kind == "technosphere"`, a biosphere link otherwise.

    A GSA result's "input_key"/"output_key" are raw bw2data node ids (not
    (database, code) keys, despite the name -- `bd.get_activity` accepts
    either), matched here against `exc.input.id` rather than `exc.input.key`
    for that reason.

    Returns `None` if not found (shouldn't normally happen, since the id
    came from this same activity's own exchanges -- but matrix aggregation
    of duplicate cells, see `evaluate_lca_for_samples`'s docstring, could
    in principle merge two exchanges into one matrix cell and make this
    lookup ambiguous rather than missing; only the first match is returned
    in that case).
    """
    exchanges = (
        output_activity.technosphere() if matrix_kind == "technosphere"
        else output_activity.biosphere()
    )
    for exc in exchanges:
        if exc.input.id == input_node_id:
            return exc
    return None


def annotate_gsa_results_with_documentation(gsa_results, documentation_check=None):
    """Add an "is_documented" / "documentation_detail" (see
    `exchange_documentation_status`) to each entry of `gsa_results` (as
    returned by `global_sensitivity_analysis_matrix_exchanges` /
    `_rank_parameters_by_delta`), among the most sensitive parameters --
    the step this module's caller asked for: "does this influential
    coefficient have a reference/source (or at least a real comment) in
    its metadata."

    The raw matrix cell a delta index is computed for only carries the two
    endpoint node ids, not the actual exchange's own metadata dict (its
    `comment`, or whatever field this project uses for a source/reference),
    so this does one extra `_find_exchange` lookup per entry -- cheap,
    since `gsa_results` is only ever the top-N (tens, not thousands) of
    parameters, not the full screened set.

    Mutates and returns `gsa_results`, adding "exchange_metadata" (the
    resolved exchange's full `dict(exc)`), "is_documented" and
    "documentation_detail". Entries whose `output_activity` couldn't be
    resolved, or whose underlying exchange can't be found (see
    `_find_exchange`), get "is_documented": None instead of True/False --
    an explicit "unknown", not silently counted as undocumented.
    """
    if documentation_check is None:
        documentation_check = exchange_documentation_status

    for entry in gsa_results:
        output_activity = entry.get("output_activity")
        input_node_id = entry.get("input_key")
        if output_activity is None or input_node_id is None:
            entry["exchange_metadata"] = None
            entry["is_documented"] = None
            entry["documentation_detail"] = None
            continue

        exc = _find_exchange(output_activity, input_node_id, entry["matrix"])
        if exc is None:
            entry["exchange_metadata"] = None
            entry["is_documented"] = None
            entry["documentation_detail"] = None
            continue

        exc_metadata = dict(exc)
        input_activity = entry.get("input_activity")
        node_metadata = dict(input_activity) if input_activity is not None else {}
        doc = documentation_check(exc_metadata, node_metadata)
        entry["exchange_metadata"] = exc_metadata
        entry["is_documented"] = doc["is_documented"]
        entry["documentation_detail"] = doc

    return gsa_results


def _rank_parameters_by_delta(
    parameters, X, Y, top_n, screening_top_k, screening_method,
    delta_num_resamples, seed, verbose, _t_start=None,
    check_documentation=True, documentation_check=None,
):
    """Shared tail of the delta-GSA pipeline: optional correlation
    screening, then `SALib.analyze.delta`, formatted into a ranked list of
    dicts, then (if `check_documentation`) a reference/source check on just
    that top-N list via `annotate_gsa_results_with_documentation`. Factored
    out of `global_sensitivity_analysis_matrix_exchanges` so the hybrid,
    contribution-restricted analysis further down
    (`hybrid_metadata_risk_analysis`) can reuse the exact same
    screening/delta/formatting/documentation-check logic on a much smaller
    `parameters` set, instead of duplicating it.
    """
    n_params = len(parameters["row"])
    t1 = _t_start if _t_start is not None else time.perf_counter()

    if screening_top_k is not None and screening_top_k < n_params:
        keep, correlation = screen_parameters_by_correlation(
            X, Y, top_k=screening_top_k, method=screening_method
        )
        t2 = time.perf_counter()
        if verbose:
            print(
                f"[GSA] {screening_method} screening: kept {keep.sum()}/{n_params} "
                f"parameters ({t2 - t1:.1f}s)"
            )
    else:
        keep = np.ones(n_params, dtype=bool)
        correlation = np.zeros(n_params)
        t2 = t1

    kept_indices = np.flatnonzero(keep)
    X_kept = X[:, kept_indices]
    names = [
        f"{parameters['matrix'][i]}[{parameters['row'][i]},{parameters['col'][i]}]"
        for i in kept_indices
    ]
    problem = {"num_vars": len(kept_indices), "names": names}
    result = salib_delta.analyze(
        problem, X_kept, Y, seed=seed, num_resamples=delta_num_resamples
    )
    t3 = time.perf_counter()
    if verbose:
        print(f"[GSA] SALib delta.analyze on {len(kept_indices)} parameters: {t3 - t2:.1f}s")

    primary_delta, primary_delta_conf, raw_delta, notes = _normalize_delta_result(result)
    order = np.argsort(primary_delta)[::-1][:top_n]

    top = []
    for rank, k in enumerate(order, start=1):
        i = kept_indices[k]  # map back to the original (unscreened) parameter index
        input_key = parameters["input_key"][i]
        output_key = parameters["output_key"][i]
        top.append({
            "rank": rank,
            "delta": float(primary_delta[k]),
            "delta_conf": float(primary_delta_conf[k]),
            "delta_raw": float(raw_delta[k]),
            "note": notes[k] if notes is not None else None,
            "S1": float(result["S1"][k]),
            "S1_conf": float(result["S1_conf"][k]),
            "screening_correlation": float(correlation[i]),
            "matrix": str(parameters["matrix"][i]),
            "row": int(parameters["row"][i]),
            "col": int(parameters["col"][i]),
            "current_amount": float(parameters["current_amount"][i]),
            "input_key": input_key,
            "output_key": output_key,
            "input_activity": bd.get_activity(input_key) if input_key is not None else None,
            "output_activity": bd.get_activity(output_key) if output_key is not None else None,
        })

    if check_documentation and top:
        annotate_gsa_results_with_documentation(top, documentation_check=documentation_check)
        if verbose:
            n_undoc = sum(1 for e in top if e["is_documented"] is False)
            n_unknown = sum(1 for e in top if e["is_documented"] is None)
            print(
                f"[GSA] documentation check: {n_undoc}/{len(top)} of the top-ranked "
                f"exchanges are undocumented (no source/reference and no real comment)"
                + (f", {n_unknown} could not be resolved" if n_unknown else "") + "."
            )

    return top


def global_sensitivity_analysis_matrix_exchanges(
    activity,
    method,
    amount=1,
    n_samples=5,
    top_n=20,
    restrict_to_active_supply_chain=True,
    exclude_biosphere_without_characterization=False,
    characterization_tolerance=0.0,
    screening_top_k=500,
    screening_method="spearman",
    delta_num_resamples=100,
    check_documentation=True,
    documentation_check=None,
    seed=42,
    verbose=True,
):
    """Moment-independent (Delta, Borgonovo 2007 / Plischke et al. 2013, via
    `SALib.analyze.delta`) global sensitivity analysis of an LCA score with
    respect to every uncertain exchange amount in the technosphere and
    biosphere matrices, using the uncertainty distributions already stored
    in the project.

    Two-stage design, matching how this is kept tractable at LCA scale in
    the literature (e.g. Kim et al.'s `gsa_framework`, Cucurachi et al.
    2022 JIE 26(2):374-391): a single Monte Carlo batch of `n_samples`
    joint LCA re-solves is collected (cost O(n_samples), independent of how
    many parameters D there are), then a cheap rank-correlation screen
    (`screen_parameters_by_correlation`) picks the `screening_top_k`
    parameters most plausibly influential, and only *those* go through
    `SALib.analyze.delta`'s expensive per-parameter KDE/bootstrap loop
    (cost O(screening_top_k), not O(D)). On a full ecoinvent-scale database
    D (active uncertain exchanges) can run into the thousands, so this
    screening step is normally what determines whether the analysis
    finishes in minutes or hours -- see `screen_parameters_by_correlation`'s
    docstring.

    Returns a dict:
      "results": the `top_n` most sensitive exchanges (sorted by the delta
        index, descending), each a dict with:
        "rank", "delta", "delta_conf" (SALib's delta moment-independent
            index and its bootstrap CI -- the bias-corrected "balanced"
            estimate when the installed SALib version provides one,
            otherwise falls back to "raw"/the old plain "delta"; see
            `_normalize_delta_result`), "delta_raw" (the plain/uncorrected
            estimate, for comparison -- a large gap from "delta" is exactly
            what SALib's own "Potential Bias Notice" flags), "note" (any
            per-parameter warning SALib attached, e.g. a bin-merge notice,
            or None), "S1", "S1_conf" (the first-order Sobol' index SALib
            also computes alongside delta),
        "screening_correlation" (the Spearman/Pearson correlation that got
            this exchange past the screening step, for context),
        "matrix" ("technosphere"/"biosphere"), "row", "col",
        "current_amount" (the exchange's amount currently in the matrix),
        "input_key" / "output_key" (raw bw2data node ids -- accepted
            directly by `bd.get_activity`, despite the name),
        "input_activity" / "output_activity" (the resolved bw2data nodes,
            where resolvable),
        "exchange_metadata" (the real exchange's full `dict(exc)`, from
            `check_documentation`'s lookup -- includes its "comment" field
            among whatever else this project stores on it),
        "is_documented" (bool, or None if it couldn't be resolved) and
            "documentation_detail" (see `exchange_documentation_status`) --
            whether this influential exchange has a recognizable
            source/reference, or failing that a real (>=15 char) comment.
      "X": the raw `(n_samples, D)` Monte Carlo sample matrix (every
        active-supply-chain parameter, i.e. before `screening_top_k` cut it
        down for `delta.analyze` -- not just the plotted/ranked "results"),
        as produced by `sample_uncertain_parameters`.
      "Y": the corresponding `(n_samples,)` array of LCA scores, one per
        row of "X", from `evaluate_lca_for_samples`.
      "parameters": the full parameter metadata dict `X`'s D columns are
        aligned with (see `collect_uncertain_matrix_parameters`) -- needed
        to know which exchange a given column of "X" actually is, since
        "results" only covers the top_n.
      "lca": the already-solved `bw2calc.LCA` this run used (see
        `build_lca_for_gsa`) -- e.g. for `report_biosphere_weights`, or to
        inspect `lca.characterization_matrix` / `lca.score` /
        `lca.supply_array` directly, without a second LCA solve.
    No plotting is done with any of "X"/"Y"/"parameters"/"lca"; they're
    returned for your own inspection (e.g. checking a specific parameter's
    raw samples against Y, or re-running a different analysis over the
    same Monte Carlo batch without resampling).

    `check_documentation` (default True): run that reference/source check
    on the returned top-N list (see `annotate_gsa_results_with_documentation`
    -- cheap, since it's only ever the top-N, not every screened parameter).
    `documentation_check` overrides the default heuristic
    (`exchange_documentation_status`) with a project-specific one; see that
    function's docstring for the field list it looks for and how to adapt
    it if this project records a source/reference paper under a different
    metadata key than the generic ones it checks.

    `restrict_to_active_supply_chain` (default True) and
    `exclude_biosphere_without_characterization` /
    `characterization_tolerance` (default True / 0.0): see
    `collect_uncertain_matrix_parameters` -- the latter is what keeps a
    biosphere flow the chosen method assigns no weight to from ever being
    sampled at all, so it can't show up as "sensitive" by sampling-noise
    artifact (a real risk at low `n_samples`, since such a flow's true
    delta is exactly 0 but its *estimated* one, from a finite sample, is
    not). Set either to False/0 to sweep every uncertain cell regardless
    of relevance -- can be very large (millions of parameters) on a full
    ecoinvent-scale database.

    `screening_top_k` (default 500): how many parameters survive the cheap
    screen and get a real delta index. Set to `None` to skip screening
    entirely and run delta on every active-supply-chain parameter (this is
    what was slow before). `delta_num_resamples` (default 100, SALib's own
    default) is exposed directly since it's the other lever on
    `delta.analyze`'s per-parameter cost -- lowering it (e.g. to 20-30)
    trades tighter confidence intervals for speed.

    Cost: `n_samples` full LCA re-solves (one sparse linear system per
    sample) -- keep `n_samples` modest (hundreds, not many thousands) on
    large background databases; increase it for tighter confidence
    intervals once a smaller run confirms everything works as expected.
    """
    if salib_delta is None:
        raise ImportError(
            "SALib is required for this analysis (`pip install SALib`)."
        ) from _salib_import_error

    lca = build_lca_for_gsa(activity, method, amount=amount, verbose=verbose)
    parameters = collect_uncertain_matrix_parameters(
        lca, restrict_to_active_supply_chain=restrict_to_active_supply_chain,
        exclude_biosphere_without_characterization=exclude_biosphere_without_characterization,
        characterization_tolerance=characterization_tolerance,
    )
    n_params = len(parameters["row"])
    if n_params == 0:
        raise ValueError("No uncertain, sampleable exchanges found for this functional unit.")

    t0 = time.perf_counter()
    X = sample_uncertain_parameters(parameters, n_samples, seed=seed)
    Y = evaluate_lca_for_samples(lca, parameters, X)
    t1 = time.perf_counter()
    if verbose:
        print(
            f"[GSA] sampling + {n_samples} LCA re-solves over {n_params} parameters: "
            f"{t1 - t0:.1f}s"
        )

    top = _rank_parameters_by_delta(
        parameters, X, Y, top_n=top_n, screening_top_k=screening_top_k,
        screening_method=screening_method, delta_num_resamples=delta_num_resamples,
        seed=seed, verbose=verbose, _t_start=t1,
        check_documentation=check_documentation, documentation_check=documentation_check,
    )
    return {"results": top, "X": X, "Y": Y, "parameters": parameters, "lca": lca}


def _truncate(value, max_length):
    """`str(value)`, shortened to `max_length` chars with a trailing
    ellipsis if needed -- used to keep a plot's name line readable without
    mangling the (usually short) code line next to it."""
    text = str(value)
    return text if len(text) <= max_length else text[: max_length - 1] + "…"


def _default_gsa_entry_label(entry, max_name_length=45):
    """Default per-bar label for `plot_delta_sensitivity`: name(s) on one
    line, `[input code] -> [output code]` on the next -- falling back to
    the raw node id wherever a node, or its code, couldn't be resolved."""
    output_activity = entry.get("output_activity")
    out_name = output_activity["name"] if output_activity is not None else str(entry["output_key"])
    out_code = output_activity.get("code") if output_activity is not None else entry["output_key"]

    input_activity = entry.get("input_activity")
    in_name = input_activity["name"] if input_activity is not None else str(entry["input_key"])
    in_code = input_activity.get("code") if input_activity is not None else entry["input_key"]
    if entry["matrix"] == "biosphere":
        in_name = f"{in_name} (biosphere)"

    name_line = _truncate(f"{in_name} -> {out_name}", max_name_length)
    return f"{name_line}\n[{in_code}] -> [{out_code}]"


def plot_delta_sensitivity(gsa_results, ax=None, title=None, label_fn=None, max_name_length=45):
    """Horizontal bar chart of the delta moment-independent index for each
    exchange in `gsa_results` (as returned by
    `global_sensitivity_analysis_matrix_exchanges` /
    `hybrid_metadata_risk_analysis`'s "gsa" entry), with its SALib bootstrap
    confidence interval (`delta_conf`) drawn as an error bar -- the most
    sensitive exchange at the top.

    If `gsa_results` entries carry an "is_documented" key (true whenever
    `check_documentation=True`, the default -- see
    `annotate_gsa_results_with_documentation`), bars are colored by that: a
    neutral color when documented, a warning color when not, grey when
    unresolved/unknown -- so the plot doubles as "which influential
    exchanges also lack a reference," the other half of what was asked for
    here.

    `label_fn(entry) -> str` customizes the per-bar label (default:
    `_default_gsa_entry_label`, "<input> -> <output>" name(s) on one line,
    `[input code] -> [output code]` on the next, name(s) truncated to
    `max_name_length`).

    Returns the `Axes` used (a new figure is created if `ax` is None).
    """
    if not gsa_results:
        raise ValueError("gsa_results is empty -- nothing to plot.")
    if label_fn is None:
        label_fn = lambda entry: _default_gsa_entry_label(entry, max_name_length=max_name_length)

    # Reverse so the most sensitive (first/rank 1) ends up drawn at the top
    # of a `barh` plot, which otherwise stacks bottom-to-top.
    entries = list(reversed(gsa_results))
    labels = [label_fn(e) for e in entries]
    deltas = [e["delta"] for e in entries]
    errors = [e.get("delta_conf") or 0.0 for e in entries]

    has_doc_flags = all("is_documented" in e for e in entries)
    documented_color, undocumented_color, unknown_color = "#4C72B0", "#C44E52", "#999999"
    if has_doc_flags:
        colors = [
            documented_color if e["is_documented"] else
            unknown_color if e["is_documented"] is None else
            undocumented_color
            for e in entries
        ]
    else:
        colors = documented_color

    if ax is None:
        _, ax = plt.subplots(figsize=(9, max(3, 0.35 * len(entries))))

    ax.barh(labels, deltas, xerr=errors, color=colors, ecolor="black", capsize=3)
    ax.set_xlabel("Delta moment-independent index (± bootstrap CI)")
    ax.set_title(title or "Most sensitive exchanges")

    if has_doc_flags:
        from matplotlib.patches import Patch
        handles = [Patch(color=documented_color, label="documented")]
        if any(e["is_documented"] is False for e in entries):
            handles.append(Patch(color=undocumented_color, label="undocumented"))
        if any(e["is_documented"] is None for e in entries):
            handles.append(Patch(color=unknown_color, label="unresolved"))
        ax.legend(handles=handles, loc="lower right")

    ax.figure.tight_layout()
    return ax


def report_biosphere_weights(gsa_results, lca):
    """Direct, GSA-machinery-independent check of whether a biosphere
    exchange showing up in `gsa_results` (a "results" list, as returned by
    `global_sensitivity_analysis_matrix_exchanges` -- pass `gsa_output["lca"]`
    for `lca`) genuinely has any weight under the chosen method at all.

    With `exclude_biosphere_without_characterization=True` (the default),
    every entry here should already show a nonzero weight, since such flows
    are now excluded before ever being sampled -- this is the
    belt-and-suspenders check for when that filter was turned off, or to
    double-check the filter itself is doing what it claims. Prints one
    line per biosphere entry: its delta index next to its own row's total
    characterization weight (`_biosphere_flow_weights`) -- a weight of
    exactly 0 means something in the sampling/scoring pipeline is wrong
    and worth reporting; a small but nonzero weight means the method does
    characterize that flow, just perhaps not under the name expected.
    """
    flow_weights = _biosphere_flow_weights(lca)
    bio_entries = [e for e in gsa_results if e["matrix"] == "biosphere"]
    if not bio_entries:
        print("[Weights check] no biosphere exchanges in gsa_results.")
        return
    for e in bio_entries:
        weight = float(flow_weights[e["row"]])
        input_activity = e.get("input_activity")
        name = input_activity["name"] if input_activity is not None else str(e["input_key"])
        flag = "  <-- ZERO WEIGHT, should not be possible with the filter on" if weight == 0 else ""
        print(f"delta={e['delta']:.4g}  weight={weight:.6g}  {name}{flag}")


# Example usage (adjust the method and activity to your project):

method = ("ecoinvent-3.10", "IPCC 2013", "climate change", "global warming potential (GWP100)")
gsa_output = global_sensitivity_analysis_matrix_exchanges(
    example_activity, method, n_samples=100, top_n=20,
)
top_sensitive_exchanges = gsa_output["results"]
gsa_X, gsa_Y, gsa_parameters, gsa_lca = (
    gsa_output["X"], gsa_output["Y"], gsa_output["parameters"], gsa_output["lca"],
)

report_biosphere_weights(top_sensitive_exchanges, gsa_lca)

for entry in top_sensitive_exchanges:
    print(
        entry["rank"], entry["delta"], entry["matrix"], entry["input_activity"], "->",
        entry["output_activity"], "| documented:", entry["is_documented"],
    )

plot_delta_sensitivity(top_sensitive_exchanges)
plt.show()


# =====================================================================
# 2) Recursive contribution analysis + metadata/documentation audit
# =====================================================================
#
# The GSA above answers "how much does this exchange's *uncertainty*
# move the score" -- it needs a real distribution and Monte Carlo, and
# its cost scales with the number of uncertain cells in the *whole*
# active supply chain (thousands, on an ecoinvent-scale background),
# which is exactly why it's heavy.
#
# What's actually being asked here is a different, cheaper question:
# "how much of the *point-estimate* score flows through this exchange,
# right now" -- plain contribution analysis, the same idea as
# brightway's legacy `GraphTraversal` / Activity Browser's Sankey
# diagrams. It needs a single LCA solve plus one sparse LU factorization
# of the technosphere matrix (`_UnitScoreSolver`, reused for every node's
# "score to produce exactly 1 unit of this activity" query), and it walks
# the *real* `Activity.technosphere()` / `.biosphere()` exchanges (not
# raw matrix cells), so every recorded coefficient carries its full
# bw2data metadata dict -- including whatever field(s) this project uses
# to record a source/reference paper -- for a documentation check.
#
# Recursion is pruned by a relative-score cutoff (an exchange whose
# branch contributes less than `cutoff` of the total score is not
# expanded further), the same mechanism legacy `GraphTraversal` uses to
# stay tractable on a full ecoinvent-scale background: cost scales with
# the number of branches that clear the cutoff (typically a few hundred
# nodes for a 0.5-2% cutoff), not with the size of the database.
#
# `hybrid_metadata_risk_analysis` at the bottom chains the two: run the
# cheap contribution scan first to find the (typically a few dozen)
# undocumented coefficients that actually matter for this functional
# unit, then run the existing GSA machinery restricted to just that set
# -- so the expensive per-parameter SALib delta step runs on tens of
# parameters instead of thousands.

from scipy.sparse.linalg import splu

# `DEFAULT_SOURCE_FIELDS` / `exchange_documentation_status` used to live here,
# but the plain delta-GSA pipeline above now runs the same documentation
# check on its own top-N results (`annotate_gsa_results_with_documentation`),
# and that code executes earlier in the file (see its "Example usage" block)
# than this section is defined -- so both now live next to
# `_normalize_delta_result`, above, as the single shared definition.


class _UnitScoreSolver:
    """Caches one sparse LU factorization (`scipy.sparse.linalg.splu`) of
    `lca.technosphere_matrix` so that "the LCA score of producing exactly
    one unit of any activity's reference product" can be answered with a
    single cheap triangular solve per new node, instead of a full LCA
    re-solve -- this is what makes recursing arbitrarily deep into the
    supply chain tractable.

    Assumes one reference product per activity, i.e. a square
    technosphere matrix (true for standard allocated databases like
    ecoinvent's cutoff/consequential/APOS system models).
    """

    def __init__(self, lca):
        if lca.technosphere_matrix.shape[0] != lca.technosphere_matrix.shape[1]:
            raise ValueError(
                "technosphere_matrix is not square -- this fast per-node "
                "unit-score solve assumes one reference product per "
                "activity (true for standard allocated ecoinvent-style "
                "databases)."
            )
        self.lca = lca
        self._lu = splu(lca.technosphere_matrix.tocsc())
        self._n_rows = lca.technosphere_matrix.shape[0]
        self._flow_weights = _biosphere_flow_weights(lca)
        self._cache = {}

    def score_per_unit(self, activity_node):
        key = activity_node.id
        if key not in self._cache:
            row = self.lca.dicts.product[key]
            demand = np.zeros(self._n_rows)
            demand[row] = 1.0
            supply = self._lu.solve(demand)
            inventory = self.lca.biosphere_matrix @ supply
            score = (self.lca.characterization_matrix @ inventory).sum()
            self._cache[key] = float(score)
        return self._cache[key]

    def biosphere_flow_weight(self, flow_node):
        row = self.lca.dicts.biosphere[flow_node.id]
        return float(self._flow_weights[row])


def recursive_contribution_metadata_scan(
    activity,
    method,
    amount=1,
    cutoff=0.01,
    max_depth=15,
    max_visits=50000,
    documentation_check=None,
    verbose=True,
):
    """Recursively walk `activity`'s supply chain, visiting every node
    whose incoming branch contributes at least `cutoff` of the total LCIA
    score, and record *every* technosphere and biosphere exchange
    belonging to *every visited node* -- not just the ones that themselves
    clear `cutoff` -- checking each one for whether it looks documented
    (see `exchange_documentation_status` / `documentation_check`) along
    the way.

    `cutoff` therefore no longer decides what gets *returned* (everything
    a visited node has does), only what gets *recursed into further*: an
    exchange whose own branch is too small to expand is still recorded as
    a (leaf) entry, with `meets_cutoff=False`, it just isn't walked past.
    This keeps the traversal itself just as tractable as before (recursion
    depth is still pruned by `cutoff`), while the returned list reflects
    every exchange actually looked at, so nothing a visited node has is
    silently dropped from the documentation check or later plots.

    See the module-level comment above for how this differs from (and
    is meant to be combined with) the GSA further up.

    Returns `(edges, lca)`:
      `edges` -- a list of dicts, sorted by |fraction_of_total|
        descending, one per exchange belonging to a visited node:
          "type": "technosphere" or "biosphere"
          "depth", "path" (list of (database, code) keys from the root
            down to, but not including, this exchange's consumer)
          "consumer_key", "consumer_id"
          "producer_key", "producer_id" (technosphere) or "flow_key",
            "flow_id" (biosphere)
          "exchange_amount" (the exchange's own stored amount)
          "cumulative_amount" (that amount scaled by how much of the
            consumer is actually being produced at this point in the
            tree)
          "score_contribution", "fraction_of_total"
          "meets_cutoff" (bool -- whether this edge was large enough to
            be recursed into further; small/leaf edges are still
            included, just with this False)
          "exchange_metadata" (full `dict(exchange)`)
          "is_documented", "documentation_detail" (from
            `documentation_check`)
      `lca` -- the underlying, already-solved `bw2calc.LCA`. Reuse it
        (don't rebuild) if you need `lca.score`, `lca.dicts`, etc., or
        want to feed the same node identity space into
        `restrict_parameters_to_edges`.

    `cutoff` is the main cost/completeness lever for how *deep* the
    recursion goes: lower catches more but visits more nodes (cost is
    roughly proportional to the number of branches that clear it, not to
    database size or to `len(edges)`, which also grows with how many
    exchanges each visited node happens to have). `max_depth` and
    `max_visits` are hard safety stops for pathological/cyclic supply
    chains (recycling loops are common in ecoinvent); in practice the
    cutoff prunes those long before either limit is reached, since each
    pass through a converging loop multiplies the contribution by a
    fraction less than one. Downstream consumers that only want the
    significant ones (e.g. `flag_coefficients_to_check`,
    `plot_contribution_documentation`) filter/rank `edges` themselves,
    typically by `abs(fraction_of_total)` and/or `meets_cutoff`.
    """
    t0 = time.perf_counter()
    lca = bc.LCA({activity: amount}, method)
    lca.lci()
    lca.lcia()
    if verbose:
        print(f"[Contribution scan] build + solve baseline LCA: {time.perf_counter() - t0:.1f}s")
    total_score = lca.score
    if total_score == 0:
        raise ValueError("Total LCA score is 0 -- a relative cutoff is undefined.")

    solver = _UnitScoreSolver(lca)
    if documentation_check is None:
        documentation_check = exchange_documentation_status

    edges = []
    state = {"visits": 0}

    def node_key(node):
        return (node.get("database"), node.get("code"))

    def visit(node_activity, node_amount, depth, path):
        state["visits"] += 1
        if state["visits"] > max_visits:
            return

        for exc in node_activity.biosphere():
            flow = exc.input
            contribution = node_amount * exc["amount"] * solver.biosphere_flow_weight(flow)
            fraction = contribution / total_score
            exc_metadata = dict(exc)
            doc = documentation_check(exc_metadata, dict(flow))
            edges.append({
                "type": "biosphere",
                "depth": depth,
                "path": path + [node_key(node_activity)],
                "consumer_key": node_key(node_activity),
                "consumer_id": node_activity.id,
                "flow_key": node_key(flow),
                "flow_id": flow.id,
                "exchange_amount": exc["amount"],
                "cumulative_amount": node_amount * exc["amount"],
                "score_contribution": contribution,
                "fraction_of_total": fraction,
                "meets_cutoff": abs(fraction) >= cutoff,  # biosphere is always a leaf; informational only
                "exchange_metadata": exc_metadata,
                "is_documented": doc["is_documented"],
                "documentation_detail": doc,
            })

        if depth >= max_depth:
            return

        for exc in node_activity.technosphere():
            producer = exc.input
            if producer.id == node_activity.id:
                continue  # skip self-loops
            edge_amount = node_amount * exc["amount"]
            producer_unit_score = solver.score_per_unit(producer)
            contribution = edge_amount * producer_unit_score
            fraction = contribution / total_score
            meets_cutoff = abs(fraction) >= cutoff

            exc_metadata = dict(exc)
            doc = documentation_check(exc_metadata, dict(producer))
            edges.append({
                "type": "technosphere",
                "depth": depth,
                "path": path + [node_key(node_activity)],
                "consumer_key": node_key(node_activity),
                "consumer_id": node_activity.id,
                "producer_key": node_key(producer),
                "producer_id": producer.id,
                "exchange_amount": exc["amount"],
                "cumulative_amount": edge_amount,
                "score_contribution": contribution,
                "fraction_of_total": fraction,
                "meets_cutoff": meets_cutoff,
                "exchange_metadata": exc_metadata,
                "is_documented": doc["is_documented"],
                "documentation_detail": doc,
            })

            # Every exchange of a visited node is recorded above regardless
            # of size; only branches that clear `cutoff` get walked further,
            # which is what keeps the recursion itself tractable.
            if meets_cutoff:
                visit(producer, edge_amount, depth + 1, path + [node_key(node_activity)])

    visit(activity, amount, 0, [])

    edges.sort(key=lambda e: abs(e["fraction_of_total"]), reverse=True)
    if verbose:
        n_undocumented = sum(1 for e in edges if not e["is_documented"])
        n_expanded = sum(1 for e in edges if e["meets_cutoff"])
        print(
            f"[Contribution scan] total_score={total_score:.4g}, visited "
            f"{state['visits']} nodes, recorded {len(edges)} exchanges total "
            f"({n_expanded} >= {cutoff:.2%} of score and expanded further, "
            f"{n_undocumented} flagged as undocumented)."
        )
    return edges, lca


def flag_coefficients_to_check(edges, top_n=None, min_fraction=None):
    """Filter `edges` (from `recursive_contribution_metadata_scan`) down
    to the undocumented ones, sorted by |contribution| descending -- the
    actionable "check these" list. `min_fraction` (e.g. 0.02) additionally
    requires at least that share of the total score; `top_n` caps the
    list length."""
    flagged = [e for e in edges if not e["is_documented"]]
    if min_fraction is not None:
        flagged = [e for e in flagged if abs(e["fraction_of_total"]) >= min_fraction]
    flagged.sort(key=lambda e: abs(e["fraction_of_total"]), reverse=True)
    return flagged[:top_n] if top_n is not None else flagged


def print_flagged_coefficients(flagged, limit=20):
    """Human-readable dump of a `flag_coefficients_to_check` result."""
    for i, e in enumerate(flagged[:limit], start=1):
        if e["type"] == "technosphere":
            where = f"{e['producer_key']} -> {e['consumer_key']}"
        else:
            where = f"{e['flow_key']} (biosphere) @ {e['consumer_key']}"
        comment = e["documentation_detail"]["comment"][:60]
        print(
            f"{i:>3}. {e['fraction_of_total']:>7.2%}  depth={e['depth']:<2} "
            f"{e['type']:<12} {where}  amount={e['exchange_amount']:.4g}  "
            f"comment={comment!r}"
        )


def _default_contribution_entry_label(edge, max_name_length=45):
    """Default per-bar label for `plot_contribution_documentation`: name(s)
    on one line, `[input code] -> [output code]` on the next. Codes are
    read straight off the edge's own `*_key` tuples (`(database, code)`,
    no lookup needed); names need one `bd.get_activity` call each -- fine
    here since this only ever runs for whichever edges actually get
    plotted (`top_n` of them), not the full, possibly large, `edges` list.
    """
    consumer_key = edge["consumer_key"]
    consumer_name = bd.get_activity(consumer_key)["name"] if edge.get("consumer_id") is not None else str(consumer_key)

    input_key = edge["producer_key"] if edge["type"] == "technosphere" else edge["flow_key"]
    input_id = edge.get("producer_id") if edge["type"] == "technosphere" else edge.get("flow_id")
    input_name = bd.get_activity(input_key)["name"] if input_id is not None else str(input_key)
    if edge["type"] == "biosphere":
        input_name = f"{input_name} (biosphere)"

    name_line = _truncate(f"{input_name} -> {consumer_name}", max_name_length)
    return f"{name_line}\n[{input_key[1]}] -> [{consumer_key[1]}]"


def plot_contribution_documentation(
    edges, top_n=30, ax=None, title=None, label_fn=None, max_name_length=45,
):
    """Horizontal bar chart of |contribution to the total score| for the
    `top_n` largest-magnitude exchanges in `edges` (from
    `recursive_contribution_metadata_scan`), colored by "is_documented" --
    the same documented/undocumented/unresolved view as
    `plot_delta_sensitivity`, but for share of the point-estimate score
    rather than delta sensitivity to uncertainty. `edges` is typically much
    larger than what's plotted (every exchange belonging to every visited
    node, see that function's docstring), so this ranks by
    `abs(fraction_of_total)` and keeps only the top `top_n`.

    `label_fn(edge) -> str` customizes the per-bar label (default:
    `_default_contribution_entry_label`, name(s) on one line,
    `[input code] -> [output code]` on the next, name(s) truncated to
    `max_name_length`).

    Returns the `Axes` used (a new figure is created if `ax` is None).
    """
    if not edges:
        raise ValueError("edges is empty -- nothing to plot.")
    if label_fn is None:
        label_fn = lambda edge: _default_contribution_entry_label(edge, max_name_length=max_name_length)

    ranked = sorted(edges, key=lambda e: abs(e["fraction_of_total"]), reverse=True)[:top_n]
    # Reverse so the largest contributor ends up drawn at the top of a
    # `barh` plot, which otherwise stacks bottom-to-top.
    entries = list(reversed(ranked))

    labels = [label_fn(e) for e in entries]
    percentages = [e["fraction_of_total"] * 100 for e in entries]

    documented_color, undocumented_color, unknown_color = "#4C72B0", "#C44E52", "#999999"
    colors = [
        undocumented_color if e["is_documented"] is False else
        unknown_color if e["is_documented"] is None else
        documented_color
        for e in entries
    ]

    if ax is None:
        _, ax = plt.subplots(figsize=(9, max(3, 0.35 * len(entries))))

    ax.barh(labels, percentages, color=colors)
    ax.set_xlabel("Contribution to total score (%)")
    ax.set_title(title or f"Largest contributing exchanges (top {len(entries)} of {len(edges)})")

    from matplotlib.patches import Patch
    handles = [Patch(color=documented_color, label="documented")]
    if any(e["is_documented"] is False for e in entries):
        handles.append(Patch(color=undocumented_color, label="undocumented"))
    if any(e["is_documented"] is None for e in entries):
        handles.append(Patch(color=unknown_color, label="unresolved"))
    ax.legend(handles=handles, loc="lower right")

    ax.figure.tight_layout()
    return ax


def restrict_parameters_to_edges(parameters, lca, edges):
    """Build a `parameters`-shaped subset (see
    `collect_uncertain_matrix_parameters`) containing only the matrix
    cells backing the given contribution-analysis `edges` -- i.e.
    intersect "flagged by the recursive contribution scan" with "actually
    carries a real, sampleable uncertainty distribution". `lca` must be
    the same LCA instance `parameters` was built from (row/col indices
    are only meaningful relative to one LCA's own `.dicts`); node
    identity is resolved through each edge's `*_id` via that LCA's own
    dicts, so it's safe for `edges` to have come from a *different*
    LCA instance (e.g. the plain contribution-scan one), as long as it
    was built for the same functional unit/database state.
    """
    wanted = set()
    for e in edges:
        col = lca.dicts.activity[e["consumer_id"]]
        if e["type"] == "technosphere":
            row = lca.dicts.product[e["producer_id"]]
            wanted.add(("technosphere", row, col))
        else:
            row = lca.dicts.biosphere[e["flow_id"]]
            wanted.add(("biosphere", row, col))

    mask = np.fromiter(
        ((m, r, c) in wanted
         for m, r, c in zip(parameters["matrix"], parameters["row"], parameters["col"])),
        dtype=bool, count=len(parameters["row"]),
    )
    out = {}
    for key, val in parameters.items():
        if key in ("input_key", "output_key"):
            out[key] = [v for v, keep in zip(val, mask) if keep]
        else:
            out[key] = np.asarray(val)[mask]
    return out


def hybrid_metadata_risk_analysis(
    activity,
    method,
    amount=1,
    cutoff=0.01,
    max_depth=15,
    documentation_check=None,
    run_gsa_on_flagged=True,
    gsa_n_samples=200,
    gsa_top_n=30,
    gsa_delta_num_resamples=100,
    seed=42,
    verbose=True,
):
    """Recommended entry point. Two rankings, run in cheap-then-expensive
    order, answer two different questions about the same coefficients:

      1. Contribution (cheap, always run): `recursive_contribution_metadata_scan`
         finds every exchange that clears `cutoff` of the *point-estimate*
         score, and checks whether it's documented. This alone is
         normally enough to build a "coefficients to check" list.
      2. Sensitivity (optional, `run_gsa_on_flagged=True`): the existing
         delta-GSA machinery further up, but restricted to only the
         *flagged* (undocumented + significant) coefficients that also
         carry a real uncertainty distribution -- so the expensive
         per-parameter SALib step runs on tens of parameters instead of
         every uncertain cell in the active supply chain, which is what
         made the whole-matrix version slow.

    A coefficient can score high on one and low on the other -- a large
    but well-constrained (low-uncertainty) input scores high on
    contribution, low on delta; a small but wildly uncertain one can be
    the reverse. Both are independent reasons to check the metadata
    behind the number, so flagging is done on contribution +
    documentation (step 1) and delta is reported as extra context where
    available (step 2), not used as an additional filter.

    Returns a dict:
      "edges": every edge from step 1 (not just flagged ones)
      "flagged": the undocumented, significant ones (`flag_coefficients_to_check`)
      "gsa": `None` if `run_gsa_on_flagged=False` or nothing flagged carried
        a sampleable distribution, otherwise a dict (same shape
        `global_sensitivity_analysis_matrix_exchanges` returns): "results"
        (step 2's ranked list, see `_rank_parameters_by_delta`), "X"/"Y"
        (the Monte Carlo sample matrix and scores this restricted GSA pass
        used, for your own inspection -- not plotted), "parameters" (the
        metadata "X"'s columns are aligned with), "lca" (this GSA pass's
        own solved LCA -- distinct from the top-level "lca" below, which
        is step 1's).
      "lca": the contribution-scan LCA (already solved)
    """
    edges, lca = recursive_contribution_metadata_scan(
        activity, method, amount=amount, cutoff=cutoff, max_depth=max_depth,
        documentation_check=documentation_check, verbose=verbose,
    )
    # `edges` now includes every exchange belonging to every visited node
    # (see `recursive_contribution_metadata_scan`), not just the ones that
    # individually clear `cutoff` -- so `min_fraction=cutoff` here restores
    # this function's original "significant AND undocumented" flagged set
    # (keeping the restricted GSA step below tens, not thousands, of
    # parameters), while `edges` itself (also returned, below) still
    # carries everything for anyone who wants the full picture.
    flagged = flag_coefficients_to_check(edges, min_fraction=cutoff)
    if verbose:
        print(f"[Hybrid] {len(flagged)}/{len(edges)} significant coefficients are undocumented.")

    gsa_results = None
    if run_gsa_on_flagged and flagged:
        if salib_delta is None:
            raise ImportError(
                "SALib is required for the GSA step (`pip install SALib`)."
            ) from _salib_import_error

        gsa_lca = build_lca_for_gsa(activity, method, amount=amount, verbose=verbose)
        gsa_parameters_all = collect_uncertain_matrix_parameters(
            gsa_lca, restrict_to_active_supply_chain=True
        )
        gsa_parameters = restrict_parameters_to_edges(gsa_parameters_all, gsa_lca, flagged)
        n_params = len(gsa_parameters["row"])
        if n_params == 0:
            if verbose:
                print(
                    "[Hybrid] none of the flagged coefficients carry a sampleable "
                    "uncertainty distribution -- skipping the GSA step."
                )
        else:
            X = sample_uncertain_parameters(gsa_parameters, gsa_n_samples, seed=seed)
            Y = evaluate_lca_for_samples(gsa_lca, gsa_parameters, X)
            top = _rank_parameters_by_delta(
                gsa_parameters, X, Y, top_n=min(gsa_top_n, n_params),
                screening_top_k=None, screening_method="spearman",
                delta_num_resamples=gsa_delta_num_resamples, seed=seed, verbose=verbose,
            )
            gsa_results = {
                "results": top, "X": X, "Y": Y, "parameters": gsa_parameters, "lca": gsa_lca,
            }

    return {"edges": edges, "flagged": flagged, "gsa": gsa_results, "lca": lca}


# Example usage: the cheap first pass (contribution + documentation only)
# is normally enough on its own to build the "coefficients to check"
# list -- start here, and only add the GSA step once this confirms
# things work as expected on this project's actual metadata schema
# (`exchange_documentation_status`'s default field list almost certainly
# needs adjusting first -- see its docstring).

contribution_edges, contribution_lca = recursive_contribution_metadata_scan(
    example_activity, method, cutoff=0.01, max_depth=15,
)
coefficients_to_check = flag_coefficients_to_check(contribution_edges, top_n=30)
print_flagged_coefficients(coefficients_to_check)

plot_contribution_documentation(contribution_edges, top_n=30)
plt.show()

# Full hybrid (adds a restricted GSA pass over just the flagged
# coefficients that also carry a real uncertainty distribution):
#
# hybrid_report = hybrid_metadata_risk_analysis(
#     example_activity, method, cutoff=0.01, max_depth=15, gsa_n_samples=200,
# )
# if hybrid_report["gsa"]:
#     plot_delta_sensitivity(
#         hybrid_report["gsa"]["results"], title="Flagged coefficients -- delta sensitivity"
#     )
#     plt.show()
#     # hybrid_report["gsa"]["X"] / ["Y"] / ["parameters"] are also available
#     # here, same as global_sensitivity_analysis_matrix_exchanges's return.