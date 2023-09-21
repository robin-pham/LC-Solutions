#  35 - Search Insert Position - 5:18 - 5:25

# binary search - O(log N)

def search_position(nums, target):
    lower, upper = 0, len(nums) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            upper = mid - 1
        else: 
            lower = mid + 1
    return mid if nums[mid] > target else mid + 1

nums = [1,3,5,6]
print(search_position(nums,-1))