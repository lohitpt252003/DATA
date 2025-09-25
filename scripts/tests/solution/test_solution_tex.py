import os
import sys
import argparse
import re
from scripts.utils.data_utils import get_solution_path

def validate_solution_tex(solution_tex_path):
    if not os.path.exists(solution_tex_path):
        return f"Error: solution.tex not found at {solution_tex_path}"

    with open(solution_tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    required_sections = [
        r"\section*{Problem Description}",
        r"\section*{Simple Answer}",
        r"\section*{Detailed Explanation}",
        r"\subsection*{Python",
        r"\subsection*{C++",
        r"\subsection*{C"
    ]

    for section in required_sections:
        if not re.search(re.escape(section), content):
            return f"Missing required section in solution.tex: {section}"

    return None

def main():
    parser = argparse.ArgumentParser(description='Validate solution.tex file for a given problem_id.')
    parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
    args = parser.parse_args()

    solution_path = get_solution_path(args.problem_id)
    solution_tex_path = os.path.join(solution_path, 'solution.tex')

    error = validate_solution_tex(solution_tex_path)
    if error:
        print(f"Error in {solution_tex_path}: {error}")
        sys.exit(1)
    else:
        print(f"{solution_tex_path} is valid.")

if __name__ == "__main__":
    main()