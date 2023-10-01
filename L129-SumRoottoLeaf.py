# 129 - Sum Root to Leaf Numbers
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_root(root):
    root_leaves = []

    def dfs(node, leaf_path):
        if not node.left and not node.right:
            root_leaves.append(leaf_path * 10 + node.val)
            return
        if node.left:
            dfs(node.left, leaf_path * 10 + node.val)
        if node.right:
            dfs(node.right, leaf_path * 10 + node.val)

    dfs(root, 0)
    sum = 0
    print(root_leaves)
    for num in root_leaves:
        sum += num
    return sum


a = TreeNode(4)
a.left = TreeNode(9)
a.right = TreeNode(0)
a.left.left = TreeNode(5)
a.left.right = TreeNode(1)

print(sum_root(a))
