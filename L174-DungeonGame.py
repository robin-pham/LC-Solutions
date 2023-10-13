# 174 - H - Dungeon Game


"""
going from top left to bottom right of dungeon
we can only move right or down
each cell has a number -> neg numbers decrease health, pos numbers increase health
if your HP <= 0, you die immediately
what is the minimum intiial health - return int

i think its like path sums, but tuples thorugh each cell, so we keep track of current health and abs min along that path
so (curr, min) for every path sum
path_sum = (d[0][0], d[0][0])
for num in d[0][1:]:
    current = path_sum[-1][0]
    abs_min = min(current, path_sum[-1][1])
"""


def min_HP(dungeon):
    inv_dun = [
        [num for num in dungeon[row][::-1]] for row in range(len(dungeon) - 1, -1, -1)
    ]
    row_health = [max(1, 1 - inv_dun[0][0])]
    for idx, num in enumerate(inv_dun[0]):
        if idx == 0:
            continue
        row_health.append(max(1, row_health[-1] - num))
    for row in inv_dun[1:]:
        for col, damage in enumerate(row):
            if col == 0:
                row_health[0] = max(1, row_health[0] - damage)
                continue
            row_health[col] = max(1, min(row_health[col], row_health[col - 1]) - damage)
    return row_health[-1]


# [[-5, 30, 10],
# [1, -10, -5],
# [3, -3, -2]]

dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
d = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
print(min_HP(dungeon))
