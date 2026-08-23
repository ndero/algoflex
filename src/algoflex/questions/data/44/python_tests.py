import sys

nums1 = [2, 3, 1, 1, 4]
nums2 = [0]
nums3 = [2, 1, 1, 0, 4]
nums4 = list(range(200_000))
nums5 = [1] * 200_000
nums6 = [0, 0]
nums7 = [200_000] + [0] * 200_000

test_cases = [
    [(nums1,), True],
    [(nums2,), True],
    [(nums3,), False],
    [(nums4,), False],
    [(nums5,), True],
    [(nums6,), False],
    [(nums7,), True],
    # Edge cases
    [([1],), True],
    [([1, 0],), True],
    [([0, 1],), False],
    [([1, 1, 0],), True],
    [([2, 0, 0],), True],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(can_reach_end, test_cases))  # type: ignore  # noqa: F821
