L53 - Max_Subarray.py


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
        if len(nums) == 1:
            return nums[0]
        for idx, num in enumerate(nums[1:], 1):
            if current_sum + num > num:
                current_sum += num
                max_sum = current_sum if current_sum >= max_sum else max_sum
            else:  # num > current_sum + num
                current_sum = num
                max_sum = num if num >= max_sum else max_sum
        return max_sum
