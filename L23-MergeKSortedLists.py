# 23 - Merge K Sorted Lists


"""
given array of k linked-lists, sorted in ascending order, merge all into one and return it
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, node):
        self.heap.append(node)
        idx = self.size
        self.size += 1
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx].val < self.heap[parent].val:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def heap_size(self):
        return self.size

    def pop_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped_node = self.heap.pop()
        self.size -= 1
        idx = 0
        while idx * 2 + 1 < self.size:
            left_child = idx * 2 + 1
            right_child = left_child + 1
            min_child = (
                right_child
                if right_child < self.size
                and self.heap[right_child].val < self.heap[left_child].val
                else left_child
            )
            if self.heap[idx].val > self.heap[min_child].val:
                self.heap[idx], self.heap[min_child] = (
                    self.heap[min_child],
                    self.heap[idx],
                )
                idx = min_child
            else:
                break
        return popped_node


def merge_lists(lists):
    node_heap = MinHeap()
    for node in lists:
        node_heap.insert(node)
    print(node_heap.heap_size())
    head = node = ListNode(0)
    while node_heap.heap_size() > 0:
        min_node = node_heap.pop_min()
        node.next = min_node
        if min_node.next:
            node_heap.insert(min_node.next)
        node = node.next
    return head.next


ok = merge_lists([first, second, third])
while ok:
    print(ok.val)
    ok = ok.next


def make_LL(arr):
    prev = None
    for num in arr:
        curr = ListNode(num)
        if not prev:
            head = curr
        else:
            prev.next = curr
        prev = curr
    return head


first = make_LL([1, 2, 3])
second = make_LL([100, 200, 600, 601])
third = make_LL([2, 4, 105, 220, 221])
