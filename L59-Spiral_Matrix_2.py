L59 - Spiral_Matrix_2


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for _ in range(n)] for _ in range(n)]
        dir_r, dir_c = 0, 1
        row, col = 0, -1

        for num in range(1, n**2 + 1):
            if (
                row + dir_r not in range(n)
                or col + dir_c not in range(n)
                or matrix[row + dir_r][col + dir_c]
            ):
                dir_r, dir_c = dir_c, -dir_r
            matrix[row + dir_r][col + dir_c] = num
            row += dir_r
            col += dir_c
        return matrix
