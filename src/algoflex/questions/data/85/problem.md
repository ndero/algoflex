### Median of Two Sorted Arrays
Given two sorted arrays `nums1` and `nums2` of sizes `m` and `n` respectively, return the **median** of the combined sorted array.

The overall run time complexity should be `O(log(m + n))`.

### Definition of Median
For a sorted array:
- If the total number of elements is **odd**, the median is the middle element.
- If the total number of elements is **even**, the median is the average of the two middle elements.


### Examples
```text
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.00000
How: The merged array is [1, 2, 3], and the median is 2.
```

```text
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.50000
How: The merged array is [1, 2, 3, 4], and the median is (2 + 3) / 2 = 2.5.
```

```text
Input: nums1 = [], nums2 = [1]
Output: 1.00000
How: The merged array is [1], and the median is 1.
```

### Constraints
```text
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
```
