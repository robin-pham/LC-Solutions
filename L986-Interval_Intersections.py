L986 - Interval_Intersections.py


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        overlap = []
        if not firstList or not secondList:
            return overlap

        first_idx = second_idx = 0
        while first_idx < len(firstList) and second_idx < len(secondList):
            if firstList[first_idx][0] > secondList[second_idx][1]:
                second_idx += 1
            elif secondList[second_idx][0] > firstList[first_idx][1]:
                first_idx += 1
            else:
                overlap.append(
                    [
                        max(firstList[first_idx][0], secondList[second_idx][0]),
                        min(firstList[first_idx][1], secondList[second_idx][1]),
                    ]
                )
                if firstList[first_idx][1] < secondList[second_idx][1]:
                    first_idx += 1
                else:
                    second_idx += 1

        return overlap
