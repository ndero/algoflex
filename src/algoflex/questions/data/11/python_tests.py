import sys

test_cases = [
    [(64,), True],
    [(20,), False],
    [(1024,), True],
    [(2,), True],
    [(0,), False],
    [(1267650600228229401496703205376,), True],
    [(1267650600228229401496703205377,), False],
    [(-64,), False],
    # Edge cases
    [(1,), True],  # 2^0
    [(-2,), False],  # Negative power of 2
]

if __name__ == "__main__":
    sys.exit(run_python_tests(is_power_of_two, test_cases))  # type: ignore  # noqa: F821
