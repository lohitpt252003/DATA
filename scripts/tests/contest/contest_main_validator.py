import sys
import os
import argparse

# Import individual validators
from scripts.tests.contest.test_contest_meta import validate_contest_meta
from scripts.tests.contest.test_contest_markdown_files import validate_contest_markdown_files
from scripts.tests.contest.test_contest_participants import validate_contest_participants

def validate_contest_structure(contest_id, base_path):
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
    parser = argparse.ArgumentParser(description='Run all contest validation tests for a given contest_id.')
    parser.add_argument('--contest_id', required=True, help='The ID of the contest to validate (e.g., C1)')
    args = parser.parse_args()

    # When run directly, base_path should be ".." to refer to the DATA root
    success, messages = validate_contest_structure(args.contest_id, base_path="..")
    if success:
        print(f"Contest {args.contest_id} structure is valid.")