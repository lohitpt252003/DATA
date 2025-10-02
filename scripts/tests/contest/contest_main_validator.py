import sys
import os

# Import individual validators
from scripts.tests.contest.test_contest_meta import validate_contest_meta
from scripts.tests.contest.test_contest_markdown_files import validate_contest_markdown_files
from scripts.tests.contest.test_contest_participants import validate_contest_participants

def validate_contest_structure(contest_id, base_path="."):
    all_errors = []

    # Run meta.json validation
    success, errors = validate_contest_meta(contest_id, base_path)
    if not success:
        all_errors.extend(errors)

    # Run markdown files validation
    success, errors = validate_contest_markdown_files(contest_id, base_path)
    if not success:
        all_errors.extend(errors)

    # Run participants.json validation
    success, errors = validate_contest_participants(contest_id, base_path)
    if not success:
        all_errors.extend(errors)

    if all_errors:
        return False, all_errors
    return True, []

if __name__ == "__main__":
    if len(sys.argv) > 1:
        contest_id = sys.argv[1]
        success, messages = validate_contest_structure(contest_id, base_path=".") # Changed base_path to "."
        if success:
            print(f"Contest {contest_id} structure is valid.")
        else:
            print(f"Contest {contest_id} structure has errors:")
            for msg in messages:
                print(f"- {msg}")
            sys.exit(1) # <--- Add this line to exit with a non-zero status code on error
    else:
        print("Usage: python contest_main_validator.py <contest_id>")