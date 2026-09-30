### Lowest common ancestor
Given the `root` of a binary tree with unique values, and two node values `p` and `q`. Find the lowest common ancestor (LCA) of p and q. 

The values p and q are guaranteed to be in the tree. 

> The lowest common ancestor of two nodes `p` and `q` is the lowest node in a tree that has both p and q as descendants. A node can be a descendant of itself. 

**Example 1**

* **Input:** `root = [5, 3, 7]`, `p = 3`, `q = 7`
```text
      5
     / \
    3   7
```
* **Output:** `5`

**Example 2**

* **Input:** `root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]`, `p = 8`, `q = 6`
```text
            3
          /   \
         5     1
        / \   / \
       6  2  0   8
         / \
        7   4
```
* **Output:** `3` 

**Example 3**

* **Input:** `root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]`, `p = 5`, `q = 2`
```text
            3
          /   \
         5     1
        / \   / \
       6  2  0   8
         / \
        7   4
```
* **Output:** `5` (5 as a descendant of itself)

**Constraints**

* `1 <= root.length <= 10^4`
* `root[i]` can be `None` or `0 < root[i] < 10^4`
