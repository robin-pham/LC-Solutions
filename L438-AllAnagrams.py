# 438 - Find All Anagrams in a String

# anagrams require seeing freq of letters in a string, so use dict with freq
# a static dict for p, then one for the sliding window of char with length of p for s
# add and remove letters
from collections import defaultdict


def find_anagrams(s, p):
    if len(s) < len(p):
        return []
    window = len(p)
    p_dict = defaultdict(int)
    s_dict = defaultdict(int)
    for ch in p:
        p_dict[ch] += 1

    for idx in range(window):
        s_dict[s[idx]] += 1

    anagram_indices = [0] if p_dict == s_dict else []
    for idx, ch in enumerate(s[window:], 1):
        print(idx, ch, s_dict)
        print(anagram_indices)
        s_dict[ch] += 1
        if s_dict[s[idx - 1]] == 1:
            del s_dict[s[idx - 1]]
        else:
            s_dict[s[idx - 1]] -= 1
        if p_dict == s_dict:
            anagram_indices.append(idx)
    return anagram_indices


s = "abab"
p = "ab"
print(find_anagrams(s, p))
