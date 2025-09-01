import json
import sys
import argparse
import os

def validate_index_json(problem_id, index_data):
    """
    Validates the index.json data for a specific problem_id.
    """
    if problem_id not in index_data:
        return f"Error: {problem_id} not found in index.json"

    problem_info = index_data[problem_id]
    required_fields = ["title", "difficulty", "tags", "authors"]
    for field in required_fields:
        if field not in problem_info:
            return f"Missing required field '{field}' for {problem_id} in index.json"

    return None

def main(problem_id_arg=None):
    problem_id_to_check = problem_id_arg
    if not problem_id_to_check:
        parser = argparse.ArgumentParser(description='Validate an index.json file.')
        parser.add_argument('--problem_id', help='The ID of the problem to validate (e.g., P1)')
        args = parser.parse_args()
        problem_id_to_check = args.problem_id

    file_path = os.path.join("data", "problems", "index.json")

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            errors = []
            if problem_id_to_check:
                # Validate a specific problem_id
                error = validate_index_json(problem_id_to_check, data)
                if error:
                    errors.append(error)
            else:
                # Validate all entries
                for problem_id in data:
                    error = validate_index_json(problem_id, data)
                    if error:
                        errors.append(error)
            
            if errors:
                for err in errors:
                    print(f"Error in {file_path}: {err}")
            else:
                if problem_id_to_check:
                    print(f"Entry for {problem_id_to_check} in {file_path} is valid.")
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