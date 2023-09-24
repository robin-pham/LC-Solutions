#  53 - Maximum Subarray

# [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# keep a max so far
# current start idx, current idx
#  csi, ci = 0, max = -2
#  ci += 1 - compare -2+1 to 1 -> 1 is larger so csi = ci 1
#  csi, ci = 1, max = 1
#  1 -3 or -3, -2 is larger so ci +1
#  csi = 1, ci = 3 -> 2 or 4, so csi = ci = 3


def max_subarray(nums):
    max_sum = current_sum = nums[0]
    start, current = 0, 1
    while current < len(nums):
        if current_sum + nums[current] > nums[current]:
            current_sum += nums[current]
        else:
            current_sum = nums[current]
            start = current
        current += 1
        max_sum = max(max_sum, current_sum)
        print(start, current, current_sum)
    return max_sum


nums = [5, 4, -1, 7, 8]
print(max_subarray(nums))
