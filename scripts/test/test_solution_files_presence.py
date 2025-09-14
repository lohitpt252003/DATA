import os
import sys
import json

from ..utils.data_utils import get_problem_path, get_solution_path

def test_solution_files_presence(problem_id):
    print(f"Running test_solution_files_presence for problem: {problem_id}")

    solution_base_path = get_solution_path(problem_id)

    # Define expected solution files and their corresponding languages
    expected_solution_files = {
        'python': os.path.join(solution_base_path, 'solution.py'),
        'cpp': os.path.join(solution_base_path, 'solution.cpp'),
        'c': os.path.join(solution_base_path, 'solution.c'),
    }

    # Check for the presence of each expected solution file
    for lang, file_path in expected_solution_files.items():
        if not os.path.exists(file_path):
            raise AssertionError(f"Missing {lang} solution file for problem {problem_id}: {file_path}")
        
    print(f"All expected solution files for problem {problem_id} are present.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python -m scripts.test.test_solution_files_presence <problem_id>")
        sys.exit(1)

    problem_id = sys.argv[1]
    try:
        test_solution_files_presence(problem_id)
        print(f"Test for problem {problem_id} solution files presence PASSED.")
    except AssertionError as e:
        print(f"Test for problem {problem_id} solution files presence FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during testing: {e}")
        sys.exit(1)
