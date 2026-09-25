### Top K Frequent Elements
Given an integer array `nums` and an integer `k`, return the `k` most frequently occurring elements in the array.

Return the ans ordered by highest count and position in the array where there are ties. 

### Examples
```text
Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
How: 1 appears 3 times, 2 appears 2 times, and 3 appears 1 time.
The two most frequent elements are 1 and 2.
```

```text
Input: nums = [1, 2, 2, 3, 3, 3, 1], k = 2`
Output: [3, 1]
How: 3 appears three times, both 1 and 2 appear two times each but 1 is the element that appear first in the array 
```

```text
Input: nums = [2], k = 1
Output: [2]
```

### Constraints
```text
1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in nums]
-10^4 <= nums[i] <= 10^4
```
