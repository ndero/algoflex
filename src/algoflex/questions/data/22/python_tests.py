import sys

test_cases = [
    [(0,), 0],
    [(1,), 1],
    [(2,), 2],
    [(10,), 89],
    [(51,), 32951280099],
    # Edge cases
    [(3,), 3],
    [(4,), 5],
    [(5,), 8],
    [(46,), 2971215073],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(climb_stairs, test_cases))  # type: ignore  # noqa: F821
