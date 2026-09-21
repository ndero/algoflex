import sys

test_cases = [
    # Minimum length
    [([1],), [1, 1]],
    # Two elements
    [([1, 2],), [1, 2, 1, 2]],
    # Three elements
    [([1, 2, 3],), [1, 2, 3, 1, 2, 3]],
    # All elements the same
    [([5, 5, 5, 5],), [5, 5, 5, 5, 5, 5, 5, 5]],
    # Repeated pattern
    [([1, 2, 1, 2],), [1, 2, 1, 2, 1, 2, 1, 2]],
    # Already symmetric
    [([1, 2, 3, 2, 1],), [1, 2, 3, 2, 1, 1, 2, 3, 2, 1]],
    # Minimum and maximum allowed values
    [([1, 1000],), [1, 1000, 1, 1000]],
    # Maximum value repeated
    [([1000, 1000, 1000],), [1000, 1000, 1000, 1000, 1000, 1000]],
    # Mixed values
    [([7, 42, 999, 13, 500],), [7, 42, 999, 13, 500, 7, 42, 999, 13, 500]],
    # Increasing sequence
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],),
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ],
    # Decreasing sequence
    [
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1],),
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    ],
    # Larger input
    [
        ([i for i in range(1, 101)],),
        [i for i in range(1, 101)] * 2,
    ],
    # Maximum length: all minimum values
    [
        ([1] * 1000,),
        [1] * 2000,
    ],
    # Maximum length: all maximum values
    [
        ([1000] * 1000,),
        [1000] * 2000,
    ],
    # Maximum length: mixed values
    [
        ([i % 1000 + 1 for i in range(1000)],),
        [i % 1000 + 1 for i in range(1000)] * 2,
    ],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(concatenate, test_cases))  # type: ignore  # noqa: F821
