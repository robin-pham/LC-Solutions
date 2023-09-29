# L78 - Subsets.py


def subsets(nums):
    subset = [[]]
    for num in nums:
        print(subset)
        new_subset = []
        for item in subset:
            new_subset.append(item + [num])
        subset += new_subset
    return subset


subsets([1, 2, 3, 4])
