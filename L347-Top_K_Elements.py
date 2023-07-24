# L347-Top-K-Freq-Elements
class MinHeap:
    def __init__(self):
        self.heap = []
        self.heapsize = 0

    def peek(self):
        return self.heap[0][1]

    def size(self):
        return self.heapsize

    def insert(self, freq, element):
        self.heap.append((freq, element))
        value_idx = self.heapsize
        self.heapsize += 1
        while value_idx > 0:
            parent_idx = (value_idx - 1) // 2
            if self.heap[value_idx][0] < self.heap[parent_idx][0]:
                self.heap[parent_idx], self.heap[value_idx] = (
                    self.heap[value_idx],
                    self.heap[parent_idx],
                )
            else:
                break
            value_idx = parent_idx

    def shuffle_down(self):
        value_idx = 0
        while value_idx * 2 + 1 < self.heapsize:
            left_child = value_idx * 2 + 1
            right_child = value_idx * 2 + 2
            min_child = (
                right_child
                if right_child < self.heapsize
                and self.heap[right_child][0] < self.heap[left_child][0]
                else left_child
            )
            if self.heap[value_idx][0] > self.heap[min_child][0]:
                self.heap[value_idx], self.heap[min_child] = (
                    self.heap[min_child],
                    self.heap[value_idx],
                )
            else:
                break
            value_idx = min_child

    def delete_and_return_min(self):
        self.heap[0], self.heap[self.heapsize - 1] = (
            self.heap[self.heapsize - 1],
            self.heap[0],
        )
        min = self.heap.pop()
        self.heapsize -= 1
        self.shuffle_down()
        return min

    def replace_min(self, freq, element):
        self.heap.append((freq, element))
        self.heap[0], self.heap[self.heapsize] = self.heap[self.heapsize], self.heap[0]
        self.heap.pop()
        self.shuffle_down()


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for element in nums:
            freq_dict[element] = freq_dict.get(element, 0) + 1

        min_heap = MinHeap()
        for element, freq in freq_dict.items():
            min_heap.insert(-freq, element)

        results = [min_heap.delete_and_return_min()[1] for _ in range(k)]
        return results
