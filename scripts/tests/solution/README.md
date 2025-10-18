# Solution Validation Tests

This directory contains scripts for validating the official solution for a problem.

## Main Validator

-   **Script:** `solution_validator.py`
-   **Description:** This is the main validator for solutions. It orchestrates the validation process by calling the other specialized test scripts in this directory. It runs the solution code against the test cases and checks for correctness and time limits.
-   **Usage:**
    ```bash
    python -m scripts.tests.solution.solution_validator --problem_id <problem_id>
    ```

## Specialized Tests

### Solution Runners

-   **Scripts:** `run_c_solution.py`, `run_cpp_solution.py`, `run_py_solution.py`
-   **Description:** These scripts are responsible for compiling (if necessary) and running the solution code in C, C++, and Python, respectively. They are called by the `solution_validator.py`.

### Solution Files Presence Test

-   **Script:** `test_solution_files_presence.py`
-   **Description:** This script checks for the presence of the solution files (e.g., `solution.py`, `solution.cpp`, `solution.c`, `solution.md`).
-   **Usage:**
    ```bash
    python -m scripts.tests.solution.test_solution_files_presence --problem_id <problem_id>
    ```

### Other Tests

This directory also contains other specialized tests, such as:
-   `test_pdf_solution_presence.py`: Checks for the presence of a PDF solution if specified in the metadata.
-   `test_solution_md.py`: Validates the `solution.md` file.
-   `test_solution_tex.py`: Validates the TeX file for the solution.
