import sys

test_cases = [
    [([1, 2, 5], 11), 3],
    [([1, 2, 5, 10], 11), 2],
    [([1], 0), 0],
    [([1, 2, 5, 10, 20], 11), 2],
    [([1, 2, 5, 10, 20], 110), 6],
    [([2, 5], 3), -1],
    [([1, 2, 5, 10, 20], 63), 5],
    [([1, 2, 5, 10, 20, 50], 16), 3],
    [([1, 2, 5, 10, 20, 50], 28), 4],
    [([1, 2, 5, 10, 20, 50], 77), 4],
    # edge cases
    [([], 0), 0],  # zero amount needs zero coins
    [([], 1), -1],  # impossible without coins
    [([5, 1, 2], 11), 3],  # unsorted coins
    [([1], 1), 1],  # single coin exactly matches
    [([3], 2), -1],  # coin larger than amount
    [([7, 5, 3], 4), -1],  # no combination possible
    [([2, 5, 10], 20), 2],  # multiple coins needed
    [([1, 2, 5], 100), 20],  # large amount with small coins
]

if __name__ == "__main__":
    sys.exit(run_python_tests(min_coins, test_cases))  # type: ignore  # noqa: F821
