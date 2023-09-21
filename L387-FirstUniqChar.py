# 387 - First Unique Character in a String
from collections import defaultdict

def first_uniq_char(word):
    # put every letter in the word into a dictionary as key with value as frequency
    # enumerate through letters, if freq == 1, return idx, if entire word, then return -1
    char_freq_dict = defaultdict(int)
    for ch in word:
        char_freq_dict[ch] += 1
    for idx, ch in enumerate(word):
        if char_freq_dict[ch] == 1:
            print(ch)
            return idx
    return -1


test = 'loveleetcode'
print(first_uniq_char(test))



