### Lowest common ancestor
Given the `root` of a binary tree with unique values, and two node values `p` and `q`. Find the lowest common ancestor (LCA) of p and q. The values p and q are guaranteed to be in the tree. 

> The lowest common ancestor of two nodes `p` and `q` is the lowest node in a tree that has both p and q as descendants. A node can be a descendant of itself. 

### Example
```
root = [5, 3, 7], p = 3, q = 7

      5
     / \
    3   7

output = 5
```

```
root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 8, q = 6

            3
          /   \
         5     1
        / \   / \
       6  2  0   8
         / \
        7   4

output = 3 
```

```
root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5, q = 2

            3
          /   \
         5     1
        / \   / \
       6  2  0   8
         / \
        7   4

output = 5 (5 as a descendant of itself)
```