### Daily temperatures
Given an array of daily temperatures `temperatures,` return an array answer such that `answer[i]` is the number of days you have to wait until a warmer temperature. If there is no future day with warmer temperature, set answer[i] = 0.

**Example**

* **Input:** `temperatures = [3, 1, 2]`
* **Output:** `[0, 1, 0]`
* **How:** no day in future higher than 3, 1 day in future higher than 1 and no day in future after 2.

**Constraints**

* `0 <= temperatures.length <= 10^4`
* `0 <= temperatures[i] <= 10^6`