# L295-Find_Median_from_Stream


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def peek(self):
        return self.heap[0]

    def sized(self):
        return self.size

    def insert(self, value):
        self.heap.append(value)
        idx = self.size
        self.size += 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx], self.heap[parent_idx] = (
                    self.heap[parent_idx],
                    self.heap[idx],
                )
                idx = parent_idx
            else:
                break

    def pop_min(self):
        self.heap[-1], self.heap[0] = self.heap[0], self.heap[-1]
        popped = self.heap.pop()
        self.size -= 1
        idx = 0
        while idx * 2 + 1 < self.size:
            left_child = idx * 2 + 1
            right_child = idx * 2 + 2
            min_child = (
                right_child
                if idx * 2 + 2 < self.size
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
        return popped


class MedianFinder:
    def __init__(self):
        self.lower_heap = MinHeap()
        self.higher_heap = MinHeap()

    def addNum(self, num: int) -> None:
        if (
            self.lower_heap.sized() == 0 and self.higher_heap.sized() == 0
        ) or num <= -self.lower_heap.peek():
            self.lower_heap.insert(-num)
            if self.lower_heap.sized() > self.higher_heap.sized() + 1:
                self.higher_heap.insert(-self.lower_heap.pop_min())
        else:
            self.higher_heap.insert(num)
            if self.higher_heap.sized() > self.lower_heap.sized() + 1:
                self.lower_heap.insert(-self.higher_heap.pop_min())

    def findMedian(self) -> float:
        if self.lower_heap.sized() > self.higher_heap.sized():
            return -self.lower_heap.peek()
        elif self.higher_heap.sized() > self.lower_heap.sized():
            return self.higher_heap.peek()
        else:
            return (-self.lower_heap.peek() + self.higher_heap.peek()) / 2
