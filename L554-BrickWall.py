# 554 - Brick Wall


# n row, each row has # of bricks with different widths - total width of each row is same
# draw vertical line to crow the least bricks - edge is not crossed
# return min number of crossed bricks

"""
[[1,2,2,1],
[3,1,2],
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]]

min rows initialized at number of rows
have a qeueu with all the rows - looking at -1 index each loop
subtracting 1 from end brick - if brick == 0, then add 1 min_at_level, also pop the brick from that row
if at end of loop, min_at_level < min_rows, new min rows
if no more bricks, return min
seems like BFS
"""

from collections import defaultdict


def least_bricks(wall):
    edges = defaultdict(int)
    for row in wall:
        position = 0
        for brick in row[:-1]:
            position += brick
            edges[position] += 1
    print(edges)
    print(max(edges.values()))
    return len(wall) if not edges else len(wall) - max(edges.values())


wall = [[1, 1], [2], [1, 1]]
least_bricks(wall)
