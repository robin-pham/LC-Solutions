# 108 - array ot bst

# [-10, -3, 0, 5, 9]  - left is smaller, right is larger
#  find mid point - node.left = left of mid point, node.right = right of mid
# 11:40

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def array_to_BST(nums):
    if not nums:
        return
    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = array_to_BST(nums[:mid])
    node.right = array_to_BST(nums[mid+1:])

    return node

nums = [-10, -3, 0, 5, 9]
head = array_to_BST(nums)
print(head.val)

