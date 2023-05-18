L73 - Set_Zero.py


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for x, row in enumerate(matrix):
            for y, cell in enumerate(row):
                if cell == 0:
                    for idx in range(len(matrix[0])):
                        matrix[x][idx] = 1.1 if matrix[x][idx] != 0 else 0
                    for idx in range(len(matrix)):
                        matrix[idx][y] = 1.1 if matrix[idx][y] != 0 else 0
        for x, row in enumerate(matrix):
            for y, cell in enumerate(row):
                if cell == 1.1:
                    matrix[x][y] = 0


# time O(m*n*(m+n)) - nested row and col loops with another nest (row + col) loop
# space O(1) - no new initiliazed variables
