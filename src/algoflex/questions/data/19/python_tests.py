import sys


def array_to_tree(arr, index=0):
    if index >= len(arr) or arr[index] is None:
        return None

    root = TreeNode(arr[index])  # pyright: ignore[reportUndefinedVariable] # noqa: F821
    root.left = array_to_tree(arr, index * 2 + 1)
    root.right = array_to_tree(arr, index * 2 + 2)
    return root


root1 = array_to_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
root2 = array_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
root3 = array_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1] * 10_000)
root4 = array_to_tree([])
root5 = array_to_tree([100, 50, 600, 45, 55, 500, 1000])

# Edge cases
root6 = array_to_tree([5])
root7 = array_to_tree([0, 0, 0])
root8 = array_to_tree([-2, -3, None, -4])
root9 = array_to_tree([1, 2, 3, 4, 5, 6, 7])

test_cases = [
    [(root1, 8), 3],
    [(root2, 22), 3],
    [(root2, 20), 1],
    [(root3, 20), 1896],
    [(root3, 22), 2273],
    [(root4, 0), 0],
    [(root5, 195), 1],
    [(root5, 1000), 1],
    [(root5, 40), 0],
    # Edge cases
    [(root6, 5), 1],
    [(root6, 0), 0],
    [(root7, 0), 5],
    [(root8, -5), 1],
    [(root8, -7), 1],
    [(root9, 7), 3],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(count_paths, test_cases))  # type: ignore  # noqa: F821
