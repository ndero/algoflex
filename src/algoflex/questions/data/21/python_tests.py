import sys

test_cases = [
    [([1, 5, 11, 5],), True],  # 11 vs 1+5+5
    [([6],), False],  # single element
    [([i for i in range(300)],), True],  # sum=44850, target=22425
    [([1, 5, 13, 5],), False],  # total=24, target=12 impossible
    [([1, 5, 11, 5] * 100,), True],  # repeated pattern
    [([1, 5, 13, 5, 35, 92, 11, 17, 13, 53],), False],
    [([i for i in range(1, 330, 2)],), False],  # odd numbers sum=27225 (odd)
    # Edge cases
    [([],), True],  # empty
    [([0],), True],  # single zero
    [([0, 0],), True],
    [([1, 1],), True],
    [([1, 1, 1],), False],  # sum=3 odd
    [([1, 2, 3],), True],  # 1+2=3
    [([1, 2, 3, 4, 5, 6, 7],), True],  # total=28, target=14
    [([1, 2, 5],), False],
    [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],), False],  # sum=55 odd
    [([1, 2, 3, 4, 5, 6, 7, 8, 9],), False],  # sum=45 odd
    [([1] * 100,), True],  # 100 ones (even count)
    [([2] * 99,), False],  # 99 twos (odd count)
]

if __name__ == "__main__":
    sys.exit(run_python_tests(can_partition, test_cases))  # type: ignore  # noqa: F821
