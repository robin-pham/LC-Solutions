L684 - Redundant_Connection


class DSU:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def find(self, node):
        if node not in self.parents:
            self.parents[node] = node
            return
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def get_rank(self, node):
        if node not in self.ranks:
            self.ranks[node] = 0
        return self.ranks[node]

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


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        tree = DSU()
        for edge in edges:
            tree.find(edge[0])
            tree.find(edge[1])
            if tree.find(edge[0]) == tree.find(edge[1]):
                return edge
            else:
                tree.union(edge[0], edge[1])


# time O((m+n)a(m,n)) m is number of nodes, n is number of edges, a is INVERSE ACKERMANN FUNCTION
# space O(m)
