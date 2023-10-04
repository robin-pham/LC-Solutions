# 744 - Find Smallest Letter Greater Than Target


def find_smallest(letters, target):
    lower, upper = 0, len(letters) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if letters[mid] <= target:
            lower = mid + 1
        else:
            upper = mid - 1
    if mid == len(letters) - 1 and letters[mid] <= target:
        return letters[0]
    return letters[mid + 1] if letters[mid] <= target else letters[mid]


letters = ["c", "f", "j"]
print(find_smallest(letters, "d"))
