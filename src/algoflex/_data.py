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
An example: k = abcdddeeeeaabbbed has three valid substrings: "ddd",
"eeee" and "bbb".
You must order the pairs by the start index in ascending order
### Example
```
Input: k = "abcdddeeeeaabbbcd"
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
```""",
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
}
