### Jump to zero
Given an integer array `nums` where `nums[i]` represents the maximum forward or backward jump length from index `i` and a starting index `start`. Check if you can jump to an index where the value is 0.

### Example
```
Input: nums = [4,2,3,0,3,1,2], start = 5
output = true
How: index 5 -> 4 -> 1 -> 3 or 5 -> 6 -> 4 -> 1 -> 3
```

```
Input: nums = [3,0,2,1,2], start = 2
output = false
How: There is no way to get to index 1 starting from index 2.
```
