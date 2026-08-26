import sys

# Create instances
arr1 = [1, 3, 7, 7, 7, 3, 4, 1, 7]
rf1 = RangeFreq(arr1)  # type: ignore # noqa: F821

arr2 = [i for i in range(100_000)]
rf2 = RangeFreq(arr2)  # type: ignore # noqa: F821

arr3 = [i for i in range(1, 100_000)] + [22] * 50_000 + [-15] * 100_000
rf3 = RangeFreq(arr3)  # type: ignore # noqa: F821

# Store instances in a list for the lambda to access by index
objects = [rf1, rf2, rf3]

# Test cases: [(object_index, left, right, value), expected]
test_cases = [
    [(0, 2, 4, 7), 3],
    [(0, 0, 8, 1), 2],
    [(0, 4, 7, 4), 1],
    [(0, 2, 4, 9), 0],
    [(0, 8, 8, 7), 1],
    [(1, 0, 100_000, 897), 1],
    [(1, 0, 100_000, 0), 1],
    [(1, 0, 100_000, 99_999), 1],
    [(1, 0, 10, 7), 1],
    [(1, 50_000, 50_000, 50_000), 1],
    [(2, 0, 250_000, 0), 0],
    [(2, 0, 250_000, 22), 50_001],
    [(2, 0, 250_000, -15), 100_000],
    [(2, 100_000, 150_000, 22), 49_999],
    [(2, 100_000, 150_005, -15), 7],
]


if __name__ == "__main__":
    sys.exit(
        run_python_tests(  # noqa: F821 # type: ignore
            lambda idx, left, right, value: objects[idx].query(left, right, value),
            test_cases,
        )
    )
