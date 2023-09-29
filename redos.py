# redundant connections
# 12:19


class DSU:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def find(self, node):
        if node not in self.parents:
            self.parents[node] = node
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
        rank_a = self.get_rank(node_a)
        rank_b = self.get_rank(node_b)
        if rank_a > rank_b:
            self.parents[parent_b] = parent_a
        else:
            self.parents[parent_a] = parent_b
            if rank_a == rank_b:
                rank_b += 1


def find_redundant(edges):
    graph = DSU()
    for point_a, point_b in edges:
        if graph.find(point_a) == graph.find(point_b):
            return [point_a, point_b]
        else:
            graph.union(point_a, point_b)


edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(find_redundant(edges))
