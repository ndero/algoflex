### Range frequency query
Given an `arr` design a data structure `RangeFreq` with a method `query(left: int, right: int, value: int) -> int` that returns the number of times the given value occurs in the subarray arr[left...right] (both left and right inclusive)

**Example**

arr = [1, 3, 7, 7, 7, 3, 4, 1, 7]
rf = RangeFreq(arr)

* **Input:** `rf.query(2, 5, 7)`
* **Output:** `3`  
* **How:** 7 appears 3 times between indices 1 and 6.

* **Input:** `rf.query(2, 4, 7)`
* **Output:** `3`

* **Input:** `rf.query(0, 8, 1)`
* **Output:** `2`

* **Input:** `rf.query(4, 7, 4)`
* **Output:** `1`

**Constraints**

* `0 <= n <= 2 * 10^5` where `n` is the length of `arr`
* `0 <= left, right <= n` and `left <= right`