#!/usr/bin/env bash
# Rebuild the generated notebooks and run them end to end. Run this before teaching.
set -euo pipefail
cd "$(dirname "$0")/.."
export MPLBACKEND=Agg
PY=.venv/bin/python

$PY .course/build_sommerhus.py
$PY .course/build_dyncar.py

$PY .course/run_notebook.py solutions/2_sommerhus/2_sommerhus_SOLVED.ipynb
# a student who solved nothing: must still run to the end, checkpoint reporting what's missing
$PY .course/run_notebook.py 2_sommerhus.ipynb
# and one who used the escape hatch
$PY .course/run_notebook.py 2_sommerhus.ipynb --as-student

$PY .course/run_notebook.py solutions/3_dynamic_characterization/3_dynamic_characterization_SOLVED.ipynb
# notebook 3's later cells build on the exercise results, so the blank version cannot run
# end to end by design - only the escape-hatch path is checked
$PY .course/run_notebook.py 3_dynamic_characterization.ipynb --as-student

$PY .course/run_notebook.py solutions/4_sommerhus_dynamic/4_sommerhus_dynamic_SOLVED.ipynb
$PY .course/run_notebook.py 4_sommerhus_dynamic.ipynb
$PY .course/run_notebook.py 4_sommerhus_dynamic.ipynb --as-student

echo
echo "ALL NOTEBOOKS OK"
