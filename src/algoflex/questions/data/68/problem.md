### Rotting oranges
Given an `m * n` grid where each cell can have a value of `0`, `1` or `2`:
- 0 - empty cell
- 1 - fresh orange
- 2 - rotten orange

Any fresh orange that is next (up, down, left, right) to a rotten one rots within a minute.

Return the minimum time within which all the oranges in the grid become rotten. Return -1 if it's impossible for all to get rotten.

### Example
```
Input: grid = [[1]]
Output: -1
```

```
Input: grid = [[1, 2]]
Output: 1
```

```
Input:
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

Output: 4

How:
Minute 0:    Minute 1:    Minute 2:    Minute 3:    Minute 4:
2 1 1        2 2 1        2 2 2        2 2 2        2 2 2
1 1 0   ->   2 1 0   ->   2 2 0   ->   2 2 0   ->   2 2 0
0 1 1        0 1 1        0 1 1        0 2 1        0 2 2
```
