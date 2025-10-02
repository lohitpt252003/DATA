import argparse
import sys
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Run validation tests for a given problem_id or contest_id.')
    parser.add_argument('--problem_id', help='The ID of the problem to validate (e.g., P1)')
    parser.add_argument('--contest_id', help='The ID of the contest to validate (e.g., C1)')
    args = parser.parse_args()

    if args.problem_id and args.contest_id:
        print("Error: Please provide either --problem_id or --contest_id, not both.")
        sys.exit(1)
    elif not args.problem_id and not args.contest_id:
        print("Error: Please provide either --problem_id or --contest_id.")
        sys.exit(1)

    if args.problem_id:
        item_id = args.problem_id
        if not item_id.startswith('P'):
            print("Error: problem_id must be prefixed with 'P'.")
            sys.exit(1)
        print(f"--- Running all validations for Problem {item_id} ---")
        validators_to_run = [
            ("Problem Structure", ["python", "-m", "scripts.tests.test_problem_structure", item_id]),
            ("Solution Files Presence", ["python", "-m", "scripts.tests.test_solution_files_presence", item_id]),
            ("Model Files Presence", ["python", "-m", "scripts.tests.test_model_files_presence", item_id])
        ]
    elif args.contest_id:
        item_id = args.contest_id
        if not item_id.startswith('C'):
            print("Error: contest_id must be prefixed with 'C'.")
            sys.exit(1)
        print(f"--- Running all validations for Contest {item_id} ---")
        validators_to_run = [
            ("Contest Structure", ["python", "-m", "scripts.tests.contest.contest_main_validator", item_id])
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
