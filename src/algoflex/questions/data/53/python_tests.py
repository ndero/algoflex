import sys

network1 = [
    [0, 4],
    [0, 8],
    [0, 1],
    [0, 2],
    [0, 3],
    [8, 4],
    [4, 5],
    [5, 3],
    [3, 6],
    [6, 7],
    [1, 7],
]
network2 = [[i, i + 1] for i in range(10)]
network3 = [[i, i + 1] for i in range(10)] + [[10, 1]]

test_cases = [
    [(4, [[0, 1], [1, 2], [2, 0], [1, 3]]), [[1, 3]]],
    [
        (7, [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [4, 5], [5, 6]]),
        [[1, 3], [1, 4], [4, 5], [5, 6]],
    ],
    [
        (7, [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [4, 5], [5, 6], [2, 6]]),
        [[1, 3]],
    ],
    [(9, network1), [[0, 2]]],
    [(11, network2), [[i, i + 1] for i in range(10)]],
    [(11, network3), [[0, 1]]],
    # edge cases
    [(1, []), []],  # single node, no edges
    [(2, [[0, 1]]), [[0, 1]]],  # single edge is a bridge
    [(3, [[0, 1], [1, 2], [2, 0]]), []],  # triangle, no bridges
    [
        (4, [[0, 1], [2, 3]]),
        [[0, 1], [2, 3]],
    ],  # disconnected graph, both edges are bridges
    [(4, [[0, 1], [0, 2], [0, 3], [1, 2]]), [[0, 3]]],  # one bridge, rest in cycle
    [
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]]),
        [[0, 1], [1, 2], [2, 3], [3, 4]],
    ],  # line graph, all bridges
]

if __name__ == "__main__":
    sys.exit(run_python_tests(critical_connections, test_cases))  # type: ignore  # noqa: F821
