# 530 - Minimum Abs Difference in BST

"""
the smallest distance between a node and its children will be the right most of node.left or left most of node.right
so need to recursive look at these differences for all nodes in the tree
"""


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def abs_difference(root):
    # THIS IS INORDER TRAVERVSAL DUDE
    prev = None
    min_diff = float("inf")

    def inorder(node):
        nonlocal prev, min_diff
        if not node:
            return
        inorder(node.left)
        if prev is None:
            prev = node.val
        else:
            print(prev, node.val)
            min_diff = min(min_diff, abs(node.val - prev))
            prev = node.val
        inorder(node.right)

    inorder(root)
    return min_diff

    # min_diff = float("inf")

    # def find_min(node, val):
    #     # passing in node.right, check left most node
    #     while node.left:
    #         node = node.left
    #     return abs(node.val - val)

    # def find_max(node, val):
    #     while node.right:
    #         node = node.right
    #     return abs(node.val - val)

    # def dfs(node):
    #     nonlocal min_diff
    #     if node.left:
    #         dfs(node.left)
    #         min_diff = min(find_max(node.left, node.val), min_diff)
    #     if node.right:
    #         dfs(node.right)
    #         min_diff = min(find_min(node.right, node.val), min_diff)

    # dfs(root)
    # return min_diff


a = TreeNode(0)
a.right = TreeNode(2236)
a.right.left = TreeNode(1277)
a.right.left.left = TreeNode(519)
a.right.right = TreeNode(2776)

print(abs_difference(a))
