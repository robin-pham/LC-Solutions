# 162 - Find Peak Element

# log n = binary search


def find_peak(nums):
    if len(nums) == 1 or nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return len(nums) - 1
    lower, upper = 0, len(nums) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        print(mid, nums[mid])
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid - 1] < nums[mid]:
            lower = mid + 1
        else:
            upper = mid - 1
    return max(mid, mid - 1, mid + 1, key=lambda x: nums[x])


nums = [1, 2, 1, 2, 1]
print(find_peak(nums))
