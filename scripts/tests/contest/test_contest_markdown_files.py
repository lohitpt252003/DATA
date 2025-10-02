import os
import argparse

def validate_contest_markdown_files(contest_id, base_path="."):
    contest_path = os.path.join(base_path, "data", "contests", contest_id)
    errors = []

    contest_md_file = os.path.join(contest_path, "contest.md")
    theory_md_file = os.path.join(contest_path, "theory.md")

    # Validate contest.md and theory.md are not empty
    try:
        with open(contest_md_file, 'r', encoding='utf-8') as f:
            if not f.read().strip():
                errors.append(f"contest.md for contest {contest_id} is empty")
    except FileNotFoundError:
        errors.append(f"Missing contest.md for contest {contest_id}")
    except Exception as e:
        errors.append(f"Error reading contest.md for contest {contest_id}: {e}")

    try:
        with open(theory_md_file, 'r', encoding='utf-8') as f:
            if not f.read().strip():
                errors.append(f"theory.md for contest {contest_id} is empty")
    except FileNotFoundError:
        errors.append(f"Missing theory.md for contest {contest_id}")
    except Exception as e:
        errors.append(f"Error reading theory.md for contest {contest_id}: {e}")

    if errors:
        return False, errors
    return True, []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate contest markdown files.')
    parser.add_argument('--contest_id', required=True, help='The ID of the contest to validate (e.g., C1)')
    args = parser.parse_args()

    success, messages = validate_contest_markdown_files(args.contest_id, base_path="..")
    if success:
        print(f"Contest {args.contest_id} markdown files are valid.")
    else:
        print(f"Contest {args.contest_id} markdown files have errors:")
        for msg in messages:
            print(f"- {msg}")
        sys.exit(1)