### Jump to zero
Given an integer array `nums` where `nums[i]` represents the maximum forward or backward jump length from index `i` and a starting index `start`. Check if you can jump to an index where the value is 0.

**Example 1**

* **Input:** `nums = [4,2,3,0,3,1,2]`, `start = 5`
* **Output:** `true`
* **How:** index 5 -> 4 -> 1 -> 3 or 5 -> 6 -> 4 -> 1 -> 3

**Example 2**

* **Input:** `nums = [3,0,2,1,2]`, `start = 2`
* **Output:** `false`
* **How:** There is no way to get to index 1 starting from index 2.

**Constraints**

* `1 <= nums.length <= 2 * 10^5`
* `0 <= nums[i] < 10`

