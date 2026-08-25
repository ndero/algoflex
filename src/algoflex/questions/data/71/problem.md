### Count SCCs
Given a directed graph with `V` vertices and `E` edges, find the number of Strongly Connected Components (SCCs) in the graph.

> A Strongly Connected Component of a directed graph is a maximal set of vertices such that for every pair of vertices `u` and `v` in the component, there is a directed path from `u` to `v` and a directed path from `v` to `u`. In other words, every vertex in an SCC is reachable from every other vertex in that component.

### Example
```
Input: V = 5, edges = [[1,3], [1,4], [2,1], [3,2], [4,5]]
Output: 3
How:
    1 -> 3 -> 2
    ↑    ↓
    └────┘
    ↓
    4 -> 5

    the SCCs are {1, 2, 3}, {4} and {5}

Input: V = 4, edges = [[1,2], [2,3], [3,4]]
Output: 4
How: simple path, each vertex is its own SCC.
```
