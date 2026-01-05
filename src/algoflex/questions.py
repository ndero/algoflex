binary_tree = """
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def array_to_tree(arr, index=0):
    if index >= len(arr) or arr[index] is None:
        return None
    root = TreeNode(arr[index])
    root.left = array_to_tree(arr, index * 2 + 1)
    root.right = array_to_tree(arr, index * 2 + 2)
    return root

def tree_to_array(root):
    # BFS
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            queue.append(node.left)
            queue.append(node.right)
            result.append(node.val)
        else:
            result.append(None)
    return result

"""
linked_list = """
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def array_to_list(arr, i=0):
    if i >= len(arr):
        return None
    head = ListNode(arr[i])
    head.next = array_to_list(arr, i + 1)
    return head

def list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr
"""
questions = {
    0: {
        "markdown": """
### Score tally
Given an array of scores e.g `[ '5', '2', 'C', 'D', '+', '+', 'C' ]`, calculate the total points where:
```
+  add the last two scores.
D  double the last score.
C  cancel the last score and remove it.
x  add the score
```
You're always guaranteed to have the last two scores for `+` and the previous score for `D`.

#### Example
```markdown
input: [ '5', '2', 'C', 'D', '+', '+', 'C' ]
output: 30
How:
    '5' - add 5 -> [5]
    '2' - add 2 -> [5, 2]
    'C' - cancel last score -> [5]
    'D' - double last score -> [5, 10]
    '+' - sum last two scores -> [5, 10, 15]
    '+' - sum last two scores -> [5, 10, 15, 25]
    'C' - cancel last score -> [5, 10, 15]
    
    return sum -> 30
```
""",
        "test_cases": """
test_cases = [
    [[["5", "2", "C", "D", "+", "+", "C"]], 30],
    [[["9", "C", "6", "D", "C", "C"]], 0],
    [[["3", "4", "9", "8"]], 24],
    [[["4", "D", "+", "C", "D"]], 28],
    [[["1", "C"]], 0],
    [[["1", "1", "+", "+", "+", "+", "+", "+", "+", "+"]], 143],
    [[["1", "D", "D", "D", "D", "D"]], 63],
    [[["1", "1"] + ["+"] * 1_00], 2427893228399975082452],
    [[["1", "1"] + ["D"] * 1_00], 2535301200456458802993406410752],
    [[["1", "1"] + ["D"] * 100_000 + ["C"] * 100_001], 1],
    [[["1", "1"] + ["+"] * 50 + ["C"] * 30 + ["+"] * 20], 701408732],
    [[["1", "1", "C", "D", "D", "+"] * 1000], 1300],
]
""",
        "title": "Score tally",
        "level": "Breezy",
    },
    1: {
        "markdown": """
### Repeated letters
Given a string `s` of lower-case letters. Find all substrings of `s` that contains at least three consecutive identical letters. Return an array of the indices `[start, end]` of the substrings. Order the indices by the start index in ascending order.  

#### Example
```
Input: "abcdddeeeeaabbbcd"
Output: [[3,5], [6,9], [12,15]]
How: "abcdddeeeeaabbbed" has three valid substrings: "ddd",
"eeee" and "bbb".

```
""",
        "test_cases": """
test_cases = [
    [["abcdddeeeeaabbbb"], [[3, 5], [6, 9], [1azqa  1qwv                                         b2, 15]]],
    [["xxxcyyyyydkkkkkk"], [[0, 2], [4, 8], [10, 15]]],
    [
        ["abcdddeeeeaabbbb" * 6],
        [
            [3, 5],
            [6, 9],
            [12, 15],
            [19, 21],
            [22, 25],
            [28, 31],
            [35, 37],
            [38, 41],
            [44, 47],
            [51, 53],
            [54, 57],
            [60, 63],
            [67, 69],
            [70, 73],
            [76, 79],
            [83, 85],
            [86, 89],
            [92, 95],
        ],
    ],
    [["abcd"], []],
    [["aabbccdd"], []],
    [[""], []],
    [["abcdefffghijkl"], [[5, 7]]],
    [["abcdeffghijkl" * 100_000], []],
    [["abcdeffghijkl" * 100_000 + "kkk"], [[1_300_000, 1_300_002]]],
    [["kkk" + "abcdeffghijkl" * 100_000], [[0, 2]]],
    [["abcdefffghijkl" * 100_000], [[5 + i, 7 + i] for i in range(0, 100_000 * 14, 14)]],
]""",
        "title": "Repeated letters",
        "level": "Breezy",
    },
    2: {
        "markdown": """
### Valid matching brackets
Given a string of brackets that can either be `[]`, `()` or `{}`.
Check if the brackets are valid.

There no other characters in the string apart from '[', ']', '(', ')', '{'and '}'.

#### Example
```
input: "[](){}"
output: True

input: "{{}}[][](()"
output: False

input: "[[[()]]]{}"
output: True
```
""",
        "test_cases": """
test_cases = [
    [["[](){}"], True],
    [["{{}}[][](()"], False],
    [["[[[()]]]{}"], True],
    [["[[[(((((((()))))))]]]{[{[{[{{({})}}]}]}]}"], False],
    [["[[[([[[[[[[[[[[[[[[()]]]]]]]]]]]]]]])]]]{}"], True],
    [["[[[()]]]{[](){}()[{[{{]}}]}]}"], False],
    [["[[[()]]]{[](){}()[{[{{[]]}}]}]}{}[]((()))"], False],
    [["[[[()]]]{}"], True],
    [["["], False],
    [["{}" * 50_000 + "()" * 50_000 + "[]"], True],
    [
        [
            "{{{{{{{{{{{{{{{{{{{{{{{{{{{{[[[[[[[[[[()]]]]]]]]]]}}}}}}}}}}}}}}}}}}}}}}}}}}}}"
        ],
        True,
    ],
    [["[" + "()" * 100_000 + ")"], False],
    [["[" + "()" * 100_000 + "]"], True],
]
""",
        "title": "Valid matching brackets",
        "level": "Breezy",
    },
    3: {
        "markdown": """
### Max sum sub array
Given a non empty integer array `nums`, find a contiguous non-empty subarray within the array that has the largest sum and return the sum.

#### Example
```
input: [-2, 0, -1]
output: 0

input: [2, 3, -2, 4]
output: 7
```
```
""",
        "test_cases": """
test_cases = [
    [[[-2, 0, -1]], 0],
    [[[-2, 0, -1] * 1000], 0],
    [[[2, 3, -2, 4]], 7],
    [[[2, 3, -2, 4] * 100_000], 700_000],
    [[[-2]], -2],
    [[[i for i in range(100_000)]], 4_999_950_000],
    [[[2] * 50_000 + [-2] * 50_000], 100_000],
    [[[2, -4, 8, 6, 9, -1, 3, -4, 12]], 33],
    [[[2, -4, 8, 0, 9, -1, 0, -4, 12]], 24],
    [[[2, -4, 8, 0, 9, -1, 0, -4, 12] * 10_000], 220_002],
]
""",
        "title": "Max sum sub array",
        "level": "Breezy",
    },
    4: {
        "markdown": """
### Max product sub array
Given a non empty integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product and return the product.

#### Example
```
input: [-2, 0, -1]
output: 0

input: [2, 3, -2, 4]
output: 6
```
```
""",
        "test_cases": """
test_cases = [
    [[[-2, 0, -1]], 0],
    [[[2, 3, -2, 4]], 6],
    [[[-2, 0, -1, -3]], 3],
    [[[-2]], -2],
    [[[1 for _ in range(200_000)]], 1],
    [[[2, -4, 8, 6, 9, -1, 3, -4, 12]], 497664],
    [[[2, 0, 0, 0, 0, 0, 0, 0, 12]], 12],
    [[[2, -4, 1, -6, 0, -1, 3, 0, 12]], 48],
    [[[2, -4, 8, 0, 9, -1, 3, -4, 0]], 12],
    [[[2, -4, 0, 6, 9, 0, 3, -4, 12]], 54],
    [[[2, 0, 8, 6, 9, 0, 3, 0, 12]], 432],
    [[[1, -1, 1, 1, 1, -1, 1, -1, 1]], 1],
    [[[2, -1, -1, 1, 1, -1, 0, 2, 1]], 2],
    [[[2, -1, -1, 1, 1, -1, 0, 2, 1] * 100_000], 4],
]
""",
        "title": "Max product sub array",
        "level": "Breezy",
    },
    5: {
        "markdown": """
### Symmetric difference
Create a function that takes two or more arrays and returns a set of their symmetric difference. The returned array must contain only unique values.

> The mathematical term symmetric difference (△ or ⊕) of two sets is the set of elements which are in either of the two sets but not in both.

#### Example
```
input: [[1, 2, 3], [2, 3, 4]]
output: [1, 4]
```
""",
        "test_cases": """
test_cases = [
    [[[1, 2, 3], [2, 3, 4]], {1, 4}],
    [[[1, 2, 3, 3, 2]], {1, 2, 3}],
    [[[1], [2], [3], [4], [5], [6]], {1, 2, 3, 4, 5, 6}],
    [[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], {1, 7}],
    [[[1, 2, 4, 4], [0, 1, 6], [0, 1]], {2, 4, 6}],
    [[[i] for i in range(6)], {0, 1, 2, 3, 4, 5}],
    [[[-1], [], [], [0], [1]], {-1, 0, 1}],
    [
        [
            [9, -4, 8, 3, 12, 0, -4, 8],
            [3, 3, 8, 6, 7, 10],
            [11, 12, 10, 13],
            [5, 15, 3],
            [11, 15, 11, 11, 6, -2],
        ],
        {9, -4, 0, 7, 13, 5, -2},
    ],
    [[[2] * 50_000 + [-2] * 50_000], {2, -2}],
    [[[i for i in range(100_000)], [i for i in range(100_000)]], {}],
    [
        [[i for i in range(100_000)], [i for i in range(10, 100_000)]],
        {i for i in range(10)},
    ],
]
""",
        "title": "Symmetric difference",
        "level": "Breezy",
    },
    6: {
        "markdown": """
### Pairwise
Given an array `arr`, find element pairs whose sum equal the second argument `target` and return the sum of their indices.

Each element can only construct a single pair.

#### Example
```
inputs:
    arr: [7, 9, 11, 13, 15]
    target: 20
output: 6
How: pairs 7 + 13 and 9 + 11, indices 0 + 3 and 1 + 2, total 6

inputs:
    arr: [0, 0, 0, 0, 1, 1]
    target: 1
output: 10
How: pairs 0 + 1 and 0 + 1, indices 0 + 4 and 1 + 5, total 10
```
""",
        "test_cases": """
test_cases = [
    [[[7, 9, 11, 13, 15], 20], 6],
    [[[0, 0, 0, 0, 1, 1], 1], 10],
    [[[-1, 6, 3, 2, 4, 1, 3, 3], 5], 15],
    [[[1, 6, 5], 6], 2],
    [[[1, 6, 5, 15, 13, 2, 11], 10], 0],
    [[[i for i in range(0, 100_000, 10)], 10], 1],
]
""",
        "title": "Pairwise",
        "level": "Breezy",
    },
    7: {
        "markdown": """
### Min length sub array
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to target.

If there is no such subarray, return `0` instead.

#### Example
```
inputs:
    arr: [2, 3, 1, 2, 4, 3],
    target: 7
output: 2
How: sub array [4, 3] has sum >= 7

inputs:
    arr: [1, 3, 6, 2, 1],
    target: 4
output: 1
How: sub array [6] has sum >= 4
```
""",
        "test_cases": """
test_cases = [
    [[[2, 3, 1, 2, 4, 3], 7], 2],
    [[[1, 3, 6, 2, 1], 4], 1],
    [[[i for i in range(500_000)], 3_000_000], 7],
    [[[i for i in range(-10, 10)], 60], 0],
]
""",
        "title": "Min length sub array",
        "level": "Steady",
    },
    8: {
        "markdown": """
### Min in rotated array
Given a sorted (ascending order) but rotated array `nums`, return the minimum element of this array. You must write an algorithm that runs in **O(log n)** time. 

> an example of rotating an array. If `[0, 1, 2, 4, 5, 6, 7]` is rotated 4 times it becomes `[4, 5, 6, 7, 0, 1, 2]`.

#### Example
```
input: arr: [4, 5, 6, 7, 0, 1, 2]
output: 0
```
""",
        "test_cases": """
test_cases = [
    [[[4, 5, 6, 7, 0, 1, 2]], 0],
    [[[16, 23, 43, 55, -7, -4, 3, 5, 9, 15]], -7],
    [[[i for i in range(36, 1_000_000, 10)]], 36],
    [
        [
            [i for i in range(-10, 1_000_000, 10)]
            + [i for i in range(-1_000_000, -10, 10)]
        ],
        -1_000_000,
    ],
    [[[2]], 2],
]
""",
        "title": "Min in rotated array",
        "level": "Steady",
    },
    9: {
        "markdown": """
### Count primes
Given a positive integer `n`, write an algorithm to return the number of prime numbers in `[0, n]`.

#### Example
```
input: 1000
output: 168
How:
    There are 168 prime numbers between 0 and 1000 inclusive.
```
""",
        "test_cases": """
test_cases = [
    [[100], 25],
    [[1_000], 168],
    [[10_000], 1229],
    [[100_000], 9592],
    [[2], 1],
    [[3], 2],
    [[1], 0],
    [[1_000_000], 78498],
],
""",
        "title": "Count primes",
        "level": "Steady",
    },
    10: {
        "markdown": """
### Single number
Given a non-empty array of integers `nums` where every element appears twice except for one. Return the element that appears once.

You must write an algorithm that runs in **O(n)** average time complexity and uses constant space.

#### Example
```
input: [4, 1, 2, 1, 2]
output: 4
```
""",
        "test_cases": """
test_cases =  [
    [[[4, 1, 2, 1, 2]], 4],
    [[[2]], 2],
    [[[i for i in range(1, 500_000)] + [i for i in range(500_000)]], 0],
]
""",
        "title": "Single number",
        "level": "Breezy",
    },
    11: {
        "markdown": """
### Powers of 2
Given an integer `n`, find whether it is a power of `2`.

#### Example
```
input: 64
output: True

input: 20
output: False
```
""",
        "test_cases": """
test_cases = [
    [[64], True],
    [[20], False],
    [[1024], True],
    [[2], True],
    [[0], False],
    [[1267650600228229401496703205376], True],
    [[1267650600228229401496703205377], False],
    [[-64], False],
]
""",
        "title": "Powers of 2",
        "level": "Breezy",
    },
    12: {
        "markdown": """
### Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

Division between two integers should truncate toward zero and it is guaranteed that the given RPN expression is always valid.

#### Example
```
input: ["2", "1", "+", "3", "*"]
output: 9
How: ((2 + 1) * 3) = 9

input: ["4", "13", "5", "/", "+"]
output: 6
How: (4 + (13 / 5)) = 6
```
""",
        "test_cases": """
test_cases = [
    [[["2", "1", "+", "3", "*"]], 9],
    [[["4", "13", "5", "/", "+"]], 6],
    [
        [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]],
        12,
    ],
]
""",
        "title": "Reverse polish notation",
        "level": "Breezy",
    },
    13: {
        "markdown": """
### Roman numerals
Convert a given integer, `n`,  to its equivalent roman numerals for `0 < n < 4000`.

|Decimal | 1000 | 900 | 400 | 100 | 90 | 50 | 40 | 10 | 9 | 5 | 4 | 1 |
|--------|------|-----|-----|-----|----|----|----|----|---|---|---|---|
|Roman | M | CM | CD | C | XC | L | XL | X | IX | V | IV | I|


#### Example
```
input: 4
output: 'IV'

input: 23
output: 'XXIII'
```
""",
        "title": "Roman numerals",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[4], "IV"],
    [[23], "XXIII"],
    [[768], "DCCLXVIII"],
    [[1], "I"],
    [[3999], "MMMCMXCIX"],
    [[369], "CCCLXIX"],
    [[1318], "MCCCXVIII"],
    [[1089], "MLXXXIX"],
    [[2424], "MMCDXXIV"],
    [[999], "CMXCIX"],
]
""",
    },
    14: {
        "markdown": """
