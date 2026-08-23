import sys

arr1 = [8, 2, 4, 9, 12, 18, 16, 13]
arr2 = list(range(100_000, -1, -1))
arr3 = list(range(10_000))
arr4 = [8, 1, 5] * 100_000
arr5 = [3]

test_cases = [
    [(arr1,), [2, 4, 8, 9, 12, 13, 16, 18]],
    [(arr2,), list(range(100_001))],
    [(arr3,), list(range(10_000))],
    [(arr4,), [1] * 100_000 + [5] * 100_000 + [8] * 100_000],
    [(arr5,), [3]],
    # Edge cases
    [([],), []],
    [([1],), [1]],
    [([2, 1],), [1, 2]],
    [([5, 5, 5, 5],), [5, 5, 5, 5]],
    [([-3, 2, -1, 0],), [-3, -1, 0, 2]],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(merge_sort, test_cases))  # type: ignore  # noqa: F821
