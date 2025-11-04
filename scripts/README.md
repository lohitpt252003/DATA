# Problem Data Validation Scripts

This directory contains scripts for validating the problem data in this repository.

## Main Validator

The `main_validator.py` script is the primary script for validating problem or contest data. It orchestrates the validation process by calling specialized validators based on the provided ID.

### Usage

To run the main validator, execute the following command from the root of the `DATA` directory:

```bash
python -m scripts.main_validator --problem_id <problem_id>
# or
python -m scripts.main_validator --contest_id <contest_id>
```

**Examples:**

```bash
python -m scripts.main_validator --problem_id C0A
python -m scripts.main_validator --contest_id C1
```

-   If `--problem_id` is provided, it will run a complete suite of tests for the given `problem_id`, including problem statement, solution, and model validations.
-   If `--contest_id` is provided, it will run a complete suite of tests for the given `contest_id`, including contest structure validation.

**Error:** Please provide either `--problem_id` or `--contest_id`, not both.

## Specialized Validators

The validation logic is now split into several main components, located in the `scripts/tests/` directory.

### Problem Structure Validator

-   **Script:** `scripts/tests/test_problem_structure.py`
-   **Description:** This script runs all tests related to the problem's definition, including the `meta.json` (validating fields, data types, and values), `problem.md` (combining description, input/output, constraints, and notes), test cases, and overall data structure.
-   **Usage:**
    ```bash
    python -m scripts.tests.test_problem_structure --problem_id <problem_id>
    ```

### Solution Files Presence Validator

-   **Script:** `scripts/tests/test_solution_files_presence.py`
-   **Description:** This script runs all tests related to the problem's official solution. It checks for the presence of solution files and runs the solution code against the test cases to verify its correctness, including checking for time limits.
-   **Usage:**
    ```bash
    python -m scripts.tests.test_solution_files_presence --problem_id <problem_id>
    ```

### Model Validator

-   **Script:** `scripts/tests/test_model_files_presence.py`
-   **Description:** This script runs tests to ensure the presence and basic structure of the Python blueprint files in the `DATA/blueprint` directory.
-   **Usage:**
    ```bash
    python -m scripts.tests.test_model_files_presence
    ```

### Contest Structure Validator

-   **Script:** `scripts/tests/contest/contest_main_validator.py`
-   **Description:** This is the main validator for contests. It orchestrates the validation process by calling specialized validators for contest metadata, markdown files, and participants.json.
-   **Usage:**
    ```bash
    python -m scripts.tests.contest.contest_main_validator --contest_id <contest_id>
    ```

For more details on the individual test scripts that these validators run, please see the [README.md in the tests directory](./tests/README.md).

## Problem-Specific Validator (`validator.py`)

In addition to the validation scripts in this directory, each problem has its own `validator.py` script located in the problem's directory (e.g., `data/contests/C1/problems/A/validator.py`).

This script acts as a **custom judge** for the problem. Its role is to:

1.  Take a user's output file and the correct output file as command-line arguments.
2.  Compare the two files to determine if the user's output is correct.
3.  Handle cases where multiple correct answers are possible.
4.  Print a verdict, such as "Accepted" or "Wrong Answer".

This problem-specific validator is used by the judging system to grade submissions.

## Testcase Generators

For convenience when bootstrapping problems, a generic testcase generator is provided at `scripts/generators/generate_cp_cases.py`.

Usage (from the DATA root or repo root):

```bash
python -m scripts.generators.generate_cp_cases ../DATA/data/contests/<ContestId>/problems/<Letter>/testcases --seed 42 --cap 100000 --val-lo -1000000000 --val-hi 1000000000
```

It emits five `.in` files with common competitive programming shapes:
- 1–2: random packs with total `sum(n)` ≤ `--cap`
- 3: single large case (`n=1e5`) for TLE stress
- 4–5: curated edge/corner patterns (including negatives and zeros if the range spans them)

Problems can also include a bespoke generator script under their own `testcases/` directory if their input format differs from the default.
