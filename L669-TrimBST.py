# 669 - Trim a Binary Search Tree


"""
given low and high values, remove nodes from tree that exceed these values
there is a unique answer
any nodes descendant remains! even if trimmed

dfs approach - call function on node.left and node.right
base case - if not node, return 
    -otherwise return node, node.left, node.right, or None
case 1 - root is outside the high low values!
    if too low
        - head = node.right

    if too high
        - head = node.left

case 2 - node is too low
    - call function on node.right, return node.right

case 3 - node is too high
    - call function on node.left, return node.left

case 4 - node is ok
    - call function - node.left = func, node.right = func
"""


def trimBST(root, low, high):
    def trim_node(node):
        if not node:
            return
        node.left = trim_node(node.left)
        node.right = trim_node(node.right)
        if node.val < low:
            return node.right
        if node.val > high:
            return node.left
        return node

    if root.val < low:
        return trim_node(node.right)
    if root.val > high:
        return trim_node(node.left)
    root.left = trim_node(root.left)
    root.right = trim_node(root.right)
    return root


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = TreeNode(3)
a.left = TreeNode(0)
a.left.right = TreeNode(2)
a.left.right.left = TreeNode(1)
a.right = TreeNode(4)
x = trimBST(a, 1, 3)
q = [x]
while q:
    new_q = []
    for node in q:
        print(node.val)
        if node.left:
            new_q.append(node.left)
        if node.right:
            new_q.append(node.right)
    q = new_q
