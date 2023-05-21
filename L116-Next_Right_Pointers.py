L116 - Next_Right_Pointers.py

#  DFS - O(N) time and space
class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.next and root.left:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

        return root


# BFS - O(N) time and space


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        queue = [root]
        if not root:
            return
        while queue:
            new_queue = []
            for idx, node in enumerate(queue):
                node.next = queue[idx + 1] if idx + 1 < len(queue) else None
                if node.left:
                    new_queue.append(node.left)
                    new_queue.append(node.right)
            queue = new_queue
        return root
