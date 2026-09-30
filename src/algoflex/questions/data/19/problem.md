### Paths with sum
Given the `root` of a binary tree and an integer `target`, return the number of paths where the sum of the values along the path equals `target`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

**Example**

* **Input:** `root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]`, `target = 8`
```text
                10
               /  \
              5   -3
             / \    \
            3   2    11
           / \    \
          3  -2    1
```
* **output:** `3`
* **How:** `10 -> (5 -> 3) -> 3`, `10 -> (5 -> 2 -> 1)` and `10 -> (-3 -> 11)`

**Constraints**

* `0 <= root.length <= 13 * 10^4`.
* `root[i]` can be `None` or `-10 < root[i] <= 1000`  
* `-10 < target <= 1000`
