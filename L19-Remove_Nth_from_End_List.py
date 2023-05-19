L19 - Remove_Nth_from_End_List.py


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        node = head
        while node.next:
            node = node.next
            length += 1

        if length == 1:
            return
        elif length == n:
            head = head.next
            return head

        node = head
        for i in range(0, length - n - 1):
            node = node.next
        node.next = node.next.next if n > 1 else None
        return head

    # time O(n) - traverse list twice
    #  space O(1) - intialize a pointer and an int
