# 240 - Search 2D Matrix 2

"""
binary search along the top-left to bottom-right diagonal to find which row/column the target is in
(number on diagonal will be higher)
must do binary search along both column and row

x x x x x

x x x x x 
x x x x x



"""

# 10:52


# def search_matrix(matrix, target):
#     def find_diagonal():
#         lower = (0, 0)
#         upper = (rows, cols)
#         while lower[0] <= upper[0] and lower[1] <= upper[1]:
#             mid = ((lower[0] + upper[0]) // 2, (lower[1] + upper[1]) // 2)
#             print("diagona", mid, matrix[mid[0]][mid[1]])
#             if matrix[mid[0]][mid[1]] == target:
#                 return True
#             elif matrix[mid[0]][mid[1]] > target:
#                 upper = (mid[0] - 1, mid[1] - 1)
#             else:  # cell < target
#                 lower = (mid[0] + 1, mid[1] + 1)
#         if (mid == (0, 0) and matrix[mid[0]][mid[1]] > target) or (
#             mid == (len(matrix) - 1, len(matrix[0]) - 1)
#             and matrix[mid[0]][mid[1]] < target
#         ):
#             return False
#         return (
#             mid
#             if matrix[mid[0]][mid[1]] > target
#             else (min(rows, mid[0] + 1), min(cols, mid[1] + 1))
#         )

#     def search_row():
#         lower, upper = 0, diagonal[1]
#         while lower <= upper:
#             mid = (lower + upper) // 2
#             print(mid, matrix[diagonal[0]][mid])
#             if matrix[diagonal[0]][mid] == target:
#                 return True
#             elif matrix[diagonal[0]][mid] > target:
#                 upper = mid - 1
#             else:
#                 lower = mid + 1
#         return True if matrix[diagonal[0]][mid] == target else False

#     def search_col():
#         lower, upper = 0, diagonal[0]
#         while lower <= upper:
#             mid = (lower + upper) // 2
#             print(mid, matrix[mid][diagonal[1]])
#             if matrix[mid][diagonal[1]] == target:
#                 return True
#             elif matrix[mid][diagonal[1]] > target:
#                 upper = mid - 1
#             else:
#                 lower = mid + 1
#         return True if matrix[mid][diagonal[1]] == target else False

#     rows, cols = len(matrix) - 1, len(matrix[0]) - 1

#     diagonal = find_diagonal()
#     print(diagonal)
#     if type(diagonal) == bool:
#         return diagonal
#     else:
#         return search_row() or search_col()


def search_matrix(matrix, target):
    row, col = len(matrix) - 1, 0
    while col < len(matrix[0]) and row >= 0:
        print(row, col, matrix[row][col])
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            col += 1
        else:
            row -= 1
    return (
        True
        if (
            row in range(len(matrix))
            and col in range(len(matrix[0]))
            and matrix[row][col] == target
        )
        else False
    )


matrix = [[5], [6]]
print(search_matrix(matrix, 5))
