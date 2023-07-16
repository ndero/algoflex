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
}
