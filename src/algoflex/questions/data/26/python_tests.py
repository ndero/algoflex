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


root1 = array_to_tree([9, 8, 16])
root2 = array_to_tree([9, 8, 16, 4])
root3 = array_to_tree([12, 3, 20, None, 5])
root5 = array_to_tree([])
root6 = array_to_tree([100, 50, 600, 45, 55, 500, 1000])
root7 = sorted_to_bst([i for i in range(100)])
root8 = sorted_to_bst([i for i in range(-100_000, 100_000)])

# Edge cases
root9 = array_to_tree([5])

test_cases = [
    [(root1,), 8],
    [(root2,), 4],
    [(root3,), 3],
    [(root6,), 45],
    [(root7,), 0],
    [(root8,), -100_000],
    # Edge cases
    [(array_to_tree([5]),), 5],
    [(array_to_tree([5, 3]),), 3],
    [(array_to_tree([5, None, 8]),), 5],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(bst_min, test_cases))  # type: ignore  # noqa: F821
