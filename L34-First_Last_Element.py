# L34 - First_Last_Element


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_lower(lower_nums):
            lowest_idx = len(lower_nums)
            lower, upper = 0, len(lower_nums) - 1
            while lower <= upper:
                mid = (lower + upper) // 2
                if lower_nums[mid] < target:
                    lower = mid + 1
                else:
                    lowest_idx = mid
                    upper = mid - 1
            return lowest_idx

        def find_upper(upper_nums):
            highest_idx = -1
            lower, upper = 0, len(upper_nums) - 1
            while lower <= upper:
                mid = (lower + upper) // 2
                if upper_nums[mid] > target:
                    upper = mid - 1
                else:
                    highest_idx = mid
                    lower = mid + 1
            return highest_idx

        found_positions = [-1, -1]
        if not nums:
            return found_positions
        if len(nums) == 1:
            return found_positions if nums[0] != target else [0, 0]

        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            mid = (lower + upper) // 2
            if nums[mid] > target:
                upper = mid - 1
            elif nums[mid] < target:
                lower = mid + 1
            else:
                first = find_lower(nums[: mid + 1])
                last = find_upper(nums[mid:])
                return [first, mid + last]

        return [-1, -1]
