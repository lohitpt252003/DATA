import os
import sys
import argparse
from scripts.utils.data_utils import DATA_BASE_PATH

def test_model_files_presence():
    print("Running test_model_files_presence...")

    models_base_path = os.path.join(DATA_BASE_PATH, "models")

    expected_files = {
        "problems": "problem.py",
        "solutions": "solution.py",
        "submissions": "submission.py",
        "users": "user.py",
    }

    for sub_dir, file_name in expected_files.items():
        path = os.path.join(models_base_path, sub_dir, file_name)
        if not os.path.exists(path):
            raise AssertionError(f"Missing model file: {path}")
        else:
            print(f"Found expected model file: {path}")

    print("All expected model files are present.")

if __name__ == '__main__':
    try:
        test_model_files_presence()
        print("Model files presence check PASSED.")
    except AssertionError as e:
        print(f"Model files presence check FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
