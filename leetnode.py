from __future__ import annotations

from collections import deque
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
        arr = [self.val]
        last_non_none = 1
        nodes = deque([self])
        while nodes:
            node = nodes.popleft()
            if node.left:
                arr.append(node.left.val)
                last_non_none = len(arr)
                nodes.append(node.left)
            else:
                arr.append(None)
            if node.right:
                arr.append(node.right.val)
                last_non_none = len(arr)
                nodes.append(node.right)
            else:
                arr.append(None)
        return arr[:last_non_none]

    def tree_string(self) -> str:
        def _build_tree_string(root: TreeNode[T], curr_index: int) -> (List[str], int, int, int):
            if root is None:
                return [], 0, 0, 0

            line1 = []
            line2 = []
            node_repr = str(root.val)

            new_root_width = gap_size = len(node_repr)

            # Get the left and right sub-boxes, their widths, and root repr positions
            l_box, l_box_width, l_root_start, l_root_end = _build_tree_string(root.left, 2 * curr_index + 1)
            r_box, r_box_width, r_root_start, r_root_end = _build_tree_string(root.right, 2 * curr_index + 2)

            # Draw the branch connecting the current root node to the left sub-box
            # Pad the line with whitespaces where necessary
            if l_box_width > 0:
                l_root = (l_root_start + l_root_end) // 2 + 1
                line1.append(' ' * (l_root + 1))
                line1.append('_' * (l_box_width - l_root))
                line2.append(' ' * l_root + '/')
                line2.append(' ' * (l_box_width - l_root))
                new_root_start = l_box_width + 1
                gap_size += 1
            else:
                new_root_start = 0

            # Draw the representation of the current root node
            line1.append(node_repr)
            line2.append(' ' * new_root_width)

            # Draw the branch connecting the current root node to the right sub-box
            # Pad the line with whitespaces where necessary
            if r_box_width > 0:
                r_root = (r_root_start + r_root_end) // 2
                line1.append('_' * r_root)
                line1.append(' ' * (r_box_width - r_root + 1))
                line2.append(' ' * r_root + '\\')
                line2.append(' ' * (r_box_width - r_root))
                gap_size += 1
            new_root_end = new_root_start + new_root_width - 1

            # Combine the left and right sub-boxes with the branches drawn above
            gap = ' ' * gap_size
            new_box = [''.join(line1), ''.join(line2)]
            for i in range(max(len(l_box), len(r_box))):
                l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
                r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
                new_box.append(l_line + gap + r_line)

            # Return the new box, its width and its root repr positions
            return new_box, len(new_box[0]), new_root_start, new_root_end

        return '\n' + '\n'.join((line.rstrip() for line in _build_tree_string(self, 0)[0]))


def build_btree(arr: List[T]) -> Optional[TreeNode[T]]:
    if not arr or arr[0] is None:
        return None

    nodes = [TreeNode(val) if val else None for val in arr]
    children = nodes[::-1]
    root = children.pop()
    if children:
        for node in nodes:
            if node:
                node.left = children.pop()
                if not children:
                    break
                node.right = children.pop()
                if not children:
                    break

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
        return '[' + ' -> '.join([repr(node.val) for node in list(self)]) + ']'

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
    for list_node in llist1:
        print(list_node.val + list_node.next.val if list_node.next is not None else list_node.val)
    print()

    btree1 = build_btree([3, 9, 20, 8, 16, 15, 7, 1, 2, None, None, 3, None, None, None, None, None, 12])
    btree2 = TreeNode.from_list([5, 9, 20, None, 42, 15, 7, None, None, None, None, 222, 13, 6])
    print(btree1)
    print(btree1.tree_string())
    print(btree2)
    print(btree2.tree_string())
    print()

    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[3, 0, 8, 4], [2, 2340, 5, 7], [97, 2, 6, 3], [0, 3, 1, 13]]
    print(matrix_to_string(mat1))
    print(matrix_to_string(mat2))
