PRAGMA foreign_keys = ON;

CREATE TABLE test_config (
    ordered INTEGER NOT NULL CHECK (ordered IN (0, 1))
);

-- This problem requires ordered results (total_attempts DESC, name ASC).
INSERT INTO test_config (ordered) VALUES (1);

CREATE TABLE users (
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    email      TEXT UNIQUE,
    age        INTEGER,
    status     TEXT NOT NULL,
    role       TEXT NOT NULL,
    created_at TEXT NOT NULL
);

INSERT INTO users (id, name, email, age, status, role, created_at) VALUES
    (1,  'Alice',   'alice@example.test',   29,   'active',   'admin',     '2023-01-10 09:00:00'),
    (2,  'Bob',     'bob@example.test',     34,   'pending',  'member',    '2023-02-11 09:00:00'),
    (3,  'Charlie', 'charlie@example.test', 42,   'inactive', 'admin',     '2023-03-12 09:00:00'),
    (4,  'David',   'david@example.test',   22,   'active',   'moderator', '2023-04-13 09:00:00'),
    (5,  'Eve',     'eve@example.test',     31,   'banned',   'admin',     '2023-05-14 09:00:00'),
    (6,  'Frank',   'frank@example.test',   17,   'pending',  'admin',     '2023-06-15 09:00:00'),
    (7,  'Grace',   'grace@example.test',   18,   'active',   'member',    '2023-07-16 09:00:00'),
    (8,  'Henry',   'henry@example.test',   NULL, 'inactive', 'moderator', '2023-08-17 09:00:00'),
    (9,  'Ivy',     NULL,                   25,   'active',   'admin',     '2023-09-18 09:00:00'),
    (10, 'Jack',    'jack@example.test',    20,   'pending',  'moderator', '2023-10-19 09:00:00'),
    (11, 'Kira',    'kira@example.test',    19,   'active',   'admin',     '2023-11-20 09:00:00'),
    (12, 'Leo',     'leo@example.test',     30,   'deleted',  'admin',     '2023-12-21 09:00:00'),
    (13, 'Mona',    NULL,                   28,   'pending',  'admin',     '2024-01-22 09:00:00'),
    (14, 'Nina',    'nina@example.test',    35,   'active',   'moderator', '2024-02-23 09:00:00'),
    (15, 'Omar',    'omar@example.test',    40,   'inactive', 'moderator', '2024-03-24 09:00:00'),
    (16, 'Pia',     'pia@example.test',     18,   'pending',  'admin',     '2024-04-25 09:00:00'),
    (17, 'Quinn',   'quinn@example.test',   22,   'active',   'member',    '2024-05-26 09:00:00'),
    (18, 'Rita',    'rita@example.test',    29,   'banned',   'moderator', '2024-06-27 09:00:00'),
    (19, 'Sam',     'sam@example.test',     33,   'pending',  'moderator', '2024-07-28 09:00:00'),
    (20, 'Tina',    'tina@example.test',    27,   'active',   'admin',     '2024-08-29 09:00:00');

CREATE TABLE attempts (
    attempt_id  INTEGER PRIMARY KEY,
    user_id     INTEGER NOT NULL REFERENCES users(id),
    problem_id  INTEGER NOT NULL,
    status      TEXT NOT NULL,
    elapsed     INTEGER NOT NULL,
    score       INTEGER NOT NULL CHECK (score BETWEEN 0 AND 100),
    created_at  TEXT NOT NULL,
    language_id INTEGER NOT NULL
);

-- Per-user attempt distributions.
-- Covered edge cases:
--   * exactly 10 attempts with exactly 5 successes  -> included (Bob, Ivy)
--   * exactly 10 attempts with 4 successes          -> excluded (David)
--   * 9 attempts with 5 successes                   -> excluded (Charlie)
--   * 8 attempts with 6 successes                   -> excluded (Frank)
--   * 0 attempts (no rows)                          -> excluded (Quinn)
--   * 20 attempts with 12 successes                 -> included (Grace)
--   * statuses other than success/failed present    -> only success/failed counted
WITH user_attempt_counts(user_id, total, successful, failed) AS (
    VALUES
        (1,  12, 6,  4),   -- Alice:   total 12, success 6,  failed 4, other 2 -> included
        (2,  10, 5,  5),   -- Bob:     total 10, success 5,  failed 5         -> included
        (3,  9,  5,  4),   -- Charlie: total 9,  success 5,  failed 4         -> excluded (total < 10)
        (4,  10, 4,  6),   -- David:   total 10, success 4,  failed 6         -> excluded (success < 5)
        (5,  15, 10, 3),   -- Eve:     total 15, success 10, failed 3, other 2 -> included
        (6,  8,  6,  2),   -- Frank:   total 8,  success 6,  failed 2         -> excluded (total < 10)
        (7,  20, 12, 8),   -- Grace:   total 20, success 12, failed 8         -> included
        (8,  10, 0,  10),  -- Henry:   total 10, success 0,  failed 10        -> excluded (success < 5)
        (9,  10, 5,  5),   -- Ivy:     total 10, success 5,  failed 5         -> included
        (11, 11, 6,  0),   -- Kira:    total 11, success 6,  failed 0, other 5 -> included
        (14, 12, 5,  0),   -- Nina:    total 12, success 5,  failed 0, other 7 -> included
        (20, 10, 5,  5)    -- Tina:    total 10, success 5,  failed 5         -> included
        -- Quinn (17) and others intentionally have no attempts.
),
seq(n) AS (
    SELECT 1 UNION ALL SELECT n + 1 FROM seq WHERE n < 25
)
INSERT INTO attempts (
    attempt_id, user_id, problem_id, status, elapsed, score, created_at, language_id
)
SELECT
    1000 + u.user_id * 100 + s.n AS attempt_id,
    u.user_id,
    200 + (s.n % 7) AS problem_id,
    CASE
        WHEN s.n <= u.successful THEN 'success'
        WHEN s.n <= u.successful + u.failed THEN 'failed'
        ELSE 'in_progress'
    END AS status,
    120 + s.n AS elapsed,
    50 + (s.n % 50) AS score,
    datetime('2025-01-01 00:00:00', printf('+%d minutes', s.n)) AS created_at,
    1 + (s.n % 3) AS language_id
FROM user_attempt_counts u
JOIN seq s ON s.n <= u.total;

-- Expected results:
--   total_attempts >= 10 AND successful_attempts >= 5
--   ordered by total_attempts DESC, then name ASC.
CREATE TABLE expected_results (
    position             INTEGER PRIMARY KEY,
    id                   INTEGER NOT NULL,
    name                 TEXT NOT NULL,
    total_attempts       INTEGER NOT NULL,
    successful_attempts  INTEGER NOT NULL,
    failed_attempts      INTEGER NOT NULL
);

INSERT INTO expected_results (position, id, name, total_attempts, successful_attempts, failed_attempts) VALUES
    (1, 7,  'Grace', 20, 12, 8),
    (2, 5,  'Eve',   15, 10, 3),
    (3, 1,  'Alice', 12, 6,  4),
    (4, 14, 'Nina',  12, 5,  0),
    (5, 11, 'Kira',  11, 6,  0),
    (6, 2,  'Bob',   10, 5,  5),
    (7, 9,  'Ivy',   10, 5,  5),
    (8, 20, 'Tina',  10, 5,  5);
