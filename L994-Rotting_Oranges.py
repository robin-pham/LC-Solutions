L994 - Rotting_Oranges


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0
        queue = []
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 2:
                    queue.append((r, c))
        while queue:
            new_queue = []
            for (
                r,
                c,
            ) in queue:
                for dr, dc in directions:
                    if (
                        r + dr in range(len(grid))
                        and c + dc in range(len(grid[0]))
                        and grid[r + dr][c + dc] == 1
                    ):
                        new_queue.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = 2
            queue = new_queue
            minutes = minutes + 1 if queue else minutes
            print(minutes, queue)

        for row in grid:
            for cell in row:
                if cell == 1:
                    return -1
        return minutes
