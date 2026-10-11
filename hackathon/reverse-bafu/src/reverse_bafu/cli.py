"""reverse-bafu: dis-aggregate BAFU-2026 system processes into unit processes.

  one spec:      resolve | calibrate | build | check | run  <spec.json>
  every spec:    run-all
  make specs:    draft-all, or per dataset locate | evidence | draft | assemble  <code>
  benchmark:     benchmark --mode calibration|extraction
"""

from __future__ import annotations

import argparse
import sys
import warnings
from pathlib import Path

from . import db, spec as spec_mod


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="reverse-bafu", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("command", choices=["resolve", "calibrate", "build", "check", "run", "benchmark", "evidence", "draft", "assemble", "locate", "draft-all", "run-all"])
    p.add_argument("spec", nargs="?", help="spec JSON (see src/reverse_bafu/spec.py); for evidence/draft/assemble: the target code")
    p.add_argument("--report", help="evidence: the report PDF")
    p.add_argument("--pages", help="evidence: page range in the PDF, e.g. 16-17")
    p.add_argument("--ecospold", default="data/ecospold", help="evidence: unzipped BAFU XML folder")
    p.add_argument("--dry-run", action="store_true", help="draft: write the prompts, call no model")
    p.add_argument("--from-response", action="append", default=[], metavar="STEP=FILE",
                   help="draft/locate: ingest a response obtained elsewhere; STEP is locate, extract or map; add by=<who> to record the author")
    p.add_argument("--reports", default="BAFU-2026 v1_Documentation/BAFU-2026 v1_Documentation/BAFU-2026 v1 LCI Reports",
                   help="locate/draft-all: folder with the report PDFs")
    p.add_argument("--only", default="", help="draft-all: comma-separated dataset codes (or 8-char prefixes) to process")
    p.add_argument("--datasets", default="results/system_terminated_extended.csv",
                   help="draft-all: the CSV of system processes to work through (default: all 138, see scripts/find_system_processes.py)")
    p.add_argument("--by", default="", help="draft-all: author label for responses answered outside the API")
    p.add_argument("--no-fallback", action="store_true",
                   help="draft-all: stop at pages-not-found / no-pdf instead of trying the template and metadata routes")
    p.add_argument("--n", type=int, default=30, help="benchmark: number of synthetic cases")
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--scenarios", default="oracle,bounded,partial,distractors,blind")
    p.add_argument("--shard", default=None, help="benchmark: i/k runs every k-th case from i (merge with benchmark.merge_shards)")
    p.add_argument("--name", default=None, help="benchmark: output name (default n<N>-seed<S>)")
    p.add_argument("--mode", choices=["calibration", "extraction"], default="calibration",
                   help="benchmark: calibration (amounts from a given list) or extraction (the whole route incl. the PDF)")
    p.add_argument("--project", default="bafu-2026")
    p.add_argument("--apply", action="store_true", help="calibrate / run / run-all: write fitted amounts back into the spec")
    p.add_argument("--no-hybrid", action="store_true", help="build: skip the residual (hybrid) node")
    args = p.parse_args(argv)

    warnings.filterwarnings("ignore", message=".*pypardiso.*")
    db.set_project(args.project)
    if args.command == "benchmark":
        from . import benchmark
        if args.mode == "extraction":
            only = {x.strip() for x in args.only.split(",") if x.strip()} or None
            benchmark.run_extraction(args.n, args.seed, args.name or f"n{args.n}-seed{args.seed}", args.project, Path(args.ecospold),
                                     Path(args.reports), args.dry_run, args.by or "manual", only)
        else:
            shard = tuple(map(int, args.shard.split("/"))) if args.shard else None
            unknown = set(args.scenarios.split(",")) - set(benchmark.SCENARIOS)
            if unknown:
                p.error(f"unknown scenario(s) {', '.join(sorted(unknown))}; choose from {', '.join(benchmark.SCENARIOS)}")
            benchmark.run(args.n, args.seed, args.scenarios.split(","), args.name or f"n{args.n}-seed{args.seed}", shard=shard)
        return 0
    if args.command == "run-all":
        from . import runall
        runall.run_all(args.project, args.apply)
        return 0
    if args.command == "draft-all":
        from . import draft as draft_mod
        only = {x.strip() for x in args.only.split(",") if x.strip()} or None
        draft_mod.draft_all(args.project, Path(args.ecospold), Path(args.reports), args.dry_run, only, args.by or "manual",
                            datasets=Path(args.datasets), fallbacks=not args.no_fallback)
        return 0
    if args.command in ("evidence", "draft", "assemble", "locate"):
        from . import draft as draft_mod
        if not args.spec:
            p.error("the target code is required")
        if args.command == "locate":
            if not args.report:
                p.error("locate needs --report")
            fr = dict(kv.split("=", 1) for kv in args.from_response)
            r = draft_mod.locate(args.spec, Path(args.report), Path(args.ecospold), args.dry_run,
                                 Path(fr["locate"]) if "locate" in fr else None, fr.get("by", "manual"))
            print(r if r else "prompt written (dry run)")
        elif args.command == "evidence":
            if not (args.report and args.pages):
                p.error("evidence needs --report and --pages")
            draft_mod.evidence(args.spec, Path(args.report), args.pages, Path(args.ecospold), args.project)
        elif args.command == "draft":
            fr = dict(kv.split("=", 1) for kv in args.from_response)
            fr = {k: (Path(v) if k != "by" else v) for k, v in fr.items()}
            draft_mod.draft(args.spec, args.dry_run, fr or None, args.project)
        else:
            draft_mod.assemble(args.spec, args.project)
        return 0
    if not args.spec:
        p.error("spec is required")
    spec = spec_mod.load(args.spec)
    print(f"== {args.command}: {spec.target_name} ({spec.target_code}) ==", file=sys.stderr)

    if args.command in ("resolve", "run"):
        from . import resolve
        if not resolve.run(spec):
            return 2
        spec_mod.save(spec)
    if args.command in ("calibrate", "run"):
        from . import calibrate
        calibrate.run(spec, apply=args.apply)
    if args.command in ("build", "run"):
        from . import build
        if args.command == "build":
            spec = spec_mod.load(args.spec)  # pick up codes written by resolve
        build.run(spec, hybrid=not args.no_hybrid)
    if args.command in ("check", "run"):
        from . import check
        check.run(spec_mod.load(args.spec))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
