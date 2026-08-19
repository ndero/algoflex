import sys

test_cases = [
    [(19,), True],
    [(2,), False],
    [(17,), False],
    [(202,), False],
    [(711,), False],
    [(176,), True],
    [(19_345_672,), False],
    [(345_000_000,), False],
    [(1_703_932,), False],
    [(2_147_483_647,), False],
    [(1,), True],
    # Edge cases
    [(7,), True],  # Small happy number
    [(10,), True],  # 1² + 0² = 1
    [(100,), True],  # 1² + 0² + 0² = 1
    [(4,), False],  # Small unhappy number
]

if __name__ == "__main__":
    sys.exit(run_python_tests(is_happy, test_cases))  # type: ignore  # noqa: F821
