### Replace words
Given an array `roots` of strings and a `sentence` of words separated by spaces. Replace all the words in the sentence with the root forming it. If a word can be replaced by more than one root, replace it with the shortest length root.

Return the sentence after the replacement.

### Example
```
input: roots = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery"
output = "the cat was rat by the bat"
```

```
input: roots = ["a", "b", "c"], sentence = "aadsfasf absbs bbab cadsfafs"
output = "a a b c"
```

### Take it further
Can you do it in a single pass through each word? i.e O(nm) where n is number of words in the sentence and m is the longest word length?
