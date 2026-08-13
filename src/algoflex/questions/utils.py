def format_arg(value, max_length=80, max_items=10):
    if isinstance(value, str):
        if len(value) > max_length:
            return repr(value[:max_length]) + "..."
        return repr(value)

    if isinstance(value, (list, tuple, set)):
        if len(value) > max_items:
            items = ", ".join(
                format_arg(item, max_length, max_items) for item in list(value)[:3]
            )
            return f"[{items}, ... ({len(value)} items)]"

        return repr(value)

    return repr(value)


def format_result(value, max_length=100, max_items=10):
    if isinstance(value, str):
        if len(value) > max_length:
            return repr(value[:max_length]) + "..."
        return repr(value)

    if isinstance(value, (list, tuple, set)):
        if len(value) > max_items:
            items = ", ".join(
                format_result(item, max_length, max_items) for item in list(value)[:3]
            )
            return f"[{items}, ... ({len(value)} items)]"

        return repr(value)

    if isinstance(value, dict):
        if len(value) > max_items:
            items = ", ".join(
                f"{format_result(k)}: {format_result(v)}"
                for k, v in list(value.items())[:3]
            )
            return f"{{{items}, ... ({len(value)} items)}}"

        return repr(value)

    return repr(value)


def run_python_tests(func, test_cases) -> int:
    for i, [args, expected] in enumerate(test_cases):
        try:
            result = func(*args)
            if result == expected:
                print(f"[green][b]✓[/][/] test case {i + 1} \tPASS")
            else:
                parameters = ", ".join(format_arg(arg) for arg in args)
                print(
                    f"[red][b]x[/][/] test case {i + 1} \tFAIL\n"
                    f"\t[b]args[/]: {parameters}\n"
                    f"\t[b]got[/]: [red]{format_result(result)}[/]\n"
                    f"\t[b]expected[/]: [green]{format_result(expected)}[/]"
                )
                return 1
        except Exception as e:  # noqa: BLE001
            print(
                f"[red][b]x[/][/] test case {i + 1} \tERROR\n\t[b][red]error[/][/]: {e}"
            )
            return 1
    print(f"\n{len(test_cases)} passed!")
    return 0


# tree helpers
class TreeNode:
    __slots__ = ("left", "right", "val")

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_tree(arr, index=0):
    if index >= len(arr) or arr[index] is None:
        return None
    root = TreeNode(arr[index])
    root.left = array_to_tree(arr, index * 2 + 1)
    root.right = array_to_tree(arr, index * 2 + 2)
    return root


def tree_to_array(root):
    # BFS
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            queue.append(node.left)
            queue.append(node.right)
            result.append(node.val)
        else:
            result.append(None)
    return result


def sorted_to_bst(nums):  # returns balanced bst from a sorted list
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_to_bst(nums[:mid])
    root.right = sorted_to_bst(nums[mid + 1 :])
    return root


def same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)


# linked list helpers
class ListNode:
    __slots__ = ("next", "val")

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# prefer iterative to recursive for all these helpers
# - recursive hit depth limit real fast
def array_to_list(arr):
    dummy = ListNode()
    curr = dummy

    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next


def list_to_array(head):
    result = []
    curr = head

    while curr:
        result.append(curr.val)
        curr = curr.next

    return result


def same_list(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

    return head1 is None and head2 is None
