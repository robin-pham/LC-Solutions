L78 - Subsets.py


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for num in nums:
            new_subset = []
            for item in subset:
                new_subset.append(item + [num])
            subset += new_subset
        return subset
