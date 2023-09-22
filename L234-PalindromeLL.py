# 234 - Palindrome Linked List

#  N time and 1 space
#  node_count
#  reverse the LL until the middle of LL
#  check if characters are the same

# 11:15

class LLNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def pal_linked_list(head):
    count = 0
    node = head
    while node:
        node = node.next
        count += 1

    # if we have 4 nodes, reverse until 2
    # if we have 5 nodes, reverse until 2

    # how to reverse LL
    # have prev, current, and next
    # current.next = prev
    # prev, current, next = current, next, next.next
    print(count)
    prev, current, after = None, head, head.next
    for _ in range(count // 2):
        print('start', prev, current.val, after.val)
        current.next = prev
        prev = current
        current = after
        after = current.next
        print('end', prev.val, current.val, after.val)
    if count % 2 == 0:
        left, right = prev, current
    else:
        left = prev
        right = after if after else current
    while left and right:
        print(left.val, right.val)
        if left.val == right.val:
            left = left.next
            right = right.next
        else:
            return False
    return True
    
a = LLNode(1)
b = LLNode(2)
c = LLNode(3)
d = LLNode(2)
e = LLNode(1)
a.next = b
b.next = c
c.next = d
d.next = e

print(pal_linked_list(a))