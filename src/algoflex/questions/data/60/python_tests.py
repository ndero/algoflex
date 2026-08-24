import sys
from itertools import combinations


# Helper to compute expected sorted combinations
def expected_combinations(s, k):
    return sorted(["".join(c) for c in combinations(s, k)])


# Test data
s1, k1 = "abcd", 3
s2, k2 = "", 2
s3, k3 = "rat", 3
s4, k4 = "rat", 1
s5, k5 = "rat", 0
s6, k6 = "abcdefghijklmnopqrstuvwxyz", 1
s7, k7 = "abcdefghijklmnopqrstuvwxyz", 5
s8, k8 = "abcd", 5

test_cases = [
    [(s1, k1), expected_combinations(s1, k1)],
    [(s2, k2), expected_combinations(s2, k2)],
    [(s3, k3), expected_combinations(s3, k3)],
    [(s4, k4), expected_combinations(s4, k4)],
    [(s5, k5), expected_combinations(s5, k5)],
    [(s6, k6), expected_combinations(s6, k6)],
    [(s7, k7), expected_combinations(s7, k7)],
    [(s8, k8), expected_combinations(s8, k8)],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(combs, test_cases))  # type: ignore  # noqa: F821
