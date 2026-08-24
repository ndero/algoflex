import sys

test_cases = [
    # Minimal / edge cases
    ((["a1 9 2 3 1"],), ["a1 9 2 3 1"]),
    ((["a1 act car"],), ["a1 act car"]),
    (([],), []),
    # Standard example
    (
        (
            [
                "dig1 8 1 5 1",
                "let1 art can",
                "dig2 3 6",
                "let2 own kit dig",
                "let3 art zero",
            ],
        ),
        [
            "let1 art can",
            "let3 art zero",
            "let2 own kit dig",
            "dig1 8 1 5 1",
            "dig2 3 6",
        ],
    ),
    # All digit logs
    (
        (["d1 1 2 3", "d2 4 5 6", "d3 7 8 9"],),
        ["d1 1 2 3", "d2 4 5 6", "d3 7 8 9"],
    ),
    # All letter logs
    (
        (["l1 abc def", "l2 abc deg", "l3 bcd efg"],),
        ["l1 abc def", "l2 abc deg", "l3 bcd efg"],
    ),
    # Same content, different identifiers
    (
        (["l2 abc def", "l1 abc def", "d1 1 2"],),
        ["l1 abc def", "l2 abc def", "d1 1 2"],
    ),
    # Content tie-break by identifier
    (
        (["a2 same content", "a1 same content", "d1 4 5"],),
        ["a1 same content", "a2 same content", "d1 4 5"],
    ),
    # Digit logs maintain original order
    (
        (["d1 3 4", "d2 1 2", "l1 abc def"],),
        ["l1 abc def", "d1 3 4", "d2 1 2"],
    ),
    # Letter content sorting
    (
        (["l1 zoo alpha", "l2 apple pie", "l3 zoo beta"],),
        ["l2 apple pie", "l1 zoo alpha", "l3 zoo beta"],
    ),
    # Mixed with similar prefixes
    (
        (
            [
                "let1 art zero",
                "let2 art can",
                "let3 art apple",
                "dig1 3 6",
            ],
        ),
        [
            "let3 art apple",
            "let2 art can",
            "let1 art zero",
            "dig1 3 6",
        ],
    ),
    # Single-word content
    (
        (["l1 apple", "l2 banana", "d1 5"],),
        ["l1 apple", "l2 banana", "d1 5"],
    ),
    # Long content
    (
        (
            [
                "l1 this is a long log message",
                "l2 another long log message",
                "d1 9 8 7",
            ],
        ),
        [
            "l2 another long log message",
            "l1 this is a long log message",
            "d1 9 8 7",
        ],
    ),
    # Mixed ordering
    (
        (
            [
                "d1 4 2",
                "l1 abc def",
                "l2 abc deg",
                "d2 0 1",
            ],
        ),
        [
            "l1 abc def",
            "l2 abc deg",
            "d1 4 2",
            "d2 0 1",
        ],
    ),
    # Many digit logs at end
    (
        (
            [
                "l1 aa bb",
                "d1 1 1",
                "d2 2 2",
                "d3 3 3",
            ],
        ),
        [
            "l1 aa bb",
            "d1 1 1",
            "d2 2 2",
            "d3 3 3",
        ],
    ),
    # Identifier tie-break
    (
        (
            [
                "x9 alpha beta",
                "x1 alpha beta",
                "x3 alpha beta",
            ],
        ),
        [
            "x1 alpha beta",
            "x3 alpha beta",
            "x9 alpha beta",
        ],
    ),
    # 100 logs
    (
        (
            [f"let{i} content {i}" for i in range(50)]
            + [f"dig{i} {i} {i + 1}" for i in range(50)],
        ),
        sorted(
            [f"let{i} content {i}" for i in range(50)],
            key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]),
        )
        + [f"dig{i} {i} {i + 1}" for i in range(50)],
    ),
    # Extra edge cases
    # Digit logs interspersed throughout letter logs.
    (
        (
            [
                "d1 9 9",
                "l3 cat dog",
                "d2 1 2",
                "l1 apple pie",
                "d3 5 6",
                "l2 banana split",
                "d4 0 0",
            ],
        ),
        [
            "l1 apple pie",
            "l2 banana split",
            "l3 cat dog",
            "d1 9 9",
            "d2 1 2",
            "d3 5 6",
            "d4 0 0",
        ],
    ),
    # Equal content but different identifiers.
    (
        (
            [
                "id3 hello world",
                "id1 hello world",
                "id2 hello world",
            ],
        ),
        [
            "id1 hello world",
            "id2 hello world",
            "id3 hello world",
        ],
    ),
    # Content differs only after the first word.
    (
        (
            [
                "a1 abc z",
                "a2 abc a",
                "a3 abc m",
            ],
        ),
        [
            "a2 abc a",
            "a3 abc m",
            "a1 abc z",
        ],
    ),
    # Different identifiers must not affect a stronger content ordering.
    (
        (
            [
                "z9 apple z",
                "a1 banana a",
                "m5 apple a",
                "b2 banana z",
            ],
        ),
        [
            "m5 apple a",
            "z9 apple z",
            "a1 banana a",
            "b2 banana z",
        ],
    ),
    # Digit logs with different values but identical identifiers prefix.
    (
        (
            [
                "d1 9 9",
                "d1 1 1",
                "d1 5 5",
                "l1 alpha beta",
            ],
        ),
        [
            "l1 alpha beta",
            "d1 9 9",
            "d1 1 1",
            "d1 5 5",
        ],
    ),
    # Mixed single-word content.
    (
        (
            [
                "d1 5",
                "l2 banana",
                "d2 1",
                "l1 apple",
                "d3 9",
            ],
        ),
        [
            "l1 apple",
            "l2 banana",
            "d1 5",
            "d2 1",
            "d3 9",
        ],
    ),
    # All logs have one content word.
    (
        (
            [
                "x3 zebra",
                "x1 apple",
                "x2 banana",
                "d1 3",
                "d2 1",
            ],
        ),
        [
            "x1 apple",
            "x2 banana",
            "x3 zebra",
            "d1 3",
            "d2 1",
        ],
    ),
    # Uppercase/lowercase ordering should follow normal string ordering.
    (
        (
            [
                "a1 apple",
                "a2 Apple",
                "a3 banana",
            ],
        ),
        [
            "a2 Apple",
            "a1 apple",
            "a3 banana",
        ],
    ),
    # Digits stay in exact original order even when their identifiers
    # would otherwise sort differently.
    (
        (
            [
                "z9 1 1",
                "a1 2 2",
                "m5 3 3",
                "b2 apple pie",
            ],
        ),
        [
            "b2 apple pie",
            "z9 1 1",
            "a1 2 2",
            "m5 3 3",
        ],
    ),
]

if __name__ == "__main__":
    sys.exit(run_python_tests(reorder_logs, test_cases))  # type: ignore # noqa: F821
