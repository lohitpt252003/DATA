import math
import json

def count_divisors(x: int) -> int:
    """Return number of divisors of x using sqrt(x) method."""
    cnt = 0
    i = 1
    while i * i <= x:
        if x % i == 0:
            cnt += 1 if i * i == x else 2
        i += 1
    return cnt


def validator(input_data: str, expected_output: str, user_output: str):
    """
    Validate whether user_output is correct for given input_data.
    Returns a dict with 'result': True/False and an explanation.
    """

    # Parse input
    lines = input_data.strip().split()
    n = int(lines[0])
    nums = list(map(int, lines[1:]))

    if len(nums) != n:
        return {"result": False, "message": "Input count mismatch."}

    # Compute correct output
    correct = [str(count_divisors(x)) for x in nums]

    # Normalize all outputs
    user_lines = user_output.strip().split()
    if len(user_lines) != len(correct):
        return {
            "result": False,
            "message": f"Expected {len(correct)} lines, got {len(user_lines)}."
        }

    # Compare line by line
    for i, (u, c) in enumerate(zip(user_lines, correct), start=1):
        if u.strip() != c:
            return {
                "result": False,
                "message": f"Mismatch at line {i}: expected {c}, got {u}."
            }

    return {"result": True, "message": "Correct output!"}


if __name__ == "__main__":
    data = json.loads(input())
    res = validator(
        data["input"],
        data.get("expected_output", ""),  # optional
        data["user_output"]
    )
    print(json.dumps(res))
