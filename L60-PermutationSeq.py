# 60 - Permutation Sequence


def perm_sequence(n, k):
    def make_perms(current, remaining):
        nonlocal perms
        if perms >= k:
            return
        if not remaining:
            perms += 1
            if perms == k:
                result.append(current)
            return
        for idx, num in enumerate(remaining):
            make_perms(current + [num], remaining[:idx] + remaining[idx + 1 :])

    nums = [i for i in range(1, n + 1)]
    perms = 0
    result = []
    make_perms([], nums)
    return "".join(map(str, result[0]))


print(perm_sequence(3, 3))
