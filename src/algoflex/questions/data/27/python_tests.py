import sys


def array_to_tree(arr, index=0):
    if index >= len(arr) or arr[index] is None:
        return None

    root = TreeNode(arr[index])  # pyright: ignore[reportUndefinedVariable] # noqa: F821
    root.left = array_to_tree(arr, index * 2 + 1)
    root.right = array_to_tree(arr, index * 2 + 2)
    return root


def sorted_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])  # pyright: ignore[reportUndefinedVariable] # noqa: F821
    root.left = sorted_to_bst(nums[:mid])
    root.right = sorted_to_bst(nums[mid + 1 :])
    return root


root1 = array_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
root2 = array_to_tree([5])
root3 = array_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1])
root4 = array_to_tree([9, 8, 16])
root5 = array_to_tree(
    [9, 8, 16, None, None, None, 6, None, None, None, None, None, None, 7]
)
root6 = array_to_tree([12, 3, 20, None, 5])
root7 = array_to_tree([])
root8 = array_to_tree([100, 50, 600, 45, 55, 500, 1000])
root9 = sorted_to_bst([i for i in range(100)])
root10 = sorted_to_bst([i for i in range(-100_000, 100_000)])
root11 = array_to_tree([5, 3])
root12 = array_to_tree([4, None, 9, None, None, None, 12])

test_cases = [
    [(root1,), False],
    [(root2,), True],
    [(root3,), False],
    [(root4,), True],
    [(root5,), False],
    [(root6,), True],
    [(root7,), True],
    [(root8,), True],
    [(root9,), True],
    [(root10,), True],
    [(root11,), True],
    [(root12,), False],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(is_balanced, test_cases))  # type: ignore  # noqa: F821
