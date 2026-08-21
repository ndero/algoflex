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


root1 = array_to_tree([6, 3, 9, None, 5, 4, 9])
root2 = array_to_tree([6, 3, 9, None, 5, 4, 9])
root3 = sorted_to_bst([i for i in range(10_000)])
root4 = sorted_to_bst([i for i in range(10_000)])
root5 = array_to_tree([])
root6 = array_to_tree([])
root7 = array_to_tree([1, 2])
root8 = array_to_tree([1, None, 2])
root9 = array_to_tree([1, 2, 3, 4, 5, None, 6])
root10 = array_to_tree([1, 2, 3, 4, 5, 7, 6])
root11 = array_to_tree([5])
root12 = array_to_tree([5])

test_cases = [
    [(root1, root2), True],
    [(root3, root4), True],
    [(root2, root3), False],
    [(root5, root6), True],
    [(root4, root6), False],
    [(root7, root8), False],
    [(root8, root8), True],
    [(root9, root10), False],
    [(root11, root12), True],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(same_binary_tree, test_cases))  # type: ignore  # noqa: F821
