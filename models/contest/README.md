# Contest Model

This directory contains a template for creating a new contest.

## `meta.json` fields

- `id`: The unique ID of the contest (e.g., "C1").
- `name`: The name of the contest.
- `description`: A brief description of the contest.
- `startTime`: The start time of the contest in ISO 8601 format.
- `endTime`: The end time of the contest in ISO 8601 format.
- `problems`: A list of problem IDs that are part of this contest.
- `authors`: A list of authors of the contest.
- `is_practice`: A boolean flag. If set to `false`, the `theory.md` file will not be loaded. This is useful for non-practice contests where the theory should not be revealed during the contest.
