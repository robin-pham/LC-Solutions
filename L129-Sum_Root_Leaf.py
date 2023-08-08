# L129 - Sum_Root_Leaf.py


def sumNumbers(self, root: Optional[TreeNode]) -> int:
    root_to_leaf = []
    sum = 0

    def calculate_sum(path):
        path_sum = 0
        for power, digit in enumerate(path[::-1]):
            path_sum += 10**power * digit
        return path_sum

    def path(node, path_list):
        nonlocal sum
        if not node:
            return
        if not node.left and not node.right:
            sum += calculate_sum(path_list + [node.val])
            return
        path(node.left, path_list + [node.val])
        path(node.right, path_list + [node.val])

    path(root, root_to_leaf)
    return sum
