#  83 - Remove Duplicates from Sorted List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    node = head
    # if not node or not node.next:     THIS PART ISNT NECESSARY
    #     return node
    while node: 
        while node.next and node.next.val == node.val:
            node.next = node.next.next
        node = node.next
    return head


a = ListNode(1)
b = ListNode(1)
c = ListNode(1)
d = ListNode(1)
a.next = b
b.next = c
c.next = d

result = remove_duplicates([])
while result:
    print(result.val)
    result = result.next
