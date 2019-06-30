from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __iter__(self):
        arr = flatten_binary_tree(self)
        for val in arr:
            yield val

    def __repr__(self) -> str:
        return str(flatten_binary_tree(self))


def construct_binary_tree(arr: List) -> Optional[TreeNode]:
    def construct(i, node):
        nonlocal arr
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


def flatten_binary_tree(root: TreeNode) -> Optional[list]:
    arr = {}

    def flatten(i, node):
        nonlocal arr
        if node is None:
            arr[i] = None
        else:
            arr[i] = node.val
            flatten((i << 1) + 1, node.left)
            flatten((i << 1) + 2, node.right)

    flatten(0, root)
    arr = [v for k, v in sorted(arr.items())]
    i = len(arr) - 1
    while i >= 0 and arr[i] is None:
        i -= 1
    return arr[:i + 1]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __iter__(self):
        current = self
        while current is not None:
            yield current.val
            current = current.next

    def __repr__(self) -> str:
        return str(list(self))


def construct_linked_list(arr: List) -> Optional[ListNode]:
    if not arr:
        return None

    head = ListNode(arr[0])
    node = head
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    return head


def matrix_to_string(matrix: List[List]) -> str:
    if not isinstance(matrix, List) or len(matrix) == 0 or not isinstance(matrix[0], List):
        raise TypeError

    lengths = [len(str(item)) for row in matrix for item in row]
    item_spacing = 0 if len(lengths) == 0 else max(lengths)
    del lengths

    str_arr = []
    for i in range(len(matrix)):
        str_arr.append('[ [ ' if i == 0 else '  [ ')
        str_arr.append(''.join([f'{item:>{item_spacing}}, ' for item in matrix[i]])[:-2] + ' ]')
        str_arr.append(' ]' if i == len(matrix) - 1 else ',\n')
    return ''.join(str_arr)


if __name__ == '__main__':
    llist = construct_linked_list([0, 1, 2, 3, 4, 5])
    btree = construct_binary_tree([3, 9, 20, None, None, 15, 7])
    a = flatten_binary_tree(btree)
    print(list(llist))
    print(list(btree))
    print(matrix_to_string([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 2340]]))