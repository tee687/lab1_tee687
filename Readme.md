# Lab 1: Grade Evaluator & Archiver

## Files Included

| File | Description |
|:--- |:--- |
| `grade-evaluator.py` | Python script for grade calculation. |
| `organizer.sh` | Bash script for file management and archiving. |
| `grades.csv` | Data source file. |

---

## How to Run

1. **Python Application**: Run `python3 grade-evaluator.py` to see the final grade and GPA.
2. **Shell Script**: Run `bash organizer.sh` to archive the current grades and reset the workspace.

---

## What the Python Script Does
- Checks that all scores are between 0 and 100.
- Calculates the final grade and GPA.
- Shows a **PASS** only if the student gets 50% or more in both homework and tests.

## What the Shell Script Does
1. Creates a folder called `archive` if it is not there.
2. Moves the old `grades.csv` into the `archive` folder.
3. Makes a new, empty `grades.csv` file.
4. Writes a note in `organizer.log` to show it is done.
