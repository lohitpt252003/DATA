import sys
from collections import Counter


def fail(msg: str = "Wrong Answer") -> None:
    print(msg)
    sys.exit(0)


def main() -> None:
    if len(sys.argv) != 3:
        fail()

    # Contract: argv[1] -> user_output_file, argv[2] -> test_input_file
    out_path, inp_path = sys.argv[1], sys.argv[2]

    try:
        # Read input and parse t, then for each test read n and array
        with open(inp_path, "r", encoding="utf-8") as f:
            in_tokens = f.read().strip().split()
        if not in_tokens:
            fail()

        ptr = 0
        try:
            t = int(in_tokens[ptr]); ptr += 1
        except Exception:
            fail()
        if t <= 0:
            fail()

        arrays = []
        for _ in range(t):
            if ptr >= len(in_tokens):
                fail()
            try:
                n = int(in_tokens[ptr]); ptr += 1
            except Exception:
                fail()
            if n < 1:
                fail()
            if ptr + n > len(in_tokens):
                fail()
            try:
                arr = [int(x) for x in in_tokens[ptr:ptr+n]]
            except Exception:
                fail()
            ptr += n
            arrays.append(arr)

        # Read user output tokens, then split sequentially per test case
        with open(out_path, "r", encoding="utf-8") as f:
            out_tokens_all = f.read().strip().split()
        try:
            out_ints = [int(x) for x in out_tokens_all]
        except Exception:
            fail()

        optr = 0
        for arr in arrays:
            n = len(arr)
            if optr + n > len(out_ints):
                fail()
            out_arr = out_ints[optr:optr+n]
            optr += n
            # Check multiset equality
            if Counter(out_arr) != Counter(arr):
                fail()
            # Check non-ascending order
            if out_arr != sorted(out_arr, reverse=True):
                fail()

        # No extra tokens allowed
        if optr != len(out_ints):
            fail()

        print("Accepted")
    except Exception:
        fail()


if __name__ == "__main__":
    main()
