import sys

test_cases = [
    # Minimal cases
    [(2, [[0, 1]]), 2],
    [(2, [[0, 1], [1, 0]]), 1],
    [(1, []), 1],
    [(2, []), 2],
    # Small simple cycles
    [(3, [[0, 1], [1, 2], [2, 0]]), 1],
    [(3, [[0, 1], [1, 2]]), 3],
    [(3, [[0, 1], [1, 0], [1, 2]]), 2],
    [(4, [[0, 1], [1, 2], [2, 3], [3, 0]]), 1],
    # Disconnected graphs
    [(4, []), 4],
    [(5, [[0, 1], [1, 0], [3, 4], [4, 3]]), 3],
    [(6, [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5]]), 4],
    # Self loops
    [(3, [[0, 0], [1, 1], [2, 2]]), 3],
    [(3, [[0, 1], [1, 0], [2, 2]]), 2],
    # Chain graph
    [(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 5],
    [(10, [[i, i + 1] for i in range(9)]), 10],
    # Reverse chain
    [(5, [[4, 3], [3, 2], [2, 1], [1, 0]]), 5],
    # Two separate cycles
    [
        (
            6,
            [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]],
        ),
        2,
    ],
    # Cycle with tail
    [(5, [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4]]), 3],
    [
        (
            6,
            [[0, 1], [1, 2], [2, 0], [3, 4], [4, 3], [4, 5]],
        ),
        3,
    ],
    # Star patterns
    [(5, [[0, 1], [0, 2], [0, 3], [0, 4]]), 5],
    [(5, [[1, 0], [2, 0], [3, 0], [4, 0]]), 5],
    # Complete digraph
    [
        (
            4,
            [[i, j] for i in range(4) for j in range(4) if i != j],
        ),
        1,
    ],
    # Sparse mixed graphs
    [
        (
            7,
            [
                [0, 1],
                [1, 2],
                [2, 0],
                [3, 4],
                [4, 5],
                [5, 3],
                [6, 5],
            ],
        ),
        3,
    ],
    [
        (
            8,
            [[0, 1], [1, 2], [2, 0], [3, 4], [4, 3], [5, 6]],
        ),
        5,
    ],
    # Diamond DAG
    [(4, [[0, 1], [0, 2], [1, 3], [2, 3]]), 4],
    # Bidirectional components
    [
        (
            5,
            [[0, 1], [1, 0], [2, 3], [3, 2], [3, 4], [4, 3]],
        ),
        2,
    ],
    # Large single SCC
    [(10, [[i, (i + 1) % 10] for i in range(10)]), 1],
    # Two SCC blocks
    [
        (
            10,
            [[i, (i + 1) % 5] for i in range(5)]
            + [[i, 5 + ((i - 5 + 1) % 5)] for i in range(5, 10)],
        ),
        2,
    ],
    # Alternating connections
    [
        (
            6,
            [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5]],
        ),
        4,
    ],
    # Bridge between cycles
    [
        (
            6,
            [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [2, 3]],
        ),
        2,
    ],
    # Long chain with back edge
    [(20, [[i, i + 1] for i in range(19)] + [[19, 0]]), 1],
    # Many tiny SCCs
    [(20, [[i, i] for i in range(20)]), 20],
    # Dense but separated SCCs
    [
        (
            6,
            [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [0, 3]],
        ),
        2,
    ],
    # Large sparse chain
    [(50, [[i, i + 1] for i in range(49)]), 50],
    # Large cycle
    [(50, [[i, (i + 1) % 50] for i in range(50)]), 1],
    # Two large cycles connected one way
    [
        (
            20,
            [[i, (i + 1) % 10] for i in range(10)]
            + [[i, 10 + ((i - 10 + 1) % 10)] for i in range(10, 20)]
            + [[5, 15]],
        ),
        2,
    ],
    # Many isolated vertices plus one cycle
    [(10, [[0, 1], [1, 2], [2, 0]]), 8],
    # Bidirectional line
    [
        (
            6,
            [[i, i + 1] for i in range(5)] + [[i + 1, i] for i in range(5)],
        ),
        1,
    ],
    # Complex mixed graph
    [
        (
            12,
            [
                [0, 1],
                [1, 2],
                [2, 0],
                [3, 4],
                [4, 5],
                [5, 3],
                [6, 7],
                [8, 9],
                [9, 8],
                [10, 11],
            ],
        ),
        7,
    ],
    # Dense complete graph
    [
        (
            15,
            [[i, j] for i in range(15) for j in range(15) if i != j],
        ),
        1,
    ],
    # Large DAG
    [
        (
            30,
            [[i, j] for i in range(30) for j in range(i + 1, 30)],
        ),
        30,
    ],
    # Additional edge cases
    [(1, [[0, 0]]), 1],
    [(3, [[0, 1], [1, 2], [2, 1]]), 2],
    [(4, [[0, 1], [1, 0], [1, 2], [2, 3], [3, 2]]), 2],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(count_scc, test_cases))  # type: ignore  # noqa: F821
