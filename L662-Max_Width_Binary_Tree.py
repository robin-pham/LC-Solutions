# L662 - Max_Width_Binary_Tree

"""
max width among all levels - width is length between end nodes that are non null - including null nodes in between
am i doing bfs, with tuples containing node and position? idx*2+1, idx*2+2 for left and right
then at each level, left most if first non null node idx, right most is last one, level width = diff
in the bfs, only pass tuples when the node is present
            0
        1       2
    3   4       5   6
7   8           11 12   13  14



"""


def max_width(root):
    max_width = 1
    queue = [(root, 0)]
    while queue:
        new_queue = []
        max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
        for node, idx in queue:
            if node.left:
                new_queue.append((node.left, idx * 2 + 1))
            if node.right:
                new_queue.append((node.right, idx * 2 + 2))
        queue = new_queue
    return max_width

    # max_width = 1
    # queue = [(root, 0)]
    # while queue:
    #     max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
    #     new_queue = []
    #     for node, idx in queue:
    #         if node.left:
    #             new_queue.append((node.left, 2 * idx + 1))
    #         if node.right:
    #             new_queue.append((node.right, 2 * idx + 2))
    #     queue = new_queue
    # return max_width
