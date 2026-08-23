import sys

nums1 = [4, 2, 3, 0, 3, 1, 2]
nums2 = [3, 0, 2, 1, 2]
nums3 = [4, 2, 3, 0, 3, 1, 2]
nums4 = [1] * 200_000 + [0]
nums5 = [0]
nums6 = [2, 4, 0, 1, 1, 1, 0, 2, 1]

test_cases = [
    [(nums1, 0), True],
    [(nums2, 2), False],
    [(nums3, 5), True],
    [(nums4, 567), True],
    [(nums5, 0), True],
    [(nums6, 8), True],
    # Edge cases
    [([0, 1], 0), True],
    [([0, 1], 1), True],
    [([1, 0], 0), True],
    [([1, 0], 1), True],
    [([2, 1, 1], 0), False],
    [([2, 1, 1], 1), False],
    [([1, 1, 1], 0), False],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(can_reach_zero, test_cases))  # type: ignore  # noqa: F821
