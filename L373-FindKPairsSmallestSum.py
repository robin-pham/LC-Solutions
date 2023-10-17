# 373 - Find K Pairs with Smallest Sums

"""
given nums1 and nums2 sortedi non-decreasing order and int k
make pairs [u, v] where u is from nums1 and v is from nums2
return k pairs of [u,v] with the smallest sums

00, 01 02 10 11 12 21 22

[1,2,3,4,5] and [0,0,1,1,2]
00 vs 00, tie
01 (0) vs 10 (2), 01
02 (1) vs 10 (2), 02
03 (1) vs 10 (2), 03
04 (3) vs 10 (2), 10
04 (3) vs 20 (3), 04
11 ()
04 (3) vs 30, 30
04 (3) vs 40, 
04 vs 12, 04 - 04 reached end, reset to 1
12
"""

import heapq


def smallest_pairs(nums1, nums2, k):
    visited = set((0, 0))
    k_smallest_pairs = []
    min_sum_heap = [(nums1[0] + nums2[0], 0, 0)]
    while len(k_smallest_pairs) < k:
        sum, idx1, idx2 = heapq.heappop(min_sum_heap)
        k_smallest_pairs.append([nums1[idx1], nums2[idx2]])
        if idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in visited:
            heapq.heappush(
                min_sum_heap, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2)
            )
            visited.add((idx1 + 1, idx2))
        if idx2 + 1 < len(nums2) and (idx1, idx2 + 1) not in visited:
            heapq.heappush(
                min_sum_heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1)
            )
            visited.add((idx1, idx2 + 1))
    return k_smallest_pairs


nums1 = [1, 2]
nums2 = [3]
print(smallest_pairs(nums1, nums2, 3))
#  00 01 10 20 02 11 21 12 22 30 31 32 40 41 42
