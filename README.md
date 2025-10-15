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
        - `C0A/`, `C0B/`, etc.: Each problem has its own directory, named with a unique problem ID in the format `C<contest_id><problem_letter>` (e.g., `C0A`, `C1C`, `C1000F`). If there are more than 26 problems in a contest, the problem letters will continue as `AA`, `AB`, etc. (e.g., `C1AA`, `C1AB`).
            - `meta.json`: Contains metadata specific to the problem (e.g., `id`, `title`, `timeLimit`, `memoryLimit`, `number_of_submissions`, `contest_id`).
            - ... (other problem files like `details/`, `testcases/`, etc.)
    - `description.md`: Markdown description of the contest.
    - `theory.md`: Markdown explanation of the theory behind the contest problems.
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

The data is stored in a hierarchical file system structure. Problems are now organized within their respective contests. The problem ID format is `C<contest_id><problem_letter>` (e.g., `C0A`, `C1C`, `C1000F`). If there are more than 26 problems in a contest, the problem letters will continue as `AA`, `AB`, etc. (e.g., `C1AA`, `C1AB`).

## Validation and Solution Scripts

The `scripts/` directory contains validation scripts. For detailed instructions, refer to the [README.md in the scripts directory](./scripts/README.md).