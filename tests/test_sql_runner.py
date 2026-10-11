"""
pytest suite for the SQL test-runner module.
"""

import sqlite3
import sys
from pathlib import Path

import pytest

from algoflex.sql_runner import (
    _sql_query_authorizer,
    color_result,
    format_result,
    main,
    run_sql_tests,
)


# Helpers
def write_setup(tmp_path: Path, body: str) -> Path:
    path = tmp_path / "setup.sql"
    path.write_text(body, encoding="utf-8")
    return path


def minimal_setup(*, ordered: int = 1) -> str:
    return f"""
    CREATE TABLE test_config (ordered INTEGER NOT NULL CHECK (ordered IN (0, 1)));
    INSERT INTO test_config (ordered) VALUES ({ordered});

    CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
    INSERT INTO users (id, name) VALUES (1, 'Alice'), (2, 'Bob');

    CREATE TABLE expected_results (
        position INTEGER PRIMARY KEY,
        id       INTEGER NOT NULL,
        name     TEXT    NOT NULL
    );
    INSERT INTO expected_results (position, id, name) VALUES
        (1, 1, 'Alice'),
        (2, 2, 'Bob');
    """


# format_result
class TestFormatResult:
    def test_no_columns(self):
        assert format_result([], []) == "(no columns to display)"

    @pytest.mark.parametrize(
        "kwargs",
        [
            {"max_columns": 0},
            {"max_rows": 0},
            {"max_length": 0},
            {"max_columns": -1},
            {"max_rows": -5},
            {"max_length": -2},
        ],
    )
    def test_invalid_limits_raise(self, kwargs):
        with pytest.raises(ValueError):
            format_result([], ["a"], **kwargs)

    def test_basic_formatting(self):
        out = format_result([(1, "Alice"), (2, "Bob")], ["id", "name"])
        lines = out.splitlines()
        # header row, separator row, 2 data rows
        assert len(lines) == 4
        assert "id" in lines[0]
        assert "name" in lines[0]
        assert "Alice" in lines[2]
        assert "Bob" in lines[3]

    def test_no_rows_placeholder(self):
        out = format_result([], ["id"])
        assert "(no rows returned)" in out

    def test_row_truncation(self):
        rows = [(i,) for i in range(50)]
        out = format_result(rows, ["n"], max_rows=5)
        assert "... additional rows omitted" in out
        # Only the first five rows should be present.
        assert "4" in out
        assert "5" not in out

    def test_no_row_truncation_when_exact(self):
        rows = [(i,) for i in range(5)]
        out = format_result(rows, ["n"], max_rows=5)
        assert "... additional rows omitted" not in out

    def test_column_truncation(self):
        out = format_result([(1, 2, 3, 4)], ["a", "b", "c", "d"], max_columns=2)
        assert "... 2 additional columns omitted" in out

    def test_cell_value_truncation(self):
        long = "x" * 200
        out = format_result([(long,)], ["col"], max_length=10)
        # repr(long) is 202 chars; truncated to first 7 + "..."
        assert "'xxxxxx..." in out

    def test_cell_value_truncation_short_max_length(self):
        # max_length <= 3 -> no ellipsis, just a hard cut.
        out = format_result([("abcde",)], ["col"], max_length=3)
        # repr("abcde") == "'abcde'"; value[:3] == "'ab"
        assert "'ab" in out
        assert "abcde" not in out

    def test_repr_is_used_for_values(self):
        out = format_result([(None, "hello")], ["a", "b"])
        assert "None" in out
        assert "'hello'" in out

    def test_short_row_padded_with_blanks(self):
        # A row shorter than the headers should not crash and should be padded.
        out = format_result([(1,)], ["a", "b"])
        # We do not assert exact spacing, only that it doesn't blow up.
        assert "1" in out

    def test_header_truncation(self):
        out = format_result([(1,)], ["x" * 50], max_length=10)
        assert "..." in out


