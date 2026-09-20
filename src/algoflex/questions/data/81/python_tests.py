import sys

test_cases = [
    # Single digits
    [(0,), True],
    [(1,), True],
    [(-7,), False],
    [(9,), True],
    # Basic palindromes
    [(11,), True],
    [(22,), True],
    [(121,), True],
    [(1_221,), True],
    [(-12_321,), False],
    [(123_321,), True],
    [(-1_234_321,), False],
    [(12_344_321,), True],
    [(123_454_321,), True],
    # Basic non-palindromes
    [(10,), False],
    [(12,), False],
    [(123,), False],
    [(1234,), False],
    [(12345,), False],
    [(-123_456,), False],
    [(12_021,), True],
    [(123_451,), False],
    # Numbers with zeros
    [(100,), False],
    [(101,), True],
    [(1001,), True],
    [(-10001,), False],
    [(10010,), False],
    [(100_001,), True],
    [(1000001,), True],
    [(1000000,), False],
    # Negative numbers
    [(-1,), False],
    [(-11,), False],
    [(-121,), False],
    [(-1221,), False],
    [(-12321,), False],
    # Numbers containing zeros in the middle
    [(10201,), True],
    [(-10301,), False],
    [(10501,), True],
    [(1002001,), True],
    [(10020001,), False],
    [(102030201,), True],
    [(102030401,), False],
    # Values around common boundaries
    [(2_147_483_647,), False],
    [(2_147_483_646,), False],
    [(-2_147_483_648,), False],
    # Repeated digits
    [(111,), True],
    [(-1111,), False],
    [(11111,), True],
    [(-222222,), False],
    [(999999,), True],
    # Almost-palindromes
    [(11211,), True],
    [(12131,), False],
    [(-12321,), False],
    [(12341,), False],
    [(-123451,), False],
    [(1234322,), False],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(is_palindrome, test_cases))  # type: ignore  # noqa: F821
