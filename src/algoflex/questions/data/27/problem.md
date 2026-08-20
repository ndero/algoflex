### Balanced tree
Given the `root` of a binary tree, return `True` if it is balanced or `False` otherwise

> A balanced tree is one whose difference between maximum height and minimum height is less than 2

### Example
```
root = [12, 8, 16, 4, 9, 13, 18, 11]

                12
               /  \
              8    16
             / \   / \
            4   9 13  18
           /
          11

output = True
```

```
root = [4, None, 9, None, None, None, 12]

    4
     \
      9
       \
        12

output = False
```
