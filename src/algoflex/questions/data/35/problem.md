### Same binary tree
Check if two binary trees `p` and `q` are the same given their roots.

> Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example 1**

* **Input:** `p = [1,2,3]`, `q = [1,2,3]`
```text
p =     1
       / \
      2   3

q =     1
       / \
      2   3
```
* **Output:** `true`

**Example 2**

* **Input:** `p = [1,2]`, `q = [1,None,2]`
```text
p =     1
       /
      2

q =    1
        \
        2
```
* **Output:** `false`

**Constraints**

For each `root` `p` or `q`:
* `0 <= root.length <= 10^4`
* `root[i]` can be `None` or `0 < root[i] < 10^4`

