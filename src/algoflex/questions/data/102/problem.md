### Active Users with Attempt History

Given the SQL tables **`users`** and **`attempts`**, write a SQLite query that returns users who have made at least 10 attempts, of which at least 5 were successful. For each qualifying user, show their total attempts, successful attempts, and failed attempts.

Return the following columns:

- `id` — the user’s unique identifier (`users.id`)
- `name` — the user’s name (`users.name`)
- `total_attempts` — the total number of attempts made by the user
- `successful_attempts` — the number of attempts with `status = 'success'`
- `failed_attempts` — the number of attempts with `status = 'failed'`

Sort the results by `total_attempts` descending, then by `name` ascending.

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
| `status` | TEXT | The attempt's status, such as `'success'` or `'failed'`. |
| `elapsed` | INTEGER | The time taken to complete the attempt. |
| `created_at` | TEXT | The date and time the attempt was created. |
| `language_id` | INTEGER | The ID of the programming language used. |
