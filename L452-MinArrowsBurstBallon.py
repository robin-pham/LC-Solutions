# 452 - Minimum Number of Arrows to Burst Balloon
"""
 [[10,16], [2,8], [1,6], [7,12]]
am i trying to generate intervals of overlap with each incoming coord?
[10, 16]
then we get [2,8] - which gives us [2,8],[10,16]
then [1,6] which has [2,6] overlap with [2,8]
then [7,12] which has [7,8] overlap with [2,8] and [10,12] with [10, 16]
2 arrows

[[1,2],[2,3], [3,4], [4,5]]
one arrow will hit both [1,2] and [2,3] - so the one point counts as overlap
[1,2] intervals = [[1,2]]
then [2,3]  - there is overlap at [2,2] with [1,2]
then [3,4] - there is overlap at [3,3] with [2,3]
then [4,5] there is overlap at [4,4] with [3,4]
then one arrow at 2 - takes balloon [1,2] and [2,3]
topoligcal sort???

this makes me think of DSU - where the parent could be the overlapping interval
if the rank is higher (more balloons) then you shooting at it is prioritized
what happens when the interval is decreased as arrows come in?
how do we union? [1,2] and [2,3] are union at 2 - [3,4] not union - what is parent?


points length 1-10^5
and values -2**31 - 2**31

TOP SORT
adj list[prereq] = [courses]
in_degrees[course] = number of prereqs
the prereqs are teh arrows that can hit it? 
the higher the number of in_degrees, the more arrows can hit it
and the longer the adj list, the higher the arrow is ranked?
how do we describe a prereq/arrow? one point or a range?
do we have to sort the balloons first? (nlogn) then n

regular sorting
[[1,6],[2,8],[7,12],[10,16]]
[2,6] covers 0 and 1
[7,8] covers 1 and 2
[10,12] covers 2 and 3

intervals = [[(2,6), 0, 1]]
"""


def pop_balloons(points):
    points = sorted(points)
    intervals = [[(points[0][0], points[0][1]), 0]]
    print(intervals)
    for start, end in points[1:]:
        print(start, end)


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
pop_balloons(points)
