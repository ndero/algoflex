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
}
