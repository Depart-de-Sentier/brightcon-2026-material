"""Run benchmark grids using a real script and one process per solver case."""

import json
import subprocess
import sys
from itertools import product
from pathlib import Path
from time import perf_counter

import psutil


def run_benchmark(
    name,
    *,
    sizes,
    solvers,
    topology="constant-degree",
    degree=8,
    degrees=None,
    densities=None,
    rhs_counts=None,
    matrix_family="lca-random",
    blocks=8,
    rtol=1e-4,
    seed=2026,
    restart=50,
    maxiter=300,
    worker_timeout=60,
    total_budget=None,
    memory_guard_mib=None,
    construction_memory_multiplier=3.0,
):
    """Return every requested case, including failures and cases skipped for safety.

    The memory estimate covers matrix construction, not LU factorization.
    Each subprocess has a time limit; the notebook itself stays in this process.
    """
    if memory_guard_mib is None:
        memory_guard_mib = min(8192, psutil.virtual_memory().available / 2**20 * 0.25)
    script = Path(__file__).with_name("benchmark_synthetic.py")
    started = perf_counter()
    results = []
    cases = product(
        sizes, degrees or [degree], densities or [0.001], rhs_counts or [1], solvers
    )
    for size, links, density, rhs_count, solver in cases:
        if topology == "fixed-density":
            estimated_nnz = int(size * size * density) + size
        elif topology == "banded":
            estimated_nnz = size * (2 * links + 1)
        else:
            estimated_nnz = size * (links + 1)
        # Allow 64-bit indices and construction copies, plus dense storage if needed.
        storage_bytes = estimated_nnz * 16 + (size + 1) * 8
        construction_mib = storage_bytes * construction_memory_multiplier / 2**20
        if solver == "numpy-dense":
            construction_mib += size * size * 8 * 3 / 2**20
        result = dict(
            suite=name,
            solver=solver,
            size=size,
            shape=[size, size],
            topology=topology,
            degree=links,
            target_density=density if topology == "fixed-density" else None,
            matrix_family=matrix_family,
            rhs_count=rhs_count,
            seed=seed,
            rtol=rtol,
            restart=restart,
            maxiter=maxiter,
            estimated_nnz=estimated_nnz,
            estimated_construction_mib=construction_mib,
            status="SKIPPED",
            error="",
            skip_reason="",
            converged=False,
            solve_seconds=None,
            factorization_seconds=None,
            rhs_solve_seconds=None,
            peak_rss_bytes=None,
            incremental_peak_rss_bytes=None,
            relative_residual=None,
            density=None,
        )
        remaining = (
            None if total_budget is None else total_budget - (perf_counter() - started)
        )
        if construction_mib > memory_guard_mib:
            result["skip_reason"] = "MEMORY GUARD"
        elif solver == "numpy-dense" and size > 2500:
            result["skip_reason"] = "DENSE SIZE LIMIT"
        elif remaining is not None and remaining <= 0:
            result["skip_reason"] = "TIME BUDGET"
        else:
            options = dict(
                solver=solver,
                size=size,
                topology=topology,
                degree=links,
                density=density,
                matrix_family=matrix_family,
                blocks=blocks,
                rhs_count=rhs_count,
                seed=seed,
                rtol=rtol,
                restart=restart,
                maxiter=maxiter,
            )
            command = [sys.executable, str(script)]
            for key, value in options.items():
                command.extend(["--" + key.replace("_", "-"), str(value)])
            timeout = (
                worker_timeout if remaining is None else min(worker_timeout, remaining)
            )
            case_started = perf_counter()
            try:
                completed = subprocess.run(
                    command, capture_output=True, text=True, check=True, timeout=timeout
                )
                result.update(json.loads(completed.stdout))
                result["status"] = "COMPLETED" if result["converged"] else "FAILED"
                if not result["converged"]:
                    result["error"] = "Convergence or residual check failed"
            except subprocess.TimeoutExpired:
                result["status"] = "TIMEOUT"
            except subprocess.CalledProcessError as error:
                result.update(status="FAILED", error=error.stderr[-2000:])
            except (ValueError, OSError) as error:
                result.update(status="FAILED", error=str(error))
            result["worker_wall_seconds"] = perf_counter() - case_started
        results.append(result)
    print(
        f"{name}: "
        + ", ".join(
            f"{sum(r['status'] == status for r in results)} {status}"
            for status in ["COMPLETED", "SKIPPED", "TIMEOUT", "FAILED"]
        )
    )
    return {"results": results, "suite_wall_seconds": perf_counter() - started}
