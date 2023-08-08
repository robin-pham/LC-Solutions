L274 - H_index


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
            parent = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def pop_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped = self.heap.pop()
        self.size -= 1
        idx = 0
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
        return popped


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = MinHeap()
        for citation in citations:
            papers.insert(citation)
        h_idx = 0
        while papers.sized() > 0:
            if papers.peek() <= papers.sized():
                h_idx = papers.pop_min()
            else:
                if papers.sized() > h_idx and papers.peek() > h_idx:
                    h_idx = papers.sized()
                break
        return h_idx
