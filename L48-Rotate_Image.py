# L48 - Rotate_Image.py


def rotate(matrix):
    n = len(matrix) - 1
    for row in range((n + 1) // 2):
        for col in range((n + 2) // 2):
            (
                matrix[row][col],
                matrix[col][n - row],
                matrix[n - row][n - col],
                matrix[n - col][row],
            ) = (
                matrix[n - col][row],
                matrix[row][col],
                matrix[col][n - row],
                matrix[n - row][n - col],
            )
