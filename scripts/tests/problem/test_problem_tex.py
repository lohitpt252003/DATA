import os
import sys
import argparse
import re
from scripts.utils.data_utils import get_problem_path

def validate_problem_tex(problem_tex_path):
    if not os.path.exists(problem_tex_path):
        return f"Error: problem.tex not found at {problem_tex_path}"

    with open(problem_tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    required_commands = [
        r"\ProblemTitle",
        r"\Difficulty",
        r"\Tags",
        r"\Authors",
        r"\Statement",
        r"\InputFormat",
        r"\OutputFormat",
        r"\Constraints"
    ]

    for command in required_commands:
        if not re.search(re.escape(command), content):
            return f"Missing required command in problem.tex: {command}"

    return None

def main():
    parser = argparse.ArgumentParser(description='Validate problem.tex file for a given problem_id.')
    parser.add_argument('problem_id', help='The ID of the problem to validate (e.g., P1)')
    args = parser.parse_args()

    problem_path = get_problem_path(args.problem_id)
    problem_tex_path = os.path.join(problem_path, 'problem.tex')

    error = validate_problem_tex(problem_tex_path)
    if error:
        print(f"Error in {problem_tex_path}: {error}")
        sys.exit(1)
    else:
        print(f"{problem_tex_path} is valid.")

if __name__ == "__main__":
    main()
