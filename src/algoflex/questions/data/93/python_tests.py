import sys

test_cases = [
    # Boundary / smallest values
    [(0,), 0],
    [(1,), 1],
    [(2,), 1],
    [(3,), 1],
    [(4,), 2],
    # Small perfect squares
    [(9,), 3],
    [(16,), 4],
    [(25,), 5],
    [(36,), 6],
    [(49,), 7],
    [(64,), 8],
    [(81,), 9],
    [(100,), 10],
    # Values between perfect squares
    [(5,), 2],
    [(6,), 2],
    [(7,), 2],
    [(8,), 2],
    [(10,), 3],
    [(15,), 3],
    [(17,), 4],
    [(24,), 4],
    [(26,), 5],
    [(35,), 5],
    # Larger perfect squares
    [(121,), 11],
    [(144,), 12],
    [(1000,), 31],
    [(1024,), 32],
    [(10000,), 100],
    [(1_000_000,), 1000],
    # Large non-perfect squares
    [(2_147_395_599,), 46339],
    [(2_147_483_646,), 46340],
    # Maximum 32-bit signed integer
    [(2_147_483_647,), 46340],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(sqrt_x, test_cases))  # noqa: F821 # type: ignore
