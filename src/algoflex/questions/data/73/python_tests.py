import sys

test_cases = [
    # ===== Minimal Edge Cases =====
    (("a", "a"), "a"),
    (("a", "b"), ""),
    (("ab", "a"), "a"),
    (("ab", "b"), "b"),
    (("aa", "aa"), "aa"),
    (("aa", "aaa"), ""),
    # ===== Classic Example =====
    (("ADOBECODEBANC", "ABC"), "BANC"),
    # ===== Case Sensitivity =====
    (("aAaAaA", "Aa"), "aA"),
    (("aAaAaA", "aa"), "aAa"),
    (("ABC", "abc"), ""),
    # ===== Window At Beginning =====
    (("ABCXYZ", "ABC"), "ABC"),
    (("AABCXYZ", "AABC"), "AABC"),
    # ===== Window At End =====
    (("XYZABC", "ABC"), "ABC"),
    (("XYZAAABC", "AABC"), "AABC"),
    # ===== Window In Middle =====
    (("XYZABCXYZ", "ABC"), "ABC"),
    (("ZZZABCZZZ", "ABC"), "ABC"),
    # ===== Repeated Characters In T =====
    (("AAABBC", "AABC"), "AABBC"),
    (("ABAACBAB", "ABC"), "ACB"),
    (("ABAACBAB", "AABC"), "BAAC"),
    # ===== All Characters Same =====
    (("aaaaaaa", "aaa"), "aaa"),
    (("aaaaaaa", "aaaaaa"), "aaaaaa"),
    (("aaaaaaa", "aaaaaaaa"), ""),
    # ===== No Possible Window =====
    (("abcdef", "gh"), ""),
    (("short", "longer"), ""),
    # ===== Tight Windows =====
    (("abc", "ac"), "abc"),
    (("cab", "ab"), "ab"),
    (("bba", "ab"), "ba"),
    # ===== Many Extra Characters =====
    (("aaaaaaaaaabbbbbcdd", "abcdd"), "abbbbbcdd"),
    (("xyyzyzyx", "xyz"), "zyx"),
    # ===== Multiple Possible Windows =====
    (("aaflslflsldkalskaaa", "aaa"), "aaa"),
    (("abdabca", "abc"), "abc"),
    # ===== Large Duplicate Stress =====
    (("ABABABABABABABABAB", "AABB"), "ABAB"),
    (("AAABBBCCC", "ABC"), "ABBBC"),
    # ===== Exact Full Coverage =====
    (("abc", "abc"), "abc"),
    # ===== Additional Edge Cases =====
    # t contains a character exactly once, but s contains many.
    (("aaaaab", "ab"), "ab"),
    # Duplicates matter.
    (("aabbcc", "abc"), "abbc"),
    (("aabbcc", "aabc"), "aabbc"),
    # Repeated target character is spread across the window.
    (("abaaca", "aaa"), "abaa"),
    # Target requires characters in both directions around the center.
    (("xxabxcax", "abc"), "abxc"),
    # Single-character target with many candidates.
    (("abcdefg", "d"), "d"),
    # Single-character target repeated.
    (("xxxyyyxxx", "xxx"), "xxx"),
    # Target consists entirely of duplicates.
    (("bbbaaaaccc", "aaa"), "aaa"),
    # Window must include a distant final character.
    (("abcxxxxxxxxxxd", "ad"), "abcxxxxxxxxxxd"),
    # Exact match buried inside noise.
    (("zzzaaaabzzz", "aab"), "aab"),
    # Multiple valid windows; choose the unique shortest one.
    (("cabwefgewcwaefgcf", "cae"), "cwae"),
    # Case-sensitive repeated requirements.
    (("aAbBAa", "AB"), "BA"),
    # No window because one duplicate is missing.
    (("aabc", "aabcaa"), ""),
    # t longer than s but with repeated characters.
    (("abc", "aabc"), ""),
    # Entire string is the unique minimum window.
    (("xabcx", "xabx"), "xabcx"),
]

if __name__ == "__main__":
    sys.exit(run_python_tests(min_window, test_cases))  # type: ignore  # noqa: F821
