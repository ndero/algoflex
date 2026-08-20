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


root1 = array_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
root2 = array_to_tree([5])
root3 = array_to_tree([12, 8, 16, 4, 9, 13, 18, 1])
root4 = array_to_tree(
    [9, 8, 16, None, None, None, 18, None, None, None, None, None, None, 19]
)
root5 = array_to_tree(
    [9, 8, 16, None, None, None, 18, None, None, None, None, None, 15, 19]
)
root6 = array_to_tree([12, 3, 20, None, 5])
root7 = array_to_tree([])
root8 = array_to_tree([100, 50, 600, 45, 55, 500, 1000])
root9 = sorted_to_bst([i for i in range(100)])
root10 = sorted_to_bst([i for i in range(-100_000, 100_000)])
root11 = array_to_tree([5, None, 3])
root12 = array_to_tree([4, None, 9, None, None, None, 12])
root13 = array_to_tree(
    [9, 8, 16, None, None, None, 18, None, None, None, None, None, None, 18]
)


test_cases = [
    [(root1,), 15],
    [(root2,), 0],
    [(root3,), 43],
    [(root4,), 34],
    [(root5,), 34],
    [(root6,), 25],
    [(root7,), 0],
    [(root8,), 1655],
    [(root9,), 1868],
    [(root10,), 539765],
    [(root11,), 3],
    [(root12,), 21],
    [(root13,), 34],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(sum_right_nodes, test_cases))  # type: ignore  # noqa: F821
