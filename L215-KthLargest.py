# 215 - Kth largest element in an array

# no sorting - heap


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        idx = self.size
        self.size += 1
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def pop_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped_value = self.heap.pop()
        idx = 0
        self.size -= 1
        while idx * 2 + 1 < self.size:
            left_child = idx * 2 + 1
            right_child = left_child + 1
            min_child = (
                right_child
                if right_child < self.size
                and self.heap[right_child] < self.heap[left_child]
                else left_child
            )
            if self.heap[idx] > self.heap[min_child]:
                self.heap[idx], self.heap[min_child] = (
                    self.heap[min_child],
                    self.heap[idx],
                )
                idx = min_child
            else:
                break
        return popped_value


def kth_largest(nums, k):
    heap = MinHeap()
    for num in nums:
        heap.insert(num)
        if heap.size > k:
            heap.pop_min()
    return heap.peek()


nums = [3, 2, 1, 5, 6, 4]
print(kth_largest(nums, 2))
