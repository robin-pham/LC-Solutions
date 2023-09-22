#  283 Move Zeroes

'''
    [0,6,0,1,0,3,12]
    [4,2,4,0,0,3,0,5,1,0]

    you only need to swap when the num_idx > zero_idx
    you only need to go through the numbers once
'''

def move_zero_pointers(nums):
    z_idx = 0
    while z_idx < len(nums)-1 and nums[z_idx] != 0:
        z_idx += 1
    if z_idx == len(nums)-1:
        return
    start = z_idx + 1
    for idx, num in enumerate(nums[z_idx+1:]):
        idx += start
        if num != 0:
            nums[idx], nums[z_idx] = nums[z_idx], nums[idx]
        while z_idx < len(nums) and nums[z_idx] != 0:
            z_idx += 1
        print(nums)

nums = [4,2,4,0,0,3,0,5,1,0]
move_zero_pointers(nums)
