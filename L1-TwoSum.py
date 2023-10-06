# 1 - Two Sum

"""
dict of ch with idx
see if target - num in dict
pointer - as you move along, add num to dict

"""


def two_sum(nums, target):
    pointer = 0
    num_idx = {}
    while pointer < len(nums):
        if target - nums[pointer] in num_idx:
            return [num_idx[target - nums[pointer]], pointer]
        num_idx[nums[pointer]] = pointer
        pointer += 1


nums = [3, 3]
print(two_sum(nums, 6))