# color_result
class TestColorResult:
    def test_single_line(self):
        assert color_result("hello", "red") == "[red]hello[/red]"

    def test_multiple_lines(self):
        out = color_result("a\nb\nc", "green")
        assert out == "[green]a[/green]\n[green]b[/green]\n[green]c[/green]"

    def test_empty_string(self):
        assert color_result("", "blue") == ""


# _sql_query_authorizer
class TestSqlQueryAuthorizer:
    def test_select_allowed(self):
        assert (
            _sql_query_authorizer(sqlite3.SQLITE_SELECT, None, None, None, None)
            == sqlite3.SQLITE_OK
        )

    def test_read_allowed(self):
        assert (
            _sql_query_authorizer(sqlite3.SQLITE_READ, "users", "id", "main", None)
            == sqlite3.SQLITE_OK
        )

    def test_function_allowed(self):
        assert (
            _sql_query_authorizer(sqlite3.SQLITE_FUNCTION, None, "upper", None, None)
            == sqlite3.SQLITE_OK
        )

    def test_load_extension_denied(self):
        assert (
            _sql_query_authorizer(
                sqlite3.SQLITE_FUNCTION, None, "load_extension", None, None
            )
            == sqlite3.SQLITE_DENY
        )

    def test_load_extension_denied_case_insensitive(self):
        assert (
            _sql_query_authorizer(
                sqlite3.SQLITE_FUNCTION, "Load_Extension", None, None, None
            )
            == sqlite3.SQLITE_DENY
        )

    @pytest.mark.parametrize(
        "action",
        [
            sqlite3.SQLITE_INSERT,
            sqlite3.SQLITE_UPDATE,
            sqlite3.SQLITE_DELETE,
            sqlite3.SQLITE_CREATE_TABLE,
            sqlite3.SQLITE_DROP_TABLE,
            sqlite3.SQLITE_ALTER_TABLE,
        ],
    )
    def test_write_actions_denied(self, action):
        assert (
            _sql_query_authorizer(action, "users", "name", "main", None)
            == sqlite3.SQLITE_DENY
        )

    def test_recursive_allowed_when_available(self):
        recursive = getattr(sqlite3, "SQLITE_RECURSIVE", None)
        if recursive is None:
            pytest.skip("SQLITE_RECURSIVE not exposed by this sqlite3 build")
        assert (
            _sql_query_authorizer(recursive, None, None, None, None)
            == sqlite3.SQLITE_OK
        )


# run_sql_tests – success paths
class TestRunSqlTestsSuccess:
    def test_ordered_match(self, tmp_path, capsys):
        setup = write_setup(tmp_path, minimal_setup(ordered=1))
        rc = run_sql_tests("SELECT id, name FROM users ORDER BY id", setup)
        captured = capsys.readouterr().out
        assert rc == 0
        assert "ok" in captured.lower()

    def test_ordered_match_with_extra_ordering_column(self, tmp_path):
        # Ordering determined by the expected_results position column,
        # not the query's ORDER BY.
        setup = write_setup(tmp_path, minimal_setup(ordered=1))
        assert run_sql_tests("SELECT id, name FROM users ORDER BY id ASC", setup) == 0

    def test_unordered_match_same_order(self, tmp_path):
        setup = write_setup(tmp_path, minimal_setup(ordered=0))
        assert run_sql_tests("SELECT id, name FROM users ORDER BY id", setup) == 0

    def test_unordered_match_reversed_order(self, tmp_path):
        # Unordered comparison uses Counter, so any order must pass.
        setup = write_setup(tmp_path, minimal_setup(ordered=0))
        assert run_sql_tests("SELECT id, name FROM users ORDER BY id DESC", setup) == 0

    def test_recursive_cte_allowed(self, tmp_path):
        body = """
        CREATE TABLE test_config (ordered INTEGER NOT NULL);
        INSERT INTO test_config (ordered) VALUES (1);

        CREATE TABLE expected_results (
            position INTEGER PRIMARY KEY,
            n INTEGER NOT NULL
        );
        INSERT INTO expected_results (position, n) VALUES (1, 1), (2, 2), (3, 3);
        """
        setup = write_setup(tmp_path, body)
        sql = (
            "WITH RECURSIVE cnt(n) AS ("
            "  SELECT 1 UNION ALL SELECT n+1 FROM cnt WHERE n < 3"
            ") SELECT n FROM cnt ORDER BY n"
        )
        assert run_sql_tests(sql, setup) == 0


