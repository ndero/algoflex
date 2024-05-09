questions = {
    1: {
        "markdown": """
### Score tally
Given an array of scores e.g `[ '5', '2', 'C', 'D', '+', '+', 'C' ]`, calculate the total points where:
```
+  add the last two scores.
D  double the last score.
C  cancel the last score and remove it.
x  add the score
```
You're always guaranteed to have the last two scores for `+` and the previous score for `D`.
### Example
```
input: [ '5', '2', 'C', 'D', '+', '+', 'C' ]
output: 30
explanation:
    '5' - add 5 -> [5]
    '2' - add 2 -> [5, 2]
    'C' - cancel last score -> [5]
    'D' - double last score -> [5, 10]
    '+' - sum last two scores -> [5, 10, 15]
    '+' - sum last two scores -> [5, 10, 15, 25]
    'C' - cancel last score -> [5, 10, 15]
    return sum -> 30
```
""",
        "title": "Score tally",
        "difficulty": "Easy",
        "test_cases": [
            [[["5", "2", "C", "D", "+", "+", "C"]], 30],
            [[["9", "C", "6", "D", "C", "C"]], 0],
            [[["3", "4", "9", "8"]], 24],
            [[["4", "D", "+", "C", "D"]], 28],
            [[["1", "C"]], 0],
            [[["1", "1", "+", "+", "+", "+", "+", "+", "+", "+"]], 143],
            [[["1", "D", "D", "D", "D", "D"]], 63],
        ],
    },
    2: {
        "markdown": """
### Repeated letters
Given a string k of lower-case letters. the letters can be repeated and
exist consecutively. A substring from k is considered valld if it contains
at least three consecutive identical letters.

An example: k = "abcdddeeeeaabbbed" has three valid substrings: "ddd",
"eeee" and "bbb".

You must order the pairs by the start index in ascending order
### Example
```
Input: "abcdddeeeeaabbbcd"
Output: [[3,5], [6,9], [12,14]]
```
""",
        "title": "Repeated letters",
        "difficulty": "Easy",
        "test_cases": [
            [["abcdddeeeeaabbbb"], [[3, 5], [6, 9], [12, 15]]],
            [["xxxcyyyyydkkkkkk"], [[0, 2], [4, 8], [10, 15]]],
            [
                ["abcdddeeeeaabbbb" * 6],
                [
                    [3, 5],
                    [6, 9],
                    [12, 15],
                    [19, 21],
                    [22, 25],
                    [28, 31],
                    [35, 37],
                    [38, 41],
                    [44, 47],
                    [51, 53],
                    [54, 57],
                    [60, 63],
                    [67, 69],
                    [70, 73],
                    [76, 79],
                    [83, 85],
                    [86, 89],
                    [92, 95],
                ],
            ],
            [["abcd"], []],
            [["aabbccdd"], []],
            [[""], []],
            [["abcdefffghijkl"], [[5, 7]]],
        ],
    },
    3: {
        "markdown": """
### Majority element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than
⌊n / 2⌋ times.

You may assume that the majority element always
exists in the array.
### Example
```
Input: [3, 2, 3]
Output: 3
```
""",
        "title": "Majority element",
        "difficulty": "Easy",
        "test_cases": [
            [[[3, 2, 3]], 3],
            [[[6] * 20], 6],
            [[[9] * 21 + [7] * 20], 9],
            [[[2]], 2],
            [[[]], None],
            [[[6] * 100_000 + [9] * 100_001], 9],
            [[[-2, -2, -4, -2, -4, -4, -4]], -4],
        ],
    },
    4: {
        "markdown": """
### Max profit
You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
### Example
```
input: [7, 1, 5, 3, 6, 4]
output: 5
explanation: buy at price = 1 sell at price = 6

input: [7, 6, 4, 3, 1]
output: 0
```
""",
        "title": "Max profit",
        "difficulty": "Easy",
        "test_cases": [
            [[[7, 1, 5, 3, 6, 4]], 5],
            [[[7, 6, 4, 3, 1]], 0],
            [[[0, 0, 0, 0]], 0],
            [[[4] * 2_000 + [15] * 1_000], 11],
            [[[90] * 10_000 + [50] * 20_000], 0],
            [[[]], 0],
            [[[i for i in range(1, 100_000)]], 99_998],
        ],
    },
    5: {
        "markdown": """
### Valid matching brackets
Given a string of brackets that can either be `[]`, `()` or `{}`.
Check if the brackets are valid.

There no other characters in the string apart from '[', ']', '(', ')', '{'and '}'.

### Example
```
input: "[](){}"
output: True

input: "{{}}[][](()"
output: False

input: "[[[()]]]{}"
output: True
```
""",
        "title": "Valid matching brackets",
        "difficulty": "Easy",
        "test_cases": [
            [["[](){}"], True],
            [["{{}}[][](()"], False],
            [["[[[()]]]{}"], True],
            [["["], False],
            [["{}" * 50_000 + "()" * 50_000 + "[]"], True],
            [
                [
                    "{{{{{{{{{{{{{{{{{{{{{{{{{{{{[[[[[[[[[[()]]]]]]]]]]}}}}}}}}}}}}}}}}}}}}}}}}}}}}"
                ],
                True,
            ],
            [["[" + "()" * 100_000 + ")"], False],
            [["[" + "()" * 100_000 + "]"], True],
        ],
    },
    6: {
        "markdown": """
### Max sum sub array
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest sum,
and return the sum.

### Example
```
input: [-2, 0, -1]
output: 0

input: [2, 3, -2, 4]
output: 7
```
```
""",
        "title": "Max sum sub array",
        "difficulty": "Easy",
        "test_cases": [
            [[[-2, 0, -1]], 0],
            [[[2, 3, -2, 4]], 7],
            [[[-2]], -2],
            [[[i for i in range(100_000)]], 4_999_950_000],
            [[[2] * 50_000 + [-2] * 50_000], 100_000],
            [[[2, -4, 8, 6, 9, -1, 3, -4, 12]], 33],
        ],
    },
    7: {
        "markdown": """
### Max product sub array
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
and return the product.

### Example
```
input: [-2, 0, -1]
output: 0

input: [2, 3, -2, 4]
output: 6
```
```
""",
        "title": "Max product sub array",
        "difficulty": "Easy",
        "test_cases": [
            [[[-2, 0, -1]], 0],
            [[[2, 3, -2, 4]], 6],
            [[[-2, 0, -1, -3]], 3],
            [[[-2]], -2],
            [[[1 for _ in range(200_000)]], 1],
            [[[2, -4, 8, 6, 9, -1, 3, -4, 12]], 497664],
        ],
    },
    8: {
        "markdown": """
### Symmetric difference
Create a function that takes two or more arrays and returns an array of their symmetric difference. The returned array must contain only unique values (no duplicates).

The mathematical term symmetric difference (△ or ⊕) of two sets is the set of elements which are in either of the two sets but not in both.

Return the elements in order of appearance from left to right.

### Example
```
input: [[1, 2, 3], [2, 3, 4]]
output: [1, 4]
```
""",
        "title": "Symmetric difference",
        "difficulty": "Easy",
        "test_cases": [
            [[[1, 2, 3], [2, 3, 4]], [1, 4]],
            [[[1, 2, 4, 4], [0, 1, 6], [0, 1]], [2, 4, 6]],
            [[[i] for i in range(6)], [0, 1, 2, 3, 4, 5]],
            [[[-1], [], [], [0], [1]], [-1, 0, 1]],
            [
                [
                    [9, -4, 8, 3, 12, 0, -4, 8],
                    [3, 3, 8, 6, 7, 10],
                    [11, 12, 10, 13],
                    [5, 15, 3],
                    [11, 15, 11, 11, 6, -2],
                ],
                [9, -4, 0, 7, 13, 5, -2],
            ],
            [[[2] * 50_000 + [-2] * 50_000], [2, -2]],
            [[[i for i in range(100_000)], [i for i in range(100_000)]], []],
            [
                [[i for i in range(100_000)], [i for i in range(10, 100_000)]],
                [i for i in range(10)],
            ],
        ],
    },
    9: {
        "markdown": """
### Pairwise
Given an array `arr`, find element pairs whose sum equal the second argument `target` and return the sum of their indices.
e.g pairwise([7, 9, 11, 13, 15], 20) returns 6 and pairwise([0, 0, 0, 0, 1, 1], 1) returns 10.

Each element can only construct a single pair.

### Example
```
inputs:
    arr: [7, 9, 11, 13, 15]
    target: 20
output: 6
explanation:
    pairs 7 + 13 and 9 + 11, indices 0 + 3 and 1 + 2, total 6

inputs:
    arr: [0, 0, 0, 0, 1, 1]
    target: 1
output: 10
explanation: pairs 0 + 1 and 0 + 1, indices 0 + 4 and 1 + 5, total 10
```
""",
        "title": "Pairwise",
        "difficulty": "Easy",
        "test_cases": [
            [[[7, 9, 11, 13, 15], 20], 6],
            [[[0, 0, 0, 0, 1, 1], 1], 10],
            [[[-1, 6, 3, 2, 4, 1, 3, 3], 5], 15],
            [[[1, 6, 5], 6], 2],
            [[[1, 6, 5, 15, 13, 2, 11], 10], 0],
            [[[i for i in range(0, 100_000, 10)], 10], 1],
        ],
    },
    10: {
        "markdown": """
### Single pair sum
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers as an array.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

### Example
```
inputs:
    arr: [2, 7, 11, 15],
    target: 13
output: [1, 3]
explanation: 2 + 11 one-based indices: 1 and 3

inputs:
    arr: [2, 4, 7, 14],
    target: 6
output: [1, 2]
explanation: 2 + 4, indices 1 and 2
```
""",
        "title": "Single pair sum sorted list",
        "difficulty": "Easy",
        "test_cases": [
            [[[2, 7, 11, 15], 13], [1, 3]],
            [[[2, 4, 7, 14], 6], [1, 2]],
            [[[i for i in range(400_000)], 5], [1, 6]],
            [[[i for i in range(-10, 10)], -10], [1, 11]],
        ],
    },
    11: {
        "markdown": """
### Min length sub array
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target.

If there is no such subarray, return 0 instead.

### Example
```
inputs:
    arr: [2, 3, 1, 2, 4, 3],
    target: 7
output: 2
explanation: sub array [4, 3] has sum >= 7

inputs:
    arr: [1, 3, 6, 2, 1],
    target: 4
output: 1
explanation: sub array [6] has sum >= 4
```
""",
        "title": "Min length sub array",
        "difficulty": "Medium",
        "test_cases": [
            [[[2, 3, 1, 2, 4, 3], 7], 2],
            [[[1, 3, 6, 2, 1], 4], 1],
            [[[i for i in range(500_000)], 3_000_000], 7],
            [[[i for i in range(-10, 10)], 60], 0],
        ],
    },
    12: {
        "markdown": """
### Min in rotated array
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0, 1, 2, 4, 5, 6, 7] becomes [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times. [0, 1, 2, 4, 5, 6, 7] if it was rotated 7 times.

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
### Example
```
input: arr: [4, 5, 6, 7, 0, 1, 2]
output: 0
```
""",
        "title": "Min in rotated array",
        "difficulty": "Medium",
        "test_cases": [
            [[[4, 5, 6, 7, 0, 1, 2]], 0],
            [[[16, 23, 43, 55, -7, -4, 3, 5, 9, 15]], -7],
            [[[i for i in range(36, 1_000_000, 10)]], 36],
            [
                [
                    [i for i in range(-10, 1_000_000, 10)]
                    + [i for i in range(-1_000_000, -10, 10)]
                ],
                -1_000_000,
            ],
            [[[2]], 2],
        ],
    },
    13: {
        "markdown": """
### Count primes
Given a positive integer `n`, write an algorithm to return the number of prime numbers in [0, n]
### Example
```
input: 1000
output: 168
explanation:
    There are 168 prime numbers between 0 and 1000 inclusive.
```
""",
        "title": "Count primes",
        "difficulty": "Medium",
        "test_cases": [
            [[100], 25],
            [[1_000], 168],
            [[10_000], 1229],
            [[100_000], 9592],
            [[2], 1],
            [[3], 2],
            [[1], 0],
            [[1_000_000], 78498],
        ],
    },
    14: {
        "markdown": """
### Permutations
Given an array nums of distinct integers, return all the possible permutations.
You can return the permutations in any order.

Can you do it without python's itertools?

### Example
```
input: [1, 2]
output: [[1, 2], [2, 1]]
```
""",
        "title": "Permutations",
        "difficulty": "Medium",
        "test_cases": [
            [[[1, 2]], [[1, 2], [2, 1]]],
            [
                [[i for i in range(1, 5)]],
                [
                    [1, 2, 3, 4],
                    [1, 2, 4, 3],
                    [1, 3, 2, 4],
                    [1, 3, 4, 2],
                    [1, 4, 2, 3],
                    [1, 4, 3, 2],
                    [2, 1, 3, 4],
                    [2, 1, 4, 3],
                    [2, 3, 1, 4],
                    [2, 3, 4, 1],
                    [2, 4, 1, 3],
                    [2, 4, 3, 1],
                    [3, 1, 2, 4],
                    [3, 1, 4, 2],
                    [3, 2, 1, 4],
                    [3, 2, 4, 1],
                    [3, 4, 1, 2],
                    [3, 4, 2, 1],
                    [4, 1, 2, 3],
                    [4, 1, 3, 2],
                    [4, 2, 1, 3],
                    [4, 2, 3, 1],
                    [4, 3, 1, 2],
                    [4, 3, 2, 1],
                ],
            ],
            [[[1]], [[1]]],
        ],
    },
    15: {
        "markdown": """
### Combinations
Given a string and a positive integer k, return all possible combinations of characters of size k.
You can return the combinations in any order.

Are your hands tied without python's itertools 😅?

### Example
```
input:
    string: "abcd",
    k: 3
output: 'abc', 'abd', 'acd', 'bcd'
```
""",
        "title": "Combinations",
        "difficulty": "Medium",
        "test_cases": [
            [["abcd", 3], ["abc", "abd", "acd", "bcd"]],
            [
                ["combinations", 2],
                [
                    "co",
                    "cm",
                    "cb",
                    "ci",
                    "cn",
                    "ca",
                    "ct",
                    "ci",
                    "co",
                    "cn",
                    "cs",
                    "om",
                    "ob",
                    "oi",
                    "on",
                    "oa",
                    "ot",
                    "oi",
                    "oo",
                    "on",
                    "os",
                    "mb",
                    "mi",
                    "mn",
                    "ma",
                    "mt",
                    "mi",
                    "mo",
                    "mn",
                    "ms",
                    "bi",
                    "bn",
                    "ba",
                    "bt",
                    "bi",
                    "bo",
                    "bn",
                    "bs",
                    "in",
                    "ia",
                    "it",
                    "ii",
                    "io",
                    "in",
                    "is",
                    "na",
                    "nt",
                    "ni",
                    "no",
                    "nn",
                    "ns",
                    "at",
                    "ai",
                    "ao",
                    "an",
                    "as",
                    "ti",
                    "to",
                    "tn",
                    "ts",
                    "io",
                    "in",
                    "is",
                    "on",
                    "os",
                    "ns",
                ],
            ],
            [["rat", 3], ["rat"]],
            [["rat", 1], ["r", "a", "t"]],
            [["rat", 0], []],
        ],
    },
    16: {
        "markdown": """
### Single number
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

### Example
```
input: [4, 1, 2, 1, 2]
output: 4
```
""",
        "title": "Single number",
        "difficulty": "Easy",
        "test_cases": [
            [[[4, 1, 2, 1, 2]], 4],
            [[[2]], 2],
            [[[i for i in range(1, 500_000)] + [i for i in range(500_000)]], 0],
        ],
    },
    17: {
        "markdown": """
### Powers of 2
Given an integer `n`, find whether it is a power of `2`.

### Example
```
input: 64
output: True

input: 20
output: False
```
""",
        "title": "Powers of 2",
        "difficulty": "Easy",
        "test_cases": [
            [[64], True],
            [[20], False],
            [[1024], True],
            [[2], True],
            [[0], False],
            [[1267650600228229401496703205376], True],
            [[1267650600228229401496703205377], False],
            [[-64], False],
        ],
    },
    18: {
        "markdown": """
### Reverse Polish Notation
Evaluate the value of an arithmetic opression in Reverse Polish Notation. Valid operators are +, -, *, and /. Each operand may be an integer or another opression.

Note that division between two integers should truncate toward zero. It is guaranteed that the given RPN opression is always valid. That means the expression will always evaluate to a result, and there will not be any division by zero operation.

### Example
```
input: ["2", "1", "+", "3", "*"]
output: 9
explanation: ((2 + 1) * 3) = 9

input: ["4", "13", "5", "/", "+"]
output: 6
explanation: (4 + (13 / 5)) = 6
```
""",
        "title": "Reverse polish notation",
        "difficulty": "Easy",
        "test_cases": [
            [[["2", "1", "+", "3", "*"]], 9],
            [[["4", "13", "5", "/", "+"]], 6],
            [
                [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]],
                12,
            ],
        ],
    },
    19: {
        "markdown": """
### Roman numerals
Convert a given integer, `n`,  to its equivalent roman numerals for 0 < `n` < 4000.

|Decimal | 1000 | 900 | 400 | 100 | 90 | 50 | 40 | 10 | 9 | 5 | 4 | 1 |
|--------|------|-----|-----|-----|----|----|----|----|---|---|---|---|
|Roman | M | CM | CD | C | XC | L | XL | X | IX | V | IV | I|


### Example
```
input: 4
output: 'IV'

input: 23
output: 'XXIII'
```
""",
        "title": "Roman numerals",
        "difficulty": "Medium",
        "test_cases": [
            [[4], "IV"],
            [[23], "XXIII"],
            [[768], "DCCLXVIII"],
            [[1], "I"],
            [[3999], "MMMCMXCIX"],
            [[369], "CCCLXIX"],
            [[1318], "MCCCXVIII"],
            [[1089], "MLXXXIX"],
            [[2424], "MMCDXXIV"],
            [[999], "CMXCIX"],
        ],
    },
    20: {
        "markdown": """
### Longest common subsequence (LCS)
Given two strings text1 and text2, return their longest common subsequence. If there is no common subsequence, return ''.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, ‘ace’ is a subsequence of ‘abcde’. A common subsequence of two strings is a subsequence that is common to both strings.

### Example
```
input:
    text1: "math"
    text2: 'arithmetic'
output: 'ath'
```
""",
        "title": "Longest common subsequence",
        "difficulty": "Medium",
        "test_cases": [
            [["math", "arithmetic"], "ath"],
            [["original", "origin"], "origin"],
            [["foo", "bar"], ""],
            [["", "arithmetic"], ""],
            [["shesellsseashellsattheseashore", "isawyouyesterday"], "saester"],
            [["@work3r", "m@rxkd35rt"], "@rk3r"],
        ],
    },
    21: {
        "markdown": """
### Longest common substring (LCS)
Given two strings text1 and text2, return their longest common substring. If there is no common substring, return ''.

A substring of a string is a new string generated from the original string with adjacent characters.
For example, "rain" is a substring of "grain". A common substring of two strings is a substring that is common to both strings.

### Example
```
input:
    text1: "brain"
    text2: 'drain'
output: 'rain'
```
""",
        "title": "Longest common substring",
        "difficulty": "Medium",
        "test_cases": [
            [["brain", "drain"], "rain"],
            [["math", "arithmetic"], "th"],
            [["blackmarket", "stagemarket"], "market"],
            [
                ["theoldmanoftheseaissowise", "sowisetheoldmanoftheseais"],
                "theoldmanoftheseais",
            ],
        ],
    },
    22: {
        "markdown": """
### Happy number
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.

Implement a function that returns true if the number is happy, or false if not.
### Example
```
input: 2
output: False

input: 7
output: True
```
""",
        "title": "Happy number",
        "difficulty": "Easy",
        "test_cases": [
            [[2], False],
            [[7], True],
            [[17], False],
            [[19], True],
            [[300_003], False],
            [[20_345_329], False],
            [[0], False],
            [[1], True],
        ],
    },
    23: {
        "markdown": """
### Jump game I
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

### Example
```
input: [2, 3, 1, 1, 4]
output: True
```
Jump 1 step to index 1. jump 3 steps from index 1 to get to the end of array
""",
        "title": "Jump game I",
        "difficulty": "Easy",
        "test_cases": [
            [[[2, 3, 1, 1, 4]], True],
            [[[0]], True],
            [[[2, 1, 1, 0, 4]], False],
            [[[i for i in range(200_000)]], False],
            [[[1 for _ in range(200_000)]], True],
            [[[0, 0]], False],
            [[[200_000] + [0] * 200_000], True],
        ],
    },
    24: {
        "markdown": """
### Jump game II
Given an array of non-negative integers nums, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. You can assume that you can always reach the last index.

Return the number of jumps

### Example
```
input: [2, 3, 1, 1, 4]
output: 2
```
Jump 1 step to index 1. jump 3 steps from index 1 to get to the end of array. Total 2 jumps
""",
        "title": "Jump game II",
        "difficulty": "Easy",
        "test_cases": [
            [[[2, 3, 1, 1, 4]], 2],
            [[[1]], 0],
            [[[1, 5]], 1],
            [[[1 for _ in range(200_000)]], 199_999],
            [[[200_000] + [0] * 200_000], 1],
        ],
    },
    25: {
        "markdown": """
### Jump game III
Given an array of non-negative integers arr, you are initially positioned at a start index of the array. When you are at index i, you can jump to i + arr[i] or i — arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

### Example
```
input:
    arr: [4, 2, 3, 0, 3, 1, 2],
    start: 0
output: True
```
""",
        "title": "Jump game III",
        "difficulty": "Medium",
        "test_cases": [
            [[[4, 2, 3, 0, 3, 1, 2], 0], True],
            [[[3, 0, 2, 1, 2], 2], False],
            [[[4, 2, 3, 0, 3, 1, 2], 5], True],
        ],
    },
    26: {
        "markdown": """
### House robber I
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

### Example
```
input: [1, 2, 3, 1]
output: 4
explanation: rob the first and the third house.
```
""",
        "title": "House robber I",
        "difficulty": "Medium",
        "test_cases": [
            [[[1, 2, 3, 1]], 4],
            [[[1, 7, 2, 1, 6]], 13],
            [[[1, 2]], 2],
            [[[3]], 3],
            [[[i for i in range(0, 100_000, 100)]], 25_000_000],
        ],
    },
    27: {
        "markdown": """
### House robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

### Example
```
input: [1, 2, 3, 1]
output: 4
explanation: rob houses at indices 0 and 2
```
""",
        "title": "House robber II",
        "difficulty": "Medium",
        "test_cases": [
            [[[1, 2, 3, 1]], 4],
            [[[1, 7, 2, 1, 6]], 13],
            [[[1, 2, 3]], 3],
            [[[i for i in range(0, 100_000, 100)]], 25_000_000],
        ],
    },
    28: {
        "markdown": """
### Course schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Given the number of courses `n` and  a `prerequisites` array, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

### Example
```
input:
    n = 2,
    prerequisites = [[1, 0]]
output: [0, 1]

input:
    n = 4,
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
output: [0, 1, 2, 3] or [0, 2, 1, 3]
```
""",
        "title": "Course schedule",
        "difficulty": "Medium",
        "test_cases": [
            [[2, [[1, 0]]], [0, 1]],
            [[4, [[1, 0], [2, 0], [3, 1], [3, 2]]], [0, 1, 2, 3]],
            [[1, []], [0]],
        ],
    },
    29: {
        "markdown": """
### Minimum height trees (MHTs)
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of `n` nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h)) are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order. The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

### Example
```
input:
    n = 4,
    edges = [[1, 0], [1, 2], [1, 3]]
output: [1]

input:
    n = 6,
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
output: [3, 4]
```
""",
        "title": "Minimum height trees",
        "difficulty": "Medium",
        "test_cases": [
            [[4, [[1, 0], [1, 2], [1, 3]]], [1]],
            [[6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]], [3, 4]],
        ],
    },
    30: {
        "markdown": """
### Trie/Prefix tree
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

### Example
```
input:
    dictionary = ["cat", "bat", "rat"],
    sentence = "the cattle was rattled by the battery"
output: "the cat was rat by the bat"

input:
    dictionary = ["a", "b", "c"],
    sentence = "aadsfasf absbs bbab cadsfafs"
output: "a a b c"
```
""",
        "title": "Trie/Prefix tree",
        "difficulty": "Medium",
        "test_cases": [
            [
                [["cat", "bat", "rat"], "the cattle was rattled by the battery"],
                "the cat was rat by the bat",
            ],
            [[["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"], "a a b c"],
        ],
    },
    31: {
        "markdown": """
### Longest common prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

### Example
```
input: dictionary = ["flower", "flow", "flight"]
output: "fl"

input: dictionary = ["dog", "racecar", "car"]
output: ""
```
""",
        "title": "Longest common prefix",
        "difficulty": "Medium",
        "test_cases": [
            [[["flower", "flow", "flight"]], "fl"],
            [[["dog", "racecar", "car"]], ""],
            [
                [
                    [
                        "algology",
                        "algologies",
                        "algologists",
                        "algometer",
                        "algometric",
                        "algometry",
                        "algophobia",
                        "algologically",
                        "algorithm",
                        "algorism",
                    ]
                ],
                "algo",
            ],
            [[["ORGANOMETALLICS", "ORGANOPHOSPHATE", "ORGANOTHERAPY "]], "ORGANO"],
            [[["lower", "low", "light"]], "l"],
            [
                [
                    [
                        "SYSTEMATISE",
                        "SYSTEMATISED",
                        "SYSTEMATISER",
                        "SYSTEMATISERS",
                        "SYSTEMATISES",
                        "SYSTEMATISING",
                        "SYSTEMATISM",
                        "SYSTEMATISMS",
                        "SYSTEMATIST",
                    ]
                ],
                "SYSTEMATIS",
            ],
            [[["garden", "gardener", "gardened", "gardenful", "gardenia"]], "garden"],
            [[["flytrap", "flyway", "flyweight", "flywheel"]], "fly"],
            [[["flower", "flow", ""]], ""],
        ],
    },
    32: {
        "markdown": """
### Cheapest flight with at most k stops
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei. You are also given three integers src, dest, and k.

Return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

### Example
```
inputs:
    n = 4,
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
    src = 0,
    dest = 3,
    k = 1
output: 700
explanation: the cheapest flight from city 0 to 3 with at most one stop is:
0 -> 1 at a cost of 100
1 -> 3 at a cost of 600
Total cost 700
```
""",
        "title": "Cheapest flight with at most k stops",
        "difficulty": "Medium",
        "test_cases": [
            [
                [
                    4,
                    [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                    0,
                    3,
                    1,
                ],
                700,
            ],
            [
                [
                    4,
                    [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                    0,
                    3,
                    2,
                ],
                400,
            ],
            [
                [
                    3,
                    [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                    0,
                    2,
                    1,
                ],
                200,
            ],
            [
                [
                    3,
                    [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                    0,
                    2,
                    0,
                ],
                500,
            ],
        ],
    },
    33: {
        "markdown": """
### Network delay time
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target. We will send a signal from a given node k.

Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

### Example
```
inputs:
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]],
    n = 4,
    src = 2
output: 2
```
""",
        "title": "Network delay time",
        "difficulty": "Medium",
        "test_cases": [
            [[[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2], 2],
            [[[[1, 2, 1]], 2, 1], 1],
            [[[[1, 2, 1]], 4, 2], -1],
        ],
    },
    34: {
        "markdown": """
### Reachable cities
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

### Example
```
inputs:
    n = 4,
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]],
    threshold = 4
output: 3
```
""",
        "title": "Reachable cities",
        "difficulty": "Medium",
        "test_cases": [
            [[4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4], 3],
            [
                [
                    5,
                    [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],
                    2,
                ],
                0,
            ],
        ],
    },
    35: {
        "markdown": """
### Minimum spanning trees
There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1.

The cost is the sum of the connections’ costs used.

### Example
```
inputs:
    n = 3,
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
output: 6

inputs:
    n = 4,
    connections = [[1, 2, 3], [3, 4, 4]]
output: -1
```
""",
        "title": "Minimum spanning trees",
        "difficulty": "Medium",
        "test_cases": [
            [[3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]], 6],
            [[4, [[1, 2, 3], [3, 4, 4]]], -1],
        ],
    },
    36: {
        "markdown": """
### Critical connections
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Given integer `n` and `connections` arr, return all critical connections in the network in any order.

### Example
```
inputs:
    n = 4,
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
output: [[1, 3]]
```
""",
        "title": "Critical connections",
        "difficulty": "Hard",
        "test_cases": [
            [[4, [[0, 1], [1, 2], [2, 0], [1, 3]]], [[1, 3]]],
            [
                [7, [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [4, 5], [5, 6]]],
                [[1, 3], [5, 6], [4, 5], [1, 4]],
            ],
            [
                [7, [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [4, 5], [5, 6], [2, 6]]],
                [[1, 3]],
            ],
        ],
    },
    37: {
        "markdown": """
### Fractional knapsack
Given a knapsack capacity and two arrays, the first one for weights and the second one for values. Add items to the knapsack to maximize the sum of the values of the items that can be added so that the sum of the weights is less than or equal to the knapsack capacity.

You are allowed to add a fraction of an item.

### Example
```
inputs:
  capacity = 50
  weights = [10, 20, 30]
  values = [60, 100, 120]
output: 240
```
""",
        "title": "Fractional knapsack",
        "difficulty": "Easy",
        "test_cases": [
            [[50, [10, 20, 30], [60, 100, 120]], 240],
            [[60, [10, 20, 30], [60, 100, 120]], 280],
            [[5, [10, 20, 30], [60, 100, 120]], 30],
        ],
    },
    38: {
        "markdown": """
### Subarrays with sum
Given an array and targetSum, return the total number of contigous subarrays inside the array whose sum is equal to targetSum

### Example
```
inputs:
  arr = [13, -1, 8, 12, 3, 9]
  target = 12
output: 3
explanation: [13, -1], [12] and [3, 9]
```
""",
        "title": "Subarrays with sum",
        "difficulty": "Easy",
        "test_cases": [
            [[[13, -1, 8, 12, 3, 9], 12], 3],
            [[[13, -1, 8, 12, 3, 9], 2], 0],
            [[[13, -1, 8, 12, 3, 9], 10], 0],
            [[[13, -1, 8, 12, 3, 9, 7, 5, 9, 10], 75], 1],
            [[[13, -1, 8, 12, 3, 9] * 20_000, 12], 60_000],
            [[[13, -1, 8, 12, 3, 9, 7, 5, 9, 10] * 10_000, 24], 30_000],
        ],
    },
    "_39": {
        "markdown": """
### Paths with sum
> TODO: fix root input
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
### Example
```
inputs:
  root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
  target = 8
output: 3
```
""",
        "title": "Paths with sum",
        "difficulty": "Medium",
        "test_cases": [
            [[6, 8], 3],
            [[8, 22], 3],
            [[9, 20], 1],
        ],
    },
    40: {
        "markdown": """
### Remove occurence
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s. Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.
### Example
```
inputs:
  s = "axeaxae"
  part = "ax"
output: 'eae'
```
""",
        "title": "Remove occurence",
        "difficulty": "Easy",
        "test_cases": [
            [["axeaxae", "ax"], "eae"],
            [["axxxxyyyyb", "xy"], "ab"],
            [["daa-cbaa-c-c", "a-c"], "dab"],
            [["shesellsseashellsattheseashore", "sh"], "esellsseaellsattheseaore"],
        ],
    },
    41: {
        "markdown": """
### Spinal case
Given a string. Convert it to spinal case

Spinal case is all-lowercase-words-joined-by-dashes.

### Example
```
input: "Hello World!"
output: "hello-world"
```
""",
        "title": "Spinal case",
        "difficulty": "Easy",
        "test_cases": [
            [["Hello World!"], "hello-world"],
            [["The Greatest of All Time."], "the-greatest-of-all-time"],
            [["yes/no"], "yes-no"],
            [["...I-am_here lookingFor  You.See!!"], "i-am-here-looking-for-you-see"],
        ],
    },
    42: {
        "markdown": """
### 0/1 knapsack
Given a knapsack capacity and two arrays, the first one for weights and the second one for values. Add items to the knapsack to maximize the sum of the values of the items that can be added so that the sum of the weights is less than or equal to the knapsack capacity.

You can only either include or not include an item. i.e you can't add a part of it.

Return a tuple of maximum value and selected items

### Example
```
inputs:
  capacity = 50
  weights = [10, 20, 30]
  values = [60, 100, 120]

output: (220, [0, 1, 1])
```
""",
        "title": "0/1 knapsack",
        "difficulty": "Easy",
        "test_cases": [
            [[50, [10, 20, 30], [60, 100, 120]], (220, [0, 1, 1])],
            [[60, [10, 20, 30], [60, 100, 120]], (280, [1, 1, 1])],
            [[5, [10, 20, 30], [60, 100, 120]], (0, [0, 0, 0])],
        ],
    },
    43: {
        "markdown": """
### Job scheduling
You have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

### Example
```
inputs:
    start_time = [1, 2, 3, 3],
    end_time = [3, 4, 5, 6],
    profit = [50, 10, 40, 70]

output: 120
```
""",
        "title": "Job scheduling",
        "difficulty": "Easy",
        "test_cases": [
            [[[1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]], 120],
            [[[1, 1, 1], [2, 3, 4], [5, 6, 4]], 6],
        ],
    },
    44: {
        "markdown": """
### Equal array partitions
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

### Example
```
input: [1, 5, 11, 5]
output: True
explanation: [1, 5, 5] and [11]
```
""",
        "title": "Equal array partitions",
        "difficulty": "Medium",
        "test_cases": [
            [[[1, 5, 11, 5]], True],
            [[[6]], False],
            [[[i for i in range(300)]], True],
            [[[1, 5, 13, 5]], False],
            [[[1, 5, 11, 5] * 100], True],
            [[[1, 5, 13, 5, 35, 92, 11, 17, 13, 53]], False],
            [[[i for i in range(1, 330, 2)]], False],
        ],
    },
    45: {
        "markdown": """
### Coin change I
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of each kind of coin.

### Example
```
input:
  coins = [1, 2, 5]
  amount = 11
output: 3
explanation: two 5 coins and one 1 coin.
```
""",
        "title": "Coin change I",
        "difficulty": "Medium",
        "test_cases": [
            [[[1, 2, 5], 11], 3],
            [[[1, 2, 5, 10], 11], 2],
            [[[1, 2, 5, 10, 20], 11], 2],
            [[[1, 2, 5, 10, 20], 110], 6],
            [[[1, 2, 5, 10, 20], 63], 5],
            [[[1, 2, 5, 10, 20, 50], 16], 3],
            [[[1, 2, 5, 10, 20, 50], 28], 4],
            [[[1, 2, 5, 10, 20, 50], 77], 4],
        ],
    },
    46: {
        "markdown": """
### Min cost tickets
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365. Train tickets are sold in three different ways:

- a 1-day pass is sold for costs[0] dollars,
- a 7-day pass is sold for costs[1] dollars
- a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel. Return the minimum number of dollars you need to travel every day in the given list of days.

### Example
```
inputs:
  days = [1, 4, 6, 7, 8, 20]
  costs = [2, 7, 15]

output: 11
```
""",
        "title": "Min cost tickets",
        "difficulty": "Medium",
        "test_cases": [
            [[[1, 4, 6, 7, 8, 20], [2, 7, 15]], 11],
            [[[1, 2, 3, 4, 5, 6, 7], [2, 7, 15]], 7],
            [[[i for i in range(1, 31)], [2, 7, 15]], 15],
            [[[1, 4, 6], [2, 7, 15]], 6],
            [[[5, 6, 7, 8, 9, 10, 11], [2, 7, 15]], 7],
            [[[5, 6, 7, 8, 9, 10, 11, 210, 211, 212, 213, 365], [2, 7, 15]], 16],
            [[[i for i in range(1, 366)], [2, 7, 15]], 190],
        ],
    },
    46: {
        "markdown": """
### Fibonacci numbers
Given a positive interger `n`, return the n<sup>th</sup> fibonacci number

The first 6 fibonacci numbers are:
[0, 1, 1, 2, 3, 5]
### Example
```
input: 0
output: 0

input: 1
output: 1

input: 5
output: 5
```
""",
        "title": "Fibonacci numbers",
        "difficulty": "Easy",
        "test_cases": [
            [[0], 0],
            [[1], 1],
            [[5], 5],
            [[10], 55],
            [[23], 28657],
            [[50], 12586269025],
            [[100], 354224848179261915075],
        ],
    },
    47: {
        "markdown": """
### Climb stairs
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Example
```
input: 0
output: 0
explanation: no stairs, no way to get to the top

input: 1
output: 1
explanation: 1 stair, one way to get to the top

input: 2
output: 2
explanation:
  2 ways to get to the top
    - climb stair 1 then stair 2
    - climb 2 steps to stair 2
```
""",
        "title": "Climb stairs",
        "difficulty": "Easy",
        "test_cases": [
            [[0], 0],
            [[1], 1],
            [[2], 2],
            [[10], 89],
            [[36], 24157817],
        ],
    },
    48: {
        "markdown": """
### Ways to make change
There are four types of common coins in US currency:
  - quarters (25 cents)
  - dimes (10 cents)
  - nickels (5 cents)
  - pennies (1 cent)

  There are six ways to make change for 15 cents:
    - A dime and a nickel
    - A dime and 5 pennies
    - 3 nickels
    - 2 nickels and 5 pennies
    - A nickel and 10 pennies
    - 15 pennies

Implement a function to determine how many ways there are to make change for a given input, `cents`, that represents an amount of US pennies using these common coins.

### Example
```
input: 15
output: 6
```
""",
        "title": "Ways to make change",
        "difficulty": "Medium",
        "test_cases": [
            [[15], 6],
            [[10], 4],
            [[5], 2],
            [[55], 60],
            [[1000], 142511],
            [[10_000], 134235101],
        ],
    },
}
