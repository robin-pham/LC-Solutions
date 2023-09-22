#  75 Sort Colors

'''
    [2,0,2,1,1,0]
left = 0    (2)
right = 5   (0) swap and change idx
    [0,0,2,1,1,2]
left = 2 (+1 until not 0)   (2)
right = 4                   (1) swap
    [0,0,1,1,2,2]
left = 2 

loop through all the numbers
but we have a pointer at left for the first non 0 number
and a pointer at the right for hte first non 2 number
if the number we are at is 0 or 2, we swap
'''

def sort_colors(nums):
    left, current, right = 0, 0, len(nums) - 1

    while current <= right:
        if nums[current] == 0:
            nums[left], nums[current] = nums[current], nums[left]
            left +=1
            current += 1
        elif nums[current] == 2:
            nums[current], nums[right] = nums[right], nums[current]
            right -= 1
        else:   
            current += 1
        print(nums, left, current, right)


nums = [1,2,2,1,1,1,2,2,0,0,0,1,1]
sort_colors(nums)
print(nums)