# L283 - Move_Zeroes


def moveZeroes(nums) -> None:
    zero_idx = number_idx = 0
    while zero_idx < len(nums) and number_idx < len(nums):
        while zero_idx < len(nums) and nums[zero_idx] != 0:
            zero_idx += 1
        while number_idx < len(nums) and nums[number_idx] == 0:
            number_idx += 1
        if zero_idx < number_idx and number_idx < len(nums):
            nums[zero_idx], nums[number_idx] = nums[number_idx], nums[zero_idx]
        number_idx += 1


print(moveZeroes([0, 1, 0, 3, 12]))
print(moveZeroes([0]))
