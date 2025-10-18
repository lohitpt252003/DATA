# Contest Management Scripts

This directory contains Python scripts for managing contest data in the MongoDB database.

## Scripts:

- `add_contest.py`: Adds a new contest to the database.
  - Usage: `python add_contest.py --id C1 --name "Test Contest" --authors "John Doe" --problems C1A C1B`
- `get_all_contests.py`: Retrieves all contests from the database.
  - Usage: `python get_all_contests.py`
- `get_contest_by_id.py`: Retrieves a contest by its ID.
  - Usage: `python get_contest_by_id.py --id C1`
- `update_contest.py`: Updates an existing contest.
  - Usage: `python update_contest.py --id C1 --name "New Contest Name" --add-problems C1C --remove-problems C1A`
- `delete_contest.py`: Deletes a contest by its ID.
  - Usage: `python delete_contest.py --id C1`

## ID Validation:

- Contest IDs must be in the format `C<number>` (e.g., `C1`, `C100`).
- Problem IDs must be in the format `C<contest_id><problem_letter>` (e.g., `C1A`, `C100AA`).
