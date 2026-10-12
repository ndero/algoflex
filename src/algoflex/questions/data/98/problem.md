### Recent Completed Attempts
Given the SQL tables **`users`** and **`attempts`**, write a SQLite query that returns the **21st - 30th most recent completed attempts** sorted from most recent to least recent. 

Return the following columns:

- `name` — the user’s name (`users.name`)
- `problem_id` — the attempted problem ID (`attempts.problem_id`)
- `score` — the score earned (`attempts.score`)
- `attempt_time` — the date and time the attempt was created (`attempts.created_at`)

Order the results from newest to oldest by `attempt_time`. When multiple attempts share the same `created_at` timestamp, use `attempts.attempt_id` as a tie-breaker.


### Tables 

**`users`**

| Name | Type | Description |
|---|---|---|
| `id` | INTEGER | The user's unique identifier. primary key|
| `name` | TEXT | The user's name. |
| `email` | TEXT | The user's email address. |
| `age` | INTEGER | The user's age; may be `NULL`. |
| `status` | TEXT | The user's account status, such as `'active'`. |
| `role` | TEXT | The user's role on the platform. |
| `created_at` | TEXT | The date and time the user account was created. |

**`attempts`**

| Name | Type | Description |
|---|---|---|
| `attempt_id` | INTEGER | The attempt's unique identifier. primary key|
| `user_id` | INTEGER | The ID of the user who made the attempt. References `users.id`|
| `problem_id` | INTEGER | The ID of the problem attempted. |
| `status` | TEXT | The attempt's status, such as `'completed'`. |
| `elapsed` | INTEGER | The time taken to complete the attempt. |
| `score` | INTEGER | The score earned for the attempt. [0, 100] |
| `created_at` | TEXT | The date and time the attempt was created. |
| `language_id` | INTEGER | The ID of the programming language used. |

### Rules

- A user qualifies only when `users.status = 'active'` and `users.age >= 18`. Users with `NULL` age do not qualify. 
- A completed attempt is one where `attempts.status = 'completed'`.