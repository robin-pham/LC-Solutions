L2 - Add_Two_Nums.py


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = current = ListNode()
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


# time O(N) space O(N)
