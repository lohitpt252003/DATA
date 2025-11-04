# Generic Validator Blueprint
import sys

def validate(user_output, test_input):
    """
    Compares the user's output with the expected output.

    Args:
        user_output (str): The content of the user's output file.
        test_input (str): The content of the test input file.
    """
    # --- Your validation logic here ---
    # Example: Check if user's output matches the test input exactly
    if user_output.strip() == test_input.strip():
        print("Accepted")
    else:
        print("Wrong Answer")

def main():
    """
    Main function to read files and run validation.
    """
    if len(sys.argv) != 3:
        print("Usage: python validator.py <user_output_file> <test_input_file>")
        sys.exit(1)

    user_output_filename = sys.argv[1]
    test_input_filename = sys.argv[2]

    try:
        with open(user_output_filename, 'r') as f:
            user_output_content = f.read()
        
        with open(test_input_filename, 'r') as f:
            test_input_content = f.read()

        validate(user_output_content, test_input_content)
        sys.exit(0)

    except IOError:
        print("Validator Error: Could not read files.")
        sys.exit(1)
    except Exception as e:
        print(f"Validator Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
