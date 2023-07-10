L94 - Inorder_traversal


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node_stack = []
        io_values = []

        if not root:
            return io_values

        node = root
        while node or node_stack:
            while node:
                node_stack.append(node)
                node = node.left
            node = node_stack.pop()
            io_values.append(node.val)
            node = node.right
        return io_values
