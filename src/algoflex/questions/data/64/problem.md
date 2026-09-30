### Largest rectangle in histogram
Given an array of integers `heights` representing a histogram's bar height where the width of each bar is 1, find the area of the largest rectangle that can be formed within the histogram.

**Example**

* **Input:** `heights = [3, 1, 2, 5, 4, 1]`
```text
 7 |
 6 |
 5 |      █
 4 |      █ █
 3 |█     █ █
 2 |█   █ █ █
 1 |█ █ █ █ █ █
   +-------------
    0 1 2 3 4 5
```
* **Output:** `8` 
* **How:** formed by bars at indices 3 and 4 with a height of 4

**Constraints**

* `0 <= heights.length <= 10^4`
* `0 <= heights[i] <= 10^5`