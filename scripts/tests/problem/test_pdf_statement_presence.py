import os
import sys
import json
import argparse
from scripts.utils.data_utils import get_problem_path

def test_pdf_statement_presence(problem_id):
    problem_path = get_problem_path(problem_id)
    meta_file_path = os.path.join(problem_path, 'meta.json')
    pdf_statement_path = os.path.join(problem_path, 'details', 'statement.pdf')

    if not os.path.exists(meta_file_path):
        raise AssertionError(f"meta.json not found for problem {problem_id}: {meta_file_path}")

    with open(meta_file_path, 'r', encoding='utf-8') as f:
        meta_data = json.load(f)

    if meta_data.get("has_pdf_statement") is True:
        if not os.path.exists(pdf_statement_path):
            raise AssertionError(f"meta.json for {problem_id} is marked with \"has_pdf_statement\": true, but statement.pdf is missing at {pdf_statement_path}")
        else:
            print(f"Found expected PDF statement for {problem_id} at {pdf_statement_path}")
    else:
        print(f"No PDF statement expected for {problem_id}. Skipping check.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validate PDF statement presence for a given problem_id.')
    parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
    args = parser.parse_args()

    try:
        test_pdf_statement_presence(args.problem_id)
        print(f"PDF statement presence check PASSED for {args.problem_id}.")
    except AssertionError as e:
        print(f"PDF statement presence check FAILED for {args.problem_id}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
