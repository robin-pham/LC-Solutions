# 278 - First Bad Version


def firstBadVersion(n):
    lower, upper = 0, n
    while lower <= upper:
        mid = (lower + upper) // 2
        if isBadVersion(mid):
            upper = mid - 1
        else:
            lower = mid + 1
    return mid if isBadVersion(mid) else mid + 1
