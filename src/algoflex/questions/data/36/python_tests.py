import sys

test_cases = [
    [([2, 4, 8, 9, 12, 13, 16, 18], 18), True],
    [([i for i in range(5_000_000)], 45), True],
    [([i for i in range(5_000_000)], 5_000_000), False],
    [([i for i in range(-1_000_000, 1_000_000)], 0), True],
    [([i for i in range(-1_000_000, 1_000_000)], -223), True],
    [([i for i in range(-1_000_000, 1_000_000, 10)], 33), False],
    # Edge cases
    [([], 1), False],
    [([5], 5), True],
    [([5], 4), False],
    [([1, 2], 1), True],
    [([1, 2], 2), True],
    [([1, 2], 3), False],
    [([-5, -2, 0, 3, 7], -5), True],
    [([-5, -2, 0, 3, 7], 6), False],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(binary_search, test_cases))  # type: ignore  # noqa: F821
