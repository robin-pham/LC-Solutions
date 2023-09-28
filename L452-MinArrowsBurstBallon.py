# 452 - Minimum Number of Arrows to Burst Balloon


def pop_balloons(points):
    points.sort(key=lambda x: x[1])

    arrows = 1
    prev = points[0][1]
    for point in points:
        if point[0] > prev:
            prev = point[1]
            arrows += 1
    return arrows


balloons = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(pop_balloons(balloons))
