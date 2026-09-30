### Go Bananas
Momo loves to eat bananas. There are `n` piles of bananas, where the `i`-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Momo can decide his **bananas-per-hour eating speed** `k`. Each hour, he chooses some pile of bananas and eats `k` bananas from that pile.

If the pile has less than `k` bananas, he eats all of them instead and will **not** eat any more bananas during that hour.

Momo likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the **minimum integer** `k` such that he can eat all the bananas within `h` hours.

**Example 1**

* **Input:** `piles = [2, 4, 5]`, `h = 5`
* **Output:** `3`
* **How:**
    With k = 3:
    - Pile 2 takes ceil(2 / 3) = 1 hour
    - Pile 4 takes ceil(4 / 3) = 2 hours
    - Pile 5 takes ceil(5 / 3) = 2 hours
    Total = 1 + 2 + 2 = 5 hours.
    With k = 2, the total would be 6 hours, so 3 is the minimum.

**Example 2**

* **Input:** `piles = [1, 2, 3, 4, 5, 6]`, `h = 6`
* **Output:** `6`
* **How:** With 6 piles and 6 hours, Momo must finish one pile per hour. The largest pile has 6 bananas, so the minimum speed is 6.

**Constraints**

* `1 <= piles.length <= 10^4`
* `piles.length <= h <= 10^9`
* `1 <= piles[i] <= 10^9`
