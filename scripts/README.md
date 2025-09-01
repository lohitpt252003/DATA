
# Problem Data Validation Scripts

This directory contains scripts for validating the problem data in this repository.

## Main Validator

The `main_validator.py` script is the primary script for validating a problem. It runs a complete suite of tests for a given `problem_id` to ensure that the problem's data is well-formed and complete.

### Usage

To run the main validator, execute the following command from the root of the `DATA` directory:

```bash
python -m scripts.main_validator <problem_id>
```

**Example:**

```bash
python -m scripts.main_validator P1
```

## Individual Tests

For more granular testing, you can run individual validation scripts for specific components of the problem data. These scripts are located in the `test/` subdirectory.

For detailed instructions on how to run the individual tests, please refer to the [README.md in the test directory](./test/README.md).
