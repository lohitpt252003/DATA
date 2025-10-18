# Problem Management Scripts

This directory contains Python scripts for managing problem data in the MongoDB database.

## Scripts:

- `add_problem.py`: Adds a new problem to the database.
  - Usage: `python add_problem.py --id C1A --title "Test Problem" --difficulty Easy --tags easy test --authors Gemini`
- `get_all_problems.py`: Retrieves all problems from the database.
  - Usage: `python get_all_problems.py`
- `get_problem_by_id.py`: Retrieves a problem by its ID.
  - Usage: `python get_problem_by_id.py --id C1A`
- `update_problem.py`: Updates an existing problem.
  - Usage: `python update_problem.py --id C1A --title "New Test Problem"`
- `delete_problem.py`: Deletes a problem by its ID.
  - Usage: `python delete_problem.py --id C1A`

## ID Validation:

- Problem IDs must be in the format `C<contest_id><problem_letter>` (e.g., `C1A`, `C100AA`).
