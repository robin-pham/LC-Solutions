# L111-Min_Depth_Binary_Tree


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        depth = 0

        while root and queue:
            new_queue = []
            depth += 1
            for node in queue:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return depth
