import sys

test_cases = [
    [(10,), 4],
    [(15,), 6],
    [(5,), 2],
    [(55,), 60],
    [(1_000,), 142_511],
    [(10_000,), 134_235_101],
    # Edge cases
    [(0,), 1],
    [(1,), 1],
    [(2,), 1],
    [(4,), 1],
    [(25,), 13],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(count_ways, test_cases))  # type: ignore  # noqa: F821
