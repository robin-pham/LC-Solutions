#  100 - Same Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    # left = same_tree(p.left, q.left)
    # right = same_tree(p.right, q.right)
    # print(p.val, q.val, left, right)
    return (
        (p.val == q.val) and same_tree(p.left, q.left) and same_tree(p.right, q.right)
    )


p = Node(1)
p.left = Node(3)
# p.right = Node(2)

q = Node(1)
# q.left = Node(2)
q.right = Node(3)

print(same_tree(p, q))
