import sys

test_cases = [
    [([2, 3, 1, 2, 4, 3], 7), 2],
    [([1, 3, 6, 2, 1], 4), 1],
    [([i for i in range(500_000)], 3_000_000), 7],
    [([i for i in range(100)], 60), 1],
    [([i for i in range(100_000)], 60_000_000), 602],
    [([i for i in range(1_000_000)], 60_000_000), 61],
    [([1, 1, 1, 1, 1], 6), 0],
    [([1], 1), 1],  # Single element, exact match
    [([5, 5, 5, 5], 5), 1],  # All elements >= target
    [([1], 10), 0],  # Single element, impossible
    [([1, 2, 3, 4, 5], 15), 5],  # Entire array needed
    [([49, 1, 49, 1, 49], 50), 2],  # Multiple valid windows
]

if __name__ == "__main__":
    sys.exit(run_python_tests(min_sub_arr_len, test_cases))  # type: ignore  # noqa: F821
