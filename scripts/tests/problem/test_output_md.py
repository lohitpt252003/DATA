import os
import sys
import argparse

from scripts.utils.data_utils import get_problem_path

def validate_output_md(content):
    """
    Validates the output.md content.
    """
    if not content.strip():
        return "Output description cannot be empty."
    return None

def main(problem_id_arg=None):
    if problem_id_arg:
        problem_id = problem_id_arg
    else:
        parser = argparse.ArgumentParser(description='Validate an output.md file for a given problem_id.')
        parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
        args = parser.parse_args()
        problem_id = args.problem_id

    problem_path = get_problem_path(problem_id)
    file_path = os.path.join(problem_path, "details", "output.md")

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            error = validate_output_md(content)
            if error:
                print(f"Error in {file_path}: {error}")
                sys.exit(1)
            else:
                print(f"{file_path} is valid.")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()