# 455 Assign Cookies


# 10:35

#  do we have to make sure the greediest children are fed first in all cases?
#  heap implementation 
#  have max heaps for cookies and children
#  returning number of fed children
#  if no cookie remaining or no child remaining, return fed
#  if max cookie size > max greed of child - pop both and increase fed
#  if max cookie size < max greed, pop child

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def heap_size(self):
        return self.size
    
    def insert(self, value):
        self.heap.append(value)
        idx = self.size
        self.size += 1
        while idx > 0:
            parent = (idx - 1)//2
            if self.heap[parent] > self.heap[idx]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                return

    def pop_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped_value = self.heap.pop()
        self.size -= 1
        idx = 0
        while idx * 2 + 1 < self.size:
            left_child = idx*2+1
            right_child = left_child + 1
            min_child = right_child if right_child < self.size and self.heap[right_child] < self.heap[left_child] else left_child
            if self.heap[min_child] < self.heap[idx]:
                self.heap[idx], self.heap[min_child] = self.heap[min_child], self.heap[idx]
                idx = min_child
            else:
                break
        return popped_value

    def peek_min(self):
        return self.heap[0]

def assign_cookies(greed, size):
    kids_fed = 0
    child_heap = MinHeap()
    cookie_heap = MinHeap()
    for kid in greed:
        child_heap.insert(-kid)
    for cookie in size:
        cookie_heap.insert(-cookie)
    while cookie_heap.heap_size() > 0 and child_heap.heap_size() > 0:
        if -cookie_heap.peek_min() < -child_heap.peek_min():
            child_heap.pop_min()
        else:
            cookie_heap.pop_min()
            child_heap.pop_min()
            kids_fed += 1
    
    return kids_fed

g = [1,2,3]
s = [1,1,2]

print(assign_cookies(g,s))