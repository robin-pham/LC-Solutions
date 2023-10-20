# L36-Valid Sudoku


def isValidSudoku(board):
    def check_nine(subarray):
        number_set = set()
        for element in subarray:
            if element.isnumeric():
                if element in number_set:
                    return False
                else:
                    number_set.add(element)
        return True

    for row in board:
        if not check_nine(row):
            return False
    for idx in range(9):
        col = [board[row][idx] for row in range(9)]
        if not check_nine(col):
            return False
    for sq1 in range(3):
        for sq2 in range(3):
            sq = [board[sq1 * 3 + i][sq2 * 3 + c] for i in range(3) for c in range(3)]
            if not check_nine(sq):
                return False
    return True
