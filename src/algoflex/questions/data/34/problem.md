### Binary tree cousins
Given the `root` of a binary tree with unique values and the value of two different nodes in the tree `x` and `y`, check whether x and y are cousins. 

x and y are guaranteed to be in the tree. 

> Two nodes of a binary tree are cousins if they have the same depth with different parents.

### Example
```
root = [100, 50, 600, 45, 55, 500, 1000], x = 45, y = 500

                 100
               /     \
             50       600
            /  \     /    \
          45   55   500   1000

output = True
```

```
root = [5, 3, 7], x = 3, y = 7

      5
     / \
    3   7

output = False (same depth but same parent)
```