### Longest common substring (LCS)
Given two strings `text1` and `text2`, return their longest common substring. If there is no common substring, return ''.

> A substring of a string is a new string generated from the original string with adjacent characters. For example, "rain" is a substring of "grain". 

#### Example
```
input:
    text1: "brain"
    text2: 'drain'
output: 'rain'
```
""",
        "title": "Longest common substring",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [["brain", "drain"], "rain"],
    [["math", "arithmetic"], "th"],
    [["blackmarket", "stagemarket"], "market"],
    [
        ["theoldmanoftheseaissowise", "sowisetheoldmanoftheseais"],
        "theoldmanoftheseais",
    ],
],
""",
    },
    15: {
        "markdown": """
### Happy number
Given a positive integer `n`, return whether it is a happy number or not. 

> A happy number is a number which if you repeatedly sum the squares of its digits the process will eventually lead to 1. For example, 19 → `1²+9²=82` → `8²+2²=68` → `6²+8²=100` → `1`.
#### Example
```
input: 19
output: True

input: 2
output: False
```
""",
        "title": "Happy number",
        "level": "Breezy",
        "test_cases": """
test_cases = [
    [[19], True],
    [[2], False],
    [[17], False],
    [[202], False],
    [[711], False],
    [[176], True],
    [[19_345_672], False],
    [[345_000_000], False],
    [[1_703_932], False],
    [[2_294_967_295], False],
    [[1], True],
],
""",
    },
    16: {
        "markdown": """
### Trie/Prefix tree
Given an array `roots` of strings and a `sentence` of words separated by spaces. Replace all the words in the sentence with the root forming it. If a word can be replaced by more than one root, replace it with the shortest length root. 

Return the sentence after the replacement.

#### Example
```
input:
    roots = ["cat", "bat", "rat"],
    sentence = "the cattle was rattled by the battery"
output: "the cat was rat by the bat"

input:
    roots = ["a", "b", "c"],
    sentence = "aadsfasf absbs bbab cadsfafs"
output: "a a b c"
```
""",
        "title": "Trie/Prefix tree",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [
        [["cat", "bat", "rat"], "the cattle was rattled by the battery"],
        "the cat was rat by the bat",
    ],
    [[["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"], "a a b c"],
]
""",
    },
    17: {
        "markdown": """
### Fractional knapsack
Given a knapsack `capacity` and two arrays, the first one for `weights` and the second one for `values`. Add items to the knapsack to maximize the sum of the values of the items that can be added so that the sum of the weights is less than or equal to the knapsack capacity.

You are allowed to add a fraction of an item.

#### Example
```
inputs:
  capacity = 50
  weights = [10, 20, 30]
  values = [60, 100, 120]
output: 240
```
""",
        "title": "Fractional knapsack",
        "level": "Breezy",
        "test_cases": """
test_cases = [
    [[50, [10, 20, 30], [60, 100, 120]], 240],
    [[60, [10, 20, 30], [60, 100, 120]], 280],
    [[5, [10, 20, 30], [60, 100, 120]], 30],
],
""",
    },
    18: {
        "markdown": """
### Subarrays with sum
Given an array `arr` and `target`, return the total number of contigous subarrays inside the array whose sum is equal to `target`

#### Example
```
inputs:
  arr = [13, -1, 8, 12, 3, 9]
  target = 12
output: 3
How: [13, -1], [12] and [3, 9]
```
""",
        "title": "Subarrays with sum",
        "level": "Breezy",
        "test_cases": """
test_cases = [
    [[[13, -1, 8, 12, 3, 9], 12], 3],
    [[[13, -1, 8, 12, 3, 9], 2], 0],
    [[[13, -1, 8, 12, 3, 9], 10], 0],
    [[[13, -1, 8, 12, 3, 9, 7, 5, 9, 10], 75], 1],
    [[[13, -1, 8, 12, 3, 9] * 20_000, 12], 60_000],
    [[[13, -1, 8, 12, 3, 9, 7, 5, 9, 10] * 10_000, 24], 30_000],
],
""",
    },
    19: {
        "markdown": """
### Paths with sum
Given the `root` of a binary tree and an integer `target`, return the number of paths where the sum of the values along the path equals `target`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

#### Example
```
inputs:
  root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
  target = 8
output: 3
```
""",
        "test_cases": f"""
{binary_tree}
root1 = array_to_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
root2 = array_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
test_cases = [
        [[root1, 8], 3],
        [[root2, 22], 3],
        [[root2, 20], 1],
]
""",
        "title": "Paths with sum",
        "level": "Steady",
    },
    20: {
        "markdown": """
### Power set 
Given an array `nums` of unique numbers, return all subsets (power set) of the given array. 

#### Example
```
input: [1, 2, 3]
output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

input: [0]
output: [[], [0]]
```
""",
        "title": "Power set",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[[1, 2, 3]], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]],
    [[[0]], [[], [0]]],
]
""",
    },
    21: {
        "markdown": """
### Spinal case
Given a string. Convert it to spinal case

> Spinal case is all-lowercase-words-joined-by-dashes.

#### Example
```
input: "Hello World!"
output: "hello-world"
```
""",
        "title": "Spinal case",
        "level": "Breezy",
        "test_cases": """
test_cases = [
    [["Hello World!"], "hello-world"],
    [["The Greatest of All Time."], "the-greatest-of-all-time"],
    [["yes/no"], "yes-no"],
    [["...I-am_here lookingFor  You.See!!"], "i-am-here-looking-for-you-see"],
]
""",
    },
    22: {
        "markdown": """
### 0/1 knapsack
Given a knapsack `capacity` and two arrays, the first one for `weights` and the second one for `values`. Add items to the knapsack to maximize the sum of the values of the items that can be added so that the sum of the weights is less than or equal to the knapsack capacity.

You can only either include or not include an item. i.e you can't add a portion of it.

Return a tuple of maximum value and selected items

#### Example
```
inputs:
  capacity = 50
  weights = [10, 20, 30]
  values = [60, 100, 120]

output: (220, [0, 1, 1])
```
""",
        "title": "0/1 knapsack",
        "level": "Breezy",
        "test_cases": """
test_cases = [
    [[50, [10, 20, 30], [60, 100, 120]], (220, [0, 1, 1])],
    [[60, [10, 20, 30], [60, 100, 120]], (280, [1, 1, 1])],
    [[5, [10, 20, 30], [60, 100, 120]], (0, [0, 0, 0])],
]
""",
    },
    23: {
        "markdown": """
### Equal array partitions
Given an integer array `nums`, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

#### Example
```
input: [1, 5, 11, 5]
output: True
How: [1, 5, 5] and [11]
```
""",
        "title": "Equal array partitions",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[[1, 5, 11, 5]], True],
    [[[6]], False],
    [[[i for i in range(300)]], True],
    [[[1, 5, 13, 5]], False],
    [[[1, 5, 11, 5] * 100], True],
    [[[1, 5, 13, 5, 35, 92, 11, 17, 13, 53]], False],
    [[[i for i in range(1, 330, 2)]], False],
]
""",
    },
    24: {
        "markdown": """
