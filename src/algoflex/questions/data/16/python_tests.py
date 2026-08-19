import sys

test_cases = [
    [
        (["cat", "bat", "rat"], "the cattle was rattled by the battery"),
        "the cat was rat by the bat",
    ],
    [(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"), "a a b c"],
    [
        (["a", "b", "c"], "aadsfasf absbs bbab cadsfafs " * 100_000),
        ("a a b c " * 100_000).rstrip(),
    ],
    [
        (list("aceghikmnprsuvwxyz"), "the quick brown fox jumped over the lazy dog"),
        "the quick brown fox jumped over the lazy dog",
    ],
    [
        (
            list("abcdefghijklmnopqrstuvwxyz"),
            "the quick brown fox jumped over the lazy dog",
        ),
        "t q b f j o t l d",
    ],
    [(list("abcdefghijklmnopqrstuvwxyz"), ""), ""],
    # Edge cases
    [(["a"], "a"), "a"],  # Single root, single word
    [(["ab"], "abc"), "ab"],  # Root is prefix
    [(["abc"], "ab"), "ab"],  # Word shorter than root
    [(["cat", "cattle"], "cattle"), "cat"],  # Multiple roots, shortest wins
    [([], "hello world"), "hello world"],  # No roots
    [
        (["pre", "post"], "prefix postfix prepare"),
        "pre post pre",
    ],  # Non-contiguous matches
]

if __name__ == "__main__":
    sys.exit(run_python_tests(replace_words, test_cases))  # type: ignore  # noqa: F821
