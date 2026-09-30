### Score tally
Given an array of `scores` e.g `[ '5', '2', 'C', 'D', '+', '+', 'C' ]`, calculate the total points where:
```text
+  add the last two scores.
D  double the last score.
C  cancel the last score and remove it.
x  add the score.
```
You're always guaranteed to have the last two scores for `+` and the previous score for `D` and `C`.

**Example**

* **Input:** `scores = [ '5', '2', 'C', 'D', '+', '+', 'C' ]`
* **Output:** = `30`
* **How:**
```text
'5' - add 5 -> [5]
'2' - add 2 -> [5, 2]
'C' - cancel last score -> [5]
'D' - double last score -> [5, 10]
'+' - sum last two scores -> [5, 10, 15]
'+' - sum last two scores -> [5, 10, 15, 25]
'C' - cancel last score -> [5, 10, 15]

return total -> 5 + 10 + 15 = 30
```

**Constraints**

* `0 <= scores.length <= 10^4`
* `scores` contains the characters `D`, `C`, `+` and a string integer `x` where `0 <= x <= 2^31 - 1`