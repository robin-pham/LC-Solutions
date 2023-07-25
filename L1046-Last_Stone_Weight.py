# L1046 - Last_Stone_Weight


class MinHeap:
    def __init__(self):
        self.heap = []
        self.heapsize = 0

    def size(self):
        return self.heapsize

    def insert(self, value):
        self.heap.append(value)
        idx = self.heapsize
        self.heapsize += 1
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
        self.heap[0], self.heap[self.heapsize - 1] = (
            self.heap[self.heapsize - 1],
            self.heap[0],
        )
        min_value = self.heap.pop()
        idx = 0
        self.heapsize -= 1
        while idx * 2 + 1 < self.heapsize:
            left_child = idx * 2 + 1
            right_child = idx * 2 + 2
            min_child = (
                right_child
                if right_child < self.heapsize
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
        return min_value


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = MinHeap()
        for stone in stones:
            stone_heap.insert(-stone)
        while stone_heap.size() > 1:
            x = -stone_heap.pop_min()
            y = -stone_heap.pop_min()
            print(x, y)
            if x != y:
                stone_heap.insert(y - x)
                print(stone_heap.heap)
        return -stone_heap.heap[0] if stone_heap.size() else 0
