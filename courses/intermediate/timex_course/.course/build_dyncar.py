"""Split the dynamic-characterization notebook into a student and a solved version.

    .course/sources/3_dynamic_characterization.ipynb     - the authored master, edit this one
    3_dynamic_characterization.ipynb                                          - what the students open
    solutions/3_dynamic_characterization/3_dynamic_characterization_SOLVED.ipynb  - filled in

The master marks its exercises the way it always has: an empty (or skeleton) code cell for
the student, followed by a cell starting with `#SOLUTION`. Here the two are separated - the
solved notebook keeps the solution, the student notebook keeps the placeholder plus a
`# %load solutions/...` escape hatch, exactly like the sommerhus notebooks.

Verify with `./scripts/check_all.sh`.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from nbtools import code, for_solutions_dir, load, save, strip_outputs  # noqa: E402

HERE = Path(__file__).resolve().parent.parent
SOURCE = HERE / ".course" / "sources" / "3_dynamic_characterization.ipynb"
SOLUTIONS = HERE / "solutions" / "3_dynamic_characterization"

HATCH = (
    "# Stuck, or out of time? Uncomment the line below, run this cell twice,\n"
    "# and you're back in sync with everyone else.\n"
    "# %load {file}\n"
)

#: One entry per exercise, in the order they appear in the master. `todo` replaces an empty
#: placeholder cell; a skeleton placeholder (`FILL YOURSELF`) is kept as the author wrote it.
EXERCISES = [
    {
        "file": "1_characterize_inventory.py",
        "todo": "# TODO: characterize the dummy inventory above with `characterize()`.\n"
        "#       Map flow 1 to ar6.characterize_co2 and flow 3 to ar6.characterize_ch4,\n"
        "#       metric='radiative_forcing', time_horizon=4.\n",
    },
    {
        "file": "2_build_timexlca.py",
        "todo": "# TODO: build a TimexLCA for {('test', 'A'): 1} with the ('GWP', 'example') method,\n"
        "#       then build_timeline(starting_datetime=..., temporal_grouping='day'),\n"
        "#       lci() and static_lcia().\n",
    },
    {
        "file": "3_dynamic_inventory.py",
        "todo": "# TODO: show the dynamic inventory dataframe of your TimexLCA.\n",
    },
    {
        "file": "4_characterize_ghgs.py",
        "todo": "# TODO: map the three biosphere flows (CH4, CO2, N2O - look them up by code) to the\n"
        "#       matching ar6 functions, then characterize the dynamic inventory over 100 years.\n",
    },
    {
        "file": "5_dynamic_lcia.py",
        "todo": "# TODO: the same thing again, but through tlca.dynamic_lcia() instead of\n"
        "#       characterize() - same arguments.\n",
    },
    {
        "file": "6_water_characterization_function.py",
        "todo": None,  # the author's skeleton is the placeholder
    },
    {
        "file": "7_apply_water_function.py",
        "todo": "# TODO: apply your function. You need a dynamic inventory dataframe (100 m3 in\n"
        "#       January, May and July), a {flow_id: function} mapping, and characterize().\n",
    },
]


def is_solution(cell):
    return cell["cell_type"] == "code" and "".join(cell["source"]).lstrip().lower().startswith(
        "#solution"
    )


def is_placeholder(cell):
    if cell["cell_type"] != "code":
        return False
    source = "".join(cell["source"])
    return not source.strip() or "FILL YOURSELF" in source


def strip_marker(cell):
    """The solution cell without its `#SOLUTION` marker line."""
    lines = "".join(cell["source"]).splitlines(keepends=True)
    while lines and lines[0].lstrip().lower().startswith("#solution"):
        lines = lines[1:]
    while lines and not lines[0].strip():
        lines = lines[1:]
    return "".join(lines)


def split(nb):
    """Return (solved_cells, student_cells) and write the solution files."""
    SOLUTIONS.mkdir(parents=True, exist_ok=True)
    cells = nb["cells"]
    solutions = [i for i, cell in enumerate(cells) if is_solution(cell)]
    assert len(solutions) == len(EXERCISES), (
        f"{len(solutions)} solution cells in the master, {len(EXERCISES)} described here"
    )

    # each solution belongs to the closest placeholder before it
    owner = {}
    for n, index in enumerate(solutions):
        candidates = [i for i in range(index) if is_placeholder(cells[i]) and i not in owner]
        assert candidates, f"no placeholder found for the solution in cell {index}"
        owner[candidates[-1]] = n

    solved, student = [], []
    pending_hatch = None  # the author's "**Hint:**" cells belong before the escape hatch
    for i, cell in enumerate(cells):
        text = "".join(cell["source"])
        if cell["cell_type"] == "markdown" and not text.strip():
            continue  # empty markdown cells in the master

        if pending_hatch and not (
            cell["cell_type"] == "markdown" and text.lstrip().startswith("**Hint")
        ):
            student.append(pending_hatch)
            pending_hatch = None

        if i in owner:  # a placeholder
            exercise = EXERCISES[owner[i]]
            student.append(code(exercise["todo"]) if exercise["todo"] else cell)
            pending_hatch = code(HATCH.format(file=f"solutions/3_dynamic_characterization/{exercise['file']}"))
            continue  # the solved notebook shows the solution instead

        if is_solution(cell):
            source = strip_marker(cell)
            name = EXERCISES[solutions.index(i)]["file"]
            (SOLUTIONS / name).write_text(source.rstrip() + "\n")
            print(f"wrote solutions/3_dynamic_characterization/{name}")
            solved.append(code(source))
            continue

        solved.append(cell)
        student.append(cell)

    if pending_hatch:
        student.append(pending_hatch)

    return solved, student


def notebook(nb, cells):
    out = dict(nb, cells=cells)
    strip_outputs(out)
    return out


master = load(SOURCE)
solved_cells, student_cells = split(master)

save(notebook(master, student_cells), HERE / "3_dynamic_characterization.ipynb")
print(f"wrote 3_dynamic_characterization.ipynb with {len(student_cells)} cells (student version)")

solved_cells = for_solutions_dir(solved_cells)
save(notebook(master, solved_cells), SOLUTIONS / "3_dynamic_characterization_SOLVED.ipynb")
print(f"wrote solutions/3_dynamic_characterization/3_dynamic_characterization_SOLVED.ipynb with {len(solved_cells)} cells")