# run_sql_tests – failure paths
class TestRunSqlTestsFailures:
    def test_ordered_mismatch(self, tmp_path, capsys):
        setup = write_setup(tmp_path, minimal_setup(ordered=1))
        rc = run_sql_tests("SELECT id, name FROM users ORDER BY id DESC", setup)
        assert rc == 1
        out = capsys.readouterr().out
        assert "FAIL" in out

    def test_wrong_row_count(self, tmp_path):
        setup = write_setup(tmp_path, minimal_setup(ordered=1))
        assert run_sql_tests("SELECT id, name FROM users WHERE id = 1", setup) == 1

    def test_wrong_column_count(self, tmp_path):
        setup = write_setup(tmp_path, minimal_setup(ordered=0))
        assert run_sql_tests("SELECT id FROM users", setup) == 1

    def test_extra_rows_beyond_max(self, tmp_path, capsys):
        body = """
        CREATE TABLE test_config (ordered INTEGER NOT NULL);
        INSERT INTO test_config (ordered) VALUES (0);

        CREATE TABLE expected_results (
            position INTEGER PRIMARY KEY,
            n INTEGER NOT NULL
        );
        INSERT INTO expected_results (position, n) VALUES (1, 1);
        """
        setup = write_setup(tmp_path, body)
        sql = (
            "WITH RECURSIVE cnt(n) AS ("
            "  SELECT 1 UNION ALL SELECT n+1 FROM cnt WHERE n < 100"
            ") SELECT n FROM cnt"
        )
        rc = run_sql_tests(sql, setup, max_rows=10)
        assert rc == 1
        out = capsys.readouterr().out
        assert "10" in out

    def test_write_statement_denied(self, tmp_path, capsys):
        setup = write_setup(tmp_path, minimal_setup(ordered=1))
        rc = run_sql_tests("INSERT INTO users (id, name) VALUES (99, 'Zed')", setup)
        assert rc == 1
        out = capsys.readouterr().out
        assert "read-only" in out.lower()

    def test_load_extension_denied_in_query(self, tmp_path):
        setup = write_setup(tmp_path, minimal_setup(ordered=1))
        rc = run_sql_tests("SELECT load_extension('evil.so')", setup)
        assert rc == 1

    def test_sql_syntax_error(self, tmp_path, capsys):
        setup = write_setup(tmp_path, minimal_setup(ordered=1))
        rc = run_sql_tests("SELEKT nope", setup)
        assert rc == 1
        out = capsys.readouterr().out
        assert "ERROR" in out or "FAIL" in out


