import argparse
import sys
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description='Run all validation tests for a given problem_id.')
    parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
    args = parser.parse_args()

    problem_id = args.problem_id
    if not problem_id.startswith('P'):
        print("Error: problem_id must be prefixed with 'P'.")
        sys.exit(1)

    print(f"--- Running all validations for {problem_id} ---")

    tests_to_run = [
        ("meta.json", ["python", "-m", "scripts.test.test_meta", problem_id]),
        ("description.md", ["python", "-m", "scripts.test.test_description_md", problem_id]),
        ("input.md", ["python", "-m", "scripts.test.test_input_md", problem_id]),
        ("output.md", ["python", "-m", "scripts.test.test_output_md", problem_id]),
        ("constraints.md", ["python", "-m", "scripts.test.test_constraints_md", problem_id]),
        ("notes.md", ["python", "-m", "scripts.test.test_notes_md", problem_id]),
        ("header.md", ["python", "-m", "scripts.test.test_header_md", problem_id]),
        ("testcases", ["python", "-m", "scripts.test.test_testcases", problem_id]),
        ("index.json", ["python", "-m", "scripts.test.test_index", "--problem_id", problem_id]),
        ("solution.md", ["python", "-m", "scripts.test.test_solution_md", problem_id]),
        ("Problem Submissions Structure", ["python", "-m", "scripts.test.test_problem_submissions_structure", problem_id]),
        ("Solution Files Presence", ["python", "-m", "scripts.test.test_solution_files_presence", problem_id]),
        ("User Structure", ["python", "-m", "scripts.test.test_user_structure"]), # Test all users
        ("Python Solution", ["python", "-m", "scripts.test.run_py_solution", problem_id]),
        ("C Solution", ["python", "-m", "scripts.test.run_c_solution", problem_id]),
        ("C++ Solution", ["python", "-m", "scripts.test.run_cpp_solution", problem_id])
    ]

    for test_name, test_command in tests_to_run:
        print(f"\n--- Validating {test_name} ---")
        result = subprocess.run(test_command, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        
        if result.returncode != 0 or "Error" in result.stdout or "Error" in result.stderr:
            print(f"--- {test_name} validation FAILED ---")
            print(result.stdout)
            print(result.stderr)
            print(f"\n--- Validation failed for {test_name}. Exiting. ---")
            sys.exit(1)
        else:
            print(f"--- {test_name} validation PASSED ---")

    print("\n--- All validations passed ---")

    print("\n--- Validation complete ---")

if __name__ == "__main__":
    main()