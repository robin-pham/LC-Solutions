# 310 - Minimum Height Trees

"""
tree is undirected graph with any 2 vertices connected by exactly one path - no cycles
this is the cat neighbour problem from robin - minimum height tree of an undirected path has a root with shortest path distance to all lonely cats (ends)


"""


def shortest_trees(n, edges):
    adj_list = {idx: [] for idx in range(n)}
    for node_a, node_b in edges:
        adj_list[node_a].append(node_b)
        adj_list[node_b].append(node_a)
    end_points = [node for node in adj_list if len(adj_list[node]) <= 1]
    while end_points:
        new_end_points = []
        for node in end_points:
            for connection in adj_list[node]:
                adj_list[connection].remove(node)
                if len(adj_list[connection]) == 1:
                    new_end_points.append(connection)
        if not new_end_points:
            break
        end_points = new_end_points
    return end_points


tests = [[4, [[1, 0], [1, 2], [1, 3]]], [6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]]]
for n, edges in tests:
    print(shortest_trees(n, edges))
