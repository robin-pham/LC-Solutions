# 650 - 2 keys Keyboard

"""
there is an A on screen
can only copy all or paste
min number of operations to get to n number of As?

BFS or DFS? 
bfs allows us to terminate when we get to a min answer
"""


# dfs way too slow
def two_keys_dfs(n):
    min_operations = n

    def dfs(current, copied, operations):
        nonlocal min_operations
        if operations > min_operations or operations >= n:
            return
        if current == n:
            min_operations = min(min_operations, operations)
            return
        dfs(current + copied, copied, operations + 1)
        if current != copied:
            dfs(current, current, operations + 1)

    dfs(1, 1, 0)
    return min_operations


# pretty slow
def two_keys_bfs(n):
    if n == 1:
        return 0
    queue = [(1, 1)]
    operations = 1
    while queue:
        new_queue = []
        for number, copied in queue:
            if number == n:
                return operations
            if number > n:
                continue
            new_queue.append((number + copied, copied))
            if number != copied:
                new_queue.append(((number, number)))
        queue = new_queue
        operations += 1


"""
1 0
2 2
3 3
4 4
5 5
6 5
7 7
8 6
9 6
10 7
11 11
12 7
13 13
14 9
15 8
16 8
17 17
18 8
19 19"""

# if prime number, then min = n
# otherwise it is factor's op + nubmer of that factor


def two_keys_dp(n):
    if n == 1:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            print(n, i)
            return two_keys_dp(n // i) + i


print(two_keys_dp(19))
