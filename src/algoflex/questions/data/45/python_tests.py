import sys

nums1 = [2, 3, 1, 1, 4]
nums2 = [1]
nums3 = [1, 5]
nums4 = [1] * 200_000
nums5 = [200_000] + [0] * 200_000
nums6 = list(range(1, 100_000))

test_cases = [
    [(nums1,), 2],
    [(nums2,), 0],
    [(nums3,), 1],
    [(nums4,), 199_999],
    [(nums5,), 1],
    [(nums6,), 17],
    # Edge cases
    [([2, 1],), 1],
    [([1, 1, 1],), 2],
    [([3, 1, 1, 1],), 1],
    [([1, 2, 1, 1],), 2],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(min_jumps, test_cases))  # type: ignore  # noqa: F821
