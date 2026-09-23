import sys

test_cases = [
    # Empty / single character
    [("",), 0],
    [("a",), 1],
    [(" ",), 1],
    [("1",), 1],
    [("@",), 1],
    # Simple repetitions
    [("aa",), 1],
    [("aaa",), 1],
    [("aaaaa",), 1],
    [("ab",), 2],
    [("aba",), 2],
    [("abba",), 2],
    [("abcabcbb",), 3],
    [("bbbbb",), 1],
    [("pwwkew",), 3],
    # All unique
    [("abcdef",), 6],
    [("abcdefghijklmnopqrstuvwxyz",), 26],
    [("0123456789",), 10],
    [("!@#$%^&*()",), 10],
    # Spaces are valid characters
    [("a b",), 3],
    [("  ",), 1],
    [("a  b",), 2],
    [("abc def",), 7],
    [("a b c a",), 3],
    # Mixed letters, digits, symbols
    [("a1b2c3",), 6],
    [("a1a2",), 3],
    [("a!b@c#",), 6],
    [("a!a@b",), 4],
    [("Aa",), 2],
    [("A a",), 3],
    # Repetition occurring after a long unique substring
    [("abcdefga",), 7],
    [("abcdeafgh",), 8],
    [("dvdf",), 3],
    # Repeated pattern
    [("abcabcabc",), 3],
    [("abcdabc",), 4],
    # Long input
    [("a" * 50_000,), 1],
    [("abcdefghijklmnopqrstuvwxyz" * 2_000,), 26],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(longest_substring, test_cases))  # noqa: F821 #type: ignore
