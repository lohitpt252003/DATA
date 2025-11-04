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
    if len(sys.argv) != 3:
        print("Usage: python validator.py <user_output_file> <test_input_file>")
        sys.exit(1)

    user_output_filename = sys.argv[1]
    correct_input_filename = sys.argv[2]

    try:
        with open(correct_input_filename, 'r') as f:
            input_lines = f.read().strip().split('\n')
        
        with open(user_output_filename, 'r') as f:
            user_lines = f.read().strip().split('\n')

        if not input_lines or not input_lines[0]:
            print("Wrong Answer") # Handles empty input file
            sys.exit(0)

        n = int(input_lines[0])
        
        if len(input_lines) != n + 1:
            print("Wrong Answer") # Incorrect number of lines in input
            sys.exit(0)

        numbers = [int(line) for line in input_lines[1:]]

        if len(user_lines) != n:
            print("Wrong Answer") # User output has wrong number of lines
            sys.exit(0)

        for i in range(n):
            expected_divisors = count_divisors(numbers[i])
            user_divisors = int(user_lines[i])
            if user_divisors != expected_divisors:
                print("Wrong Answer")
                sys.exit(0)
                
        print("Accepted")
        sys.exit(0)

    except (IOError, ValueError):
        # If file reading fails or int conversion fails, it's a Wrong Answer
        print("Wrong Answer")
        sys.exit(0)


if __name__ == "__main__":
    main()