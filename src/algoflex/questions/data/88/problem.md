### Reverse Integer
Given a signed 32-bit integer `x`, return `x` with its digits reversed.

If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, return `0`.

**Note:** Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

### Examples
```text
Input: x = 12
Output: 21
```

```text
Input: x = -12
Output: -21
```

```text
Input: x = 100
Output: 1
How: Leading zeros are dropped after reversing.
```

```text
Input: x = 0
Output: 0
```

```text
Input: x = 2_000_000_003
Output: 0
Explanation: 2_000_000_003 reversed is 3_000_000_002, which is outside the signed 32-bit integer range.
```

### Constraints
```text
-2^31 <= x <= 2^31 - 1
```