### Max water held
Given an array `nums` where each number represents the height of a vertical wall, find two walls that hold the most water between them and return the units of water contained. 

> To calculate Units of water held, multiply the `width(base)` by `height`

#### Example
```
input: [1,8,6,2,5,4,8,3,7]
output: 49
how: water held between lines 2 and 9

input: [1, 1]
output: 1
```
""",
        "title": "Max water held",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[[1,8,6,2,5,4,8,3,7]], 49],
    [[[1, 1]], 1],
],
""",
    },
    25: {
        "markdown": """
### Climb stairs
You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#### Example
```
input: 0
output: 0
How: no stairs, no way to get to the top

input: 1
output: 1
How: 1 stair, one way to get to the top

input: 2
output: 2
How:
  2 ways to get to the top
    - climb stair 1 then stair 2
    - climb 2 steps to stair 2
```
""",
        "title": "Climb stairs",
        "level": "Breezy",
        "test_cases": """
test_cases = [
    [[0], 0],
    [[1], 1],
    [[2], 2],
    [[10], 89],
    [[36], 24157817],
],
""",
    },
    26: {
        "markdown": """
### Ways to make change
Write an algorithm to determine how many ways there are to make change for a given input, `cents` of US currency. 

There are four types of common coins in US currency:
  - quarters (25 cents)
  - dimes (10 cents)
  - nickels (5 cents)
  - pennies (1 cent)

#### Example
```
input: 15
output: 6
How: There are six ways to make change for 15 cents
  - A dime and a nickel
  - A dime and 5 pennies
  - 3 nickels
  - 2 nickels and 5 pennies
  - A nickel and 10 pennies
  - 15 pennies

```
""",
        "title": "Ways to make change",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[15], 6],
    [[10], 4],
    [[5], 2],
    [[55], 60],
    [[1000], 142511],
    [[10_000], 134235101],
],
""",
    },
    27: {
        "markdown": """
