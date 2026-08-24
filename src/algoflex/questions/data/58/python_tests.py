import sys

nums1 = [i for i in range(10_000)]  # strictly increasing
nums2 = [1 for _ in range(10_000)]  # all equal
nums3 = [10, 9, 2, 5, 3, 7, 101, 18]
nums4 = [0, 1, 0, 3, 2, 3]

test_cases = [
    [([0, 1, 0, 3, 2, 3],), 4],
    [([6, 6, 6, 6, 6, 6, 6, 6],), 1],
    [([10, 9, 2, 5, 3, 7, 101, 18],), 4],
    [(nums1,), 10_000],
    [(nums2,), 1],
    [(nums3,), 4],
    [(nums4,), 4],
    [([],), 0],
    [([5],), 1],
    [([5, 4, 3, 2, 1],), 1],
    [([1, 2, 3, 1, 2, 3, 1, 2, 3],), 3],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(longest_increasing_subsequence, test_cases))  # type: ignore  # noqa: F821
