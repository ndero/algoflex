PRAGMA foreign_keys = ON;

CREATE TABLE test_config (
    ordered INTEGER NOT NULL CHECK (ordered IN (0, 1))
);

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

CREATE TABLE expected_results (
    position   INTEGER PRIMARY KEY,
    id         INTEGER NOT NULL,
    name       TEXT NOT NULL,
    email      TEXT NOT NULL,
    age        INTEGER NOT NULL,
    status     TEXT NOT NULL,
    role       TEXT NOT NULL,
    created_at TEXT NOT NULL
);

INSERT INTO expected_results (position, id, name, email, age, status, role, created_at) VALUES
    (1,  1,  'Alice', 'alice@example.test', 29, 'active',  'admin',     '2023-01-10 09:00:00'),
    (2,  4,  'David', 'david@example.test', 22, 'active',  'moderator', '2023-04-13 09:00:00'),
    (3,  10, 'Jack',  'jack@example.test',  20, 'pending', 'moderator', '2023-10-19 09:00:00'),
    (4,  11, 'Kira',  'kira@example.test',  19, 'active',  'admin',     '2023-11-20 09:00:00'),
    (5,  14, 'Nina',  'nina@example.test',  35, 'active',  'moderator', '2024-02-23 09:00:00'),
    (6,  16, 'Pia',   'pia@example.test',   18, 'pending', 'admin',     '2024-04-25 09:00:00'),
    (7,  19, 'Sam',   'sam@example.test',   33, 'pending', 'moderator', '2024-07-28 09:00:00'),
    (8,  20, 'Tina',  'tina@example.test',  27, 'active',  'admin',     '2024-08-29 09:00:00');
