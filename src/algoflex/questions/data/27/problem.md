### Balanced tree
Given the `root` of a binary tree, return `true` if it is balanced or `false` otherwise.

> A balanced tree is one whose difference between maximum height and minimum height is less than 2.

**Example 1**

* **Input:** `root = [12, 8, 16, 4, 9, 13, 18, 11]`
```text
                12
               /  \
              8    16
             / \   / \
            4   9 13  18
           /
          11
```
* **Output:** `true`

**Example 2**

* **Input:** `root = [4, None, 9, None, None, None, 12]`
```text
    4
     \
      9
       \
        12
```
* **Output:** `false`

**Constraints**

* `0 <= root.length <= 2 * 10^5`
* `root[i]` can be `None` or `-10^5 < root[i] < 10^5`

