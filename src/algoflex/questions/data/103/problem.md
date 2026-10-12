### Users with At Least One Attempt

Given the SQL tables **`users`** and **`attempts`**, write a SQLite query that returns all users who have made at least one attempt.

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
| `status` | TEXT | The user's account status, such as `'active'`. |
| `role` | TEXT | The user's role on the platform. |
| `created_at` | TEXT | The date and time the user account was created. |

**`attempts`**

| Name | Type | Description |
|---|---|---|
| `attempt_id` | INTEGER | The attempt's unique identifier. Primary key. |
| `user_id` | INTEGER | The ID of the user who made the attempt. References `users.id`. |
| `problem_id` | INTEGER | The ID of the problem attempted. |
| `status` | TEXT | The attempt's status, such as `'completed'`. |
| `elapsed` | INTEGER | The time taken to complete the attempt. |
| `created_at` | TEXT | The date and time the attempt was created. |
| `language_id` | INTEGER | The ID of the programming language used. |

### Rules

- Results may be returned in any row order.