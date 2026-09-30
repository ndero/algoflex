### Tree in-order traversal
Given the `root` of a binary tree, traverse the tree in order and return the values as an array.

**Example**
* **Input:** `root = [12, 8, 16, 4, 9, 13, 18, 1]`
```text
                12
               /  \
              8    16
             / \   / \
            4   9 13  18
           /
          1
```
* **Output** `[1, 4, 8, 9, 12, 13, 16, 18]`

**Constraints**

* `0 <= root.length <= 2 * 10^5`
* `root[i]` can be `None` or `-10^5 < root[i] < 10^5`
