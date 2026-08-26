### Range frequency query
Given an `arr` design a data structure `RangeFreq` with a method `query(left: int, right: int, value: int) -> int` that returns the number of times the given value occurs in the subarray arr[left...right] (both left and right inclusive)

### Example
```
arr = [1, 3, 7, 7, 7, 3, 4, 1, 7]
rf = RangeFreq(arr)

input: rf.query(2, 5, 7)
output = 3  # 7 appears 3 times between indices 1 and 6

input: rf.query(2, 4, 7)
output = 3

input: rf.query(0, 8, 1)
output = 2

input: rf.query(4, 7, 4)
output = 1
```
