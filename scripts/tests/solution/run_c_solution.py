import os
import sys
import argparse
import subprocess
from scripts.utils.data_utils import get_problem_path, get_solution_path

import json
import subprocess
from scripts.utils.data_utils import get_problem_path, get_solution_path

def run_c_solution(problem_id):
    solution_dir = get_solution_path(problem_id)
    solution_path = os.path.join(solution_dir, "solution.c")
    executable_path = os.path.abspath(os.path.join(solution_dir, "solution_c_executable.exe")) # Temporary executable name
    problem_path = get_problem_path(problem_id)
    testcases_dir = os.path.join(problem_path, "testcases")
    samples_dir = os.path.join(problem_path, "details", "samples")

    if not os.path.exists(solution_path):
        print(f"Error: C solution not found at {solution_path}")
        return

    try:
        with open(os.path.join(problem_path, 'meta.json'), 'r') as f:
            meta_data = json.load(f)
            time_limit = meta_data.get("timeLimit", 1000) / 1000  # Convert to seconds
    except FileNotFoundError:
        print(f"Warning: meta.json not found for {problem_id}. Using default time limit of 1 second.")
        time_limit = 1

    # Compile the C solution
    print(f"--- Compiling C solution for {problem_id} ---")
    compile_command = ["gcc", solution_path, "-o", executable_path]
    try:
        compile_result = subprocess.run(compile_command, check=True, capture_output=True, text=True)
        print("Compilation successful.")
        if compile_result.stdout:
            print(f"Compiler stdout: {compile_result.stdout.strip()}")
        if compile_result.stderr:
            print(f"Compiler stderr: {compile_result.stderr.strip()}")
    except subprocess.CalledProcessError as e:
        print("Compilation failed.")
        print(f"Stderr: {e.stderr.strip()}")
        return

    print(f"Executable path: {executable_path}")
    if not os.path.exists(executable_path):
        print(f"Error: Executable not found after compilation at {executable_path}")
        try:
            os.remove(executable_path) # Clean up executable if compilation failed but left a trace
        except OSError as e:
            print(f"Error cleaning up executable: {e}")
        return

    def _run_tests(test_dir, test_type):
        if not os.path.isdir(test_dir):
            print(f"No {test_type} directory found at {test_dir}. Skipping {test_type} tests.")
            return

        test_files = sorted([f for f in os.listdir(test_dir) if f.endswith('.in')])

        if not test_files:
            print(f"No {test_type} found for {problem_id}. Skipping {test_type} tests.")
            return

        print(f"--- Running C solution for {problem_id} ({test_type}) ---")

        for test_file in test_files:
            test_case_number = os.path.splitext(test_file)[0]
            input_path = os.path.join(test_dir, test_file)
            expected_output_path = os.path.join(test_dir, f"{test_case_number}.out")

            if not os.path.exists(expected_output_path):
                print(f"Warning: Missing expected output file for {test_type} {test_case_number}")
                continue

            with open(input_path, 'r') as f_in:
                try:
                    process = subprocess.run(
                        [executable_path],
                        stdin=f_in,
                        capture_output=True,
                        text=True,
                        check=True,
                        timeout=time_limit
                    )
                    actual_output = process.stdout.strip()
                except subprocess.TimeoutExpired:
                    print(f"{test_type} {test_case_number}: Time Limit Exceeded")
                    continue
                except subprocess.CalledProcessError as e:
                    print(f"{test_type} {test_case_number}: Runtime Error")
                    print(f"Stderr: {e.stderr.strip()}")
                    continue
                except Exception as e:
                    print(f"{test_type} {test_case_number}: Execution Failed - {e}")
                    continue

            with open(expected_output_path, 'r') as f_out:
                expected_output = f_out.read().strip()

            print(f"{test_type} {test_case_number}: {'PASSED' if actual_output == expected_output else 'FAILED'}")
            print(f"  Input: {open(input_path).read().strip()}")
            print(f"  Expected: '{expected_output}'")
            print(f"  Actual:   '{actual_output}'")

    _run_tests(testcases_dir, "Test Case")
    _run_tests(samples_dir, "Sample")

    try:
        os.remove(executable_path) # Clean up executable after all tests
    except OSError as e:
        print(f"Error cleaning up executable: {e}")

def main():
    parser = argparse.ArgumentParser(description='Run C solution against test cases.')
    parser.add_argument('problem_id', help='The ID of the problem (e.g., P1)')
    args = parser.parse_args()

    run_c_solution(args.problem_id)

if __name__ == "__main__":
    main()