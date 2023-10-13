# 24 - Swap Nodes in Pairs

"""
swap nodes in pairs


first pair of nodes
prev, curr -> None, head (1)

after = curr.next (2)
curr.next = after.next (3)
after.next = curr (1)
prev, curr = curr, curr.next (1) (3)


mid pairs of nodes
prev, curr = (1), (3)
after = curr.next (4)
prev.next = after (4)
curr.next = after.next (5)
after.next = curr (3)
prev, curr = curr, curr.next (3) (5)


last pair of nodes
prev, curr = (1), (3)
after = curr.next (4)
prev.next = after (4)
curr.next = after.next (None)
after.next = curr (3)
prev, curr = curr, curr.next (3) (None)


odd number of nodes
prev, curr = (1), (3)
after = curr.next (None)


while curr.next:

"""


def swap_node_pairs(head):
    if not head or not head.next:
        return head

    prev, curr = None, head
    new_head = curr.next
    while curr and curr.next:
        after = curr.next
        if prev:
            prev.next = after
        curr.next = after.next
        after.next = curr
        prev, curr = curr, curr.next

    return new_head


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


LL = [1, 2, 3, 4, 5, 6, 7]
head = node = ListNode(LL[0])
for idx in range(1, len(LL)):
    after = ListNode(LL[idx])
    node.next = after
    node = after

x = swap_node_pairs(head)
while x:
    print(x.val)
    x = x.next
