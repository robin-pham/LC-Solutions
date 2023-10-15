# 688 - Knight PRobability in ChessBoard

"""
given k, n, row, col
k = number of moves being made
n = nxn size of board - top left is [0,0], bottom right is [n-1,n-1]
row, col is the starting coordinate
the horse can make 8 possible moves
if the horse moves off the board, it will, and stop moving
the horse will make k number of moves
whats hte probability it stays on the board

1 <= n <= 25
0 <= k <= 100
0 <= row,col <= n-1

100 moves is a lot of moves.....
can a horse move to every position on a chess board? yes

for each move/coord - i'm passing the percentage slice of it going there, the move number
it is returning percentage of staying on the board 
if not valid coord, return 0 

so for the first call of the function, we are passing the or9ginal coord, and 100% of slice

"""


def knight_moves(n, k, row, column):
    def is_valid(row, col):
        if 0 <= row < n and 0 <= col < n:
            return True
        return False

    directions = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]

    board_per = [[0 for _ in range(n)] for _ in range(n)]
    board_per[row][column] = 1

    for move in range(1, k + 1):
        new_board_per = [[0 for _ in range(n)] for _ in range(n)]
        for row_idx, row in enumerate(board_per):
            for col_idx, cell in enumerate(row):
                if cell != 0:
                    for dr, dc in directions:
                        if is_valid(dr + row_idx, dc + col_idx):
                            new_board_per[dr + row_idx][dc + col_idx] += cell / 8
        board_per = new_board_per

    remaining_per = 0
    for row in board_per:
        for cell in row:
            remaining_per += cell
    print(board_per)
    return remaining_per


print(knight_moves(8, 30, 6, 6))

# recursive solution
# def percentage_valid(row, col, slice, move_number):
#     if move_number == k:
#         return slice
#     percent = 0
#     for dr, dc in directions:
#         if 0 <= dr + row < n and 0 <= dc + col < n:
#             percent += percentage_valid(
#                 dr + row, dc + col, slice / 8, move_number + 1
#             )
#     return percent

# return percentage_valid(row, column, 1, 0)
