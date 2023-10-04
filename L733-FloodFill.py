# 733 - Flood Fill


#  if directional coords are valid and same color, call function on them
def flood_fill(image, sr, sc, color):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]

    def is_valid(row, col):
        if 0 <= row < len(image) and 0 <= col < len(image[0]) and not visited[row][col]:
            return True
        return False

    def flood(row, col, orig):
        image[row][col] = color
        visited[row][col] = True
        for dr, dc in directions:
            n_row = dr + row
            n_col = dc + col
            if is_valid(n_row, n_col) and image[n_row][n_col] == orig:
                flood(n_row, n_col, orig)

    flood(sr, sc, image[sr][sc])
    return image


im = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(flood_fill(im, 1, 1, 2))
