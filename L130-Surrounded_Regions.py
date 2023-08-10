L130 - Surrounded_Regions


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = [(0, idx) for idx, col in enumerate(board[0]) if col == "O"]
        queue += [
            (len(board) - 1, idx) for idx, col in enumerate(board[-1]) if col == "O"
        ]
        queue += [(row, 0) for row, _ in enumerate(board) if board[row][0] == "O"]
        queue += [
            (row, len(board[0]) - 1)
            for row, _ in enumerate(board)
            if board[row][-1] == "O"
        ]

        while queue:
            new_queue = []
            for r, c in queue:
                board[r][c] = 0
                for dr, dc in directions:
                    if (
                        r + dr in range(len(board))
                        and c + dc in range(len(board[0]))
                        and board[r + dr][c + dc] == "O"
                    ):
                        new_queue.append((r + dr, c + dc))
            queue = new_queue
        print(board)
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == 0:
                    board[r][c] = "O"
                elif cell == "O":
                    board[r][c] = "X"
