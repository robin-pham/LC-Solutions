# 230 - Kth Smallest Element in BST


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse all the way to the left - no node.left
        # count increases every time we traverse a node
        # inorder traversal of nodes
        node_count = 0
        kth_node = None

        def find_k(node):
            nonlocal node_count, kth_node
            if not node:
                return
            find_k(node.left)
            node_count += 1
            kth_node = node.val if node_count == k else kth_node
            find_k(node.right)

        find_k(root)

        return kth_node
