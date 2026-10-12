### Distinct User Role and Account Status

Given the SQL table **`users`**, write a SQLite query that returns every distinct combination of user `role` and account `status`.

Return the following columns:

- `role` — the user’s role (`users.role`)
- `status` — the user’s account status (`users.status`)

Each unique `(role, status)` combination should appear only once.

### Tables

**`users`**

| Name | Type | Description |
|---|---|---|
| `id` | INTEGER | The user's unique identifier. Primary key. |
| `name` | TEXT | The user's name. |
| `email` | TEXT | The user's email address. |
| `age` | INTEGER | The user's age; may be `NULL`. |
| `status` | TEXT | The user's account status, such as `'active'`. |
| `role` | TEXT | The user's role on the platform. |
| `created_at` | TEXT | The date and time the user account was created. |

### Rules

- Return only the `role` and `status` columns, in any row order.
