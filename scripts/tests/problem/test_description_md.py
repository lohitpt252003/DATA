import re
import sys
import argparse
import os
from scripts.utils.data_utils import get_problem_path

def validate_problem_md(description):
    """
    Validates the problem.md description.
    """
    if not description.strip():
        return "Description cannot be empty."
    return None

def main(problem_id_arg=None):
    if problem_id_arg:
        problem_id = problem_id_arg
    else:
        parser = argparse.ArgumentParser(description='Validate a problem.md file for a given problem_id.')
        parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
        args = parser.parse_args()
        problem_id = args.problem_id

    problem_path = get_problem_path(problem_id)
    file_path = os.path.join(problem_path, "details", "description.md")

    try:
        with open(file_path, 'r') as f:
            description = f.read()
            error = validate_problem_md(description)
            if error:
                print(f"Error in {file_path}: {error}")
            else:
                print(f"{file_path} is valid.")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()
