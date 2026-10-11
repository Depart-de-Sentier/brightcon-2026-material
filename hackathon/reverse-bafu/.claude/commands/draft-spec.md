---
description: Draft a reverse-bafu spec for a BAFU-2026 system process from a report excerpt, with the fixed prompts, using this Claude Code session as the model
argument-hint: <target code> --report "<pdf>" --pages <a-b>
---

Draft a spec for the system process given in `$ARGUMENTS` (a BAFU-2026 dataset code, the report PDF and the PDF page range), running this session as the model. Follow these steps exactly; do not skip the validation and do not improvise beyond the prompts.

1. `uv run reverse-bafu evidence <code> --report "<pdf>" --pages <a-b>` (add `--project <name>` if the Brightway project is not `bafu-2026`). If it fails because the pages do not contain the dataset's inventory table, find the right PDF pages (they differ from the printed page numbers) and rerun.
2. `uv run reverse-bafu draft <code> --dry-run`. This writes `specs/evidence/<code>/prompt-1-extract.md` and `schema-1-extract.json`.
3. Read `prompt-1-extract.md` in full and answer it: produce exactly one JSON object that satisfies `schema-1-extract.json`, obeying the prompt's eight rules (verbatim quotes from the excerpt, raw values and units as printed, no conversions beyond a stated factor with its source, no inputs the excerpt does not mention — those go into `gaps`, uncertain items flagged not omitted). Write it to `specs/evidence/<code>/response-1-extract.json` with the Write tool. Do not read the interactive specs or other evidence folders first; the answer must come from the excerpt alone.
4. `uv run reverse-bafu draft <code> --from-response extract=specs/evidence/<code>/response-1-extract.json --from-response "by=claude-code:<model you are running as>"`. This validates the response against the schema (fix and rerun if it is rejected) and writes `prompt-2-map.md`, `schema-2-map.json` and the deterministic candidate lists.
5. Read `prompt-2-map.md` in full and answer it: one JSON object satisfying `schema-2-map.json`; every `chosen` value must be one of the listed candidates or null with a reason. Write it to `specs/evidence/<code>/response-2-map.json`.
6. `uv run reverse-bafu draft <code> --from-response extract=… --from-response map=specs/evidence/<code>/response-2-map.json --from-response "by=claude-code:<model>"`. This validates, assembles `specs/<code>-<slug>.draft.json` and prints what was skipped and the gaps.
7. `uv run reverse-bafu run specs/<code>-<slug>.draft.json` and report: the resolve table, the check summary, the gaps, and every entry with `confidence` = low. Do not edit amounts or add inputs yourself; those decisions belong to the reviewer, who records them in the spec with `reviewed_by`.

Report at the end: which model this session ran as, the files written, and the check summary.
