# 70 - Climbing Stairs

"""
trying to generate combinations of 1,2 to sum to n
[1,2]
- recursive generation of combination sums
- send current subset, its sum, and start idx
"""


def climbing_stairs(n):
    if n < 4:
        return n
    first, second = 1, 2
    for _ in range(2, n):
        first, second = second, first + second
    return second

    # combinations = 0
    # steps = [1, 2]

    # def perm_sum(current, sum):
    #     nonlocal combinations
    #     if sum == n:
    #         combinations += 1
    #         return
    #     for step in steps:
    #         if step + sum <= n:
    #             perm_sum(current + [step], sum + step)

    # perm_sum([], 0)
    # return combinations


for i in range(1, 10):
    print(i, climbing_stairs(i))
