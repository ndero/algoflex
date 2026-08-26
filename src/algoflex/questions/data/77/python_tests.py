import sys

calendar = MyCalendar()  # type: ignore # noqa: F821

test_cases = [
    [(10, 20), True],
    [(10, 20), False],
    [(15, 25), False],
    [(20, 30), True],
    [(30, 31), True],
    [(100, 2000), True],
    [(2_000, 6_000_000), True],
    [(3_000, 50_000), False],
    [(10_000, 20_000), False],
    [(0, 6_000_000), False],
    [(55_556, 3_000_000), False],
    [(2000, 2020), False],
    [(5_999_999, 6_000_001), False],
    [(100_000, 200_000), False],
    [(31, 41), True],
    [(42, 50), True],
    [(50, 60), True],
    [(60, 70), True],
    [(70, 80), True],
    [(80, 90), True],
    [(90, 100), True],
]

if __name__ == "__main__":
    sys.exit(
        run_python_tests(  # type: ignore # noqa: F821
            lambda start, end: calendar.book(start, end), test_cases
        )
    )
