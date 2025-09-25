# Individual Test Scripts

This directory contains the individual test scripts that are orchestrated by the validators in the parent directory. The tests are now organized into two subdirectories: `problem` and `solution`.

**Important:** All commands must be run from the root of the `DATA` directory.

## Problem Statement Tests (`problem/`)

These scripts validate the structure and content of the problem statement files.

-   `test_meta.py`: Validates `meta.json`.
-   `test_description_md.py`: Validates `description.md`.
-   `test_input_md.py`: Validates `input.md`.
-   `test_output_md.py`: Validates `output.md`.
-   `test_constraints_md.py`: Validates `constraints.md`.
-   `test_notes_md.py`: Validates `notes.md`.
-   `test_header_md.py`: Validates `header.md`.
-   `test_testcases.py`: Validates the `testcases` directory.
-   `test_index.py`: Validates the main `index.json` file.
-   `test_problem_submissions_structure.py`: Validates the submission structure within a problem.
-   `test_user_structure.py`: Validates the overall user data structure.
-   `test_pdf_statement_presence.py`: Checks for `statement.pdf` if `has_pdf_statement` is true in `meta.json`.
-   `test_problem_tex.py`: Checks for the presence and correct section structure of `problem.tex`.

### Usage Example

To run an individual problem test (e.g., `test_meta.py`):

```bash
python -m scripts.tests.problem.test_meta P1
```

## Solution Tests (`solution/`)

These scripts validate and run the official solutions for a problem.

-   `test_solution_md.py`: Validates `solution.md`.
-   `test_solution_files_presence.py`: Checks for the existence of solution code files.
-   `run_py_solution.py`: Runs the Python solution against test cases.
-   `run_c_solution.py`: Compiles and runs the C solution against test cases.
-   `run_cpp_solution.py`: Compiles and runs the C++ solution against test cases.
-   `test_pdf_solution_presence.py`: Checks for `solution.pdf` if `has_pdf_solution` is true in `meta.json`.
-   `test_solution_tex.py`: Checks for the presence and correct section structure of `solution.tex`.

### Usage Example

To run an individual solution test (e.g., `run_py_solution.py`):

```bash
python -m scripts.tests.solution.run_py_solution P1
```
