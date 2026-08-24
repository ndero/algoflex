import sys

test_cases = [
    # Minimal edge cases
    [(1,), 1],
    [(2,), 0],
    [(3,), 0],
    # Small cases
    [(4,), 2],
    [(5,), 10],
    # Medium cases
    [(6,), 4],
    [(7,), 40],
    # Large cases
    [(8,), 92],
    [(9,), 352],
    # Edge case, n = 0
    [(0,), 1],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(n_queens, test_cases))  # type: ignore  # noqa: F821
