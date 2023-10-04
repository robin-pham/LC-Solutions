# 62 - Unique paths


"""
given m and n - representing dimensions of grid
robot starts top left [0][0] - it can only move down or right - how many unique paths to bottom right can it take

if we have 3 x 3
1 1 1
1 2 3
1 3 6

along axes, there is only 1 path
along other corners, it is the sum of the two paths (top and left)
have an array for number of paths along each column
for each loop, it will add to the unique paths at each point in the next row
"""


def unique_paths(m, n):
    paths = [1 for _ in range(n)]
    for row in range(1, m):
        print(paths)
        for col in range(1, n):
            paths[col] += paths[col - 1]
    return paths[-1]


print(unique_paths(3, 7))
