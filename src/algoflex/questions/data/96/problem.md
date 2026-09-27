### Sort Colors
Given an array `colors` containing `n` integers where each integer is either `0`, `1`, or `2`, sort the array **in-place** so that all `0`s come first, then all `1`s, then all `2`s.

This problem is also known as the **Dutch National Flag** problem, where the colors are represented as:

```text
0 -> Red
1 -> White
2 -> Blue
```

You must solve the problem **without using a built-in sort function** and ideally in **one pass**.

### Examples
```text
Input: colors = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
```

```text
Input: colors = [0]
Output: [0]
```

### Constraints
```text
n == colors.length
1 <= n <= 300
colors[i] is either 0, 1, or 2.
```
