# LeetNode
A small Python 3 library to make doing LeetCode linked list, binary tree and matrix problems more convenient.

## Linked Lists
### Building a linked list from a list
    llist1 = build_linked_list(['a', 'b', 'c', 'd'])

or

    llist2 = ListNode.from_list(['e', 'f', 'g', 'h'])

### Printing a linked list
    >>> print(llist1)
    ['a', 'b', 'c', 'd']
    >>> print(llist2)
    ['e', 'f', 'g', 'h']

## Binary Trees
### Building a binary tree
`btree1 = build_btree([3, 9, 20, 8, 16, 15, 7, 1, 2, None, None, 3])`

or

`btree2 = TreeNode.from_list([3, 9, 20, None, 42, 15, 7, None, None, None, None, 222, 13, 6])`

### Printing a list representation of a binary tree

    >>> print(btree1)
    [3, 9, 20, 8, 16, 15, 7, 1, 2, None, None, 3]
    >>> print(btree2)
    [3, 9, 20, None, 42, 15, 7, None, None, None, None, 222, 13, 6]

### Printing a tree representation of a binary tree

    >>> print(btree1.to_tree_string())
                  3
                 /  \
          9               20
         /  \            /  \
      8       16      15      7
     /  \            /
    1   2           3
    >>> print(btree2.to_tree_string())
                          3
                        /   \
              9                      20
                \                   /   \
                   42          15           7
                              /   \       /
                            222   13     6

## Matrices
### Printing a matrix
    >>> mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> mat2 = [[3, 0, 8, 4], [2, 2340, 5, 7], [97, 2, 6, 3], [0, 3, 1, 13]]
    >>> print(matrix_to_string(mat1))
    [ [ 1, 2, 3 ],
      [ 4, 5, 6 ],
      [ 7, 8, 9 ] ]
    >>> print(matrix_to_string(mat2))
    [ [    3,    0,    8,    4 ],
      [    2, 2340,    5,    7 ],
      [   97,    2,    6,    3 ],
      [    0,    3,    1,   13 ] ]
