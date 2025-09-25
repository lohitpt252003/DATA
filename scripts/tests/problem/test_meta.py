import json
import sys
import argparse
import os
from scripts.utils.data_utils import get_problem_path

def validate_meta_json(meta_data):
    """
    Validates the meta.json data.
    """
    required_fields = ["id", "title", "timeLimit", "memoryLimit", "number_of_submissions"]
    for field in required_fields:
        if field not in meta_data:
            return f"Missing required field in meta.json: {field}"
    return None

def main(problem_id_arg=None):
    if problem_id_arg:
        problem_id = problem_id_arg
    else:
        parser = argparse.ArgumentParser(description='Validate a meta.json file for a given problem_id.')
        parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
        args = parser.parse_args()
        problem_id = args.problem_id

    problem_path = get_problem_path(problem_id)
    file_path = os.path.join(problem_path, "meta.json")

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            error = validate_meta_json(data)
            if error:
                print(f"Error in {file_path}: {error}")
            else:
                print(f"{file_path} is valid.")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Could not decode {file_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()
