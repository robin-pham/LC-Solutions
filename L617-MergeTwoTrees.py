# 617 - Merge TWo Binary Trees

"""
if two nodes overlap, sum node as two
otherwise the non-null nodei s used as node of new tree - return merged tree

-am i creating a brand new tree, or am i changing nodes on the trees 
num of nodes in both trees [0,2000]

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def merge_trees(root1, root2):
    if not root1 or not root2:
        return root1 or root2

    new_root = TreeNode(root1.val + root2.val)
    new_root.left = merge_trees(root1.left, root2.left)
    new_root.right = merge_trees(root1.right, root2.right)

    return new_root


a = TreeNode(1)
a.left = TreeNode(3)
a.right = TreeNode(2)
a.left.left = TreeNode(5)

b = TreeNode(2)
b.left = TreeNode(1)
b.left.right = TreeNode(4)
b.right = TreeNode(3)
b.right.right = TreeNode(7)

x = merge_trees(a, b)


def io_traversal(node):
    if not node:
        return
    io_traversal(node.left)
    print(node.val)
    io_traversal(node.right)


io_traversal(x)
