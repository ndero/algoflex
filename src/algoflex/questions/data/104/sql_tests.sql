PRAGMA foreign_keys = ON;

CREATE TABLE test_config (
    ordered INTEGER NOT NULL CHECK (ordered IN (0, 1))
);

-- This problem requires ordered results (rank ASC, name ASC).
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
    (11, 'Aaron',   'aaron@example.test',   30,   'active',   'admin',     '2023-11-11 09:00:00');

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

-- Attempt distribution designed to exercise edge cases:
--   * Bob (2), David (4), Grace (7), Jack (10): no attempts -> excluded
--   * Alice (1):   2 attempts; latest chosen by created_at
--   * Charlie (3): 2 attempts; latest has larger elapsed
--   * Eve (5):     single attempt
--   * Frank (6):   2 attempts sharing created_at -> attempt_id tie-breaker decides latest
--   * Henry (8):   single attempt, NULL age
--   * Ivy (9):     2 attempts, NULL email
--   * Aaron (11):  single attempt, elapsed 120 (ties with Alice and Henry)
--   * Elapsed ties: Frank (100) rank 1; Alice/Henry/Aaron (120) rank 2; Eve (150) rank 5;
--     Ivy (180) rank 6; Charlie (400) rank 7.
--   * Omitting the name tie-breaker in ORDER BY would leave Alice/Henry/Aaron in an
--     unspecified order, which this testcase detects.
INSERT INTO attempts (
    attempt_id, user_id, problem_id, status, elapsed, score, created_at, language_id
) VALUES
    -- Alice: 2 attempts; latest is attempt 102 (2025-01-02, elapsed 120)
    (101, 1, 200, 'completed',   300, 50, '2025-01-01 00:00:00', 1),
    (102, 1, 201, 'completed',   120, 80, '2025-01-02 00:00:00', 1),

    -- Charlie: 2 attempts; latest is attempt 104 (2025-01-03, elapsed 400)
    (103, 3, 202, 'completed',   200, 60, '2025-01-01 01:00:00', 2),
    (104, 3, 203, 'failed',      400, 70, '2025-01-03 00:00:00', 2),

    -- Eve: single attempt (elapsed 150)
    (105, 5, 204, 'in_progress', 150, 90, '2025-01-05 00:00:00', 1),

    -- Frank: 2 attempts sharing the same created_at.
    -- Latest is attempt 107 (higher attempt_id) with elapsed 100.
    (106, 6, 205, 'failed',      250, 40, '2025-01-06 00:00:00', 3),
    (107, 6, 206, 'failed',      100, 55, '2025-01-06 00:00:00', 3),

    -- Henry: single attempt (elapsed 120), NULL age
    (108, 8, 207, 'completed',   120, 65, '2025-01-07 00:00:00', 1),

    -- Ivy: 2 attempts; latest is attempt 109 (2025-01-08, elapsed 180), NULL email
    (110, 9, 209, 'completed',    90, 30, '2025-01-01 00:00:00', 2),
    (109, 9, 208, 'completed',   180, 75, '2025-01-08 00:00:00', 2),

    -- Aaron: single attempt (elapsed 120, ties with Alice and Henry)
    (114, 11, 212, 'completed',  120, 70, '2025-01-09 00:00:00', 1);

-- Expected results:
--   For each user with >= 1 attempt, take their latest attempt
--   (created_at DESC, attempt_id DESC), then rank by elapsed ASC.
--
--   Latest attempts (name, problem_id, score, elapsed):
--     Frank   (206, 55, 100)  -> rank 1
--     Aaron   (212, 70, 120)  -> rank 2  (tie)
--     Alice   (201, 80, 120)  -> rank 2  (tie)
--     Henry   (207, 65, 120)  -> rank 2  (tie)
--     Eve     (204, 90, 150)  -> rank 5  (gap after three-way tie)
--     Ivy     (208, 75, 180)  -> rank 6
--     Charlie (203, 70, 400)  -> rank 7
--
--   Ordered by rank ASC, then name ASC for determinism within ties.
CREATE TABLE expected_results (
    position   INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    problem_id INTEGER NOT NULL,
    score      INTEGER NOT NULL,
    rank       INTEGER NOT NULL
);

INSERT INTO expected_results (position, name, problem_id, score, rank) VALUES
    (1, 'Frank',   206, 55, 1),
    (2, 'Aaron',   212, 70, 2),
    (3, 'Alice',   201, 80, 2),
    (4, 'Henry',   207, 65, 2),
    (5, 'Eve',     204, 90, 5),
    (6, 'Ivy',     208, 75, 6),
    (7, 'Charlie', 203, 70, 7);

