import sys


def array_to_list(arr):
    dummy = ListNode()  # type: ignore # noqa: F821
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)  # type: ignore # noqa: F821
        curr = curr.next
    return dummy.next


def list_to_array(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


test_cases = [
    # Basic merging
    [([2, 4, 6, 6, 12, 22], [3, 7, 8, 9]), [2, 3, 4, 6, 6, 7, 8, 9, 12, 22]],
    # Both empty
    [([], []), []],
    # One empty, one non-empty
    [([], [0]), [0]],
    [([1, 2, 3], []), [1, 2, 3]],
    # Single element each, equal values
    [([2], [2]), [2, 2]],
    [([1], [2]), [1, 2]],
    [([5], [3]), [3, 5]],
    # Large range merging
    [(list(range(60_000)), list(range(-100, 0))), list(range(-100, 60_000))],
    # Many duplicates
    [([1] * 1_000, [2] * 2_000), [1] * 1_000 + [2] * 2_000],
    [([0] * 500, [0] * 500), [0] * 1000],
    # Negative numbers and mixed
    [([-5, -3, 1, 4], [-4, -1, 0, 2]), [-5, -4, -3, -1, 0, 1, 2, 4]],
    # Alternating values
    [([1, 3, 5, 7], [2, 4, 6, 8]), [1, 2, 3, 4, 5, 6, 7, 8]],
    [([1, 4, 7], [2, 5, 8]), [1, 2, 4, 5, 7, 8]],
    # Uneven lengths
    [([1, 2, 3, 4, 5], [6]), [1, 2, 3, 4, 5, 6]],
    [([10, 20], [1, 2, 3, 30]), [1, 2, 3, 10, 20, 30]],
    # Large lists with overlap
    [(list(range(0, 100, 2)), list(range(1, 100, 2))), list(range(100))],
    # Duplicate values interleaved
    [([1, 1, 2, 3], [1, 2, 2, 3]), [1, 1, 1, 2, 2, 2, 3, 3]],
    # Very large lists (10^5 each) to test performance
    [(list(range(0, 100_000, 2)), list(range(1, 100_000, 2))), list(range(100_000))],
    # Mixed positive and negative large
    [(list(range(-50_000, 0)), list(range(50_000))), list(range(-50_000, 50_000))],
    # Single elements repeated
    [([5] * 10_000, [5] * 10_000), [5] * 20_000],
]


if __name__ == "__main__":
    sys.exit(
        run_python_tests(  # type: ignore # noqa: F821
            lambda l1, l2: list_to_array(
                merge_list(array_to_list(l1), array_to_list(l2))  # type: ignore # noqa: F821
            ),
            test_cases,
        )
    )
