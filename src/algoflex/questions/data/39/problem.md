### Minimum connection cost
You are given `n` cities numbered from 1 to n and an array `connections` where connections[i] = [x, y, cost] indicates a weighted bidirectional connection between cities x and y.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities.

> The cost is the sum of the connections’ costs used.

Return -1 if it isn't possible to connect all n cities.

### Example
```
n = 3
connections = [
        [1, 2, 10],
        [1, 2, 1],
        [2, 3, 2],
]
output = 3
```
