import sys

test_cases = [
    [([13, -1, 8, 12, 3, 9], 12), 3],
    [([13, -1, 8, 12, 3, 9], 2), 0],
    [([13, -1, 8, 12, 3, 9], 10), 0],
    [([1, 4, -5, 5, 10], 5), 3],
    [([13, -1, 8, 12, 3, 9, 7, 5, 9, 10], 75), 1],
    [([13, -1, 8, 12, 3, 9] * 20_000, 12), 60_000],
    [([13, -1, 8, 12, 3, 9, 7, 5, 9, 10] * 10_000, 24), 30_000],
    # Edge cases
    [([], 5), 0],  # Empty array
    [([5], 5), 1],  # Single matching element
    [([1], 5), 0],  # Single non-matching element
    [([0, 0, 0], 0), 6],  # Array of zeros
    [([-1, -2, -3], -3), 2],  # Negative numbers
]

if __name__ == "__main__":
    sys.exit(run_python_tests(count_arrs, test_cases))  # type: ignore  # noqa: F821
