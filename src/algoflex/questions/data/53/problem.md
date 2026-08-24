### Critical connections
Given `n` servers labelled 0 to n - 1 connected by undirected `connections` where connections[i] = [a, b] indicates a connection between servers a and b. Return all the critical connections in the network in any order.

> A critical connection is one that, if removed, will make some servers not be able to reach the rest of the server network.

### Examples
```
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
output = [[1,3]]
```

```
Input: n = 2, connections = [[0,1]]
output = [[0,1]]
```
