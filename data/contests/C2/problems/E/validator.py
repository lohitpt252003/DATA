import sys

def validate():
    user_output_file = sys.argv[1]
    test_input_file = sys.argv[2]

    with open(user_output_file, 'r') as f:
        user_output = f.read().strip().split('\n')

    with open(test_input_file, 'r') as f:
        test_input_lines = f.read().strip().split('\n')

    t = int(test_input_lines[0])
    expected_outputs = []
    for i in range(1, t + 1):
        n = int(test_input_lines[i])
        expected_outputs.append(str(n // 2))

    if len(user_output) != len(expected_outputs):
        print("Wrong Answer")
        return

    for i in range(len(user_output)):
        if user_output[i].strip() != expected_outputs[i].strip():
            print("Wrong Answer")
            return

    print("Accepted")

if __name__ == '__main__':
    validate()