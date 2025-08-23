# Data Directory Structure

This document outlines the structure of the `data` directory, which serves as the database for this project.

## Overview

The `data` directory is organized into three main subdirectories:

- `problems`: Contains information about the coding problems.
- `submissions`: Contains user submissions for the problems.
- `users`: Contains information about the users.

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
│   └───users\
│       ├───index.json
│       ├───U1\
│       │   ├───meta.json
│   │   │   └───submissions\
│   │   │       ├───S1.json
│   │   │       └───S2.json
│       └───U2\
│           ├───meta.json
│           └───submissions\
│               ├───S1.json
│               └───S2.json
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

- `S1/`, `S2/`, etc.: Each submission has its own directory, named with a unique submission ID (e.g., `S1`). **Here, `S` stands for "submission" and the number is the `submission_id`.**
    - `code.cpp`: The source code of the submission.
    - `meta.json`: Contains metadata about the submission, such as the user who submitted it, the problem it's for, and the submission time.

### `users`

- `index.json`: A JSON file that contains a list of all users and their metadata, such as username and name.
- `U1/`, `U2/`, etc.: Each user has their own directory, named with a unique user ID (e.g., `U1`). **Here, `U` stands for "user" and the number is the `user_id`.**
    - `meta.json`: Contains metadata specific to the user.
    - `submissions/`: A directory containing submissions made by this user.

## General Structure

The data is stored in a hierarchical file system structure, with each directory representing an entity (e.g., a problem, a submission, a user) and JSON files within those directories storing metadata. This approach allows for a simple, human-readable database that can be easily managed and version-controlled.

The use of `index.json` files in the `problems` and `users` directories provides a quick way to get a list of all items without having to traverse the entire directory structure. The individual entity directories (e.g., `P1`, `S1`, `U1`) contain the specific data for that entity.

This structure is designed to be easily extensible. For example, to add a new problem, you would simply create a new directory with a unique problem ID and add the necessary files.
