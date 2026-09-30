### Sqrt(x)
Given a **non-negative integer** `x`, return the **integer square root** of `x`, rounded **down** to the nearest integer.

The integer square root of `x` is the largest integer `r` such that:

```text
r * r <= x
```

You must **not** use any built-in exponent function or operator, such as `pow(x, 0.5)` or `x ** 0.5`. You also must not use any built-in `sqrt` function.

**Example 1**

* **Input:** `x = 9`
* **Output:** `3`
* **How:** The square root of 9 is 3, so we return 3.

**Example 2**

* **Input:** `x = 123`
* **Output:** `11`
* **How:** The square root of 123 is 11.0905365..., and since we round it down to the nearest integer, 11 is returned.

**Constraints**

* `0 <= x <= 2^31 - 1`
