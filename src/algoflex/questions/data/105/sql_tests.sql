PRAGMA foreign_keys = ON;

CREATE TABLE test_config (
    ordered INTEGER NOT NULL CHECK (ordered IN (0, 1))
);

-- This problem returns a single row, so ordering is not significant.
INSERT INTO test_config (ordered) VALUES (0);

CREATE TABLE users (
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    email      TEXT NOT NULL UNIQUE,
    age        INTEGER,
    status     TEXT NOT NULL,
    role       TEXT NOT NULL,
    created_at TEXT NOT NULL
);

INSERT INTO users (id, name, email, age, status, role, created_at) VALUES
    (1, 'Alice',   'alice@example.test',   29,   'active',   'admin',     '2023-01-10 09:00:00'),
    (2, 'Bob',     'bob@example.test',     34,   'pending',  'member',    '2023-02-11 09:00:00'),
    (3, 'Charlie', 'charlie@example.test', 42,   'inactive', 'member',    '2023-03-12 09:00:00'),
    (4, 'David',   'david@example.test',   22,   'active',   'moderator', '2023-04-13 09:00:00'),
    (5, 'Eve',     'eve@example.test',     31,   'banned',   'member',    '2023-05-14 09:00:00'),
    (6, 'Frank',   'frank@example.test',   17,   'pending',  'admin',     '2023-06-15 09:00:00'),
    (7, 'Grace',   'grace@example.test',   18,   'active',   'member',    '2023-07-16 09:00:00'),
    (8, 'Henry',   'henry@example.test',   NULL, 'inactive', 'moderator', '2023-08-17 09:00:00'),
    (9, 'Ivy',     'ivy@example.test',     25,   'active',   'member',    '2023-09-18 09:00:00');

-- customers: ids {1, 2, 3, 4, 5}
--   * ids 1 and 2 also appear in suppliers  -> both
--   * ids 3, 4, 5 do not appear in suppliers -> customers only
--   * id 3 is deliberately given a slightly different name to prove
--     the set operations match on id, not name.
CREATE TABLE customers (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO customers (id, name) VALUES
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Charlie C'),   -- name differs from users.name on purpose
    (4, 'David'),
    (5, 'Eve');

-- suppliers: ids {1, 2, 6, 7}
--   * ids 1 and 2 also appear in customers  -> both
--   * ids 6 and 7 are suppliers only
--   * id 1 given a slightly different name to prove id-based matching.
CREATE TABLE suppliers (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO suppliers (id, name) VALUES
    (1, 'Alice S'),     -- name differs from users.name on purpose
    (2, 'Bob'),
    (6, 'Frank'),
    (7, 'Grace');

-- Expected counts:
--   both_count            = |customers INTERSECT suppliers| = |{1, 2}| = 2
--   customers_only_count  = |customers EXCEPT suppliers|    = |{3, 4, 5}| = 3
--   either_count          = |customers UNION suppliers|     = |{1,2,3,4,5,6,7}| = 7
CREATE TABLE expected_results (
    position              INTEGER PRIMARY KEY,
    both_count            INTEGER NOT NULL,
    customers_only_count  INTEGER NOT NULL,
    either_count          INTEGER NOT NULL
);

INSERT INTO expected_results (position, both_count, customers_only_count, either_count) VALUES
    (1, 2, 3, 7);
