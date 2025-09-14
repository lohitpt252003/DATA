import os
import sys
import argparse
import re

def validate_solution_md(solution_md_path):
    if not os.path.exists(solution_md_path):
        return f"Error: solution.md not found at {solution_md_path}"

    with open(solution_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    required_sections = [
        r"## Problem Description", 
        r"## Simple Answer", 
        r"## Detailed Explanation", 
        r"### Python", 
        r"### C++", 
        r"### C"
    ]

    for section in required_sections:
        if not re.search(section, content):
            return f"Missing required section: {section}"

    # Check if sections are not empty (basic check)
    # This is a simple check, more robust checks would involve parsing markdown
    if not re.search(r"## Simple Answer\s*\n\s*[^#]+", content, re.DOTALL):
        return "Simple Answer section appears empty or malformed."
    if not re.search(r"## Detailed Explanation\s*\n\s*[^#]+", content, re.DOTALL):
        return "Detailed Explanation section appears empty or malformed."

    return None

def main(problem_id_arg=None):
    if problem_id_arg:
        problem_id = problem_id_arg
    else:
        parser = argparse.ArgumentParser(description='Validate solution.md file for a given problem_id.')
        parser.add_argument('problem_id', help='The ID of the problem (e.g., P1)')
        args = parser.parse_args()
        problem_id = args.problem_id

    DATA_BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    solution_md_path = os.path.join(DATA_BASE_PATH, "data", "solutions", problem_id, "solution.md")



    error = validate_solution_md(solution_md_path)
    if error:
        print(f"Error in {solution_md_path}: {error}")
    else:
        print(f"{solution_md_path} is valid.")

if __name__ == "__main__":
    main()