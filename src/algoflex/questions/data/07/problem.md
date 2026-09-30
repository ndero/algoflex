### Min length sub array
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to target.

If there is no such subarray, return `0`.

**Example 1**

* **Input:** `nums = [2, 3, 1, 2, 4, 3]`, `target = 7`
* **Output** `2`
* **How:** sub array [4, 3] has sum >= 7

**Example 2**

* **Input:** `nums = [1, 3, 6, 2, 1]`, `target = 4`
* **Output** `1`
* **How:** sub array [6] has sum >= 4

**Constraints**

* `1 <= nums.length <= 10^6`
* `0 <= nums[i] < 2^31 - 1`
* `0 <= target <= 6 * 10^7`