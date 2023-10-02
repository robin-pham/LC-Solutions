# 623 - Add One Row to Tree


# depth 1 is root of three
#  if depth = 1, put new node which is root of tree, original node is left subtree
#  for each non-null node at depth-1, make 2 new tree nodes with val - node.left is left subtree, node.right is right
#
# set original level (at root ) to be 1, when level is depth-1, add the new nodes
# BFS to keep all ndoes at each level in the queue
# when we are at the correct level, for node in queue, 2 new nodes, then transfer node.left and node.right
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def add_row(root, val, depth):
    if depth == 1:
        new_root = TreeNode(val)
        new_root.left = root
        return new_root
    level = 1
    queue = [root]
    while level < depth - 1:
        new_queue = []
        for node in queue:
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        queue = new_queue
        level += 1
    # reached the row to add new nodes, queue has nodes we need
    for node in queue:
        new_left = TreeNode(val)
        new_left.left = node.left
        node.left = new_left
        new_right = TreeNode(val)
        new_right.right = node.right
        node.right = new_right
    return root


a = TreeNode(4)
a.left = TreeNode(2)
a.left.left = TreeNode(3)
a.left.right = TreeNode(1)
a.right = TreeNode(6)
a.right.left = TreeNode(5)

x = add_row(a, 1, 2)
queue = [x]
while queue:
    new_q = []
    for node in queue:
        print(node.val)
        if node.left:
            new_q.append(node.left)
        if node.right:
            new_q.append(node.right)
    queue = new_q
