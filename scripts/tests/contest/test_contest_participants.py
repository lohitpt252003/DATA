import os
import json

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
    import sys
    if len(sys.argv) > 1:
        contest_id = sys.argv[1]
        success, messages = validate_contest_participants(contest_id, base_path=".") # Changed base_path to "."
        if success:
            print(f"Contest {contest_id} participants.json is valid.")
        else:
            print(f"Contest {contest_id} participants.json has errors:")
            for msg in messages:
                print(f"- {msg}")
    else:
        print("Usage: python test_contest_participants.py <contest_id>")