### Has path sum
Given the `root` of a binary tree and an integer `target`, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals `target`.

> A leaf is a node with no children.

#### Example
```
input:
  root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
  target = 18
output: True
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1])
t2 = array_to_tree([1, 2, 3, None, 4])
test_cases = [
    [[t1, 18], True],
]
""",
        "title": "Has path sum",
        "level": "Steady",
    },
    28: {
        "markdown": """
### Has node BST
Given the `root` of a binary search tree and a value `x`, check whether x is in the tree and return `True` or `False`

#### Example
```
input:
  root = [9, 8, 16]
  x = 5
output: False

input:
  root = [12, 3, 20]
  x = 3
output: True
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([9, 8, 16])
t2 = array_to_tree([9, 8, 16, 4])
t3 = array_to_tree([12, 3, 20])
t4 = array_to_tree([12, 3, 20, None, 5])
test_cases = [
    [[t1, 5], False],
    [[t3, 3], True],
    [[t2, 4], True],
    [[t4, 21], False],
]
""",
        "title": "Has node BST",
        "level": "Steady",
    },
    29: {
        "markdown": """
### BST min
Given the `root` of a binary search tree find the minimum value and return it

#### Example
```
input: [12, 3, 20]
output: 3
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([9, 8, 16])
t2 = array_to_tree([9, 8, 16, 4])
t3 = array_to_tree([12, 3, 20])
t4 = array_to_tree([12, 3, 20, None, 5])
test_cases = [
    [[t3], 3],
    [[t1], 8],
    [[t2], 4],
    [[t4], 3],
]
""",
        "title": "BST min",
        "level": "Steady",
    },
    30: {
        "markdown": """
### Balanced tree
Given the `root` of a binary search tree, return `True` if it is balanced or `False` otherwise

> A balanced tree is one whose difference between maximum height and minimum height is less than 2

#### Example
```
input: [12, 8, 16, 4, 9, 13, 18, 11]
output: True

input: [4, None, 9, None, None, None, 12]
output: False
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([12, 8, 16, 4, 9, 13, 18, 11])
t2 = array_to_tree([4, None, 9, None, None, None, 12])
t3 = array_to_tree([12, 3, 20, None, 5])
test_cases = [
    [[t1], True],
    [[t2], False],
    [[t3], True],
]
""",
        "title": "Balanced tree",
        "level": "Steady",
    },
    31: {
        "markdown": """
### Tree in-order traversal
Given the `root` of a binary search tree, traverse the tree in order and return the values as an array.

#### Example
```
input: [12, 8, 16, 4, 9, 13, 18, 11]
output: [4, 8, 9, 11, 12, 13, 16, 18]
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([12, 8, 16, 4, 9, 13, 18, 11])
test_cases = [
    [[t1], [4, 8, 9, 11, 12, 13, 16, 18]],
]
""",
        "title": "Tree in-order traversal",
        "level": "Steady",
    },
    32: {
        "markdown": """
### Generate parentheses
Given a positive integer `n`, generate all combinations of well formed parentheses with n pairs. 

#### Example
```
input: n = 3
output: ["((()))","(()())","(())()","()(())","()()()"]

input: n = 1
output: ["()"]
```
""",
        "test_cases": """
test_cases = [
    [[1], ["()"]],
    [[3], ["((()))","(()())","(())()","()(())","()()()"]],
]
""",
        "title": "Generate parentheses",
        "level": "Steady",
    },
    33: {
        "markdown": """
### Valid BST
Given the `root` of a binary search tree, check whether it is a valid BST.

> **Valid BST:** for every node, all nodes in its left subtree are less than the node value and all nodes in its right subtree are greater than the node value. 

#### Example
```
input: [2, 1, 3]
output: true

input: [5, 1, 4, None, None, 3, 6]
output: false 
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([5, 1, 4, None, None, 3, 6])
t2 = array_to_tree([2, 1, 3])
test_cases = [
    [[t2], True],
    [[t1], False],
]
""",
        "title": "Valid BST",
        "level": "Steady",
    },
    34: {
        "markdown": """
### Tree level-order traversal
Given the `root` of a binary search tree, traverse the tree using level order traversal and return the values as an array.

#### Example
```
input: [12, 8, 16, 4, 9, 13, 18, 11]
output: [12, 8, 16, 4, 9, 13, 18, 11]
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([12, 8, 16, 4, 9, 13, 18, 11])
test_cases = [
    [[t1], [12, 8, 16, 4, 9, 13, 18, 11]],
]
""",
        "title": "Tree level-order traversal",
        "level": "Steady",
    },
    35: {
        "markdown": """
### Tree leaves
Given the `root` of a binary search tree, return all the leaves as an array ordered from left to right.

> A leaf is tree node with no children. 

#### Example
```
input: [12, 8, 16, 4, 9, 13, 18, 11]
output: [4, 11, 13, 18]
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([12, 8, 16, 4, 9, 13, 18, 11])
test_cases = [
    [[t1], [4, 11, 13, 18]],
]
""",
        "title": "Tree leaves",
        "level": "Steady",
    },
    36: {
        "markdown": """
### Sum right nodes
Given the `root` of a binary search tree, return the sum of all the right nodes

#### Example
```
input: [12, 8, 16, 4, 9, 13, 18, 11]
output: 25
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([12, 8, 16, 4, 9, 13, 18, 11])
test_cases = [
    [[t1], 25],
]
""",
        "title": "Sum right nodes",
        "level": "Steady",
    },
    37: {
        "markdown": """
### Value in array
Given an array of integers `arr` sorted in a non decreasing order, and a target `y`. Return `True` if y is in the array or `False` otherwise

You must write an algorithm that runs in **O(log n)** average time complexity. 

#### Example
```
input:
  arr = [2, 4, 8, 9, 12, 13, 16, 18]
  y = 18
