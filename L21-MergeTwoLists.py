# L21 - Merge Two SOrted Lists

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def merge_lists(list1, list2):
    if not list1 or not list2:
        return list1 or list2
    head = node = ListNode(0)
    while list1 or list2:
        if (list1 and list2 and list1.val <= list2.val) or not list2:
            node.next = list1
            list1 = list1.next
        elif (list1 and list2 and list2.val < list1.val) or not list1:
            node.next = list2
            list2 = list2.next
        node = node.next
    return head.next

a = ListNode(0)
b = ListNode(1)
c = ListNode(4)

d = ListNode(1)
e = ListNode(3)
f = ListNode(6)

a.next = b
b.next = c
d.next = e
e.next = f

x = merge_lists(a, d)
while x:
    print(x.val)
    x = x.next
