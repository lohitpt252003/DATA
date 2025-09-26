# Data Directory Structure

This document outlines the structure of the `data` directory, which serves as the database for this project.

## Overview

The `data` directory is organized into three main subdirectories:

- `problems`: Contains information about the coding problems.
- `submissions`: Contains user submissions for the problems.
- `users`: Contains information about the users.
- `solutions`: Contains official solutions for the problems.

## Directory Structure

```
E:\NEW\DATA\
├───.git\
├───data\
│   ├───problems\...
│   ├───submissions\...
│   ├───users\...
│   └───solutions\...
├───models\
│   ├───problems\
│   │   └───problem.py
│   ├───solutions\
│   │   └───solution.py
│   ├───submissions\
│   │   └───submission.py
│   └───users\
│       └───user.py
├───scripts\
│   ├───main_validator.py
│   ├───README.md
│   ├───tests\
│   │   ├───problem\
│   │   │   ├───problem_statement_validator.py
│   │   │   ├───test_constraints_md.py
│   │   │   ├───test_description_md.py
│   │   │   ├───test_header_md.py
│   │   │   ├───test_index.py
│   │   │   ├───test_input_md.py
│   │   │   ├───test_meta.py
│   │   │   ├───test_notes_md.py
│   │   │   ├───test_output_md.py
│   │   │   ├───test_pdf_statement_presence.py
│   │   │   ├───test_problem_submissions_structure.py
│   │   │   ├───test_problem_tex.py
│   │   │   └───test_user_structure.py
│   │   ├───solution\
│   │   │   ├───run_c_solution.py
│   │   │   ├───run_cpp_solution.py
│   │   │   ├───run_py_solution.py
│   │   │   ├───solution_validator.py
│   │   │   ├───test_pdf_solution_presence.py
│   │   │   ├───test_solution_files_presence.py
│   │   │   ├───test_solution_md.py
│   │   │   └───test_solution_tex.py
│   │   ├───model\
│   │   │   ├───model_validator.py
│   │   │   └───test_model_files_presence.py
│   │   └───README.md
│   └───utils\
│       └───data_utils.py
├───LICENSE
└───README.md
```


### `problems`

-   `index.json`: A JSON file that contains a list of all problems and their metadata, such as title, difficulty, tags, and authors.
-   `P1/`, `P2/`, etc.: Each problem has its own directory, named with a unique problem ID (e.g., `P1`). **Here, `P` stands for "problem" and the number is the `problem_id`.**
    -   `meta.json`: Contains metadata specific to the problem (e.g., `id`, `title`, `timeLimit`, `memoryLimit`, `number_of_submissions`, `has_pdf_statement`, `has_pdf_solution`).
    -   `problem.tex`: The LaTeX source file for the problem statement.
    -   `details/`: A directory containing detailed problem descriptions, split into multiple Markdown files.
        -   `description.md`: The main problem statement.
        -   `input.md`: Description of the input format.
        -   `output.md`: Description of the output format.
        -   `constraints.md`: Constraints for the problem.
        -   `notes.md`: Any additional notes or clarifications (optional).
        -   `header.md`: Additional header information (optional).
        -   `statement.pdf`: The compiled PDF version of the problem statement (optional, indicated by `has_pdf_statement` in `meta.json`).
        -   `samples/`: A directory containing sample input and output files.
            -   `1.in`, `2.in`, etc.: Sample input files.
            -   `1.out`, `2.out`, etc.: Corresponding sample output files.
    -   `submissions/`: A directory containing references to submissions made for this problem.
        -   `S1.json`, `S2.json`, etc.: JSON files, each referencing a submission ID and its status for this problem.
    -   `testcases/`: A directory containing test cases for this problem.
        -   `1.in`, `2.in`, etc.: Input files for the test cases.
        -   `1.out`, `2.out`, etc.: Corresponding output files for the test cases.

### `submissions`

-   `meta.json`: A JSON file that contains the total number of submissions.
-   `S1/`, `S2/`, etc.: Each submission has its own directory, named with a unique submission ID (e.g., `S1`). **Here, `S` stands for "submission" and the number is the `submission_id`.**
    -   `code.c`, `code.cpp`, or `code.py`: The source code of the submission with the appropriate file extension.
    -   `meta.json`: Contains metadata about the submission, such as the user who submitted it, the problem it's for, the submission time, status (e.g., "Queued", "Running... (Testcase 1)", "Accepted"), and detailed test results.

### `users`