output: True
```
""",
        "test_cases": """
test_cases = [
    [[[2, 4, 8, 9, 12, 13, 16, 18], 18], True],
    [[[i for i in range(5_000_000)], 45], True],
    [[[i for i in range(5_000_000)], 5_000_000], False],
]
""",
        "title": "Value in array",
        "level": "Breezy",
    },
    38: {
        "markdown": """
### Merge sort
Given an array of integers `nums`, use merge sort algorithm to return an array of all the integers sorted in non decreasing order.

#### Example
```
input: [8, 2, 4, 9, 12, 18, 16, 13]
output: [2, 4, 8, 9, 12, 13, 16, 18]
```
""",
        "test_cases": """
test_cases = [
    [[[8, 2, 4, 9, 12, 18, 16, 13]], [2, 4, 8, 9, 12, 13, 16, 18]],
    [[[i for i in range(100_000, -1, -1)]], [i for i in range(100_001)]],
]
""",
        "title": "Merge sort",
        "level": "Breezy",
    },
    39: {
        "markdown": """
### Heap sort
Given an array of integers `nums`, use heap sort algorithm to return an array of all the integers sorted in non decreasing order.

#### Example
```
input: [8, 2, 4, 9, 12, 18, 16, 13]
output: [2, 4, 8, 9, 12, 13, 16, 18]
```
""",
        "test_cases": """
test_cases = [
    [[[8, 2, 4, 9, 12, 18, 16, 13]], [2, 4, 8, 9, 12, 13, 16, 18]],
    [[[i for i in range(100_000, -1, -1)]], [i for i in range(100_001)]],
]
""",
        "title": "Heap sort",
        "level": "Breezy",
    },
    40: {
        "markdown": """
### Quick sort
Given an array of integers `nums`, use quick sort algorithm to return an array of all the integers sorted in non decreasing order.

#### Example
```
input: [8, 2, 4, 9, 12, 18, 16, 13]
output: [2, 4, 8, 9, 12, 13, 16, 18]
```
""",
        "test_cases": """
test_cases = [
    [[[8, 2, 4, 9, 12, 18, 16, 13]], [2, 4, 8, 9, 12, 13, 16, 18]],
    [[[i for i in range(100_000, -1, -1)]], [i for i in range(100_001)]],
]
""",
        "title": "Quick sort",
        "level": "Breezy",
    },
    41: {
        "markdown": """
### Bubble sort
Given an array of integers `nums`, use bubble sort algorithm to return an array of all the integers sorted in non decreasing order.

#### Example
```
input: [8, 2, 4, 9, 12, 18, 16, 13]
output: [2, 4, 8, 9, 12, 13, 16, 18]
```
""",
        "test_cases": """
test_cases = [
    [[[8, 2, 4, 9, 12, 18, 16, 13]], [2, 4, 8, 9, 12, 13, 16, 18]],
    [[[i for i in range(100_000, -1, -1)]], [i for i in range(100_001)]],
]
""",
        "title": "Bubble sort",
        "level": "Breezy",
    },
    42: {
        "markdown": """
### Smaller to the right
Given an integer array `nums`, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

#### Example
```
input: [5, 2, 2, 6, 1]
output: [3, 1, 1, 1, 0]

input: [-1, -1]
output: [0, 0]
```
""",
        "test_cases": """
test_cases = [
    [[[5, 2, 2, 6, 1]], [3, 1, 1, 1, 0]],
    [[[-1, -1]], [0, 0]],
    [[[8, 2, 4, 9, 12, 18, 16]], [2, 0, 0, 0, 0, 1, 0]],
    [[[i for i in range(100_000, -1, -1)]], [0 for i in range(100_001)]],
]
""",
        "title": "Smaller to the right",
        "level": "Edgy",
    },
    43: {
        "markdown": """
### Majority element 
Given an array nums of size n, return the majority element.

> The majority element is the element that appears more than
⌊n / 2⌋ times.

The majority element is guaranteed to exist in the array. 

#### Example
```
Input: [3, 2, 3]
Output: 3
```
""",
        "test_cases": """
test_cases = [
    [[[3, 2, 3]], 3],
    [[[6] * 20], 6],
    [[[9] * 21 + [7] * 20], 9],
    [[[2]], 2],
    [[[]], None],
    [[[6] * 100_000 + [9] * 100_001], 9],
    [[[-2, -2, -4, -2, -4, -4, -4]], -4],

]""",
        "title": "Majority element",
        "level": "Breezy",
    },
    44: {
        "markdown": """
### Max profit
Given an array `prices` where `prices[i]` is the price of a given stock on the ith day. Return the maximum profit that can be made by choosing a single day to buy and choosing a different day in the future to sell that stock. 

If you cannot achieve any profit, return 0.

#### Example
```
Input: prices = [7,1,5,3,6,4]
Output: 5
How: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Input: prices = [7,6,4,3,1]
Output: 0
```
""",
        "test_cases": """
test_cases = [
    [[[7, 1, 5, 3, 6, 4]], 5],
    [[[7, 6, 4, 3, 1]], 0],
    [[[0, 0, 0, 0]], 0],
    [[[4] * 2_000 + [15] * 1_000], 11],
    [[[90] * 10_000 + [50] * 20_000], 0],
    [[[]], 0],
    [[[i for i in range(1, 100_000)]], 99_998],
]
""",
        "title": "Max profit",
        "level": "Breezy",
    },
    45: {
        "markdown": """
### **Pair sum equal target**
Find two numbers in an array `nums` that add up to a specific `target`. Return the indices `[i, j]` such that `nums[i] + nums[j] = target`. 

Each input has exactly one solution.

#### Example
```
- Input → nums = [2, 7, 1, 15], target = 9
- Output → [0, 1] (because 2 + 7 = 9)
```
""",
        "test_cases": """
test_cases = [
    [[[2, 7, 1, 15], 13], [1, 3]],
    [[[2, 4, 7, 14], 6], [1, 2]],
    [[[i for i in range(400_000)], 5], [1, 6]],
    [[[i for i in range(-10, 10)], -10], [1, 11]],
],
""",
        "title": "Pair sum equal target",
        "level": "Breezy",
    },
    46: {
        "markdown": """
### Longest common subsequence (LCS) 
Given two strings `str1` and `str2`, both lowercase, return their longest common subsequence. 

> A subsequence of a string is generated by selecting some characters from the original string while maintaining the relative order of the original characters. e.g 'man' is a subsequence of 'mountain'

#### Example
```
Input: str1 = "mountain", text2 = "man"
Output: 'man'

Input: str1 = "dent", str2 = "crab"
Output: ''
```
""",
        "title": "Longest common subsequence",
        "level": "Steady",
        "test_cases": [
            [["math", "arithmetic"], "ath"],
            [["original", "origin"], "origin"],
            [["foo", "bar"], ""],
            [["", "arithmetic"], ""],
            [["shesellsseashellsattheseashore", "isawyouyesterday"], "saester"],
            [["@work3r", "m@rxkd35rt"], "@rk3r"],
        ],
    },
    47: {
        "markdown": """
### Can you reach the last index?
Given an integer array `nums` where `nums[i]` represents the maximum forward jump length from index `i`. Determine if, starting from the first index (0), you can reach the last index. 

#### Example
```
Input: nums = [2,3,1,1,4]
Output: true

Input: nums = [3,2,1,0,4]
Output: false
```
""",
        "title": "Can you reach the last index?",
        "level": "Steady",
        "test_cases": [
            [[[2, 3, 1, 1, 4]], True],
            [[[0]], True],
            [[[2, 1, 1, 0, 4]], False],
            [[[i for i in range(200_000)]], False],
            [[[1 for _ in range(200_000)]], True],
            [[[0, 0]], False],
            [[[200_000] + [0] * 200_000], True],
        ],
    },
    48: {
        "markdown": """
### Min jumps to reach last index
Given an integer array `nums` where `nums[i]` represents the maximum forward jump length from index `i`. Return the minimum jumps to get from the first index (0) to the last index. 

You are guaranteed to reach the last index. 

#### Example
```
Input: nums = [2,5,2,1,4]
Output: 2
How: jump 1 step to index 1 then 3 steps to the last index. 

