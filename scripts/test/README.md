
# Problem Validation Scripts

This directory contains a suite of Python scripts designed to validate the structure and content of problem data before it is added to the repository.

**Important:** All commands must be run from the root of the `DATA` directory.

## Main Validator

The `main_validator.py` script, located in the parent `scripts/` directory, is the main entry point for validating an entire problem directory. It runs all the individual test scripts for a given `problem_id`.

### Usage

From the `DATA` directory, run the following command:

```bash
python -m scripts.main_validator <problem_id>
```

**Example:**

```bash
python -m scripts.main_validator P1
```

## Individual Test Scripts

You can also run each validation test separately from this `test/` directory. This is useful for debugging a specific part of a problem's data. Remember to run these commands from the `DATA` directory.

### `test_meta.py`

Validates the `meta.json` file for a specific problem.

**Usage:**

```bash
python -m scripts.test.test_meta <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_meta P1
```

### `test_md.py`

Validates the `problem.md` file for a specific problem.

**Usage:**

```bash
python -m scripts.test.test_md <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_md P1
```

### `test_testcases.py`

Validates the `testcases` directory for a specific problem.

**Usage:**

```bash
python -m scripts.test.test_testcases <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_testcases P1
```

### `test_index.py`

Validates the main `index.json` file.

**Usage:**

To validate the entire `index.json` file:

```bash
python -m scripts.test.test_index
```

To validate a specific problem's entry in `index.json`:

```bash
python -m scripts.test.test_index --problem_id <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_index --problem_id P1
```
