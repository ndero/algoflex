import sys

test_cases = [
    # Basic test cases
    (
        ([73, 74, 75, 71, 69, 72, 76, 73],),
        [1, 1, 4, 2, 1, 1, 0, 0],
    ),
    (([30, 40, 50, 60],), [1, 1, 1, 0]),
    (([60, 50, 40, 30],), [0, 0, 0, 0]),
    (([70, 70, 70, 70],), [0, 0, 0, 0]),
    # Edge cases
    (([30],), [0]),
    (([],), []),
    (([30, 31],), [1, 0]),
    (([31, 30],), [0, 0]),
    # Complex patterns
    (
        ([80, 70, 90, 60, 85, 75, 95],),
        [2, 1, 4, 1, 2, 1, 0],
    ),
    (
        ([73, 72, 71, 70, 74, 73, 72, 75],),
        [4, 3, 2, 1, 3, 2, 1, 0],
    ),
    (
        ([40, 45, 50, 55, 50, 45, 40],),
        [1, 1, 1, 0, 0, 0, 0],
    ),
    (
        ([60, 50, 40, 30, 40, 50, 60],),
        [0, 5, 3, 1, 1, 1, 0],
    ),
    (
        ([50, 50, 50, 60, 50, 70],),
        [3, 2, 1, 2, 1, 0],
    ),
    # Special scenarios
    (
        ([100, 50, 51, 52, 53, 54],),
        [0, 1, 1, 1, 1, 0],
    ),
    (
        ([30, 31, 32, 33, 34, 35, 36, 29],),
        [1, 1, 1, 1, 1, 1, 0, 0],
    ),
    (
        ([50, 49, 48, 47, 46, 51],),
        [5, 4, 3, 2, 1, 0],
    ),
    (
        ([90, 50, 91, 51, 92, 52, 93],),
        [2, 1, 2, 1, 2, 1, 0],
    ),
    (([0, 100, 0, 100],), [1, 0, 1, 0]),
    # Stress test 1: strictly increasing
    (
        (list(range(1, 10_001)),),
        [1] * 9_999 + [0],
    ),
    # Stress test 2: strictly decreasing
    (
        (list(range(10_000, 0, -1)),),
        [0] * 10_000,
    ),
    # Stress test 3: constant temperature
    (
        ([70] * 10_000,),
        [0] * 10_000,
    ),
    # Stress test 4: mountain
    (
        (list(range(1, 5_001)) + list(range(5_000, 0, -1)),),
        [1] * 4_999 + [0] * 5_001,
    ),
    # Stress test 5: valley
    (
        (list(range(5_000, 0, -1)) + list(range(1, 5_001)),),
        [0] + list(range(9_998, 0, -2)) + [1] * 4_999 + [0],
    ),
    # Stress test 6: alternating high-low
    (
        ([100 if i % 2 == 0 else 0 for i in range(10_000)],),
        [0 if i % 2 == 0 else 1 for i in range(9_999)] + [0],
    ),
    # Stress test 8: decreasing then one spike
    (
        (list(range(10_000, 0, -1)) + [100_001],),
        list(range(10_000, -1, -1)),
    ),
    # Stress test 9: one warmer day in the middle
    (
        ([10**6] * 5_000 + [10**6 + 1] + [10**6] * 4_999,),
        list(range(5_000, -1, -1)) + [0] * 4_999,
    ),
    # Alternating extreme values
    (
        ([1, 10**6, 2, 10**6 - 1, 3, 10**6 - 2],),
        [1, 0, 1, 0, 1, 0],
    ),
    # All equal except final warmer day.
    (
        ([70] * 10 + [71],),
        list(range(10, 0, -1)) + [0],
    ),
    # Warmer temperature immediately after every day.
    (
        ([1, 2, 3, 4, 5],),
        [1, 1, 1, 1, 0],
    ),
    # No warmer temperature anywhere.
    (
        ([5, 4, 3, 2, 1],),
        [0, 0, 0, 0, 0],
    ),
    # Equal temperatures are NOT warmer.
    (
        ([5, 5, 6],),
        [2, 1, 0],
    ),
    # Multiple rises after a long plateau.
    (
        ([5, 5, 5, 6, 5, 5, 7],),
        [3, 2, 1, 3, 2, 1, 0],
    ),
]

if __name__ == "__main__":
    sys.exit(run_python_tests(daily_temperatures, test_cases))  # type: ignore # noqa: F821
