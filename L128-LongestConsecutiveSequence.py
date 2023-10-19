# 128 - Longest Consecutive Sequence

"""
given unsorted array of int nums - return len of longest consecutive elements sequence
must run in O(N) time

making groups of consecutive numbers - union find
go through elements in nums, find element - if n-1 or n+1 in parents, union 
"""


class DSU:
    def __init__(self):
        self.parents = {}
        self.rank = {}

    def find(self, node):
        if node not in self.parents:
            self.parents[node] = node
            return node
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def get_rank(self, node):
        if node not in self.rank:
            self.rank[node] = 0
        return self.rank[node]

    def union(self, node_a, node_b):
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)
        if parent_a == parent_b:
            return
        rank_a = self.get_rank(parent_a)
        rank_b = self.get_rank(parent_b)
        if rank_a > rank_b:
            self.parents[parent_b] = parent_a
        else:
            self.parents[parent_a] = parent_b
            if rank_a == rank_b:
                rank_b += 1


from collections import defaultdict


def consecutive_seq(nums):
    num_family = DSU()
    for num in nums:
        num_family.find(num)
        if num + 1 in num_family.parents:
            num_family.union(num, num + 1)
        if num - 1 in num_family.parents:
            num_family.union(num, num - 1)
    sequences = defaultdict(set)
    for num in nums:
        parent = num_family.find(num)
        sequences[parent].add(num)
    return len(max(sequences.values(), key=lambda x: len(x)))


nums = [100, 4, 200, 1, 3, 2]
print(consecutive_seq(nums))
