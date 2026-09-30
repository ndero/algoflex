### Tree leaves
Given the `root` of a binary tree, return all the leaves as an array ordered from left to right.

> A leaf is tree node with no children.

**Example 1**

* **Input:** `root = [100, 50, 600, 45, 55, 500, 1000]`
```text
                 100
               /     \
             50       600
            /  \     /    \
          45   55   500   1000
```
* **Output:** `[45, 55, 500, 1000]`

**Example 2**

* **Input:** `root = [7, 5, None, None, 6]`
```text
        7
      /   
    5 
      \
        6
```
* **Output:** `[6]`

**Constraints**

* `0 <= root.length <= 2 * 10^5`
* `root[i]` can be `None` or `-10^5 < root[i] < 10^5`
