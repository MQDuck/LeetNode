# LeetNode
A small Python 3.5+ library to make debugging LeetCode binary tree, linked list and matrix problems more convenient.

## Binary Trees
`from leetnode import TreeNode, build_btree`

### Creating a binary tree node
`btree_node = TreeNode('val')`

### Creating a binary tree from a list
`btree1 = build_btree([3, 9, 20, 8, 16, 15, 7, 1, 2, None, None, 3, None, None, None, None, None, 12])`

or

`btree2 = TreeNode.from_list(['a', 'b', 'cd', None, 'ef', 'gh', 'i', None, None, None, None, 'jkl', 'mn', 'o'])`

or, from a JSON string

`btree3 = TreeNode.from_list('[1, null, 555555, null, 43, 1]')`

### Printing a list representation of a binary tree

    >>> print(btree1)
    [3, 9, 20, 8, 16, 15, 7, 1, 2, None, None, 3, None, None, None, None, None, 12]
    
    >>> print(btree2)
    ['a', 'b', 'cd', None, 'ef', 'gh', 'i', None, None, None, None, 'jkl', 'mn', 'o']
    
    >>> print(btree3)
    [1, None, 555555, None, 43, 1]

### Printing a tree representation of a binary tree

    >>> print(btree1.tree_string())
               ___3_____
              /         \
        _____9          _20
       /      \        /   \
      8___     16     15    7
     /    \          /
    1     _2        3
         /
        12
        
    >>> print(btree2.tree_string())
       ______'a'______
      /               \
    'b'_            __'cd'___________
        \          /                 \
        'ef'     'gh'              __'i'_
                                  /      \
                              _'jkl'     'mn'
                             /
                           'o'
                           
    >>> print(btree3.tree_string())
    1__
       \
      555555__
              \
               43
              /
             1


## Linked Lists
`from leetnode import ListNode, build_linked_list`

### Creating a linked list node
`list_node = ListNode('val')`

### Creating a linked list from a list
`llist1 = build_linked_list(['a', 'b', 'c', 'd'])`

or

`llist2 = ListNode.from_list([1, 2, 3, 4, 5])`

or, from a JSON string

`llist3 = ListNode.from_list('["e", "f", "g", "h"]')`

### Printing a linked list
    >>> print(llist1)
    ['a' -> 'b' -> 'c' -> 'd']
    
    >>> print(llist2)
    [1 -> 2 -> 3 -> 4 -> 5]
    
    >>> print(llist3)
    ['e' -> 'f' -> 'g' -> 'h']

### Iterating over a linked list
    >>> for node in llist1:
    ...     print(node.val + node.next.val if node.next is not None else node.val)
    ...
    ab
    bc
    cd
    d

## Matrices
### Printing a matrix
    >>> mat1 = [[1.2, 2.33, 3.0], [4.5, 6.7777, 8], [9.0, 10.98, 111.42]]
    >>> mat2 = [[3, 0, 8, 4], [2, 2340, 5, 7], [97, 432, 6, 3], [0, 3, 1, 13]]
    >>> mat3 = mat3 = '[["a", "b", "ccc"], ["dd", "e", "ff"], ["g", "h", "i"]]'
    
    >>> print(matrix_to_string(mat1))
    [ [ 1.2,    2.33,   3.0      ],
      [ 4.5,    6.7777, 8        ],
      [ 9.0,    10.98,  111.42   ] ]
      
    >>> print(matrix_to_string(mat2))
    [ [    3,    0,    8,    4,  ],
      [    2, 2340,    5,    7,  ],
      [   97,  432,    6,    3,  ],
      [    0,    3,    1,   13,  ] ]

    >>> print(matrix_to_string(mat3))
    [ [ 'a',   'b',   'ccc'   ],
      [ 'dd',  'e',   'ff'    ],
      [ 'g',   'h',   'i'     ] ]
