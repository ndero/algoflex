### Repeated letters
Given a string `s` of lower-case letters. Find all substrings of `s` that contains at least three consecutive identical letters. Return an array of the indices `[start, end]` of the substrings. Order the indices by the start index in ascending order.

**Example**

* **Input:** `s = "abcdddeeeeaabbbcd"`
* **Output:** `[[3,5], [6,9], [12,15]]`
* **How:** "abcdddeeeeaabbbed" has three valid substrings: "ddd","eeee" and "bbb".

**Constraints**

* `0 <= s.length <= 10^5`
* `s` contains all lower-case letters