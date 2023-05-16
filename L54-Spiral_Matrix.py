L54 - Spiral_Matrix.py


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        visited = set()
        row, col = 0, -1
        r_next, c_next = 0, 1
        while len(spiral) < (len(matrix) * len(matrix[0])):
            if (
                (row + r_next, col + c_next) in visited
                or (row + r_next) == len(matrix)
                or (row + r_next) == -1
                or (col + c_next) == len(matrix[0])
                or (col + c_next) == -1
            ):
                r_next, c_next = c_next, -r_next
            row += r_next
            col += c_next
            spiral.append(matrix[row][col])
            visited.add((row, col))
        return spiral
