import sys

if __name__ == '__main__':
    user_output = sys.argv[1]

    if user_output.strip().lower() == "prime":
        print("Accepted")
    else:
        print("Wrong Answer")
