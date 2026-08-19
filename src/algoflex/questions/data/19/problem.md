### Paths with sum
Given the `root` of a binary tree and an integer `target`, return the number of paths where the sum of the values along the path equals `target`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

### Example
```
root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], target = 8

                10
               /  \
              5   -3
             / \    \
            3   2    11
           / \    \
          3  -2    1

output = 3
```
