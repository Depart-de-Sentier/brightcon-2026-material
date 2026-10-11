---
description: Run the extraction benchmark (the whole reverse-bafu route on unit processes with a known answer) with this Claude Code session as the model
argument-hint: --n <cases> [--seed <s>] [--name <run>] [--project <name>]
---

Run `reverse-bafu benchmark --mode extraction` with this session answering the prompts. `$ARGUMENTS` carries `--n`, `--seed`, `--name`, `--project`; pass them through unchanged. The cases are BAFU *unit processes* with a known answer: never look up their exchanges, their names in `data/ecospold`, or Brightway while answering — the answers must come from the report excerpts alone, exactly as for a real system process.

1. `uv run reverse-bafu benchmark --mode extraction --dry-run --by "claude-code:<the model you are running as>" $ARGUMENTS`. It writes `results/benchmark/extraction-<name>.csv`; each row's `status` says how far that case got. Prompts and responses live under `results/benchmark/extraction/evidence/<code>/`.
2. For every row with status `prompt-0-written`: read `prompt-0-locate.md` in full and answer it (one JSON object per `schema-0-locate.json`); write `response-0-locate.json`.
3. For every row with status `prompt-1-written`: read `prompt-1-extract.md`, answer per its rules (verbatim quotes, raw values, no inputs the excerpt does not mention); write `response-1-extract.json`.
4. For every row with status `prompt-2-written`: read `prompt-2-map.md`; every `chosen` is one of the listed candidates or null with a reason; write `response-2-map.json`.
5. Rerun step 1 (rejected responses are named with the failing path — fix and rerun). Repeat until every row is `scored`, `pages-not-found`, `unresolved` or `error`.
6. Report the summary line of `results/benchmark/extraction-<name>.md` and, per scored case, inputs matched / missed / extra and the amounts within ±20 %.
