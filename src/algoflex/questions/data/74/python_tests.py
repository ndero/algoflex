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
    (([1, 2, 3, 4, 5, 6],), [6, 5, 4, 3, 2, 1]),
    ((list(range(100_000)),), list(range(99_999, -1, -1))),
    (([3] * 100_000,), [3] * 100_000),
    (([],), []),
    (([6] + [0] * 99_999 + [9],), [9] + [0] * 99_999 + [6]),
    ((list(range(-100_000, 0)),), list(range(-1, -100_001, -1))),
]


if __name__ == "__main__":
    sys.exit(
        run_python_tests(  # noqa: F821 # type: ignore
            lambda arr: list_to_array(reverse_list(array_to_list(arr))),  # noqa: F821 # type: ignore
            test_cases,
        )
    )
