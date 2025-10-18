# Blueprint

This directory contains the blueprints for creating new contests, problems, and solutions for the Annaforces platform. These blueprints provide a consistent starting point for new content.

## Contest Blueprint (`contest/`)

The `contest` blueprint contains the following files and directories:

-   `meta.json`: A JSON file with placeholder metadata for the contest, including ID, name, description, duration, problems, and authors.
-   `contest.md`: A Markdown file for the main contest description.
-   `rules.md`: A Markdown file for the contest rules.
-   `theory.md`: A Markdown file for any theoretical concepts relevant to the contest.
-   `problems/`: A placeholder directory for the contest's problems.

## Problem Blueprint (`problem/`)

The `problem` blueprint contains the following files and directories:

-   `meta.json`: A JSON file with placeholder metadata for the problem, including ID, title, time/memory limits, tags, authors, and difficulty.
-   `problem.md`: A Markdown file for the problem description, input/output format, constraints, and notes.
-   `validator.py`: A script that acts as a judge for the problem. It takes a user's output file and the correct output file as arguments and compares them to produce a verdict (e.g., "Accepted", "Wrong Answer").
-   `samples/`: A directory for sample test cases.
-   `testcases/`: A directory for the main test cases.

## Solution Blueprint (`solution/`)

The `solution` blueprint provides templates for writing problem solutions in various formats:

-   `solution.c`: A template for a C solution.
-   `solution.cpp`: A template for a C++ solution.
-   `solution.py`: A template for a Python solution.
-   `solution.md`: A Markdown template for a detailed explanation of the solution, including the approach, complexity analysis, and code snippets.
-   `solution.tex`: A LaTeX template for creating a high-quality PDF version of the solution explanation.

## Content Guidelines

### Mathematical Notation

When writing problem descriptions, constraints, or any other content that includes mathematical formulas, please use KaTeX for rendering. Enclose inline math expressions in single dollar signs (`$`) and block math expressions in double dollar signs (`$$`).

For example:
- Inline: `$x^2 + y^2 = z^2$`
- Block: `$$ \sum_{i=1}^{n} i = \frac{n(n+1)}{2} $$`
