### Add Two Numbers as linked lists

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number `0` itself.

**Example 1**

* **Input:** `head1 = [1, 2, 3]`, `head2 = [4, 5, 6]`
* **Output:** `[5, 7, 9]`
* **How:** 321 + 654 = 975

**Example 2**

* **Input:** `head1 = [0]`, `head2 = [0]`
* **Output:** `[0]`
* **How:** 0 + 0 = 0

**Example 3**

* **Input:** `head1 = [9, 4]`, `head2 = [1, 5]`
* **Output:** `[0, 0, 1]`
* **How:** 49 + 51 = 100

**Constraints**

* The number of nodes in each linked list is in the range `[1, 100]`.
* `0 <= Node.val <= 9`
* It is guaranteed that the list represents a number that does not have leading zeros, except for the number 0 itself.
