import sys

test_cases = [
    [([1, 4, 6, 7, 8, 20], [2, 7, 15]), 11],
    [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]), 17],
    [([1, 2, 3, 4, 5, 6, 7], [2, 7, 15]), 7],
    [([i for i in range(1, 31)], [2, 7, 15]), 15],
    [([1, 4, 6], [2, 7, 15]), 6],
    [([5, 6, 7, 8, 9, 10, 11], [2, 7, 15]), 7],
    [([5, 6, 7, 8, 9, 10, 11, 210, 211, 212, 213, 365], [2, 7, 15]), 16],
    [([i for i in range(1, 366)], [2, 7, 15]), 187],
    [([], [2, 7, 15]), 0],  # no travel days
    [([1], [2, 7, 15]), 2],  # single day
    [([1, 365], [2, 7, 15]), 4],  # two far apart days, daily is cheapest
    [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 7, 15]), 14],  # weekly cheaper than daily
]

if __name__ == "__main__":
    sys.exit(run_python_tests(min_cost_tickets, test_cases))  # type: ignore  # noqa: F821
