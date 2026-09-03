### Containers at the Docks

**Description:**
You are a master thief planning a heist at a shipyard where a row of `n` shipping containers is waiting to be processed. Each container holds a specific value of goods.

The dock's security system is highly advanced: opening any two adjacent containers will immediately trigger an alarm.

Given an integer array `nums` where `nums[i]` represents the value of the goods inside the $i$-th container, return the maximum total value you can steal without triggering the security system.


**Example 1:**

* **Input:** `nums = [1, 2, 3, 1]`
* **Output:** `4`
* **Explanation:** You rob container 0 (value = 1) and then container 2 (value = 3). Total value stolen = 1 + 3 = 4.

**Example 2:**

* **Input:** `nums = [2, 7, 9, 3, 1]`
* **Output:** `12`
* **Explanation:** You rob container 0 (value = 2), container 2 (value = 9), and container 4 (value = 1). Total value stolen = 2 + 9 + 1 = 12.

**Constraints:**

* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 400`
