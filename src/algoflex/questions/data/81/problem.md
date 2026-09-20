### Palindrome Number
Given an integer `x`, determine whether `x` is a palindrome number and return `True` or `False`. A palindrome number is an integer that reads the same from left to right and from right to left.

Can you do it without converting the integer to a string? With O(log10(x)) time complexity using O(1) extra space?

### Examples
```
Input: x = 123
Output: False
How: 123 reads as 321 from right to left. Not a palindrome. 
```

```
Input: x = 101
Output: True
How: reads 101 from right to left too. Therefore a palindrome.
```

```
Input: x = -111
Output: False
How: reads 111- from right to left. Not a palindrome 
```

### Constraints
```
-2^31 <= x <= 2^31 - 1
```