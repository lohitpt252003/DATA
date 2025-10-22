import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    user_output = sys.argv[1]
    input_file = sys.argv[2]

    with open(input_file, 'r') as f:
        n = int(f.read().strip())

    if is_prime(n):
        correct_output = "Prime"
    else:
        correct_output = "Not Prime"

    if user_output.strip().lower() == correct_output.lower():
        print("Accepted")
    else:
        print("Wrong Answer")