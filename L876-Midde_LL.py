L876 - Midde_LL.py


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use 2 pointers - fast point moves at double hte speed of the first one - when it reaches the end, the first pointer will reach the middle point

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# time O(N) space O(1)
