### User Status Priority

Given the SQL table **`users`**, write a SQLite query that returns every user’s `name`, `status`, and a numeric `status_priority` based on their account status.

Return the following columns:

- `name` — the user’s name (`users.name`)
- `status` — the user’s account status (`users.status`)
- `status_priority` — a numeric priority derived from `status`: `active` = `1`, `pending` = `2`, everything else = `3`

Sort the results by `status_priority` ascending.

### Tables

**`users`**

| Name | Type | Description |
|---|---|---|
| `id` | INTEGER | The user's unique identifier. Primary key. |
| `name` | TEXT | The user's name. |
| `email` | TEXT | The user's email address. |
| `age` | INTEGER | The user's age; may be `NULL`. |
| `status` | TEXT | The user's account status, such as `'active'`, `'pending'`, or `'inactive'`. |
| `role` | TEXT | The user's role on the platform. |
| `created_at` | TEXT | The date and time the user account was created. |
