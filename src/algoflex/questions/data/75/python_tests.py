import sys


def array_to_list(arr):
    dummy = ListNode()  # type: ignore # noqa: F821
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)  # type: ignore # noqa: F821
        curr = curr.next
    return dummy.next


def create_cycle_list(arr, pos):
    if not arr:
        return None

    # Create all nodes
    nodes = [ListNode(val) for val in arr]  # type: ignore # noqa: F821

    # Link them
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create cycle
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0] if nodes else None


# test cases: [ (array, pos), expected ]
test_cases = [
    # Basic test cases - no cycle
    [([], -1), False],  # 1 - Empty list
    [([1], -1), False],  # 2 - Single node, no cycle
    [([1, 2], -1), False],  # 3 - Two nodes, no cycle
    [([1, 2, 3], -1), False],  # 4 - Three nodes, no cycle
    [([1, 2, 3, 4, 5], -1), False],  # 5 - Five nodes, no cycle
    # Basic test cases - with cycle
    [([1], 0), True],  # 6 - Single node pointing to itself
    [([1, 2], 0), True],  # 7 - Two nodes, cycle at head
    [([1, 2], 1), True],  # 8 - Two nodes, cycle at tail
    [([3, 2, 0, -4], 1), True],  # 9 - standard example
    [([1, 2, 3, 4, 5], 2), True],  # 10 - Cycle in middle
    # Edge cases - cycle positions
    [([1, 2, 3, 4, 5], 0), True],  # 11 - Cycle to head
    [([1, 2, 3, 4, 5], 4), True],  # 12 - Cycle to last node (tail to itself)
    [([1, 2, 3, 4, 5], 3), True],  # 13 - Cycle to node before last
    [([1, 2, 3, 4, 5], 1), True],  # 14 - Cycle to second node
    [([1], -1), False],  # 15 - Single node, no cycle (explicit -1)
    # Lists with duplicate values
    [([1, 1, 1, 1, 1], -1), False],  # 16 - Duplicate values, no cycle
    [([1, 1, 1, 1, 1], 2), True],  # 17 - Duplicate values with cycle
    [([1, 2, 2, 3, 3], -1), False],  # 18 - Duplicate values pattern
    [([1, 2, 2, 3, 3], 1), True],  # 19 - Duplicate values with cycle
    # Large lists
    [(list(range(1000)), -1), False],  # 20 - Large list, no cycle
    [(list(range(1000)), 500), True],  # 21 - Large list with cycle in middle
    [(list(range(10000)), 0), True],  # 22 - Very large list, cycle to head
    [(list(range(10000)), 9999), True],  # 23 - Very large list, cycle to last
    # Special patterns
    [([-1, -2, -3, -4], 2), True],  # 24 - Negative values with cycle
    [([0, 0, 0, 0], 1), True],  # 25 - All zeros with cycle
    [([10**6, 10**6, 10**6], 0), True],  # 26 - Large values, cycle at head
    [([1], 0), True],  # 27 - Single node self-cycle
    [([1, 2, 3, 4, 5], -1), False],  # 28 - Explicit no cycle with -1
    # Additional cycle lengths and positions
    [([1, 2, 3, 4], 3), True],  # 29 - Cycle length 1 (self-loop at tail)
    [([1, 2, 3, 4, 5], 3), True],  # 30 - Cycle length 2
    [([1, 2, 3, 4, 5], 1), True],  # 31 - Cycle length n-1
    [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), True],  # 32 - Cycle at head with long tail
    [(list(range(100)), 1), True],  # 33 - Cycle at position 1 with many nodes
    [([1, -1, 2, -2, 3, -3], 2), True],  # 34 - Alternating values with cycle
    # Extremely long lists
    [(list(range(100000)), -1), False],  # 35 - 10^5 nodes, no cycle
    [(list(range(100000)), 0), True],  # 36 - 10^5 nodes, cycle at beginning
    [(list(range(100000)), 50000), True],  # 37 - 10^5 nodes, cycle at middle
    [(list(range(100000)), 99999), True],  # 38 - 10^5 nodes, cycle at end
    # Maximum values
    [([10**4] * 10**4, 5000), True],  # 39 - 10^4 nodes with value 10^4
]


if __name__ == "__main__":
    sys.exit(
        run_python_tests(  # noqa: F821 # type: ignore
            lambda arr, pos: has_cycle(create_cycle_list(arr, pos)),  # noqa: F821 # type: ignore
            test_cases,
        )
    )
