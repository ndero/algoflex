import sys

nums1 = [1, 2, 3, 1]
nums2 = [1, 7, 2, 1, 6]
nums3 = [1, 2]
nums4 = [3]
nums5 = [133, 99, 17, 39, 54, 98, 57, 34, 23, 100]
nums6 = list(range(0, 100_000, 100))

test_cases = [
    [(nums1,), 4],
    [(nums2,), 13],
    [(nums3,), 2],
    [(nums4,), 3],
    [(nums5,), 404],
    [(nums6,), 25_000_000],
    # Edge cases
    [([],), 0],
    [([0],), 0],
    [([1, 1],), 1],
    [([2, 1, 1, 2],), 4],
    [([5, 1, 5, 1, 5],), 15],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(max_loot, test_cases))  # type: ignore  # noqa: F821
