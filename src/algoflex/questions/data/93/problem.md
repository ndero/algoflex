### Sqrt(x)
Given a **non-negative integer** `x`, return the **integer square root** of `x`, rounded **down** to the nearest integer.

The integer square root of `x` is the largest integer `r` such that:

```text
r * r <= x
```

You must **not** use any built-in exponent function or operator, such as `pow(x, 0.5)` or `x ** 0.5`. You also must not use any built-in `sqrt` function.

### Examples
```text
Input: x = 9
Output: 3
How: The square root of 9 is 3, so we return 3.
```

```text
Input: x = 123
Output: 11
How: The square root of 123 is 11.0905365..., and since we round it down to the nearest integer, 11 is returned.
```

```text
Input: x = 0
Output: 0
```

### Constraints
```text
0 <= x <= 2^31 - 1
```
