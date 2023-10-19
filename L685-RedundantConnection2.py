from collections import defaultdict


class DSU:
    def __init__(self):
        self.parents = {}
        self.direct_parent = defaultdict(list)
        self.ranks = {}

    def find(self, node):
        if node not in self.parents:
            self.parents[node] = node
            return node
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def multiple_parent(self):
        for happy_node, parents in self.direct_parent.items():
            if len(parents) == 2:
                parent_a, parent_b = parents
                print("found two parents for node", happy_node, parent_a, parent_b)
                # check which one is in a cycle vs outside
                queue = [(parent_a, parent_a), (parent_b, parent_b)]
                print(self.direct_parent)
                while len(queue) == 2:
                    print(queue)
                    new_queue = []
                    for node, parent in queue:
                        if self.direct_parent[node]:
                            new_queue.append((self.direct_parent[node][0], parent))
                    queue = new_queue
                print(queue)
                return [queue[0][1], happy_node]
        return

    def get_rank(self, node):
        if node not in self.ranks:
            self.ranks[node] = 0
        return self.ranks[node]

    def union(self, node_a, node_b):
        self.direct_parent[node_b].append(node_a)
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)
        if parent_a != parent_b:
            rank_a = self.get_rank(parent_a)
            rank_b = self.get_rank(parent_b)
            if rank_a > rank_b:
                self.parents[parent_b] = parent_a
            else:
                self.parents[parent_a] = parent_b
                if rank_a == rank_b:
                    self.ranks[parent_b] += 1
            return

    """
    there is a cycle where there is a node with 2 parents or not - if not, just return latest cycling edge 
    if cycle - the parent,child edge that is in the cycle - how do we find that? 
    
    have regular DSU and an extra direct parent parameter - if directparent parameter already set, find hte cycle

    """


def redundant_connection(edges):
    tree = DSU()
    for parent, child in edges:
        if tree.find(parent) == tree.find(child):
            r_connection = [parent, child]
        tree.union(parent, child)

    parent_check = tree.multiple_parent()
    if parent_check:
        return parent_check
    else:
        return r_connection


"""
[[5,2],[5,1],[3,1],[3,4],[3,5]]

    5    <-   3 
2       1       4

"""

print(redundant_connection([[5, 2], [5, 1], [3, 1], [3, 4], [3, 5]]))
