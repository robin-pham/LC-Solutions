# 350 - Intersection of Two Arrays 2


"""
two int arrays nums1 and nums2 - return array of intersection (elements in both) - can be any order
-not ordered
- 1 <= len(nums1 or 2) <= 1000  so not empty
- 0 <= x <= 1000 in nums1 or 2

O(N) time and space solution - put elements in one array into frequency counting dictionary, go thorugh other array and see if element in array, update freq

"""
from collections import defaultdict


def array_intersection(nums1, nums2):
    nums1_freq_dict = defaultdict(int)
    intersection_array = []

    for num in nums1:
        nums1_freq_dict[num] += 1

    for num in nums2:
        if nums1_freq_dict[num] > 0:
            intersection_array.append(num)
            nums1_freq_dict[num] -= 1

    return intersection_array


test_cases = [[[1, 2, 2, 1], [2, 2]], [[4, 9, 5], [9, 4, 9, 8, 4]]]

for test in test_cases:
    print(array_intersection(test[0], test[1]))


"""
followup qs
if sorted, then two pointers for num1 and num2 - iterate
- if equal, add to int_array and increment both pointers, otherwise increment pointer of smaller number
-return list when a pointer has reached end
-improve space complexity, O(1) extra space


"""
