import sys

n1 = 1
e1 = []
k1 = 0

n2 = 2
e2 = [[0, 1, 3]]
k2 = 5

n3 = 2
e3 = [[0, 1, 10]]
k3 = 5

n4 = 5
e4 = [
    [0, 1, 1],
    [1, 2, 1],
    [2, 3, 1],
    [3, 4, 1],
]
k4 = 1

n5 = 5
e5 = [
    [0, 1, 1],
    [0, 2, 1],
    [0, 3, 1],
    [0, 4, 1],
]
k5 = 1

n6 = 6
e6 = [
    [0, 1, 1],
    [1, 2, 1],
    [3, 4, 1],
]
k6 = 2

n7 = 4
e7 = [
    [0, 1, 1],
    [0, 2, 1],
    [0, 3, 1],
    [1, 2, 1],
    [1, 3, 1],
    [2, 3, 1],
]
k7 = 2

n8 = 4
e8 = [
    [0, 1, 10],
    [0, 2, 1],
    [2, 1, 1],
    [1, 3, 1],
]
k8 = 2

n9 = 3
e9 = [
    [0, 1, 10],
    [0, 1, 1],
    [1, 2, 1],
]
k9 = 2

n10 = 5
e10 = [
    [0, 1, 5],
    [1, 2, 5],
    [2, 3, 5],
    [3, 4, 5],
]
k10 = 100

cities = [
    [0, 4, 10],
    [0, 8, 25],
    [0, 1, 10],
    [0, 2, 30],
    [0, 3, 20],
    [8, 4, 60],
    [4, 5, 60],
    [5, 3, 70],
    [3, 6, 10],
    [6, 7, 5],
    [1, 7, 50],
]

test_cases = [
    ((9, cities, 5), 8),
    ((9, cities, 70), 5),
    ((9, cities, 1), 8),
    ((n1, e1, k1), 0),
    ((n2, e2, k2), 1),
    ((n3, e3, k3), 1),
    ((n4, e4, k4), 4),
    ((n5, e5, k5), 4),
    ((n6, e6, k6), 5),
    ((n7, e7, k7), 3),
    ((n8, e8, k8), 3),
    ((n9, e9, k9), 2),
    ((n10, e10, k10), 4),
    # Edge cases
    # No edges: every city has zero reachable neighbors.
    # Tie -> greatest index.
    ((5, [], 100), 4),
    # Threshold of zero: no other city is reachable.
    (
        (
            4,
            [
                [0, 1, 1],
                [1, 2, 1],
                [2, 3, 1],
            ],
            0,
        ),
        3,
    ),
    # A path whose direct edges exceed k, but a shorter path exists.
    (
        (
            4,
            [
                [0, 1, 10],
                [0, 2, 2],
                [2, 1, 2],
                [1, 3, 2],
            ],
            4,
        ),
        3,
    ),
    # Two disconnected components with a tie.
    # Counts: 0=1, 1=1, 2=1, 3=1 -> choose 3.
    (
        (
            4,
            [
                [0, 1, 1],
                [2, 3, 1],
            ],
            1,
        ),
        3,
    ),
    # Multiple edges between the same pair; shortest edge should win.
    (
        (
            3,
            [
                [0, 1, 100],
                [0, 1, 2],
                [1, 2, 2],
            ],
            4,
        ),
        2,
    ),
]

if __name__ == "__main__":
    sys.exit(run_python_tests(reachable_cities, test_cases))  # type: ignore  # noqa: F821