Input: nums = [2,3,0,1,4,0]
Output: 3
How: jump 1 step to index 1, 3 steps to index 4 then 1 step to the last index.
```
""",
        "title": "Min jumps to reach last index",
        "level": "Steady",
        "test_cases": [
            [[[2, 3, 1, 1, 4]], 2],
            [[[1]], 0],
            [[[1, 5]], 1],
            [[[1 for _ in range(200_000)]], 199_999],
            [[[200_000] + [0] * 200_000], 1],
        ],
    },
    49: {
        "markdown": """
### Jump to zero
Given an integer array `nums` where `nums[i]` represents the maximum forward or backward jump length from index `i` and a starting index `start'. Check if you can jump to an index where the value is 0.

#### Example
```
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
How: index 5 -> 4 -> 1 -> 3 or 5 -> 6 -> 4 -> 1 -> 3

Input: arr = [3,0,2,1,2], start = 2
Output: false
How: There is no way to get to index 1 starting from index 2.
```
""",
        "title": "Jump to zero",
        "level": "Steady",
        "test_cases": [
            [[[4, 2, 3, 0, 3, 1, 2], 0], True],
            [[[3, 0, 2, 1, 2], 2], False],
            [[[4, 2, 3, 0, 3, 1, 2], 5], True],
        ],
    },
    50: {
        "markdown": """
### Max loot 
Given an integer array `nums` where each `nums[i]` represents the amount of cash stashed in a boat, return the maximum amount that you can steal from the boats given that you cannot steal from any two adjacent boats.  

#### Example
```
Input: nums = [2,2,5,1]
Output: 7
How: Rob boats 1 (2) and 3 (5) -> total loot 7 

Input: nums = [2]
Output: 2
How:  Only one boat, no adjacent boats to worry about. 
```
""",
        "title": "Max loot",
        "level": "Steady",
        "test_cases": [
            [[[1, 2, 3, 1]], 4],
            [[[1, 7, 2, 1, 6]], 13],
            [[[1, 2]], 2],
            [[[3]], 3],
            [[[i for i in range(0, 100_000, 100)]], 25_000_000],
        ],
    },
    51: {
        "markdown": """
### Max loot circle
Given an integer array `nums` where each `nums[i]` represents the amount of cash stashed in a boat, return the maximum amount that you can steal from the boats given that you cannot steal from any two adjacent boats and the boats are arranged in a circle i.e the last boat is adjacent to the first one. 

#### Example
```
Input: nums = [3,5,3]
Output: 5
How: Cannot rob boats 1 and 3 for total of 6 because they are adjacent. So rob boat 2. 
```
""",
        "title": "Max loot circle",
        "level": "Steady",
        "test_cases": [
            [[[1, 2, 3, 1]], 4],
            [[[1, 7, 2, 1, 6]], 13],
            [[[1, 2, 3]], 3],
            [[[i for i in range(0, 100_000, 100)]], 25_000_000],
        ],
    },
    52: {
        "markdown": """
### Course schedule 
Given an array of `courses` representing the courses you have to take where courses[i] = [a, b] indicates that you must take course b in order to take course a. And an integer `n` representing the total number of courses with the courses being labelled from 0 to n - 1. Determine whether you can finish all the courses. 

#### Example
Input: n = 2, courses = [[1,0]]
Output: true
How: Take course 0 then 1. 

Input: n = 2, courses = [[1,0],[0,1]]
Output: false
How: To take course 1 you first need to take course 0 but to take course 0 you need to first take course 1 so no way to take any of them. 
""",
        "title": "Course schedule",
        "level": "Steady",
        "test_cases": [
            [[2, [[1, 0]]], [0, 1]],
            [[4, [[1, 0], [2, 0], [3, 1], [3, 2]]], [0, 1, 2, 3]],
            [[1, []], [0]],
        ],
    },
    53: {
        "markdown": """
### Minimum height trees (MHTs) 
Given an integer `n` representing number of nodes in a tree and an array of `n-1` edges where edges[i] = [a, b] represent an undirected edge between nodes a and b. Return a list of minimum height trees root labels in any order. 

The nodes are labelled from 0 to n - 1. 

> A tree is an undirected graph in which any two vertices are connected by exactly one path. 

> The minimum height trees (MHTs) are nodes from a tree that if choosen as the root result to the minimum `height` of the tree. 

> The height of a tree is the number of edges on the path from the root to the the farthest leaf. 

#### Example
```
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
```
""",
        "title": "Minimum height trees",
        "level": "Steady",
        "test_cases": [
            [[4, [[1, 0], [1, 2], [1, 3]]], [1]],
            [[6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]], [3, 4]],
        ],
    },
    54: {
        "markdown": """
### Longest common prefix
Given an array of strings `strs`, all lowercase, return the longest common prefix of all the strings. 

#### Example
```
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
```
""",
        "title": "Longest common prefix",
        "level": "Steady",
        "test_cases": [
            [[["flower", "flow", "flight"]], "fl"],
            [[["dog", "racecar", "car"]], ""],
            [
                [
                    [
                        "algology",
                        "algologies",
                        "algologists",
                        "algometer",
                        "algometric",
                        "algometry",
                        "algophobia",
                        "algologically",
                        "algorithm",
                        "algorism",
                    ]
                ],
                "algo",
            ],
            [[["ORGANOMETALLICS", "ORGANOPHOSPHATE", "ORGANOTHERAPY "]], "ORGANO"],
            [[["lower", "low", "light"]], "l"],
            [
                [
                    [
                        "SYSTEMATISE",
                        "SYSTEMATISED",
                        "SYSTEMATISER",
                        "SYSTEMATISERS",
                        "SYSTEMATISES",
                        "SYSTEMATISING",
                        "SYSTEMATISM",
                        "SYSTEMATISMS",
                        "SYSTEMATIST",
                    ]
                ],
                "SYSTEMATIS",
            ],
            [[["garden", "gardener", "gardened", "gardenful", "gardenia"]], "garden"],
            [[["flytrap", "flyway", "flyweight", "flywheel"]], "fly"],
            [[["flower", "flow", ""]], ""],
        ],
    },
    55: {
        "markdown": """
### Cheapest flight with at most k stops
You are given `n` cities connected by a number of `flights` represented as an array where flights[i] = [from, to, cost] indicate a flight from city `from` to city `to` that costs `cost`. 

You are also given three integers `src`, `dst` and `k`. Find the cheapest cost from `src` to `dst` with at most `k` stops. 

Return -1 if there's no such route.

#### Example
```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
```
""",
        "title": "Cheapest flight with at most k stops",
        "level": "Steady",
        "test_cases": [
            [
                [
                    4,
                    [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                    0,
                    3,
                    1,
                ],
                700,
            ],
            [
                [
                    4,
                    [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                    0,
                    3,
                    2,
                ],
                400,
            ],
            [
                [
                    3,
                    [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                    0,
                    2,
                    1,
                ],
                200,
            ],
            [
                [
                    3,
                    [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                    0,
                    2,
                    0,
                ],
                500,
            ],
        ],
    },
    56: {
        "markdown": """
### Network delay time 
Given a network of `n` nodes, labelled 1 to n and a list of travel `times` as directed edges where times[i] = (u, v, w) with u being the source, v the target and w the time it takes for a signal to travel from u to v. 

Find the minimum time it takes for a signal from a source node `k` to reach all the other nodes. 

Return -1 if it's impossible for all the nodes to receive the signal. 

#### Example
```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```
""",
        "title": "Network delay time",
        "level": "Steady",
        "test_cases": [
            [[[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2], 2],
            [[[[1, 2, 1]], 2, 1], 1],
            [[[[1, 2, 1]], 4, 2], -1],
        ],
    },
    57: {
        "markdown": """
### Reachable cities
Given `n` cities labelled 0 to n - 1 and an array `edges` where edges[i] = [from, to, weight] represents a weighted bidirectional edge between cities `from` and `to`.  Return the smallest number of cities that are reachable and whose distance is at most `distanceThreshold`. 

If multiple such cities, return the one with the greatest number. 

