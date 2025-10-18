import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Validate the output of a user\'s submission.')
    parser.add_argument('user_output_file', help='The path to the user\'s output file.')
    parser.add_argument('correct_output_file', help='The path to the correct output file.')
    args = parser.parse_args()

    try:
        with open(args.user_output_file, 'r', encoding='utf-8') as f:
            user_output = f.read().strip()
    except FileNotFoundError:
        print("Wrong Answer: User output file not found.")
        sys.exit(1)

    try:
        with open(args.correct_output_file, 'r', encoding='utf-8') as f:
            correct_output = f.read().strip()
    except FileNotFoundError:
        print("Internal Error: Correct output file not found.")
        sys.exit(1)

    # Case-insensitive comparison
    if user_output.lower() == correct_output.lower():
        print("Accepted")
    else:
        print("Wrong Answer")

if __name__ == "__main__":
    main()