import sqlite3
import sys
from collections import Counter
from collections.abc import Iterable, Sequence
from itertools import islice
from pathlib import Path


def format_result(
    rows: Iterable[Sequence[object]],
    columns: Sequence[str],
    *,
    max_columns: int = 5,
    max_rows: int = 10,
    max_length: int = 100,
) -> str:
    """Format SQL query results as a readable table."""

    if min(max_columns, max_rows, max_length) < 1:
        raise ValueError("Formatting limits must be positive.")

    columns = list(columns)

    if not columns:
        return "(no columns to display)"

    # Fetch at most one extra row to detect truncation.
    rows = list(islice(rows, max_rows + 1))

    has_more_rows = len(rows) > max_rows
    rows = rows[:max_rows]

    displayed_columns = columns[:max_columns]
    omitted_columns = len(columns) - len(displayed_columns)

    def truncate(value: str) -> str:
        if len(value) <= max_length:
            return value

        if max_length <= 3:
            return value[:max_length]

        return value[: max_length - 3] + "..."

    def format_cell(value: object) -> str:
        return truncate(repr(value))

    headers = [truncate(str(column)) for column in displayed_columns]

    data = []

    for row in rows:
        values = [format_cell(value) for value in row[: len(displayed_columns)]]

        # Keep every row aligned with the displayed headers.
        values.extend([""] * (len(headers) - len(values)))
        data.append(values)

    # Include the headers even when there are no result rows.
    widths = [
        max([len(headers[i]), *(len(row[i]) for row in data)])
        for i in range(len(headers))
    ]

    def format_row(values: Sequence[str]) -> str:
        return " | ".join(value.ljust(widths[i]) for i, value in enumerate(values))

    separator = "-+-".join("-" * width for width in widths)

    result = [
        format_row(headers),
        separator,
    ]

    if data:
        result.extend(format_row(row) for row in data)
    else:
        result.append("(no rows returned)")

    if has_more_rows:
        result.append("... additional rows omitted")

    if omitted_columns:
        result.append(f"... {omitted_columns} additional columns omitted")

    return "\n".join(result)


def color_result(result: str, color: str) -> str:
    return "\n".join(f"[{color}]{line}[/{color}]" for line in result.splitlines())


def _sql_query_authorizer(
    action: int,
    arg1: str | None,
    arg2: str | None,
    database_name: str | None,
    trigger_name: str | None,
) -> int:
    """Allow read-only SQL queries."""

    allowed_actions = {
        sqlite3.SQLITE_SELECT,
        sqlite3.SQLITE_READ,
        sqlite3.SQLITE_FUNCTION,
    }

    recursive_action = getattr(sqlite3, "SQLITE_RECURSIVE", None)

    if recursive_action is not None:
        allowed_actions.add(recursive_action)

    if action not in allowed_actions:
        return sqlite3.SQLITE_DENY

    if action == sqlite3.SQLITE_FUNCTION:
        function_name = (arg2 or arg1 or "").lower()

        if function_name == "load_extension":
            return sqlite3.SQLITE_DENY

    return sqlite3.SQLITE_OK


def run_sql_tests(
    sql: str,
    tests_path: str | Path,
    *,
    max_rows: int = 1_000,
) -> int:
    """Run a SQL query against the expected results for a question."""

    connection = None

    try:
        # Set up the database using the question's trusted test script.
        connection = sqlite3.connect(":memory:")
        connection.executescript(Path(tests_path).read_text(encoding="utf-8"))

        # Retrieve the expected result column names.
        columns = [
            row[1] for row in connection.execute("PRAGMA table_info(expected_results)")
        ]

        if not columns or columns[0] != "position":
            raise ValueError("expected_results must start with a 'position' column")

        expected_columns = columns[1:]

        if not expected_columns:
            raise ValueError("expected_results must define at least one result column")

        # Position controls ordering but is not part of the query output.
        expected_rows = [
            tuple(row[1:])
            for row in connection.execute(
                "SELECT * FROM expected_results ORDER BY position"
            )
        ]

        # Read problem configs to check if result should be ordered or not.
        config = connection.execute("SELECT ordered FROM test_config").fetchone()

        if config is None:
            raise ValueError("test_config must contain an ordering setting")

        if config[0] not in (0, 1):
            raise ValueError("test_config.ordered must be 0 or 1")

        ordered = bool(config[0])

        connection.execute("DROP TABLE expected_results")
        connection.execute("DROP TABLE test_config")
        # Restrict the submitted query to read-only operations.
        connection.execute("PRAGMA query_only = ON")
        connection.set_authorizer(_sql_query_authorizer)

        # Execute the submitted query and collect its results.
        try:
            cursor = connection.execute(sql)

            if cursor.description is None:
                print(
                    "[b]x[/] test case 1\t[red]... FAIL[/]\n"
                    "\t[b]error[/]: Query returned no result set."
                )
                return 1

            actual_columns = [column[0] for column in cursor.description]

            # Fetch one extra row to detect excessive results.
            actual_rows = [tuple(row) for row in cursor.fetchmany(max_rows + 1)]

        except sqlite3.Error as exc:
            if "not authorized" in str(exc).lower():
                message = "Only read-only SELECT queries are allowed."
            else:
                message = str(exc)

            print(f"[b]x[/] test case 1\t[red]... ERROR[/]\n\t[b]error[/]: {message}")
            return 1

        # Reject unexpectedly large result sets.
        if len(actual_rows) > max_rows:
            print(
                "[b]x[/] test case 1\t[red]... FAIL[/]\n"
                f"\t[b]error[/]: Query returned more than "
                f"{max_rows:,} rows."
            )
            return 1

        # Compare results
        if ordered:
            passed = actual_rows == expected_rows
        else:
            passed = Counter(actual_rows) == Counter(expected_rows)

        if not passed:
            got = color_result(
                format_result(actual_rows, actual_columns),
                "red",
            )
            expected = color_result(
                format_result(expected_rows, expected_columns),
                "green",
            )

            print(
                "[b]x[/] test case 1\t[red]... FAIL[/]\n"
                f"\n[b]got[/]:\n\n{got}\n"
                f"\n\n[b]expected[/]:\n\n{expected}"
            )
            return 1

        print("[b]✓[/] test case 1\t[green]... ok[/]")
        print("\n passed!")

        return 0

    except (OSError, sqlite3.Error, ValueError) as exc:
        print(f"[b]x[/] SQL test setup\t[red]... ERROR[/]\n\t[b]error[/]: {exc!s}")
        return 1

    finally:
        if connection is not None:
            connection.close()


def main() -> int:
    try:
        tests_path = Path(sys.argv[2])
        sql_path = Path(sys.argv[1])
        sql = sql_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(
            f"Failed to read SQL submission: {exc}",
            file=sys.stderr,
        )
        return 1

    return run_sql_tests(sql, tests_path)


if __name__ == "__main__":
    raise SystemExit(main())
