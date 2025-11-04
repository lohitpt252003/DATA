import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n % 2 != 0:
        return n * (n - 1) * (n - 2)
    else:
        if n % 3 != 0:
            return n * (n - 1) * (n - 3)
        else:
            return (n - 1) * (n - 2) * (n - 3)

def main():
    if len(sys.argv) != 3:
        print("Usage: python validator.py <user_output_file> <test_input_file>")
        sys.exit(1)

    user_output_filename = sys.argv[1]
    correct_input_filename = sys.argv[2]

    try:
        with open(correct_input_filename, 'r') as f:
            n = int(f.read().strip())
        
        with open(user_output_filename, 'r') as f:
            user_lcm = int(f.read().strip())

        correct_lcm = solve(n)

        if user_lcm == correct_lcm:
            print("Accepted")
        else:
            print("Wrong Answer")
        
        sys.exit(0)

    except (IOError, ValueError):
        print("Wrong Answer")
        sys.exit(0)

if __name__ == "__main__":
    main()
