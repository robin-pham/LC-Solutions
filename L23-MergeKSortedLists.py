# 23 - Merge K Sorted Lists


"""
given array of k linked-lists, sorted in ascending order, merge all into one and return it
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

m = ListNode(100)
n = ListNode(200)
o = ListNode(600)
p = ListNode(601)
m.next, n.next, o.next = n, o, p

v = ListNode(2)
w = ListNode(4)
x = ListNode(105)
y = ListNode(220)
z = ListNode(221)
v.next, w.next, x.next, y.next = w, x, y, z


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


ok = merge_lists([a, m, v])
while ok:
    print(ok.val)
    ok = ok.next
