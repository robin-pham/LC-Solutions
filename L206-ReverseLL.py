# 206 - reverse linked list

# 11:05


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def reverse_LL(head):
    prev, current = None, head
    while current:
        after = current.next
        current.next = prev
        prev = current
        current = after
    return prev


a = [0, 1, 3, 6]
prev = head = ListNode(0)
for val in a:
    current = ListNode(val)
    prev.next = current
    prev = prev.next

x = reverse_LL(head.next)
while x:
    print(x.val)
    x = x.next
