# 692 - Top K Frequent Words
# class MinHeap:
#     def __init__(self):
#         self.heap = []
#         self.size = 0

#     def insert(self, val):


#     def pop_min(self):


from collections import defaultdict


def top_words(words, k):
    word_freq_dict = defaultdict(int)
    for word in words:
        word_freq_dict[word] += 1
    return sorted(word_freq_dict, key=lambda x: (-word_freq_dict[x], x))[:k]


words = ["i", "love", "leetcode", "i", "love", "coding", "coding"]
print(top_words(words, 3))
