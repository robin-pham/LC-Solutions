# 841 - Keys and Rooms

"""
give an array of rooms - you can only open rooms[0] to begin with
in the room is a list of distinct keys - each key has a number of the room it unlocks
return True if you can visit every room, false if not

2 <= rooms.length <= 1000
1 <= num of keys <= 3000
0 <= rooms[i][j] < n

so keys can be repeated but not within the same room

strat - create dictionary of rooms with keys they contain (adj_list)
-in degrees of all rooms except 0 is 1
-queue of keys in room 1
-keep track of number of rooms opened
-BFS

"""


def open_rooms(rooms):
    locked_rooms = set([idx for idx in range(1, len(rooms))])
    queue = rooms[0]
    while queue:
        print(queue)
        new_queue = []
        for key in queue:
            if key in locked_rooms:
                locked_rooms.remove(key)
                new_queue += [
                    new_key for new_key in rooms[key] if new_key in locked_rooms
                ]
        queue = new_queue
    print(locked_rooms)
    return True if not locked_rooms else False


tests = [[[1], [2], [3], []], [[1, 3], [3, 0, 1], [2], [0]]]
for idx, rooms in enumerate(tests):
    print(idx, open_rooms(rooms))
