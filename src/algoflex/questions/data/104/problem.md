### Latest Attempt with Overall Rank

Given the SQL tables **`users`** and **`attempts`**, write a SQLite query that returns every user with at least one attempt, along with details of their latest attempt and their overall rank among users based on the `elapsed` time of their latest attempt.

Return the following columns:

- `name` — the user’s name (`users.name`)
- `problem_id` — the problem ID of the user’s latest attempt (`attempts.problem_id`)
- `score` — the score of the user’s latest attempt (`attempts.score`)
- `rank` — the user’s overall rank among all qualifying users, ordered by the `elapsed` time of their latest attempt (smallest `elapsed` = rank 1)

The “latest attempt” for a user is the attempt with the greatest `created_at` for that user. When multiple attempts share the same `created_at`, use the greatest `attempt_id` as a tie-breaker.

Sort the results by `rank` ascending.

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
| `score` | INTEGER | The score earned for the attempt. Range: `[0, 100]`. |
| `created_at` | TEXT | The date and time the attempt was created. |
| `language_id` | INTEGER | The ID of the programming language used. |

### Rules

- Return only `name`, `problem_id`, `score`, and `rank`.
- Results must be sorted by `rank` ascending.