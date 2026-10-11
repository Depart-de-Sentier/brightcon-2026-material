---
description: Draft specs for every BAFU-2026 system process in results/system_terminated_extended.csv, using this Claude Code session as the model for the drafting prompts
argument-hint: [--only <codes>] [--datasets <csv>] [--no-fallback] [--project <name>]
---

Run the reverse-bafu batch drafter over the 138 system processes in `results/system_terminated_extended.csv`, this session being the model. `$ARGUMENTS` may pass `--only <comma-separated codes or 8-char prefixes>`, `--datasets <csv>`, `--no-fallback` and `--project <name>`; pass them through unchanged. Loop until nothing is pending; never edit amounts, add inputs or read the interactive specs (`specs/*.json` without `.draft`) — those are the reviewer's decisions.

1. `uv run reverse-bafu draft-all --dry-run --by "claude-code:<the model you are running as>" $ARGUMENTS`. It writes `results/drafting_status.csv`; each row's `status` says how far that dataset got.
2. For every row whose status is `prompt-0-written`: read `specs/evidence/<code>/prompt-0-locate.md` in full and answer it with one JSON object satisfying `schema-0-locate.json` (the page range of the inventory table, or `found: false` with the reason); write it to `response-0-locate.json` with the Write tool.
3. For every row whose status is `prompt-1-written`: read `prompt-1-extract.md` and answer per its eight rules (verbatim quotes, raw values, no inputs the excerpt does not mention — those go into `gaps`); write `response-1-extract.json`.
4. For every row whose status is `prompt-2-written`: read `prompt-2-map.md`; every `chosen` must be one of the listed candidates or null with a reason; write `response-2-map.json`.
5. Rows whose report prints no inventory continue on the template and metadata routes:
   - `prompt-3-written`: read `prompt-3-template.md`; choose a candidate only if it makes the same product (else `chosen_code` null), copy input names exactly into `free_inputs`; write `response-3-template.json`.
   - `prompt-4-written`: read `prompt-4-metadata.md` and answer per its six rules (quote the phrase that names each input; one amount basis per item; for `stoichiometry` write the balanced equation with IUPAC atomic weights and the arithmetic; no solvents, catalysts or yields the metadata does not state; no items at all for a multi-output process without allocation); write `response-4-metadata.json`.
   - `prompt-5-written`: read `prompt-5-map.md` and answer it like step 4; write `response-5-map.json`.
6. Rerun step 1. Ingested responses are validated; fix and rerun any the command rejects. Repeat 1–6 until every row is `drafted`, `no-usable-evidence` or `error`.
7. Report the final status counts, and for each `drafted` dataset its `route`, the spec path and the model's `gaps`. Then run `uv run reverse-bafu run specs/<code>-<slug>.draft.json` (add the `--project` from `$ARGUMENTS`, if one was given) for each drafted spec and report the check summaries. Do not run `--apply`.
