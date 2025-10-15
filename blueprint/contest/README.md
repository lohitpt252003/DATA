# Contest Blueprint

This directory contains a template for creating a new contest.

To create a new contest, copy this directory and rename it to the new contest ID (e.g., `C0`). Then, update the files inside to match the new contest.

The structure of a contest directory is as follows:

-   `contest_details.md`: A Markdown file containing the contest description, rules, and theory.
-   `meta.json`: A JSON file containing metadata about the contest, such as its ID, name, start/end times, and problems (using the format `C<contest_id><problem_letter>`).
-   `participants.json`: A JSON file containing a list of users registered for the contest.