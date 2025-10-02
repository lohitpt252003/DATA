# Problem Data Validation Scripts

This directory contains scripts for validating the problem data in this repository.

## Main Validator

The `main_validator.py` script is the primary script for validating a problem. It orchestrates the validation process by calling three specialized validators: the `problem_statement_validator.py`, the `solution_validator.py`, and the `model_validator.py`.

### Usage

To run the main validator, execute the following command from the root of the `DATA` directory:

```bash
python -m scripts.main_validator <problem_id>
```

**Example:**

```bash
python -m scripts.main_validator P1
```

This will run a complete suite of tests for the given `problem_id`, first validating the problem statement and then the solution.

## Specialized Validators

The validation logic is now split into two main components, located in the `scripts/tests/` directory.

### Problem Statement Validator

-   **Script:** `scripts/tests/problem/problem_statement_validator.py`
-   **Description:** This script runs all tests related to the problem's definition, including the `meta.json` (validating fields, data types, and values), markdown files (`description.md`, `input.md`, etc.), test cases, and overall data structure.
-   **Usage:**
    ```bash
    python -m scripts.tests.problem.problem_statement_validator <problem_id>
    ```

### Solution Validator

-   **Script:** `scripts/tests/solution/solution_validator.py`
-   **Description:** This script runs all tests related to the problem's official solution. It checks for the presence of solution files and runs the solution code against the test cases to verify its correctness, including checking for time limits.
-   **Usage:**
    ```bash
    python -m scripts.tests.solution.solution_validator <problem_id>
    ```

### Model Validator

-   **Script:** `scripts/tests/model/model_validator.py`
-   **Description:** This script runs tests to ensure the presence and basic structure of the Python model files in the `DATA/models` directory.
-   **Usage:**
    ```bash
    python -m scripts.tests.model.model_validator
    ```

For more details on the individual test scripts that these validators run, please see the [README.md in the tests directory](./tests/README.md).