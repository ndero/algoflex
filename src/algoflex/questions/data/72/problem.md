### Common free time
Given a list `schedule` of employees, which represents the working time for each employee. Each employee has a list of non-overlapping intervals sorted by start time. These intervals represent the employee's working hours.

Return the list of finite intervals representing common, positive-length free time for all employees, also sorted in order of start time.

### Example
```
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
How:
- Employee 1 works: [1,2] and [5,6]
- Employee 2 works: [1,3]
- Employee 3 works: [4,10]
The only common free time across all employees is [3,4].
```

```
Input: schedule = [[[1,2],[3,4]],[[2,3]],[[4,5]]]
Output: []
How:
- Employee 1 works: [1,2] and [3,4]
- Employee 2 works: [2,3]
- Employee 3 works: [4,5]
The schedule covers [1,5] continuously with no gaps.
```
