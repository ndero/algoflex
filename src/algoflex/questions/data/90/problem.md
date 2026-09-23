### Roman to Integer
Given a string `s` representing a **Roman numeral**, convert it to an integer.

Roman numerals are represented by seven different symbols:

Symbol| I | V | X | L | C | D | M | 
------|---|---|---|---|---|---|---|
Value | 1 | 5 | 10 | 50 | 100 | 50 | 1000

Roman numerals are usually written from **largest to smallest** and are added together. For example:

```text
II = 2
XII = 12
XXVII = 27
```

However, there are special **subtractive** cases where a smaller numeral appears before a larger numeral, meaning subtraction is used instead of addition:

```text
IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900
```

### Examples

```text
Input: s = "II"
Output: 2
How: 1 + 1 =  2, hence II
```

```text
Input: s = "IX"
Output: 9
Explanation: X = 10, I = 1 -> 10 - 1 = 9, one of the special subtraction cases
```

```text
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4, so 1000 + 900 + 90 + 4 = 1994.
```

### Constraints
```text
1 <= s.length <= 15
s contains only the characters 'I', 'V', 'X', 'L', 'C', 'D', 'M'.
It is guaranteed that s is a valid Roman numeral in the range [1, 3999].
```