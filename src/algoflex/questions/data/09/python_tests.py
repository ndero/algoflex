import sys

test_cases = [
    [(100,), 25],
    [(1_000,), 168],
    [(10_000,), 1229],
    [(100_000,), 9592],
    [(2,), 1],
    [(3,), 2],
    [(1,), 0],
    [(1_000_000,), 78498],
    # Edge cases
    [(0,), 0],  # Zero
    [(4,), 2],  # First composite
    [(5,), 3],  # Prime after first composite
    [(6,), 3],  # Composite
    [(10,), 4],  # Small number
    [(999_983,), 78498],  # Large prime
]

if __name__ == "__main__":
    sys.exit(run_python_tests(count_primes, test_cases))  # type: ignore  # noqa: F821
