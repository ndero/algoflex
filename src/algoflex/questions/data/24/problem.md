### Has root to leaf sum
Given the `root` of a binary tree and an integer `target`, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals `target`.

> A leaf is a node with no children.

**Example**

* **Input:** `root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]`, `target = 18`
```text
                    5
                   / \
                  4   8
                 /   / \
                11  13  4
               /  \      \
              7    2      1
```
* **Output:** `true`
* **How:** 5 + 8 + 4 + 1 = 18

**Constraints**

* `0 <= root.length <= 2 * 10^5`
* `root[i]` can be `None` or `-10^5 <= root[i] < 10^5`
* `-10^5 < target <= 10^3`