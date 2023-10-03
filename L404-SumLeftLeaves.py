# 404 - Sum of Left Leaves

# if node is a leaf, return value
# if node.left returns a value, add it to sum
# otherwise return


def sum_leaves(root):
    sum = 0

    def search_leaves(node):
        nonlocal sum
        if not node:
            return
        if node.left and not node.left.left and not node.left.right:
            sum += node.left.val

        search_leaves(node.left)
        search_leaves(node.right)

    search_leaves(root)
    return sum


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

print(sum_leaves(a))
