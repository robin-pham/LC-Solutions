L143 - Reorder_List.py


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # first find mid point of LL
        fast = slow = first_half = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)

        # reverse second half
        mid = slow

        prev, current = None, slow
        while current:
            temp = current.next
            current.next = prev
            prev, current = current, temp

        # reorder nodes
        second_half = prev
        while second_half.next:
            first_temp, second_temp = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = first_temp
            first_half, second_half = first_temp, second_temp


# time O(N) - traversed list 3 times
# space O(1)
