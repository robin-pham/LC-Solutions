# L662 - Max_Width_Binary_Tree


def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    max_width = 1
    queue = [(root, 0)]
    while queue:
        max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
        new_queue = []
        for node, idx in queue:
            if node.left:
                new_queue.append((node.left, 2 * idx + 1))
            if node.right:
                new_queue.append((node.right, 2 * idx + 2))
        queue = new_queue
    return max_width
