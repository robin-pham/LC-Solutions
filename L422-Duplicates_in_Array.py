L422 - Duplicates_in_Array


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(3):
            for idx in range(len(nums)):
                nums[nums[idx] - 1], nums[idx] = nums[idx], nums[nums[idx] - 1]
        print(nums)
        for idx in range(len(nums)):
            if idx != nums[idx] - 1 and nums[nums[idx] - 1] == nums[idx]:
                duplicates.append(nums[idx])
        return duplicates


# time O(n) - 4 passes through solution... what is the dependence of size of nums and number of times we have to rearrange the items?
# space O(n) - array solution to be returned depends on nums
