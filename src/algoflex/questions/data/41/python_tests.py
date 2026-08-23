import sys

nums1 = [3, 2, 3]
nums2 = [6] * 20
nums3 = [9] * 21 + [7] * 20
nums4 = [2]
nums6 = [6] * 100_000 + [9] * 100_001
nums7 = [-2, -2, -4, -2, -4, -4, -4]

test_cases = [
    [(nums1,), 3],
    [(nums2,), 6],
    [(nums3,), 9],
    [(nums4,), 2],
    [(nums6,), 9],
    [(nums7,), -4],
    # Edge cases
    [([1, 1, 2],), 1],
    [([1, 2, 1, 1, 2, 1, 1],), 1],
    [([-1, -1, 2, -1],), -1],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(majority, test_cases))  # type: ignore  # noqa: F821