# run_sql_tests – setup validation
class TestRunSqlTestsSetupValidation:
    def test_missing_position_column(self, tmp_path, capsys):
        body = """
        CREATE TABLE test_config (ordered INTEGER NOT NULL);
        INSERT INTO test_config (ordered) VALUES (1);

        CREATE TABLE expected_results (
            id INTEGER NOT NULL,
            name TEXT NOT NULL
        );
        INSERT INTO expected_results (id, name) VALUES (1, 'Alice');
        """
        setup = write_setup(tmp_path, body)
        rc = run_sql_tests("SELECT 1 AS id, 'x' AS name", setup)
        assert rc == 1
        out = capsys.readouterr().out
        assert "position" in out.lower()

    def test_no_columns_beyond_position(self, tmp_path, capsys):
        body = """
        CREATE TABLE test_config (ordered INTEGER NOT NULL);
        INSERT INTO test_config (ordered) VALUES (1);

        CREATE TABLE expected_results (
            position INTEGER PRIMARY KEY
        );
        """
        setup = write_setup(tmp_path, body)
        rc = run_sql_tests("SELECT 1 AS id", setup)
        assert rc == 1
        out = capsys.readouterr().out
        assert "column" in out.lower()

    def test_missing_test_config(self, tmp_path, capsys):
        body = """
        CREATE TABLE expected_results (
            position INTEGER PRIMARY KEY,
            id INTEGER NOT NULL
        );
        INSERT INTO expected_results (position, id) VALUES (1, 1);
        """
        setup = write_setup(tmp_path, body)
        rc = run_sql_tests("SELECT 1 AS id", setup)
        assert rc == 1
        out = capsys.readouterr().out
        assert "ERROR" in out or "error" in out.lower()

    def test_empty_test_config(self, tmp_path, capsys):
        body = """
        CREATE TABLE test_config (ordered INTEGER NOT NULL);

        CREATE TABLE expected_results (
            position INTEGER PRIMARY KEY,
            id INTEGER NOT NULL
        );
        INSERT INTO expected_results (position, id) VALUES (1, 1);
        """
        setup = write_setup(tmp_path, body)
        rc = run_sql_tests("SELECT 1 AS id", setup)
        assert rc == 1
        out = capsys.readouterr().out
        assert "ordered" in out.lower() or "test_config" in out.lower()

    def test_invalid_ordered_value(self, tmp_path, capsys):
        # No CHECK constraint, so the row is stored even though it's invalid.
        body = """
        CREATE TABLE test_config (ordered INTEGER NOT NULL);
        INSERT INTO test_config (ordered) VALUES (2);

        CREATE TABLE expected_results (
            position INTEGER PRIMARY KEY,
            id INTEGER NOT NULL
        );
        INSERT INTO expected_results (position, id) VALUES (1, 1);
        """
        setup = write_setup(tmp_path, body)
        rc = run_sql_tests("SELECT 1 AS id", setup)
        assert rc == 1
        out = capsys.readouterr().out
        assert "0 or 1" in out

    def test_missing_setup_file(self, tmp_path, capsys):
        missing = tmp_path / "does_not_exist.sql"
        rc = run_sql_tests("SELECT 1", missing)
        assert rc == 1
        out = capsys.readouterr().out
        assert "ERROR" in out

    def test_broken_setup_sql(self, tmp_path, capsys):
        setup = write_setup(tmp_path, "CREATE TABL oops (")
        rc = run_sql_tests("SELECT 1", setup)
        assert rc == 1
        out = capsys.readouterr().out
        assert "ERROR" in out


# main
class TestMain:
    def test_missing_arguments(self, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["prog"])
        with pytest.raises(IndexError):
            main()

    def test_sql_file_missing(self, monkeypatch, tmp_path, capsys):
        tests_path = tmp_path / "tests.sql"
        tests_path.write_text(minimal_setup(), encoding="utf-8")
        missing_sql = tmp_path / "nope.sql"
        monkeypatch.setattr(sys, "argv", ["prog", str(missing_sql), str(tests_path)])
        rc = main()
        assert rc == 1
        err = capsys.readouterr().err
        assert "Failed to read SQL submission" in err

    def test_run_success(self, monkeypatch, tmp_path, capsys):
        tests_path = tmp_path / "tests.sql"
        tests_path.write_text(minimal_setup(ordered=1), encoding="utf-8")

        sql_path = tmp_path / "query.sql"
        sql_path.write_text("SELECT id, name FROM users ORDER BY id", encoding="utf-8")

        monkeypatch.setattr(sys, "argv", ["prog", str(sql_path), str(tests_path)])
        assert main() == 0
        out = capsys.readouterr().out
        assert "ok" in out.lower()

    def test_run_failure(self, monkeypatch, tmp_path, capsys):
        tests_path = tmp_path / "tests.sql"
        tests_path.write_text(minimal_setup(ordered=1), encoding="utf-8")

        sql_path = tmp_path / "query.sql"
        sql_path.write_text("SELECT id FROM users", encoding="utf-8")

        monkeypatch.setattr(sys, "argv", ["prog", str(sql_path), str(tests_path)])
        assert main() == 1
        out = capsys.readouterr().out
        assert "FAIL" in out
