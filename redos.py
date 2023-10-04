#  77 - Combinations
#  all combos of k numbers in range 1-n
#  n = 4, k = 2 - [1,2],[1,3],[1,4],[2,3],[2,4],[3,4]
# recursive solution, calling function, and passing the current combo, numbers to choose from
# if current combo len == k, add to combos
# otherwise call function with combo + numbers


def combinations(n, k):
    combos = []

    def make_combo(current_combo):
        if len(current_combo) == k:
            combos.append(current_combo)
            return
        for num in range(current_combo[-1] + 1, n + 1):
            make_combo(current_combo + [num])

    for num in range(1, n + 1):
        make_combo([num])
    return combos


# 39 - Combo Sums - 10 min
# use numbers unlimited times
def combo_sum(candidates, target):
    combos = []

    def make_sums(current_combo, sum, start):
        print(current_combo)
        if sum == target:
            combos.append(current_combo)
            return
        elif sum > target:
            return

        for idx, num in enumerate(candidates[start:]):
            if num <= (target - sum):
                make_sums(current_combo + [num], sum + num, start + idx)

    make_sums([], 0, 0)
    return combos


# 78 - Subsets 2:14
# give array nums of unique elements, return all subsets - no dupicates, in any order
# only add numbers larger than previously added
# pass current set, and start idx number passed into the set
#  for num in nums[start:] -> call function with new set + num


def subsets(nums):
    # recursive
    subset = []

    def make_sets(set, start):
        subset.append(set)
        if start == len(nums):
            return
        for idx, num in enumerate(nums[start:]):
            make_sets(set + [num], start + idx + 1)

    make_sets([], 0)
    return subset


# iterative
# subset = [[]]
# for num in nums:
#     current = []
#     for set in subset:
#         current.append(set + [num])
#     subset += current
#     print(subset)
# return subset


# 46 - Permutations - 9 min
# array of nums - they are distinct, return all permutations
#  have a perm function that takes in current perm, and remaining elements


def permutations(nums):
    perms = []

    def make_perms(current, remaining):
        if not remaining:
            perms.append(current)
            return
        for idx, num in enumerate(remaining):
            make_perms(current + [num], remaining[:idx] + remaining[idx + 1 :])

    make_perms([], nums)
    return perms


print(permutations([1, 2, 3]))
