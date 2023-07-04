L108 - Sorted_Array_to_BST


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # go to mid of nums to initiate root
        # pass nums[:mid] for left and nums[mid+1:] for right

        if not nums:
            return
        idx = len(nums) // 2
        root = TreeNode(nums[idx])
        root.left = self.sortedArrayToBST(nums[:idx])
        if idx + 1 < len(nums):
            root.right = self.sortedArrayToBST(nums[idx + 1 :])
        return root
