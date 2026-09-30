### Dutch National Flag
Given an array `colors` containing `n` integers where each integer is either `0`, `1`, or `2` representing the colors of the Dutch national flag:
```text
0 -> Red
1 -> White
2 -> Blue
```
Sort the array **in-place** so that all `0`s come first, then all `1`s, then all `2`s.

You must solve the problem **without using a built-in sort function** and ideally in **one pass**.

**Example 1**

* **Input:** `colors = [2, 0, 2, 1, 1, 0]`
* **Output:** `[0, 0, 1, 1, 2, 2]`

**Example 2**

* **Input:** `colors = [0]`
* **Output:** `[0]`

**Constraints**

* `n == colors.length`
* `1 <= n <= 300`
* `colors[i]` is either `0`, `1` or `2`.
