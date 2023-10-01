# 814 - Prune Tree

# if theres a branch without 1, prune it (delete it)
# DFS - return false if no 1, true if yes, set node.left or right to None if faalse, return left or right bool


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def prune_tree(root):
    if not root:
        return None
    root.left = prune_tree(root.left)
    root.right = prune_tree(root.right)
    return root if (root.val or root.left or root.right) else None

    # def cancel_nodes(node):
    #     if not node or (not node.left and not node.right and node.val == 0):
    #         return False
    #     left_path = cancel_nodes(node.left)
    #     right_path = cancel_nodes(node.right)
    #     if not left_path:
    #         node.left = None
    #     if not right_path:
    #         node.right = None
    #     current = True if node.val == 1 else False
    #     return left_path or right_path or current

    # cancel_nodes(root)
    # return root


a = TreeNode(1)
a.right = TreeNode(0)
a.right.left = TreeNode(0)
a.right.right = TreeNode(1)

b = prune_tree(a)
print(b, b.val, b.right.val, b.right.right.val)
