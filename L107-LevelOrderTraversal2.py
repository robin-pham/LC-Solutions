# 107 - Binary Tree Level ORder Traversal 2


def level_order(root):
    level_order = []
    queue = [root]
    while queue:
        new_queue = []
        level_nodes = []
        for node in queue:
            level_nodes.append(node.val)
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        queue = new_queue
        level_order.append(level_nodes)
    return level_order[::-1]


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


print(level_order(a))
