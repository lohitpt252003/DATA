# Contest Validation Tests

This directory contains scripts for validating the structure and content of a contest.

## Main Validator

-   **Script:** `contest_main_validator.py`
-   **Description:** This is the main validator for contests. It orchestrates the validation process by calling the other specialized test scripts in this directory.
-   **Usage:**
    ```bash
    python -m scripts.tests.contest.contest_main_validator --contest_id <contest_id>
    ```

## Specialized Tests

### Markdown Files Test

-   **Script:** `test_contest_markdown_files.py`
-   **Description:** This script validates the presence and content of the markdown files for a contest, including `contest.md`, `rules.md`, and `theory.md`. It checks that the files are not empty.
-   **Usage:**
    ```bash
    python -m scripts.tests.contest.test_contest_markdown_files --contest_id <contest_id>
    ```

### Metadata Test

-   **Script:** `test_contest_meta.py`
-   **Description:** This script validates the `meta.json` file for a contest. It checks for the presence of required fields, correct data types, and valid values.
-   **Usage:**
    ```bash
    python -m scripts.tests.contest.test_contest_meta --contest_id <contest_id>
    ```

### Participants Test

-   **Script:** `test_contest_participants.py`
-   **Description:** This script validates the `participants.json` file for a contest. It checks that the file is a valid JSON and contains a list of user IDs.
-   **Usage:**
    ```bash
    python -m scripts.tests.contest.test_contest_participants --contest_id <contest_id>
    ```
