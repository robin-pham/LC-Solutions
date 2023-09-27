# 101 - Symmetric Tree

# 1:38


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def symmetric(node):
    def check_same_values(node_a, node_b):
        if not node_a and not node_b:
            return True
        if not node_a or not node_b or node_a.val != node_b.val:
            return False
        return check_same_values(node_a.left, node_b.right) and check_same_values(
            node_a.right, node_b.left
        )

    return check_same_values(node.left, node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(3)

print(symmetric(root))
