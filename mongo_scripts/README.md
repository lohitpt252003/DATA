# MongoDB Management Scripts

This directory contains Python scripts organized into subdirectories for managing different types of data in the MongoDB database.

## Subdirectories:

-   **`contests/`**: Contains scripts for managing contest data.
    -   [View Contest Scripts README](./contests/README.md)
-   **`problems/`**: Contains scripts for managing problem data.
    -   [View Problem Scripts README](./problems/README.md)

## Usage Examples:

To run any of the scripts, navigate to the respective subdirectory and execute the script using Python. Ensure your `.env` file is correctly configured in the parent `DATA` directory.

### Contest Management:

-   **Add a new contest:**
    ```bash
    python contests/add_contest.py --id C1
    ```
-   **Get all contests:**
    ```bash
    python contests/get_all_contests.py
    ```
-   **Update a contest:**
    ```bash
    python contests/update_contest.py --id C1
    ```

### Problem Management:

-   **Add a new problem:**
    ```bash
    python problems/add_problem.py --id C1A
    ```
-   **Get a problem by ID:**
    ```bash
    python problems/get_problem_by_id.py --id C1A
    ```
-   **Update a problem:**
    ```bash
    python problems/update_problem.py --id C1A
    ```
-   **Delete a problem:**
    ```bash
    python problems/delete_problem.py --id C1A
    ```