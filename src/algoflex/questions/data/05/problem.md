### Elements in exactly one array 
Create a function that takes two or more `arrays` and returns a `set` of all elements that appear in exactly one array. 

> Return the set of elements belonging to exactly one of the sets.

**Example 1**

* **Input:** `arrays = [1, 2, 3], [2, 3, 4]`
* **Output** `{1, 4}`

**Example 2**

* **Input:** `arrays = [1, 2, 4, 4], [0, 1, 6], [0, 1]`
* **Output:** `{2, 4, 6}` 

**Constraints**

* `1 <= arrays.length < 100`
* `1 <= arrays[i].length < 10^5`
* `-2^31 < arrays[i][j] < 2^31 - 1`