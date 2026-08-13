import sqlite3
from pathlib import Path
from typing import TypedDict

from platformdirs import user_data_dir

APP_NAME = "algoflex"
_CONNECTION: sqlite3.Connection | None = None


class Attempt(TypedDict):
    problem_id: int
    passed: bool
    elapsed: float
    created_at: float
    code: str
    lang_id: int


class Draft(TypedDict):
    problem_id: int
    lang_id: int
    code: str
    elapsed: float
    updated_at: float


def get_db() -> sqlite3.Connection:
    """Returns Algoflex sqlite3 database connection"""
    global _CONNECTION

    if _CONNECTION is not None:
        return _CONNECTION

    db_dir = Path(user_data_dir(APP_NAME))
    db_dir.mkdir(parents=True, exist_ok=True)
    db_path = db_dir / "algoflex.db"
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")

    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS languages (
            lang_id INTEGER PRIMARY KEY,
            lang TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS attempts (
            attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
            problem_id INTEGER NOT NULL,
            passed INTEGER NOT NULL,
            elapsed REAL NOT NULL,
            created_at REAL NOT NULL,
            code TEXT NOT NULL,
            lang_id INTEGER NOT NULL,
            FOREIGN KEY (lang_id) REFERENCES languages(lang_id)
        );

        CREATE TABLE IF NOT EXISTS drafts (
            problem_id INTEGER NOT NULL,
            lang_id INTEGER NOT NULL,
            code TEXT NOT NULL,
            elapsed REAL NOT NULL,
            updated_at REAL NOT NULL,
            PRIMARY KEY (problem_id, lang_id),
            FOREIGN KEY (lang_id) REFERENCES languages(lang_id)
        );

        CREATE INDEX IF NOT EXISTS idx_attempts_problem ON attempts(problem_id);

        CREATE INDEX IF NOT EXISTS idx_attempts_created ON attempts(created_at);

        CREATE INDEX IF NOT EXISTS idx_attempts_lang ON attempts(lang_id);

        """
    )

    db.executemany(
        """
        INSERT OR IGNORE INTO languages (lang_id, lang)
        VALUES (?, ?)
        """,
        [
            (1, "python"),
            (2, "rust"),
        ],
    )

    db.commit()

    _CONNECTION = db
    return db


def add_attempt(attempt: Attempt) -> None:
    db = get_db()
    with db:
        db.execute(
            """
            INSERT INTO attempts (
                problem_id,
                passed,
                elapsed,
                created_at,
                code,
                lang_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                attempt["problem_id"],
                int(attempt["passed"]),
                attempt["elapsed"],
                attempt["created_at"],
                attempt["code"],
                attempt["lang_id"],
            ),
        )


def get_attempts(problem_id: int) -> list[sqlite3.Row]:
    db = get_db()
    return db.execute(
        """
        SELECT * FROM attempts
        WHERE problem_id = ?
        """,
        (problem_id,),
    ).fetchall()


def get_all_attempts() -> list[sqlite3.Row]:
    db = get_db()
    return db.execute("SELECT * FROM attempts").fetchall()


def get_passed_problems() -> set[int]:
    db = get_db()
    rows = db.execute(
        "SELECT DISTINCT problem_id FROM attempts WHERE passed = 1"
    ).fetchall()
    return {row["problem_id"] for row in rows}


def add_draft(draft: Draft) -> None:
    db = get_db()
    with db:
        db.execute(
            """
            INSERT INTO drafts(
                problem_id,
                lang_id,
                code,
                elapsed,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(problem_id, lang_id)
            DO UPDATE SET
                code = excluded.code,
                elapsed = excluded.elapsed,
                updated_at = excluded.updated_at
            """,
            (
                draft["problem_id"],
                draft["lang_id"],
                draft["code"],
                draft["elapsed"],
                draft["updated_at"],
            ),
        )


def get_draft(problem_id: int, lang_id: int = 1) -> sqlite3.Row:
    db = get_db()
    return db.execute(
        """
        SELECT *
        FROM drafts
        WHERE problem_id = ? AND lang_id = ?
        """,
        (problem_id, lang_id),
    ).fetchone()


def delete_draft(problem_id: int, lang_id: int = 1) -> None:
    db = get_db()
    with db:
        db.execute(
            """
            DELETE FROM drafts
            WHERE problem_id = ? AND lang_id = ?
            """,
            (problem_id, lang_id),
        )
