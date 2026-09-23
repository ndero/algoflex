### Remove Duplicates from Sorted Array
Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same.

Return the number of unique elements in `nums`, denoted as `k`.

After modifying the array in-place, the first `k` elements of `nums` should contain the unique elements in the order they appeared originally. The remaining elements beyond index `k - 1` do not matter.

### Examples
```text
Input: nums = [1, 2, 2]
Output: 2, nums = [1, 2, _]
How: The first two elements of nums are 1 and 2, which are the unique elements.
The underscore represents elements that do not matter.
```

```text
Input: nums = [0, 0, 1, 1, 2, 2]
Output: 5, nums = [0, 1, 2, _, _, _]
How: The first three elements of nums are 0, 1 and 2, which are the unique elements.
```

### Constraints
```text
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
```