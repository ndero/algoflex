### Reachable cities
Given `n` cities labelled 0 to n - 1 and an array `edges` where `edges[i] = [from, to, weight]` represents a weighted bidirectional edge between cities `from` and `to`.  Return city with the smallest number of cities that are reachable and whose distance is at most `k`.

If multiple such cities, return the one with the greatest number.

**Example**

* **Input:**
    n = 5,
    edges = [
        [0, 1, 1],
        [1, 2, 1],
        [2, 3, 1],
        [3, 4, 1],
    ],
    k = 1
* **Output:** `4`
* **How:** reachable counts: 0 -> 1, 1 -> 2, 2 -> 2, 4 -> 1

**Constraints**

* `1 <= n <= 9`
* `0 <= from, to < n`
* `0 <= edges.length <= 11`
* `0 <= k <= 100`