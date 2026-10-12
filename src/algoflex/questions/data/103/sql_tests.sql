PRAGMA foreign_keys = ON;

CREATE TABLE test_config (
    ordered INTEGER NOT NULL CHECK (ordered IN (0, 1))
);

-- This problem does not require ordered results.
INSERT INTO test_config (ordered) VALUES (0);

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
    (10, 'Jack',    'jack@example.test',    20,   'pending',  'moderator', '2023-10-19 09:00:00');

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
--   * Alice (1):    exactly 1 attempt                       -> included (boundary)
--   * Bob (2):      0 attempts                              -> excluded
--   * Charlie (3):  3 attempts, mixed statuses              -> included
--   * David (4):    0 attempts                              -> excluded
--   * Eve (5):      1 attempt with status 'in_progress'     -> included (no status filter)
--   * Frank (6):    5 attempts, statuses 'failed' only      -> included (no status filter)
--   * Grace (7):    0 attempts                              -> excluded
--   * Henry (8):    2 attempts with statuses 'completed'    -> included
--   * Ivy (9):      1 attempt, email is NULL                -> included (no email filter)
--   * Jack (10):    0 attempts                              -> excluded
INSERT INTO attempts (
    attempt_id, user_id, problem_id, status, elapsed, score, created_at, language_id
) VALUES
    -- Alice: 1 attempt
    (101, 1, 200, 'completed',   120, 80, '2025-01-01 00:00:00', 1),

    -- Charlie: 3 attempts, mixed statuses
    (102, 3, 200, 'completed',   130, 70, '2025-01-01 01:00:00', 1),
    (103, 3, 201, 'failed',      140, 40, '2025-01-01 02:00:00', 2),
    (104, 3, 202, 'in_progress', 150, 20, '2025-01-01 03:00:00', 3),

    -- Eve: 1 attempt, in_progress
    (105, 5, 203, 'in_progress', 160, 10, '2025-01-01 04:00:00', 1),

    -- Frank: 5 attempts, all failed
    (106, 6, 204, 'failed', 100, 30, '2025-01-01 05:00:00', 1),
    (107, 6, 205, 'failed', 100, 31, '2025-01-01 06:00:00', 2),
    (108, 6, 206, 'failed', 100, 32, '2025-01-01 07:00:00', 3),
    (109, 6, 207, 'failed', 100, 33, '2025-01-01 08:00:00', 1),
    (110, 6, 208, 'failed', 100, 34, '2025-01-01 09:00:00', 2),

    -- Henry: 2 attempts, completed
    (111, 8, 209, 'completed', 200, 60, '2025-01-01 10:00:00', 1),
    (112, 8, 210, 'completed', 210, 61, '2025-01-01 11:00:00', 2),

    -- Ivy: 1 attempt
    (113, 9, 211, 'completed', 220, 90, '2025-01-01 12:00:00', 1);

-- Expected results: users with at least one attempt.
-- Users 2 (Bob), 4 (David), 7 (Grace), and 10 (Jack) have no attempts and are excluded.
-- Row order is unspecified; position is used only to enumerate expected rows.
CREATE TABLE expected_results (
    position   INTEGER PRIMARY KEY,
    id         INTEGER NOT NULL,
    name       TEXT NOT NULL,
    email      TEXT,
    age        INTEGER,
    status     TEXT NOT NULL,
    role       TEXT NOT NULL,
    created_at TEXT NOT NULL
);

INSERT INTO expected_results (position, id, name, email, age, status, role, created_at) VALUES
    (1, 1, 'Alice',   'alice@example.test',   29,   'active',   'admin',     '2023-01-10 09:00:00'),
    (2, 3, 'Charlie', 'charlie@example.test', 42,   'inactive', 'admin',     '2023-03-12 09:00:00'),
    (3, 5, 'Eve',     'eve@example.test',     31,   'banned',   'admin',     '2023-05-14 09:00:00'),
    (4, 6, 'Frank',   'frank@example.test',   17,   'pending',  'admin',     '2023-06-15 09:00:00'),
    (5, 8, 'Henry',   'henry@example.test',   NULL, 'inactive', 'moderator', '2023-08-17 09:00:00'),
    (6, 9, 'Ivy',     NULL,                   25,   'active',   'admin',     '2023-09-18 09:00:00');
