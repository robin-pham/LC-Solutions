# L2022-Convert_1D_to_2D


def construct2DArray(original, m: int, n: int):
    new_array = []
    if m * n != len(original):
        return new_array
    for row in range(m):
        new_array.append(original[row * n : row * n + n])

    return new_array


print(construct2DArray([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3))
