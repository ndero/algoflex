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


root1 = array_to_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
root2 = array_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
root4 = array_to_tree([])
root5 = array_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1])

# BSTs
root6 = array_to_tree([100, 50, 600, 45, 55, 500, 1000])
root7 = sorted_to_bst([i for i in range(100)])
root8 = sorted_to_bst([i for i in range(-100_000, 100_000)])

# Edge cases
root9 = array_to_tree([5])
root10 = array_to_tree([-2, -3, None, -4])
root11 = array_to_tree([0, 0, 0])

test_cases = [
    [(root1, 18), True],
    [(root2, 17), True],
    [(root2, 26), False],
    [(root2, 22), True],
    [(root2, 27), True],
    [(root4, 0), False],
    [(root5, 26), True],
    [(root6, 1000), False],
    [(root6, 205), True],
    [(root7, 577), True],
    [(root7, 411), False],
    [(root8, -99996), True],
    # Edge cases
    [(root9, 5), True],
    [(root9, 0), False],
    [(root10, -9), True],
    [(root10, -2), False],
    [(root11, 0), True],
    [(root11, 1), False],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(has_path_sum, test_cases))  # type: ignore  # noqa: F821
