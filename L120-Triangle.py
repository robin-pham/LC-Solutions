# L120 - Triangle


def minimumTotal(self, triangle: List[List[int]]) -> int:
    prev_level_sum = [triangle[0][0]]
    for level in triangle[1:]:
        current_level_sum = []
        for idx, num in enumerate(level):
            if idx == 0:
                current_level_sum.append(num + prev_level_sum[0])
            elif idx == len(level) - 1:
                current_level_sum.append(num + prev_level_sum[-1])
            else:
                prev_min = min(prev_level_sum[idx], prev_level_sum[idx - 1])
                current_level_sum.append(prev_min + num)

        prev_level_sum = current_level_sum
    return min(prev_level_sum)
