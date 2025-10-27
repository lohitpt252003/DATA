# validator.py
import sys, math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    if len(sys.argv) < 3:
        print("Usage: validator.py <user_output_file> <test_input_file>")
        sys.exit(1)

    user_output_file = sys.argv[1]
    test_input_file = sys.argv[2]

    # --- Read user output ---
    with open(user_output_file, 'r') as f:
        user_out = f.read().strip().lower()   # case-insensitive

    # --- Read test input ---
    with open(test_input_file, 'r') as f:
        try:
            num = int(f.read().strip())
        except ValueError:
            print("FAIL: Test input is not an integer")
            sys.exit(1)

    expected_out = "prime" if is_prime(num) else "not prime"

    if user_out == expected_out:
        print("Accepted")
        sys.exit(0)
    else:
        print(f"FAIL: Expected '{expected_out}', got '{user_out}'")
        sys.exit(1)

if __name__ == "__main__":
    main()
