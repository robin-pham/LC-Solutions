# 725 - Split Linked List in Parts

"""
input head of LL and int k - split LL into k consecutive LL parts
length of each part should be as equal as possible, size differ <= 1
parts should be in order of occurence, parts earlier should have size greater or equal to parts later

ex. [1,2,3] -> [1], [2], [3], [], []
return array of k parts -> these should be LL nodes parts, not values
num of nodes in head is [0, 1000]
1 <= k <= 50

3 LL where k = 5 -> 1,1,1,0,0
9 LL where k = 3 -> 3,3,3
8 LL where k = 3 -> 3,3,2

so it's LL//k + 1 while remainder > 0, else LL/k
remainder goes down with each LL part that is split


so i first want to find the number of nodes in the LL
then part_size = LL-size / k rounded up?
then have parts array, add head to it, wehn traversed part_size nodes, have next = null, and add next node to array

"""


def split_list(head, k):
    LL_parts = [None] * k
    if not head:
        return LL_parts

    node = head.next
    count = 1
    while node:
        node = node.next
        count += 1

    part_size, remainder = count // k + 1, count % k
    prev, current = None, head
    LL_parts[0] = head
    print(part_size, remainder)
    for idx in range(1, k):
        node_count = part_size if remainder > 0 else part_size - 1
        while node_count > 0:
            prev, current = current, current.next
            node_count -= 1
        LL_parts[idx] = current
        if prev:
            prev.next = None
        remainder -= 1
    print(LL_parts)
    return LL_parts


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next, b.next, c.next, d.next, e.next = b, c, d, e, f
x = split_list(a, 2)
print(x)
for i in x:
    if i is not None:
        print(i.val)
