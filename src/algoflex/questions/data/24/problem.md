### Has path sum
Given the `root` of a binary tree and an integer `target`, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals `target`.

> A leaf is a node with no children.

### Example
```
root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1], target = 18

                    5
                   / \
                  4   8
                 /   / \
                11  13  4
               /  \      \
              7    2      1

output = True (5 + 8 + 4 + 1)
```
