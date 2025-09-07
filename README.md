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
│   ├───problems\
│   │   ├───index.json
│   │   ├───P1\
│   │   │   ├───meta.json
│   │   │   ├───problem.md
│   │   │   ├───submissions\
│   │   │   │   ├───S1.json
│   │   │   │   └───S2.json
│   │   │   └───testcases\
│   │   │       ├───1.in
│   │   │       ├───1.out
│   │   │       ├───2.in
│   │   │       └───2.out
│   │   └───P2\
│   │       ├───meta.json
│   │       ├───problem.md
│   │       ├───submissions\
│   │       │   ├───S1.json
│   │       │   └───S2.json
│   │       └───testcases\
│   │           ├───1.in
│   │           ├───1.out
│   │           ├───2.in
│   │           ├───2.out
│   │           ├───3.in
│   │           └───3.out
│   ├───submissions\
│   │   ├───S1\
│   │   │   ├───code.cpp
│   │   │   └───meta.json
│   │   ├───S2\
│   │   │   ├───code.py
│   │   │   └───meta.json
│   │   ├───S3\
│   │   │   ├───code.py
│   │   │   └───meta.json
│   │   └───S4\
│   │       ├───code.py
│   │       └───meta.json
│   ├───users\
│   │   ├───index.json
│   │   ├───U1\
│   │   │   ├───meta.json
│   │   │   └───submissions\
│   │   │       ├───S1.json
│   │   │       └───S2.json
│   │   └───U2\
│   │       ├───meta.json
│   │       └───submissions\
│   │           ├───S1.json
│   │           └───S2.json
│   └───solutions\
│       ├───P1\
│       │   ├───solution.c
│   │   │   ├───solution.cpp
│   │   │   ├───solution.md
│   │   │   └───solution.py
│       └───P2\
│           ├───solution.c
│           ├───solution.cpp
│           ├───solution.md
│           └───solution.py
├───scripts\
│   ├───main_validator.py
│   └───test\
│       ├───run_c_solution.py
│       ├───run_cpp_solution.py
│       ├───run_py_solution.py
│       ├───test_index.py
│       ├───test_md.py
│       ├───test_meta.py
│       ├───test_solution_md.py
│       └───test_testcases.py
├───LICENSE
└───README.md
```

### `problems`

- `index.json`: A JSON file that contains a list of all problems and their metadata, such as title, difficulty, tags, and authors.
- `P1/`, `P2/`, etc.: Each problem has its own directory, named with a unique problem ID (e.g., `P1`). **Here, `P` stands for "problem" and the number is the `problem_id`.**
    - `meta.json`: Contains metadata specific to the problem.
    - `problem.md`: The problem description in Markdown format.
    - `submissions/`: A directory containing submissions for this problem.
    - `testcases/`: A directory containing test cases for this problem.

### `submissions`

- `meta.json`: A JSON file that contains the total number of submissions.
- `S1/`, `S2/`, etc.: Each submission has its own directory, named with a unique submission ID (e.g., `S1`). **Here, `S` stands for "submission" and the number is the `submission_id`.**
    - `code.c`, `code.cpp`, or `code.py`: The source code of the submission with the appropriate file extension.
    - `meta.json`: Contains metadata about the submission, such as the user who submitted it, the problem it's for, the submission time, status, and detailed test results.

### `users`

- `index.json`: A JSON file that contains a list of all users and their metadata, such as username, name, and email.
- `U1/`, `U2/`, etc.: Each user has their own directory, named with a unique user ID (e.g., `U1`). **Here, `U` stands for "user" and the number is the `user_id`.**
    - `meta.json`: Contains metadata specific to the user.
    - `submissions/`: A directory containing submissions made by this user.

### `solutions`

- `P1/`, `P2/`, etc.: Each problem has a directory containing its official solutions.
    - `solution.py`, `solution.cpp`, `solution.c`: The solution code in different languages.
    - `solution.md`: An explanation of the solution approach.

## General Structure

The data is stored in a hierarchical file system structure, with each directory representing an entity (e.g., a problem, a submission, a user) and JSON files within those directories storing metadata. This approach allows for a simple, human-readable database that can be easily managed and version-controlled.

The use of `index.json` files in the `problems` and `users` directories provides a quick way to get a list of all items without having to traverse the entire directory structure. The individual entity directories (e.g., `P1`, `S1`, `U1`) contain the specific data for that entity.

This structure is designed to be easily extensible. Problems are primarily added and managed manually. To add a new problem, you would create a new directory with a unique problem ID (e.g., `P3`) under `data/problems/` and populate it with the necessary `meta.json`, `problem.md`, and `testcases` files. This manual approach ensures direct control over problem data.

## Validation and Solution Scripts

The `scripts/` directory contains a suite of Python scripts designed to validate the problem data and run official solutions against test cases. The main entry point is `main_validator.py`.

For detailed instructions on how to use these scripts, please refer to the [README.md in the scripts directory](./scripts/README.md).
