# LCA of a Binary Tree


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def LCA(node, p, q):
    if not node:
        return
    left_subtree = LCA(node.left, p, q)
    right_subtree = LCA(node.right, p, q)
    print(node.val, left_subtree, right_subtree)
    if (left_subtree and right_subtree) or (node.val == p or node.val == q):
        return node
    elif left_subtree or right_subtree:
        return left_subtree or right_subtree


a = TreeNode(3)
a.left = TreeNode(5)
a.left.left = TreeNode(6)
a.left.right = TreeNode(2)
a.left.right.left = TreeNode(7)
a.left.right.right = TreeNode(4)
a.right = TreeNode(1)
a.right.left = TreeNode(0)
a.right.right = TreeNode(8)

x = LCA(a, 5, 1)
print(x, x.val)

# '''
# first ex, looking for 5 and 1
# node.left retursn true since it has a 5
# node.right retursn true since it has 1
# so if node.left and node.right, return node.val, 3

# second ex, looking for 5 and 4
# dfs into node.left

# node.right returns true
# and node.val is p, so return node.val = 5
# root receives node.val = 5, retru n5


# so at each node, x and y will be lca node left, node right
# if x and y, return nodeval
# OR x or y, nodeval == p or q, return nodeval
# elif x or y, return x or y
# OR nodeval == p or q, return true
# else
#     false
# '''
