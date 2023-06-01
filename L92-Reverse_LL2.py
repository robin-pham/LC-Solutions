L92 - Reverse_LL2.py


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head.next or left == right:
            return head
        node = head
        for idx in range(1, right):
            if idx + 1 == left:
                pre_L = node
            elif idx == left:
                point_L = node
            node = node.next
        point_R = node
        if left > 1:
            pre_L.next = point_R
        else:
            head = point_R

        first, second = point_L, point_L.next
        point_L.next = point_R.next if point_R.next else None

        while first != point_R:
            third = second.next
            second.next = first
            first, second = second, third
        return head


# time O(N) space O(1)
