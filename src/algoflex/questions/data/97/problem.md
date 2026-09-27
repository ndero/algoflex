### First Missing Positive
Given an unsorted integer array `nums`, return the **smallest positive integer** that is **not present** in `nums`.

You must implement an algorithm that runs in **O(n)** time and uses **O(1)** auxiliary space.

### Examples
```text
Input: nums = [1, 2, 0]
Output: 3
Explanation:
The numbers 1 and 2 are present. The smallest missing positive integer is 3.
```

```text
Input: nums = [3, 4, -1, 1]
Output: 2
Explanation:
The numbers 1, 3, and 4 are present. The smallest missing positive integer is 2.
```

```text
Input: nums = [7, 8, 9, 11, 12]
Output: 1
Explanation:
The smallest positive integer 1 is missing.
```

```text
Input: nums = [1]
Output: 2
```

**Example 5**
```text
Input: nums = [1, 1]
Output: 2
Explanation:
The array contains duplicates, and 2 is missing.
```

### Constraints
```text
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
```
