### Score tally
Given an array of `scores` e.g `[ '5', '2', 'C', 'D', '+', '+', 'C' ]`, calculate the total points where:
```
+  add the last two scores.
D  double the last score.
C  cancel the last score and remove it.
x  add the score
```
You're always guaranteed to have the last two scores for `+` and the previous score for `D`.

### Example
```markdown
scores = [ '5', '2', 'C', 'D', '+', '+', 'C' ]
output = 30
How:
    '5' - add 5 -> [5]
    '2' - add 2 -> [5, 2]
    'C' - cancel last score -> [5]
    'D' - double last score -> [5, 10]
    '+' - sum last two scores -> [5, 10, 15]
    '+' - sum last two scores -> [5, 10, 15, 25]
    'C' - cancel last score -> [5, 10, 15]

    return sum -> 30
```