-   `index.json`: A JSON file that contains a list of all users and their metadata, such as username, name, and email.
-   `U1/`, `U2/`, etc.: Each user has their own directory, named with a unique user ID (e.g., `U1`). **Here, `U` stands for "user" and the number is the `user_id`.**
    -   `meta.json`: Contains metadata specific to the user (e.g., `id`, `username`, `name`, `email`, `bio`, `joined`, `number_of_submissions`, `attempted`, `solved`, `not_solved`). `attempted`, `solved`, and `not_solved` are dictionaries storing problem IDs as keys and timestamps as values, representing the problems the user has attempted, successfully solved, or attempted but not yet solved, respectively.
    -   `submissions/`: A directory containing references to submissions made by this user.
        -   `S1.json`, `S2.json`, etc.: JSON files, each referencing a submission ID and its status for this user.

### `solutions`

-   `P1/`, `P2/`, etc.: Each problem has a directory containing its official solutions.
    -   `solution.py`, `solution.cpp`, `solution.c`: The solution code in different languages.
    -   `solution.md`: An explanation of the solution approach.
    -   `solution.tex`: The LaTeX source file for the solution explanation.
    -   `solution.pdf`: The compiled PDF version of the solution (optional, indicated by `has_pdf_solution` in `problem_id/meta.json`).

## General Structure

The data is stored in a hierarchical file system structure, with each directory representing an entity (e.g., a problem, a submission, a user) and JSON files within those directories storing metadata. This approach allows for a simple, human-readable database that can be easily managed and version-controlled.

The use of `index.json` files in the `problems` and `users` directories provides a quick way to get a list of all items without having to traverse the entire directory structure. The individual entity directories (e.g., `P1`, `S1`, `U1`) contain the specific data for that entity.

This structure is designed to be easily extensible. Problems are primarily added and managed manually. To add a new problem, you would create a new directory with a unique problem ID (e.g., `P3`) under `data/problems/` and populate it with the necessary `meta.json`, `problem.md`, and `testcases` files. This manual approach ensures direct control over problem data. Mathematical expressions within problem descriptions and solutions are written using LaTeX syntax for rendering with KaTeX.

### Detailed Data Subdirectory Contents

#### `data/problems/`

-   `index.json`: Contains metadata for all problems.
-   `P<problem_id>/` (e.g., `P1/`):
    -   `meta.json`: Problem-specific metadata (ID, title, time/memory limits, submission count, PDF flags).
    -   `problem.tex`: LaTeX source for the problem statement.
    -   `details/`:
        -   `description.md`: Problem description in Markdown.
        -   `input.md`: Input format description.
        -   `output.md`: Output format description.
        -   `constraints.md`: Constraints for the problem.
        -   `notes.md`: Optional additional notes.
        -   `header.md`: Optional header information.
        -   `statement.pdf`: Compiled PDF of the problem statement (if `has_pdf_statement` is true).
        -   `samples/`:
            -   `1.in`, `1.out`, etc.: Sample input/output pairs.
    -   `submissions/`:
        -   `S<submission_id>.json`: References to submissions for this problem.
    -   `testcases/`:
        -   `1.in`, `1.out`, etc.: Official test input/output pairs.

#### `data/submissions/`

-   `meta.json`: Global submission metadata (e.g., total submission count).
-   `S<submission_id>/` (e.g., `S1/`):
    -   `code.<ext>`: Submitted source code (e.g., `code.py`, `code.cpp`).
    -   `meta.json`: Submission-specific metadata (user, problem, timestamp, status, test results).

#### `data/users/`

-   `index.json`: Contains metadata for all users.
-   `U<user_id>/` (e.g., `U1/`):
    -   `meta.json`: User-specific metadata (ID, username, name, email, bio, join date, submission count).
    -   `submissions/`:
        -   `S<submission_id>.json`: References to submissions made by this user.

#### `data/solutions/`

-   `P<problem_id>/` (e.g., `P1/`):
    -   `solution.py`, `solution.cpp`, `solution.c`: Official solution code in various languages.
    -   `solution.md`: Markdown explanation of the solution approach.
    -   `solution.tex`: LaTeX source for the solution explanation.
    -   `solution.pdf`: Compiled PDF of the solution (if `has_pdf_solution` is true).

## Validation and Solution Scripts

The `scripts/` directory contains a suite of Python scripts designed to validate the problem data and run official solutions against test cases. The main entry point is `main_validator.py`. These scripts now provide detailed input/output for each test case, including samples, to aid in debugging and understanding.

For detailed instructions on how to use these scripts, please refer to the [README.md in the scripts directory](./scripts/README.md).