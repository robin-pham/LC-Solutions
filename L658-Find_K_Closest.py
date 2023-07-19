# L658-Find_K_Closest


def findClosestElements(arr, k, x):
    if x <= arr[0]:
        return arr[:k]
    elif x >= arr[-1]:
        return arr[-k:]

    def find_int():
        lower, upper = 0, len(arr) - 1
        gap = arr[-1] - arr[0]
        while True:
            mid = (lower + upper) // 2
            if lower + 1 == upper:
                if abs(arr[upper] - x) < abs(arr[lower] - x):
                    return upper
                else:
                    return lower
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                lower = mid
            elif arr[mid] > x:
                upper = mid

    lower = find_int()
    upper = lower + 1
    while upper - lower != k:
        if lower == 0:
            upper += 1
        elif upper == len(arr):
            lower -= 1
        elif abs(arr[upper] - x) < abs(arr[lower - 1] - x):
            upper += 1
        else:
            lower -= 1
    return arr[lower:upper]


arr = [1, 4, 6, 8, 10, 15, 17]
x = 5

findClosestElements(arr, 5, 5)
