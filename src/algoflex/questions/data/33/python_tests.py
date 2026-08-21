import sys


def array_to_tree(arr, index=0):
    if index >= len(arr) or arr[index] is None:
        return None

    root = TreeNode(arr[index])  # type: ignore # noqa: F821
    root.left = array_to_tree(arr, index * 2 + 1)
    root.right = array_to_tree(arr, index * 2 + 2)
    return root


def sorted_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])  # pyright: ignore # noqa: F821
    root.left = sorted_to_bst(nums[:mid])
    root.right = sorted_to_bst(nums[mid + 1 :])
    return root


root1 = array_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
root2 = array_to_tree([1, 2])
root3 = sorted_to_bst([i for i in range(10)])
root4 = array_to_tree([5])
root5 = array_to_tree([5, 3, 7])
root6 = sorted_to_bst([i for i in range(10_000)])

test_cases = [
    [(root1, 8, 6), 3],
    [(root1, 5, 2), 5],
    [(root2, 2, 1), 1],
    [(root3, 1, 3), 2],
    [(root3, 3, 6), 5],
    [(root3, 0, 9), 5],
    [(root6, 3, 6), 4],
    [(root6, 500, 5), 312],
    [(root6, 6700, 9800), 7500],
    [(root6, 1234, 5678), 5000],
    [(root6, 111, 999), 625],
    [(root6, 0, 9999), 5000],
    # Edge cases
    [(root4, 5, 5), 5],
    [(root5, 3, 7), 5],
    [(root5, 5, 7), 5],
    [(root5, 3, 5), 5],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(lowest_common_ancestor, test_cases))  # type: ignore  # noqa: F821
