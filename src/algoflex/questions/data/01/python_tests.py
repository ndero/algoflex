import sys

test_cases = [
    [("abcdddeeeeaabbbb",), [[3, 5], [6, 9], [12, 15]]],
    [("xxxcyyyyydkkkkkk",), [[0, 2], [4, 8], [10, 15]]],
    [
        ("abcdddeeeeaabbbb" * 6,),
        [
            [3, 5],
            [6, 9],
            [12, 15],
            [19, 21],
            [22, 25],
            [28, 31],
            [35, 37],
            [38, 41],
            [44, 47],
            [51, 53],
            [54, 57],
            [60, 63],
            [67, 69],
            [70, 73],
            [76, 79],
            [83, 85],
            [86, 89],
            [92, 95],
        ],
    ],
    [("abcd",), []],
    [("aabbccdd",), []],
    [("",), []],
    [("abcdefffghijkl",), [[5, 7]]],
    [("abcdeffghijkl" * 100_000,), []],
    [("abcdeffghijkl" * 100_000 + "kkk",), [[1_300_000, 1_300_002]]],
    [("kkk" + "abcdeffghijkl" * 100_000,), [[0, 2]]],
    [
        ("abcdefffghijkl" * 100_000,),
        [[5 + i, 7 + i] for i in range(0, 100_000 * 14, 14)],
    ],
]


if __name__ == "__main__":
    sys.exit(run_python_tests(repeated, test_cases))  # type: ignore  # noqa: F821
