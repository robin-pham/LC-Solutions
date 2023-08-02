# L1203-Sort_Respecting_Dependencies.py

from collections import defaultdict


def sortItems(n: int, m: int, group, beforeItems):
    def check_ungrouped():
        ungrouped_queue = []
        for item in grouping[m]:
            if in_degrees[item] == 0:
                ungrouped_queue.append(item)
                in_degrees[item] -= 1
                for following in adj_list[item]:
                    in_degrees[following] -= 1
        return ungrouped_queue

    def check_group(item_group):
        group_queue, queue = [], []
        local_degrees = {item: in_degrees[item] for item in item_group}
        for item in item_group:
            if local_degrees[item] == 0:
                queue.append(item)
                group_queue.append(item)
        while queue:
            new_queue = []
            for item in queue:
                for following in adj_list[item]:
                    if following in local_degrees:
                        local_degrees[following] -= 1
                        if local_degrees[following] == 0:
                            new_queue.append(following)
                            group_queue.append(following)
            queue = new_queue
        if set(group_queue) == item_group:
            for item in group_queue:
                in_degrees[item] -= 1
                for following in adj_list[item]:
                    in_degrees[following] -= 1
            return group_queue
        else:
            return []

    adj_list, in_degrees = defaultdict(list), defaultdict(int)
    queue = []
    grouping = [set() for _ in range(m + 1)]
    for item in range(n):
        grouping[group[item]].add(item)
        for prev in beforeItems[item]:
            adj_list[prev].append(item)
            in_degrees[item] += 1

    queue += check_ungrouped()
    for groups in grouping:
        queue += check_group(groups)
        queue += check_ungrouped()
    sorted_items = list(queue)

    while queue:
        new_queue = []
        for item in queue:
            for following in adj_list[item]:
                if in_degrees[following] > -1:
                    if group[following] == m:
                        new_queue += check_ungrouped()
                    else:
                        new_queue += check_group(grouping[group[following]])
        queue = new_queue
        sorted_items += new_queue
    return sorted_items


sortItems(4, 1, [-1, 0, 0, -1], [[], [0], [1, 3], [2]])
