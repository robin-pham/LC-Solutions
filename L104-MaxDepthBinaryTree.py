def max_depth(root):
    queue = [root]
    depth = 0
    while queue:
        new_queue = []
        for node in queue:
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        queue = new_queue
        depth += 1
    return depth


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

print(max_depth(a))
