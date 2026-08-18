import sys

test_cases = [
    [([4, 1, 2, 1, 2],), 4],
    [([2],), 2],
    [([i for i in range(1, 500_000)] + [i for i in range(500_000)],), 0],
    [
        ([i for i in range(500_000)] + [-2, -3] + [i for i in range(500_000)] + [-2],),
        -3,
    ],
    [([i for i in range(1, 500_000)] * 2 + [-4],), -4],
    [([500_001] + [i for i in range(-500_000, 500_000)] * 2,), 500_001],
    # Edge cases
    [([0],), 0],  # Single zero
    [([-1],), -1],  # Single negative
    [([1, 2, 3, 2, 1],), 3],  # Middle element
    [([-2, -1, -2],), -1],  # Negative numbers
    [([0, 0, 1],), 1],  # Zero pairs
    [
        ([2_147_483_647, -2_147_483_648, 2_147_483_647],),
        -2_147_483_648,
    ],  # Extreme values
]

if __name__ == "__main__":
    sys.exit(run_python_tests(single_number, test_cases))  # type: ignore  # noqa: F821
