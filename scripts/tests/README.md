# Specialized Validation Scripts

This directory contains specialized Python scripts for validating different aspects of the problem and contest data. These scripts are typically called by `main_validator.py` but can also be run individually for specific testing.

## Usage

To run any of these scripts, execute them from the root of the `DATA` directory using `python -m <module_path>`.

### Problem Structure Validator

-   **Script:** `test_problem_structure.py`
-   **Description:** Validates the overall structure and content of a problem, including `meta.json`, markdown files, and test cases.
-   **Usage:**
    ```bash
    python -m scripts.tests.problem.problem_statement_validator --problem_id <problem_id>
    ```

### Solution Files Presence Validator

-   **Script:** `test_solution_files_presence.py`
-   **Description:** Checks for the existence of expected solution files (e.g., `.py`, `.cpp`, `.c`, `.md`) for a given problem.
-   **Usage:**
    ```bash
    python -m scripts.tests.solution.solution_validator --problem_id <problem_id>
    ```

### Model Files Presence Validator

-   **Script:** `test_model_files_presence.py`
-   **Description:** Ensures that the necessary Python model files are present in the `DATA/models` directory.
-   **Usage:**
    ```bash
    python -m scripts.tests.model.model_validator
    ```

### Contest Main Validator

-   **Script:** `contest/contest_main_validator.py`
-   **Description:** This is the main validator for contests. It orchestrates the validation process by calling specialized validators for contest metadata, markdown files, and participants.json.
-   **Usage:**
    ```bash
    python -m scripts.tests.contest.contest_main_validator --contest_id <contest_id>
    ```

### Contest Meta Validator

-   **Script:** `contest/test_contest_meta.py`
-   **Description:** Validates the `meta.json` file of a contest, checking for required fields, data types, and logical consistency (e.g., `startTime` before `endTime`).
-   **Usage:**
    ```bash
    python -m scripts.tests.contest.test_contest_meta --contest_id <contest_id>
    ```

### Contest Markdown Files Validator

-   **Script:** `contest/test_contest_markdown_files.py`
-   **Description:** Validates the presence and non-emptiness of `contest.md` and `theory.md` files for a contest.
-   **Usage:**
    ```bash
    python -m scripts.tests.contest.test_contest_markdown_files --contest_id <contest_id>
    ```

### Contest Participants Validator

-   **Script:** `contest/test_contest_participants.py`
-   **Description:** Validates the `participants.json` file of a contest, ensuring it is a valid JSON file.
-   **Usage:**
    ```bash
    python -m scripts.tests.contest.test_contest_participants --contest_id <contest_id>
    ```