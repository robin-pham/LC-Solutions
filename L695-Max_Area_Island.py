L695 - Max_Area_Island


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        islands_visited = set()

        def check_coord(row, col):
            if (
                (row, col) in islands_visited
                or row < 0
                or col < 0
                or row >= len(grid)
                or col >= len(grid[0])
            ):
                return False
            return True

        def check_island(row, col):
            if not check_coord(row, col) or grid[row][col] == 0:
                return 0
            current_area = 1
            islands_visited.add((row, col))
            current_area += check_island(row + 1, col)
            current_area += check_island(row - 1, col)
            current_area += check_island(row, col + 1)
            current_area += check_island(row, col - 1)
            return current_area

        for row, island_row in enumerate(grid):
            for col, value in enumerate(island_row):
                if value == 1:
                    island_area = check_island(row, col)
                    max_area = max(max_area, island_area)
        return max_area
