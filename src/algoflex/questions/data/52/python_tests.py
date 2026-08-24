import sys

network = (
    [[i, i + 1, i * 100] for i in range(1, 10)]
    + [[i, i + 2, 100] for i in range(1, 10, 2)]
    + [[10, 1, 10_000]]
)

test_cases = [
    [([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2],
    [([[1, 2, 1]], 2, 1), 1],
    [([[1, 2, 1]], 4, 2), -1],
    [([[1, 2, 6]], 2, 1), 6],
    [([[1, 2, 6]], 2, 2), -1],
    [(network, 11, 1), 1300],
    [(network, 11, 2), 11400],
    [(network, 11, 11), -1],
    [(network, 11, 5), 11500],
    # edge case
    [([], 1, 1), 0],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(min_network_delay, test_cases))  # type: ignore  # noqa: F821
