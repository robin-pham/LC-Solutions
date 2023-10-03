# 98 - Validate Binary Search Tree


"""
left subtree only values less than node
right subtree only values greater than node

return (bool, smallest, largest) of values in subtree? and compare to node.val?

5
node.left reutnrs (1,1)
node.right

    4 
    node.left returns (3,3)
    node.right returns(6,6)
    valid
    4 returns (3,6)
3 is less than 5 so not valid
"""


# def validate_tree(root):
#     def DFS(node):
#         if not node:
#             return (True, None, None)
#         if not node.left and not node.right:
#             return (True, node.val, node.val)

#         l_valid, l_min, l_max = DFS(node.left)
#         r_valid, r_min, r_max = DFS(node.right)
#         print(node.val, l_valid, l_min, l_max, r_valid, r_min, r_max)
#         if (
#             not l_valid
#             or not r_valid
#             or (l_max is not None and l_max >= node.val)
#             or (r_min is not None and r_min <= node.val)
#         ):
#             return (False, 0, 0)
#         return (True, l_min or node.val, r_max or node.val)

#     valid, _, _ = DFS(root)
#     return valid

"""
rather than return max/min values from the subtrees to the node and then comparing, 
send the node value down the subtrees at teh max or min - if a node value exceeds that, then return false/true

"""


def is_valid(root):
    def search_tree(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False

        return search_tree(node.left, min_val, node.val) and search_tree(
            node.right, node.val, max_val
        )

    return search_tree(root, float("-inf"), float("inf"))


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = TreeNode(1)
a.left = TreeNode(0)
a.right = TreeNode(0)
# a.right.left = TreeNode(3)
# a.right.right = TreeNode(6)
print(is_valid(a))
