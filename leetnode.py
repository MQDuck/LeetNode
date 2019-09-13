from typing import List, Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __iter__(self):
        arr = btree_to_list(self)
        for val in arr:
            yield val

    def __repr__(self) -> str:
        return str(btree_to_list(self))


def construct_btree(arr: List) -> Optional[TreeNode]:
    if not arr or arr[0] is None:
        return None

    def construct(i, node):
        nonlocal arr
        if (i << 1) + 1 < len(arr):
            if arr[(i << 1) + 1] is not None:
                node.left = TreeNode(arr[(i << 1) + 1])
                construct((i << 1) + 1, node.left)
            if (i << 1) + 2 < len(arr) and arr[(i << 1) + 2] is not None:
                node.right = TreeNode(arr[(i << 1) + 2])
                construct((i << 1) + 2, node.right)

    root = TreeNode(arr[0])
    construct(0, root)
    return root


def btree_to_list(root: TreeNode) -> List:
    length = 1
    level_length = 1
    node = root
    while True:
        if node.right is not None:
            node = node.right
            level_length <<= 1
            length += level_length
        elif node.left is not None:
            node = node.left
            level_length = (level_length << 1) - 1
            length += level_length
        else:
            break

    arr = [None] * length

    del node
    del length
    del level_length

    def flatten(i, node):
        nonlocal arr
        if node is not None:
            arr[i] = node.val
            flatten((i << 1) + 1, node.left)
            flatten((i << 1) + 2, node.right)

    flatten(0, root)
    return arr


def btree_list_to_string(arr: List) -> str:
    if not arr:
        return ''

    item_spacing = max([1 if item is None else len(str(item)) for item in arr])
    height = int.bit_length(len(arr)) - 1

    str_arr = []
    i = 0
    for level in range(height + 1):
        spacing_margin = ((1 << (height - level)) - 1) * item_spacing
        spacing_middle = ((1 << (height - level + 1)) - 1) * item_spacing

        str_arr.append(' ' * spacing_margin)
        for i in range(i, end):
            str_arr.append(' ' * item_spacing if arr[i] is None else f'{arr[i]:^{item_spacing}}')
            str_arr.append('\n' if i == end - 1 else ' ' * spacing_middle)
        i += 1

    return ''.join(str_arr)


def btree_to_string(root: TreeNode) -> str:
    return btree_list_to_string(btree_to_list(root))


class ListNode:
    def __init__(self, val):
        self.val = val
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
    btree = construct_btree([3, 9, 20, None, None, 15, 7, None, None, None, None, 222, None, 6])
    # btree = construct_btree([3, 9, 20, 8, 16, 15, 7, 1, 2, None, None, 3])
    a = btree_to_list(btree)
    mat = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 2340]]
    print(list(llist))
    print(btree)
    print(btree_to_string(btree))
    print(a)
    print(matrix_to_string(mat))
