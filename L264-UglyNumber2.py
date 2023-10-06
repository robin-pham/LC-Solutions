# 264 - Ugly Number 2


"""
ugly number is a number with only prime factors in [2,3,5]
return the nth ugly number
1,2,3,4,5,8,9,10,12 - 12 is the 10th ugly number

i want to generate ugly numbers using a combo sum type approach - recursive products of 2,3,5
these products get put into a max_heap or stack?? 

when do we stop? 
if structure size is n, add to it if product is lower than max - pop the max - should be a stack
    if product is larger than max, return
"""


# this worked for up to n=463 on LC
class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

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

    def pop(self):
        self.heap[-1], self.heap[0] = self.heap[0], self.heap[-1]
        self.heap.pop()
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

    def peek(self):
        return self.heap[0]

    def sized(self):
        return self.size


def ugly_number1(n):
    product_set = set()
    ugly_heap = MinHeap()
    factors = [2, 3, 5]

    def product_sum(product):
        product_set.add(product)

        if ugly_heap.sized() == n:
            if product > -ugly_heap.peek():
                return
            else:
                ugly_heap.pop()
                ugly_heap.insert(-product)
        elif ugly_heap.sized() < n:
            ugly_heap.insert(-product)

        for num in factors:
            if product * num not in product_set:
                product_sum(product * num)

    product_sum(1)
    return -ugly_heap.peek()


"""
DP SOLUTION USING BUCKETS

"""


def ugly_number(n):
    n_buckets = [0] * n
    count_two = count_three = count_five = 0
    n_buckets[0] = 1

    for idx in range(1, n):
        n_buckets[idx] = min(
            n_buckets[count_two] * 2,
            n_buckets[count_three] * 3,
            n_buckets[count_five] * 5,
        )
        if n_buckets[idx] == n_buckets[count_two] * 2:
            count_two += 1
        if n_buckets[idx] == n_buckets[count_three] * 3:
            count_three += 1
        if n_buckets[idx] == n_buckets[count_five] * 5:
            count_five += 1
    return n_buckets[-1]


print(ugly_number(463))
