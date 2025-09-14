
# Problem Data Validation Scripts

This directory contains scripts for validating the problem data in this repository.

## Main Validator

The `main_validator.py` script is the primary script for validating a problem. It runs a complete suite of tests for a given `problem_id` to ensure that the problem's data is well-formed and complete. This includes validating individual markdown files (description, input, output, constraints, notes, header) within the problem's `details` directory, as well as running the provided solutions against both the main test cases and sample test cases.

The validator will run the tests sequentially and will exit immediately if any test fails, printing a clear message indicating which test failed.

### Usage

To run the main validator, execute the following command from the root of the `DATA` directory:

```bash
python -m scripts.main_validator <problem_id>
```

**Example:**

```bash
python -m scripts.main_validator P1
```

### Output

The script will print the progress of the validation, indicating whether each test passed or failed. For solution tests, it will also display the input, the actual output from the solution, and the expected output for each test case (including samples). If a test fails, the script will print the error message from the test and exit. If all tests pass, it will print a success message.


