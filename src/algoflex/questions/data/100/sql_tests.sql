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

INSERT INTO users (id, name, email, age, status, role, created_at) VALUES
    (1, 'Alice',   'alice@example.test',   29, 'active',   'admin',     '2023-01-10 09:00:00'),
    (2, 'Bob',     'bob@example.test',     34, 'pending',  'member',    '2023-02-11 09:00:00'),
    (3, 'Charlie', 'charlie@example.test', 42, 'inactive', 'member',    '2023-03-12 09:00:00'),
    (4, 'David',   'david@example.test',   22, 'active',   'moderator', '2023-04-13 09:00:00'),
    (5, 'Eve',     'eve@example.test',     31, 'banned',   'member',    '2023-05-14 09:00:00'),
    (6, 'Frank',   'frank@example.test',   17, 'pending',  'admin',     '2023-06-15 09:00:00'),
    (7, 'Grace',   'grace@example.test',   18, 'active',   'member',    '2023-07-16 09:00:00'),
    (8, 'Henry',   'henry@example.test',   NULL, 'inactive', 'moderator', '2023-08-17 09:00:00');

CREATE TABLE expected_results (
    position        INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    status          TEXT NOT NULL,
    status_priority INTEGER NOT NULL
);

INSERT INTO expected_results (position, name, status, status_priority) VALUES
    (1, 'Alice',   'active',   1),
    (2, 'David',   'active',   1),
    (3, 'Grace',   'active',   1),
    (4, 'Bob',     'pending',  2),
    (5, 'Frank',   'pending',  2),
    (6, 'Charlie', 'inactive', 3),
    (7, 'Eve',     'banned',   3),
    (8, 'Henry',   'inactive', 3);
