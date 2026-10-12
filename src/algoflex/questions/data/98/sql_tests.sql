PRAGMA foreign_keys = ON;

CREATE TABLE test_config (
    ordered INTEGER NOT NULL CHECK (ordered IN (0, 1))
);

INSERT INTO test_config (ordered) VALUES (1);

CREATE TABLE users (
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    email      TEXT NOT NULL UNIQUE,
    age        INTEGER,
    status     TEXT NOT NULL,
    role       TEXT NOT NULL,
    created_at TEXT NOT NULL
);

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

INSERT INTO users (id, name, email, age, status, role, created_at) VALUES
    (1, 'Alice Ngugi',   'alice@example.test', 29,   'active',   'member', '2023-01-10 09:00:00'),
    (2, 'Brian Otieno',  'brian@example.test', 34,   'active',   'member', '2023-02-11 09:00:00'),
    (3, 'Carol Wanjiku', 'carol@example.test', 42,   'active',   'member', '2023-03-12 09:00:00'),
    (4, 'David Kamau',   'david@example.test', 22,   'active',   'member', '2023-04-13 09:00:00'),
    (5, 'Esther Njeri',  'esther@example.test', 31,  'inactive', 'member', '2023-05-14 09:00:00'),
    (6, 'Felix Mwangi',  'felix@example.test', 17,   'active',   'member', '2023-06-15 09:00:00'),
    (7, 'Grace Achieng', 'grace@example.test', 18,   'active',   'member', '2023-07-16 09:00:00'),
    (8, 'Henry Kariuki', 'henry@example.test', NULL, 'active',   'member', '2023-08-17 09:00:00');

-- Create 35 eligible completed attempts. Their timestamps are spaced one hour apart
WITH RECURSIVE seq(n) AS (
    SELECT 0
    UNION ALL
    SELECT n + 1 FROM seq WHERE n < 34
)
INSERT INTO attempts (
    attempt_id, user_id, problem_id, status, elapsed, score, created_at, language_id
)
SELECT
    1001 + n,
    CASE (n % 5)
        WHEN 0 THEN 1
        WHEN 1 THEN 2
        WHEN 2 THEN 3
        WHEN 3 THEN 4
        ELSE 7
    END,
    200 + (n % 7),
    'completed',
    120 + n,
    100 - n,
    datetime('2025-01-01 00:00:00', printf('+%d hours', n)),
    1 + (n % 3)
FROM seq;

INSERT INTO attempts (
    attempt_id, user_id, problem_id, status, elapsed, score, created_at, language_id
) VALUES
    (2001, 5, 901, 'completed',   90,  99, '2025-02-05 11:00:00', 1),
    (2002, 6, 901, 'completed',   90,  65, '2025-02-05 11:00:00', 2),
    (2003, 6, 902, 'completed',   95,  98, '2025-02-05 11:00:00', 1),
    (2004, 1, 903, 'in_progress', 40,  97, '2025-02-05 10:00:00', 1),
    (2005, 2, 904, 'failed',      65,  96, '2025-02-05 09:00:00', 2),
    (2006, 8, 905, 'completed',   70,  95, '2025-02-05 08:00:00', 3);

-- add a case that will need an attempt_id tie breaker
INSERT INTO users (id, name, email, age, status, role, created_at) VALUES
    (9, 'Ivy Mwende', 'ivy@example.test', 25, 'active', 'member', '2023-09-18 09:00:00');

INSERT INTO attempts (
    attempt_id, user_id, problem_id, status, elapsed, score, created_at, language_id
) VALUES
    (1000, 9, 999, 'completed', 100, 100, '2025-01-01 05:00:00', 1);

-- create expected results table 
CREATE TABLE expected_results (
    position    INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    problem_id  INTEGER NOT NULL,
    score       INTEGER NOT NULL,
    attempt_time TEXT NOT NULL
);

INSERT INTO expected_results
    (position, name, problem_id, score, attempt_time)
VALUES
    (1,  'Grace Achieng', 200, 86, '2025-01-01 14:00:00'),
    (2,  'David Kamau',   206, 87, '2025-01-01 13:00:00'),
    (3,  'Carol Wanjiku', 205, 88, '2025-01-01 12:00:00'),
    (4,  'Brian Otieno',  204, 89, '2025-01-01 11:00:00'),
    (5,  'Alice Ngugi',   203, 90, '2025-01-01 10:00:00'),
    (6,  'Grace Achieng', 202, 91, '2025-01-01 09:00:00'),
    (7,  'David Kamau',   201, 92, '2025-01-01 08:00:00'),
    (8,  'Carol Wanjiku', 200, 93, '2025-01-01 07:00:00'),
    (9,  'Brian Otieno',  206, 94, '2025-01-01 06:00:00'),
    (10, 'Alice Ngugi',   205, 95, '2025-01-01 05:00:00');