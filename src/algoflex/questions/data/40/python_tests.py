import sys

arr1 = [5, 2, 2, 6, 1]
arr2 = [0]
arr3 = []
arr4 = [8, 2, 4, 9, 12, 18, 16]
arr5 = list(range(100_000))
arr6 = list(range(100_000, 0, -1))

test_cases = [
    [(arr1,), [3, 1, 1, 1, 0]],
    [(arr2,), [0]],
    [(arr3,), []],
    [(arr4,), [2, 0, 0, 0, 0, 1, 0]],
    [(arr5,), [0] * 100_000],
    [(arr6,), list(range(99_999, -1, -1))],
    # Edge cases
    [([1, 1, 1, 1],), [0, 0, 0, 0]],
    [([3, 2, 1],), [2, 1, 0]],
    [([1, 2, 3],), [0, 0, 0]],
    [([-2, -5, -1, -3],), [2, 0, 1, 0]],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(smaller_to_the_right, test_cases))  # type: ignore  # noqa: F821
