### Concatenation of Array

Given an integer array `nums` of length `n`, create an array `ans` of length `2n` where:

- `ans[i] = nums[i]` for `0 <= i < n`
- `ans[i + n] = nums[i]` for `0 <= i < n`

In other words, `ans` is formed by concatenating `nums` with itself.

Return the array `ans`.

Can you solve this problem in `O(n)` time and `O(n)` extra space?

### Examples
```text
Input: nums = [1, 2, 1]
Output: [1, 2, 1, 1, 2, 1]
How: The array [1, 2, 1] is concatenated with itself to form [1, 2, 1, 1, 2, 1].
```

```text
Input: nums = [1, 3, 2, 1]
Output: [1, 3, 2, 1, 1, 3, 2, 1]
How: The array [1, 3, 2, 1] is concatenated with itself to form [1, 3, 2, 1, 1, 3, 2, 1].
```

### Constraints
```text
1 <= nums.length <= 1000
1 <= nums[i] <= 1000
```
