L328 - Odd_Even_LL.py


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = even_start = head.next
        while even and even.next:
            odd.next, even.next = even.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = even_start

        return head


# time O(N) - traverse LL once
# space O(1) - variables for pointers not dependent on length of LL
