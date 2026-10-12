### Customer and Supplier Overlap

Given the SQL tables **`users`**, **`customers`**, and **`suppliers`**, write a SQLite query that returns three counts:

- The total number of users who are **both** a customer and a supplier.
- The total number of users who are **strictly** customers and **not** suppliers.
- The total number of users who are **either** a customer or a supplier (or both).

Return the following columns:

- `both_count` — the number of users present in both `customers` and `suppliers`
- `customers_only_count` — the number of users present in `customers` but not in `suppliers`
- `either_count` — the number of users present in `customers` or `suppliers` (union)

The result must be a single row containing all three counts.

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

**`customers`**

| Name | Type | Description |
|---|---|---|
| `id` | INTEGER | The customer's user ID. References `users.id`. |
| `name` | TEXT | The customer's name. |

**`suppliers`**

| Name | Type | Description |
|---|---|---|
| `id` | INTEGER | The supplier's user ID. References `users.id`. |
| `name` | TEXT | The supplier's name. |

### Rules

- Return the three counts as a single row with columns `both_count`, `customers_only_count`, and `either_count`.
