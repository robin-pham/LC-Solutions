L74 - Search_2D_Matrix.py


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lower, upper = 0, len(matrix) * len(matrix[0]) - 1

        while lower <= upper:
            mid = (lower + upper) // 2
            if target == matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
                return True
            elif target < matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
                upper = mid - 1
            else:
                lower = mid + 1
        return target == matrix[mid // len(matrix[0])][mid % len(matrix[0])]


# time O(logN), space O(1)
