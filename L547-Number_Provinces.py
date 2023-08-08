L547 - Number_Provinces


class DSU:
    def __init__(self):
        self.parents = {}
        self.rank = {}

    def find(self, node_id):
        if node_id not in self.parents:
            self.parents[node_id] = node_id
            return
        if self.parents[node_id] != node_id:
            self.parents[node_id] = self.find(self.parents[node_id])
        return self.parents[node_id]

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

    def get_rank(self, node_id):
        if node_id not in self.rank:
            self.rank[node_id] = 0
        return self.rank[node_id]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = DSU()
        for city in range(len(isConnected)):
            cities.find(city)
        for i, row in enumerate(isConnected):
            for j, connection in enumerate(row):
                if i != j and connection == 1:
                    cities.union(i, j)
        province = set()
        for city in range(len(isConnected)):
            province.add(cities.find(city))
        return len(province)


# time O((m+n)a(m,n)) m is number of cities, n is number of connections, a is INVERSE ACKERMANN FUNCTION
# space O(n)
