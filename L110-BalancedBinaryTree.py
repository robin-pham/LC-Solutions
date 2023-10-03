# 110 - Balanced Binary Tree

# 11:50

"""
height balanced
def of height balanced - depth of 2 subtrees differs at most by 1

have dfs, and return depth of that subtree
3 - node.left returns 1
    -node.right returns 2
20 - node.left returns 1, right 1

1 - node.left 3, node.right 1
3 is 1 and 1
2 and 2 and 1
1 and 3 and 1
send depth and node through DFS - return depth - compare left and right
"""


def is_balanced(root):
    def DFS(node, depth):
        if not node:
            return depth
        depth += 1
        left_depth = DFS(node.left, depth)
        right_depth = DFS(node.right, depth)
        print(node.val, left_depth, right_depth)
        if (not left_depth or not right_depth) or abs(left_depth - right_depth) > 1:
            return False
        else:
            return max(left_depth, right_depth)

    return True if DFS(root, 0) else False


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = TreeNode(1)
a.left = TreeNode(2)
a.left.left = TreeNode(3)
a.right = TreeNode(29)
print(is_balanced(a))
