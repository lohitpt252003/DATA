import os
import json
import argparse
import re
import random

# This script provides a framework for generating input files for test cases
# for a given problem. You will need to fill in the problem-specific logic
# in the `generate_input` function.

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def generate_input():
    """
    Generates 25 test cases for the "Prime or not" problem (C1A).
    """
    test_cases = []

    # 1. Corner cases
    test_cases.extend([0, 1, 2, 10000000000])

    # 2. Random prime cases
    prime_cases = 0
    while prime_cases < 8:
        n = random.randint(3, 10000000000)
        if is_prime(n):
            test_cases.append(n)
            prime_cases += 1

    # 3. Random non-prime cases
    non_prime_cases = 0
    while non_prime_cases < 8:
        n = random.randint(4, 10000000000)
        if not is_prime(n):
            test_cases.append(n)
            non_prime_cases += 1

    # 4. TLE cases (large primes close to the upper bound)
    tle_cases = 0
    while tle_cases < 5:
        n = random.randint(10000000000 - 1000, 10000000000)
        if n % 2 != 0 and is_prime(n):
            test_cases.append(n)
            tle_cases += 1
    
    # Make sure we have 25 cases. If not, add more random non-primes.
    while len(test_cases) < 25:
        n = random.randint(4, 10000000000)
        if not is_prime(n):
            test_cases.append(n)

    return test_cases[:25]

def main():
    parser = argparse.ArgumentParser(description='Generate input files for test cases for a given problem.')
    parser.add_argument('--problem_id', required=True, help='The ID of the problem (e.g., C1A)')
    args = parser.parse_args()

    problem_id = args.problem_id

    # --- Find the problem directory ---
    match = re.match(r"C(\d+)([A-Z]+)", problem_id)
    if not match:
        print(f"Error: Invalid problem_id format: {problem_id}")
        return
    
    contest_id_num = match.group(1)
    problem_letter = match.group(2)
    contest_id = f"C{contest_id_num}"

    # Assuming the script is run from the root of the DATA directory
    problem_dir = os.path.join("data", "contests", contest_id, "problems", problem_letter)
    if not os.path.isdir(problem_dir):
        print(f"Error: Problem directory not found: {problem_dir}")
        return

    testcases_dir = os.path.join(problem_dir, "testcases")
    if not os.path.isdir(testcases_dir):
        os.makedirs(testcases_dir)

    # --- Generate and save input files ---
    inputs = generate_input()
    for i, input_data in enumerate(inputs):
        input_str = str(input_data)

        input_filename = os.path.join(testcases_dir, f"{i+1}.in")

        with open(input_filename, 'w', encoding='utf-8') as f:
            f.write(input_str)
        
        print(f"Generated input file {i+1}: input='{input_str}'")

    print(f"Successfully generated {len(inputs)} input files for problem {problem_id}")

if __name__ == "__main__":
    main()
