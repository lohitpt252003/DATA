import os
import sys
import argparse

def validate_testcases(testcases_path):
    """
    Validates the testcases directory.
    """
    if not os.path.isdir(testcases_path):
        return f"Error: testcases directory not found at {testcases_path}"

    in_files = [f for f in os.listdir(testcases_path) if f.endswith('.in')]
    out_files = [f for f in os.listdir(testcases_path) if f.endswith('.out')]

    if not in_files or not out_files:
        return "Error: No .in or .out files found in testcases directory."

    if len(in_files) != len(out_files):
        return "Error: Mismatch between number of .in and .out files."

    return None

def main(problem_id_arg=None):
    if problem_id_arg:
        problem_id = problem_id_arg
    else:
        parser = argparse.ArgumentParser(description='Validate a testcases directory for a given problem_id.')
        parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
        args = parser.parse_args()
        problem_id = args.problem_id

    dir_path = os.path.join("data", "problems", problem_id, "testcases")

    error = validate_testcases(dir_path)
    if error:
        print(f"Error in {dir_path}: {error}")
    else:
        print(f"{dir_path} is valid.")

if __name__ == "__main__":
    main()