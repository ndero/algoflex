### Critical connections
Given `n` servers labelled 0 to n - 1 connected by undirected `connections` where connections[i] = [a, b] indicates a connection between servers a and b. Return all the critical connections in the network in any order.

> A critical connection is one that, if removed, will make some servers not be able to reach the rest of the server network.

**Example 1**

* **Input:** `n = 4`, `connections = [[0,1],[1,2],[2,0],[1,3]]`
* **Output:** `[[1,3]]`

**Example 2**

* **Input:** `n = 2`, `connections = [[0,1]]`
* **Output:** `[[0,1]]`

**Constraints**

* `1 <= n <= 11`
* `0 <= connections.length < 30`
* `connections[i].length == 2`
* `1 <= a, b <= n`