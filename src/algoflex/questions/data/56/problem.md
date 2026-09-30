### How many islands
Given an `m x n grid` where each value is either 1 or 0 with 1 indicating land and 0 indicating water, return the number of islands in the grid. 

All four edges of the grid are surrounded by water.

> An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

**Example**

* **Input:**
```
grid = [
    ['1', '1', '1', '1'],
    ['0', '0', '0', '0'],
    ['1', '1', '1', '1'],
]
```
* **Output:** = `2`  
* **How:** 2 horizontal islands.

**Constraints**

* `1 <= m <= 5 * 10^4`
* `0 <= n <= 3 * 10^3`
