# 141 - Linked List Cycle

"""
get head of linked list, determine if it has cycle
return true if cycle, otherwise false
number of nodes is [0, 10**4]

"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle(head):
    if not head or not head.next:
        return False

    slow, fast = head, head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


a = ListNode(1)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

a.next = b
b.next = c
c.next = d
print(detect_cycle(a))
