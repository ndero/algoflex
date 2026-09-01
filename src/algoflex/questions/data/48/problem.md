### Course Schedule

**Description:**
There are a total of `num_courses` courses you must take, labeled from `0` to `num_courses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`.

Return the ordering of courses you should take to finish all courses. If it is impossible to finish all courses due to circular dependencies, return an empty array `[]`. If there are multiple valid answers, return any of them.


### Examples
```
* Input: `num_courses = 2`, `prerequisites = [[1, 0]]`
* Output: `[0, 1]`
* Explanation: There are 2 courses to take. To take course 1, you must first finish course 0. So the correct course order is `[0, 1]`.
```
```
* Input: `num_courses = 2`, `prerequisites = [[1, 0], [0, 1]]`
* Output: `[]`
* Explanation: To take course 1, you must first take course 0. However, to take course 0, you must first take course 1. Because of this circular dependency, it is impossible to complete all courses.
```
```
* Input: `num_courses = 4`, `prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]`
* Output: `[0, 1, 2, 3]`
* Explanation: There are 4 courses to take. To take course 3, you should have finished both courses 1 and 2. Both courses 1 and 2 require course 0. So a valid order is `[0, 1, 2, 3]`. Another valid order is `[0, 2, 1, 3]`.
```

### Constraints

* `1 <= num_courses <= 2000`
* `0 <= prerequisites.length <= 5000`
* `prerequisites[i].length == 2`
* `0 <= a, b < num_courses`
* All prerequisite pairs `[a, b]` are distinct.