#### Examples
```
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
```
""",
        "title": "Reachable cities",
        "level": "Steady",
        "test_cases": [
            [[4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4], 3],
            [
                [
                    5,
                    [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],
                    2,
                ],
                0,
            ],
        ],
    },
    58: {
        "markdown": """
### Minimum spanning trees 
You are given `n` cities numbered from 1 to n and an array `connections` where connections[i] = [x, y, cost] indicates a weighted bidirectional connection between cities x and y. 

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. 

> The cost is the sum of the connections’ costs used.

Return -1 if it isn't possible to connect all n cities. 

#### Example
```
inputs:
    n = 3,
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
output: 6

inputs:
    n = 4,
    connections = [[1, 2, 3], [3, 4, 4]]
output: -1
```
""",
        "title": "Minimum spanning trees",
        "level": "Steady",
        "test_cases": [
            [[3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]], 6],
            [[4, [[1, 2, 3], [3, 4, 4]]], -1],
        ],
    },
    59: {
        "markdown": """
### Critical connections
Given `n` servers labelled 0 to n - 1 connected by undirected `connections` where connections[i] = [a, b] indicates a connection between servers a and b. Return all the critical connections in the network in any order. 

> A critical connection is one that, if removed, will make some servers not be able to reach some other server. 

#### Examples
```
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
```
""",
        "title": "Critical connections",
        "level": "Edgy",
        "test_cases": [
            [[4, [[0, 1], [1, 2], [2, 0], [1, 3]]], [[1, 3]]],
            [
                [7, [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [4, 5], [5, 6]]],
                [[1, 3], [5, 6], [4, 5], [1, 4]],
            ],
            [
                [7, [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [4, 5], [5, 6], [2, 6]]],
                [[1, 3]],
            ],
        ],
    },
    60: {
        "markdown": """
### Job scheduling
Given arrays `startTime`, `endTime` and `profit` representing `n` jobs with the ith job scheduled to be done from startTime[i] to endTime[i] generating profit[i]. Find the maximum profit you can make from the jobs

If you choose a job that ends at time x you can be able to choose another one that starts at time x. 

#### Example
```
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120

Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
```
""",
        "title": "Job scheduling",
        "level": "Steady",
        "test_cases": [
            [[[1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]], 120],
            [[[1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]], 150],
            [[[1, 1, 1], [2, 3, 4], [5, 6, 4]], 6],
        ],
    },
    61: {
        "markdown": """
### Fewest coins to make change
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing the total amount of money, return the minimum number of coints that you need to make up that amount. 

Return -1 if `amount` cannot be made by any combination of the coins. 

You may assume that you have an infinite number of each kind of coin.

#### Example
```
Input: coins = [1,2,5], amount = 11
Output: 3
How: 11 = 5 + 5 + 1
```
""",
        "title": "Coin change I",
        "level": "Steady",
        "test_cases": [
            [[[1, 2, 5], 11], 3],
            [[[1, 2, 5, 10], 11], 2],
            [[[1], 0], 0],
            [[[1, 2, 5, 10, 20], 11], 2],
            [[[1, 2, 5, 10, 20], 110], 6],
            [[[2, 5], 3], -1],
            [[[1, 2, 5, 10, 20], 63], 5],
            [[[1, 2, 5, 10, 20, 50], 16], 3],
            [[[1, 2, 5, 10, 20, 50], 28], 4],
            [[[1, 2, 5, 10, 20, 50], 77], 4],
        ],
    },
    62: {
        "markdown": """
### Min cost tickets
Given an array `days` representing planned annual train travalling days and `costs` where costs = [daily, weekly, monthly] indicating the daily (1 day), weekly (7 days) and monthly (30 days) ticket costs respectively, return the minimum cost for travelling every day in the given list of days. 

Each day is an integer between 1 and 365.

#### Example
```
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
```
""",
        "title": "Min cost tickets",
        "level": "Steady",
        "test_cases": [
            [[[1, 4, 6, 7, 8, 20], [2, 7, 15]], 11],
            [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]], 17],
            [[[1, 2, 3, 4, 5, 6, 7], [2, 7, 15]], 7],
            [[[i for i in range(1, 31)], [2, 7, 15]], 15],
            [[[1, 4, 6], [2, 7, 15]], 6],
            [[[5, 6, 7, 8, 9, 10, 11], [2, 7, 15]], 7],
            [[[5, 6, 7, 8, 9, 10, 11, 210, 211, 212, 213, 365], [2, 7, 15]], 16],
            [[[i for i in range(1, 366)], [2, 7, 15]], 190],
        ],
    },
    63: {
        "markdown": """
### Max loot binary tree
Given the `root` of a binary tree where each node represents the amount of cash stashed in a boat, return the maximum amount that you can steal from the boats given that you cannot steal from any directly connected boats i.e parent node and child node. 

#### Example
```
Input: root = [3,2,3,null,3,null,1]
Output: 7
How: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
```
""",
        "test_cases": f"""
{binary_tree}
root1 = array_to_tree([6, 3, 9, None, 5, 4, 9])
root2 = array_to_tree([3,2,3,None,3,None,1])
root3 = array_to_tree([3,4,5,1,3,None,1])
test_cases = [
    [[root1], 24],
    [[root2], 7],
    [[root3], 9],
]
""",
        "title": "Max loot binary tree",
        "level": "Steady",
    },
    64: {
        "markdown": """
### Lowest common ancestor 
Given the `root` of a binary tree and two nodes `p` and `q`, find the lowest common ancestor (LCA) of p and q.

> According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in a tree that has both p and q as descendants (where a node can be a descendant of itself).”

#### Example
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
```
""",
        "test_cases": f"""
{binary_tree}
root1 = array_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
root2 = array_to_tree([1, 2])
test_cases = [
    [[root1, 5, 1], 3],
    [[root1, 5, 4], 5],
    [[root2, 1, 2], 1],
]
""",
        "title": "Lowest common ancestor",
        "level": "Steady",
    },
    65: {
        "markdown": """
### Same binary tree 
Check if two binary trees `p` and `q` are the same given their roots. 

> Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

#### Example
```
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([6, 3, 9, None, 5, 4, 9])
t2 = array_to_tree([6, 3, 9, None, 5, 4, 9])
t3 = array_to_tree([6, 3, 9, 6, 5, 4, 9])
t4 = array_to_tree([])
t5 = array_to_tree([])
t6 = array_to_tree([1, 2])
t7 = array_to_tree([1, None, 2])
test_cases = [
    [[t1, t2], True],
    [[t2, t3], False],
    [[t4, t5], True],
    [[t6, t7], False],
]
""",
        "title": "Same binary tree",
        "level": "Breezy",
    },
    66: {
        "markdown": """
### Boolean tree 
Given the `root` of a full binary tree with the following properties:
- Leaf nodes have either the value 0 or 1, where 0 represents false and 1 represents true. 
- Non leaf nodes have either the value 2 or 3, with 2 representing boolean **OR** and 3 representing boolean **AND**. 

Evalulate each node as follows:
- If leaf node, the evaluation is the value of the node, i.e true or false. 
- if non leaf node, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations. 

Return the boolean result of evaluating the root node.

> A full binary tree is a binary tree where each node has either 0 or 2 children.

> A leaf node is a node that has no children.

