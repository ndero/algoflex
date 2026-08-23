import sys


def _generate_parentheses(n: int) -> list[str]:
    res, path = [], []

    def backtrack(open: int, close: int) -> None:
        if len(path) == 2 * n:
            res.append("".join(path))
            return
        if open < n:
            path.append("(")
            backtrack(open + 1, close)
            path.pop()
        if close < open:
            path.append(")")
            backtrack(open, close + 1)
            path.pop()

    backtrack(0, 0)
    return res


test_cases = [
    [(3,), _generate_parentheses(3)],
    [(1,), _generate_parentheses(1)],
    [(2,), _generate_parentheses(2)],
    [(0,), _generate_parentheses(0)],
    [(12,), _generate_parentheses(12)],
    [(5,), _generate_parentheses(5)],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(_generate_parentheses, test_cases))  # type: ignore  # noqa: F821
