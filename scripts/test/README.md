
# Problem Validation Scripts

This directory contains a suite of Python scripts designed to validate the structure and content of problem data before it is added to the repository. This includes ensuring correct LaTeX syntax for mathematical expressions within problem descriptions. It also contains a `utils` directory with helper functions for path resolution.

**Important:** All commands must be run from the root of the `DATA` directory.



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

### `test_description_md.py`

Validates the `description.md` file for a specific problem, ensuring it's not empty.

**Usage:**

```bash
python -m scripts.test.test_description_md <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_description_md P1
```

### `test_input_md.py`

Validates the `input.md` file for a specific problem, ensuring it's not empty.

**Usage:**

```bash
python -m scripts.test.test_input_md <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_input_md P1
```

### `test_output_md.py`

Validates the `output.md` file for a specific problem, ensuring it's not empty.

**Usage:**

```bash
python -m scripts.test.test_output_md <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_output_md P1
```

### `test_constraints_md.py`

Validates the `constraints.md` file for a specific problem, ensuring it's not empty and uses correct LaTeX syntax for mathematical expressions.

**Usage:**

```bash
python -m scripts.test.test_constraints_md <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_constraints_md P1
```

### `test_notes_md.py`

Validates the `notes.md` file for a specific problem. This file is optional and can be empty or missing. If present, it should use correct LaTeX syntax for mathematical expressions (rendered with KaTeX).

**Usage:**

```bash
python -m scripts.test.test_notes_md <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_notes_md P1
```

### `test_header_md.py`

Validates the `header.md` file for a specific problem. This file is optional and can be empty or missing.

**Usage:**

```bash
python -m scripts.test.test_header_md <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_header_md P1
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

### `test_solution_md.py`

Validates the `solution.md` file for a specific problem.

**Usage:**

```bash
python -m scripts.test.test_solution_md <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_solution_md P1
```

## Individual Test Scripts

### `test_problem_submissions_structure.py`

Validates the structure and content of submission files within a problem's `submissions` directory.

**Usage:**

```bash
python -m scripts.test.test_problem_submissions_structure <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_problem_submissions_structure P1
```

### `test_solution_files_presence.py`

Validates the presence of solution files (e.g., `solution.py`, `solution.cpp`, `solution.c`) for a specific problem.

**Usage:**

```bash
python -m scripts.test.test_solution_files_presence <problem_id>
```

**Example:**

```bash
python -m scripts.test.test_solution_files_presence P1
```

### `test_user_structure.py`

Validates the structure and content of user directories, including `meta.json` and submission files.

**Usage:**

```bash
python -m scripts.test.test_user_structure [user_id]
```

**Example:**

```bash
python -m scripts.test.test_user_structure U1
```

## Solution Test Runners

These scripts run the provided solutions against the problem's test cases and report the results. They now also include sample test cases and provide detailed input, actual output, and expected output for each test.

### `run_py_solution.py`

Runs the Python solution for a specific problem against its test cases.

**Usage:**

```bash
python -m scripts.test.run_py_solution <problem_id>
```

**Example:**

```bash
python -m scripts.test.run_py_solution P1
```

### `run_c_solution.py`

Compiles and runs the C solution for a specific problem against its test cases.

**Usage:**

```bash
python -m scripts.test.run_c_solution <problem_id>
```

**Example:**

```bash
python -m scripts.test.run_c_solution P1
```

### `run_cpp_solution.py`

Compiles and runs the C++ solution for a specific problem against its test cases.

**Usage:**

```bash
python -m scripts.test.run_cpp_solution <problem_id>
```

**Example:**

```bash
python -m scripts.test.run_cpp_solution P1
```
p_solution P1
```
