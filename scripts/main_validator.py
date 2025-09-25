import argparse
import sys
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Run all validation tests for a given problem_id.')
    parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
    args = parser.parse_args()

    problem_id = args.problem_id
    if not problem_id.startswith('P'):
        print("Error: problem_id must be prefixed with 'P'.")
        sys.exit(1)

    print(f"--- Running all validations for {problem_id} ---")

    validators_to_run = [
        ("Problem Statement", ["python", "-m", "scripts.tests.problem.problem_statement_validator", problem_id]),
        ("Solution", ["python", "-m", "scripts.tests.solution.solution_validator", problem_id]),
        ("Model", ["python", "-m", "scripts.tests.model.model_validator"])
    ]

    for validator_name, validator_command in validators_to_run:
        print(f"\n--- Running {validator_name} Validator ---")
        result = subprocess.run(validator_command, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        
        if result.returncode != 0:
            print(f"--- {validator_name} Validator FAILED ---")
            print(f"\n--- Validation failed for {validator_name}. Exiting. ---")
            sys.exit(1)
        else:
            print(f"--- {validator_name} Validator PASSED ---")

    print("\n--- All validations passed ---")

    print("\n--- Validation complete ---")

if __name__ == "__main__":
    main()
