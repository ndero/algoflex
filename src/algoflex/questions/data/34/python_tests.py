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


root1 = array_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1])
root2 = array_to_tree([9, 8, 16])
root3 = array_to_tree([100, 50, 600, 45, 55, 500, 1000])
root4 = sorted_to_bst([i for i in range(10_000)])
root5 = array_to_tree([5])
root6 = array_to_tree([5, 3, 7])
root7 = array_to_tree([5, 3, 7, 1, None, None, 9])

test_cases = [
    [(root1, 11, 13), True],
    [(root1, 7, 4), False],
    [(root2, 9, 16), False],
    [(root3, 55, 500), True],
    [(root4, 4, 13), False],
    [(root4, 3, 9999), True],
    # Edge cases
    [(root5, 5, 5), False],  # x and y are required to be different
    [(root6, 3, 7), False],
    [(root6, 5, 3), False],
    [(root7, 1, 9), True],
    [(root7, 3, 1), False],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(are_cousins, test_cases))  # type: ignore  # noqa: F821
