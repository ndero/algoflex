### Split Array Largest Sum
Given an integer array `nums` and an integer `k`, split `nums` into `k` **non-empty contiguous subarrays** such that the **largest sum** among these subarrays is **minimized**.

Return the minimized largest sum.


### Examples
```text
Input: nums = [7, 2, 5, 10, 8], k = 2
Output: 18
How:
There are several ways to split nums into 2 subarrays.
- [7, 2, 5] and [10, 8] → sums are 14 and 18, largest = 18.
- [7, 2, 5, 10] and [8] → sums are 24 and 8, largest = 24.
- [7, 2] and [5, 10, 8] → sums are 9 and 23, largest = 23.
The minimized largest sum is 18.
```

```text
Input: nums = [1, 2, 3, 4, 5], k = 2
Output: 9
How:
The best split is [1, 2, 3] and [4, 5].
Their sums are 6 and 9, so the largest sum is 9.
```

```text
Input: nums = [1, 4, 4], k = 3
Output: 4
How:
The only valid split into 3 non-empty subarrays is [1], [4], [4].
The largest sum is 4.
```

```text
Input: nums = [1, 2, 3, 4, 5], k = 1
Output: 15
How:
With only 1 subarray, the largest sum is the sum of the entire array.
```

### Constraints
```text
1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= k <= min(50, nums.length)
```
