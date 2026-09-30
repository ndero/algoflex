### Max water held
Given an array `nums` where each number represents the height of a vertical wall, find two walls that hold the most water between them and return the units of water contained.

> To calculate Units of water held, multiply the `width(base)` by `height`

**Example 1**

* **Input:** `nums = [3, 1, 2, 7]`
* **Output:** `9`
* **How:** 9 units of water held between the first and last wall. 

**Example 2**

* **Input:** `nums = [1, 1]`
* **Output:** `1`

**Constraints**

* `0 <= nums.length <= 10^5`
* `0 < nums[i] <= 10^3`
