import os
import json
from datetime import datetime
import argparse

def validate_contest_meta(contest_id, base_path="."):
    contest_path = os.path.join(base_path, "data", "contests", contest_id)
    errors = []

    meta_file = os.path.join(contest_path, "meta.json")

    if not os.path.exists(meta_file):
        errors.append(f"Missing meta.json for contest {contest_id}")
        return False, errors

    try:
        with open(meta_file, 'r', encoding='utf-8') as f:
            meta_data = json.load(f)

        # Required fields and types
        if not isinstance(meta_data.get("id"), str) or not meta_data["id"].startswith("C"):
            errors.append(f"meta.json: 'id' is missing or invalid for {contest_id}")
        if not isinstance(meta_data.get("name"), str) or not meta_data["name"]:
            errors.append(f"meta.json: 'name' is missing or empty for {contest_id}")
        if not isinstance(meta_data.get("description"), str) or not meta_data["description"]:
            errors.append(f"meta.json: 'description' is missing or empty for {contest_id}")
        if not isinstance(meta_data.get("problems"), list):
            errors.append(f"meta.json: 'problems' is missing or not a list for {contest_id}")
        if not isinstance(meta_data.get("authors"), list) or not meta_data["authors"]:
            errors.append(f"meta.json: 'authors' is missing or empty for {contest_id}")
        if not isinstance(meta_data.get("is_practice"), bool):
            errors.append(f"meta.json: 'is_practice' is missing or not a boolean for {contest_id}")

        # Date/Time validation
        start_time_str = meta_data.get("startTime")
        end_time_str = meta_data.get("endTime")

        if not isinstance(start_time_str, str):
            errors.append(f"meta.json: 'startTime' is missing or not a string for {contest_id}")
        if not isinstance(end_time_str, str):
            errors.append(f"meta.json: 'endTime' is missing or not a string for {contest_id}")

        if start_time_str and end_time_str:
            try:
                start_time = datetime.fromisoformat(start_time_str.replace('Z', '+00:00'))
            except ValueError:
                errors.append(f"meta.json: 'startTime' is not a valid ISO 8601 format for {contest_id}")
            try:
                end_time = datetime.fromisoformat(end_time_str.replace('Z', '+00:00'))
            except ValueError:
                errors.append(f"meta.json: 'endTime' is not a valid ISO 8601 format for {contest_id}")

            if 'start_time' in locals() and 'end_time' in locals() and start_time >= end_time:
                errors.append(f"meta.json: 'startTime' must be before 'endTime' for {contest_id}")

    except json.JSONDecodeError:
        errors.append(f"meta.json for contest {contest_id} is not a valid JSON file")
    except Exception as e:
        errors.append(f"Error reading meta.json for contest {contest_id}: {e}")

    if errors:
        return False, errors
    return True, []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate contest meta.json.')
    parser.add_argument('--contest_id', required=True, help='The ID of the contest to validate (e.g., C1)')
    args = parser.parse_args()

    success, messages = validate_contest_meta(args.contest_id, base_path="..") # Changed base_path to ".."
    if success:
        print(f"Contest {args.contest_id} meta.json is valid.")
    else:
        print(f"Contest {args.contest_id} meta.json has errors:")
        for msg in messages:
            print(f"- {msg}")
        sys.exit(1)