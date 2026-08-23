import sys

prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
prices3 = [0, 0, 0, 0]
prices4 = [4] * 2_000 + [15] * 1_000
prices5 = [90] * 10_000 + [50] * 20_000
prices6 = []
prices7 = list(range(1, 100_000))

test_cases = [
    [(prices1,), 5],
    [(prices2,), 0],
    [(prices3,), 0],
    [(prices4,), 11],
    [(prices5,), 0],
    [(prices6,), 0],
    [(prices7,), 99_998],
    # Edge cases
    [([1],), 0],
    [([1, 2],), 1],
    [([2, 1],), 0],
    [([5, 5],), 0],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(max_profit, test_cases))  # type: ignore  # noqa: F821
