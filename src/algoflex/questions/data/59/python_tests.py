import sys

nums1 = "ab" * 100  # "abab...ab" (200 chars)
nums2 = "a" * 100  # 100 'a's
nums3 = "abcdefghijklmnopqrstuvwxyz"
nums4 = "a" * 1000 + "b" + "a" * 1000  # 2001 chars
nums5 = "a" * 1000 + "b" + "a" * 50  # 1051 chars

test_cases = [
    [("babad",), "bab"],
    [("abcde",), "a"],
    [(nums1,), "a" + "ba" * 99],
    [(nums2,), "a" * 100],
    [(nums3,), "a"],
    [(nums4,), "a" * 1000 + "b" + "a" * 1000],
    [(nums5,), "a" * 1000],
    [("",), ""],
    [("cbbd",), "bb"],
    [("a",), "a"],
    [("aa",), "aa"],
    [("aaa",), "aaa"],
    [("abcba",), "abcba"],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(lps, test_cases))  # type: ignore  # noqa: F821
