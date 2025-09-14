import os
import sys
import json

from ..utils.data_utils import get_user_path, get_all_user_ids

def test_user_structure(user_id=None):
    print(f"Running test_user_structure for user: {user_id if user_id else 'all users'}")

    user_ids = [user_id] if user_id else get_all_user_ids()

    if not user_ids:
        raise AssertionError("No users found to test.")

    for current_user_id in user_ids:
        user_path = get_user_path(current_user_id)
        meta_file_path = os.path.join(user_path, 'meta.json')
        submissions_dir_path = os.path.join(user_path, 'submissions')

        # 1. Verify the existence of meta.json
        if not os.path.exists(meta_file_path):
            raise AssertionError(f"meta.json not found for user {current_user_id}: {meta_file_path}")

        # 2. Verify the content of meta.json
        try:
            with open(meta_file_path, 'r', encoding='utf-8') as f:
                meta_data = json.load(f)
        except json.JSONDecodeError:
            raise AssertionError(f"Invalid JSON in meta.json for user {current_user_id}: {meta_file_path}")

        required_meta_fields = ['id', 'username', 'name', 'email']
        for field in required_meta_fields:
            if field not in meta_data:
                raise AssertionError(f"Missing required field '{field}' in {meta_file_path}")
        
        if meta_data['id'] != current_user_id:
            raise AssertionError(f"User ID mismatch in {meta_file_path}. Expected {current_user_id}, got {meta_data['id']}")

        # 3. Verify the existence of submissions directory, or handle if no submissions
        if not os.path.isdir(submissions_dir_path):
            # If the directory doesn't exist, assume no submissions and skip further checks
            print(f"Submissions directory not found for user {current_user_id}. Assuming no submissions.")
            continue # Skip to the next user or end of loop

        # 4. Verify the format of submission JSON files within submissions directory
        submission_files = [f for f in os.listdir(submissions_dir_path) if f.endswith('.json')]
        for submission_file in submission_files:
            submission_file_path = os.path.join(submissions_dir_path, submission_file)
            try:
                with open(submission_file_path, 'r', encoding='utf-8') as f:
                    submission_data = json.load(f)
            except json.JSONDecodeError:
                raise AssertionError(f"Invalid JSON in submission file {submission_file_path}")

            required_submission_fields = ['submission_id', 'problem_id', 'timestamp', 'status']
            for field in required_submission_fields:
                if field not in submission_data:
                    raise AssertionError(f"Missing required field '{field}' in {submission_file_path}")

    print(f"All user structures and submission files passed validation.")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Usage: python -m scripts.test.test_user_structure [user_id]")
        sys.exit(1)

    user_id = sys.argv[1] if len(sys.argv) == 2 else None
    try:
        test_user_structure(user_id)
        print(f"Test for user structure PASSED.")
    except AssertionError as e:
        print(f"Test for user structure FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during testing: {e}")
        sys.exit(1)
