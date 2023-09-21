# L105 - Construct Binary Tree from Preorder and Inorder Traversal

# start 5:38 - 6:35, then 9:22 - 9:41

'''
        3
    9       20
12  2       15  7
pre - 3 9 12 2 20 15 7
in - 12 9 2 3 15 20 7

left = [12 9 2]
node 3
is left, so node.left with left_stack
leftleft = [12] 
node 9

'''
from collections import deque
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def construct_tree(preorder, inorder):
    inorder_deque = deque(inorder)
    idx = 0

    def createNode(inorder):
        nonlocal idx
        left_stack = deque([])
        while preorder[idx] != inorder[0]:
            left_stack.append(inorder.popleft())
        node = TreeNode(preorder[idx])
        idx += 1
        inorder.popleft()
        if left_stack:
            node.left = createNode(left_stack)
        if inorder:
            node.right = createNode(inorder)

        return node

    root = createNode(inorder_deque)
    return root
        
pre = [3,9,20,15,7]
ino = [9,3,15,20,7]

node = construct_tree(pre, ino)

queue = [node]
while queue:
    new_queue = []
    for node in queue:
        print(node.val)
        if node.left:
            new_queue.append(node.left)
        if node.right:
            new_queue.append(node.right)
    queue = new_queue

