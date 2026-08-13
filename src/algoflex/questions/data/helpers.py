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
