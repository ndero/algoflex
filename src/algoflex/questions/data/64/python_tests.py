import sys

test_cases = [
    # Basic test cases
    (([1],), 1),
    (([3, 1, 2, 5, 4, 1],), 8),
    (([2, 4],), 4),
    # Empty and edge cases
    (([],), 0),
    (([0],), 0),
    (([0, 0, 0],), 0),
    (([0, 1, 0],), 1),
    (([1, 0, 1],), 1),
    # Increasing heights
    (([1, 2, 3, 4, 5],), 9),
    (([1, 2, 3, 4, 5, 6],), 12),
    # Decreasing heights
    (([5, 4, 3, 2, 1],), 9),
    (([6, 5, 4, 3, 2, 1],), 12),
    # Plateau (equal heights)
    (([5, 5, 5, 5],), 20),
    (([3, 3, 3, 3, 3],), 15),
    # Valley shapes
    (([5, 4, 1, 4, 5],), 8),
    (([6, 5, 2, 5, 6],), 10),
    # Peak shapes
    (([1, 3, 5, 3, 1],), 9),
    (([2, 4, 6, 4, 2],), 12),
    # Single tall bar with smaller surroundings
    (([1, 2, 10, 2, 1],), 10),
    (([1, 2, 3, 10, 3, 2, 1],), 10),
    # Multiple valleys
    (([2, 1, 4, 5, 1, 3, 3],), 8),
    (([3, 2, 5, 4, 2, 3, 4],), 14),
    # Alternating heights
    (([1, 3, 2, 4, 3, 5],), 10),
    (([2, 1, 3, 2, 4, 3],), 8),
    # Large differences
    (([100, 1, 100],), 100),
    (([1000, 1, 1000, 1, 1000],), 1000),
    # Zero in middle
    (([3, 2, 0, 2, 3],), 4),
    (([4, 3, 2, 0, 2, 3, 4],), 6),
    # Very large arrays
    ((list(range(1, 10_001)),), 25_005_000),
    ((list(range(10_000, 0, -1)),), 25_005_000),
    # Random combinations
    (([2, 1, 2, 3, 1, 2, 3, 2],), 8),
    (([4, 2, 0, 3, 2, 5, 4, 3],), 10),
    # Boundary tests
    (([1] * 10_000,), 10_000),
    (([10**5] * 100,), 10_000_000),
    # Mountain shape
    (([1, 2, 3, 4, 5, 4, 3, 2, 1],), 15),
    # Staircase pattern
    (([1, 2, 3, 4, 5, 6, 7, 8],), 20),
    (([8, 7, 6, 5, 4, 3, 2, 1],), 20),
    # Complex patterns
    (([6, 2, 5, 4, 5, 1, 6],), 12),
    (([3, 6, 5, 7, 4, 8, 1, 0],), 20),
    # Single element with zero
    (([5, 0, 5, 0, 5],), 5),
    # Long increasing then decreasing
    (
        (list(range(1, 5_001)) + list(range(5_000, 0, -1)),),
        12_505_000,
    ),
    # Checkerboard pattern
    (([10, 1, 10, 1, 10, 1, 10],), 10),
    # All same except one dip
    (([5] * 100 + [1] + [5] * 100,), 500),
    # Maximum values with constraints
    (([10**5] * 10_000,), 1_000_000_000),
    # Extra edge cases
    # Two equal bars
    (([7, 7],), 14),
    # Tall bar at either boundary
    (([10, 1, 1, 1],), 10),
    (([1, 1, 1, 10],), 10),
    # Zero at the boundary
    (([0, 5, 5],), 10),
    (([5, 5, 0],), 10),
    # Multiple equal minima
    (([4, 2, 2, 2, 4],), 10),
    # Best rectangle spans the entire histogram
    (([3, 3, 3, 3],), 12),
    # Best rectangle is strictly in the middle
    (([1, 5, 5, 5, 1],), 15),
    # Large spike surrounded by equal bars
    (([2, 2, 10, 2, 2],), 10),
    # Several competing rectangles
    (([2, 6, 6, 5, 5, 5, 2],), 25),
    # Zeros split the histogram into independent regions
    (([2, 4, 3, 0, 5, 5, 1],), 10),
]

if __name__ == "__main__":
    sys.exit(run_python_tests(max_rectangle, test_cases))  # type: ignore  # noqa: F821
