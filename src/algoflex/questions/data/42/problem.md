### Maximum profit
Given an array `prices` where `prices[i]` is the price of a given stock on the ith day. Return the maximum profit that can be made by choosing a single day to buy and choosing a different day in the future to sell that stock.

If you cannot achieve any profit, return 0.

**Example 1**

* **Input:** `prices = [7, 1, 5, 3, 6, 4]`
* **Output:** `5`
* **How:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

**Example 2**

* **Input:** `prices = [7, 6, 4, 3, 1]`
* **Output:** `0`
* **How:** There is no way to make a profit.

**Constraints**

* `0 <= prices.length <= 10^5`
* `0 <= price[i] < 10^5`
