import sys

test_cases = [
    [("brain", "drain"), "rain"],
    [("math", "arithmetic"), "th"],
    [("abca" * 360, "bca" * 500), "abca"],
    [("abc" * 400, "xyz" * 300), ""],
    [("blackmarket", "stagemarket"), "market"],
    [("theoldmanoftheseaissowise", "sowisetheoldmanoftheseais"), "theoldmanoftheseais"],
    # Edge cases
    [("", ""), ""],  # Both empty
    [("a", ""), ""],  # One empty
    [("", "b"), ""],  # Other empty
    [("a", "a"), "a"],  # Single character match
    [("a", "b"), ""],  # Single character no match
    [("abc", "abc"), "abc"],  # Identical strings
    [("aaaa", "aa"), "aa"],  # Repeated characters
    [("abcdef", "fedcba"), "a"],  # Reversed strings
]

if __name__ == "__main__":
    sys.exit(run_python_tests(longest_common_substring, test_cases))  # type: ignore  # noqa: F821
