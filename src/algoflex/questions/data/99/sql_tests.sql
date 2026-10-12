PRAGMA foreign_keys = ON;

CREATE TABLE test_config (
    ordered INTEGER NOT NULL CHECK (ordered IN (0, 1))
);

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
    (1,  'Alice Ngugi',   'alice@example.test',   29,   'active',   'admin',     '2023-01-10 09:00:00'),
    (2,  'Brian Otieno',  'brian@example.test',   34,   'active',   'admin',     '2023-02-11 09:00:00'),
    (3,  'Carol Wanjiku', 'carol@example.test',   42,   'banned',   'admin',     '2023-03-12 09:00:00'),
    (4,  'David Kamau',   'david@example.test',   22,   'active',   'member',    '2023-04-13 09:00:00'),
    (5,  'Esther Njeri',  'esther@example.test',  31,   'inactive', 'member',    '2023-05-14 09:00:00'),
    (6,  'Felix Mwangi',  'felix@example.test',   17,   'active',   'member',    '2023-06-15 09:00:00'),
    (7,  'Grace Achieng', 'grace@example.test',   18,   'active',   'moderator', '2023-07-16 09:00:00'),
    (8,  'Henry Kariuki', 'henry@example.test',   NULL, 'inactive', 'moderator', '2023-08-17 09:00:00'),
    (9,  'Ivy Mwende',    'ivy@example.test',     25,   'banned',   'member',    '2023-09-18 09:00:00'),
    (10, 'Jack Omondi',   'jack@example.test',    37,   'active',   'moderator', '2023-10-19 09:00:00'),
    (11, 'Kira Wambui',   'kira@example.test',    28,   'banned',   'admin',     '2023-11-20 09:00:00'),
    (12, 'Leo Mutua',     'leo@example.test',     33,   'inactive', 'member',    '2023-12-21 09:00:00');

-- Expected distinct (role, status) combinations.
CREATE TABLE expected_results (
    position INTEGER PRIMARY KEY,
    role     TEXT NOT NULL,
    status   TEXT NOT NULL
);

INSERT INTO expected_results (position, role, status) VALUES
    (1, 'admin',     'active'),
    (2, 'admin',     'banned'),
    (3, 'member',    'active'),
    (4, 'member',    'banned'),
    (5, 'member',    'inactive'),
    (6, 'moderator', 'active'),
    (7, 'moderator', 'inactive');
