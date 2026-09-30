### Fewest coins to make change
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing the total amount of money, return the minimum number of coins that you need to make up that amount.

Return `-1` if `amount` cannot be made by any combination of the coins.

You may assume that you have an infinite number of each kind of coin.

**Example**

* **Input:** `coins = [1,2,5]`, `amount = 11`
* **Output:** `3`
* **How:** 11 = 5 + 5 + 1

**Constraints**

* `0 <= coins.length <= 6`
* `1 <= coins[i] <= 50`
* `0 <= amount <= 100`