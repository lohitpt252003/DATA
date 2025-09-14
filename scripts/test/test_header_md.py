import os
import sys
import argparse

from ..utils.data_utils import get_problem_path

def validate_header_md(content):
    """
    Validates the header.md content.
    """
    # Header can be empty, so we only check if the file exists.
    # If it exists, it's considered valid for now.
    return None

def main(problem_id_arg=None):
    if problem_id_arg:
        problem_id = problem_id_arg
    else:
        parser = argparse.ArgumentParser(description='Validate a header.md file for a given problem_id.')
        parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
        args = parser.parse_args()
        problem_id = args.problem_id

    problem_path = get_problem_path(problem_id)
    file_path = os.path.join(problem_path, "details", "header.md")

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            error = validate_header_md(content)
            if error:
                print(f"Error in {file_path}: {error}")
                sys.exit(1)
            else:
                print(f"{file_path} is valid.")
    except FileNotFoundError:
        # Header.md is optional, so if not found, it's still considered valid.
        print(f"header.md not found at {file_path}. This is optional and considered valid.")
        sys.exit(0) # Exit with 0 for success

if __name__ == "__main__":
    main()