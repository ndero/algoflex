### Binary Search Tree has node with value
Given the `root` of a binary search tree and a value `x`, check whether the value x is in the tree and return `true` or `false`.

**Example 1**

* **Input:** `root = [9, 8, 16]`, `x = 5`
```text
      9
     / \
    8   16
```
* **Output:** `false`

**Example 2**

* **Input:** `root = [12, 3, 20]`, `x = 3`
```text
      12
     /  \
    3    20
```
* **Output:** `true`

**Constraints**

* `0 <= root.length < 2 * 10^5`
* `root[i]` can be `None` or `-10^5 <= root[i] < 10^5`
* `-10^5 <= target <= 10^5`