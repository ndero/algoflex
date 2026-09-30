### Valid Binary search tree
Given the `root` of a binary tree, check whether it is a valid binary search tree.

> **Valid BST:** for every node, all nodes in its left subtree are less than the node value and all nodes in its right subtree are greater than the node value.

**Example**

* **Input:** `root = [9, 8, 16]`
```text
      9
     / \
    8  16
```
* **Output:** `true`

**Constraints**

* `0 <= root.length <= 2 * 10^5`
* `root[i]` can be `None` or `-10^5 < root[i] < 10^5`
