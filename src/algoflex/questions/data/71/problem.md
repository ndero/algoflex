### Count SCCs
Given a directed graph with `n` vertices labelled from 0 to n - 1 and a list of `edges` where each edge indicate a directed path `[u, v]`.  find the number of Strongly Connected Components (SCCs) in the graph.

> A Strongly Connected Component of a directed graph is a maximal set of vertices such that for every pair of vertices `u` and `v` in the component, there is a directed path from `u` to `v` and a directed path from `v` to `u`. In other words, every vertex in an SCC is reachable from every other vertex in that component.

### Example
```
Input: n = 5, edges = [[0,2], [0,3], [1,0], [2,1], [3,4]]
Output: 3
How:

                           ┌──────┐
                           ↓      │
      4 <─── 3 <─── 0 ───> 2 ───> 1
                    │             │
                    ↑             ↓
                    └─────────────┘

    the SCCs are {0, 1, 2}, {3} and {4}

Input: n = 4, edges = [[0,1], [1,2], [2,3]]
Output: 4
How: simple path, each vertex is its own SCC.
```
