### Eligible Users

Given the SQL table **`users`**, write a SQLite query that returns all users who meet the following conditions:

- Are at least 18 years old.
- Have a status of either `'active'` or `'pending'`.
- Are not banned or deleted.
- Have a role of either `'admin'` or `'moderator'`.
- Have an email address that is not `NULL`.

Return the following columns:

- `id` — the user’s unique identifier (`users.id`)
- `name` — the user’s name (`users.name`)
- `email` — the user’s email address (`users.email`)
- `age` — the user’s age (`users.age`)
- `status` — the user’s account status (`users.status`)
- `role` — the user’s role (`users.role`)
- `created_at` — the date and time the user account was created (`users.created_at`)

### Tables

**`users`**

| Name | Type | Description |
|---|---|---|
| `id` | INTEGER | The user's unique identifier. Primary key. |
| `name` | TEXT | The user's name. |
| `email` | TEXT | The user's email address. |
| `age` | INTEGER | The user's age; may be `NULL`. |
| `status` | TEXT | The user's account status, such as `'active'`, `'pending'`, `'banned'`, or `'deleted'`. |
| `role` | TEXT | The user's role on the platform, such as `'admin'`, `'moderator'`, or `'member'`. |
| `created_at` | TEXT | The date and time the user account was created. |

### Rules

- Results may be returned in any row order.