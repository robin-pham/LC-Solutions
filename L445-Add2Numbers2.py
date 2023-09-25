# 445 -Add two numbers 2

# the nodes are pointing forwards, and we are to add two linked lists - our output will also be going forward in the digis
# - numbers have no leading zeroes - do this without reversing the inputs

# i think go through the LLs to find the difference in number of diigts, add leading zeroes to the one with fewer digits
# no think does work great


# stack of LL node values? then pop them out to make sum nodes?
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def add_numbers(l1, l2):
    l1_stack, l2_stack = [], []
    while l1:
        l1_stack.append(l1.val)
        l1 = l1.next
    while l2:
        l2_stack.append(l2.val)
        l2 = l2.next

    carryover = 0
    after = None
    while l1_stack or l2_stack or carryover != 0:
        print(l1_stack, l2_stack)
        if l1_stack:
            carryover += l1_stack.pop()
        if l2_stack:
            carryover += l2_stack.pop()
        node = ListNode(carryover % 10)
        carryover //= 10
        node.next = after
        after = node

    return after


a = ListNode(7)
b = ListNode(2)
c = ListNode(4)
d = ListNode(3)
a.next = b
b.next = c
c.next = d

e = ListNode(5)
f = ListNode(6)
g = ListNode(2)
e.next = f
f.next = g

x = add_numbers(a, e)
while x:
    print(x.val)
    x = x.next
