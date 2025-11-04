# Data Directory Structure

This document outlines the structure of the `data` directory, which serves as the database for this project.

## Overview

The `data` directory is organized into the following main subdirectories:

- `contests`: Contains information about contests and the problems within them.
- `submissions`: Contains user submissions for the problems.
- `users`: Contains information about the users.
- `solutions`: Contains official solutions for the problems.

## Directory Structure

```
E:\NEW\DATA\
├───.git\
├───data\
│   ├───contests\
│   │   ├───C0\
│   │   │   ├───meta.json
│   │   │   └───problems\
│   │   │       ├───C0-A\
│   │   │       └───C0-B\
│   │   ├───C1\
│   │   └───...
│   ├───submissions\ ...
│   ├───users\ ...
│   └───solutions\ ...
├───blueprint\
│   ├───problem\
│   └───contest\
├───scripts\
└───README.md
```

### `blueprint`

The `blueprint` directory contains templates for creating new problems, solutions, and contests.

- `problem`: Contains a template for a new problem.
- `solution`: Contains a template for a new solution.
- `contest`: Contains a template for a new contest.

### `contests`

- `index.json`: A JSON file that contains a list of all contests and their metadata.
- `C0/`, `C1/`, etc.: Each contest has its own directory, named with a unique contest ID (e.g., `C0`).
    - `meta.json`: Contains metadata specific to the contest (e.g., `id`, `name`, `startTime`, `endTime`, `problems`, `authors`).
    - `problems/`: A directory containing the problems for this contest.
        - `A/`, `B/`, etc.: Each problem has its own directory within the contest's `problems` directory, named with a problem letter (e.g., `A`, `B`, `C`). If there are more than 26 problems, the folder names will continue as `AA`, `AB`, etc. The `id` field in the problem's `meta.json` file should be in the format `C<contest_id><problem_letter>` (e.g., `C1A`, `C1AA`).
            - `meta.json`: Contains metadata specific to the problem (e.g., `id`, `title`, `timeLimit`, `memoryLimit`, `number_of_submissions`, `contest_id`).
            - ... (other problem files like `details/`, `testcases/`, etc.)
    -   `contest.md`: A Markdown file containing the contest description, rules, and theory.
    - `participants.json`: Stores a list of users registered for the contest.
    - `leaderboard.json`: Stores the current standings of the contest.

### `submissions`

- `meta.json`: A JSON file that contains the total number of submissions.
- `S1/`, `S2/`, etc.: Each submission has its own directory, named with a unique submission ID (e.g., `S1`).
    - `code.c`, `code.cpp`, or `code.py`: The source code of the submission.
    - `meta.json`: Contains metadata about the submission.

### `users`

- `index.json`: A JSON file that contains a list of all users.
- `<username>/`: Each user has their own directory, named with their unique `username`.
    - `meta.json`: Contains metadata specific to the user.
    - `submissions/`: A directory containing references to submissions made by this user.

### `solutions`

- `C0-A/`, `C0-B/`, etc.: Each problem has a directory containing its official solutions, named with the problem ID.
    - `solution.py`, `solution.cpp`, `solution.c`: The solution code in different languages.
    - `solution.md`: An explanation of the solution approach.

## General Structure

The data is stored in a hierarchical file system structure. Problems are now organized within their respective contests. The problem folder is named with a letter (e.g., `A`, `B`, `C`). If there are more than 26 problems, the folder names will continue as `AA`, `AB`, etc. The problem `id` in the `meta.json` file is in the format `C<contest_id><problem_letter>` (e.g., `C1A`, `C1AA`).

## Validation and Solution Scripts

The `scripts/` directory contains validation scripts. For detailed instructions, refer to the [README.md in the scripts directory](./scripts/README.md).

### Problem-Specific Validator (`validator.py`)

Each problem now has its own `validator.py` script located in the problem's directory (e.g., `data/contests/C1/problems/A/validator.py`). This script acts as a **custom judge** for the problem.

Its role is to:

1.  Take a user's output (as a string) and the path to the input file as command-line arguments.
2.  Compare the user's output with the correct answer (which it derives from the input).
3.  Print a verdict, such as "Accepted" or "Wrong Answer". This script is executed by the `judge_service` (part of the backend) which communicates with the code execution engine's `/api/validate` endpoint.

### Test Cases

Test cases for each problem are now stored as `.in` files (e.g., `1.in`, `2.in`). The `judge_service` will run the user's code with the content of these `.in` files and then use the problem's `validator.py` to determine the correctness of the output.