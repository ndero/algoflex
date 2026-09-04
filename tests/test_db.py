from pathlib import Path

import pytest

from algoflex import db
from algoflex.types import Attempt, Draft


@pytest.fixture
def test_db(tmp_path: Path):
    db_path = tmp_path / "algoflex_test.db"

    db._CONNECTION = None

    connection = db.get_db(db_path)

    yield connection

    connection.close()
    db._CONNECTION = None


def test_database_initializes(test_db):
    tables = {
        row["name"]
        for row in test_db.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            """
        )
    }

    assert tables >= {"languages", "attempts", "drafts"}


def test_languages_are_initialized(test_db):
    rows = test_db.execute(
        "SELECT lang_id, lang FROM languages ORDER BY lang_id"
    ).fetchall()

    assert len(rows) == len(db.Language)
    assert {row["lang"] for row in rows} == {language.slug for language in db.Language}


def test_foreign_keys_are_enabled(test_db):
    enabled = test_db.execute("PRAGMA foreign_keys").fetchone()[0]

    assert enabled == 1


def test_add_attempt(test_db):
    attempt: Attempt = {
        "problem_id": 42,
        "status": db.RunStatus.PASSED,
        "elapsed": 1.25,
        "created_at": 1000.0,
        "code": "print('hello')",
        "lang_id": db.Language.PYTHON,
    }

    db.add_attempt(attempt)

    row = test_db.execute("SELECT * FROM attempts").fetchone()

    assert row["problem_id"] == 42
    assert row["status"] == db.RunStatus.PASSED
    assert row["elapsed"] == 1.25
    assert row["created_at"] == 1000.0
    assert row["code"] == "print('hello')"
    assert row["lang_id"] == db.Language.PYTHON


def test_problem_pass_ratio_counts_passed_and_total(test_db):
    attempts: list[Attempt] = [
        {
            "problem_id": 1,
            "status": db.RunStatus.PASSED,
            "elapsed": 1.0,
            "created_at": 1.0,
            "code": "pass",
            "lang_id": db.Language.PYTHON,
        },
        {
            "problem_id": 1,
            "status": db.RunStatus.FAILED,
            "elapsed": 2.0,
            "created_at": 2.0,
            "code": "fail",
            "lang_id": db.Language.PYTHON,
        },
        {
            "problem_id": 1,
            "status": db.RunStatus.PASSED,
            "elapsed": 3.0,
            "created_at": 3.0,
            "code": "pass",
            "lang_id": db.Language.PYTHON,
        },
    ]

    for attempt in attempts:
        db.add_attempt(attempt)

    assert db.get_problem_pass_ratio(1) == (2, 3)


def test_problem_pass_ratio_for_unknown_problem(test_db):
    assert db.get_problem_pass_ratio(999) == (0, 0)


def test_get_recent_attempts_orders_by_created_at_desc(test_db):
    for created_at in (10.0, 30.0, 20.0):
        db.add_attempt(
            {
                "problem_id": 1,
                "status": db.RunStatus.PASSED,
                "elapsed": created_at,
                "created_at": created_at,
                "code": str(created_at),
                "lang_id": db.Language.PYTHON,
            }
        )

    rows = db.get_recent_attempts(2)

    assert [row["created_at"] for row in rows] == [30.0, 20.0]


def test_get_recent_attempts_filters_by_problem(test_db):
    for problem_id, created_at in ((1, 10.0), (2, 20.0), (1, 30.0)):
        db.add_attempt(
            {
                "problem_id": problem_id,
                "status": db.RunStatus.PASSED,
                "elapsed": 1.0,
                "created_at": created_at,
                "code": "pass",
                "lang_id": db.Language.PYTHON,
            }
        )

    rows = db.get_recent_attempts(n=-1, problem_id=1)

    assert [row["created_at"] for row in rows] == [30.0, 10.0]


def test_get_recent_attempts_breaks_timestamp_tie_with_attempt_id(test_db):
    for code in ("first", "second"):
        db.add_attempt(
            {
                "problem_id": 1,
                "status": db.RunStatus.PASSED,
                "elapsed": 1.0,
                "created_at": 100.0,
                "code": code,
                "lang_id": db.Language.PYTHON,
            }
        )

    rows = db.get_recent_attempts(2)

    assert [row["code"] for row in rows] == ["second", "first"]


def test_get_best_attempts_only_uses_passed_attempts(test_db):
    db.add_attempt(
        {
            "problem_id": 1,
            "status": db.RunStatus.FAILED,
            "elapsed": 0.1,
            "created_at": 1.0,
            "code": "failed",
            "lang_id": db.Language.PYTHON,
        }
    )

    db.add_attempt(
        {
            "problem_id": 1,
            "status": db.RunStatus.PASSED,
            "elapsed": 2.0,
            "created_at": 2.0,
            "code": "passed",
            "lang_id": db.Language.PYTHON,
        }
    )

    rows = db.get_best_attempts(problem_id=1)

    assert len(rows) == 1
    assert rows[0]["code"] == "passed"


def test_get_best_attempts_returns_fastest_attempt(test_db):
    for elapsed in (5.0, 2.0, 3.0):
        db.add_attempt(
            {
                "problem_id": 1,
                "status": db.RunStatus.PASSED,
                "elapsed": elapsed,
                "created_at": elapsed,
                "code": str(elapsed),
                "lang_id": db.Language.PYTHON,
            }
        )

    rows = db.get_best_attempts(n=-1, problem_id=1)

    assert [row["elapsed"] for row in rows] == [2.0, 3.0, 5.0]


def test_get_best_attempts_returns_best_per_problem(test_db):
    attempts = [
        (1, 5.0),
        (1, 2.0),
        (2, 8.0),
        (2, 3.0),
        (3, 1.0),
    ]

    for problem_id, elapsed in attempts:
        db.add_attempt(
            {
                "problem_id": problem_id,
                "status": db.RunStatus.PASSED,
                "elapsed": elapsed,
                "created_at": elapsed,
                "code": str(elapsed),
                "lang_id": db.Language.PYTHON,
            }
        )

    rows = db.get_best_attempts(n=-1)

    assert [(row["problem_id"], row["elapsed"]) for row in rows] == [
        (3, 1.0),
        (1, 2.0),
        (2, 3.0),
    ]


def test_get_attempts_today_counts_today_only(test_db, monkeypatch):
    monkeypatch.setattr(db, "midnight", lambda: 100.0)

    attempts = [
        (1, db.RunStatus.PASSED, 99.0),  # yesterday
        (1, db.RunStatus.PASSED, 100.0),  # today
        (2, db.RunStatus.FAILED, 110.0),  # today
        (3, db.RunStatus.PASSED, 120.0),  # today
    ]

    for problem_id, status, created_at in attempts:
        db.add_attempt(
            {
                "problem_id": problem_id,
                "status": status,
                "elapsed": 1.0,
                "created_at": created_at,
                "code": "code",
                "lang_id": db.Language.PYTHON,
            }
        )

    assert db.get_attempts_today() == (2, 3)


def test_get_passed_problem_ids(test_db):
    for problem_id, status in (
        (1, db.RunStatus.PASSED),
        (1, db.RunStatus.FAILED),
        (2, db.RunStatus.PASSED),
        (3, db.RunStatus.FAILED),
    ):
        db.add_attempt(
            {
                "problem_id": problem_id,
                "status": status,
                "elapsed": 1.0,
                "created_at": 1.0,
                "code": "code",
                "lang_id": db.Language.PYTHON,
            }
        )

    assert db.get_passed_problem_ids() == {1, 2}


def test_get_passed_problem_ids_empty(test_db):
    assert db.get_passed_problem_ids() == set()


def test_get_most_attempted_problems(test_db):
    attempts = [
        (1, db.RunStatus.PASSED),
        (1, db.RunStatus.FAILED),
        (1, db.RunStatus.PASSED),
        (2, db.RunStatus.PASSED),
        (2, db.RunStatus.FAILED),
        (3, db.RunStatus.PASSED),
    ]

    for problem_id, status in attempts:
        db.add_attempt(
            {
                "problem_id": problem_id,
                "status": status,
                "elapsed": 1.0,
                "created_at": 1.0,
                "code": "code",
                "lang_id": db.Language.PYTHON,
            }
        )

    rows = db.get_most_attempted_problems(3)

    assert [
        (row["problem_id"], row["total_count"], row["passed_count"]) for row in rows
    ] == [
        (1, 3, 2),
        (2, 2, 1),
        (3, 1, 1),
    ]


def test_attempts_preserve_language(test_db):
    db.add_attempt(
        {
            "problem_id": 1,
            "status": db.RunStatus.PASSED,
            "elapsed": 1.0,
            "created_at": 1.0,
            "code": "print('python')",
            "lang_id": db.Language.PYTHON,
        }
    )

    db.add_attempt(
        {
            "problem_id": 1,
            "status": db.RunStatus.PASSED,
            "elapsed": 2.0,
            "created_at": 2.0,
            "code": "fn main() {}",
            "lang_id": db.Language.RUST,
        }
    )

    rows = db.get_recent_attempts(2)

    assert [row["lang_id"] for row in rows] == [
        db.Language.RUST,
        db.Language.PYTHON,
    ]


def test_add_and_get_draft(test_db):
    draft: Draft = {
        "problem_id": 10,
        "lang_id": db.Language.PYTHON,
        "code": "print('hello')",
        "elapsed": 5.5,
        "updated_at": 100.0,
    }

    db.add_draft(draft)

    row = db.get_draft(10, db.Language.PYTHON)

    assert row is not None
    assert row["problem_id"] == 10
    assert row["lang_id"] == db.Language.PYTHON
    assert row["code"] == "print('hello')"
    assert row["elapsed"] == 5.5
    assert row["updated_at"] == 100.0


def test_get_missing_draft_returns_none(test_db):
    assert db.get_draft(999, db.Language.PYTHON) is None


def test_add_draft_updates_existing_draft(test_db):
    db.add_draft(
        {
            "problem_id": 10,
            "lang_id": db.Language.PYTHON,
            "code": "first",
            "elapsed": 1.0,
            "updated_at": 100.0,
        }
    )

    db.add_draft(
        {
            "problem_id": 10,
            "lang_id": db.Language.PYTHON,
            "code": "second",
            "elapsed": 2.0,
            "updated_at": 200.0,
        }
    )

    row = db.get_draft(10, db.Language.PYTHON)

    assert row["code"] == "second"
    assert row["elapsed"] == 2.0
    assert row["updated_at"] == 200.0


def test_drafts_are_separate_per_language(test_db):
    db.add_draft(
        {
            "problem_id": 10,
            "lang_id": db.Language.PYTHON,
            "code": "python code",
            "elapsed": 1.0,
            "updated_at": 100.0,
        }
    )

    db.add_draft(
        {
            "problem_id": 10,
            "lang_id": db.Language.RUST,
            "code": "rust code",
            "elapsed": 2.0,
            "updated_at": 200.0,
        }
    )

    assert db.get_draft(10, db.Language.PYTHON)["code"] == "python code"
    assert db.get_draft(10, db.Language.RUST)["code"] == "rust code"


def test_delete_draft(test_db):
    db.add_draft(
        {
            "problem_id": 10,
            "lang_id": db.Language.PYTHON,
            "code": "print('hello')",
            "elapsed": 1.0,
            "updated_at": 100.0,
        }
    )

    db.delete_draft(10, db.Language.PYTHON)

    assert db.get_draft(10, db.Language.PYTHON) is None


def test_delete_missing_draft_is_noop(test_db):
    db.delete_draft(999, db.Language.PYTHON)
