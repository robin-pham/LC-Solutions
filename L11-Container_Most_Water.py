# L11 - Container With Most Water


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_idx, right_idx, max_area = 0, len(height) - 1, 0

        while left_idx < right_idx:
            area = (right_idx - left_idx) * (min(height[left_idx], height[right_idx]))
            max_area = max(area, max_area)

            if height[left_idx] > height[right_idx]:
                right_idx -= 1
            else:
                left_idx += 1

        return max_area
