from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def construct_binary_tree(arr: List) -> Optional[TreeNode]:
    def construct(i, node):
        if (i << 1) + 1 < len(arr):
            if arr[(i << 1) + 1] is not None:
                node.left = TreeNode(arr[(i << 1) + 1])
                construct((i << 1) + 1, node.left)
            if (i << 1) + 2 < len(arr) and arr[(i << 1) + 2] is not None:
                node.right = TreeNode(arr[(i << 1) + 2])
                construct((i << 1) + 2, node.right)

    if not arr:
        return None

    root = TreeNode(arr[0])
    construct(0, root)

    return root


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        vals = []
        node = self.next
        while node is not None:
            vals.append(str(", " + repr(node.val)))
            node = node.next
        return "[" + str(self.val) + "".join(vals) + "]"


def construct_linked_list(arr: List) -> Optional[ListNode]:
    if not arr:
        return None

    head = ListNode(arr[0])
    node = head
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    return head


if __name__ == "__main__":
    root = construct_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])