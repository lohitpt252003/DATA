
import os
import sys
import argparse
import subprocess

def run_python_solution(problem_id):
    solution_path = os.path.join("solutions", problem_id, "solution.py")
    testcases_dir = os.path.join("data", "problems", problem_id, "testcases")

    if not os.path.exists(solution_path):
        print(f"Error: Python solution not found at {solution_path}")
        return

    if not os.path.isdir(testcases_dir):
        print(f"Error: Testcases directory not found at {testcases_dir}")
        return

    test_files = sorted([f for f in os.listdir(testcases_dir) if f.endswith('.in')])

    if not test_files:
        print(f"No test cases found for {problem_id}")
        return

    print(f"--- Running Python solution for {problem_id} ---")

    for test_file in test_files:
        test_case_number = os.path.splitext(test_file)[0]
        input_path = os.path.join(testcases_dir, test_file)
        expected_output_path = os.path.join(testcases_dir, f"{test_case_number}.out")

        if not os.path.exists(expected_output_path):
            print(f"Warning: Missing expected output file for test case {test_case_number}")
            continue

        with open(input_path, 'r') as f_in:
            try:
                process = subprocess.run(
                    ["python", solution_path],
                    stdin=f_in,
                    capture_output=True,
                    text=True,
                    check=True
                )
                actual_output = process.stdout.strip()
            except subprocess.CalledProcessError as e:
                print(f"Test Case {test_case_number}: Runtime Error")
                print(f"Stderr: {e.stderr.strip()}")
                continue
            except Exception as e:
                print(f"Test Case {test_case_number}: Execution Failed - {e}")
                continue

        with open(expected_output_path, 'r') as f_out:
            expected_output = f_out.read().strip()

        if actual_output == expected_output:
            print(f"Test Case {test_case_number}: PASSED")
        else:
            print(f"Test Case {test_case_number}: FAILED")
            print(f"  Input: {open(input_path).read().strip()}")
            print(f"  Expected: '{expected_output}'")
            print(f"  Actual:   '{actual_output}'")

def main():
    parser = argparse.ArgumentParser(description='Run Python solution against test cases.')
    parser.add_argument('problem_id', help='The ID of the problem (e.g., P1)')
    args = parser.parse_args()

    run_python_solution(args.problem_id)

if __name__ == "__main__":
    main()
