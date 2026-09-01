import sqlite3
from pathlib import Path

from platformdirs import user_data_dir

from algoflex.types import Attempt, Draft, Language
from algoflex.utils import midnight

APP_NAME = "algoflex"
_CONNECTION: sqlite3.Connection | None = None


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

        CREATE INDEX IF NOT EXISTS idx_attempts_problem_created
        ON attempts(problem_id, created_at DESC);

        CREATE INDEX IF NOT EXISTS idx_attempts_passed_elapsed
        ON attempts(passed, elapsed);

        CREATE INDEX IF NOT EXISTS idx_attempts_passed_problem_elapsed
        ON attempts(passed, problem_id, elapsed);

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


def get_problem_pass_ratio(problem_id: int) -> tuple[int, int]:
    db = get_db()
    row = db.execute(
        """
        SELECT 
            COUNT(*) FILTER (WHERE passed = 1) AS passed_count,
            COUNT(*) AS total_count 
        FROM attempts 
        WHERE problem_id = ?
        """,
        (problem_id,),
    ).fetchone()

    return row["passed_count"], row["total_count"]


def get_recent_attempts(n: int = 1, problem_id: int | None = None) -> list[sqlite3.Row]:
    db = get_db()

    if problem_id is None:
        return db.execute(
            """
            SELECT * 
            FROM attempts
            ORDER BY created_at DESC, attempt_id DESC
            LIMIT ?
            """,
            (n,),
        ).fetchall()

    return db.execute(
        """
        SELECT * 
        FROM attempts 
        WHERE problem_id = ? 
        ORDER BY created_at DESC, attempt_id DESC
        LIMIT ?
        """,
        (problem_id, n),
    ).fetchall()


def get_best_attempts(n: int = 1, problem_id: int | None = None) -> list[sqlite3.Row]:
    db = get_db()

    if problem_id is not None:
        return db.execute(
            """
            SELECT * 
            FROM attempts
            WHERE problem_id = ? AND passed = 1
            ORDER BY elapsed ASC, attempt_id DESC
            LIMIT ?
            """,
            (problem_id, n),
        ).fetchall()

    return db.execute(
        """
        WITH best_per_problem AS (
            SELECT 
                *,
                ROW_NUMBER() OVER (
                    PARTITION BY problem_id
                    ORDER BY elapsed ASC, attempt_id DESC
                ) as rn
                FROM attempts
                WHERE passed = 1 
        )
        SELECT * 
        FROM best_per_problem
        WHERE rn = 1
        ORDER BY elapsed ASC, attempt_id DESC
        LIMIT ?
        """,
        (n,),
    ).fetchall()


def get_attempts_today() -> tuple[int, int]:
    db = get_db()

    row = db.execute(
        """
        SELECT
            COUNT(DISTINCT CASE WHEN passed THEN problem_id END) AS today_passed,
            COUNT(*) AS today_total
        FROM attempts
        WHERE created_at >= ?
        """,
        (midnight(),),
    ).fetchone()

    return row["today_passed"], row["today_total"]


def get_passed_problem_ids() -> set[int]:
    db = get_db()

    rows = db.execute(
        """
        SELECT DISTINCT problem_id 
        FROM attempts
        WHERE passed = 1
        """
    ).fetchall()

    return {row["problem_id"] for row in rows}


def get_most_attempted_problems(n: int = 1) -> list[sqlite3.Row]:
    db = get_db()

    return db.execute(
        """
        SELECT 
            problem_id,
            COUNT(*) AS total_count,
            COUNT(*) FILTER (WHERE passed = 1) AS passed_count
            FROM attempts 
            GROUP BY problem_id 
            ORDER BY total_count DESC, passed_count DESC
            LIMIT ?
        """,
        (n,),
    ).fetchall()


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


def get_draft(problem_id: int, lang_id: Language = Language.PYTHON) -> sqlite3.Row:
    db = get_db()
    return db.execute(
        """
        SELECT *
        FROM drafts
        WHERE problem_id = ? AND lang_id = ?
        """,
        (problem_id, lang_id),
    ).fetchone()


def delete_draft(problem_id: int, lang_id: Language = Language.PYTHON) -> None:
    db = get_db()
    with db:
        db.execute(
            """
            DELETE FROM drafts
            WHERE problem_id = ? AND lang_id = ?
            """,
            (problem_id, lang_id),
        )
