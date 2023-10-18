# L787 - Cheapest Flights within K Stops
"""
given n, flights, src, dst, and k
n is the number of cities that are connected flights
flights is array of [from, to, price]
src, dst, k - return cheapest price from src to dst with at most k stops - if cannot, return -1

1<= n <= 100
there are not multiple flights between cities
0 <= k < n
src != dst

it's a graph of nodes and edges, i want to find the cheapest path so i want to use DFS to find all paths to dst, and update cheapest path as i find them
make an adj_list of direct city connections - the adj_list will hold (connected_city, price)
from src, call function passing city, current_price, stops - for each connection, call function - if city == dst, update cheapest_path - if stops == k, return
function will not return anything, as we are just updating nonlocal cheapest_path

might have to have memo too.... - dfs with memo resulted in time limit exceeded, heap with no memo has memory exceeded
memo WITH heap, sorting for cheapest flight cost
bfs can be done with priority queue instead of regular queue

"""

import heapq


def cheapest_price(n, flights, src, dst, k):
    cheapest_path = float("inf")
    city_connections = {city: [] for city in range(n)}
    for departure, arrival, cost in flights:
        city_connections[departure].append((arrival, cost))
    paths = [(0, src, 0)]
    memo = {}

    while paths:
        cost, city, stops = heapq.heappop(paths)
        if city in memo and memo[city][0] <= cost and memo[city][1] <= stops:
            continue
        else:
            memo[city] = (cost, stops)
        if city == dst:
            cheapest_path = min(cheapest_path, cost)
        if stops <= k:
            for next_city, price in city_connections[city]:
                heapq.heappush(paths, (cost + price, next_city, stops + 1))

    return cheapest_path if cheapest_path != float("inf") else -1


tests = [4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1]
print(cheapest_price(tests[0], tests[1], tests[2], tests[3], tests[4]))
