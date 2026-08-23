import sys

test_cases = [
    [("math", "arithmetic"), "ath"],
    [("original", "origin"), "origin"],
    [("foo", "bar"), ""],
    [("", "arithmetic"), ""],
    [
        (
            "shesellsseashellsatthesea",
            "isawyouyesterday",
        ),
        "saestea",
    ],
    [("@work3r", "m@rxkd35rt"), "@rk3r"],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(longest_common_subsequence, test_cases))  # type: ignore  # noqa: F821
