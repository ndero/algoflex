linked_list = {}
binary_tree = {}
arr = {
    10: {
        "markdown": """
### Permutations
Given an array nums of distinct integers, return all the possible permutations.
You can return the permutations in any order.

Can you do it without python's itertools?

### Example
```
input: [1, 2]
output: [[1, 2], [2, 1]]
```
""",
        "test_cases": """
test_cases = [
    [[[1, 2]], [[1, 2], [2, 1]]],
    [
        [[i for i in range(1, 5)]],
        [
            [1, 2, 3, 4],
            [1, 2, 4, 3],
            [1, 3, 2, 4],
            [1, 3, 4, 2],
            [1, 4, 2, 3],
            [1, 4, 3, 2],
            [2, 1, 3, 4],
            [2, 1, 4, 3],
            [2, 3, 1, 4],
            [2, 3, 4, 1],
            [2, 4, 1, 3],
            [2, 4, 3, 1],
            [3, 1, 2, 4],
            [3, 1, 4, 2],
            [3, 2, 1, 4],
            [3, 2, 4, 1],
            [3, 4, 1, 2],
            [3, 4, 2, 1],
            [4, 1, 2, 3],
            [4, 1, 3, 2],
            [4, 2, 1, 3],
            [4, 2, 3, 1],
            [4, 3, 1, 2],
            [4, 3, 2, 1],
        ],
    ],
    [[[1]], [[1]]],
]
""",
        "title": "Permutations",
        "level": "Steady",
    },
    11: {
        "markdown": """
### Combinations
Given a string and a positive integer k, return all possible combinations of characters of size k.
You can return the combinations in any order.

Are your hands tied without python's itertools 😅?

### Example
```
input:
    string: "abcd",
    k: 3
output: 'abc', 'abd', 'acd', 'bcd'
```
""",
        "test_cases": """
test_cases = [
    [["abcd", 3], ["abc", "abd", "acd", "bcd"]],
    [
        ["combinations", 2],
        [
            "co",
            "cm",
            "cb",
            "ci",
            "cn",
            "ca",
            "ct",
            "ci",
            "co",
            "cn",
            "cs",
            "om",
            "ob",
            "oi",
            "on",
            "oa",
            "ot",
            "oi",
            "oo",
            "on",
            "os",
            "mb",
            "mi",
            "mn",
            "ma",
            "mt",
            "mi",
            "mo",
            "mn",
            "ms",
            "bi",
            "bn",
            "ba",
            "bt",
            "bi",
            "bo",
            "bn",
            "bs",
            "in",
            "ia",
            "it",
            "ii",
            "io",
            "in",
            "is",
            "na",
            "nt",
            "ni",
            "no",
            "nn",
            "ns",
            "at",
            "ai",
            "ao",
            "an",
            "as",
            "ti",
            "to",
            "tn",
            "ts",
            "io",
            "in",
            "is",
            "on",
            "os",
            "ns",
        ],
    ],
    [["rat", 3], ["rat"]],
    [["rat", 1], ["r", "a", "t"]],
    [["rat", 0], []],
]
""",
        "title": "Combinations",
        "level": "Steady",
    },
    76: {
        "markdown": """
### Calendar book event
> Leetcode 
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking. A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

> MyCalendar() Initializes the calendar object.
> boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

### Example
```python
calendar = MyCalendar()
calendar.book(10, 20)  # True
calendar.book(10, 20)  # False - already booked
calendar.book(15, 25)  # False - overlapping with [10, 20)
calendar.book(20, 30)  # True  
```
""",
        "test_cases": f"""
calendar = MyCalendar()
test_cases = [
    [[calendar.book(10, 20)], True],
    [[calendar.book(10, 20)], False],
    [[calendar.book(15, 25)], False],
    [[calendar.book(20, 30)], True],
    [[calendar.book(30, 31)], True],
    [[calendar.book(100, 2000)], True],
    [[calendar.book(2_000, 6_000_000)], True],
    [[calendar.book(3_000, 50_000)], False],
    [[calendar.book(10_000, 20_000)], False],
    [[calendar.book(0, 6_000_000)], False],
    [[calendar.book(55_556, 3_000_000)], False],
    [[calendar.book(2000, 2020)], False],
    [[calendar.book(5_999_999, 6_000_001)], False],
    [[calendar.book(100_000, 200_000)], False],
    [[calendar.book(31, 41)], True],
    [[calendar.book(42, 50)], True],
    [[calendar.book(50, 60)], True],
    [[calendar.book(60, 70)], True],
    [[calendar.book(70, 80)], True],
    [[calendar.book(80, 90)], True],
    [[calendar.book(90, 100)], True],
]
""",
        "title": "Calendar book event",
        "level": "Steady",
    },
    77: {
        "markdown": """
### Range frequency query 
> Leetcode 
Design a data structure to find the frequency of a given value in a given subarray. The frequency of a value in a subarray is the number of occurrences of that value in the subarray. Implement the RangeFreqQuery class
```
# Constructs an instance of the classwith the given 0-indexed integer array arr. 
RangeFreqQuery(int[] arr)      
# Returns the frequency of value in the subarray arr[left...right]. 
int query(int left, int right, int value)  
```
A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).

### Example
```
arr = [1, 3, 7, 7, 7, 3, 4, 1, 7]
rf = RangeFreq(arr)

input: 
  left = 2, right = 5, value = 7
  rf.query(2, 5, 7) 
output:
  3
explanation:
  7 appears 3 times between indices 1 and 6


rf.query(2, 4, 7)  # 3
rf.query(0, 8, 1)  # 2
rf.query(4, 7, 4)  # 1
```
""",
        "test_cases": f"""
arr = [1, 3, 7, 7, 7, 3, 4, 1, 7]
rf1 = RangeFreq(arr)
arr2 = [i for i in range(100_000)]
rf2 = RangeFreq(arr2)
arr3 = [i for i in range(1, 100_000)] + [22] * 50_000 + [-15] * 100_000
rf3 = RangeFreq(arr3)
test_cases = [
    [[rf1.query(2, 4, 7)], 3],
    [[rf1.query(0, 8, 1)], 2],
    [[rf1.query(4, 7, 4)], 1],
    [[rf1.query(2, 4, 9)], 0],
    [[rf1.query(8, 8, 7)], 1],
    [[rf2.query(0, 100_000, 897)], 1],
    [[rf2.query(0, 100_000, 0)], 1],
    [[rf2.query(0, 100_000, 99_999)], 1],
    [[rf2.query(0, 10, 7)], 1],
    [[rf2.query(50_000, 50_000, 50_000)], 1],
    [[rf3.query(0, 250_000, 0)], 1],
    [[rf3.query(0, 250_000, 22)], 50_001],
    [[rf3.query(0, 250_000, -5)], 100_000],
    [[rf3.query(100_000, 150_000, 22)], 50_000],
    [[rf3.query(100_000, 150_005, -15)], 5],
]
""",
        "title": "Range frequency query",
        "level": "Steady",
    },
    70: {
        "markdown": """
### Sum linked lists
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example
```
input:
  l1 = [2, 4, 3]
  l2 = [5, 6, 4]
output: [7, 0, 8]
explanation: 342 + 465 = 807
```
""",
        "test_cases": f"""
{linked_list}
l1 = array_to_list([2, 4, 3])
l2 = array_to_list([5, 6, 4])
l3 = array_to_list([9, 9, 9, 9, 9, 9, 9])
l4 = array_to_list([9, 9, 9, 9])
l12 = array_to_list([7, 0, 8])
l34 = array_to_list([8, 9, 9, 9, 0, 0, 0, 1])
test_cases = [
    [[l1, l2], l12],
    [[l3, l4], l34],
]
""",
        "title": "Sum linked lists",
        "level": "Steady",
    },
    74: {
        "markdown": """
### Invert binary tree
> Leetcode #226

Given the root of a binary tree, invert the
tree, and return its root.

### Examples
Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
""",
        "test_cases": f"""
{binary_tree}
t1 = array_to_tree([4, 2, 7, 1, 3, 6, 9])
t2 = array_to_tree([4, 7, 2, 9, 6, 3, 1])
test_cases = [
    [[t1], t2],
]
""",
        "title": "Invert binary tree",
        "level": "Steady",
    },
    75: {
        "markdown": """
### Reverse a linked list
Given the head of a linked list, reverse the list, and return its head

### Example
```
input: [1, 2, 3, 4, 5, 6]
output: [6, 5, 4, 3, 2, 1]
```
""",
        "test_cases": f"""
{linked_list}
l1 = array_to_list([1, 2, 3, 4, 5, 6])
l2 = array_to_list([6, 5, 4, 3, 2, 1])
test_cases = [
    [[l1], l2],
]
""",
        "title": "Reverse linked list",
        "level": "Steady",
    },
    30: {
        "markdown": """
### Merge two sorted linked lists
Given two sorted linked lists, head1 and head2. Merge them into one sorted linked list.

### Example
```
input:
  l1 = [2, 4, 6, 6, 12, 22]
  l2 = [3, 7, 8, 9]
output: [2, 3, 4, 6, 6, 7, 8, 9, 12, 22]
```
""",
        "test_cases": f"""
{linked_list}
l1 = array_to_list([2, 4, 6, 6, 12, 22])
l2 = array_to_list([3, 7, 8, 9])
l3 = array_to_list([2, 3, 4, 6, 6, 7, 8, 9, 12, 22])
test_cases = [
    [[l1, l2], l3],
]
""",
        "title": "Merge sorted linked lists",
        "level": "Steady",
    },
}
