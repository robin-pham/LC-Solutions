# L2 Add Two Numbers -5:07 - finish 5:16

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

l1 = ListNode(9)
l12 = ListNode(9)
l13 = ListNode(9)
l1.next = l12
l12.next = l13

l2 = ListNode(9)
l22 = ListNode(9)
l23 = ListNode(9)
l2.next = l22
l22.next = l23

def add_numbers(l1, l2):
    current_digit = 0
    head = node = ListNode(0)

    while l1 or l2 or (current_digit > 0):
        if l1:
            current_digit += l1.val
            l1 = l1.next
        if l2:
            current_digit += l2.val
            l2 = l2.next
        node.next = ListNode(current_digit % 10)
        current_digit //= 10
        node = node.next

    return head.next

sum = add_numbers(l1, l2)
while sum:
    print(sum.val)
    sum = sum.next