from __future__ import annotations

from typing import List, Optional, Generic, TypeVar

T = TypeVar('T')


class TreeNode(Generic[T]):
    def __init__(self, val: T):
        self.val = val
        self.left = None
        self.right = None

    def __iter__(self) -> T:
        for val in self.to_list():
            yield val

    def __repr__(self) -> str:
        return str(self.to_list())

    @staticmethod
    def from_list(arr: List[T]) -> Optional[TreeNode[T]]:
        return build_btree(arr)

    def to_list(self) -> List[T]:
        def get_last_index(i, node):
            if node.left is None:
                if node.right is None:
                    return i
                return get_last_index((i << 1) + 2, node.right)
            if node.right is None:
                return get_last_index((i << 1) + 1, node.left)
            return max(get_last_index((i << 1) + 1, node.left), get_last_index((i << 1) + 2, node.right))

        def flatten(i, node):
            nonlocal arr
            if node is not None:
                arr[i] = node.val
                flatten((i << 1) + 1, node.left)
                flatten((i << 1) + 2, node.right)

        arr = [None] * (get_last_index(0, self) + 1)
        flatten(0, self)
        return arr

    def to_tree_string(self, draw_branches=True) -> str:
        arr = self.to_list()

        item_spacing = max([1 if item is None else len(str(item)) for item in arr])
        height = int.bit_length(len(arr)) - 1

        str_arr = []
        i = 0
        for level in range(height + 1):
            spacing_margin = ((1 << (height - level)) - 1) * item_spacing
            spacing_middle = ((1 << (height - level + 1)) - 1) * item_spacing
            end = min(i + (1 << level), len(arr))
            j = i

            str_arr.append(' ' * spacing_margin)
            for i in range(i, end):
                str_arr.append(' ' * item_spacing if arr[i] is None else f'{arr[i]:^{item_spacing}}')
                if i != end:
                    str_arr.append(' ' * spacing_middle)
            i += 1
            while str_arr[-1].isspace():
                str_arr = str_arr[0:-1]
            str_arr.append('\n')

            if draw_branches and level != height:
                str_arr.append(' ' * (spacing_margin - 1))
                for j in range(j, end):
                    if arr[j] is None:
                        str_arr.append(' ' * (item_spacing + 2))
                    else:
                        left = (j << 1) + 1
                        right = (j << 1) + 2
                        str_arr.append(' ' if left >= len(arr) or arr[left] is None else '/')
                        str_arr.append(' ' * item_spacing)
                        str_arr.append(' ' if right >= len(arr) or arr[right] is None else '\\')
                    if j != end:
                        str_arr.append(' ' * (spacing_middle - 2))
                while str_arr[-1].isspace():
                    str_arr = str_arr[0:-1]
                str_arr.append('\n')

        return ''.join(str_arr[0:-1])


def build_btree(arr: List[T]) -> Optional[TreeNode[T]]:
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


class ListNode(Generic[T]):
    def __init__(self, val: T):
        self.val = val
        self.next = None

    def __iter__(self) -> T:
        current = self
        while current is not None:
            yield current
            current = current.next

    def __repr__(self) -> str:
        return str([node.val for node in list(self)])

    @staticmethod
    def from_list(arr: List[T]) -> Optional[ListNode[T]]:
        return build_linked_list(arr)


def build_linked_list(arr: List[T]) -> Optional[ListNode[T]]:
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
    llist1 = build_linked_list(['a', 'b', 'c', 'd'])
    llist2 = ListNode.from_list(['e', 'f', 'g', 'h'])
    print(llist1)
    print(llist2)
    for node in llist1:
        print(node.val + node.next.val if node.next is not None else node.val)
    print()

    btree1 = build_btree([3, 9, 20, 8, 16, 15, 7, 1, 2, None, None, 3])
    btree2 = TreeNode.from_list([3, 9, 20, None, 42, 15, 7, None, None, None, None, 222, 13, 6])
    print(btree1)
    print(btree1.to_tree_string())
    print(btree2)
    print(btree2.to_tree_string())
    print()

    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[3, 0, 8, 4], [2, 2340, 5, 7], [97, 2, 6, 3], [0, 3, 1, 13]]
    print(matrix_to_string(mat1))
    print(matrix_to_string(mat2))
