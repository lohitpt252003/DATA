import os
import json
import argparse

def validate_contest_participants(contest_id, base_path="."):
    contest_path = os.path.join(base_path, "data", "contests", contest_id)
    errors = []

    participants_json_file = os.path.join(contest_path, "participants.json")

    if not os.path.exists(participants_json_file):
        errors.append(f"Missing participants.json for contest {contest_id}")
        return False, errors

    # Validate participants.json is valid JSON
    try:
        with open(participants_json_file, 'r', encoding='utf-8') as f:
            json.load(f)
    except json.JSONDecodeError:
        errors.append(f"participants.json for contest {contest_id} is not a valid JSON file")
    except Exception as e:
        errors.append(f"Error reading participants.json for contest {contest_id}: {e}")

    if errors:
        return False, errors
    return True, []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate contest participants.json.')
    parser.add_argument('--contest_id', required=True, help='The ID of the contest to validate (e.g., C1)')
    args = parser.parse_args()

    success, messages = validate_contest_participants(args.contest_id, base_path="..")
    if success:
        print(f"Contest {args.contest_id} participants.json is valid.")
    else:
        print(f"Contest {args.contest_id} participants.json has errors:")
        for msg in messages:
            print(f"- {msg}")
        sys.exit(1)