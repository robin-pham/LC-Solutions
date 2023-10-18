# 33 - Search in Rotated Sorted Array

"""
int array nums is sortedi n ascending order withdistinct values, and it is possibly rotated at a pivot index
also given target
return index of target if its in nums or -1 if not

alg must be O(logN)

first look at values of lower, mid, upper 4, 7, 2 
if target 0, must be between 7 and 2 -      is target <lower or <upper
then lower = 0, which is target

lower mid upper 4 7 2 - target 3, is not >lower or <upper so it is not in array

target 9
mid is 7, so lower becomes 0, is not between, so no in array

3
10
20
[2,4,6,8,10,12,14,16] 
l, m, u = 2, 10, 16 - 
target 3 - between l and m
target 10 - is mid
target 20 not in array, >upper

[10,12,14,16,2,4,6,8]
l, m, u = 10, 16, 8 
- target 3 - between mid and upper
l, m, u = 2, 4, 8
target 10 = lower
target 20 betwene mid and upper

[14,16,2,4,6,8,10,12]
l, m, u = 14, 4, 12
lowest = mid, highest is lower
target 3 - between l and m
target 10, betwene m and u
target 20, between l and m

when largest in the middle, check if l<= target <= m, or (<= u or >= m)
when larget on left/smallest in the middle, check if (target<= m or l <= target) or (m<= target <= u)
when l < m < u, check normal


either nums[lower] < nums[mid] AND/OR nums[mid] < nums[upper]
    check if the target is in between that in those cases, if yes, adjust lower/upper, else: do opposite
"""


def search_rotated(nums, target):
    lower, upper = 0, len(nums) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        if nums[mid] == target:
            return mid

        if nums[lower] <= nums[mid]:
            if nums[lower] <= target < nums[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
        else:
            if nums[mid] < target <= nums[upper]:
                lower = mid + 1
            else:
                upper = mid - 1
    return -1

    # while low < upper:
    #     mid = (low + upper) // 2
    #     print(low, mid, upper, "-", nums[low], nums[mid], nums[upper])
    #     if target == nums[mid]:
    #         return mid
    #     elif target == nums[low]:
    #         return low
    #     elif target == nums[upper]:
    #         return upper
    #     if max(nums[mid], nums[low], nums[upper]) == nums[mid]:
    #         if nums[low] < target < nums[mid]:
    #             upper = mid - 1
    #         elif target < nums[upper] or nums[mid] < target:
    #             low = mid + 1
    #         else:
    #             return -1
    #     elif max(nums[mid], nums[low], nums[upper]) == nums[upper]:
    #         if target < nums[low] or target > nums[upper]:
    #             return -1
    #         elif target < nums[mid]:
    #             upper = mid - 1
    #         else:
    #             low = mid + 1
    #     else:  # low is the highest, so mid must be smallest
    #         if nums[mid] < target < nums[upper]:
    #             low = mid + 1
    #         elif nums[low] < target or target < nums[mid]:
    #             upper = mid - 1
    #         else:
    #             return -1


# 036 - 472
nums = [4, 5, 6, 7, 0, 1, 2]
print(search_rotated(nums, 3))
