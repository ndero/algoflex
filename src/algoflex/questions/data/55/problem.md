### Minimum cost tickets
Given an array `days` representing planned annual train travelling days and `costs` where `costs = [daily, weekly, monthly]` indicating the daily (1 day), weekly (7 days) and monthly (30 days) ticket costs respectively, return the minimum cost for travelling every day in the given list of days.

Each day is an integer between 1 and 365.

**Example**

* **Input:** `days = [1,4,6,7,8,20]`, `costs = [2,7,15]`
* **Output:** `11`

**Constraints**

* `0 <= days.length <= 365`
* `1 < days[i] <= 365`
* `costs.length == 3`
* `costs[i] > 0`
