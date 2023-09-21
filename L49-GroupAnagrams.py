# 49 Group Anagrams


from collections import defaultdict
def group_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        # for ch in word:
        #     letters.append(ch)
        # letters.sort()
        letters = ''.join(sorted(word))     # damn this is nice
        anagram_dict[letters].append(word)
    return anagram_dict.values()

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(group_anagrams(words))
print(sorted('hello'))

    # dictionary with keys as set of letters in word, values are words
    # for each word, make a set of letters - add that to dictionary 
    # return values of dictionary