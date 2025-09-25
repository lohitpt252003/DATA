import argparse
import sys
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description='Run all problem statement validation tests for a given problem_id.')
    parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
    args = parser.parse_args()

    problem_id = args.problem_id
    if not problem_id.startswith('P'):
        print("Error: problem_id must be prefixed with 'P'.")
        sys.exit(1)

    print(f"--- Running all problem statement validations for {problem_id} ---")

    problem_tests = [
        ("meta.json", ["python", "-m", "scripts.tests.problem.test_meta", problem_id]),
        ("description.md", ["python", "-m", "scripts.tests.problem.test_description_md", problem_id]),
        ("input.md", ["python", "-m", "scripts.tests.problem.test_input_md", problem_id]),
        ("output.md", ["python", "-m", "scripts.tests.problem.test_output_md", problem_id]),
        ("constraints.md", ["python", "-m", "scripts.tests.problem.test_constraints_md", problem_id]),
        ("notes.md", ["python", "-m", "scripts.tests.problem.test_notes_md", problem_id]),
        ("header.md", ["python", "-m", "scripts.tests.problem.test_header_md", problem_id]),
        ("testcases", ["python", "-m", "scripts.tests.problem.test_testcases", problem_id]),
        ("index.json", ["python", "-m", "scripts.tests.problem.test_index", "--problem_id", problem_id]),
        ("Problem Submissions Structure", ["python", "-m", "scripts.tests.problem.test_problem_submissions_structure", problem_id]),
        ("User Structure", ["python", "-m", "scripts.tests.problem.test_user_structure"]),
        ("PDF Statement Presence", ["python", "-m", "scripts.tests.problem.test_pdf_statement_presence", problem_id]),
        ("Problem TeX", ["python", "-m", "scripts.tests.problem.test_problem_tex", problem_id])
    ]

    for test_name, test_command in problem_tests:
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

    print("\n--- All problem statement validations passed ---")

if __name__ == "__main__":
    main()
