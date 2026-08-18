### Pairwise
Given an array `arr`, find element pairs whose sum equal the second argument `target` and return the sum of their indices.

Each element can only construct a single pair. Make sure to pick elements from left to right i.e pair the earliest available elements. 

### Example
```
arr = [7, 9, 11, 13, 15]
target = 20
output = 6
How: pairs 7 + 13 and 9 + 11, indices 0 + 3 and 1 + 2, total 6
```

```
arr = [0, 0, 0, 0, 1, 1]
target = 1
output = 10
How: pairs 0 + 1 and 0 + 1, indices 0 + 4 and 1 + 5, total 10
```
