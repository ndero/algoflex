### Replace words
Given an array `roots` of strings and a `sentence` of words separated by spaces. Replace all the words in the sentence with the root forming it. If a word can be replaced by more than one root, replace it with the shortest length root.

Return the sentence after the replacement.

**Example 1**

* **Inputs:** `roots = ["cat", "bat", "rat"]`, `sentence = "the cattle was rattled by the battery"`
* **Output:** `"the cat was rat by the bat"`

**Example 2**

* **Input:** `roots = ["a", "b", "c"]`, `sentence = "aadsfasf absbs bbab cadsfafs"`
* **Output:** `"a a b c"`

**Constraints**

* `0 <= root.length < 30`
* `1 <= root[i] < 5`
* `0 <= sentence.length < 100`
* both `roots` and `sentence` contains only lowercase english letters. s

**Take it further**

Can you do it in a single pass through each word? i.e `O(nm)` where `n` is number of words in the sentence and `m` is the longest word length?
