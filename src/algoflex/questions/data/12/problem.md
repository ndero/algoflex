### Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

Division between two integers should truncate toward zero and it is guaranteed that the given RPN expression is always valid.

### Example
```
input: ["2", "1", "+", "3", "*"]
output = 9
How: ((2 + 1) * 3) = 9
```

```
input: ["4", "13", "5", "/", "+"]
output = 6
How: (4 + (13 / 5)) = 6
```
