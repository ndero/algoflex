### Largest rectangle in histogram
Given an array of integers `heights` representing a histogram's bar height where the width of each bar is 1, find the area of the largest rectangle that can be formed within the histogram.

### Example
```
input: [3, 1, 2, 5, 4, 1]

 7 |
 6 |
 5 |      █
 4 |      █ █
 3 |█     █ █
 2 |█   █ █ █
 1 |█ █ █ █ █ █
   +-------------
    0 1 2 3 4 5

output = 8 (formed by bars at indices 3 and 4 with a height of 4)
```
