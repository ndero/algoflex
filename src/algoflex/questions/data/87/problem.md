### Longest Consecutive Sequence
Given an unsorted array of integers `nums`, return the length of the **longest consecutive elements sequence**.

A consecutive sequence is a set of integers where each number is exactly `1` greater than the previous number. The elements do **not** need to appear consecutively in the original array; they only need to form a consecutive run when considered as a set.

Can you do it in linear time complexity?

### Examples
```text
Input: nums = [1, 3, 2, 5, 4, 0]
Output: 6
How: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5]. Therefore its length is 6.
```

```text
Input: nums = [0, 1]
Output: 2
How: The longest consecutive elements sequence is [0, 1]. Therefore its length is 2.
```

```text
Input: nums = []
Output: 0
```

### Constraints
```text
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
```
