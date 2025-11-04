import sys


def fail(msg: str = "Wrong Answer") -> None:
    print(msg)
    sys.exit(0)


def main() -> None:
    if len(sys.argv) != 3:
        fail()

    # Contract from judge-image-for-annaforces /api/validate:
    # argv[1] -> user_output_file, argv[2] -> test_input_file
    out_path, inp_path = sys.argv[1], sys.argv[2]

    try:
        with open(inp_path, "r", encoding="utf-8") as f:
            in_lines = [ln.strip() for ln in f.read().strip().splitlines()]
        if not in_lines:
            fail()

        try:
            t = int(in_lines[0])
        except Exception:
            fail()

        if t < 0 or len(in_lines) != 1 + t:
            fail()

        ranges = []
        for i in range(t):
            parts = in_lines[1 + i].split()
            if len(parts) != 2:
                fail()
            try:
                a = int(parts[0])
                b = int(parts[1])
            except Exception:
                fail()
            if a > b:
                fail()
            ranges.append((a, b))

        with open(out_path, "r", encoding="utf-8") as f:
            out_lines = [ln.strip() for ln in f.read().strip().splitlines()]

        if len(out_lines) != t:
            fail()

        for i in range(t):
            s = out_lines[i]
            try:
                x = int(s)
            except Exception:
                fail()
            a, b = ranges[i]
            if not (a <= x <= b):
                fail()

        print("Accepted")
    except Exception:
        fail()


if __name__ == "__main__":
    main()
