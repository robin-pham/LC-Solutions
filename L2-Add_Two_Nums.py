# L2 - Add_Two_Nums.py


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def addTwoNumbers(l1, l2):
    head = current = ListNode(0)
    carryover = 0

    while l1 or l2 or carryover:
        if l1:
            carryover += l1.val
            l1 = l1.next
        if l2:
            carryover += l2.val
            l2 = l2.next
        current.next = ListNode(carryover % 10)
        carryover = carryover // 10
        current = current.next

    return head.next


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(9)

b = ListNode(5)
b.next = ListNode(8)
b.next.next = ListNode(2)

x = addTwoNumbers(a, b)
while x:
    print(x.val)
    x = x.next
