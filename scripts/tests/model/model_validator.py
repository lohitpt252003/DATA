import argparse
import sys
import subprocess

def main():
    print(f"--- Running all model validations ---")

    model_tests = [
        ("Model Files Presence", ["python", "-m", "scripts.tests.model.test_model_files_presence"])
    ]

    for test_name, test_command in model_tests:
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

    print("\n--- All model validations passed ---")

if __name__ == "__main__":
    main()

