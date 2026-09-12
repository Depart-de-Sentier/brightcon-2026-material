"""Run one isolated synthetic linear-system benchmark and emit JSON.

Each invocation handles one matrix and one solver so peak RSS measurements are
not contaminated by allocations retained by an earlier solver.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import threading
import time
from dataclasses import dataclass

import numpy as np
import psutil
import scipy
from scipy import sparse
from scipy.sparse.linalg import LinearOperator, gmres, splu, spsolve


@dataclass
class MemoryMonitor:
    interval_seconds: float = 0.002

    def __post_init__(self) -> None:
        self.process = psutil.Process()
        self.baseline_bytes = self.process.memory_info().rss
        self.peak_bytes = self.baseline_bytes
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._poll, daemon=True)

    def _poll(self) -> None:
        while not self._stop.is_set():
            self.peak_bytes = max(self.peak_bytes, self.process.memory_info().rss)
            time.sleep(self.interval_seconds)

    def __enter__(self) -> "MemoryMonitor":
        self._thread.start()
        return self

    def __exit__(self, *_: object) -> None:
        self._stop.set()
        self._thread.join()
        self.peak_bytes = max(self.peak_bytes, self.process.memory_info().rss)

    @property
    def incremental_peak_bytes(self) -> int:
        return max(0, self.peak_bytes - self.baseline_bytes)


def constant_degree_matrix(
    n: int, degree: int, seed: int, diagonal_span: float
) -> sparse.csc_matrix:
    if degree < 1 or degree >= n:
        raise ValueError("degree must be between 1 and n - 1")
    rng = np.random.default_rng(seed)
    columns = np.repeat(np.arange(n, dtype=np.int64), degree)
    rows = rng.integers(0, n, size=n * degree, dtype=np.int64)
    diagonal_hits = rows == columns
    rows[diagonal_hits] = (rows[diagonal_hits] + 1) % n

    # Keep each column's absolute off-diagonal sum comfortably below one.
    coefficients = rng.uniform(0.01, 0.04, size=n * degree)
    off_diagonal = sparse.coo_matrix(
        (-coefficients, (rows, columns)), shape=(n, n)
    ).tocsc()
    matrix = sparse.eye(n, format="csc") + off_diagonal
    row_scales = 10 ** rng.uniform(-diagonal_span / 2, diagonal_span / 2, size=n)
    matrix = sparse.diags(row_scales, format="csc") @ matrix
    matrix.sum_duplicates()
    matrix.eliminate_zeros()
    matrix.sort_indices()
    return matrix


def banded_matrix(
    n: int,
    half_bandwidth: int,
    seed: int,
    diagonal_span: float,
    coupling: float = 0.8,
) -> sparse.csc_matrix:
    """Build a sparse, locally connected matrix with predictable low LU fill-in."""
    if half_bandwidth < 1 or half_bandwidth >= n:
        raise ValueError("half_bandwidth must be between 1 and n - 1")
    if not 0 < coupling < 1:
        raise ValueError("coupling must be between zero and one")

    coefficient = coupling / (2 * half_bandwidth)
    offsets = [
        offset for offset in range(-half_bandwidth, half_bandwidth + 1) if offset
    ]
    diagonals = [
        -coefficient * np.ones(n - abs(offset), dtype=float) for offset in offsets
    ]
    matrix = sparse.eye(n, format="csc") + sparse.diags(
        diagonals, offsets, shape=(n, n), format="csc"
    )

    rng = np.random.default_rng(seed)
    row_scales = 10 ** rng.uniform(-diagonal_span / 2, diagonal_span / 2, size=n)
    matrix = (sparse.diags(row_scales, format="csc") @ matrix).tocsc()
    matrix.sort_indices()
    return matrix


def fixed_density_matrix(
    n: int,
    density: float,
    seed: int,
    diagonal_span: float,
    family: str = "lca-random",
    blocks: int = 8,
) -> sparse.csc_matrix:
    if not 0 < density < 1:
        raise ValueError("density must be between zero and one")
    rng = np.random.default_rng(seed)
    if family == "lca-random":
        off_diagonal = sparse.random(
            n,
            n,
            density=density,
            format="csc",
            random_state=rng,
            data_rvs=lambda size: rng.uniform(0.01, 0.04, size),
        )
    elif family == "io-block":
        if blocks < 1 or blocks > n:
            raise ValueError("blocks must be between 1 and n")
        block_sizes = np.full(blocks, n // blocks, dtype=int)
        block_sizes[: n % blocks] += 1
        local_density = min(1.0, density * 0.8 * blocks)
        local = sparse.block_diag(
            [
                sparse.random(
                    size,
                    size,
                    density=local_density,
                    format="csc",
                    random_state=rng,
                    data_rvs=lambda count: rng.uniform(0.001, 0.02, count),
                )
                for size in block_sizes
            ],
            format="csc",
        )
        cross = sparse.random(
            n,
            n,
            density=density * 0.2,
            format="csc",
            random_state=rng,
            data_rvs=lambda size: rng.uniform(0.0001, 0.005, size),
        )
        off_diagonal = local + cross
    elif family == "banded":
        half_bandwidth = max(1, min(n - 1, round(density * n / 2)))
        return banded_matrix(n, half_bandwidth, seed, diagonal_span)
    else:
        raise ValueError(f"Unknown matrix family: {family}")
    off_diagonal.setdiag(0.0)
    off_diagonal.eliminate_zeros()

    # Normalize columns so the increasing density does not make A singular.
    column_sums = np.asarray(off_diagonal.sum(axis=0)).ravel()
    scale = np.ones(n)
    nonzero = column_sums > 0
    scale[nonzero] = np.minimum(1.0, 0.4 / column_sums[nonzero])
    off_diagonal = off_diagonal @ sparse.diags(scale, format="csc")
    matrix = sparse.eye(n, format="csc") - off_diagonal
    row_scales = 10 ** rng.uniform(-diagonal_span / 2, diagonal_span / 2, size=n)
    matrix = sparse.diags(row_scales, format="csc") @ matrix
    matrix.sum_duplicates()
    matrix.sort_indices()
    return matrix


def matrix_fingerprint(matrix: sparse.csc_matrix) -> str:
    digest = hashlib.blake2b(digest_size=12)
    for array in (matrix.indptr, matrix.indices, matrix.data):
        digest.update(np.ascontiguousarray(array).view(np.uint8))
    return digest.hexdigest()


def solve(
    matrix: sparse.csc_matrix,
    demand: np.ndarray,
    solver: str,
    rtol: float,
    restart: int,
    maxiter: int,
    x0: np.ndarray | None = None,
) -> tuple[np.ndarray, int | None, int]:
    if solver == "numpy-dense":
        return np.linalg.solve(matrix.toarray(), demand), None, 0
    if solver == "superlu":
        return spsolve(matrix, demand, use_umfpack=False), None, 0
    if solver == "umfpack":
        import scikits.umfpack  # noqa: F401

        return spsolve(matrix, demand, use_umfpack=True), None, 0
    if solver == "pardiso":
        from pypardiso import spsolve as pardiso_spsolve

        return pardiso_spsolve(matrix, demand), None, 0

    residual_history: list[float] = []
    preconditioner = None
    if solver == "jacobi-gmres":
        diagonal = matrix.diagonal()
        if np.any(diagonal == 0):
            raise ValueError("Jacobi requires a non-zero matrix diagonal")
        inverse_diagonal = 1.0 / diagonal
        preconditioner = LinearOperator(
            matrix.shape,
            matvec=lambda vector: inverse_diagonal * vector,
            dtype=matrix.dtype,
        )
    elif solver != "gmres":
        raise ValueError(f"Unknown solver: {solver}")

    solution, info = gmres(
        matrix,
        demand,
        x0=x0,
        M=preconditioner,
        rtol=rtol,
        atol=0.0,
        restart=restart,
        maxiter=maxiter,
        callback=residual_history.append,
        callback_type="pr_norm",
    )
    return solution, int(info), len(residual_history)


def solve_many(
    matrix: sparse.csc_matrix,
    demands: list[np.ndarray],
    solver: str,
    rtol: float,
    restart: int,
    maxiter: int,
) -> tuple[list[np.ndarray], int | None, list[int], float, float, float | None]:
    """Solve multiple right-hand sides and separate setup from repeated solves."""
    factorization_seconds = 0.0
    fill_ratio = None
    info: int | None = None
    iterations: list[int] = []

    if solver == "numpy-dense":
        dense = matrix.toarray()
        started = time.perf_counter()
        solutions = [np.linalg.solve(dense, demand) for demand in demands]
        return (
            solutions,
            None,
            [0] * len(demands),
            0.0,
            time.perf_counter() - started,
            None,
        )

    if solver == "superlu":
        started = time.perf_counter()
        factor = splu(matrix)
        factorization_seconds = time.perf_counter() - started
        fill_ratio = float((factor.L.nnz + factor.U.nnz) / matrix.nnz)
        started = time.perf_counter()
        solutions = [factor.solve(demand) for demand in demands]
        rhs_seconds = time.perf_counter() - started
        return (
            solutions,
            None,
            [0] * len(demands),
            factorization_seconds,
            rhs_seconds,
            fill_ratio,
        )

    if solver == "umfpack":
        import scikits.umfpack as umfpack

        context = umfpack.UmfpackContext()
        started = time.perf_counter()
        lower, upper, *_ = context.lu(matrix)
        factorization_seconds = time.perf_counter() - started
        fill_ratio = float((lower.nnz + upper.nnz) / matrix.nnz)
        started = time.perf_counter()
        solutions = [
            context.solve(umfpack.UMFPACK_A, matrix, demand) for demand in demands
        ]
        rhs_seconds = time.perf_counter() - started
        return (
            solutions,
            None,
            [0] * len(demands),
            factorization_seconds,
            rhs_seconds,
            fill_ratio,
        )

    if solver == "pardiso":
        from pypardiso import spsolve as pardiso_spsolve

        started = time.perf_counter()
        solutions = [pardiso_spsolve(matrix, demand) for demand in demands]
        rhs_seconds = time.perf_counter() - started
        return solutions, None, [0] * len(demands), 0.0, rhs_seconds, None

    solutions = []
    started = time.perf_counter()
    for demand in demands:
        solution, current_info, current_iterations = solve(
            matrix, demand, solver, rtol, restart, maxiter
        )
        solutions.append(solution)
        iterations.append(current_iterations)
        if current_info not in (None, 0):
            info = current_info
    return solutions, info or 0, iterations, 0.0, time.perf_counter() - started, None


def package_version(name: str) -> str | None:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return None


def run(args: argparse.Namespace) -> dict[str, object]:
    with MemoryMonitor() as generation_memory:
        started = time.perf_counter()
        if args.topology == "constant-degree":
            matrix = constant_degree_matrix(
                args.size, args.degree, args.seed, args.diagonal_span
            )
        elif args.topology == "banded":
            matrix = banded_matrix(
                args.size, args.degree, args.seed, args.diagonal_span
            )
        else:
            matrix = fixed_density_matrix(
                args.size,
                args.density,
                args.seed,
                args.diagonal_span,
                family=args.matrix_family,
                blocks=args.blocks,
            )
        generation_seconds = time.perf_counter() - started

    demands = []
    for index in range(args.rhs_count):
        demand = np.zeros(args.size)
        demand[index % args.size] = 1.0
        demands.append(demand)
    matrix_bytes = matrix.data.nbytes + matrix.indices.nbytes + matrix.indptr.nbytes

    with MemoryMonitor() as memory:
        started = time.perf_counter()
        (
            solutions,
            info,
            iterations,
            factorization_seconds,
            rhs_solve_seconds,
            fill_ratio,
        ) = solve_many(
            matrix,
            demands,
            args.solver,
            args.rtol,
            args.restart,
            args.maxiter,
        )
        solve_seconds = time.perf_counter() - started

    residuals = [
        float(np.linalg.norm(matrix @ solution - demand) / np.linalg.norm(demand))
        for solution, demand in zip(solutions, demands)
    ]
    relative_residual = max(residuals)
    converged = info in (None, 0) and relative_residual <= max(args.rtol * 1.01, 1e-12)

    return {
        "kind": "synthetic",
        "topology": args.topology,
        "matrix_family": "banded" if args.topology == "banded" else args.matrix_family,
        "blocks": args.blocks if args.matrix_family == "io-block" else None,
        "solver": args.solver,
        "size": args.size,
        "shape": [args.size, args.size],
        "degree": (
            args.degree if args.topology in {"constant-degree", "banded"} else None
        ),
        "target_density": args.density if args.topology == "fixed-density" else None,
        "diagonal_span_orders": args.diagonal_span,
        "nnz": int(matrix.nnz),
        "density": float(matrix.nnz / (args.size * args.size)),
        "matrix_storage_bytes": int(matrix_bytes),
        "matrix_fingerprint": matrix_fingerprint(matrix),
        "seed": args.seed,
        "rtol": args.rtol,
        "restart": args.restart,
        "maxiter": args.maxiter,
        "generation_seconds": generation_seconds,
        "generation_incremental_peak_rss_bytes": generation_memory.incremental_peak_bytes,
        "solve_seconds": solve_seconds,
        "factorization_seconds": factorization_seconds,
        "rhs_solve_seconds": rhs_solve_seconds,
        "rhs_count": args.rhs_count,
        "seconds_per_rhs": rhs_solve_seconds / args.rhs_count,
        "lu_fill_ratio": fill_ratio,
        "baseline_rss_bytes": memory.baseline_bytes,
        "peak_rss_bytes": memory.peak_bytes,
        "incremental_peak_rss_bytes": memory.incremental_peak_bytes,
        "iterations": max(iterations, default=0),
        "iterations_per_rhs": iterations,
        "solver_info": info,
        "relative_residual": relative_residual,
        "converged": converged,
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "processor": platform.processor(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "scikit_umfpack": package_version("scikit-umfpack"),
            "pypardiso": package_version("pypardiso"),
            "psutil": package_version("psutil"),
            "physical_memory_bytes": psutil.virtual_memory().total,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--solver",
        choices=(
            "numpy-dense",
            "superlu",
            "umfpack",
            "pardiso",
            "gmres",
            "jacobi-gmres",
        ),
        required=True,
    )
    parser.add_argument(
        "--topology",
        choices=("constant-degree", "fixed-density", "banded"),
        default="constant-degree",
    )
    parser.add_argument("--size", type=int, required=True)
    parser.add_argument("--degree", type=int, default=8)
    parser.add_argument("--density", type=float, default=0.001)
    parser.add_argument(
        "--matrix-family",
        choices=("lca-random", "io-block", "banded"),
        default="lca-random",
    )
    parser.add_argument("--blocks", type=int, default=8)
    parser.add_argument("--rhs-count", type=int, default=1)
    parser.add_argument("--diagonal-span", type=float, default=4.0)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--rtol", type=float, default=1e-4)
    parser.add_argument("--restart", type=int, default=50)
    parser.add_argument("--maxiter", type=int, default=300)
    args = parser.parse_args()
    print(json.dumps(run(args), sort_keys=True))


if __name__ == "__main__":
    main()
