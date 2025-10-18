# Problem Validation Tests

This directory contains scripts for validating the structure and content of a problem.

## Main Validator

-   **Script:** `problem_statement_validator.py`
-   **Description:** This is the main validator for problems. It orchestrates the validation process by calling the other specialized test scripts in this directory.
-   **Usage:**
    ```bash
    python -m scripts.tests.problem.problem_statement_validator --problem_id <problem_id>
    ```

## Specialized Tests

### Metadata Test

-   **Script:** `test_meta.py`
-   **Description:** This script validates the `meta.json` file for a problem. It checks for the presence of required fields, correct data types, and valid values.
-   **Usage:**
    ```bash
    python -m scripts.tests.problem.test_meta --problem_id <problem_id>
    ```

### Markdown Content Tests

-   **Scripts:** `test_description_md.py`, `test_input_md.py`, `test_output_md.py`, `test_constraints_md.py`, `test_notes_md.py`
-   **Description:** These scripts validate the different sections of the `problem.md` file, checking that they are not empty.
-   **Usage:**
    ```bash
    python -m scripts.tests.problem.test_description_md --problem_id <problem_id>
    ```

### Test Cases Test

-   **Script:** `test_testcases.py`
-   **Description:** This script validates the `testcases` directory for a problem. It checks that for each `.in` file, there is a corresponding `.out` file.
-   **Usage:**
    ```bash
    python -m scripts.tests.problem.test_testcases --problem_id <problem_id>
    ```

### Other Tests

This directory also contains other specialized tests, such as:
-   `test_pdf_statement_presence.py`: Checks for the presence of a PDF statement if specified in the metadata.
-   `test_problem_submissions_structure.py`: Validates the structure of the submissions for a problem.
-   `test_problem_tex.py`: Validates the TeX file for the problem statement.
