import sys

def solve(n):
    # Find the first factor
    for a in range(2, int(n**0.5) + 2):
        if a * a > n:
            break
        if n % a == 0:
            n2 = n // a
            # Find the second factor
            for b in range(a + 1, int(n2**0.5) + 2):
                if b * b > n2:
                    break
                if n2 % b == 0:
                    c = n2 // b
                    if c > b:
                        return "YES", a, b, c
    return "NO", None, None, None

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

        num_test_cases = int(input_lines[0])
        ns = [int(line) for line in input_lines[1:]]

        if len(ns) != num_test_cases:
            print("Wrong Answer: Incorrect number of test cases in input file")
            sys.exit(0)

        user_line_idx = 0
        for i in range(num_test_cases):
            n = ns[i]
            
            if user_line_idx >= len(user_lines):
                print("Wrong Answer: Not enough output for all test cases")
                sys.exit(0)

            user_verdict = user_lines[user_line_idx].strip()

            if user_verdict == "NO":
                user_line_idx += 1
                correct_verdict, _, _, _ = solve(n)
                if correct_verdict != "NO":
                    print(f"Wrong Answer: Test case {i+1}, expected YES but got NO")
                    sys.exit(0)
            elif user_verdict.startswith("YES"):
                user_line_idx += 1
                if user_line_idx >= len(user_lines):
                    print("Wrong Answer: YES should be followed by three numbers")
                    sys.exit(0)
                
                parts = user_lines[user_line_idx].strip().split()
                user_line_idx += 1

                if len(parts) != 3:
                    print(f"Wrong Answer: Test case {i+1}, expected 3 numbers after YES")
                    sys.exit(0)
                
                try:
                    a, b, c = int(parts[0]), int(parts[1]), int(parts[2])
                except ValueError:
                    print(f"Wrong Answer: Test case {i+1}, numbers are not valid integers")
                    sys.exit(0)

                if not (a >= 2 and b >= 2 and c >= 2):
                    print(f"Wrong Answer: Test case {i+1}, numbers must be >= 2")
                    sys.exit(0)
                
                if not (a != b and a != c and b != c):
                    print(f"Wrong Answer: Test case {i+1}, numbers must be distinct")
                    sys.exit(0)

                if a * b * c != n:
                    print(f"Wrong Answer: Test case {i+1}, product is not equal to n")
                    sys.exit(0)
            else:
                print(f"Wrong Answer: Test case {i+1}, unexpected output format")
                sys.exit(0)

        if user_line_idx != len(user_lines):
            print("Wrong Answer: Extra output at the end")
            sys.exit(0)

        print("Accepted")
        sys.exit(0)

    except (IOError, ValueError) as e:
        print(f"Wrong Answer: {e}")
        sys.exit(0)

if __name__ == "__main__":
    main()
