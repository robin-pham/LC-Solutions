# 687 Longeset Univalue Path


# dfs and recursion to find longest path
# need to compare longest path from left, from right, and closed branch (left + right through the node)
# should return to the node above, the curret path value - at each node, check values and set max if necessary
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def longest_path(node):
    max_path = 0

    def search_nodes(node):
        nonlocal max_path
        if not node:
            return 0
        left_path = search_nodes(node.left)
        right_path = search_nodes(node.right)
        if node.left and node.left.val == node.val:
            left_path = search_nodes(node.left) + 1
        else:
            left_path = 0
        if node.right and node.right.val == node.val:
            right_path += 1
        else:
            right_path = 0
        max_path = max(max_path, left_path + right_path)
        print(node.val, left_path, right_path)
        return max(left_path, right_path)

    search_nodes(node)
    return max_path


root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

print(longest_path(root))
