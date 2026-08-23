import sys

test_cases = [
    [(["flower", "flow", "flight"],), "fl"],
    [(["dog", "racecar", "car"],), ""],
    [
        (
            [
                "algology",
                "algologies",
                "algologists",
                "algometer",
                "algometric",
                "algometry",
                "algophobia",
                "algologically",
                "algorithm",
                "algorism",
            ],
        ),
        "algo",
    ],
    [
        (
            [
                "ORGANOMETALLICS",
                "ORGANOPHOSPHATE",
                "ORGANOTHERAPY ",
            ],
        ),
        "ORGANO",
    ],
    [(["lower", "low", "light"],), "l"],
    [
        (
            [
                "SYSTEMATISE",
                "SYSTEMATISED",
                "SYSTEMATISER",
                "SYSTEMATISERS",
                "SYSTEMATISES",
                "SYSTEMATISING",
                "SYSTEMATISM",
                "SYSTEMATISMS",
                "SYSTEMATIST",
            ],
        ),
        "SYSTEMATIS",
    ],
    [
        (
            [
                "garden",
                "gardener",
                "gardened",
                "gardenful",
                "gardenia",
            ],
        ),
        "garden",
    ],
    [(["flytrap", "flyway", "flyweight", "flywheel"],), "fly"],
    [(["flower", "flow", ""],), ""],
    # Edge cases
    [([],), ""],
    [(["hello"],), "hello"],
    [(["a", "a", "a"],), "a"],
    [(["abc", "ab", "a"],), "a"],
    [(["", ""],), ""],
    [(["same", "same"],), "same"],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(longest_common_prefix, test_cases))  # type: ignore  # noqa: F821