#### Example
```
Input: root = [2,1,3,null,null,0,1]
Output: true

Input: root = [0]
Output: false
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([2, 1, 3, None, None, 0, 1])
t2 = array_to_tree([0])
test_cases = [
    [[t1], True],
    [[t2], False],
]
""",
        "title": "Boolean binary tree",
        "level": "Breezy",
    },
    67: {
        "markdown": """
### Binary tree cousins
Given the `root` of a binary tree with unique values and the value of two different nodes in the tree `x` and `y`, check whether x and y are cousins. 

> Two nodes of a binary tree are cousins if they have the same depth with different parents.

#### Example
```
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
```
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([1, 2, 3, None, 4, None, 5])
t2 = array_to_tree([1, 2, 3, None, 4])
t3 = array_to_tree([1, 2, 3, 4])
test_cases = [
    [[t1, 5, 4], True],
    [[t2, 2, 3], False],
    [[t3, 4, 3], False],
]
""",
        "title": "Binary tree cousins",
        "level": "Steady",
    },
    68: {
        "markdown": """
### Merge intervals
Given an array of `intervals` merge all overlapping intervals. 

#### Example
```
input: [[1,3],[2,6],[8,10],[15,18]]
output: [[1,6],[8,10],[15,18]]

input: [[1, 5], [5, 10]]
output: [[1, 10]]

input: [[3, 11], [2, 6]]
output: [[2, 11]]
```
""",
        "title": "Merge intervals",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[[[1,3],[2,6],[8,10],[15,18]]], [[1,6],[8,10],[15,18]]],
    [[[[1, 5], [5, 10]]], [[1, 10]]],
    [[[[3, 11], [2, 6]]], [[2, 11]]],
],
""",
    },
    69: {
        "markdown": """
### Triplet sum equals zero
Given an array `nums` of integers, find all unique triplets that sum to zero. 

#### Example
```
input: [-1,0,1,2,-1,-4]
output: [[-1,-1,2],[-1,0,1]]

input:  [0,1,1]
output: []

input: [0,0,0]
output: [[0,0,0]]
```
""",
        "title": "Triplets sum equals zero",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[[-1,0,1,2,-1,-4]], [[-1,-1,2],[-1,0,1]]
],
    [[[0,1,1]], []],
    [[[0,0,0]], [[0,0,0]]],
],
""",
    },
    70: {
        "markdown": """
### longest increasing subsequence
Given an array `nums` of integers return the length of the longest strictly increasing subsequence

#### Example
```
input: [10,9,2,5,3,7,101,18]
output: 4
How: LIS is [2, 3, 7, 101] with length 4. 

input: [0,1,0,3,2,3]
output: 4

input: [6,6,6,6,6,6,6,6]
output: 1
```
""",
        "title": "Longest increasing subsequence",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[[0,1,0,3,2,3]], 4],
    [[[6,6,6,6,6,6,6,6]], 1],
    [[[10,9,2,5,3,7,101,18]], 4],
],
""",
    },
    71: {
        "markdown": """
### Count bits
Given a positive integer `n` return the number of 1-bits in the binary representation of each number `i` in `[0,n]`

#### Example
```
input: 2
output: [0,1,1]
How: 0 -> 0, 1 -> 1, 2 -> 10 

input: 5
output: [0,1,1,2,1,2]
How: 0, 1, 10, 11, 100, 101
```
""",
        "title": "Count bits",
        "level": "Breezy",
        "test_cases": """
test_cases = [
    [[2], [0,1,1]],
    [[5], [0,1,1,2,1,2]],
],
""",
    },
    72: {
        "markdown": """
### Trapping rain water
Given `n` positive integers representing elevation heights where the width of each bar is 1, return how much water can be trapped after rain. 

#### Example
```
input: [0,1,0,2,1,0,1,3,2,1,2,1]
output: 6

input: [4,2,0,3,2,5]
output: 9
```
""",
        "title": "Trapping rain water",
        "level": "Edgy",
        "test_cases": """
test_cases = [
    [[[0,1,0,2,1,0,1,3,2,1,2,1]], 6],
    [[[4,2,0,3,2,5]], 9],
],
""",
    },
    73: {
        "markdown": """
### Longest palidromic substring
Given a string `s`, return the longest palindromic substring in s. 

Return the first one if there are multiple longest palindromic substrings. 

#### Example
```
input: "babad"
output: "bab" 

input: "abcde"
output: "a"
```
""",
        "title": "Longest palindromic substring",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [["babad"], "bab"],
    [["abcde"], "a"],
],
""",
    },
    74: {
        "markdown": """
### Median of two sorted arrays
Given two sorted arrays `nums1` and `nums2`of sizes n and m respectively, return the median of the two sorted arrrays. 

You must write an algorithm that runs in **O(log(min(n, m)))**

#### Example
```
input: nums1 = [1, 5], nums2 = [3]
output: 3

input: nums1 = [3, 4], nums2 = [4, 5]
output: 4
```
""",
        "title": "Median of two sorted arrays",
        "level": "Edgy",
        "test_cases": """
test_cases = [
    [[[1,5], [3]], 3],
    [[[3, 4], [4, 5]], 4],
],
""",
    },
    75: {
        "markdown": """
### Most frequent elements
Return the `k` most frequent element in a given array. 

#### Example
```
input: nums = [1,1,1,2,2,3], k = 2
output: [1, 2]

input: nums = [1], k = 1 
output: [1]

input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
output: [1,2]
```
""",
        "title": "Most frequent elements",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[[1,1,1,2,2,3], 2], [1,2]],
    [[[1,2,1,2,1,2,3,1,3,2], 2], [1,2]],
    [[[1], 1], [1]],
],
""",
    },
    76: {
        "markdown": """
### Connected cities
Given an `n * n` adjacency matrix of connected cities with each cell having values 1 or 0 where 0 indicate city i is not connected to city j and 1 indicate otherwise. 

Return the number of connected groups of cities.  

#### Example
```
input: [[1,1,0],[1,1,0],[0,0,1]]
output: 2

input: [[1,0,0],[0,1,0],[0,0,1]]
output: 3
```
""",
        "title": "Connected cities",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[[[1,1,0],[1,1,0],[0,0,1]]], 2],
    [[[[1,0,0],[0,1,0],[0,0,1]]], 3],
],
""",
    },
    77: {
        "markdown": """
### Conway's game of life
Return the next state of Conway's game of life given an `m * n` board where each cell represents one of two states - 0 for dead and 1 for alive. 

Each cell interacts with its horizontal, vertical and diagonal neighbors subject to the following rules:
- Birth - Any dead cell with exactly 3 live neighbors becomes alive. 
- Life - Any live cell with 2 or 3 live neighbors lives on. 
- Death - Any live cell with fewer than 2 live neighbors or more than 3 live neighbors dies. 
#### Example
```
input: [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

input: [[1,1],[1,0]]
output: [[1,1],[1,1]]
```
""",
        "title": "Conway's game of life",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]], [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
],
    [[[[1,1],[1,0]]], [[1,1],[1,1]]],
],
""",
    },
    78: {
        "markdown": """
### Min CPU intervals
Given an array of CPU `tasks` and a positive integer representing the cooldown interval between two tasks with the same label, return the minimum number of cpu intervals required to complete all tasks. 

#### Example
```
input: tasks = ["A","A","A","B","B","B"], n = 2
output: 8
How: A -> B -> idle -> A -> B -> idle -> A -> B.

input: tasks = ["A","C","A","B","D","B"], n = 1
output: 6

input: tasks = ["A","A","A", "B","B","B"], n = 3
output: 10
```
""",
        "title": "Min CPU intervals",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[["A","A","A","B","B","B"], 2], 8],
    [[["A","C","A","B","D","B"], 1], 6],
    [[["A","A","A", "B","B","B"], 3], 10],
],
""",
    },
    79: {
        "markdown": """
### Product of array except self
Given an array `nums`, return a new array where each element is the product of all elements except itself - **without using division**. 

You must write an algorithm with **O(n)** average time complexity. 

#### Example
```
input: [1, 2, 3, 4]
output: [24, 12, 8, 6]

input: [-1, 1, 0, -3, -3]
output: [0, 0, 9, 0, 0]
```
""",
        "title": "Product of array except self",
        "level": "Steady",
        "test_cases": """
test_cases = [
    [[[1, 2, 3, 4]], [24, 12, 8, 6]],
    [[[-1, 1, 0, -3, -3]], [0, 0, 9, 0, 0]],
],
""",
    },
}
