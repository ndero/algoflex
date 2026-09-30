### Median of Two Sorted Arrays
Given two sorted arrays `nums1` and `nums2` of sizes `m` and `n` respectively, return the **median** of the combined sorted array.

The overall run time complexity should be `O(log(m + n))`.

> For a sorted array, if the total number of elements is odd, the median is the middle element. If the total number of elements is even, the median is the average of the two middle elements. 

**Example 1**

* **Input:** `nums1 = [1, 3]`, `nums2 = [2]`
* **Output:** `2.0000`
* **How:** The merged array is [1, 2, 3], and the median is 2.

**Example 2**

* **Input:** `nums1 = [1, 2]`, `nums2 = [3, 4]`
* **Output: `2.5000`
* **How:** The merged array is [1, 2, 3, 4], and the median is (2 + 3) / 2 = 2.5.

**Example 3**

* **Input:** `nums1 = []`, `nums2 = [1]`
* **Output:** `1.0000`
* **How:** The merged array is [1], and the median is 1.

**Constraints**

* `0 <= m, n <= 1000`
* `1 <= m + n <= 2000`
* `-10^6 <= nums1[i], nums2[i] <= 10^6`
