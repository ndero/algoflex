import sys

test_cases = [
    # Minimal edge cases
    (([1],), []),
    (([1, 1],), [2]),
    # Small basic cases
    (([1, 2, 3, 4],), []),
    (([4, 3, 2, 7, 8, 2, 3, 1],), [5, 6]),
    (([1, 1],), [2]),
    (([2, 2],), [1]),
    # Single missing
    (([1, 2, 2, 4],), [3]),
    (([2, 3, 4, 4, 5],), [1]),
    (([1, 2, 3, 3, 5],), [4]),
    (([1, 1, 2, 3, 4],), [5]),
    # Multiple missing
    (([2, 2, 3, 3],), [1, 4]),
    (([4, 4, 4, 4],), [1, 2, 3]),
    (([1, 3, 3, 5, 5],), [2, 4]),
    (([2, 2, 2, 2, 5, 5],), [1, 3, 4, 6]),
    # Missing at boundaries
    (([2, 3, 4, 5, 5],), [1]),
    (([1, 1, 2, 3, 4],), [5]),
    (([5, 4, 3, 2, 2],), [1]),
    # All same number
    (([3, 3, 3],), [1, 2]),
    (([1, 1, 1, 1],), [2, 3, 4]),
    # Already sorted with gaps
    (([1, 2, 4, 6, 6, 6, 7],), [3, 5]),
    (([1, 3, 5, 7, 7, 7, 7],), [2, 4, 6]),
    # Reverse order with duplicates
    (([5, 4, 3, 2, 2],), [1]),
    (([6, 5, 4, 3, 2, 2],), [1]),
    # Random distributions
    (([3, 1, 2, 5, 3],), [4]),
    (([6, 1, 1, 2, 4, 6],), [3, 5]),
    (([7, 3, 2, 1, 8, 2, 3, 1],), [4, 5, 6]),
    # Stress: large n, no missing
    ((list(range(1, 100_001)),), []),
    # Stress: large n, one missing
    (
        (list(range(1, 100_001))[:-1] + [99_999],),
        [100_000],
    ),
    # Stress: large n, missing first
    (
        (list(range(2, 100_001)) + [100_000],),
        [1],
    ),
    # Stress: half missing
    (
        (list(range(1, 50_001)) + list(range(1, 50_001)),),
        list(range(50_001, 100_001)),
    ),
    # Stress: heavy duplication
    (
        ([50_000] * 100_000,),
        [i for i in range(1, 100_001) if i != 50_000],
    ),
    # Long gap in middle
    (
        (list(range(1, 40_001)) + [40_000] * 20_000 + list(range(60_001, 100_001)),),
        list(range(40_001, 60_001)),
    ),
    # Patterned duplicates
    (
        ([i if i % 2 == 0 else 2 for i in range(1, 21)],),
        [i for i in range(1, 21) if i % 2 != 0 and i != 2],
    ),
    # Repeated small subset
    (
        ([1, 2, 3, 4, 5] * 20_000,),
        list(range(6, 100_001)),
    ),
    # Sparse unique values
    (
        ([100_000] * 99_999 + [1],),
        list(range(2, 100_000)),
    ),
    # Extra edge cases
    # Only the first value is present repeatedly.
    (([1, 1, 1, 1, 1],), [2, 3, 4, 5]),
    # Only the last value is present repeatedly.
    (([5, 5, 5, 5, 5],), [1, 2, 3, 4]),
    # Two values duplicated, everything else missing.
    (([1, 5, 1, 5, 1],), [2, 3, 4]),
    # Alternating duplicates.
    (([1, 2, 1, 2, 1, 2],), [3, 4, 5, 6]),
    # Missing values are spread throughout the range.
    (([1, 3, 5, 7, 9, 9, 9, 9, 9],), [2, 4, 6, 8]),
    # Values appear in a completely different order.
    (([5, 1, 4, 2, 5],), [3]),
    # One missing value with many irrelevant duplicates.
    (([1, 2, 3, 3, 3, 4, 4, 5],), [6, 7, 8]),
    # Missing all but one value.
    (([7, 7, 7, 7, 7, 7, 7],), [1, 2, 3, 4, 5, 6]),
]

if __name__ == "__main__":
    sys.exit(run_python_tests(find_missing, test_cases))  # type: ignore  # noqa: F821
