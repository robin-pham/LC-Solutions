# 739 - Daily Temperatures

# if not stack, answer = 0
# if stack[-1] < day, pop util it is warmer - answer = idx - idx
# if warmer, add to stack, as tuple with idx


def daily_temps(temperatures):
    warmer = [0 for days in range(len(temperatures))]
    stack = []

    for idx, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_idx = stack.pop()
            warmer[prev_idx] = idx - prev_idx
        stack.append(idx)
    return warmer


temp = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temps(temp))
