import os
import sys
import json

from ..utils.data_utils import get_problem_path, get_submission_path, get_all_problem_ids

def test_problem_submissions_structure(problem_id):
    print(f"Running test_problem_submissions_structure for problem: {problem_id}")

    problem_path = get_problem_path(problem_id)
    submissions_dir = os.path.join(problem_path, 'submissions')

    # 1. Verify the existence of the submissions directory
    if not os.path.isdir(submissions_dir):
        raise AssertionError(f"Submissions directory not found for problem {problem_id}: {submissions_dir}")

    # 2. Iterate through the submission JSON files
    submission_files = [f for f in os.listdir(submissions_dir) if f.endswith('.json')]
    if not submission_files:
        print(f"No submission files found for problem {problem_id}. Skipping detailed checks.")
        return

    for submission_file in submission_files:
        submission_id = os.path.splitext(submission_file)[0] # e.g., S1
        submission_file_path = os.path.join(submissions_dir, submission_file)

        # 3. Verify the content of these JSON files
        try:
            with open(submission_file_path, 'r', encoding='utf-8') as f:
                submission_data = json.load(f)
        except json.JSONDecodeError:
            raise AssertionError(f"Invalid JSON in submission file {submission_file_path}")

        required_fields = ['submission_id', 'user_id', 'timestamp', 'status']
        for field in required_fields:
            if field not in submission_data:
                raise AssertionError(f"Missing required field '{field}' in {submission_file_path}")
        
        if submission_data['submission_id'] != submission_id:
            raise AssertionError(f"submission_id mismatch in {submission_file_path}. Expected {submission_id}, got {submission_data['submission_id']}")

    print(f"All submission files for problem {problem_id} passed structure validation.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python -m scripts.test.test_problem_submissions_structure <problem_id>")
        sys.exit(1)

    problem_id = sys.argv[1]
    try:
        test_problem_submissions_structure(problem_id)
        print(f"Test for problem {problem_id} submissions structure PASSED.")
    except AssertionError as e:
        print(f"Test for problem {problem_id} submissions structure FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during testing: {e}")
        sys.exit(1)
