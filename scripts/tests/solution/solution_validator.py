import argparse
import sys
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description='Run all solution validation tests for a given problem_id.')
    parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
    args = parser.parse_args()

    problem_id = args.problem_id
    if not problem_id.startswith('P'):
        print("Error: problem_id must be prefixed with 'P'.")
        sys.exit(1)

    print(f"--- Running all solution validations for {problem_id} ---")

    solution_tests = [
        ("solution.md", ["python", "-m", "scripts.tests.solution.test_solution_md", problem_id]),
        ("Solution Files Presence", ["python", "-m", "scripts.tests.solution.test_solution_files_presence", problem_id]),
        ("Python Solution", ["python", "-m", "scripts.tests.solution.run_py_solution", problem_id]),
        ("C Solution", ["python", "-m", "scripts.tests.solution.run_c_solution", problem_id]),
        ("C++ Solution", ["python", "-m", "scripts.tests.solution.run_cpp_solution", problem_id]),
        ("PDF Solution Presence", ["python", "-m", "scripts.tests.solution.test_pdf_solution_presence", problem_id]),
        ("Solution TeX", ["python", "-m", "scripts.tests.solution.test_solution_tex", problem_id])
    ]

    for test_name, test_command in solution_tests:
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

    print("\n--- All solution validations passed ---")

if __name__ == "__main__":
    main()
