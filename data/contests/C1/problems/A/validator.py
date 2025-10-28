# validator.py
import sys
import math

def count_divisors(x: int) -> int:
    """Returns number of divisors of x."""
    cnt = 0
    i = 1
    while i * i <= x:
        if x % i == 0:
            cnt += 1 if i * i == x else 2
        i += 1
    return cnt


def main():
    if len(sys.argv) < 3:
        print("Usage: validator.py <user_output_file> <test_input_file>")
        sys.exit(1)

    user_output_file = sys.argv[1]
    test_input_file = sys.argv[2]

    # --- Read user output ---
    with open(user_output_file, 'r') as f:
        user_out_lines = [line.strip() for line in f if line.strip()]

    # --- Read test input ---
    with open(test_input_file, 'r') as f:
        data = f.read().strip().split()
    
    if not data:
        print("FAIL: Empty test input")
        sys.exit(1)

    try:
        n = int(data[0])
        nums = list(map(int, data[1:]))
    except ValueError:
        print("FAIL: Invalid input format (expected integers)")
        sys.exit(1)

    if len(nums) != n:
        print(f"FAIL: Expected {n} numbers, got {len(nums)}")
        sys.exit(1)

    # --- Compute expected output ---
    expected_out = [str(count_divisors(x)) for x in nums]

    # --- Validate ---
    if len(user_out_lines) != len(expected_out):
        print(f"FAIL: Expected {len(expected_out)} lines, got {len(user_out_lines)}")
        sys.exit(1)

    for i, (user_line, correct_line) in enumerate(zip(user_out_lines, expected_out), start=1):
        if user_line != correct_line:
            print(f"FAIL: Line {i}: expected '{correct_line}', got '{user_line}'")
            sys.exit(1)

    print("Accepted")
    sys.exit(0)


if __name__ == "__main__":
    main()
